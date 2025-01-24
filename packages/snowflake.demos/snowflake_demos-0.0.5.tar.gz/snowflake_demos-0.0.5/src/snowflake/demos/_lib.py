from typing import Optional

from snowflake.demos._demo_connection import DemoConnection
from snowflake.demos._demo_handle import DemoHandle
from snowflake.demos._demos_loader import DemosLoader
from snowflake.demos._environment_detection import CONSOLE_MANGAER
from snowflake.demos._utils import print_demo_list, read_demo_mapping_with_cache


def help() -> None:
    """Print help message."""
    CONSOLE_MANGAER.safe_print("Welcome to Snowflake Demos!", color="cyan")
    CONSOLE_MANGAER.safe_print("Run the following in your REPL to get started\n", color="cyan")
    CONSOLE_MANGAER.safe_print("from snowflake.demos import load_demo", color="bold magenta")
    CONSOLE_MANGAER.safe_print("demo = load_demo('<demo-name>')\n", color="cyan")
    CONSOLE_MANGAER.safe_print("If your chosen demo has multiple steps, you can change steps using", color="cyan")
    CONSOLE_MANGAER.safe_print("demo.show_next() or demo.show(step=<number>)\n", color="cyan")
    CONSOLE_MANGAER.safe_print("If you want to destroy the Notebook(s) and its resources, run", color="cyan")
    CONSOLE_MANGAER.safe_print("demo.teardown()\n", color="cyan")
    print_demo_list()


def load_demo(demo_name: str, refresh_demo: bool = False) -> Optional[DemoHandle]:
    """Load the demo with the given name.

    Parameters
    __________
      demo_name: The name of the demo to load.
      refresh_demo: Whether to refresh the demos from snowflake demo repository.

    Returns
    _______
      The demo handle which can be used perform certain actions on demo.
    """
    demo_mapping = read_demo_mapping_with_cache()
    if demo_name not in demo_mapping.keys():
        CONSOLE_MANGAER.safe_print(f"[red]Demo[/red] [green]'{demo_name}'[/green] [red]not found.[/red]", color="red")
        CONSOLE_MANGAER.safe_print("Please call help() to see the list of available demos.", color="red")
        return None
    return DemosLoader().get_demo_handle(demo_name)


def teardown() -> None:
    """Teardown all the demo."""
    demo_connection = DemoConnection()
    demo_connection.teardown()
    DemosLoader().invalidate_all_demos()
