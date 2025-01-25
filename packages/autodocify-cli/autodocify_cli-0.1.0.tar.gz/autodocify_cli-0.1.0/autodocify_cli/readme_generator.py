# import subprocess

# from pathlib import Path



# import openai



# def get_git_tracked_files(base_dir: str) -> list:
#     """
#     Retrieves all Git-tracked files in the given directory.

#     Args:
#         base_dir (str): Path to the Git repository.

#     Returns:
#         list: List of file paths relative to the repository root.
#     """
#     try:
#         result = subprocess.run(
#             ["git", "ls-files"],
#             cwd=base_dir,
#             text=True,
#             capture_output=True,
#             check=True,
#         )
#         return result.stdout.strip().split("\n")
#     except subprocess.CalledProcessError as e:
#         raise RuntimeError(f"Error retrieving Git-tracked files: {e}")

# def read_files_content(file_paths: list, base_dir: str) -> str:
#     """
#     Reads the content of a list of files and aggregates them into a single string.

#     Args:
#         file_paths (list): List of file paths to read.
#         base_dir (str): Base directory for resolving relative paths.

#     Returns:
#         str: Aggregated content of all files.
#     """
#     content = ""
#     base_path = Path(base_dir)
#     for file in file_paths:
#         file_path = base_path / file
#         try:
#             with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
#                 relative_path = file_path.relative_to(base_dir)
#                 content += f"\n# ===== File: {relative_path} =====\n"
#                 content += f.read()
#         except Exception as e:
#             print(f"Skipping file {file}: {e}")
#     return content

# def generate_readme_with_openai(base_dir: str, api_key: str) -> None:
#     """
#     Generates a README.md file using OpenAI by summarizing the Git-tracked files in the directory.

#     Args:
#         base_dir (str): Path to the project directory.
#         api_key (str): OpenAI API key.
#     """
#     # Step 1: Get Git-tracked files
#     try:
#         tracked_files = get_git_tracked_files(base_dir)
#         if not tracked_files:
#             print("No Git-tracked files found.")
#             return
#     except RuntimeError as e:
#         print(str(e))
#         return

#     # Step 2: Aggregate content from tracked files
#     content = read_files_content(tracked_files, base_dir)

#     # Step 3: Generate README using OpenAI
#     openai.api_key = api_key
#     prompt = f"""
#     You are an expert software engineer and technical writer. Using the provided content, generate a professional README.md for the project.
    
#     The README should include:
#     - A project overview
#     - Features
#     - Installation instructions
#     - Usage examples
#     - License (if applicable)

#     Here is the project content:
#     {content}
#     """
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=[
#                 {"role": "system", "content": "You are a technical documentation assistant."},
#                 {"role": "user", "content": prompt}
#             ]
#         )
#         summary = response.choices[0].message.content
#     except Exception as e:
#         print(f"Error generating README: {e}")
#         return

#     # Step 4: Write the summary to README.md
#     readme_path = Path(base_dir) / "README.md"
#     try:
#         with open(readme_path, "w", encoding="utf-8") as readme_file:
#             readme_file.write(summary)
#         print(f"README.md successfully generated at {readme_path}")
#     except Exception as e:
#         print(f"Error writing README.md: {e}")