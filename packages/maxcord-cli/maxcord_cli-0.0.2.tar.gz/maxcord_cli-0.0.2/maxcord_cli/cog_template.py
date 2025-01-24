from discord.ext import commands
from discord.ext.commands import Context


class COG_NAME(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    '''
    @commands.hybrid_command(name="test_command", description="This is a test command.")
    async def test_command(self, ctx: Context):
        await ctx.reply("Test!")
    '''


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(COG_NAME(bot))
