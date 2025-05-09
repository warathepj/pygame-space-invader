# Space Invaders Game

A classic Space Invaders clone built with Python and Pygame.

## Description

This is a simple implementation of the classic arcade game Space Invaders. The player controls a spaceship at the bottom of the screen and must shoot down alien invaders while avoiding their attacks.

## Features

- Player-controlled spaceship
- Multiple enemies with movement patterns
- Shooting mechanics
- Score tracking
- Game over screen with restart functionality

## Requirements

- Python 3.x
- Pygame 2.5.0 or higher

## Setting Up Python Environment

1. Install Python:

   - Download Python 3.x from [python.org](https://www.python.org/downloads/)
   - During installation, make sure to check "Add Python to PATH"

2. Create a virtual environment (recommended):

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

## Installation

1. Clone this repository:

```bash
git clone https://github.com/warathepj/pygame-space-invader.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## How to Play

1. Run the game:

```bash
python main.py
```

2. Controls:

- Left Arrow: Move spaceship left
- Right Arrow: Move spaceship right
- Spacebar: Shoot
- Click "Restart Game" button to play again after game over

## Game Assets Required

Make sure you have the following image files in your game directory:

- `spaceship.png` - Game window icon
- `player.png` - Player spaceship
- `enemy.png` - Enemy sprite
- `bullet.png` - Bullet sprite

## License

MIT
