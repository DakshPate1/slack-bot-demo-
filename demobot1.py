import os
from slack_bolt import App
import requests
from pathlib import Path
from dotenv import load_dotenv


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = App(token=os.environ["SLACK_BOT_TOKEN"])

@app.command("/getconvo")
def get_convo_command(ack, body, logger):
    channel_id = body["channel_id"]
    thread_ts = body["text"]
    logger.info(f"Received command to get conversation history of thread {thread_ts} in channel {channel_id}")

    # Fetch the conversation history
    conversation_history = app.client.conversations_history(
        token=os.environ["SLACK_BOT_TOKEN"],
        channel=channel_id,
        latest=thread_ts,
        inclusive=True,
        limit=1000
    )

    # Extract the messages from the conversation history
    messages = conversation_history["messages"]

    # Convert the messages to a string
    message_string = "\n".join([message["text"] for message in messages])

    # Send the message string to the API endpoint
    url = "http://127.0.0.1:5000/api"
    payload = {"messages": message_string}
    response = requests.post(url, json=payload)

    # Display the response from the API endpoint
    if response.status_code == 200:
        ack(f"Conversation history of thread {thread_ts} in channel {channel_id} sent to API endpoint")
    else:
        ack("Failed to send conversation history to API endpoint")

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 5000)))
