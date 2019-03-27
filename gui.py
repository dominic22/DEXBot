#!/usr/bin/env python3
import cProfile
from dexbot import gui

if __name__ == '__main__':
    cProfile.run('gui.main()', 'gui-stats')
