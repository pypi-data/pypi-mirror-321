#!/usr/bin/env python3
# coding=utf-8

import sys
import argparse
import functools
import inspect
from typing import Callable, get_args, Optional
import importlib
import argcomplete


class _MyArgParser(argparse.ArgumentParser):
    def error(self, message):
        print(message)
        print("----------------------------------")
        print()
        self.print_help()
        sys.exit(1)


class EasyArg:
    """
    Used to generate subparsers for target functions by decorating `@instance.command()`
    Then, call `instance.parse` to run corresponding function based on CLI command
    """

    def __init__(self, description: str = ""):
        """
        Initialize:
            - argparse.ArgumentParser & its subparsers
            - functions holder

        Last Update: @2024-11-23 14:35:26
        """
        self.parser = _MyArgParser(description=description)
        self.subparsers = self.parser.add_subparsers(dest='command', help='Execute functions from CLI commands directly')
        self.functions = {}

    def command(self, desc=""):
        """
        A function decorator, used to generate a subparser and arguments based on the function signature

        Last Update: @2024-11-23 14:37:03
        """
        def decorator(func: Callable):
            # @ Prepare
            cmd_name = func.__name__
            if not desc:
                desc2 = func.__doc__.split('\n\n')[0].strip()  # Use the first paragraph
            else:
                desc2 = desc
            parser = self.subparsers.add_parser(cmd_name, help=desc2)  # @ exp | Add a subparser with command the same as function name

            # @ Main | Add arguments with proper attributes
            shortname_recorded = set()
            sig = inspect.signature(func)
            for param_name, param in sig.parameters.items():
                # @ Retrieve-type | From annotations, take the first type for the compound types, e.g. get `str`` for `typing.Union[str, float]`
                annotation = param.annotation
                annotations = get_args(annotation)
                if annotations:
                    annotation = annotations[0]  # @ note | Take the first annotation type as the target type in command line interface

                # @ Get-Attribute
                required = param.default == inspect._empty
                default = None if required else param.default

                # @ Add-Argument | Only support intrinsic types: int, float, str & bool
                # @ - Use the first letter as short-name if no conflict
                if annotation == inspect.Parameter.empty:
                    raise TypeError(f"Parameter '{param_name}' in function '{func.__name__}' missing type hint")

                elif annotation in (int, float, str):
                    short_name = param_name[0]
                    assert short_name.isalpha()
                    if short_name not in shortname_recorded:
                        parser.add_argument(f"--{param_name}", f"-{short_name}", type=annotation, required=required, default=default, help=f"type={annotation.__name__}, {required=}, {default=}")
                        shortname_recorded.add(short_name)
                    else:
                        parser.add_argument(f"--{param_name}", type=annotation, required=required, default=default, help=f"type={annotation.__name__}, {required=}, {default=}")
                    # arg_recorded.add(param_name)

                elif annotation == bool:
                    short_name = param_name[0]
                    assert short_name.isalpha()
                    if short_name not in shortname_recorded:
                        parser.add_argument(f"--{param_name}", f"-{short_name}", action="store_true", required=required, default=default, help=f"type={annotation.__name__}, {required=}, {default=}")
                        shortname_recorded.add(short_name)
                    else:
                        parser.add_argument(f"--{param_name}", action="store_true", required=required, default=default, help=f"type={annotation.__name__}, {required=}, {default=}")
                    # arg_recorded.add(param_name)
                else:
                    raise TypeError(f"easyarg only supports types: int, float, str & bool, now is {annotation}")

            # @ Post
            self.functions[cmd_name] = func

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper
        return decorator

    def parse(self, args: Optional[list[str]] = None):
        """
        Last Update: @2024-11-23 14:40:31
        ---------------------------------
        Parse arguments and call corresponding function
        """
        argcomplete.autocomplete(self.parser)
        args = self.parser.parse_args(args)
        kwargs = {key: value for key, value in vars(args).items() if key != 'command' and value is not None}

        if args.command is None:
            self.parser.print_help()
            return

        func = self.functions[args.command]
        func(**kwargs)
