import os
import tkinter
import webcolors

pygdk_dir = os.path.dirname(os.path.abspath(__file__))

class Gk(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title("pygdk")
        self.iconbitmap(os.path.join(pygdk_dir, "assets", "pygdk.ico"))

        self._current_width = 800
        self._current_height = 600

        self._center_screen()

    def  _center_screen(self):
        # Get the dimensions of the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the position to center the window
        x_pos = (screen_width // 2) - (self._current_width // 2)
        y_pos = (screen_height // 2) - (self._current_height // 2)

        self.geometry(f'{self._current_width}x{self._current_height}+{x_pos}+{y_pos}')

class GkColor:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            if args[0].startswith("#"):
                r, g, b = webcolors.hex_to_rgb(args[0])
            else:
                r, g, b = webcolors.name_to_rgb(args[0])
        elif len(args) == 1 and isinstance(args[0], tuple):
            r, g, b = args[0]
        elif len(args) == 3 and all(isinstance(arg, int) for arg in args):
            r, g, b = args
        else:
            raise TypeError("Invalid arguments for Color")
        
        self.r = r
        self.b = b
        self.g = g
    
    @property
    def RGBName(self):
        return webcolors.rgb_to_name((self.r, self.g, self.b))