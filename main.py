import json
import os
import requests
import feedparser

# Discord Webhooks
DISCORD_WEBHOOK_HINDI = os.getenv("DISCORD_WEBHOOK")
DISCORD_WEBHOOK_ENGLISH = os.getenv("DISCORD_WEBHOOK_ENGLISH")

# Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

print("Bot Started")

# Load Channels
with open("channels.json", "r", encoding="utf-8") as f:
    channels = json.load(f)["channels"]

# Load Previous Videos
try:
    with open("last_videos.json", "r", encoding="utf-8") as f:
        last_videos = json.load(f)
except:
    last_videos = {}

for channel in channels:

    channel_id = channel["id"]
    group = channel["group"]

    feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"

    print(f"Checking: {channel_id}")

    try:
        feed = feedparser.parse(feed_url)
    except Exception as e:
        print("Feed Error:", e)
        continue

    if not feed.entries:
        print("No Entries Found")
        continue

    latest = feed.entries[0]

    video_id = latest.yt_videoid
    title = latest.title
    link = latest.link
    channel_name = latest.author

    old_video = last_videos.get(channel_id)

    if old_video == video_id:
        print("Already Posted:", title)
        continue

    # Select Discord Webhook
    if group == "hindi":

        webhook = DISCORD_WEBHOOK_HINDI

        message = f"""@everyone

🔥 NAYI VIDEO UPLOAD HO GAYI 🔥

📺 Channel: {channel_name}

🎬 Title:
{title}

🔗 Watch Now:
{link}
"""

    else:

        webhook = DISCORD_WEBHOOK_ENGLISH

        message = f"""@everyone

🚨 NEW VIDEO UPLOADED 🚨

📺 Channel: {channel_name}

🎬 Title:
{title}

🔗 Watch Now:
{link}
"""

    print("Sending Discord Notification...")

    try:

        r = requests.post(
            webhook,
            json={
                "content": message,
                "allowed_mentions": {
                    "parse": ["everyone"]
                }
            },
            timeout=20
        )

        print("Discord Status:", r.status_code)

    except Exception as e:
        print("Discord Error:", e)

    print("Sending Telegram Notification...")

    try:

        r = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            data={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message
            },
            timeout=20
        )

        print("Telegram Status:", r.status_code)

    except Exception as e:
        print("Telegram Error:", e)

    last_videos[channel_id] = video_id

# Save Last Videos
with open("last_videos.json", "w", encoding="utf-8") as f:
    json.dump(last_videos, f, indent=4)

print("Done")
