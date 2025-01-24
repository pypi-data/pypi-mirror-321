"""
Simple demonstration of keystroke simulation library.
"""

import time
from keystroke_sim import KeystrokeSimulator

def main():
    """Run a simple demonstration of keystroke simulation."""
    try:
        print("=== KeystrokeSimulator Demo ===")
        
        # Initialize simulator
        sim = KeystrokeSimulator(log_file="demo.log")
        
        print("\nDemo will start in 3 seconds...")
        print("Please open a text editor or terminal to receive input")
        time.sleep(3)
        
        # Simple typing demonstration
        print("\n1. Demonstrating basic typing...")
        sim.type_string("Hello from KeystrokeSimulator!", delay=0.1)
        
        time.sleep(1)
        
        # Demonstrate hotkey
        print("\n2. Demonstrating hotkey combination...")
        sim.press_hotkey(['ctrl', 'a'])  # Select all
        time.sleep(0.5)
        
        # Type more text
        print("\n3. Demonstrating variable delays...")
        sim.type_string("This is typed with longer delays...", delay=0.2)
        
        print("\nDemo completed successfully!")
        print("Check demo.log for the event log.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main()
