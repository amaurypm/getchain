#!/usr/bin/env python3
##
## Take a selection of chains from a set of structures and save them as new structures.
##
## Amaury Pupo Merino
## amaury.pupo@gmail.com
##
## This script is released under GPL v3.
##

## Importing modules
import argparse
import os
import sys
import numpy as np
from pymol import cmd

## Functions
"""
    rootname

Get root file name, excluding rest of the path and extensions.
"""
def rootname(filename):
    rootname, ext = os.path.splitext(os.path.basename(filename))
    if ext.lower() == ".gz":
        rootname = os.path.splitext(rootname)[0]

    return rootname

def has_chains(filename, chains):
	struct_chains = set(cmd.get_chains(rootname(filename)))
	chains = set(chains)

	return chains.issubset(struct_chains)


## Main
def main():
	"""Main function.
	"""
	parser=argparse.ArgumentParser(description="Take a selection of chains from a set of structures and save them as new structures.")
	parser.add_argument('structure', nargs='+', help='Any format supported by Pymol.')
	parser.add_argument('-c', '--chains', default='A', help='Chain string containing all the chains to be get, no space between chain IDs. Only single letter chain IDs are supported [default: %(default)s].')
	parser.add_argument('--hetatm', action='store_true', default=False, help="Include hetatm in the output files [default: %(default)s].")
	parser.add_argument('-v', '--version', action='version', version='1.0', help="Show program's version number and exit.")

	args=parser.parse_args()

	chains = "".join(sorted(set(args.chains)))

	cmd.reinitialize() # Just to print Pymol usage as a module waring in here.

	for f in args.structure:
		try:
			cmd.load(f)

		except:
			sys.stderr.write("WARNING: Can not load file {}. Ignoring it.\n".format(f))
			continue

		if not has_chains(f, chains):
			sys.stderr.write("WARNING: Structure {} does not have all requested chains: {}. Ignoring it.\n".format(f, chains))
			continue

		if args.hetatm:
			cmd.save("{}_{}.pdb".format(rootname(f), chains), "{} and chain {}".format(rootname(f), "+".join(chains)))

		else:
			cmd.save("{}_{}.pdb".format(rootname(f), chains), "{} and not hetatm and chain {}".format(rootname(f), "+".join(chains)))

		cmd.delete(rootname(f))

## Running the script
if __name__ == "__main__":
        main()
