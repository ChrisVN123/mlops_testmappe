import pstats

# Load the profile data
stats = pstats.Stats('output.prof')

# Print a summary, sorted by cumulative time
stats.strip_dirs().sort_stats('cumulative').print_stats()

# You can also try different sort options, e.g.:
stats.sort_stats('time').print_stats(10)  # Top 10 by total time
stats.sort_stats('calls').print_stats(10)  # Top 10 by call count
