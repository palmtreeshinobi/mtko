import os
import subprocess

def get_last_command():
    # Ensure the history file is the Zsh history file
    history_file = os.path.expanduser("~/.zsh_history")

    with open(history_file, "r") as file:
        lines = file.readlines()

    # Extract only the commands, ignoring timestamps and other metadata
    commands = [line.split(';', 1)[-1].strip() for line in lines if ';' in line]
    last_command = commands[-2] if commands else None

    return last_command

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip(), result.stderr.strip()
    except subprocess.CalledProcessError as e:
        return e.stdout.strip(), e.stderr.strip()