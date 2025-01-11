# Message analysis
import re

# Read function
def read(filename):
    data = []
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            data.append(line.strip())
            count += 1
    #         if count % 1000 == 0:
    #             print('It is', count, 'th runs')      
    # print('It is done running,', 'There are in total', count, 'messages')
    print(data[0])
    return data


# Function to calculate average message length
def length_calculate(data):
    length = 0
    count_d = 0
    for d in data:
        length += len(d)
        count_d += 1
        if count_d == len(data):
            print('The average length of message is', length/len(data))


# Function to filter message whose length is lower than 100
def length_filter(data):
    count_d_lower_100 = 0
    new = []
    for d in data:
        if len(d) < 100:
            new.append(d)
            count_d_lower_100 += 1
    print('In total, there are', count_d_lower_100, 'messages whose length is lower than 100')
    print(len(new))
    print(new[0])


# Function to calculate word count
def word_count(data):
    new_good = []
    for d in data:
        if 'good' in d:
            new_good.append(d)
    print('In total, there are',len(new_good), 'messages mentioning good')

    new_good_fast = [d for d in data if 'good' in d]
    print('In total, there are',len(new_good_fast), 'messages mentioning good')

    new_bad_fast = ['bad' in d for d in data]
    print(new_bad_fast)


# Calculate each word occurs how many times
def each_word_count(data):
    word_count = {}
    for d in data:
        d_split = re.split('[:."-/+=; ,()?!]', d)
        for word in d_split:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    print(len(word_count))
    return word_count


# Omly print words repeating certain times
def filter_word_count(word_count):
    for word in word_count:
        if word_count[word] >= 100000:
            print(word, word_count[word])


# Let user input word and search repeating times
def user_search(word_count):
    while True:
        user_word_input = input('Please input the word to search repeating count(Type "Break" to leave): ')
        if user_word_input == 'Break':
            print('Leave searching function')
            break
        elif user_word_input in word_count:
            print('This', user_word_input, 'repeats', word_count[user_word_input], 'times')
        else:
            print('This word is not mentioned')


def main():
    data = read('reviews.txt')
    length_calculate(data)
    length_filter(data)
    word_count = each_word_count(data)
    filter_word_count(word_count)
    user_search(word_count)

main()