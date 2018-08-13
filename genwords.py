import random

words = open('words.txt').read().split('\n')
outf = open('board.html', 'w')

template = '''
<!doctype html>
<html>
<style>
body {{
font-family: sans-serif;
font-size: 24pt;
}}

td {{ padding: 0.5em 1em; border: 1px solid #eee; text-align: center; }}
table {{ border-collapse: collapse; }}
.rev {{
color: #aaa;
transform: rotate(180deg);
}}
p {{ margin: 0; }}

</style>
<body>
<table>
{items}
</table>
</body>
</html>
'''

def render(items):
    def mkrow(row):
        """Given 5 words in a row, render the row"""
        return ''.join('<td><p class="fwd">{word}</p><p class="rev">{word}</p></td>'.format(word=word) for word in row)
    def splitrows(items):
        """Given 25 items, split it into a list of 5-item rows"""
        return [items[i:i+5] for i in range(0, 25, 5)]

    items_html = '\n'.join('<tr>{items}</tr>'.format(items=mkrow(row)) for row in splitrows(items))
    html = template.format(items=''.join(items_html))
    return html

def generate():
    selection = random.sample(words, 25)
    html = render(selection)

    outf.write(html)

generate()
