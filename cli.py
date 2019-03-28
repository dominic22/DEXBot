#!/usr/bin/env python3

import cProfile
from dexbot import cli

if __name__ == '__main__':

    cProfile.run('cli.main()', 'cli-stats')

    #cli.main()
