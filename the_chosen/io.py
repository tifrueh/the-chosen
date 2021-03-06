# coding=utf-8

"""
This input holds helper function for handling program input and output.

Functions:
    cmd_input
    interpret_single
    interpret_double
    ch_print
"""

# The Chosen  Copyright (C) 2022  Timo Früh
# Full copyright notice in __main__.py

import os
import textwrap


def cmd_input():
    """
    Read a command from input.

    :rtype: str
    """

    user_input = input("> ")

    return user_input


def interpret_single(command, key, remove=None):
    """
    Intepret a command with only one argument.

    :param command: The whole command the user has typed.
    :type command: str

    :param key: Command key that should trigger this command, e.g. "fight".
    :type key: str

    :param remove: A list of words (strings) to remove from the users input.
    :type remove: list

    :return: The interpreted command.
    :rtype: str
    """

    output = command.replace(key, "")

    if remove:
        for word in remove:
            output = output.replace(word, " ")

    return output.lower().strip()


def interpret_double(command, key, separator, remove_0=None, remove_1=None):
    """
    Interpret a command with two arguments.

    :param command: The whole command the user has typed.
    :type command: str

    :param key: Command key that should trigger this command, e.g. "fight".
    :type key: str

    :param separator: Command separator that is between the two arguments, e.g. "with".
    :type separator: str

    :param remove_0: List of words (strings) to remove from the first argument.
    :type remove_0: list

    :param remove_1: List of words (strings) to remove from the second argument.
    :type remove_1: list

    :return: Both parts of the interpreted command in a list.
    :rtype: list
    """

    without_key = command.replace(key, "")

    output = without_key.split(separator)

    try:
        output[1]

    except IndexError:
        output.append("")

    if remove_0:
        for word in remove_0:
            output[0] = output[0].replace(word, " ")

    if remove_1:
        for word in remove_1:
            output[1] = output[1].replace(word, " ")

    return [output[0].lower().strip(), output[1].lower().strip()]


def ch_print(string):
    """
    Print string but with correct text wrapping according to terminal size.

    :param string: The string to print.
    :type string: str
    """

    outlines = wrap(string)

    for line in outlines:
        print(line)


def ch_input(prompt):
    """
    Read user input and wrap the prompt correctly.

    :param prompt: The prompt to display while reading user input.
    :type prompt: str
    """

    outlines = wrap(prompt)

    for line in range(0, len(outlines) - 1):
        print(line)

    return input(outlines[-1] + " ")


def wrap(string):
    """
    Wrap the input string.

    :param string: The string to wrap.
    :type string: str

    :return: All the separate lines, correctly wrapped and in a list.
    :rtype: list
    """

    if string == "":
        return [""]

    else:
        termcolumns = os.get_terminal_size().columns

        if termcolumns > 120:
            termcolumns = 120

        splitstring = string.split("\n")

        outpars = []

        for line in splitstring:
            outpars.append(textwrap.fill(text=line, width=termcolumns))

        outlines = []

        for par in outpars:
            for line in par:
                outlines.append(line)

        return outpars
