import pygame

class Rect:
    def __init__(self, x, y, width, height, color, update_function=None, has_physics = None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.update_function = update_function
        self.has_physics = has_physics

    def update(self):
        # Call the custom update function if it exists
        if self.update_function:
            self.update_function(self)  # Pass the Cube instance to the function for context

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

class Circle:
    def __init__(self, x, y, radius, color, update_function=None, has_physics = None):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.update_function = update_function
        self.has_physics = has_physics

    def update(self):
        # Call the custom update function if it exists
        if self.update_function:
            self.update_function(self)  # Pass the Circle instance to the function for context

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

class Line:
    def __init__(self, start_pos, end_pos, color, width=1, update_function=None, has_physics = None):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.color = color
        self.width = width
        self.update_function = update_function
        self.has_physics = has_physics

    def update(self):
        # Call the custom update function if it exists
        if self.update_function:
            self.update_function(self)  # Pass the Line instance to the function for context

    def draw(self, window):
        pygame.draw.line(window, self.color, self.start_pos, self.end_pos, self.width)

class Polygon:
    def __init__(self, points, color, update_function=None, has_physics = None):
        self.points = points  # List of (x, y) tuples defining the polygon
        self.color = color
        self.update_function = update_function
        self.has_physics = has_physics

    def update(self):
        # Call the custom update function if it exists
        if self.update_function:
            self.update_function(self)  # Pass the Polygon instance to the function for context

    def draw(self, window):
        pygame.draw.polygon(window, self.color, self.points)
