"""
Fix importing from python package by adding project to the path
"""
import sys
from os import chdir, getcwd

chdir('..')
sys.path.append(getcwd())
