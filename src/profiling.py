import cProfile
import pstats
from main import main
from sys import argv

if len(argv) < 3:
    print("Usage: python profiling.py [output file] [run new test(boolean)]")
    exit()

if argv[2] == "True" or argv[2] == "1":
    cProfile.run("main()", argv[1])

p = pstats.Stats(argv[1])
p.strip_dirs()
p.sort_stats("time")
p.print_stats(.05)