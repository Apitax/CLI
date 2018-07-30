import click
from cli.api.Api import authenticate,doScript,log_printer

@click.group()
def cli():
    pass


@cli.group()
def script():
    pass


@cli.group()
def command():
    pass


@script.command()
@click.option('--username', '-u', help='Apitax username')
@click.option('--password', '-p', help='Apitax password')
@click.argument('scriptname')

def execute(username, password, scriptname):
    log_printer(doScript(authenticate(username,password), scriptname))











cli.add_command(script)
cli.add_command(command)

script.add_command(execute)
