# WebVTT Translator

WebVTT Translator is a Python package for translating WebVTT subtitle files into different languages using various translation APIs.

## Features

- Translate WebVTT subtitle files to multiple languages.
- Support for various translation APIs (e.g., Google Translate, Microsoft Translator).
- Easy-to-use command-line interface.

## Prerequisites

Before using WebVTT Translator, you need to have an OpenAI API Key. Set the API key as an environment variable:

### On Linux/macOS:

```bash
export OPENAI_API_KEY='your_openai_api_key'
```

### On Windows (Command Prompt):

```cmd
set OPENAI_API_KEY=your_openai_api_key
```

### On Windows (PowerShell):

```powershell
$env:OPENAI_API_KEY='your_openai_api_key'
```

## Installation

You can install the package using pip:

```bash
pip install webvtt-translator
```

## Usage

### Command Line Interface

To translate a WebVTT file, use the following command:

```bash
webvtt-translator translate -i input.vtt -o output.vtt -l Portuguese
```

You can also run the module via python:

```bash
python -m webvtt_translator -i input.vtt -o output.vtt -l Portuguese
```

The command line arguments are:

- `-i` or `--input`: Path to the input WebVTT file.
- `-o` or `--output`: Path to the output translated WebVTT file.
- `-l` or `--language`: Target language (e.g., Spanish, English, Portuguese).

## Contact

For any questions or suggestions, please open an issue on GitHub.
