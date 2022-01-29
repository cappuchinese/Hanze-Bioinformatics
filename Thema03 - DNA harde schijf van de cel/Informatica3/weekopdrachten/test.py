import functools

numbers = ['nul','één','twee','drie','vier','vijf','zes','zeven','acht','negen']
nr = 631452781

r = functools.reduce(lambda x, y:f"{x}-{y}", map(lambda x:numbers[x], [int(v) for v in str(nr)]) )

print(r)
