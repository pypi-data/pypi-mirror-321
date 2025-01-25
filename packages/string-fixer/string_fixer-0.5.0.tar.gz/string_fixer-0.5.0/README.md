# String Fixer

Simple tool to replace "double quotes" with 'single quotes' in Python files.

There are many tools out there to lint and format Python code. The most popular formatter, Black,
[prefers double quotes to single quotes](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#strings).
Ruff is a bit more flexible, but doesn't format docstrings with single quotes
(it [lets you skip formatting them](https://github.com/astral-sh/ruff/issues/7615#issuecomment-1831179705) to preserve your own quotation style).

Neither project seems likely to add the option for entirely single-quoted code, so this tool can work as a post-processor to fix that.

## Usage

### CLI

```bash
# run against single file
python -m string_fixer --target my_file.py
# run against directory
python -m string_fixer --target lib/src/
# run against working dir
python -m string_fixer
```

### IDE Plugins

This project has an accompanying [VSCode extension](https://github.com/Crozzers/string-fixer/tree/main/extensions/vscode).


## Configuration

Configuration is done via the `pyproject.toml` file and the default settings are as follows:
```toml
[tool.string-fixer]
# file or folder to format
target = "./"
# set to true to print planned changes but not modify any files (overrides `output` config)
dry_run = false
# write a copy of the files to this directory, rather than modifying them inplace
output = "./"
# list of glob patterns for files to ignore. this value is autopopulated from `.gitignore` files as well
# as a few default values. anything you put in this list will be added to this set, rather than replacing
# it. Use the `include` option to override
ignore = [
    # these are the defaults
    "./**/.*",
    "./**/site-packages",
    "./**/node_modules",
    "./**/build",
    "./**/dist",
    "./**/__pycache__",
    "./**/venv"
]
# list of glob patterns for files to include. This setting overrides `ignore`
include = []
# extend and override options in another pyproject.toml file
extends = ""
# python version to target for compatibility (defaults to current python version)
# this must be a string because `float("3.10") == 3.1`
target_version = "3.12"
# try to produce strings with the least number of escapes, even if that means deviating from the quote style
prefer_least_escapes = true
# preferred quote style. Allowed options are 'single' or "double"
quote_style = "single"
```

All file paths are resolved relative to the `pyproject.toml`'s location.


## See Also

- [VSCode Extension](https://marketplace.visualstudio.com/items?itemName=Crozzers.string-fixer) ([source](https://github.com/Crozzers/string-fixer/tree/main/extensions/vscode))
- [PyPI package](https://pypi.org/project/string-fixer/) ([source](https://github.com/Crozzers/string-fixer/tree/main/lib))
