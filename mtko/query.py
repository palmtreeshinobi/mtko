from openai import OpenAI

# Function to query AI
def query_ai(prompt, api_key):

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
            "role": "system",
            "content": "You will be provided with a command executed in a terminal, and the output of the command. Your job is to explain the command/output and troubleshoot any error messages."
            },
            {
            "role": "user",
            "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=256,
        top_p=1
    )
    return response.choices[0].message.content.strip()