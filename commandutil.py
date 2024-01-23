from discord.ext.commands import cooldown
from discord.ext.commands import cooldown as guildcooldown
from discord.ext.commands import cooldown as usercooldown

def subscript_only():
    def dec(func):
        return func
    return dec
