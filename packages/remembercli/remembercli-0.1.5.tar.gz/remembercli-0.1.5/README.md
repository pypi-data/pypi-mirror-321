# rememberCLI

A simple task managing CLI program written in [Python](https://www.python.org/), built with [Typer](https://typer.tiangolo.com/), and packaged with [uv](https://docs.astral.sh/uv/).

The design of the program was heavily influenced by the amazing [CLI Guidlines](https://clig.dev/).

This program is also uses the powerful date parsing tool in [dateparser](https://dateparser.readthedocs.io/en/latest/) to process stdin date inputs.

All data are stored locally as JSON.

rememberCLI may be forked and modified with no restrictions. Pull requests are encouraged so improvements may be shared with the community.

rememberCLI is still a work in progress with a lot of improvements to be made.

Prerequisites
---

### Python
The current version of remembeCLI was developed in a virtual environment running Python 3.12 so make sure your machine has the same or a newer version of python installed.

This [article](https://realpython.com/installing-python/) by Real Python is an in-depth guide for installing Python on various operating systems.

After you get Python installed, be sure to add it to PATH. This [article](https://realpython.com/add-python-to-path/), also by Real Python, explains what PATH is and how to add your fresh Python install to it.

You could also opt to take a look at the [official Python website](https://www.python.org/) instead.

### pip

[pip](https://pip.pypa.io/en/stable/) is a package installer for Python. You will be using it to install rememberCLI.

Usually, pip is included with a Python installation. You can run the following code to check if pip is installed on your machine.

```
pip --version
```

If pip isn't installed, run the following code from the [official pip documentation](https://pip.pypa.io/en/stable/installation/) to installed it.

```
python -m ensurepip --upgrade
```

Installation
---

Installing rememberCLI should be fairly easy and straightforward.

Run the following code to install rememberCLI

```
pip install remembercli
```

Try running `rem` or `rem --help` to see if rememberCLI installed properly.


Usage
---

### Important: Initializing rememberCLI after install

To use rememberCLI, you have to initialize a directory and a JSON file. Don't worry, you only have to run the following command

```
rem init
```

This command does three things:
1. First, it creates a config file that will contain the path to your vault file
2. Then, it creates a vault directory in your home directly where your vault file will live
3. And finally, it creates a vault.json file that will contain all rememberCLI data

Typically, you will only need to run this command once. If your config file, vault file, or the vault folder is accidently deleted for example, you can run this command to repair the errors.

### 

