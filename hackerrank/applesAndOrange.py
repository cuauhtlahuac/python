def countApplesAndOranges(s, t, a, b, apples, oranges):
    #s start house
    #t end house
    #a apple point tree
    #b orange point tree
    totalApples = 0
    totalOranges = 0
    for apple in apples:
        apple_in_the_house = apple + a
        if apple_in_the_house >= s and apple_in_the_house <= t:
            totalApples+=1
            
    for orange in oranges:
        orange_in_the_house = orange + b
        if orange_in_the_house >= s and orange_in_the_house <= t:
            totalOranges+=1
            
    print(str(totalApples) + "\n" + str(totalOranges))

    #Issues
    #Bad operator in py3 "&" changed to "and"
    #break in an if works fine
    

countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])
