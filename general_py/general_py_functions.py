########################################################################################################################

# Define ANSI escape codes for text styling and formatting
class format_style:
    """
    Class containing ANSI escape codes for text formatting, colouring, and styling.
    """
    # Special Text Colors
    FAIL = "\033[91m"
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    # Text Colors
    BLACK = "\033[30m"
    BLUE = "\033[34m"
    CYAN = "\033[36m"
    DARK_GREEN = "\033[2;32m"
    GREEN = "\033[32m"
    LIGHT_BLUE = "\033[94;1m"
    MAGENTA = "\033[35m"
    ORANGE = "\033[38;5;208m"
    PURPLE = "\033[35;1m"
    RED = "\033[31m"
    WHITE = "\033[37m"
    YELLOW = "\033[33m"
    # Background Colors
    BG_BLACK = "\033[40m"
    BG_BLUE = "\033[44m"
    BG_CYAN = "\033[46m"
    BG_DARK_GREEN = "\033[2;42m"
    BG_GREEN = "\033[42m"
    BG_LIGHT_BLUE = "\033[104m"
    BG_MAGENTA = "\033[45m"
    BG_ORANGE = "\033[48;5;208m"
    BG_PURPLE = "\033[105m"
    BG_RED = "\033[41m"
    BG_WHITE = "\033[47m"
    BG_YELLOW = "\033[43m"
    # Text Formatting
    BLINK = "\033[5m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    HIDDEN = "\033[8m"
    INVERSE = "\033[7m"
    ITALIC = "\033[3m"
    STRIKETHROUGH = "\033[9m"
    UNDERLINE = "\033[4m"
    # Reset
    ENDC = "\033[0m"

########################################################################################################################

# Function to format and print styled text
def print_format(texts, indent=0, pad_width=0, style=format_style.BLUE + format_style.BOLD):
    """
    Format and print text with ANSI styling, padding, and indentation.

    Parameters:
        texts (list of str): List of texts to format and display.
        indent (int or list of int): Indentation level (4 spaces per level) or a list of levels.
        pad_width (int or list of int): Width for padding text or a list of widths.
        style (str or list of str): ANSI escape code(s) for styling or a list of styles.
    """
    # Ensure parameters are lists for iteration
    indent = [indent] * len(texts) if not isinstance(indent, list) else indent
    pad_width = [pad_width] * len(texts) if not isinstance(pad_width, list) else pad_width
    style = [style] * len(texts) if not isinstance(style, list) else style

    formatted_texts = []
    for i, text in enumerate(texts):
        # Indent the text
        text = str(text)
        indented_text = " " * (indent[i] * 4) + text
        # Pad the text to specified width
        padding_length = pad_width[i] - len(indented_text)
        padded_text = indented_text + " " * max(0, padding_length)
        # Apply styling if specified
        styled_text = style[i] + padded_text + format_style.ENDC if style[i] else padded_text
        formatted_texts.append(styled_text)

    # Print the formatted texts
    print("".join(formatted_texts))

########################################################################################################################

# Function to format the tqdm string
def tqdm_format(desc, length=52, indent=0, style=None):
    """
    Format the tqdm description with padding and optional styling.

    Parameters:
    desc (str): The description to display.
    length (int): The total length of the padded description.
    indent (int): The number of indent levels (4 spaces per level).
    style (str): Optional ANSI escape code for styling.

    Returns:
    tuple: Padded description and bar format string.
    """
    # Add spaces for indentation
    desc = str(desc)
    indented_desc = ' ' * (indent * 2) + desc
    # Calculate the padding needed for the description
    padding_length = length - len(indented_desc)
    # Pad the description to the specified length
    padded_desc = indented_desc + ' ' * padding_length
    # Apply style
    if style is None:
        padded_desc = padded_desc
    else:
        padded_desc = style + padded_desc + format_style.ENDC
    # Ensure the progress bar starts at the same position
    bar_format = '{l_bar}{bar}| {n_fmt:>12}/{total_fmt:<12} {elapsed} <-- {remaining}'

    return padded_desc, bar_format

########################################################################################################################

# Function to delete specified variables from the global namespace
def delete_variables(variables):
    """
    Delete specified variables if they exist in the global namespace.

    Parameters:
        variables (list): List of variable names (as strings) to delete.
    """
    for var in variables:
        if var in globals():
            del globals()[var]

########################################################################################################################
