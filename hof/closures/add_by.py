def addByX(a):
    return lambda b: print(a + b)

addByTwo = addByX(2);

addByTwo(1)
addByTwo(2)
addByTwo(3)

addByThree = addByX(3);
addByThree(1)
addByThree(2)

addByFour = addByX(4);
addByFour(4)
addByFour(10)
