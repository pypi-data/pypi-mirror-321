'''
Created by omaxpy

Don't forget to put your bot token in the .env
'''

import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


class Bot(commands.Bot):

    def __init__(self) -> None:
        super().__init__(
            command_prefix=commands.when_mentioned_or('!'),
            intents=discord.Intents.all(),
            help_command=None,
        )

    async def setup_hook(self):
        file_path = os.path.realpath(os.path.dirname(__file__))
        for file in os.listdir(f"{file_path}/cogs"):
            if file.endswith(".py"):
                try:
                    await self.load_extension(f"cogs.{file[:-3]}")
                    print(f"Successfully loaded {file}")
                except Exception as e:
                    print(f"Couldn't load {file}\nError: {e}")

        try:
            synced = await self.tree.sync()
            print(f"{len(synced)} commands synced")
        except Exception as e:
            print(f"Sync error: {e}")


if __name__ == "__main__":
    bot = Bot()
    bot.run(os.getenv("BOT_TOKEN"))
