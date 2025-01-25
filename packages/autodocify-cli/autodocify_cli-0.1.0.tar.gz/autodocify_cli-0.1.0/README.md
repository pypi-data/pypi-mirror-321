# AutoDocify CLI: Automated Documentation and Test Generation

AutoDocify is a command-line interface (CLI) tool designed to automate the generation of project documentation and placeholder test files. Leveraging the power of Large Language Models (LLMs), AutoDocify streamlines your development workflow by creating professional READMEs, basic technical documentation, and a starting point for your testing strategy. It currently supports Google Gemini, OpenAI, and Bard (with Bard integration being a work in progress).


## Features

* **Automated README Generation:** Generates a comprehensive `README.md` file summarizing your project's key aspects, including an overview, features, installation instructions, usage examples, and licensing information. The README is tailored to be professional and informative, assisting in project communication and collaboration. Supports Gemini, OpenAI, and Bard LLMs. Gemini is the default and currently the best-supported.

* **Automated Technical Documentation Generation:** Creates a foundational technical documentation file (`DOCS.md`). This feature is under active development and its capabilities will expand in future releases.

* **Automated Test File Generation:** Creates a `tests` directory containing a `test_placeholder.py` file. This provides a readily available template for writing unit and integration tests, encouraging a test-driven development approach.

* **Git Integration:** AutoDocify leverages Git to identify and incorporate only the relevant project files into the documentation generation process.  Ensure your project is a Git repository, and your files are committed before running AutoDocify commands.

* **Multiple LLM Support:** Offers flexibility by allowing you to choose the LLM (Gemini, OpenAI, or Bard) best suited for your needs and project requirements. You'll need to set environment variables for OpenAI and Google Gemini API keys (`OPENAI_API_KEY`, `GEMINI_API_KEY`). For OpenAI, also set `OPENAI_MODEL` (e.g., "gpt-3.5-turbo").

* **Robust Error Handling and Reporting:** Provides informative error messages to facilitate troubleshooting and quick resolution of any issues encountered during execution.  Uses the `rich` library for enhanced console output.

* **Clear CLI Structure:** Uses the `typer` library to provide a user-friendly command-line interface.


## Installation

AutoDocify requires Python 3.12 or higher. It utilizes Poetry for dependency management.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/[your_github_username]/autodocify-cli.git  # Replace with your actual GitHub URL
   cd autodocify-cli
   ```

2. **Install Poetry (if necessary):** Follow the instructions at [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation).

3. **Install AutoDocify:**

   ```bash
   poetry install
   ```

4. **(Optional) Install development dependencies:** For contributing to the project, install the development dependencies:

   ```bash
   poetry install --extras dev
   ``` This installs `pytest` for testing, `flake8` for code style checking, and `black` for code formatting.


## Usage Examples

Before running any commands, ensure your project is a Git repository and you've committed your changes. Set the necessary environment variables for your chosen LLM's API key.

* **Generate README:**

   ```bash
   autodocify generate-readme
   ```
   This generates a `README.md` file in the current directory. Options include:

   ```bash
   autodocify generate-readme --output-file my_readme.md --base-dir ../my_project --llm openai
   ```
   This generates a README file named `my_readme.md` in the `../my_project` directory using the OpenAI LLM. Replace `openai` with `gemini` or `bard` as needed.


* **Generate Test Files:**

   ```bash
   autodocify generate-tests
   ```
   This creates a `tests` directory and a `test_placeholder.py` file in the current working directory. You can specify a different base directory with the `--base-dir` option.


* **Generate Technical Documentation:** (Under development)

   ```bash
   autodocify generate-docs
   ```
   This generates a `DOCS.md` file. Similar options to `generate-readme` are available.


* **Verify Installation:**

   ```bash
   autodocify greet --name "Your Name"
   ```


## Troubleshooting

* **API key not found:** Ensure your `OPENAI_API_KEY` and/or `GEMINI_API_KEY` environment variables are correctly set. For OpenAI, also ensure `OPENAI_MODEL` is set.

* **Not a Git repository:** Initialize your project as a Git repository using `git init`.

* **No tracked files found:** Commit your files to Git before running AutoDocify commands.

* **Error during LLM interaction:** Check your internet connection and API key limits. Rate limits from the LLM provider may cause failures.  Check the LLM provider's documentation for details on rate limits and usage.


## Contributing

Contributions are welcome! Please open an issue to discuss potential contributions or improvements.  A `CONTRIBUTING.md` file will be added in a future release.


## License

[Specify your license here, e.g., MIT License]
