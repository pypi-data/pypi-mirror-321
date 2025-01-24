import click
import sys
from .config import Config
from .providers import get_provider
from .shell_utils import detect_shell

@click.command()
@click.argument("command_parts", nargs=-1)
@click.option("--provider", help="AI provider to use (anthropic/openai)")
@click.option("--model", help="Model to use")
@click.version_option()
def main(command_parts, provider, model):
    if not command_parts:
        click.echo("Please provide a command to explain.", err=True)
        sys.exit(1)

    config = Config()

    if provider:
        config.defaults["provider"] = provider
    if model:
        config.defaults["model"] = model

    ai_provider = get_provider(config)  # This line needs to be here
    current_shell = detect_shell()

    query = " ".join(command_parts)
    if not query.lower().startswith("do i"):
        query = "do i " + query

    try:
        command = ai_provider.get_command(query, current_shell)
        click.echo(command)
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        sys.exit(1)

