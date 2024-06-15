import os
from dotenv import load_dotenv
from history import get_last_command, execute_command
from query import query_ai


def main():
    last_command = get_last_command()
    if last_command:
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        stdout, stderr = execute_command(last_command)
        prompt = f"Command: {last_command}\nOutput:\n{stdout}\nError:\n{stderr}\n\nResponse:"
        response = query_ai(prompt, api_key)
        print(f"Command: {last_command}\nOutput:\n{stdout}\nError:\n{stderr}\n\nResponse:")
        print(response)
    else:
        print("No command found in history.")

if __name__ == "__main__":
    main()