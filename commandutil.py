from discord.ext.commands import cooldown, Command
from discord.ext.commands import cooldown as guildcooldown
from discord.ext.commands import cooldown as usercooldown
import functools
import inspect
from typing import TYPE_CHECKING, Any, Callable, Union, Type, TypeVar, Coroutine, Protocol
from discord.ext import commands
from discord.ext.commands import BucketType, Command,Context, Cooldown

from SubscriptionUtil.exception import NoSubscription

from discord.ext.commands._types import CoroFunc
if TYPE_CHECKING:
    from typing_extensions import Concatenate, ParamSpec, Self
    from discord.ext.commands._types import BotT, ContextT, Coro, CoroFunc, Error, Hook, UserCheck

ContextT_co = TypeVar('ContextT_co', bound='Context[Any]', covariant=True)
_Bot = Union['Bot', 'AutoShardedBot']
T = TypeVar('T')
BotT = TypeVar('BotT', bound=_Bot, covariant=True)
class Check(Protocol[ContextT_co]):  # type: ignore # TypeVar is expected to be invariant

    predicate: Callable[[ContextT_co], Coroutine[Any, Any, bool]]

    def __call__(self, coro_or_commands: T) -> T:
        ...



def subscript_only() -> Check[Any]:
    def predicate(ctx: Context[BotT]) -> bool:
        if _bot.cogs["SubscriptionManager"].is_subscribe(ctx.author,ctx.guild) == None:
            raise NoSubscription()
        return True 
    def decorator(func: Union[Command, CoroFunc]) -> Union[Command, CoroFunc]:
        if isinstance(func, Command):
            func.checks.append(predicate)
        else:
            if not hasattr(func, '__commands_checks__'):
                func.__commands_checks__ = []

            func.__commands_checks__.append(predicate)

        return func

    if inspect.iscoroutinefunction(predicate):
        decorator.predicate = predicate
    else:

        @functools.wraps(predicate)
        async def wrapper(ctx: Context[BotT]):
            return predicate(ctx)

        decorator.predicate = wrapper

    return decorator  # type: ignore