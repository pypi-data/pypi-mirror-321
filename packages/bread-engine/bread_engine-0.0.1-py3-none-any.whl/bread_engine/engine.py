import pygame
from .color import Color
from .keyhandler import KeyHandler

class Engine:
    def __init__(self, debug=False, window_width=800, window_height=600, window_resizable=False, window_vsync=False,
                 fps=60, exit_bind=None, background_color=Color.WHITE):
        self.debug = debug
        self.window_width = window_width
        self.window_height = window_height
        self.window_resizable = window_resizable
        self.window_vsync = window_vsync
        self.fps = fps
        self.exit_bind = exit_bind
        self.background_color = background_color

        if self.debug: print("Initializing: pygame")
        pygame.init()

        if self.debug: print("Initializing: window")
        self.window = pygame.display.set_mode(
            (self.window_width, self.window_height),
            flags = pygame.RESIZABLE if self.window_resizable else pygame.SCALED,
            vsync = 1 if self.window_vsync else 0
        )

        if self.debug: print("Initializing: Game Elements")

        self.clock = pygame.time.Clock()
        self.objects = []
        self.running = True

        if self.debug: print("Initializing Engine Finished.")

    # Add new game objects
    def add_object(self, obj):
        if not isinstance(obj, object):
            raise TypeError(f"Expected a class, but got {type(obj).__name__}")

        self.objects.append(obj)

        if self.debug:
            if hasattr(obj, '__name__'):  # For classes
                print(f"Class {obj.__name__} added successfully.")
            else:  # For instances
                print(f"Instance of {obj.__class__.__name__} added successfully.")

    @staticmethod
    def apply_physics(obj):
        # Ensure "has_physics" exists
        if not hasattr(obj, "has_physics") or not obj.has_physics:
            return

        # Convert "has_physics" to a list if it's a single string
        if isinstance(obj.has_physics, str):
            obj.has_physics = [obj.has_physics]

        # If it's neither a list nor a valid single string, reset to an empty list
        if not isinstance(obj.has_physics, list):
            obj.has_physics = []

        # Remove duplicates by converting to a set and back to a list
        obj.has_physics = list(set(obj.has_physics))

        # Process physics based on the contents of "has_physics"
        for effect in obj.has_physics:
            if effect == "gravity":
                # Ensure required attributes exist with defaults
                obj.gravity = getattr(obj, "gravity", 0.4)
                obj.velocity_y = getattr(obj, "velocity_y", 0)

                # Apply gravity
                obj.velocity_y += obj.gravity
                if hasattr(obj, "rect"):
                    obj.rect.y += obj.velocity_y

                # Handle ground collision
                if hasattr(obj, "ground_level") and hasattr(obj, "rect"):
                    if obj.rect.y >= obj.ground_level and obj.velocity_y >= 0:
                        obj.velocity_y = 0
                        obj.rect.y = obj.ground_level

    # Update game logic
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if (event.type == pygame.KEYDOWN
                    and event.key == self.exit_bind
                    and self.exit_bind is not None): self.running = False

        for obj in self.objects:
            if hasattr(obj, "update"):
                obj.update()
            self.apply_physics(obj)

    # Render
    def draw(self):
        self.window.fill(self.background_color)

        for obj in self.objects:
            if hasattr(obj, "draw"):
                obj.draw(self.window)

        pygame.display.flip()

    # Run the engine
    def run(self):
        if self.debug: print("Running Game...")
        while self.running:
            self.update()
            self.draw()
            self.clock.tick(self.fps)

        if self.debug: print("Quitting Game...")
        pygame.quit()
