from .command import Command
from logging import getLogger

import typing as t


T = t.TypeVar("T")
logger = getLogger("bettercli")

@t.overload
def pos_option(name: 'str', type_: 'type[T]', default: 'T' = None, *, length: 'int' = 1): ...

@t.overload
def pos_option(name: 'str', type_: 'list[t.Optional[type]]' = [], *, default: 'list[t.Optional[t.Any]]' = [], min_length: 'int' = 1, max_length: 'int' = 1): ...

def pos_option(name, type_=None, *, default=None, length=None, min_length=None, max_length=None):
    def decorator(cmd:'Command'):
        logger.debug(f"OPTIONS: {name=} {type_=} {default=} {length=} {min_length=} {max_length=}")
        cmd.add_positional_option(name, type_, default=default, length=length, min_length=min_length, max_length=max_length)
        return cmd
    return decorator



@t.overload 
def kw_option(name: 'str', type_: 'type[T]', *keys: str, default: 'T' = None, length: 'int' = 2): ...

@t.overload
def kw_option(name: 'str', type_: 'list[t.Optional[type]]' = [], *keys: str, default: 'list[t.Optional[t.Any]]' = [], min_length: 'int' = 2, max_length: 'int' = 2): ...

def kw_option(name, type_=None, *keys, default=None, length=None, min_length=None, max_length=None):
    def decorator(cmd:'Command'):
        logger.debug("KW ARG")
        cmd.add_keyword_option(name, type_, default, *keys, length=length, min_length=min_length, max_length=max_length)
        return cmd
    return decorator
