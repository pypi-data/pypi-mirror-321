from pathlib import Path


def generate_test_files(current_working_directory: str) -> dict:
    """
    Creates a 'tests' folder in the current working directory if it doesn't already exist,
    and writes a default test file inside it.

    Args:
        current_working_directory (str): The path to the current working directory.

    Returns:
        dict: A dictionary containing a success message or an error message.
    """
    try:
        cwd_path = Path(current_working_directory)
        tests_folder = cwd_path / "tests"

        # Create 'tests' folder if it doesn't exist
        tests_folder.mkdir(exist_ok=True)

        # Create a test file in the folder
        test_file = tests_folder / "test_placeholder.py"
        if not test_file.exists():
            with open(test_file, "w", encoding="utf-8") as file:
                file.write(
                    """# This is for tests
# Add your test cases here
"""
                )

        return {
            "Message": f"Tests folder and placeholder file are set up at {tests_folder}"
        }
    except Exception as e:
        return {"Error": f"Failed to set up tests folder: {str(e)}"}
