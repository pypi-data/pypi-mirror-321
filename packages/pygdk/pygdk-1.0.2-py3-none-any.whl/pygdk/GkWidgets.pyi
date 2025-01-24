import tkinter
from typing import overload

class Gk(tkinter.Tk):
    """
    """
    # def __init__(self, bg_color: Optional[GkColor], **kwargs) -> None: ...
    def __init__(self) -> None: ...

class GkColor:
    r: int
    g: int
    b: int
    @overload
    def __init__(self, red: int, green: int, blue: int): ...
    @overload
    def __init__(self, hex_code: str): ...

    @property
    def RGBName(self) -> str: ...
