# File2Markdown

File2Markdown is a simple and lightweight Python program that converts files into Markdown format using Microsoft's [MarkItDown](https://github.com/microsoft/markitdown) library. This tool is currently focused on scanning and converting local files, making it ideal for desktop use.

## Features

- Convert local files (e.g., PDFs, Word documents, Excel spreadsheets) to Markdown.
- Simple command-line interface for ease of use.
- Outputs Markdown content either to the console or to a specified `.md` file.

**Note:** This tool does not yet utilize advanced features like GPT integration for additional processing. It focuses solely on converting local files to Markdown.

## Installation

### Prerequisites

- Python 3.7 or later
- `pip` package manager

### Steps

1. Clone this repository:

    ```bash
    git clone https://github.com/mthomason/File2Markdown
    cd File2Markdown
    ```

2. Create and activate an virtual environment (recommended)

    ```bash
    # On Windows:
    python -m venv venv
    venv\\Scripts\\activate
    
    # On macOS/Linux:
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the program using the following command:

### Convert a file and display Markdown content in the terminal

```bash
python src/md.py --file path/to/your/input-file.pdf
```

### Convert a file and save the output to a Markdown file

```bash
python src/md.py --file path/to/your/input-file.pdf --output path/to/output.md
```

### Example

Convert a PDF file and save the Markdown content:

```bash
python src/md.py --file sample.pdf --output sample.md
```

The above command will save the converted content in `sample.md`.

## File Structure

```bash
File2Markdown/
├── .gitignore            # Files and directories to be ignored by Git
├── .vscode/settings.json # VSCode configuration files
├── LICENSE               # MIT license file
├── requirements.txt      # Python dependencies for the project
├── src/
│   ├── __init__.py       # Placeholder for Python package
│   └── md.py             # Main script for file conversion
```

## Contributing

We welcome contributions to improve and expand the functionality of File2Markdown. Here are some ideas:

- Add support for processing files via URLs.
- Integrate GPT capabilities to provide richer context or descriptions for the content.
- Add unit tests and improve code coverage.

To contribute:

1. Fork this repository.
2. Create a new branch for your feature/bugfix.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Feedback and Support

If you encounter any issues or have suggestions for improvements, feel free to open an issue on GitHub. We value your feedback and ideas to make File2Markdown better!

---

Enjoy converting files to Markdown effortlessly with File2Markdown!