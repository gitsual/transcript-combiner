import inspect
import re


"""
DEBUGGING UTILS
---------------

    varname(p):
        Returns the name of the variable passed as argument.
        
            >>> x = 1
            >>> varname(x)
                'x'
                
            >>> varname(1)
                'p'
    
    print_debug(code_depth, variable_name, text):
        Prints the given text if debug_mode is True.
        The text is indented by the given code_depth.
        The code_depth is the number of tabs to indent the text by.
"""
debug_mode = True
code_depth = -1


def varname(p):
    """
    Returns the name of the variable passed as argument.

    Parameters
    ----------
    p : any
        The variable whose name is to be returned.

    Returns
    -------
    str
        The name of the variable passed as argument.

    Examples
    --------
    >>> x = 1
    >>> varname(x)
    'x'
    >>> varname(1)
    'p'
    """
    # inspect.currentframe() returns the frame object for the caller's frame.
    # inspect.getframeinfo(frame, context=1) returns a 5-tuple:
    #   (filename, line number, function name, code lines, index of current line in code lines)
    for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
        # The regex searches for the pattern varname(varname) in the current line.
        m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
        if m:
            # The regex returns the variable name as group(1).
            return m.group(1)


def print_debug(code_depth, variable_name, text):
    """
    Prints the given text if debug_mode is True.
    The text is indented by the given code_depth.
    The code_depth is the number of tabs to indent the text by.

    Examples:
        >>> debug_mode = True
        >>> print_debug(0, "Hello World!")
        Hello World!
        >>> print_debug(1, "Hello World!")
            Hello World!
        >>> print_debug(2, "Hello World!")
                Hello World!
        >>> debug_mode = False
        >>> print_debug(0, "Hello World!")
        >>> print_debug(1, "Hello World!")
        >>> print_debug(2, "Hello World!")
    """
    global debug_mode

    if debug_mode:
        print(('\t' * code_depth) + str(variable_name) + ': \'' + str(text).replace('\n', '\\n') + '\'')