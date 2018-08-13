#Free Associations Game

This is a word game similar to Codenames Duet (2+ player cooperative game)

## Usage:

### 1) Build a board:

```
python genwords.py
open board.html
```

This creates a file, board.html, which you can print in landscape mode.


### 2) Build keys:

```
python genkeys.py
```

This creates 2 files, a.html and b.html. It also prints out the URL you should use to load the keys on separate devices.

### 3) Load the keys on separate computers/phones

Start the server:
```
python -m SimpleHTTPServer
```
This will keep running until you press ctrl-C.

In the prior step we created 2 key web pages: a.html and b.html, which you need to visit from separate computers/smartphones, one on each side of the board.
Make sure you are connected to the same wifi as the computer which is doing the server! :)
