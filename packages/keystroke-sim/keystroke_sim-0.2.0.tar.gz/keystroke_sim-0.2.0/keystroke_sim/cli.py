"""
Command-line interface for keystroke_sim package.
"""

import os
import sys
import argparse
from typing import Optional
import signal

from .keyboard_monitor import KeyboardMonitor
from .simulator import KeystrokeSimulator

def check_permissions() -> bool:
    """Check if running with necessary permissions."""
    if os.name == 'posix' and os.geteuid() != 0:
        print("Error: Root privileges required for keyboard access.")
        print("Please run with: sudo keystroke-sim [command]")
        return False
    return True

def monitor_command(args: argparse.Namespace) -> None:
    """Handle keyboard monitoring command."""
    if not check_permissions():
        sys.exit(1)
        
    config = {
        'log_format': '%(asctime)s - %(message)s',
        'date_format': '%Y-%m-%d %H:%M:%S',
        'log_key_combinations': not args.no_combinations,
        'collect_statistics': not args.no_stats,
        'ignored_keys': set(['shift', 'alt']) if not args.track_all else set(),
        'max_combination_keys': args.max_combo_keys
    }
    
    monitor = KeyboardMonitor(log_file=args.log_file, config=config)
    
    print("=== Keyboard Monitor ===")
    print(f"\nLogging to: {monitor.log_file}")
    print("Press Ctrl+C to stop monitoring.")
    
    try:
        monitor.start()
    except KeyboardInterrupt:
        print("\nStopping monitor...")
        monitor.stop()
        if not args.no_stats:
            stats = monitor.get_statistics()
            print(f"\nTotal keystrokes: {stats['total_keystrokes']}")
    
def simulate_command(args: argparse.Namespace) -> None:
    """Handle keystroke simulation command."""
    if not check_permissions():
        sys.exit(1)
        
    sim = KeystrokeSimulator()
    
    if args.text:
        print(f"Typing text with {args.delay}s delay...")
        sim.type_string(args.text, delay=args.delay)
    elif args.hotkey:
        print(f"Pressing hotkey: {'+'.join(args.hotkey)}")
        sim.press_hotkey(args.hotkey)
    else:
        print("Error: Either --text or --hotkey must be specified.")
        sys.exit(1)

def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Keystroke Simulation and Monitoring Tool"
    )
    subparsers = parser.add_subparsers(dest='command', help='Command to run')
    
    # Monitor command
    monitor_parser = subparsers.add_parser('monitor', help='Monitor keyboard input')
    monitor_parser.add_argument(
        '--log-file',
        type=str,
        help='Custom log file path'
    )
    monitor_parser.add_argument(
        '--no-combinations',
        action='store_true',
        help='Disable logging of key combinations'
    )
    monitor_parser.add_argument(
        '--no-stats',
        action='store_true',
        help='Disable collection of keystroke statistics'
    )
    monitor_parser.add_argument(
        '--track-all',
        action='store_true',
        help='Track all keys including modifiers'
    )
    monitor_parser.add_argument(
        '--max-combo-keys',
        type=int,
        default=3,
        help='Maximum number of keys in combinations'
    )
    
    # Simulate command
    simulate_parser = subparsers.add_parser('simulate', help='Simulate keyboard input')
    simulate_parser.add_argument(
        '--text',
        type=str,
        help='Text to type'
    )
    simulate_parser.add_argument(
        '--hotkey',
        nargs='+',
        help='Hotkey combination to press (e.g., ctrl c)'
    )
    simulate_parser.add_argument(
        '--delay',
        type=float,
        default=0.1,
        help='Delay between keystrokes in seconds'
    )
    
    args = parser.parse_args()
    
    if args.command == 'monitor':
        monitor_command(args)
    elif args.command == 'simulate':
        simulate_command(args)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
