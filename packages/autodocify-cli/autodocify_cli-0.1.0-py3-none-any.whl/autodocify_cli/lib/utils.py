import subprocess
from pathlib import Path

import typer
import subprocess


def greet_user(name: str = "Comrade") -> str:
    """
    Returns a greeting message.
    """
    return f"Hello, {name}! Welcome to AutoDocify."


def get_base_path(base_dir: str):
    # Default to the current working directory if base_dir is not provided
    if base_dir is None:
        base_dir = Path.cwd()

    base_path = Path(base_dir)
    if not base_path.exists():
        typer.echo(f"Error: The directory {base_dir} does not exist.")
        raise typer.Exit(code=1)
    else:
        return base_path




def get_git_tracked_files(base_path):
    """
    Retrieve a list of all files tracked by Git in the given directory,
    excluding those that have been deleted but not yet committed.
    """
    try:

        # Get the list of tracked files
        result = subprocess.run(
            ["git", "ls-files"],
            cwd=base_path,
            text=True,
            capture_output=True,
            check=True,
        )
        tracked_files = result.stdout.strip().split("\n")

        # Get the list of deleted files not yet committed
        deleted_result = subprocess.run(
            ["git", "ls-files", "--deleted"],
            cwd=base_path,
            text=True,
            capture_output=True,
            check=True,
        )
        deleted_files = deleted_result.stdout.strip().split("\n")

        # Filter out deleted files from the tracked files list
        files_to_merge = [file for file in tracked_files if file not in deleted_files]

        if not files_to_merge:
            print("No valid files found to merge in the repository.")
            return []
        else:
            return files_to_merge
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return []
    












    
def ai_service(file_path: str, llm: str) -> None:
    typer.echo(f"Using {llm}")
    match llm:
        case "gemini":
            pass
        case "openai":
            pass
        case "bard":
            pass


def readme_prompt(content):
    prompt = f"""
    You are an expert software engineer and technical writer. Using the provided content, generate a professional README.md for the project.
    
    The README should include:
    - A project overview
    - Features
    - Installation instructions
    - Usage examples
    - License (if applicable)

    Here is the project content:
    {content}
    """
    return prompt


def technical_docs_prompt(content):
    prompt = f"""
    You are an expert software engineer and technical writer. Using the provided content, generate a professional Technical Documentation for the project.
    
    The Technical Documentation should include:
    - A project overview
    - Installation and Setup
    - Operation
    - Troublehooting and Support
    - FAQs
    - Testing and Review Process

    Here is the project content:
    {content}
    """
    return prompt


def test_prompt(content):
    prompt = f"""
    You are an expert software engineer and QA engineer. Using the provided content, generate the list of unit tests and integration tests for the project.

    Unit Tests should be under a heading "UNIT TEST"
    Integration Tests should be under a heading "INTEGRATION TEST"

    Here is the project content:
    {content}
    """
