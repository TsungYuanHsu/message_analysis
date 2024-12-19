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


# filter message whose length is lower than 100
count_d_lower_100 = 0
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
        count_d_lower_100 += 1
print('In total, there are', count_d_lower_100, 'messages whose length is lower than 100')
print(len(new))
print(new[0])

new_good = []
for d in data:
    if 'good' in d:
        new_good.append(d)

print('In total, there are',len(new_good), 'messages mentioning good')