"""Print matrices with  rows and cols highlighted."""

import sys

USE_COLORS = True
from colorama import Fore, Back, Style, init
init()

def use_colors(enabled=True):
    """Enable or disable colored output.

    :param Boolean enabled: Whether to enabe colors.
    :return: The prvious value.

    """
    global USE_COLORS  # pylint: disable=W0603
    result = USE_COLORS
    USE_COLORS = enabled
    return result



def red(text):
    return (Fore.RED+text+Fore.RESET) if USE_COLORS else text


def green(text):
    return (Fore.GREEN+text+Fore.RESET) if USE_COLORS else text


def blue(text):
    return (Fore.BLUE+text+Fore.RESET) if USE_COLORS else text


def highlight_yellow(text):
    return (Back.YELLOW+text+Back.RESET) if USE_COLORS else text


def highlight_red(text):
    if USE_COLORS :
		return (Back.YELLOW + Fore.RED +text+Fore.RESET+ Back.RESET) 
    else:
        return text

def printmat(A, pos=None,  perm=None, row=-1, col=-1, f=sys.stdout):
    """Print a matrix with a highlighted row and column.

	Parameters
	----------
    A: 
	    A matrix.
    pos: 
	    An entry to render in red.
    perm: 
	     A permutation(the original location of a row). Optional.
    row: 
	     The index of a row to highlight.
    col: 
	     The index of a clumn to highlight.
    f: 
	     A file to print the output to.
		 
	Returns
	-------
	None
    """
    m = len(A)
    n = len(A[0])
    for i in range(m):
        if perm:
            f.write('[%3d]' % perm[i])
        f.write('[')
        for j in range(n):
            if (i, j) == pos:
                f.write(highlight_yellow(red(' % 6s ' % ('%.2f' % A[i][j]))))
            elif row == i or col == j:
                f.write(highlight_yellow(' % 6s ' % ('%.2f' % A[i][j])))
            else:
                f.write(' % 6.2f ' % A[i][j])

        f.write(']\n')
    f.write('\n')
