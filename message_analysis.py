# Message analysis

data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
        count += 1
        if count % 1000 == 0:
            print('It is', count, 'th runs')      
print('It is done running,', 'There are in total', count, 'messages')


# Calculate average message length
length = 0
count_d = 0
for d in data:
    length += len(d)
    count_d += 1
    if count_d == len(data):
        print('The average length of message is', length/len(data))