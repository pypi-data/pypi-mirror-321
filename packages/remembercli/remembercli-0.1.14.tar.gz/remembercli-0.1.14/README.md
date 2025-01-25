# rememberCLI

A simple task managing CLI program written in [Python](https://www.python.org/), built with [Typer](https://typer.tiangolo.com/), and packaged with [uv](https://docs.astral.sh/uv/).

The design of the program was heavily influenced by the amazing [CLI Guidlines](https://clig.dev/).

This program is also uses the powerful date parsing tool in [dateparser](https://dateparser.readthedocs.io/en/latest/) to process stdin date inputs, as well as [dateutil](https://dateutil.readthedocs.io/en/stable/) to work with date objects.

All data are stored locally as JSON.

rememberCLI may be forked and modified with no restrictions. Pull requests are encouraged so improvements may be shared with the community.

rememberCLI is still a work in progress with a lot of improvements to be made.

Prerequisites
---

### Python

**Note that most modern computers come with a version of python installed. It is recommended that you leave this version of Python untouched as your machine uses it to run processes.**

The current version of rememberCLI was developed in a virtual environment running Python 3.12 so make sure your machine has the same or a newer version of python installed.

This [article](https://realpython.com/installing-python/) by Real Python is an in-depth guide for installing Python on various operating systems.

After you get Python installed, be sure to add it to PATH. This [article](https://realpython.com/add-python-to-path/), also by Real Python, explains what PATH is and how to add your fresh Python install to it.

You can also opt to take a look at the [official Python website](https://www.python.org/) instead.

### pip

[pip](https://pip.pypa.io/en/stable/) is a package installer for Python. You will be using it to install rememberCLI.

Usually, pip is included with a Python installation. You can run the following code to check if pip is installed on your machine.

```
pip --version
```

If pip isn't installed, run the following code from the [official pip documentation](https://pip.pypa.io/en/stable/installation/) to install it.

```
python -m ensurepip --upgrade
```

Installation
---

Installing rememberCLI is straightforward.

Run the following code to install rememberCLI

```
pip install remembercli
```

Try running `rem` or `rem --help` to see if rememberCLI installed properly.


Usage
---

The commands for rememberCLI were designed to be intuitive and easy to use.

When in doubt, use the `--help` option for learn more about a particular command. E.g. `rem show --help`

### Important: To use or not to use `--help`

Some commands, like `rem add` or `rem`, will show the help menu with and without the `--help` option explicitly typed.

Therefore, `rem add` is the same as `rem add --help`. Similarly, `rem` is the same as `rem --help`.

This is because `rem add` only adds an item when it receives arguments (inputs). Without any arguments, it defaults to showing the help menu.

The `rem` command works the same. It expects additional commands and arguments to know what exactly to do. Without them, it defaults to also showing the help menu.

However, `rem show` and `rem init` can work without any additional arguments or options passed to them. So the only way to show the help menu would be to explicitly type the `--help` option.

Therefore, it is recommended to always use the `--help` option when it doubt to avoid unintentionally running any commands.

### Important: Initializing rememberCLI after installation

To use rememberCLI, you have to initialize a directory and a JSON file. Don't worry, you only have to run the following command

```
rem init
```

This command does three things:
1. First, it creates a config file that will contain the path to your vault file
2. Then, it creates a vault directory in your home directly where your vault file will live
3. And finally, it creates a vault.json file that will contain all rememberCLI data

**rememberCLI will create directories and vault files in the home directory by default.**

- Typically, you will only need to run this command once, right after installing rememberCLI for the first time. 

- If you wish to use a new vault file, directory, or both, you can run this command again. 

- Make sure that you use a different directory name if you wish to keep using the same name for your vault file, or if you wish to keep using the same directory as before but want to use a new vault file, make sure the name of the vault file is different than the existing one. Your config file will be updated to point to your new vault file accordingly.

- You can also run the command to switch between different directories and vault files. Make sure to enter the names correctly or the init command will create unwanted directories and vault files.

### Adding a Task/Note: the `add` command

To add an item to rememberCLI, you will use the `add` command.

Go ahead and run the following command(s) to see all the options available to the `add` command

```
rem add
```
or

```
rem add --help
```

At the present, the `add` command has three additional options available to it.

**It is important that you use quotes, double or single, to pass in arguments (inputs). Without quotes, rememberCLI, and other CLI tools in general, will think of your inputs as commands it has to look for and execute.**

#### Adding a task for a given day

To add a task for a given day, you would use the following format

```
rem add 'today's task'
```

#### Adding a task with a note for a given day

To add a task and an associated note, you would use the following format

```
rem add 'today's task' --note 'note for the task'
```

#### Adding a note without any corresponding task for a given day

You can add a standalone note with the following format

```
rem add --note 'a note'
```

#### Adding a task for the next day

You can use the following format to add a task for the next day

```
rem add 'tomorrow's task' --tom
```

#### Adding a task and a note for the next day

You can use the following format to add a task and an associated note for the next day

```
rem add 'tomorrow's task' --note 'note for task' --tom
```

#### Adding a note for the next day

You can use the following format to add a standalone note for the next day

```
rem add --note 'a note' --tom
```

### Important: adding items for a specific date using the `--for` option

The `--for` option can read date inputs in various formats thanks to the powerful [dateparser](https://dateparser.readthedocs.io/en/latest/) library, but it still has its limitations.

I would encourage you to take a look at the official documentation of the [dateparser](https://dateparser.readthedocs.io/en/latest/) library to get on top of the acceptable formats.

**As of right now, rememberCLI doesn't support time parsing**

#### Adding a task for a specific date

You can use the following formats to add a task for a specific date.

```
rem add 'a task' --for 'Jan 5, 2025'
```
```
rem add 'a task' --for '23-06-2025'
```
```
rem add 'a task' --for '4th January, 2025'
```

#### Adding a task and a note for a specific date

You can use the following formats to add a task and an associated note for a specific date.

```
rem add 'a task' --note 'note for task' --for 'Jan 5, 2025'
```
```
rem add 'a task' --note 'note for task' --for '23-06-2025'
```
```
rem add 'a task' --note 'note for task' --for '4th January, 2025'
```

#### Adding a note for a specific date

You can use the following formats to add a standalone note for a specific date.

```
rem add --note 'a note' --for 'Jan 5, 2025'
```
```
rem add --note 'a note' --for '23-06-2025'
```
```
rem add --note 'a note' --for '4th January, 2025'
```

#### Adding an undated task

You can add a task without any specific dates by using the following format

```
rem add 'a task' --undated
```

#### Adding an undated task and a note

You can add a task and an associated note without any specific dates by using the following format

```
rem add 'a task' --note 'task for note' --undated
```

#### Adding an undated note

You can add a standalone note without any specific dates by using the following format

```
rem add 'a note' --undated
```

### Viewing tasks/notes: the `show` command

#### Viewing all tasks and notes for a given day

You can view all your tasks and notes for a given day by running the following code

```
rem show
```

#### Viewing all tasks only for a given day

You can view all your tasks for a given day by running the following code

```
rem show --task
```

#### View all notes for a given day

Likewise, you can view all your notes for a given day by running the following code

```
rem show --note
```

#### Viewing all tasks and notes for the next day

You can view all your tasks and notes for the next day by running the following code

```
rem show --tom
```

#### Viewing all tasks only for the next day

You can view all your tasks for a given day by running the following code

```
rem show --task --tom
```

#### View all notes only for the next day

Likewise, you can view all your notes for a given day by running the following code

```
rem show --note --tom
```

#### Viewing all tasks and notes for the current week

You can view all your tasks and notes for the current by running the following code

```
rem show --week
```

#### Viewing all tasks only for the current week

You can view all your tasks for a given day by running the following code

```
rem show --task --week
```

#### View all notes only for the current week

Likewise, you can view all your notes for a given day by running the following code

```
rem show --note --week
```

#### Viewing all tasks and notes for a specific date

You can view all your tasks and notes for a specific week by running the following code

```
rem show --for '11 Feb, 2025'
```

#### Viewing all tasks only for a specific date

You can view all your tasks for a specific date by running the following code

```
rem show --task --for 'March 28, 2026'
```

#### View all notes only for the a specific date

Likewise, you can view all your notes for a specific date by running the following code

```
rem show --note --for '2027-11-26'
```

#### Viewing all undated tasks and notes

You can view all your undated tasks and notes by running the following code

```
rem show --undated
```

#### Viewing all undated tasks only

You can view all your undated tasks by running the following code

```
rem show --task --undated
```

#### View all undated notes only

Likewise, you can view all your undated notes by running the following code

```
rem show --note --undated
```

#### View all tasks and notes in the vault

You can view all your tasks and notes in your vault file by running the following code

```
rem show --all
```

#### View all tasks in the vault

You can view all your tasks in your vault file by running the following code

```
rem show --task --all
```

#### View all notes in the vault

You can view all your notes in your vault file by running the following code 

```
rem show --note --all
```

### Removing tasks/notes for the vault: the `clean` command

#### Removing older tasks and notes (excluding undated items)

You can remove all your older tasks and notes from your vault file by running the following code (Note that this command will not touch your undated items)

```
rem clean
```

#### Removing undated items

You can remove your undated items from your vault file by running the following code (Note that this command will not touch your items with dates)

```
rem clean --undated
```

#### Removing all items

You can remove all items from your vault by running the following code (Use this command with caution)

```
rem clean --all
```


Uninstallation
---

You can easily uninstall rememberCLI, and other python packages in general, using pip.

Use the following command to uninstall rememberCLI

```
pip uninstall remembercli
```

This command will not delete the vault directory, the fault file, or the config file. Those will have to be manually deleted. This shouldn't be too difficult since all of them will be located in your machine's home directory.

Use the `ls` command to list the contents of your home directory. You should see the rememberCLI vault directory as well as the config file. Then, you can use the `rm -r` command to delete the vault directory and the config file.

**Be extremely careful when using the `rm -r` command as it will recursively delete all the contents of a directory for example, permanently.**

Here's an example of deleting the vault directory and the config file

```
ls                    // list home directory contents

rm -r [vault_name]    // will delete the directory along with any vault files inside

rm -r [config_file]   // will delete the config file
```
