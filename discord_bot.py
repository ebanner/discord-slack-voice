import discord
from slack_sdk import WebClient

# Replace 'YOUR_TOKEN' with your actual Slack OAuth token
slack_token = 'TOKEN HERE'
channel_id = 'general'  # Replace with the ID of your Slack channel

slack_client = WebClient(token=slack_token)

def send_message_slack(message):
    print(message)
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

def get_users(channel_name):
    guild = discord_client.guilds[0]  # Assuming the bot is only in one guild
    voice_channel = discord.utils.get(guild.voice_channels, name=channel_name)

    if voice_channel:
        members = voice_channel.members

        if members:
            users = [member.name for member in members]
        else:
            users = []
    else:
        raise Exception(f'Voice channel {channel_name} not found')

    return users

@discord_client.event
async def on_voice_state_update(member, before, after):
    if not before.channel and after.channel:
        channel_name = after.channel.name
        user_name = member.name
        users = get_users('Space')
        num_users = len(users)
        user_list = '\n'.join(f'* {user}' for user in users)
        message = f"""💥 {user_name} entered the <https://discord.gg/MrFpvbmc|awakened bros Space channel> on discord

{num_users} member currently in the space

{user_list}"""
    elif before.channel and not after.channel:
        user_name = member.name
        users = get_users('Space')
        num_users = len(users)
        user_list = '\n'.join(f'* {user}' for user in users)
        message = f"""💥 {user_name} left the <https://discord.gg/MrFpvbmc|awakened bros Space channel> on discord

{num_users} member currently in the space

{user_list}"""

    send_message_slack(message)

discord_client.run(TOKEN)