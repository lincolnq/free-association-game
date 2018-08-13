"""Codenames keys (for Duet) are a pair of 5x5 grids.

Each grid square is either a Bystander (white), Answer (green) or Assassin (black).

Each pair of generated grids, call them A and B, should follow the constraints such that:
- there are 9 green, 3 black and 13 white squares on each individual grid
- Of the 9 green on grid A, 3 are green on B, 1 is black and the rest are white;
- Of the black on grid A, 1 is black on B, 1 is green and 1 is white.

Another view of the grid is that each square is a pair of color, and you always
need the same set of color pairs but they are permuted into a random order.
"""

import collections
import random

def gen():
    BASE1 = 'GGGGGGGGGBBBWWWWWWWWWWWWW'
    BASE2 = 'GGGWWWWWBWGBGGGGGWWWWWWWB'
    pairs = zip(BASE1, BASE2)
    random.shuffle(pairs)
    return ''.join(x[0] for x in pairs), ''.join(x[1] for x in pairs)

template = '''
<!doctype html>
<html>
<meta name="viewport" content="width=200, initial-scale=1">
<style>
.G {{ background: #8f8; }}
.B {{ background: #444; }}
.W {{ background: #eee; }}
td {{ width: 30px; height: 30px; border: 1px solid #fff; padding: 0; margin:0; }}
table {{ border: 2px solid #000; border-collapse: collapse; }}
</style>
<body>
<table>
{data}
</table>
</body>
</html>
'''

def write(fn, x):
    def mkrow(s):
        """Given 5 chars, render the row"""
        return ''.join('<td class="{}">&nbsp;</td>'.format(c) for c in s)

    def splitrows(s):
        """Given 25 chars, split it into a list of 5-character rows"""
        return [x[i:i+5] for i in range(0, 25, 5)]

    data = '\n'.join('<tr>{items}</tr>'.format(items=mkrow(row)) for row in splitrows(x))
    html = template.format(data=data)
    f = open(fn + '.html', 'w')
    f.write(html)

import socket
def get_ip_address():
    """Get ip address based on default route"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


(a,b) = gen()
write('a', a)
write('b', ''.join(reversed(b))) # reverse = flip 180 degrees
print('Ok, visit http://{}:8000/a.html (or b.html)'.format(get_ip_address()))
