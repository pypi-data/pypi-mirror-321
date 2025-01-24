





























































































































































"""
Core keystroke simulation functionality with cross-platform support.
"""

import platform
import time
from typing import List, Dict, Optional
import logging
from datetime import datetime

import keyboard
import pynput
import pyautogui

from .logger import KeystrokeLogger

class KeystrokeSimulator:
    """
    A cross-platform keystroke simulator that provides a unified interface
    for simulating keyboard input across different operating systems.
    """
    
    def __init__(self, log_file: Optional[str] = None):
        """
        Initialize the keystroke simulator with optional logging.
        
        Args:
            log_file: Optional path to log file. If None, logs to 'keystrokes_{timestamp}.log'
        """
        self.os = platform.system().lower()
        self.logger = KeystrokeLogger(log_file)
        self._keyboard_controller = pynput.keyboard.Controller()
        self._custom_layout: Dict = {}
        self._default_delay = 0.01  # 10ms default delay between keystrokes
        
        # Initialize platform-specific controllers
        if self.os == 'windows':
            self._init_windows()
        elif self.os == 'darwin':  # macOS
            self._init_macos()
        elif self.os == 'linux':
            self._init_linux()
        else:
            raise OSError(f"Unsupported operating system: {self.os}")
            
        self.logger.info(f"Initialized KeystrokeSimulator for {self.os}")

    def _init_windows(self):
        """Initialize Windows-specific components"""
        self.logger.info("Initializing Windows-specific components")
        self._use_keyboard_lib = True

    def _init_macos(self):
        """Initialize macOS-specific components"""
        self.logger.info("Initializing macOS-specific components")
        self._use_keyboard_lib = False

    def _init_linux(self):
        """Initialize Linux-specific components"""
        self.logger.info("Initializing Linux-specific components")
        try:
            # Try to use keyboard library first on Linux
            keyboard.on_press(lambda _: None)
            keyboard.unhook_all()
            self._use_keyboard_lib = True
        except Exception:
            # Fall back to pynput if keyboard library isn't available
            self._use_keyboard_lib = False
        self.logger.info(f"Using keyboard library: {self._use_keyboard_lib}")

    def press_key(self, key: str) -> None:
        """
        Press and hold a key.
        
        Args:
            key: The key to press (e.g., 'a', 'enter', 'shift')
        """
        mapped_key = self._custom_layout.get(key, key)
        self.logger.info(f"Pressing key: {mapped_key}")
        
        try:
            if self._use_keyboard_lib:
                keyboard.press(mapped_key)
            else:
                self._keyboard_controller.press(self._get_pynput_key(mapped_key))
        except Exception as e:
            self.logger.error(f"Error pressing key {mapped_key}: {str(e)}")
            raise

    def release_key(self, key: str) -> None:
        """
        Release a previously pressed key.
        
        Args:
            key: The key to release
        """
        mapped_key = self._custom_layout.get(key, key)
        self.logger.info(f"Releasing key: {mapped_key}")
        
        try:
            if self._use_keyboard_lib:
                keyboard.release(mapped_key)
            else:
                self._keyboard_controller.release(self._get_pynput_key(mapped_key))
        except Exception as e:
            self.logger.error(f"Error releasing key {mapped_key}: {str(e)}")
            raise

    def type_string(self, text: str, delay: Optional[float] = None) -> None:
        """
        Type a string with optional delay between characters.
        
        Args:
            text: The string to type
            delay: Delay between keystrokes in seconds (default: self._default_delay)
        """
        delay = delay if delay is not None else self._default_delay
        self.logger.info(f"Typing string (length: {len(text)}) with {delay}s delay")
        
        for char in text:
            try:
                if self._use_keyboard_lib:
                    keyboard.write(char)
                else:
                    self._keyboard_controller.type(char)
                time.sleep(delay)
            except Exception as e:
                self.logger.error(f"Error typing character '{char}': {str(e)}")
                raise

    def press_hotkey(self, keys: List[str]) -> None:
        """
        Press a combination of keys simultaneously.
        
        Args:
            keys: List of keys to press together (e.g., ['ctrl', 'c'])
        """
        mapped_keys = [self._custom_layout.get(k, k) for k in keys]
        self.logger.info(f"Pressing hotkey combination: {mapped_keys}")
        
        try:
            if self._use_keyboard_lib:
                keyboard.press_and_release('+'.join(mapped_keys))
            else:
                with self._keyboard_controller.pressed(*[self._get_pynput_key(k) for k in mapped_keys]):
                    pass
        except Exception as e:
            self.logger.error(f"Error pressing hotkey {mapped_keys}: {str(e)}")
            raise

    def set_keyboard_layout(self, layout: Dict[str, str]) -> None:
        """
        Set a custom keyboard layout mapping.
        
        Args:
            layout: Dictionary mapping custom keys to actual keys
        """
        self._custom_layout = layout
        self.logger.info(f"Set custom keyboard layout: {layout}")

    def set_default_delay(self, delay: float) -> None:
        """
        Set the default delay between keystrokes.
        
        Args:
            delay: Delay in seconds
        """
        self._default_delay = delay
        self.logger.info(f"Set default delay to {delay}s")

    def _get_pynput_key(self, key: str) -> pynput.keyboard.Key:
        """
        Convert a string key representation to a pynput key.
        
        Args:
            key: String representation of the key
            
        Returns:
            pynput.keyboard.Key: The corresponding pynput key
        """
        special_keys = {
            'enter': pynput.keyboard.Key.enter,
            'tab': pynput.keyboard.Key.tab,
            'space': pynput.keyboard.Key.space,
            'backspace': pynput.keyboard.Key.backspace,
            'delete': pynput.keyboard.Key.delete,
            'esc': pynput.keyboard.Key.esc,
            'ctrl': pynput.keyboard.Key.ctrl,
            'alt': pynput.keyboard.Key.alt,
            'shift': pynput.keyboard.Key.shift,
        }
        
        return special_keys.get(key.lower(), key)

    def __enter__(self):
        """Context manager entry"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit with cleanup"""
        self.logger.info("Cleaning up KeystrokeSimulator")
        if self._use_keyboard_lib:
            keyboard.unhook_all()
