# Message analysis

data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
print(len(data))