# Maxcord-CLI
Python library to easily initialize discord bot and cogs.

# Installation

```pip install maxcord-cli```

# Documentation

Create base files
```maxcord-cli ```

Example use:
```python
@bot.command()
async def test_pagination(ctx):
    embeds = [
        discord.Embed(title="A", description="Desc", color=0x00ff00),
        discord.Embed(title="B", description="Desc", color=0x00ff00)
    ]
    pagination = Pagination(ctx, embeds)
    await pagination.init_messsage()
```