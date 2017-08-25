import pstats

p = pstats.Stats('analyse.stat')
p.strip_dirs().sort_stats('time').print_stats(20)
