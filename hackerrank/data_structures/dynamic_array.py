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
    printAnswer = []
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
        printAnswer.append(lastAnswer)
        # print value of lastAnswer
        #print(lastAnswer)
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
    return printAnswer


new input = 
100000 100000
1 740048951 924919680
1 129818301 12799555
1 330533820 889201598
1 197125749 318174700
1 603690888 520006188
1 4559415 906633769
1 353263281 296658390
1 976488274 768390744
1 922946810 485631967
1 5666709 189571204
1 867874724 454534422
1 391523798 243557156
1 567333065 132409353
1 216021110 64927271
1 326096796 123561806
1 725248096 920547678
1 954443987 784730066
1 674840519 183463026
1 694919598 143106131
# {-truncated-}

new output = 
440552560
321691100
21075956
727198126
251468495
866420844
204296234
627037796
256702893
242481312
431091665
923578431
94673176
891979511
827153086
932513768
846438092
63858795
291131405
192832422
#{-truncated-}
