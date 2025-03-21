
<p align="center">
  <img src="https://3684636823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAAWXLgBhsxb38Q3iF3ha%2Fsocialpreview%2FJYYwVSNx9yLnXY8adfAU%2Fbanner.png?alt=media&token=264b3ce3-6643-4b55-8990-ca5cd2516dce">
</p>

<h1 align="center">[Discord] - SelfBot (V2.1)</h1>
<p align="center">
  <a href="https://github.com/AstraaDev/Discord-SelfBot/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-important">
  </a>
  <a href="https://github.com/AstraaDev">
    <img src="https://img.shields.io/github/repo-size/AstraaDev/Discord-SelfBot.svg?label=Repo%20size&style=flat-square">
  </a>
</p>

<p align="center">
  [Discord] - SelfBot is a feature-rich script designed for Windows, Linux, and macOS, written in Python.
</p>

This SelfBot provides a large variety of commands to streamline your Discord experience. It features an intuitive interface, complete help documentation, and updates to keep it functional and efficient. Some unnecessary commands have been removed, but you are welcome to suggest additions via issues or Discord.

---

## Features

<details>
  <summary>All Commands</summary>

`*astraa` - Show my social networks.  
`changeprefix <prefix>` - Change the bot's prefix.  
`shutdown` - Stop the selfbot.  
`*uptime` - Returns how long the selfbot has been running.  
`*remoteuser <@user>` - Authorize a user to execute commands remotely.  
`copycat ON|OFF <@user>` - Automatically reply with the same message whenever the mentioned user speaks.  
`*ping` - Returns the bot's latency.  
`*pingweb <url>` - Ping a website and return the HTTP status code (e.g., 200 if online).  
`*geoip <ip>` - Looks up the IP's location.  
`*tts <text>` - Converts text to speech and sends an audio file (.wav).  
`*qr <text>` - Generate a QR code from the provided text and send it as an image.  
`*hidemention <message>` - Hide messages inside other messages.  
`*edit <message>` - Move the position of the (edited) tag.  
`*reverse <message>` - Reverse the letters of a message.  
`*gentoken` - Generate an invalid but correctly patterned token.  
`*hypesquad <house>` - Change your HypeSquad badge.  
`*nitro` - Generate a fake Nitro code.  
`*whremove <webhook_url>` - Remove a webhook.  
`*purge <amount>` - Delete a specific number of messages.  
`clear` - Clear messages from a channel.  
`*cleardm <amount>` - Delete all DMs with a user.  
`*spam <amount> <message>` - Spams a message for a given amount of times.  
`*quickdelete <message>` - Send a message and delete it after 2 seconds.  
`*autoreply <ON|OFF>` - Enable or disable automatic replies.  
`*afk <ON/OFF>` - Enable or disable AFK mode. Sends a custom message when receiving a DM or being mentioned.  
`*fetchmembers` - Retrieve the list of all members in the server.  
`*dmall <message>` - Send a message to all members in the server.  
`firstmessage` - Get the link to the first message in the current channel.  
`sendall <message>` - Send a message to all channels in the server.  
`*guildicon` - Get the icon of the current server.  
`*usericon <@user>` - Get the profile picture of a user.  
`*guildbanner` - Get the banner of the current server.  
`*tokeninfo <token>` - Scrape info with a token.  
`*guildinfo` - Get information about the current server.  
`*guildrename <new_name>` - Rename the server.  
`playing <status>` - Set the bot's activity status as "Playing".  
`watching <status>` - Set the bot's activity status as "Watching".  
`stopactivity` - Reset the bot's activity status.  
`ascii <message>` - Convert a message to ASCII art.  
`*airplane` - Sends a 9/11 attack (warning: use responsibly).  
`*dick <@user>` - Show the "size" of a user's dick.  
`*minesweeper <width> <height>` - Play a game of Minesweeper with custom grid size.  
`*leetpeek <message>` - Speak like a hacker, replacing letters.  

</details>

---

## How To Setup/Install

1. **Update `config/config.json`**: Enter your bot token and preferred prefix.
```json
{
  // Your Discord bot token, required to log in to the bot account
  "token": "TOKEN-HERE",
  // Prefix used to trigger bot commands (e.g., "*help")
  "prefix": "PREFIX-HERE",
  // List of user IDs that the bot will listen to for remote command execution
  "remote-users": ["USER-ID-1", "USER-ID-2"],
  
  // Auto-reply configuration for messages, channels, and specific users
  "autoreply": {
    // List of messages that the bot will use to auto-reply
    "messages": [
      "https://github.com/AstraaDev/Discord-SelfBot",
      "https://discord.gg/PKR7nM9j9U"
    ],
    // Channels where the bot will enable auto-reply functionality
    "channels": ["CHANNEL-ID-1", "CHANNEL-ID-2"],
    // Users for whom the bot will reply automatically
    "users": ["USER-ID-1", "USER-ID-2"]
  },  
  
  // AFK (Away From Keyboard) mode configuration
  "afk": {
    // Whether AFK mode is enabled or disabled
    "enabled": false,
    // The message that the bot will send when AFK is enabled
    "message": "I am currently AFK. I will respond as soon as possible!"
  },
    // Copycat
    "copycat": {
      // Copycat user
        "users": []
    }
}
```

2. **Installation**:
- **Automated**: Run `setup.bat`. Launch the new file created.
- **Manual**:
  ```bash
  $ git clone https://github.com/AstraaDev/Discord-SelfBot.git
  $ python -m pip install -r requirements.txt
  $ python main.py
  ```

---

## Command Execution via Remote User

This SelfBot supports executing commands remotely if you are listed in the `remote-users` array in `config/config.json`. You can manage the list of remote users using the `remoteuser` command.

### Example
1. Add your Discord user ID to `remote-users` in the configuration file, or use the `*remoteuser ADD @user(s)` command to add users to the list.
2. From another account, type `*help` (assuming `*` is the prefix). If you are in the list, you can execute commands.
3. You can also remove users from the list with `*remoteuser REMOVE @user(s)`.

This allows for greater flexibility in managing who can control the bot remotely.

---

## Autoreply Command

The `autoreply` command lets you set up automatic responses in specific channels or for specific users.

### Usage
- **Enable autoreply in a channel**: `autoreply ON`
  - Automatically sends preconfigured messages when someone messages in the channel.
- **Disable autoreply in a channel**: `autoreply OFF`
  - Stops automatic replies in the channel.
- **Enable autoreply for a user**: `autoreply ON @user`
  - Sends automatic replies to all messages from the specified user, regardless of the channel or DM.
- **Disable autoreply for a user**: `autoreply OFF @user`

### Configuration
Messages, channels, and users for autoreply are stored in `config/config.json`:
```json
{
  "messages": [
    "https://github.com/AstraaDev/Discord-SelfBot",
    "https://discord.gg/PKR7nM9j9U"
  ],
  "channels": ["123456789012345678"],
  "users": ["112233445566778899"]
}
```

---

## Additional Information
- Need help? Join the [Discord Server](https://astraadev.github.io/#/discord).
- Contributions are welcome! Open an issue or create a pull request.

---

## Credits
This project is a restructured and improved version of the original [@humza1400](https://github.com/humza1400) SelfBot (2019).
