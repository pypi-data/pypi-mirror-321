import os
import typer
from autodocify_cli.lib.project_content_merger import merge_files
from autodocify_cli.lib.utils import get_git_tracked_files, readme_prompt
from autodocify_cli.ai_integration import ai


def generate_read_me(base_path: str, output_file: str, llm: str) -> dict:
    """
    Generates a README.md file for the project by merging content from the specified base directory.

    Args:
        base_dir (str): The directory containing the project files to merge.
        output_file (str): The name of the output README file.
        llm (str): The AI language model to use defaults to 'gemini'

    Returns:
        dict: A dictionary containing a success message or an error message.
    """
    try:
        # Get Tracked Files
        files = get_git_tracked_files(base_path)
        # Merge files from the specified directory into the output file
        content = merge_files(base_path, files)
        prompt = readme_prompt(content)
        result = ai(prompt, llm)
        with open(output_file, "w") as out_file:
            out_file.write(result)
        os.remove(f"{base_path}/merge.txt")
        return {"Message": f"README generated successfully at {output_file}"}
    except Exception as e:
        typer.echo(f"Failed to generate README: {str(e)}")
        return {"Error": f"Failed to generate README: {str(e)}"}
