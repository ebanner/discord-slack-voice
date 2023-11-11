import discord
from slack_sdk import WebClient

# Replace 'YOUR_TOKEN' with your actual Slack OAuth token
slack_token = 'TOKEN HERE'
channel_id = 'general'  # Replace with the ID of your Slack channel

slack_client = WebClient(token=slack_token)

def send_message_slack(message):
    # Send a simple text message to the specified channel
    response = slack_client.chat_postMessage(
        channel=channel_id,
        text=message,
    )

    # Check if the message was sent successfully
    if response['ok']:
        print(f"Message sent to {channel_id}")
    else:
        print(f"Failed to send message. Error: {response['error']}")


TOKEN = 'TOKEN HERE'

intents = discord.Intents.default()
intents.all()
discord_client = discord.Client(intents=intents)

@discord_client.event
async def on_ready():
    print('Ready!')

@discord_client.event
async def on_voice_state_update(member, before, after):
    if not before.channel and after.channel:
        channel_name = after.channel.name
        user_name = member.name

        message = f"""💥 {user_name} entered Voice channel <https://discord.gg/fNAgExjG|on discord>"""
        send_message_slack(message)

discord_client.run(TOKEN)