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
        super().__init__(100, 100, 50, 50, bread_engine.Color.GREEN, has_physics="gravity")
        self.ground_level = engine.window_height - self.rect.height
        self.gravity = 0.4
        self.velocity_y = 0

    def update(self):
        keys = bread_engine.KeyHandler.get_pressed_keys()

        if keys[bread_engine.KeyHandler.Key.A] or keys[bread_engine.KeyHandler.Key.LEFT]:
            self.rect.x -= 4
        if keys[bread_engine.KeyHandler.Key.D] or keys[bread_engine.KeyHandler.Key.RIGHT]:
            self.rect.x += 4

        if keys[bread_engine.KeyHandler.Key.SPACE] and self.rect.y == self.ground_level:
            self.velocity_y = -10

def cube_update(cube):
    cube.rect.x += 1

def different_cube_update(cube):
    cube.rect.x += 2

engine = bread_engine.Engine(debug=True, window_vsync=True, exit_bind=bread_engine.KeyHandler.Key.ESCAPE)

cube = bread_engine.Rect(200, 100, 50, 50, bread_engine.Color.RED, update_function=cube_update)

player = Player()

engine.add_object(player)
engine.add_object(cube)

engine.run()
```

I recommend taking a look at the source code for a better understanding of the engine!
