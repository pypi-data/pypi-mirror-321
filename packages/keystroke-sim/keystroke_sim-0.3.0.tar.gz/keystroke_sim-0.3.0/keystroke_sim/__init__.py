"""
KeystrokeSimulator - A library for keyboard input simulation and monitoring.
"""

from .simulator import KeystrokeSimulator
from .keyboard_monitor import KeyboardMonitor
from .logger import KeystrokeLogger

__version__ = "0.2.0"
__all__ = ["KeystrokeSimulator", "KeyboardMonitor", "KeystrokeLogger"]

# Version history
# 0.1.0 - Initial release with keystroke simulation
# 0.2.0 - Added keyboard monitoring with statistics
