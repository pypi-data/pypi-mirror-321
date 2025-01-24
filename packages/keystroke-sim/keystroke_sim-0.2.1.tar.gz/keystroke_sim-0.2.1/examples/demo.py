"""
Demonstration of KeystrokeSimulator library features.
"""

import time
import threading
from keystroke_sim import KeystrokeSimulator, KeyboardMonitor

def run_monitor(duration=30):
    """Run keyboard monitor for specified duration."""
    print("\nStarting keyboard monitor...")
    monitor = KeyboardMonitor(log_file="demo_monitor.log")
    
    # Start monitoring in a separate thread
    monitor_thread = threading.Thread(target=monitor.start)
    monitor_thread.daemon = True
    monitor_thread.start()
    
    # Run for specified duration
    time.sleep(duration)
    
    # Stop monitoring and show stats
    monitor.stop()
    stats = monitor.get_statistics()
    
    print("\nMonitoring Results:")
    print(f"Total keystrokes: {stats['total_keystrokes']}")
    
    if stats['key_frequencies']:
        print("\nMost used keys:")
        sorted_keys = sorted(
            stats['key_frequencies'].items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]
        for key, count in sorted_keys:
            print(f"  {key}: {count} times")

def simulate_typing():
    """Demonstrate keystroke simulation."""
    print("\nDemonstrating keystroke simulation...")
    sim = KeystrokeSimulator()
    
    # Basic typing
    print("1. Basic typing...")
    sim.type_string("Hello from KeystrokeSimulator!", delay=0.1)
    time.sleep(1)
    
    # Hotkeys
    print("2. Hotkey combination...")
    sim.press_hotkey(['ctrl', 'a'])  # Select all
    time.sleep(0.5)
    
    # More typing
    print("3. More typing with different delay...")
    sim.type_string("This text was typed with a longer delay.", delay=0.2)
    time.sleep(1)

def main():
    print("=== KeystrokeSimulator Library Demo ===")
    print("\nThis demo will:")
    print("1. Start monitoring keyboard input")
    print("2. Simulate some keystrokes")
    print("3. Show monitoring statistics")
    
    input("\nPress Enter to begin...")
    
    # Start monitoring
    monitor_thread = threading.Thread(
        target=run_monitor,
        args=(20,)  # Run for 20 seconds
    )
    monitor_thread.start()
    
    # Wait a moment for monitor to start
    time.sleep(2)
    
    # Run simulation
    simulate_typing()
    
    print("\nContinue typing to see your keystrokes counted...")
    print("Demo will end in 15 seconds...")
    
    # Wait for monitor to finish
    monitor_thread.join()
    
    print("\nDemo completed!")
    print("Check demo_monitor.log for the complete log.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nDemo interrupted by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
