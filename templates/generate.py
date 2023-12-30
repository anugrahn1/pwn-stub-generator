#!/usr/bin/python3
import os

try:
    from colorama import Fore, Style
except ImportError:
    print("Please run pip3 install colorama.")
    exit(2)


def main():
    currentDirectory = os.getcwd()
    binary = input("Enter the name of the binary: ")
    print(currentDirectory)
    writeTemplate(currentDirectory, binary)


def writeTemplate(currentDirectory: str, binary: str) -> None:
    currentDirectory += "/get.py"
    if checkFile("./get.py"):
        overwriteChoice = input(
            "There already exists a get.py file, do you want to overwrite it?[Y/N] "
        )
        overwriteChoice = overwriteChoice.lower()
        if overwriteChoice != "y":
            printFail("[-] Didn't write get.py file.")
            exit(1)
    with open(currentDirectory, "w") as f:
        f.write("from pwn import ELF, p64, process, context, ROP, gdb\n\n")
        f.write(f"context.binary = binary = ELF('{binary}')\n")
        f.write("p = process()\n\n\n\n")
        f.write("p.interactive()")
    printSuccess("[+] Wrote get.py file successfuly!")
    exit(0)


def checkFile(filename: str) -> bool:
    return os.path.exists(filename)


def printSuccess(message: str) -> None:
    successMessage = f"{Fore.GREEN}{message}{Style.RESET_ALL}"
    print(successMessage)


def printFail(message: str) -> None:
    failMessage = f"{Fore.RED}{message}{Style.RESET_ALL}"
    print(failMessage)


if __name__ == "__main__":
    main()
