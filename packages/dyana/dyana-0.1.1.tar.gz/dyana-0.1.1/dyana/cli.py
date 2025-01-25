import pathlib
import platform as platform_pkg

# NOTE: json is too slow
import cysimdjson
import typer
from rich import box, print
from rich.table import Table

import dyana.loaders as loaders_pkg
from dyana.loaders.loader import Loader
from dyana.tracer.tracee import Tracer
from dyana.view import (
    view_disk_events,
    view_disk_usage,
    view_extra,
    view_gpus,
    view_header,
    view_network_events,
    view_process_executions,
    view_ram,
    view_security_events,
)

cli = typer.Typer(
    no_args_is_help=True,
    context_settings={"help_option_names": ["-h", "--help"]},
    help="Blackbox profiler.",
)


@cli.command(
    help="Show the available loaders.",
)
def loaders(
    build: bool = typer.Option(help="Build the loaders containers if needed.", default=False),
) -> None:
    loaders_path = loaders_pkg.__path__[0]
    loaders: list[Loader] = []
    for entry in pathlib.Path(loaders_path).iterdir():
        if entry.is_dir() and not entry.name.startswith("__") and entry.name != "base":
            loaders.append(Loader(name=entry.name, build=build, timeout=10))

    table = Table(box=box.ROUNDED)
    table.add_column("Name", style="cyan")
    table.add_column("Description")

    for loader in sorted(loaders, key=lambda x: x.name):
        table.add_row(loader.name, loader.settings.description if loader.settings else "")

    print(table)


@cli.command(
    help="Profiles the target file via the selected loader.",
    # we need to allow extra arguments because the loader might have its own arguments
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)
def trace(
    ctx: typer.Context,
    loader: str = typer.Option(help="Loader to use.", default="automodel"),
    platform: str | None = typer.Option(help="Platform to use.", default=None),
    output: pathlib.Path = typer.Option(help="Path to the output file.", default="trace.json"),
    policy: pathlib.Path | None = typer.Option(
        help="Path to a policy or directory with custom tracee policies.", default=None
    ),
    timeout: int = typer.Option(help="Execution timeout in seconds.", default=60),
    no_gpu: bool = typer.Option(help="Do not use GPUs.", default=False),
    allow_network: bool = typer.Option(help="Allow network access to the model container.", default=False),
    allow_volume_write: bool = typer.Option(help="Mount volumes as read-write.", default=False),
    verbose: bool = typer.Option(help="Verbose mode.", default=False),
) -> None:
    try:
        # disable GPU on non-Linux systems
        if not no_gpu and platform_pkg.system() != "Linux":
            no_gpu = True

        # check if policy is either a file or a directory
        if policy and not policy.exists():
            raise typer.BadParameter(f"policy file or directory not found: {policy}")

        the_loader = Loader(name=loader, timeout=timeout, platform=platform, args=ctx.args, verbose=verbose)
        the_tracer = Tracer(the_loader, policy=policy)

        trace = the_tracer.run_trace(allow_network, not no_gpu, allow_volume_write)

        print(f":card_file_box:  saving {len(trace.events)} events to {output}\n")

        with open(output, "w") as f:
            f.write(trace.model_dump_json())

        summary(output)
    except Exception as e:
        print(f":cross_mark: [bold][red]error:[/] [red]{e}[/]")
        if verbose:
            raise


@cli.command(help="Show a summary of the trace.")
def summary(trace_path: pathlib.Path = typer.Option(help="Path to the trace file.", default="trace.json")) -> None:
    with open(trace_path) as f:
        raw = f.read()
        # the standard json parser is too slow for this
        parser = cysimdjson.JSONParser()
        trace = parser.loads(raw)

    view_header(trace)
    view_ram(trace["run"])
    view_gpus(trace["run"])
    view_disk_usage(trace["run"])

    view_process_executions(trace)
    view_network_events(trace)
    view_disk_events(trace)
    view_security_events(trace)
    view_extra(trace["run"])
