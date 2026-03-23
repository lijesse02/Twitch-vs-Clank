import random, json

moves = ["a", "b", "left", "right", "up", "down"]
inputStreams = []
for i in range(100):
    inputStreams.append(random.choices(population=moves, k = 300))
with open("data.json", "w") as f:
    f.write("[\n")
    for i, row in enumerate(inputStreams):
        line = " " + json.dumps(row)
        if i < len(inputStreams) - 1:
            line += ","
        f.write(line+ "\n")
    f.write("]\n")