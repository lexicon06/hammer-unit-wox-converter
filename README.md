# Hammer Unit Wox Converter

A Wox/Flow Launcher plugin for converting between real-world measurements and Hammer units (Source Engine).

![Plugin Icon](Images/app.png)

[![GitHub](https://img.shields.io/badge/GitHub-lexicon06-blue?logo=github)](https://github.com/lexicon06/hammer-unit-wox-converter)
[![Version](https://img.shields.io/badge/version-1.0.0-green)](https://github.com/lexicon06/hammer-unit-wox-converter/releases)

## Overview

This plugin allows you to quickly convert measurements between standard units (meters, feet, inches, etc.) and Hammer Editor units used in Source Engine games like Half-Life, Counter-Strike, Portal, and Team Fortress 2.

**Compatible with both Wox and Flow Launcher!**

## Features

- 🔄 Bidirectional conversion between real-world and Hammer units
- 📋 Copy results to clipboard with Enter
- 🎯 Support for multiple unit types
- 💡 Built-in examples and suggestions
- ⚡ Fast and lightweight
- 🔧 Works with Wox and Flow Launcher

## Supported Units

### Real-world measurements
- Yards
- Feet
- Inches
- Meters
- Decimeters
- Centimeters

### Hammer Editor units
- **Units** - Standard Hammer grid units (1 unit = 0.75 inches = 1.905 cm)
- **Skybox** - 3D skybox scale units (1 skybox unit = 1 foot = 16 units)

## Installation

### Method 1: Manual Installation

#### For Wox
1. Download or clone this repository
2. Copy the plugin folder to `%APPDATA%\Wox\Plugins\`
3. Restart Wox
4. Type `hammer` to start using it

#### For Flow Launcher
1. Download or clone this repository
2. Copy the plugin folder to `%APPDATA%\FlowLauncher\Plugins\`
3. Restart Flow Launcher
4. Type `hammer` to start using it

### Method 2: Git Clone
```bash
# For Wox
cd %APPDATA%\Wox\Plugins
git clone https://github.com/lexicon06/hammer-unit-wox-converter.git

# For Flow Launcher
cd %APPDATA%\FlowLauncher\Plugins
git clone https://github.com/lexicon06/hammer-unit-wox-converter.git
```

## Usage

The basic syntax is:
```
hammer <value> <from_unit> to <to_unit>
```

### Examples

**Converting to Hammer units:**
```
hammer 1 feet to units          → 16 units
hammer 3 meters to units        → 157.5 units
hammer 12 inches to units       → 16 units
```

**Converting from Hammer units:**
```
hammer 128 units to meters      → 2.44 meters
hammer 256 units to feet        → 16 feet
hammer 64 units to inches       → 48 inches
```

**Working with skybox units:**
```
hammer 1 skybox to meters       → 0.3 meters
hammer 64 meters to skybox      → 210 skybox
```

### Quick Reference

Just type `hammer` without any arguments to see available conversions and examples!

## Tips

- Results are automatically rounded to the nearest 0.05 for cleaner values
- Press **Enter** on any result to copy it to your clipboard
- The plugin shows helpful examples if you make a syntax error

## Common Use Cases

- **Level Design**: Quickly determine how tall a door should be in units (e.g., "hammer 2 meters to units" → 105 units)
- **Prop Scaling**: Convert real-world object dimensions to Hammer units
- **3D Skybox**: Calculate proper scale for distant geometry ("hammer 512 units to skybox" → 32 skybox)
- **Reference Checking**: Verify if your measurements feel realistic

## Technical Details

- **Language**: Python
- **Action Keyword**: `hammer`
- **Version**: 1.0.0
- **Author**: Pablo Santillán ([@lexicon06](https://github.com/lexicon06))
- **Compatible with**: Wox, Flow Launcher

### Conversion Reference

| Unit Type | Value in Meters |
|-----------|----------------|
| 1 Hammer Unit | 0.01905 m |
| 1 Skybox Unit | 0.3048 m (1 foot) |

The plugin uses precise conversion ratios based on Source Engine's official unit system where:
- 1 unit = 0.75 inches = 1.905 cm
- 16 units = 1 foot
- 1 skybox unit = 16 hammer units (when placed in 3D skybox)

## Contributing

Contributions are welcome! Feel free to:
- Report bugs or issues on the [Issues page](https://github.com/lexicon06/hammer-unit-wox-converter/issues)
- Suggest new features
- Submit pull requests

## License

MIT License - feel free to use and modify as needed.

## Keywords

`wox` `flow-launcher` `plugin` `hammer` `source-engine` `valve` `unit-converter` `level-design` `game-development` `mapping`

## Acknowledgments

Built for the Source Engine mapping community. Perfect for level designers working with Hammer Editor in games like:
- Half-Life / Half-Life 2
- Counter-Strike / CS:GO / CS2
- Portal / Portal 2
- Team Fortress 2
- Left 4 Dead
- And other Source Engine games

---

**Happy Mapping! 🔨**

*If you find this plugin useful, consider giving it a ⭐ on GitHub!*
