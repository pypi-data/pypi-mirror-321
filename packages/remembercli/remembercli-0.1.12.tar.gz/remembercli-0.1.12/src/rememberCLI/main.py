import typer
from typing import Optional
from typing_extensions import Annotated
from rich.console import Console
from rich.table import Table
from rich import print
from dateutil.parser import parse
from pathlib import Path
from datetime import date, datetime
import os
import calendar
import json
from posix import dup2

console = Console()
curr_date = date.today()
cal_med = calendar.Calendar()
version = "0.1.12"
config_path = f"{Path.home()}/remembercli_config.json"

app = typer.Typer(
    no_args_is_help=True,
    rich_markup_mode='rich',
    help='A CLI task management tool for the distracted!',
    epilog=f'Made with [red]:heart:[/red] by [violet]Saysah[/violet]. Version {version}'
)


def init_json():
    path = get_vault_path()
    if not path == 'Error':
        with open(f"{path}", 'w') as file:

            data = {
                'undated' : []
            }

            json.dump(data, file, indent=4)
    else:
        print("Error fetching file path")


def update_json(task = None, note = '', date = 'undated'):

    new_item = {
        'task': task,
        'note': note,
        'date': date
    }

    path = get_vault_path()
    if not path == 'Error':
        with open(path, 'r') as file:
            data = json.load(file)
            if date in data:
                data[date].append(new_item)
            else:
                data[date] = []
                data[date].append(new_item)
        with open(path, 'w') as file:
            json.dump(data, file, indent=4, sort_keys=True)
    else:
        print("Error fetching file path")


def init_config(updated_path):
    with open(config_path, 'w') as file:

        data = {
            'activeVaultPath': f'{updated_path}'
        }

        json.dump(data, file, indent=4)


def update_config(updated_path):
    with open(config_path, 'r') as file:

        data = json.load(file)
        data['activeVaultPath'] = f'{updated_path}'

    with open(config_path, 'w') as file:

        json.dump(data, file, indent=4)


def check_vault_path():
    if Path(config_path).exists:
        with open(config_path, 'r') as file:
            data = json.load(file)
            if Path(f'{data['activeVaultPath']}').exists:
                return True
            else:
                return False
    else:
        return False


def get_vault_path():
    if check_vault_path():
        with open(config_path, 'r') as file:
            data = json.load(file)
            return data['activeVaultPath']
    else:
        return 'Error'


def get_date_diff(n1, n2):
    temp1 = parse(str(n1)).date()
    temp2 = parse(str(n2)).date()

    d1 = temp1.strftime("%d")
    m1 = temp1.strftime("%m")
    y1 = temp1.strftime("%Y")
    d2 = temp2.strftime("%d")
    m2 = temp2.strftime("%m")
    y2 = temp2.strftime("%Y")

    date1 = date(int(y1), int(m1), int(d1))
    date2 = date(int(y2), int(m2), int(d2))
    date_diff = date2 - date1

    return date_diff.days


def get_tomorrow(dt):
    str_date = parse(str(dt)).date()
    d1 = str_date.strftime("%d")
    m1 = str_date.strftime("%m")
    y1 = str_date.strftime("%Y")

    tom = date(int(y1), int(m1), (int(d1) + 1))

    return tom


def get_week_number(date):
    str_date = parse(str(date)).date()
    d1 = str_date.strftime("%d")
    m1 = str_date.strftime("%m")
    y1 = str_date.strftime("%Y")

    date_type = date(int(y1), int(m1), int(d1))

    _, week_no, _ = date_type.isocalendar()

    return week_no


def get_current_week_number_in_year():
    current_week = date.today().isocalendar()[1]
    return current_week


def get_month_day_count():
    _, month_day_count = calendar.monthrange(date.today().year, date.today().month)
    return month_day_count


def get_current_week_number_in_month():
    week_no = get_current_week_number_in_year()
    return week_no % 4


def get_current_month_weeks():
    week_list = cal_med.monthdatescalendar(date.today().year, date.today().month)
    return week_list


def get_current_month_week_count():
    week_count = len(get_current_month_weeks())
    return week_count


