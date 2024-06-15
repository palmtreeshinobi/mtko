import os

def setup_env():
    proceed = input("Do you want to create or overwrite the .env file with your OpenAI API key? (y/n): ").strip().lower()

    if proceed == 'y':
        api_key = input("Please enter your OpenAI API key: ")
        env_content = f"OPENAI_API_KEY={api_key}\n"

        with open(".env", "w") as env_file:
            env_file.write(env_content)
        
        print(".env file created with your API key.")
    else:
        print("Operation cancelled. You can manually update the .env.example file later.")

if __name__ == "__main__":
    setup_env()
