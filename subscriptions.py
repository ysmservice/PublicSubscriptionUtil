from discord.ext import commands

class SubscriptionManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cache = dict()
    
    def is_subscribe(self, user, guild):
        return None

async def setup(bot):
    await bot.add_cog(SubscriptionManager(bot))