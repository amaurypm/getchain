# getchain
Take a selection of chains from a set of structures and save them as new structures.

# Usage
```
getchain [-h] [-c CHAINS] [--hetatm] [-v] structure [structure ...]

positional arguments:
  structure             Any format supported by Pymol.

optional arguments:
  -h, --help            show this help message and exit
  -c CHAINS, --chains CHAINS
                        Chain string containing all the chains to be get, no space between chain IDs. Only single letter chain IDs are supported [default: A].
  --hetatm              Include hetatm in the output files [default: False].
  -v, --version         Show program's version number and exit.
  ```

# Installation
This is a Python script, so, you can just run the `getchain.py` file or put a symbolic link in any directory of your PATH.

# Dependencies
* Python3
* argparse
* pymol