def get_current_week():
    week_list = get_current_month_weeks()

    for week in week_list:
        if date.today() in week:
            new_list = [str(day) for day in week]
            return new_list



@app.command(help='Initialize a directory and a JSON file for rememberCLI to store data in.')
def init(
    directory_name: Annotated[str, typer.Option('--dir-name', prompt='Enter preferred name for directory. Default is: ')] = 'RememberCLIVault',
    file_name: Annotated[str, typer.Option(prompt='Enter preferred name for new JSON file. Default is: ')] = 'remCLI.json'):

        config_file = Path(config_path)
        if not config_file.exists():
            config_file.touch()
            init_config(Path(f"{Path.home()}/{directory_name}/{file_name}"))
        else:
            update_config(Path(f"{Path.home()}/{directory_name}/{file_name}"))

        if not Path(f"{Path.home()}/{directory_name}").exists():
            os.makedirs(f"{Path.home()}/{directory_name}")
        else:
            print(f'Directory {directory_name} already exists. Creating {file_name} inside directory.')


        if not Path(f"{Path.home()}/{directory_name}/{file_name}").is_file():
            Path(f"{Path.home()}/{directory_name}/{file_name}").touch()
            init_json()
        else:
            print(f'JSON file {file_name} already exists in directory. Closing init.')
            raise typer.Exit()






@app.command(no_args_is_help=True, help='Add an independent task, an independent note, or a related task and note.')
def add(
    task: Annotated[Optional[str], typer.Argument(help='Add a task.')] = '',
    note: Annotated[str, typer.Option(help='Add a note.')] = '',
    today: Annotated[bool, typer.Option('-t', help='Add a task and/or a note for today.')] = False,
    tomorrow: Annotated[bool, typer.Option('--tom', help='Add a task and/or a note for tomorrow.')] = False,
    item_date: Annotated[str, typer.Option('--for', help='Set date for a task and/or a note.')] = ''
    ):

    if not today and not tomorrow and not item_date:
        update_json(task, note)
        print('Item added')

    elif today and not tomorrow and not item_date:
        update_json(task, note, str(curr_date))
        print('Item added')

    elif not today and tomorrow and not item_date:
        tom = curr_date.strftime("%d")
        tom = int(tom) + 1
        tom = str(curr_date.strftime(f"%Y-%m-{tom}"))
        update_json(task, note, tom)
        print('Item added')

    elif not today and not tomorrow and item_date:
        specific_date = str(parse(item_date).date())
        update_json(task, note, specific_date)
        print('Item added')

    else:
        print("Error: Cannot add item")



