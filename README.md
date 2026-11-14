# Make the AI judge happy

Entry for the make.fun bounty "Make the AI judge happy" (ai-happy-01).

The entry is one joyful image: a smiling golden-retriever puppy in a
sunny flower meadow, bright warm colours, clear subject, no text.

## How it works

`main.py` deterministically copies the bundled image `happy.png`
(768x768 PNG, under 1 MiB) to `/output/entry.png`. No network, no
randomness, no clock — two runs write byte-identical output.

## Run locally

```sh
python3 main.py
```

Writes `/output/entry.png`.
