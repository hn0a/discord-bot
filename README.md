
# Discord Bot

This Discord bot is a versatile bot featuring advanced moderation commands, automated role assignment, automatic responses, and a basic points system.

## Features

- **New Member Welcome**: Automatically welcomes new members to the server.
- **Advanced Moderation Commands**: Kick, Ban, and Delete messages.
- **Automated Role Assignment**:  Assign roles to users through commands.
- **Automatic Responses**: The bot responds automatically to specified keywords.
- **Points System**: A simple points system where members can earn points for participation, view their points, and add points to others.

## Installation

1. **Install Python**: Ensure Python is installed on your machine.

2. **Clone the Repository**: Download or clone this repository.

3. **Install Dependencies**:
   ```bash
   pip install discord.py python-dotenv
   ```

4. **Add Bot Token**:
   - Create a `.env` file in the same directory as `bot_discord.py`.
   - Add your Discord bot token to this file:
     ```
     TOKEN=your_token_here
     ```

## Usage

To run the bot, execute the `bot_discord.py` script from your terminal:
```bash
python bot_discord.py
```

## Commands

- `!kick <member> [reason]`: Kicks a member from the server.
- `!ban <member> [reason]`: Bans a member from the server.
- `!role <role>`: Assigns a specified role to the user who invokes the command.
- `!points <member>`: Displays the points of a member.
- `!addpoints <member> <amount>`: Adds points to a member's total.
- `!delete <number>`: Deletes a specified number of messages in the channel.

## Customization

You can customize and extend the bot's functionalities by modifying the `bot_discord.py` script.

## License

This project is licensed under the MIT License.
