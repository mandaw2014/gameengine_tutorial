import sdl2

class Entity(object):
    def __init__(self, window, width = 20, height = 20, x = 0, y = 0, color = (255, 255, 255, 255)):
        self.window = window
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color

        self.rect = sdl2.SDL_FRect(self.x, self.y, self.width, self.height)

    def draw(self):
        sdl2.SDL_SetRenderDrawColor(self.window.renderer, self.color[0], self.color[1], self.color[2], self.color[3])

        self.rect = sdl2.SDL_FRect(self.x, self.y, self.width, self.height)

        sdl2.SDL_RenderDrawRectF(self.window.renderer, self.rect)
        sdl2.SDL_RenderFillRectF(self.window.renderer, self.rect)

        self.rect = sdl2.SDL_FRect(self.x, self.y, self.width, self.height)

    def center_x(self):
        self.x = self.window.width / 2 - self.width / 2

    def center_y(self):
        self.y = self.window.height / 2 - self.height / 2

    def center(self):
        self.x = self.window.width / 2 - self.width / 2
        self.y = self.window.height / 2 - self.height / 2