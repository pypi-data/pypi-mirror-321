from importlib.metadata import metadata

from .tic_tac_toe import TicTacToe, main

_package_metadata = metadata(str(__package__))
__version__ = _package_metadata["Version"]
__author__ = _package_metadata.get("Author-email", "")

__all__ = ["TicTacToe", "__author__", "__version__", "main"]
