#!/bin/bash
python -m cProfile -o analyse.stat $1
clear
python stats.py
