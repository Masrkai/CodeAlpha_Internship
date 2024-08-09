#ANSII.py


#------------------------------------------------------*Sweet Ergonomics:
class ANSIColor:
    COLORS = {
        'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34,
        'magenta': 35, 'cyan': 36, 'white': 37,
        'bright_black': 90, 'bright_red': 91, 'bright_green': 92,
        'bright_yellow': 93, 'bright_blue': 94, 'bright_magenta': 95,
        'bright_cyan': 96, 'bright_white': 97
    }

    BACKGROUNDS = {
        'black': 40, 'red': 41, 'green': 42, 'yellow': 43, 'blue': 44,
        'magenta': 45, 'cyan': 46, 'white': 47,
        'bright_black': 100, 'bright_red': 101, 'bright_green': 102,
        'bright_yellow': 103, 'bright_blue': 104, 'bright_magenta': 105,
        'bright_cyan': 106, 'bright_white': 107
    }

    STYLES = {
        'reset': 0, 'bold': 1, 'dim': 2, 'italic': 3, 'underline': 4,
        'blink': 5, 'inverse': 7, 'hidden': 8, 'strikethrough': 9
    }

    @staticmethod
    def format_text(text, color=None, bg_color=None, style=None):
        color_code = ANSIColor.COLORS.get(color, '')
        bg_color_code = ANSIColor.BACKGROUNDS.get(bg_color, '')
        style_code = ANSIColor.STYLES.get(style, '')

        codes = ';'.join(filter(None, [str(style_code), str(color_code), str(bg_color_code)]))

        return f"\033[{codes}m{text}\033[0m"