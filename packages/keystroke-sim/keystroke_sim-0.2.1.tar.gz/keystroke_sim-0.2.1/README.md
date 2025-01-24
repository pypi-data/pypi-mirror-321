# KeystrokeSimulator

A comprehensive Python library for keyboard input simulation and monitoring, developed by Bassem Abidi (abidi.bassem@me.com).

## Features

### Keystroke Simulation
- 🎯 Cross-platform support (Windows, macOS, Linux)
- ⌨️ Simulate individual keystrokes
- 📝 Type strings with customizable delays
- 🔥 Support for hotkey combinations
- 🔧 Custom keyboard layout definitions

### Keyboard Monitoring
- 📊 Real-time keystroke logging
- 📈 Detailed keystroke statistics
- 🔍 Key combination tracking
- 📅 Date-organized logs
- 📊 Usage analytics

## Quick Start

### Installation

```bash
pip install keystroke-sim
```

### Command Line Usage

1. Monitor keyboard input:
```bash
# Basic monitoring
sudo keystroke-sim monitor

# Advanced options
sudo keystroke-sim monitor --track-all --max-combo-keys 4
```

2. Simulate keystrokes:
```bash
# Type text
keystroke-sim simulate --text "Hello, World!" --delay 0.1

# Press hotkey
keystroke-sim simulate --hotkey ctrl c
```

### Python API Usage

```python
from keystroke_sim import KeystrokeSimulator, KeyboardMonitor

# Simulate keystrokes
sim = KeystrokeSimulator()
sim.type_string("Hello, World!", delay=0.1)
sim.press_hotkey(['ctrl', 'c'])

# Monitor keyboard
monitor = KeyboardMonitor()
monitor.start()  # Starts monitoring
```

## Features in Detail

### Keyboard Monitoring

1. **Real-time Logging**
   - Timestamps for all events
   - Key press and release tracking
   - Key combination detection
   - Organized daily log files

2. **Statistics Collection**
   - Total keystroke count
   - Most frequent keys
   - Common key combinations
   - Usage patterns

3. **Data Organization**
   ```
   logs/
   ├── 2024-01-15/
   │   ├── keystrokes_123456.log
   │   └── keystrokes_123456_stats.json
   └── 2024-01-16/
       ├── keystrokes_234567.log
       └── keystrokes_234567_stats.json
   ```

### Keystroke Simulation

1. **Basic Operations**
   - Individual key presses
   - String typing
   - Hotkey combinations
   - Custom delays

2. **Custom Layouts**
   ```python
   layout = {
       'special_key': 'enter',
       'custom_combo': ['ctrl', 'shift', 'x']
   }
   sim.set_keyboard_layout(layout)
   ```

## Configuration

### Monitor Configuration Options

```bash
keystroke-sim monitor [OPTIONS]

Options:
  --log-file PATH          Custom log file path
  --no-combinations        Disable logging of key combinations
  --no-stats              Disable collection of keystroke statistics
  --track-all             Track all keys including modifiers
  --max-combo-keys N      Maximum keys in combinations (default: 3)
```

### Simulation Configuration Options

```bash
keystroke-sim simulate [OPTIONS]

Options:
  --text TEXT             Text to type
  --hotkey KEY...         Hotkey combination (e.g., ctrl c)
  --delay SECONDS         Delay between keystrokes (default: 0.1)
```

## Platform-Specific Requirements

### Linux
```bash
# Run with sudo for keyboard access
sudo keystroke-sim monitor
```

### macOS
- Grant accessibility permissions
- Allow terminal access in Security & Privacy

### Windows
- Run as administrator for certain applications

## Safety and Privacy

1. **Data Security**
   - Local logging only
   - No network transmission
   - Clear log file locations

2. **Transparency**
   - All operations are logged
   - Statistics are saved locally
   - No hidden functionality

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `python -m pytest tests/`
5. Submit a pull request

## Support

For issues, questions, or contributions:
- GitHub Issues: [https://github.com/bassemabidi/keystroke_sim/issues](https://github.com/bassemabidi/keystroke_sim/issues)
- Email: abidi.bassem@me.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Bassem Abidi (abidi.bassem@me.com)

## Version History

See [CHANGELOG.md](CHANGELOG.md) for version history and changes.
