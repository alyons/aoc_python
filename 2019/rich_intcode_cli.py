from AoCUtils.rich import make_default_layout

from rich.console import Console
from rich.live import Live
from rich.prompt import Prompt

console = Console()
layout = make_default_layout()

def parse_command(command: str):
    match command.split():
        case ['exit' | 'quit']:
            return False
        case unknown_command:
            print(f'Unknown Command: {unknown_command}')
        
    return True


def main():
    with Live(layout, screen=True, console=console) as live:
        running = True
        while running:
            command = live.console.input('Input Command: ')
            running = parse_command(command)


if __name__ == '__main__':
    main()