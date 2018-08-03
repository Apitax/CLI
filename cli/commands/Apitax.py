import click
from cli.api.Api import Api


@click.group()
@click.option('--debug/--no-debug', '-d', help='Increases the verbosity of the logging and shell output', default=False)
@click.option('--sensitive/--no-sensitive', '-s', 
    help='Hides parameters from the log and shell output to protect sensitive information such as passwords that may be sent along with a request'
    , default=False)
@click.option('--username', '-u', help='Apitax username', type=str)
@click.option('--password', '-p', help='Apitax password', type=str)
@click.option('--host', '-h', help='The address which Apitax can be reached at', type=str)
@click.pass_context
def cli(ctx, debug, sensitive, username, password, host):
    if(not ctx.obj):
        ctx.obj = {}
    ctx.obj['debug'] = debug
    ctx.obj['sensitive'] = sensitive
    ctx.obj['username'] = username
    ctx.obj['password'] = password
    
    if(host):
        Api.setHost(host)
        


@cli.group()
@click.pass_context
def script(ctx):
    pass

@cli.group()
@click.pass_context
def command(ctx):
    pass


@script.command()
@click.argument('scriptname', type=str)
@click.pass_context
def execute(ctx, scriptname):
    Api.log_printer(Api.doScript(Api.authenticate(ctx.obj['username'],ctx.obj['password']), scriptname))

