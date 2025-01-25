# P2PChat Bot Framework

A lightweight Python framework for creating chat bots for the P2P Chat platform.

## Installation

```bash
pip install p2pchat
```
## QuickStart For your first bot
from p2pchat import Bot

bot = Bot(prefix='$')  # Custom prefix or defaults to !

@bot.command()
async def hello(ctx):
    await ctx.get('api').send_message("Hello there!", ctx.get('chat_id'))

bot.run("your_bot_token")