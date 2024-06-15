import os
import argparse
from dotenv import load_dotenv
from history import get_last_command, execute_command
from query import query_ai


def main():
    parser = argparse.ArgumentParser(description="Execute the last command and query AI for explanation and troubleshooting.")
    parser.add_argument('--files', nargs='*', help='List of file names to include in the prompt.')
    args = parser.parse_args()

    last_command = get_last_command()
    if last_command:
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        stdout, stderr = execute_command(last_command)

        file_contents = ""
        file_paths = []
        if args.files:
            for file_name in args.files:
                full_path = os.path.abspath(file_name)
                file_paths.append(full_path)
                if os.path.exists(full_path):
                    with open(full_path, 'r') as file:
                        file_contents += f"\nContents of {full_path}:\n{file.read()}\n"
                else:
                    file_contents += f"\n{full_path} not found.\n"        

        prompt = f"Command: {last_command}\nOutput:\n{stdout}\nError:\n{stderr}\n{file_contents}"
        response = query_ai(prompt, api_key)
        print(f"Command: {last_command}\nOutput:\n{stdout}\nError:\n{stderr}\n\nFile Paths:\n{file_paths}\n\nResponse:")
        print(response)
    else:
        print("No command found in history.")

if __name__ == "__main__":
    main()