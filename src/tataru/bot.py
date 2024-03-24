import discord
from discord import Interaction, Member
from discord.ext.commands import Bot

# TODO: swap to discord.Client
def get_bot() -> Bot:
    intents = discord.Intents.default()

    bot = Bot(command_prefix='!!', intents=intents)

    @bot.event
    async def on_ready():
        await bot.tree.sync()

    @bot.tree.command(name='age', description='Get the age of an account')
    async def age(interation: Interaction, member: Member):
        await interation.response.send_message(f"{member.name}'s account was created at {member.created_at}")

    return bot