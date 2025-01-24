# ScribeLog

[Read this in English](README.md) | [Leer esto en español](README_es.md)

ScribeLog is a lightweight Python library for logging messages to text files. It offers path validation and optional timestamp support for your log entries.

## Features

- Log messages to a specified `.log` file.
- Validate the file path and extension.
- Add timestamps to log entries.
- Simple configuration and usage.

## Installation

To install ScribeLog, run:

```bash
pip install ScribeLog
```

## Usage

```python
from ScribeLog import ConfigLog, Log, GetPathLogin

# Configure the log file
ConfigLog("/path/to/yourfile.log")

# Log a message with timestamp
Log("This is a test message.")

# Log a message without timestamp
Log("Another test message.", time=False)

# Retrieve the current log file path
print(GetPathLogin())
```

## Error Handling

If the log file path is invalid or doesn't meet the requirements, a `FileError` will be raised. For example:

```python
from ScribeLog import ConfigLog, FileError

try:
    ConfigLog("/invalid/path/to/file.txt")
except FileError as e:
    print(f"An error occurred: {e}")
```

## License

ScribeLog is licensed under the MIT License. See the LICENSE file for details.
