def create_env_file():

    proceed = input("Do you want to overwrite the .env.example file with your OpenAI API key? You can manually update .env.example later. (y/n): ").strip().lower()

    if proceed == 'y':
        api_key = input("Please enter your OpenAI API key: ")
        env_content = f"OPENAI_API_KEY={api_key}\n"

        with open(".env", "w") as env_file:
            env_file.write(env_content)
        print(".env file created with your API key.")
    else:
        print("Operation cancelled. You can manually update the .env.example file later.")