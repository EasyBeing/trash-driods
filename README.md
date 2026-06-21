# Trash Droids
An asteroids-like game built with Godot.

## Game Description
A space shooter game inspired by the classic Asteroids arcade game where the player controls a spaceship and destroys asteroids.

## Game Engine
- **Godot** 4.7+

## Project Setup
- [x] Godot project initialized with project.godot
- [x] Main scene created (scenes/main.tscn) - Basic 2D scene
- [x] Game manager script created (scripts/game_manager.gd) - Loads successfully
- [x] Player scene created (scenes/player.tscn) - Spaceship sprite
- [x] Player script created (scripts/player.gd) - Arrow key movement

## Project Structure
```
trash-driods/
├── project.godot               # Godot project configuration
├── scenes/
│   ├── main.tscn               # Main 2D game scene with Player instance
│   └── player.tscn             # Player spaceship scene
├── scripts/
│   ├── game_manager.gd         # Game initialization and management
│   └── player.gd               # Player movement and input handling
├── .gitignore                  # Git ignore for Godot projects
├── LICENSE
└── README.md
```

## Controls
- **Arrow Keys** - Move player in all directions

## How to Run
1. Open the project in Godot 4.7+
2. Press F5 or click "Run" to launch the game
3. The game window will open with a blank 2D scene

## Next Steps
- [ ] Create Player scene
- [ ] Implement player movement controls
- [ ] Add asteroids
- [ ] Implement shooting mechanics
- [ ] Add collision detection
- [ ] Add scoring system
- [ ] Add game over conditions
