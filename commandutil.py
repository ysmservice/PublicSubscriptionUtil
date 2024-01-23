from discord.ext.commands import cooldown
from discord.ext.commands import cooldown as guildcooldown
from discord.ext.commands import cooldown as usercooldown
from SubscriptionUtil.exception import NoSubscription

def subscript_only():
    def dec(func):
        raise NoSubscription()
    return dec
