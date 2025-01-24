from .algorithms import *
from .generators import *
from .utils import *


with open("version.txt", "r") as file:
    version = file.read()

__version__ = version
