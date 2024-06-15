from history import get_last_command, execute_command
from query import query_ai

def main():
    api_key = "your_openai_api_key"  # Replace with your actual API key
    last_command = get_last_command()
    if last_command:
        print(f"Last Command: {last_command}")
        stdout, stderr = execute_command(last_command)
        prompt = f"Command: {last_command}\nOutput:\n{stdout}\nError:\n{stderr}\n\nResponse:"
        response = query_ai(prompt, api_key)
        print(f"AI Response: {response}")
    else:
        print("No command found in history.")

if __name__ == "__main__":
    main()