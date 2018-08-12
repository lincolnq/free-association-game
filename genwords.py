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

ul {{
list-style-type: none;
}}

li {{
display: inline-block;
width: 19%;
text-align: center;
padding: 1em 0;
}}
</style>
<body>
<ul>
{items}
</ul>
</body>
</html>
'''

item_template = '''
<li>{item}</li>
'''

def generate():
    selection = random.sample(words, 25)

    items = []
    for w in selection:
        item_html = item_template.format(item=w)
        items.append(item_html)

    html = template.format(items=''.join(items))
    outf.write(html)

generate()
