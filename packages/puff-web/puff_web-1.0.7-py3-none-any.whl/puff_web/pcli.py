import click
import os
import sys

@click.group()
def cli() -> None:
    """Main command group for the application."""
    pass

@cli.command()
@click.option('-H', '--host', default='localhost', help='Server host name (default is "localhost").')
@click.option('-p', '--port', default=8000, help='Server port (default is 8000).')
def runserver(host: str, port: int) -> None:
    """Run the server.

    This command starts the server using Uvicorn with the specified host and port.
    By default, it runs on localhost at port 8000.

    Arguments:
        host (str): The hostname or IP address where the server will run.
        port (int): The port number on which the server will listen for connections.
    """
    import uvicorn
    sys.path.append(f'{os.path.dirname(os.path.abspath(sys.argv[0]))}/app')
    uvicorn.run('main:app', host=host, port=port, reload=True)
