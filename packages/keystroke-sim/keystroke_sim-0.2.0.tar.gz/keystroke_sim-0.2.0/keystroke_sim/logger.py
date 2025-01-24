"""
Logging functionality for keystroke simulation events.
"""

import logging
import os
from datetime import datetime
from typing import Optional

class KeystrokeLogger:
    """
    Logger for keystroke simulation events with enhanced security tracking.
    """
    
    def __init__(self, log_file: Optional[str] = None):
        """
        Initialize the keystroke logger.
        
        Args:
            log_file: Optional path to log file. If None, creates a timestamped log file.
        """
        if log_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file = f"keystrokes_{timestamp}.log"
        
        # Ensure the logs directory exists
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        # Configure logging
        self.logger = logging.getLogger('keystroke_sim')
        self.logger.setLevel(logging.INFO)
        
        # Create file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        
        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
        # Log initialization
        self.info(f"Keystroke logging initialized. Log file: {log_file}")
        
    def info(self, message: str) -> None:
        """Log an info message."""
        self.logger.info(self._format_message(message))
        
    def warning(self, message: str) -> None:
        """Log a warning message."""
        self.logger.warning(self._format_message(message))
        
    def error(self, message: str) -> None:
        """Log an error message."""
        self.logger.error(self._format_message(message))
        
    def critical(self, message: str) -> None:
        """Log a critical message."""
        self.logger.critical(self._format_message(message))
        
    def _format_message(self, message: str) -> str:
        """
        Format the log message with additional context.
        
        Args:
            message: The message to format
            
        Returns:
            str: Formatted message with context
        """
        # Add process information for security tracking
        pid = os.getpid()
        process_name = os.path.basename(os.path.realpath(__file__))
        
        return f"[PID:{pid}][Process:{process_name}] {message}"
        
    def __enter__(self):
        """Context manager entry."""
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Context manager exit with cleanup.
        
        Ensures all handlers are properly closed.
        """
        for handler in self.logger.handlers[:]:
            handler.close()
            self.logger.removeHandler(handler)
