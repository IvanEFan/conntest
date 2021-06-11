import click
from rich.console import Console
from rich.status import Status
from ping3 import ping

from conntest.config import Config

hostnames = [
    'www.baidu.com',
    'www.google.com',
    'www.bilibili.com',
    'www.github.com'
]

console = Console()
conf = Config()

@click.group(invoke_without_command=True)
@click.pass_context
@click.option(
    '--accurate',
    is_flag=True
)
def cli(ctx, accurate):
    if ctx.invoked_subcommand is None:
        for hostname in conf.data:
            with Status(f'[bright_red]Pinging {hostname}...'):
                resp = ping(hostname, unit='ms')
            if resp is None:
                console.print(f':disappointed_face: [red]Can not reach {hostname}')
            else:
                console.print(f':slightly_smiling_face: [green]Delay to {hostname}: [/green][bright_red]{int(resp)} ms')

def show_hostnames():
    console.print('[bright_red bold]Hostnames:')
    [console.print('[red]' + hostname) for hostname in conf.data]

@cli.group(invoke_without_command=True)
@click.pass_context
def config(ctx):
    if ctx.invoked_subcommand is None:
        # Show config
        show_hostnames()

@config.command()
@click.argument('url')
def add(url):
    if conf.add(url):
        console.print(f'[green]Added {url} to the hostname list!')
        show_hostnames()
    else:
        console.print(f'[red]{url} is already in the hostname list!')

@config.command()
@click.argument('url')
def remove(url):
    if conf.remove(url):
        console.print(f'[green]Removed {url} to the hostname list!')
        show_hostnames()
    else:
        console.print(f'[red]{url} is not in the hostname list!')

@config.command()
def clear():
    conf.clear()
    console.print('[green]Hostname list cleared!')
    show_hostnames()

if __name__ == '__main__':
    cli()