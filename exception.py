from discord.ext.commands import CommandError


class NoSubscription(CommandError):
    def __init__(self, arg=""):
        self.arg = arg