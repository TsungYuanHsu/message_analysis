# Message analysis

data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
        count += 1
        if count % 1000 == 0:
            print('It is', count, 'th runs')

print(len(data))
print(data[0])
print('---------------------------------')
print(data[1])