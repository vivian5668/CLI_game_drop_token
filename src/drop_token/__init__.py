# -*- coding: utf-8 -*-

# This file (empty) is there to tell Python that directory contains a package.
# That’s it. It could be empty just to have the simple indication, or it could have
# actual code that will run during initialization of the package itself.

from .board import Board
from .game import Game
from .cli import main

__all__ = ['Board', 'Game', 'main']