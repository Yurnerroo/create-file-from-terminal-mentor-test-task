import os
from datetime import datetime
from sys import argv
from os import mkdir, chdir


def parse_args(command_line_args: list) -> tuple:
    filename: str = ""
    directories = list()

    if "-f" in command_line_args:
        index = command_line_args.index("-f")
        filename = command_line_args[index + 1]

    if "-d" in command_line_args:
        index = command_line_args.index("-d")
        if "-f" in command_line_args:
            directories = command_line_args[index + 1: command_line_args.index("-f")]
        else:
            directories = command_line_args[index + 1: -1]
            filename = command_line_args[-1]

    return filename, directories


def get_file_data() -> list:
    file_data: list = [datetime.now().strftime("%Y-%d-%m %H:%M:%S"), "\n"]
    row_index = 1

    while True:
        line = input("Enter content line: ")
        if line == "exit":
            break
        file_data.extend([f"{row_index} ", line, "\n"])
        row_index += 1

    return file_data


def create_directories(directories: list) -> None:
    for directory in directories:
        try:
            mkdir(path=directory)
        except (FileExistsError, PermissionError, OSError):
            pass
        chdir(path=directory)


def write_file(filename: str, file_data: list) -> None:
    mode = "a" if os.path.exists(path=filename) else "w"
    with open(file=filename, mode=mode) as f:
        if mode == "a":
            f.write("\n")
        f.writelines(file_data)


def main(command_line_args: list) -> None:
    filename, directories = parse_args(command_line_args=command_line_args)
    file_data: list = get_file_data()
    create_directories(directories=directories)
    write_file(filename=filename, file_data=file_data)


if __name__ == "__main__":
    main(command_line_args=argv)
