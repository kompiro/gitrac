# -*- coding: utf-8 -*-
__version__ = "0.0.1"
__authors__ = ["Hiroki Kondo (kompiro@gmail.com)"]
__copyright__ = """
Copyright (c) 2009 
All rights reserved.
"""

from gitrac.command.DbCommand import *
from gitrac.command.ListCommand import ListCommand
from gitrac.command.AddCommand import *
from gitrac.command.RmCommand import *

#global commands;
commands = {
        'list':ListCommand(),
        'add':AddCommand(),
        'rm':RmCommand()
};

def create_command(com):
    return commands[com]