@app.command(help='Show tasks and notes for today.')
def show(
    tasks_only: Annotated[bool, typer.Option('--task', help='Show tasks only.')] = False,
    notes_only: Annotated[bool, typer.Option('--note', help='Show notes only.')] = False,
    undated_only: Annotated[bool, typer.Option('-u', '--undated', help='Show undated items')] = False,
    tomorrow: Annotated[bool, typer.Option('--tom', help='Show tasks for tomorrow.')] = False,
    curr_week: Annotated[bool, typer.Option('--week', help='Show tasks for this week.')] = False,
    specific_date: Annotated[str, typer.Option('--for', help='Show tasks for a specific date.')] = '',
    all: Annotated[bool, typer.Option('--all', help='Show all tasks in vault')] = False
    ):

    if not tomorrow and not curr_week and not specific_date and not all and not undated_only:
        if not tasks_only and not notes_only:

            file_path = get_vault_path()

            with open(file_path, 'r') as file:

                data = json.load(file)

                if str(curr_date) in data:

                    target_data = data[str(curr_date)]
                    table_items = Table('Task', 'Note', 'Date Due', 'Days Remaining')

                    for item in target_data:
                        table_items.add_row(item['task'], item['note'], item['date'], f'{get_date_diff(curr_date, item['date'])} days remaining')

                    print(table_items)

                else:
                    print('No tasks for today')

        elif tasks_only and not notes_only:

            file_path = get_vault_path()

            with open(file_path, 'r') as file:

                data = json.load(file)

                if str(curr_date) in data:

                    target_data = data[str(curr_date)]
                    table_items = Table('Task', 'Date Due', 'Days Remaining')

                    for item in target_data:
                        table_items.add_row(item['task'], item['date'], f'{get_date_diff(curr_date, item['date'])} days remaining')

                    print(table_items)

                else:
                    print('No tasks for today')

        elif not tasks_only and notes_only:

            file_path = get_vault_path()

            with open(file_path, 'r') as file:

                data = json.load(file)

                if str(curr_date) in data:

                    target_data = data[str(curr_date)]
                    table_items = Table('Note', 'Date Due', 'Days Remaining')

                    for item in target_data:
                        table_items.add_row(item['note'], item['date'], f'{get_date_diff(curr_date, item['date'])} days remaining')

                    print(table_items)

                else:
                    print('No notes for today')

        else:
            print("Command Error. Try rem show --help for more info")


    elif tomorrow and not curr_week and not specific_date and not all and not undated_only:
        if not tasks_only and not notes_only:

            file_path = get_vault_path()

            with open(file_path, 'r') as file:

                tom_date = get_tomorrow(curr_date)
                data = json.load(file)

                if str(tom_date) in data:

                    target_data = data[str(tom_date)]
                    table_items = Table('Task', 'Note', 'Date Due', 'Days Remaining')

                    for item in target_data:
                        table_items.add_row(item['task'], item['note'], item['date'], f'{get_date_diff(curr_date, item['date'])} days remaining')

                    print(table_items)

                else:
                    print('No tasks for tomorrow')

        elif tasks_only and not notes_only:

            file_path = get_vault_path()

            with open(file_path, 'r') as file:

                tom_date = get_tomorrow(curr_date)
                data = json.load(file)

                if str(tom_date) in data:

                    target_data = data[str(tom_date)]
                    table_items = Table('Task', 'Date Due', 'Days Remaining')

                    for item in target_data:
                        table_items.add_row(item['task'], item['date'], f'{get_date_diff(curr_date, item['date'])} days remaining')

                    print(table_items)

                else:
                    print('No tasks for tomorrow')

        elif not tasks_only and notes_only:

            file_path = get_vault_path()

            with open(file_path, 'r') as file:

                tom_date = get_tomorrow(curr_date)
                data = json.load(file)

                if str(tom_date) in data:

                    target_data = data[str(tom_date)]
                    table_items = Table('Note', 'Date Due', 'Days Remaining')

                    for item in target_data:
                        table_items.add_row(item['note'], item['date'], f'{get_date_diff(curr_date, item['date'])} days remaining')

                    print(table_items)

                else:
                    print('No notes for tomorrow')

        else:
            print("Command Error. Try rem show --help for more info")


    elif not tomorrow and curr_week and not specific_date and not all and not undated_only:
        if not tasks_only and not notes_only:
            week = get_current_week()
            file_path = get_vault_path()

            week_table = Table('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

            monday_items = Table('Task', 'Note')
            tuesday_items = Table('Task', 'Note')
            wednesday_items = Table('Task', 'Note')
            thursday_items = Table('Task', 'Note')
            friday_items = Table('Task', 'Note')
            saturday_items = Table('Task', 'Note')
            sunday_items = Table('Task', 'Note')

            day_list = [monday_items, tuesday_items, wednesday_items, thursday_items, friday_items, saturday_items, sunday_items]

            with open(file_path, 'r') as file:
                data = json.load(file)
                if week is not None:
                    for i in range(0, 6):
                        if week[i] in data:
                            for item in data[week[i]]:
                                day_list[i].add_row(item['task'], item['note'])
                else:
                    print('Error fetching week list')

            week_table.add_row(monday_items, tuesday_items, wednesday_items, thursday_items, friday_items, saturday_items, sunday_items)

            print(week_table)

        elif tasks_only and not notes_only:

            week = get_current_week()
            file_path = get_vault_path()

            week_table = Table('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

            monday_items = Table('Task')
            tuesday_items = Table('Task')
            wednesday_items = Table('Task')
            thursday_items = Table('Task')
            friday_items = Table('Task')
            saturday_items = Table('Task')
            sunday_items = Table('Task')

            day_list = [monday_items, tuesday_items, wednesday_items, thursday_items, friday_items, saturday_items, sunday_items]

            with open(file_path, 'r') as file:
                data = json.load(file)
                if week is not None:
                    for i in range(0, 6):
                        if week[i] in data:
                            for item in data[week[i]]:
                                day_list[i].add_row(item['task'])
                else:
                    print('Error fetching week list')

            week_table.add_row(monday_items, tuesday_items, wednesday_items, thursday_items, friday_items, saturday_items, sunday_items)

            print(week_table)

        elif not tasks_only and notes_only:

            week = get_current_week()
            file_path = get_vault_path()

            week_table = Table('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

            monday_items = Table('Note')
            tuesday_items = Table('Note')
            wednesday_items = Table('Note')
            thursday_items = Table('Note')
            friday_items = Table('Note')
            saturday_items = Table('Note')
            sunday_items = Table('Note')

            day_list = [monday_items, tuesday_items, wednesday_items, thursday_items, friday_items, saturday_items, sunday_items]

            with open(file_path, 'r') as file:
                data = json.load(file)
                if week is not None:
                    for i in range(0, 6):
                        if week[i] in data:
                            for item in data[week[i]]:
                                day_list[i].add_row(item['note'])
                else:
                    print('Error fetching week list')

            week_table.add_row(monday_items, tuesday_items, wednesday_items, thursday_items, friday_items, saturday_items, sunday_items)

            print(week_table)

        else:
            print("Command Error. Try rem show --help for more info")


    elif not tomorrow and not curr_week and specific_date and not all and not undated_only:
        if not tasks_only and not notes_only:

            parsed_date = str(parse(specific_date).date())
            file_path = get_vault_path()

            big_table = Table(f"Tasks & Notes for {parsed_date}")
            date_diff = get_date_diff(curr_date, specific_date)
            table_items = Table("Task", "Note", f"{date_diff} days remaining")

            with open(file_path, 'r') as file:
                data = json.load(file)

                if parsed_date in data:
                    for item in data[parsed_date]:
                        table_items.add_row(item['task'], item['note'], '')
                    else:
                        print('No tasks or notes for given date')

            big_table.add_row(table_items)

            print(big_table)

        elif tasks_only and not notes_only:

            parsed_date = str(parse(specific_date).date())
            file_path = get_vault_path()

            big_table = Table(f"Tasks & Notes for {parsed_date}")
            date_diff = get_date_diff(curr_date, specific_date)
            table_items = Table("Task", f"{date_diff} days remaining")

            with open(file_path, 'r') as file:
                data = json.load(file)

                if parsed_date in data:
                    for item in data[parsed_date]:
                        table_items.add_row(item['task'], '')
                    else:
                        print('No tasks or notes for given date')

            big_table.add_row(table_items)

            print(big_table)

        elif not tasks_only and notes_only:

            parsed_date = str(parse(specific_date).date())
            file_path = get_vault_path()

            big_table = Table(f"Tasks & Notes for {parsed_date}")
            date_diff = get_date_diff(curr_date, specific_date)
            table_items = Table("Note", f"{date_diff} days remaining")

            with open(file_path, 'r') as file:
                data = json.load(file)

                if parsed_date in data:
                    for item in data[parsed_date]:
                        table_items.add_row(item['note'], '')
                    else:
                        print('No tasks or notes for given date')

            big_table.add_row(table_items)

            print(big_table)

        else:
            print("Command Error. Try rem show --help for more info")


    elif not tomorrow and not curr_week and not specific_date and all and not undated_only:
        if not tasks_only and not notes_only:

            file_path = get_vault_path()
            big_table = Table("All tasks and notes")
            table_items = Table("Task", "Note", "Date", "Days Remaining")

            with open(file_path, 'r') as file:
                data = json.load(file)

                for item in data:
                    if item == "undated":
                        for entry in data['undated']:
                            table_items.add_row(entry['task'], entry['note'], 'Undated', 'Undated')
                    else:
                        for entry in data[item]:
                            table_items.add_row(entry['task'], entry['note'], entry['date'], f'{get_date_diff(curr_date, entry['date'])} days remaining')
                else:
                    print('No tasks or notes for given date')

            big_table.add_row(table_items)

            print(big_table)

        elif tasks_only and not notes_only:

            file_path = get_vault_path()
            big_table = Table("All tasks and notes")
            table_items = Table("Task", "Date", "Days Remaining")

            with open(file_path, 'r') as file:
                data = json.load(file)

                for item in data:
                    if item == "undated":
                        for entry in data['undated']:
                            table_items.add_row(entry['task'], 'Undated', 'Undated')
                    else:
                        for entry in data[item]:
                            table_items.add_row(entry['task'], entry['date'], f'{get_date_diff(curr_date, entry['date'])} days remaining')
                else:
                    print('No tasks or notes for given date')

            big_table.add_row(table_items)

            print(big_table)

        elif not tasks_only and notes_only:

            file_path = get_vault_path()
            big_table = Table("All tasks and notes")
            table_items = Table("Note", "Date", "Days Remaining")

            with open(file_path, 'r') as file:
                data = json.load(file)

                for item in data:
                    if item == "undated":
                        for entry in data['undated']:
                            table_items.add_row(entry['note'], 'Undated', 'Undated')
                    else:
                        for entry in data[item]:
                            table_items.add_row(entry['note'], entry['date'], f'{get_date_diff(curr_date, entry['date'])} days remaining')
                else:
                    print('No tasks or notes for given date')

            big_table.add_row(table_items)

            print(big_table)

        else:
            print("Error")


    elif not tomorrow and not curr_week and not specific_date and not all and undated_only:
        if not tasks_only and not notes_only:

            file_path = get_vault_path()
            big_table = Table("Undated tasks and notes")
            table_items = Table("Task", "Note")

            with open(file_path, 'r') as file:
                data = json.load(file)


            for entry in data['undated']:
                    table_items.add_row(entry['task'], entry['note'])


            big_table.add_row(table_items)

            print(big_table)

        elif tasks_only and not notes_only:

            file_path = get_vault_path()
            big_table = Table("Undated tasks")
            table_items = Table("Task")

            with open(file_path, 'r') as file:
                data = json.load(file)


            for entry in data['undated']:
                    table_items.add_row(entry['task'])


            big_table.add_row(table_items)

            print(big_table)

        elif not tasks_only and notes_only:

            file_path = get_vault_path()
            big_table = Table("Undated notes")
            table_items = Table("Note")

            with open(file_path, 'r') as file:
                data = json.load(file)


            for entry in data['undated']:
                    table_items.add_row(entry['note'])


            big_table.add_row(table_items)

            print(big_table)

        else:
            print("Error")


@app.command(help="Remove all older tasks with dates")
def clean(
    all: Annotated[bool, typer.Option('--all', help='Clean the entire vault including undated items')] = False,
    undated: Annotated[bool, typer.Option('--undated', help='Clean only undated items from the vault')] = False
):

    if all:

        json_obj = {
            'undated' : []
        }

        file_path = get_vault_path()

        with open(file_path, 'w') as file_write:
            json.dump(json_obj, file_write, indent=4)

        print('Vault cleaned!')

    elif undated:

        check = False
        file_path = get_vault_path()
        with open(file_path, 'r') as file:
            data = json.load(file)

            if data['undated'] != []:

                check = True
                data['undated'] = []

        with open(file_path, 'w') as file_write:
            json.dump(data, file_write, indent=4)

        if check:
            print('Vault cleaned!')
        else:
            print('No undated items found. Vault already clean!')

    else:
        json_obj = ''
        check = False
        file_path = get_vault_path()
        with open(file_path, 'r') as file:
            data = json.load(file)
            data_copy = data.copy()

            for item in data:
                if item != 'undated' and get_date_diff(curr_date, f'{item}') < 0:
                    check = True
                    del data_copy[item]
                json_obj = data_copy

        with open(file_path, 'w') as file_write:
            json.dump(json_obj, file_write, indent=4)

        if check:
            print('Vault cleaned!')
        else:
            print('Vault already clean! No older tasks found.')
