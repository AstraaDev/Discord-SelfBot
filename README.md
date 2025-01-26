
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

## Disclaimer

| This SelfBot is intended for **educational purposes** only. |
|-------------------------------------------------------------|
By using this SelfBot, you agree that you are responsible for any consequences resulting from its use.

---

## Features

<details>
  <summary>General Commands</summary>

```
- help <category>
- ping
- uptime
- autoreply ON|OFF [@user]
```
</details>

<details>
  <summary>Useful Commands</summary>

```
- astraa
- geoip <ip>
- pingweb <website-url>
- gentoken <user>
- quickdelete <message>
- usericon <@user>
- rolecolor <role>
```
</details>

<details>
  <summary>ATIO Commands</summary>

```
- tokeninfo <token>
- cleardm <amount>
- hypesquad <house>
- serverinfo
- nitro
- webhookremove <webhook>
```
</details>

<details>
  <summary>Exploit Commands</summary>

```
- hide <display> <hidden>
- edit <message>
```
</details>

<details>
  <summary>Fun Commands</summary>

```
- 9/11
- cum
- minesweeper <grid size>
- 1337 <message>
- dick <user>
- reverse <message>
```
</details>

<details>
  <summary>Server Commands</summary>

```
- fetchmembers
- spam <amount>
- guildicon
- guildbanner
- guildname <name>
- purge <amount>
```
</details>

<details>
  <summary>Meme Commands</summary>

```
- shrug
- lenny
- fliptable
- unflip
- empty
```
</details>

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
Messages, channels, and users for autoreply are stored in `config/autoreply-config.json`:
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
- **messages**: List of responses to cycle through.
- **channels**: Channels where autoreply is active.
- **users**: Users for whom autoreply is active.

### Example
In Channel 1, if the bot sends the first message, it will send the second and third messages sequentially. Switching to Channel 2 restarts the cycle from the first message.

---

## How To Setup/Install

1. **Update `config/config.json`**: Enter your bot token and preferred prefix.
```json
{
    "token": "TOKEN-HERE",
    "prefix": "PREFIX-HERE"
}
```

2. **Installation**:
- **Automated**: Run `setup.bat`. Launch the new file created.
- **Manual**:
  ```bash
  $ git clone https://github.com/AstraaDev/Discord-SelfBot.git
  $ python -m pip install -r requirements.txt
  $ python selfbot.py
  ```

---

## Example
<img src="https://cdn.discordapp.com/attachments/1079127307656122501/1326253525541326848/image.png?ex=67972519&is=6795d399&hm=97739a0ffa2dc302a8b966e32f5223abaec8dc9814e530d0ec4ed18cfdf53037&" alt="SelfBot Example" width="400">

---

## Additional Information
- Need help? Join the [Discord Server](https://discord.gg/PKR7nM9j9U).
- Contributions are welcome! Open an issue or create a pull request.

---

## Credits
This project is a restructured and improved version of the original [@humza1400](https://github.com/humza1400) SelfBot (2019).

