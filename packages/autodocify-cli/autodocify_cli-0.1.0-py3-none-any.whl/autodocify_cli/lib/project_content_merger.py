from pathlib import Path


# def merge_files(base_path, files):
#     """
#     Merge the content of all files tracked by Git into a single file.
#     """
#     try:

#         print(f"Found {len(files)} tracked files. Merging...")
#         output_file = "merge.txt"
#         # Merge file contents
#         with open(output_file, "w", encoding="utf-8") as out_file:
#             for file in files:
#                 relative_path = base_path / file
#                 out_file.write(f"\n# ===== File: {relative_path} =====\n")
#                 with open(
#                     relative_path, "r", encoding="utf-8", errors="ignore"
#                 ) as in_file:
#                     out_file.write(in_file.read())
#                     out_file.write("\n")

#         print(f"All files successfully merged into {output_file}")
#         with open(output_file, "r", encoding="utf-8") as merged_file:
#             content = merged_file.read()
#         return content

#     except Exception as e:
#         print(f"An error occurred: {e}")


from pathlib import Path



# merged_content = merge_files(base_path, files, exclude_extensions)

from pathlib import Path

def merge_files(base_path, files, exclude_extensions=None):
    """
    Merge the content of specified files into a single file, excluding files with certain extensions.
    
    Parameters:
    - base_path (Path): The base directory containing the files.
    - files (list): List of filenames to merge.
    - exclude_extensions (set): Set of file extensions to exclude (e.g., {'.lock', '.tmp'}).
    """
    if exclude_extensions is None:
        exclude_extensions = {'.lock', '.tmp'}  # Default to excluding '.lock' files

    try:
        # Filter out files with excluded extensions
        files_to_merge = [
            file for file in files
            if Path(file).suffix not in exclude_extensions
        ]

        print(f"Found {len(files_to_merge)} files to merge after exclusion. Merging...")
        output_file = base_path / "merge.txt"

        # Merge file contents
        with open(output_file, "w", encoding="utf-8") as out_file:
            for file in files_to_merge:
                relative_path = base_path / file
                out_file.write(f"\n# ===== File: {relative_path} =====\n")
                with open(
                    relative_path, "r", encoding="utf-8", errors="ignore"
                ) as in_file:
                    out_file.write(in_file.read())
                    out_file.write("\n")

        print(f"All files successfully merged into {output_file}")
        with open(output_file, "r", encoding="utf-8") as merged_file:
            content = merged_file.read()
        return content

    except Exception as e:
        print(f"An error occurred: {e}")
