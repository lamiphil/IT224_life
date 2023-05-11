#!/usr/bin/env python3
from expTools import *

easypapOptions = {
    "-k ": ["max"],
    "-i ": [10],
    "-v ": ["task"],
    "-s ": [2048],
    "-a ": [20],
    "-ts ": [8, 16, 32],
    "--label ": ["square"],
    "-of ": ["max.csv"]
}

# OMP Internal Control Variable
ompICV = {
    "OMP_NUM_THREADS=": [1] + list(range(2, 13, 2))
}

nbrun = 3
# Lancement des experiences
execute('./run ', ompICV, easypapOptions, nbrun, verbose=False, easyPath=".")

del easypapOptions["-ts "]
easypapOptions["--label "] = ["line"]
easypapOptions["-th "] = [1]
easypapOptions["-tw "] = [32, 64, 128, 256, 512]

execute('./run ', ompICV, easypapOptions, nbrun, verbose=False, easyPath=".")

# Lancement de la version seq avec le nombre de thread impose a 1

easypapOptions = {
    "-k ": ["mandel"],
    "-i ": [10],
    "-v ": ["seq"],
    "-s ": [512, 1024],
}
ompICV = {"OMP_NUM_THREADS=": [1]}
execute('./run ', ompICV, easypapOptions, nbrun, verbose=False, easyPath=".")
