import os

def setup_env():
    # Get the path to the directory where this script is located
    package_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(package_dir, '.env')

    proceed = input(f"Do you want to create or overwrite the .env file at {env_path} with your OpenAI API key? (y/n): ").strip().lower()

    if proceed == 'y':
        api_key = input("Please enter your OpenAI API key: ")
        env_content = f"OPENAI_API_KEY={api_key}\n"

        with open(env_path, "w") as env_file:
            env_file.write(env_content)
        
        print(f".env file created at {env_path} with your API key.")
    else:
        print("Operation cancelled. You can manually update the .env.example file later.")

if __name__ == "__main__":
    setup_env()
