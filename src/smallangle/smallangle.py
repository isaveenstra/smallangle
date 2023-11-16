# Name: Isa Veenstra
# Student number: 14578522
# This code creates a click group of functions that calculate the sin 
# and tan of a number of x-values between 0 and 2 pi 

import click
import numpy as np
from numpy import pi
import pandas as pd

# create a click group smallangle 
@click.group()
def smallangle():
    pass

# add the option --number variable that can be used in the function sin
@smallangle.command()
@click.option(
    "-n",
    "--number",
    default=2,
    help="Number of x-values between 0 and 2 pi.",
    show_default=True,  # show default in help
    )
# create a function sin that determines the sin of a number of x-values between 0 and 2 pi 
def sin(number):
    """Calculate the sin of a number of x-values between 0 and 2 pi in steps
    
    Args: 
	    number (int): number of x-values between 0 and 2 pi
    
    Returns: 
	    sin of the number of x-values between 0 and 2 pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

# add the option --number variable that can be used in the function tan 
@smallangle.command()
@click.option(
    "-n",
    "--number",
    default=2,
    help="Number of x-values between 0 and 2 pi.",
    show_default=True,  # show default in help
)
# create a function tan that determines the tan of a number of x-values between 0 and 2 pi
def tan(number):
    """Calculate the tan of a number of x-values between 0 and 2 pi in steps

    Args:
        number (int): number of x-values between 0 and 2 pi

    Returns: 
	    tan of the number of x-values between 0 and 2 pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return

if __name__ == "__main__":
    smallangle()