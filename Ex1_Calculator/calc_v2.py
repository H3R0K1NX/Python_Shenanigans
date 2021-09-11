"""
Task #1 - Calculator using numpy
Author: Eldan Gurevich
Version: 1.00
Last Update: 11.9.2021
"""
from termcolor import colored


class TerminalColors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


import numpy as np


def mult(lists, k: int) -> list:
    """
    Performs scalar multiplication on the given list(s)
    with the given scalar value.

    Args:
        lists (list): List(s) of integers.
        k (int): Scalar value.
    Returns:
        list: List of the multiplication of the scalar with the list(s).
    """
    return (np.multiply(lists, k)).tolist()


def multV(lists) -> list:
    """
    Performs dot product multiplication on the given lists.

    Args:
        lists (list): Lists of integers.
    Returns:
        list: List of the Dot product of the given lists.
    """
    return list(np.prod(lists, 0))


def sum(lists) -> list:
    """
    Performs summary on the given lists.

    Args:
        lists (list): Lists of integers.
    Returns:
        list: Summary list of the given lists.
    """
    return list(np.sum(lists, 0))


def calc(func_name: str, *user_input: tuple) -> list:
    """
    Function dispatcher.

    Args:
        func_name (str): Name of the desired function.
        *user_input (tuple): Packed list(s) or scalar value to be used
        in the chosen function.
    Returns:
        list: List output of one of the functions.
    """
    dict = {
        "mult": mult,
        "sum": sum,
        "multV": multV,
    }
    return dict[func_name](*user_input)


def populate_lists_loop() -> list:
    """
    Populates desired amount of lists to be sent into one of the functions.

    Args:
        None.
    Returns:
        list: Populated list or List of populates lists.
    """
    n = int(input("Enter the amount of desired lists: "))
    total_ls = []
    for _ in range(n):
        ls = input(
            f"Enter element for the list number {_+1} each seperated with comma: "
        )
        ls = list(map(int, ls.split(",")))
        total_ls.append(ls)
    return total_ls


def calculator_menu():
    choice = " "
    while choice != "4":
        print("###########################################")
        print(colored("\tCalculator menu", "green", attrs=["underline"]))
        print(colored("[1].", "cyan") + "Multiply list by constant")
        print(colored("[2].", "blue") + "Multiply two lists of an equal size")
        print(colored("[3].", "magenta") + "Sum of variadic lists [Minimum of two]")
        print(colored("[4].", "yellow") + "Quit the program")
        print("###########################################")
        choice = input("Please select an option: ")
        print(f"The selected choice is: [{choice}]")
        if choice == "1":
            k = int(input("Enter a scalar value: "))
            print(f"Result: {calc('mult', populate_lists_loop(), k)}\n")
        elif choice == "2":
            print(f"Result: {calc('multV', populate_lists_loop())}\n")
        elif choice == "3":
            print(f"Result: {calc('sum', populate_lists_loop())}\n")
    print(colored("\n\tYou've decided to quit the program...\n\n", "red"))


calculator_menu()
