print("start dynamic array")

def dynamicArray(n, queries):
    # Write your code here
    # Create an integer, lastAnswer , and initialize it to 0.
    global lastAnswer
    lastAnswer = 0
    # create append variable to say the current value of y
    append = 0
    # 2 types of queries
    print(id(lastAnswer))

    def query_one(x, y):
        seq = ((x ^ lastAnswer) % n)
        # append int "y" to seq
        append = queries[seq] = y
        sequenses[seq].append(append)

    def query_two(x, y):
        print("start query_two()")
        global lastAnswer
        print(id(lastAnswer))
        print(x, lastAnswer)
        seq = ((x ^ lastAnswer) % n)
        print(seq)
        # Find the value of element y% in size in seq and assign it to lastAnswer.
        index = y % len(sequenses[seq])
        print(index)
        lastAnswer = sequenses[seq][index]
        # print value of lastAnswer
        print("last answer two " + str(lastAnswer))
    # Create n sequences variables
    sequenses = {}
    for nseq in range(0, 2):
        sequenses[nseq] = []
    for query in (queries):
        current_query = query[0]
        x = query[1]
        y = query[2]
        if current_query == 1:
            query_one(x, y)
        if current_query == 2:
            query_two(x, y)
    print(sequenses)


number = 2
HRqueries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]

dynamicArray(number, HRqueries)
print("finish dynamic array")

# ISSUES:
# Variables in python avoid changing global values in a traditional way
# https://www.python-course.eu/python3_global_vs_local_variables.php

def dynamicArray(n, queries):
    # Write your code here
# Create an integer, lastAnswer , and initialize it to 0.
    global lastAnswer
    lastAnswer = 0
    # create append variable to say the current value of y
    append = 0
    # 2 types of queries
    def query_one(x, y):
        seq = ((x ^ lastAnswer) % n)
        # append int "y" to seq
        append = queries[seq] = y
        sequenses[seq].append(append)

    def query_two(x, y):
        global lastAnswer
        seq = ((x ^ lastAnswer) % n)
        # Find the value of element y% in size in seq and assign it to lastAnswer.
        index = y % len(sequenses[seq])
        lastAnswer = int(sequenses[seq][index])
        # print value of lastAnswer
        print(lastAnswer)
        #print("WTF")
    # Create n sequences variables
    sequenses = {}
    for nseq in range(0, 2):
        sequenses[nseq] = []
    for query in (queries):
        current_query = query[0]
        x = query[1]
        y = query[2]
        if current_query == 1:
            query_one(x, y)
        if current_query == 2:
            query_two(x, y)  