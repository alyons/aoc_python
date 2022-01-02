from datetime import datetime

from rich import box
from rich import progress
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.style import Style
from rich.syntax import Syntax
from rich.table import Column, Table
from rich.text import Text


class Header:
    """Display header with clock."""
    def __init__(self, description: str, year: int, day: int):
        self.description = description
        self.title = 'Advent of Code' + f': {year}' if year else ''
        self.subtitle = f'Day {day}' if day else ''

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            self.description,
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(
            grid,
            title=self.title,
            subtitle=self.subtitle
        )


def make_default_layout() -> Layout:
    layout = Layout()

    layout.split(
        Layout(name='header', size=3),
        Layout(name='main', ratio=1),
        Layout(name='footer', size=3)
    )

    layout['main'].split_row(
        Layout(name='data_vis', ratio=3),
        Layout(name='debug', ratio=2)
    )

    layout['debug'].split(
        Layout(name='variables'),
        Layout(name='log')
    )

    return layout


def make_job_progress() -> Progress:
    job_progress = Progress(
        '{task.description}',
        SpinnerColumn(),
        BarColumn(),
        TextColumn('[progress.percentage]{task.percentage:>3.0f}%')
    )
    return job_progress


def make_progress_table(job_progress: Progress) -> Table:
    progress_table = Table.grid(expand=True)
    progress_table.add_row(
        Panel(job_progress, title="[b]Jobs", border_style="Green")
    )

    return progress_table
