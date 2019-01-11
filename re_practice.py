# Just some practice
# Sources of inspiration: 
# - https://pythonspot.com/regular-expressions/
# - https://docs.python.org/2.7/howto/regex.html#regex-howto

# Metacharacters: . ^ $ * + ? { } [ ] \ | ( )
# [ ]: Specify a character class; individual characters or a range of characters
# ^: A match to characters NOT listed 
# \: Come before various characters that signify a specific search criteria, e.g.
#   \d: Any decimal digit, same as [0-9]
#   \[: Searches for '[' (a metacharacter that is stripped off its special meaning)
# *: Match zero or more times
# +: Matches one or more times
# ?: Matches zero or once (something being optional)
# {m,n}: At least m matches (default if omitted: 0), and at most n (default if omitted: Infinity)

import re

find_pid = re.compile(r"""
  [0-9]{4,5}        # Project number 4-5 numbers long, e.g. 5292 or 12830
  -PID-             
  [0-9]{3,4}        # Pipe design number 3-4 numbers long, e.g. 731 or 7904
  (\S?[^_]*)        # Optional trailing text in pipe design number that is not underscore, e.g. a or b
  """, re.VERBOSE)

find_pid2 = re.compile(r"""
  [0-9]+        # Project number 4-5 numbers long, e.g. 5292 or 12830
  \S+             
  [0-9]+        # Pipe design number 3-4 numbers long, e.g. 731 or 7904
  (\S?[^_]*)        # Optional trailing text in pipe design number that is not underscore, e.g. a or b
  """, re.VERBOSE)


p1 = "12830-PID-402_PF-06"
p2 = "5292-PID-431_PR-08"
p3 = "12416-PID-623b_GIR-06_btm"
ps = [p1, p2, p3]

pids = [find_pid.match(p).group() for p in ps]
print(pids)

pids2 = [find_pid2.match(p).group() for p in ps]
print(pids2)
