# Lightweight Python script to generate a template for PWN challenges


## Installation:

1. `wget https://raw.githubusercontent.com/anugrahn1/pwn-stub-generator/main/templates/generate.py -O generate.py`

2. `sudo cp generate.py /usr/bin/generate`

## Using the program:

After following the Installation instructions, type `generate`.
It will ask for a binary. Type in the name of the file the CTF provided, and a file called `get.py` will be generated in the current directory.

If it detects another `get.py` file, it will ask to overwrite it. 

## Example:

This is the file it creates, where `test` is the name of the binary you typed:

```py
from pwn import ELF, p64, p32, process, context, ROP, gdb, log, u64, u32

context.binary = binary = ELF('test')
p = process()



p.interactive()
```

