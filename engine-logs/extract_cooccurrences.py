import re, json, sys
from collections import defaultdict

with open("DRAFTS2/LORE_F-rev-044.md", encoding="utf-8") as f:
    text = f.read()

# Split into paragraphs (double newline)
paragraphs = re.split(r'\n\n+', text)

piece_re = re.compile(r'\[(P|S|N|T|R)-(\d{2})\]')

cooccurrences = defaultdict(int)
piece_paragraphs = defaultdict(list)

for i, para in enumerate(paragraphs):
    pieces = sorted(set(f"{m[0]}-{m[1]}" for m in piece_re.findall(para)))
    for p in pieces:
        piece_paragraphs[p].append(i)
    for j, a in enumerate(pieces):
        for b in pieces[j+1:]:
            key = tuple(sorted([a, b]))
            cooccurrences[key] += 1

# Sort by weight descending
edges = sorted(cooccurrences.items(), key=lambda x: -x[1])

print(f"Pieces: {len(piece_paragraphs)}")
print(f"Edges (co-occurrence): {len(edges)}")
print()
for (a, b), w in edges:
    print(f"  {a} -- {b}  [weight={w}]")
