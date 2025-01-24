"""
Tests for the KeystrokeSimulator class.
"""

import os
import time
import unittest
from unittest.mock import MagicMock, patch
from keystroke_sim import KeystrokeSimulator

class TestKeystrokeSimulator(unittest.TestCase):
    """Test cases for KeystrokeSimulator functionality."""
    
    def setUp(self):
        """Set up test environment before each test."""
        self.test_log_file = "test_keystrokes.log"
        self.simulator = KeystrokeSimulator(log_file=self.test_log_file)
        
    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.test_log_file):
            os.remove(self.test_log_file)
            
    @patch('keyboard.press')
    @patch('keyboard.release')
    def test_press_and_release_key(self, mock_release, mock_press):
        """Test pressing and releasing a single key."""
        self.simulator.press_key('a')
        self.simulator.release_key('a')
        
        mock_press.assert_called_once_with('a')
        mock_release.assert_called_once_with('a')
        
    @patch('keyboard.write')
    def test_type_string(self, mock_write):
        """Test typing a string."""
        test_string = "Hello, World!"
        self.simulator.type_string(test_string, delay=0)
        
        # Check that each character was typed
        self.assertEqual(mock_write.call_count, len(test_string))
        
    @patch('keyboard.press_and_release')
    def test_press_hotkey(self, mock_press_and_release):
        """Test pressing a hotkey combination."""
        hotkey = ['ctrl', 'c']
        self.simulator.press_hotkey(hotkey)
        
        mock_press_and_release.assert_called_once_with('ctrl+c')
        
    def test_custom_layout(self):
        """Test setting and using a custom keyboard layout."""
        custom_layout = {'special_key': 'enter'}
        self.simulator.set_keyboard_layout(custom_layout)
        
        with patch('keyboard.press') as mock_press:
            self.simulator.press_key('special_key')
            mock_press.assert_called_once_with('enter')
            
    def test_default_delay(self):
        """Test setting and using custom delay between keystrokes."""
        test_delay = 0.1
        self.simulator.set_default_delay(test_delay)
        
        with patch('keyboard.write') as mock_write:
            start_time = time.time()
            self.simulator.type_string("ab")
            end_time = time.time()
            
            # Verify delay between keystrokes
            self.assertGreaterEqual(end_time - start_time, test_delay)
            
    def test_logger_initialization(self):
        """Test that logging is properly initialized."""
        self.assertTrue(os.path.exists(self.test_log_file))
        
        # Verify log file contains initialization message
        with open(self.test_log_file, 'r') as f:
            log_content = f.read()
            self.assertIn("Keystroke logging initialized", log_content)
            
    @patch('keyboard.press')
    def test_error_handling(self, mock_press):
        """Test error handling during key press."""
        mock_press.side_effect = Exception("Test error")
        
        with self.assertRaises(Exception):
            self.simulator.press_key('a')
            
        # Verify error was logged
        with open(self.test_log_file, 'r') as f:
            log_content = f.read()
            self.assertIn("Error pressing key", log_content)
            
if __name__ == '__main__':
    unittest.main()
