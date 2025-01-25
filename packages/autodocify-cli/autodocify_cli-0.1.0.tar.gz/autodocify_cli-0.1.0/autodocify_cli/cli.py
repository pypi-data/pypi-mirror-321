import typer
from autodocify_cli.lib.utils import get_base_path
from autodocify_cli.lib.readme_generator import generate_read_me
from autodocify_cli.lib.test_generator import generate_test_files
from autodocify_cli.lib.doc_generator import generate_technical_docs
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

app = typer.Typer()
console = Console()

ASCII_ART = """
 █████╗ ██████╗ ████████╗ ██████╗ ██████╗  ██████╗ ██████╗ ██╗███████╗██╗   ██╗
██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝ ██╔══██╗██║██╔════╝╚██╗ ██╔╝
███████║██████╔╝   ██║   ██║   ██║██████╔╝██║  ███╗██████╔╝██║█████╗   ╚████╔╝ 
██╔══██║██╔═══╝    ██║   ██║   ██║██╔═══╝ ██║   ██║██╔═══╝ ██║██╔══╝    ╚██╔╝  
██║  ██║██║        ██║   ╚██████╔╝██║     ╚██████╔╝██║     ██║███████╗   ██║   
╚═╝  ╚═╝╚═╝        ╚═╝    ╚═════╝ ╚═╝      ╚═════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝   
"""


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """AutoDocify CLI: Automate your README generation, Technical Document Generation and testing workflows."""
    if ctx.invoked_subcommand is None:
        console.print(Text(ASCII_ART, style="bold yellow"))
        console.print(
            Panel(
                "AutoDocify: Automate your README generation and testing workflows.\n\n"
                "[bold purple]Usage:[/bold purple]\n"
                "  autodocify [bold yellow]<command>[/bold yellow] [options]\n\n"
                "[bold purple]Commands:[/bold purple]\n"
                "  greet              Greets the user.\n"
                "  generate-readme    Generate a README.md using OpenAI.\n",
                border_style="green",
            )
        )
        typer.echo(ctx.get_help())


@app.command()
def greet(name: str =typer.Argument(
    "COMRADE"
)):
    """
    Greets the user with a friendly message.
    """
    console.print(f"[bold green]Hello, {name}! Welcome to AutoDocify.[/bold green]")




@app.command()
def generate_readme(
    base_dir: str = typer.Argument(
        None,
        help="Path to the project directory. Defaults to the current working directory.",
    ),
    output_file: str = typer.Option("README.md", help="Name of the output README file"),
    llm: str = typer.Option(
        "gemini", help="Name of the language model to use. Supports openai|gemini|bard "
    ),
):
    """
    Generates a README.md file for the specified project.
    """
    base_path = get_base_path(base_dir)
    generate_read_me(base_path, output_file, llm)
    typer.echo(f"Generating README for project at: {base_dir}. Output: {output_file}")


@app.command()
def generate_tests(
    base_dir: str = typer.Argument(
        None,
        help="Path to the project directory. Defaults to the current working directory.",
    ),
):
    """
    Generates Tests for the specified project
    """
    base_path = get_base_path(base_dir)
    generate_test_files(base_path)


@app.command()
def generate_docs(
    base_dir: str = typer.Argument(
        None,
        help="Path to the project directory. Defaults to the current working directory.",
    ),
    output_file: str = typer.Option("DOCS.md", help="Name of the output DOCS file"),
    llm: str = typer.Option(
        "gemini", help="Name of the language model to use. Supports openai|gemini|bard "
    ),
):
    """
    Generates Technical Documentation for the specified project
    """
    base_path = get_base_path(base_dir)
    generate_technical_docs(base_path, output_file, llm)


if __name__ == "__main__":
    app()
