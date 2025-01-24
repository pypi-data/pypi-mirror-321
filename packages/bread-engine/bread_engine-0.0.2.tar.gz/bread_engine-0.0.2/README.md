# [Bread Engine](https://pypi.org/project/bread-engine/)
The bread engine is a basic "game engine" made using PyGame.
The engine allows you to create games much easier and is fully compatible with PyGame.

## Example usage:
```python
import bread_engine

engine = bread_engine.Engine()

engine.run()
```

## Installation
```shell
pip install pygame
pip install bread_engine
```

## More examples:
```python
import bread_engine

class Player(bread_engine.Rect):
    def __init__(self):
        super().__init__(100, 100, 50, 50, bread_engine.Color.GREEN)

    def update(self):
        self.rect.x += 1

class Player2(bread_engine.Rect):
    def __init__(self):
        super().__init__(100, 200, 50, 50, bread_engine.Color.BLACK, has_physics="gravity")
        self.ground_level = engine.window_height - self.rect.height

def cube_update(cube):
    cube.rect.x += 1

def different_cube_update(cube):
    cube.rect.x += 2

engine = bread_engine.Engine(debug=True, window_vsync=True, exit_bind=bread_engine.KeyHandler.Keys.escape)

player = Player()

cube = bread_engine.Rect(200, 100, 50, 50, bread_engine.Color.RED, update_function=cube_update)
cube.update_function = different_cube_update # Swap out update functions after initialization
player2 = Player2() # Cube with gravity

engine.add_object(player)
engine.add_object(cube)
engine.add_object(player2)

engine.run()
```

I recommend taking a look at the source code for a better understanding of the engine!
