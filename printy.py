""" A basic terminal printer for printing
in color and with other formatting.
"""
PURPLE = (162, 0, 255)
CYAN = (0, 234, 255)
BLUE = (0, 72, 255)
GREEN = (8, 212, 15)
YELLOW = (255, 251, 0)
RED = (237, 36, 0)
BLACK = (0, 0, 0)


def printc(text='', RGB=(255, 255, 255), *args):
    """Print the passed text with the given formatting.

    Parameters
    ----------
    text : `str`
        String to print to the terminal.

    RGB : `tuple`
        A tuple of three integers representing an
        [R, G, B] color value. Ex: (255, 0, 0) = Red.
        Default = (255, 255, 255)

    *args : `str`
        Additional format options.
        Ex: 'bold', 'underline'

    """
    # Needed to end the formatting
    END = '\033[0m'

    for i in RGB:
        if i < 0 or i > 255:
            raise ValueError("RGB value outside of range.")

    # Setup RGB color
    color = f'\033[38;2;{RGB[0]};{RGB[1]};{RGB[2]}m'

    # Get extra args
    argv = []
    for arg in args:
        argv.append(arg.lower())

    # Apply underline
    if 'underline' in argv:
        color = '[4;'.join(color.split('['))

    # Apply bold
    if 'bold' in argv:
        color = '[1;'.join(color.split('['))

    print(f"{color}{text}{END}")
