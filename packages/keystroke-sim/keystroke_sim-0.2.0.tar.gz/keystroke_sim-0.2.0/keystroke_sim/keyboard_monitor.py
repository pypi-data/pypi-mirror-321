"""
Keyboard monitoring functionality with advanced keystroke logging.
"""

import os
import time
import logging
from datetime import datetime
from typing import Optional, Set, Dict
import keyboard
import json

class KeyboardMonitor:
    """
    Advanced keyboard monitoring with keystroke logging and analytics.
    """
    
    def __init__(self, log_file: Optional[str] = None, config: Optional[Dict] = None):
        """
        Initialize the keyboard monitor.
        
        Args:
            log_file: Optional path to log file
            config: Optional configuration dictionary
        """
        self.config = config or self._default_config()
        self.log_file = self._setup_log_file(log_file)
        self.logger = self._setup_logger()
        self.start_time = None
        self.running = False
        self.pressed_keys: Set[str] = set()
        self.key_stats = {
            'total_keystrokes': 0,
            'key_frequencies': {},
            'common_combinations': {}
        }
        
    def _default_config(self) -> Dict:
        """Get default configuration."""
        return {
            'log_format': '%(asctime)s - %(message)s',
            'date_format': '%Y-%m-%d %H:%M:%S',
            'log_key_combinations': True,
            'collect_statistics': True,
            'ignored_keys': set(['shift', 'alt']),  # Keys to ignore in combinations
            'max_combination_keys': 3  # Maximum keys in combination
        }
        
    def _setup_log_file(self, log_file: Optional[str]) -> str:
        """Set up log file path."""
        if log_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file = f"keystrokes_{timestamp}.log"
            
        # Ensure logs directory exists
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        return log_file
        
    def _setup_logger(self) -> logging.Logger:
        """Set up logging configuration."""
        logger = logging.getLogger('keyboard_monitor')
        logger.setLevel(logging.INFO)
        
        # Create file handler
        fh = logging.FileHandler(self.log_file)
        fh.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter(
            self.config['log_format'],
            datefmt=self.config['date_format']
        )
        fh.setFormatter(formatter)
        
        # Add handler to logger
        logger.addHandler(fh)
        
        return logger
        
    def _handle_event(self, event):
        """Handle keyboard events."""
        if event.event_type == keyboard.KEY_DOWN:
            key_name = event.name.lower()
            
            # Update statistics
            if self.config['collect_statistics']:
                self.key_stats['total_keystrokes'] += 1
                self.key_stats['key_frequencies'][key_name] = \
                    self.key_stats['key_frequencies'].get(key_name, 0) + 1
            
            # Track pressed keys for combinations
            if self.config['log_key_combinations']:
                if key_name not in self.config['ignored_keys']:
                    self.pressed_keys.add(key_name)
                    
                    # Log key combination if multiple keys are pressed
                    if len(self.pressed_keys) > 1 and \
                       len(self.pressed_keys) <= self.config['max_combination_keys']:
                        combo = '+'.join(sorted(self.pressed_keys))
                        self.logger.info(f"Key combination: {combo}")
                        
                        if self.config['collect_statistics']:
                            self.key_stats['common_combinations'][combo] = \
                                self.key_stats['common_combinations'].get(combo, 0) + 1
            
            # Log individual key press
            self.logger.info(f"Key pressed: {key_name}")
            
        elif event.event_type == keyboard.KEY_UP:
            key_name = event.name.lower()
            if key_name in self.pressed_keys:
                self.pressed_keys.remove(key_name)
                
    def start(self):
        """Start keyboard monitoring."""
        self.start_time = datetime.now()
        self.running = True
        self.logger.info("=== Keyboard Monitoring Started ===")
        
        keyboard.hook(self._handle_event)
        
        try:
            while self.running:
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.stop()
            
    def stop(self):
        """Stop keyboard monitoring and save statistics."""
        self.running = False
        keyboard.unhook_all()
        
        duration = datetime.now() - self.start_time
        
        self.logger.info("=== Keyboard Monitoring Stopped ===")
        self.logger.info(f"Duration: {duration}")
        
        # Save statistics if enabled
        if self.config['collect_statistics']:
            stats_file = self.log_file.replace('.log', '_stats.json')
            with open(stats_file, 'w') as f:
                json.dump(self.key_stats, f, indent=2)
                
    def get_statistics(self) -> Dict:
        """Get current keystroke statistics."""
        return self.key_stats
