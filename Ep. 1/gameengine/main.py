import sdl2

class GameEngine:
    def __init__(self, title = None, width = 800, height = 600, bg_color = (0, 0, 0, 255)):
        self.title = title.encode() if title else b"GameEngine!"
        self.width = width
        self.height = height
        self.bg_color = bg_color

        sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)

        self.window = sdl2.SDL_CreateWindow(self.title, sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, self.width, self.height, sdl2.SDL_WINDOW_SHOWN)
        self.renderer = sdl2.SDL_CreateRenderer(self.window, -1, 0)

        self.running = True

    def loop(self):
        sdl2.SDL_ShowWindow(self.window)

        event = sdl2.SDL_Event()

        while self.running:
            if sdl2.SDL_PollEvent(event) != 0:
                if event.type == sdl2.SDL_Quit:
                    self.running = False
                if event.type == sdl2.SDL_KEYDOWN:
                    if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                        self.running = False

            sdl2.SDL_RenderClear(self.renderer)
            sdl2.SDL_SetRenderDrawColor(self.renderer, self.bg_color[0], self.bg_color[1], self.bg_color[2], self.bg_color[3])
            sdl2.SDL_RenderPresent(self.renderer)

        sdl2.SDL_DestroyRenderer(self.renderer)
        sdl2.SDL_DestroyWindow(self.window)
        sdl2.SDL_Quit()