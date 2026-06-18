# 🔔 Vishwa Push Bot

> Free, serverless YouTube notification bot — powered by GitHub Actions. No VPS. No server. No monthly cost. Just fork and go.

![GitHub stars](https://img.shields.io/github/stars/vishwajeetsahani/vishwa-push-bot-offical?style=flat-square&logo=github)
![GitHub forks](https://img.shields.io/github/forks/vishwajeetsahani/vishwa-push-bot-offical?style=flat-square&logo=github)
![GitHub issues](https://img.shields.io/github/issues/vishwajeetsahani/vishwa-push-bot-offical?style=flat-square)
![GitHub Actions](https://img.shields.io/github/actions/workflow/status/vishwajeetsahani/vishwa-push-bot-offical/notify.yml?style=flat-square&label=bot%20status)
![License](https://img.shields.io/github/license/vishwajeetsahani/vishwa-push-bot-offical?style=flat-square)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)

---

## ✨ What is this?

**Vishwa Push Bot** monitors your favorite YouTube channels and instantly sends notifications to Discord and Telegram whenever a new video is uploaded — completely free, with zero server setup.

It runs automatically every 15 minutes using GitHub Actions, which gives you 2,000 free minutes per month (more than enough).

```
YouTube Channel uploads a video
         ↓
GitHub Actions detects it (every 15 min)
         ↓
Sends notification to Discord + Telegram
         ↓
         ✅ Done
```

---

## 🆚 Why Vishwa Push Bot?

| Feature | Vishwa Push Bot | VPS Bot | Paid Services |
|---|---|---|---|
| Free to use | ✅ | ❌ | ❌ |
| No server needed | ✅ | ❌ | ✅ |
| Discord support | ✅ | ✅ | ✅ |
| Telegram support | ✅ | ✅ | ✅ |
| Open source | ✅ | ✅ | ❌ |
| Beginner friendly | ✅ | ❌ | ✅ |
| Multi-server routing | ✅ | ❌ | ❌ |
| Monthly cost | **₹0** | ₹300–1000+ | ₹200–2000+ |

---

## 🚀 Features

- 📺 **Monitor unlimited YouTube channels** — add as many as you want
- 💬 **Multiple Discord webhooks** — route different channels to different Discord servers
- 📱 **Telegram support** — optional Telegram notifications
- 🗂️ **Group routing** — send Hindi channels to one server, English to another
- 🔁 **Duplicate prevention** — never see the same notification twice
- ⚡ **Runs every 15 minutes** — near real-time alerts
- 🆓 **Completely free** — uses GitHub Actions free tier
- 👶 **Beginner friendly** — no coding knowledge required
- 🔓 **Open source** — fork, modify, and use however you want

---

## ⚡ Quick Start (5 minutes)

### Step 1 — Fork this repository

Click the **"Use this template"** button at the top of this page and create your own copy.

> ⚠️ Do not just fork — use **"Use this template"** so you get a clean copy without commit history.

### Step 2 — Add your secrets

Go to your repository → **Settings → Secrets and variables → Actions → New repository secret**

| Secret Name | Required | Description |
|---|---|---|
| `DISCORD_WEBHOOK` | ✅ Yes | Your main Discord webhook URL |
| `DISCORD_WEBHOOK_ENGLISH` | ❌ Optional | Second webhook for English group |
| `TELEGRAM_TOKEN` | ❌ Optional | Your Telegram bot token |
| `TELEGRAM_CHAT_ID` | ❌ Optional | Your Telegram channel/chat ID |

**How to get a Discord Webhook URL:**
1. Open Discord → Server Settings → Integrations → Webhooks
2. Click "New Webhook" → Copy the webhook URL

**How to get a Telegram Bot Token:**
1. Open Telegram → search `@BotFather`
2. Send `/newbot` and follow the instructions
3. Copy the token it gives you

### Step 3 — Add your YouTube channels

Edit the `channels.json` file in your repository:

```json
{
  "channels": [
    {
      "id": "UCxxxxxxxxxxxxxxxxxxxxxx",
      "name": "MrBeast",
      "group": "english"
    },
    {
      "id": "UCyyyyyyyyyyyyyyyyyyyyyy",
      "name": "CarryMinati",
      "group": "hindi"
    }
  ]
}
```

**How to find a YouTube Channel ID:**
- Go to the channel's YouTube page
- Click "More" → "About" → scroll to the bottom and copy the Channel ID
- Or use [commentpicker.com/youtube-channel-id.php](https://commentpicker.com/youtube-channel-id.php)

### Step 4 — Enable GitHub Actions

Go to your repository → **Actions tab** → Click **"I understand my workflows, go ahead and enable them"**

### Step 5 — Done! 🎉

The bot will now check for new videos every 15 minutes automatically. You can also trigger it manually by going to **Actions → YouTube Notification Bot → Run workflow**.

---

## 📁 Repository Structure

```
vishwa-push-bot/
├── .github/
│   └── workflows/
│       └── notify.yml          # GitHub Actions schedule config
│
├── config/
│   ├── channels.json           # ✏️  Edit this — your channels list
│   └── channels.example.json   # Reference example
│
├── src/
│   ├── main.py                 # Main bot logic
│   ├── youtube.py              # YouTube feed fetcher
│   ├── discord_notify.py       # Discord notification sender
│   ├── telegram_notify.py      # Telegram notification sender
│   └── utils.py                # Helpers and logging
│
├── data/
│   └── last_videos.json        # Auto-managed — don't edit this
│
├── channels.json               # ✏️  Quick-access copy (root level)
├── requirements.txt
└── README.md
```

---

## ⚙️ Configuration

### `channels.json` reference

```json
{
  "channels": [
    {
      "id": "UCxxxxxxxxxxxxxxxxxxxxxx",   // YouTube Channel ID (required)
      "name": "Channel Display Name",     // For your reference in logs
      "group": "hindi",                   // Group name for routing (required)
      "enabled": true                     // Set false to pause this channel
    }
  ]
}
```

### Group routing

Groups let you send notifications from different channels to different Discord servers. Map each group to a secret name in your workflow:

| Group Name | Secret Used |
|---|---|
| `hindi` | `DISCORD_WEBHOOK` |
| `english` | `DISCORD_WEBHOOK_ENGLISH` |
| `custom` | `DISCORD_WEBHOOK_CUSTOM` (add your own) |

To add a new group, add a new secret in GitHub and update the workflow in `.github/workflows/notify.yml`.

---

## 🔧 Notification Format

Discord notifications look like this:

```
🎥 New video from CarryMinati!

Title: Ek Villain Returns — My Reaction
🔗 https://youtube.com/watch?v=xxxxxxxxxx
```

Telegram notifications use the same format with Markdown formatting.

---

## ⚠️ Important Note

GitHub Actions scheduled workflows are not guaranteed to run exactly every 15 minutes.

GitHub may delay scheduled jobs during platform load.

For mission-critical notifications, cron-job.org can be used as an external trigger.

## 🛠️ Troubleshooting

**Bot is not sending notifications**
- Check that GitHub Actions is enabled in the Actions tab
- Verify your secrets are correctly named (no extra spaces)
- Check the Action logs: Actions → click on the latest run → view output
- Make sure the Channel ID is correct, not the channel handle (`@name`)

**Getting duplicate notifications**
- Check that `data/last_videos.json` is being committed back to the repo after each run
- Look at the Action logs for any commit errors

**Discord notifications not arriving**
- Double-check the webhook URL — paste it in a browser and you should see a JSON response
- Make sure the webhook still exists in Discord (they can be deleted)
- Confirm the secret name matches exactly: `DISCORD_WEBHOOK` (all caps, underscore)

**Telegram notifications not arriving**
- Make sure your bot has been started — send `/start` to your bot first
- For channels, the bot must be added as an admin
- The `TELEGRAM_CHAT_ID` for channels starts with `-100`

**GitHub Actions ran but nothing happened**
- This is normal if no new videos were uploaded since the last check. Check the logs — it should say "No new videos found."

---

## ❓ FAQ

**Is this really free?**
Yes. GitHub Actions gives you 2,000 free minutes/month on public repositories. This bot uses about 200–300 minutes/month even with 20+ channels.

**Can I monitor a channel that isn't mine?**
Yes, you can monitor any public YouTube channel. Just add their Channel ID.

**How often does it check?**
Every 15 minutes. This is the minimum interval GitHub Actions allows for scheduled workflows.

**Will it notify me about YouTube Shorts?**
Yes, by default. Shorts filtering is on the roadmap for a future release.

**What happens if GitHub Actions goes down?**
You might miss a notification window. The bot will resume normally on the next run and won't send duplicates for already-seen videos.

**Can I add more than 2 Discord servers?**
Yes — add more secrets and update `notify.yml` to route additional groups.

**Does this work with private/unlisted videos?**
No. Only public videos are detectable via the YouTube RSS feed.

---

## 🔓 Why Open Source?

Unlike paid notification services, Vishwa Push Bot puts you in full control.

- **You own your data** — no third party stores your tokens or channel list
- **Modify anything** — add features, change formats, route to more services
- **No lock-in** — no subscription, no account, no vendor that can shut down
- **Community driven** — bug fixes and features come from real users like you

---

## 🗺️ Roadmap

| Version | Status | Description |
|---|---|---|
| V1 | ✅ Current | Open-source GitHub Template — free, serverless |
| V2 | 🔜 Planned | GitHub Pages setup wizard — generate config visually |
| V3 | 💭 Future | Full SaaS dashboard — manage everything from a web UI |

### Upcoming Features

| Feature | Status |
|---|---|
| YouTube Shorts filtering | 🔜 Planned |
| Keyword-based filtering | 🔜 Planned |
| Discord embeds with thumbnails | 🔜 Planned |
| Role ping support | 🔜 Planned |
| Email notifications | 💭 Idea |
| GitHub Pages setup wizard | 💭 Idea |
| Analytics dashboard | 💭 Idea |

Have a feature idea? [Open an issue](../../issues/new) — we read everything.

---

## 🤝 Contributing

Contributions are welcome! Whether it's a bug fix, new feature, or documentation improvement.

1. Fork the repo
2. Create your branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add my feature'`
4. Push: `git push origin feature/my-feature`
5. Open a Pull Request

Please read `CONTRIBUTING.md` for guidelines.

---

## 🔒 Security

- Never put webhook URLs or tokens directly in `channels.json` or any file in the repo
- Always use GitHub Secrets for sensitive values
- If you accidentally expose a secret, rotate it immediately (regenerate the Discord webhook, revoke the Telegram token)

Found a security issue? Please report it privately rather than opening a public issue.

---

## 💡 Suggestions & Feedback

| | |
|---|---|
| 🐛 Found a bug? | [Create a Bug Report](../../issues/new?template=bug_report.md) |
| 💡 Have an idea? | [Create a Feature Request](../../issues/new?template=feature_request.md) |
| 🙋 Have a question? | [Start a Discussion](../../discussions) |

Community contributions are always welcome.

---

## ❤️ Support The Project

If this bot saves you time, consider:

- ⭐ **Star the repository** — helps others discover it
- 🍴 **Fork and build** — extend it for your own needs
- 📢 **Share it** — with other creators who need free notifications
- 🐛 **Report bugs** — help make it better for everyone
- 💡 **Suggest features** — shape the roadmap

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

You're free to use, modify, and distribute this for any purpose, including commercial use.

---

<div align="center">
  Made with ❤️ for the creator community<br>
  <a href="../../issues/new?template=bug_report.md">Report a bug</a> · 
  <a href="../../issues/new?template=feature_request.md">Request a feature</a> · 
  <a href="../../discussions">Join the discussion</a>
</div>
