#engineSpeed = [800, 2000, 3000, 4000, 4750, 5930, 6200]
curve = [115, 150, 170, 175, 189, 200, 221, 245, 263, 278, 303, 324, 368, 385, 412, 420, 450, 468, 489, 502, 512, 538, 568, 604, 635, 689, 701, 712, 734, 745]


def FindPositionOnCurve(curve, ratio = 0.5):
    maxLoops = round(len(curve)**0.5) + 1
    testIndex = round(len(curve) / 2)
    offset = testIndex 
    targetValue = curve[0] + (curve[-1] - curve[0]) * ratio
    counter = 0
    isLocated = False
    result = [0, 0]

    if ratio == 0:
        isLocated = True
        result[0] = 0
        print(f"Target value was located at index: 0 ({curve[0]})") 
    if ratio == 1:
        isLocated = True
        result[0] = len(curve) - 1
        result[1] = len(curve) - 1
        print(f"Target value was located at index: {result[0]} ({curve[-1]})") 

    while isLocated == False:
        print(f"The test index is: {testIndex}")

        if curve[testIndex] == targetValue or testIndex == 0:
            isLocated = True
            result[0] = testIndex
            print(f"Target value was located at index: {testIndex} ({curve[testIndex]})") 

        elif curve[testIndex] < targetValue: # Check if test index is smaller
            if curve[testIndex + 1] > targetValue: # Check if the next index is larger
                isLocated = True
                print(f"Target value ({targetValue}) was located between index {testIndex} ({curve[testIndex]}) and index {testIndex + 1} ({curve[testIndex + 1]})") 
                result[0] = testIndex
                result[1] = testIndex + 1

            offset = round(offset / 2)
            testIndex += offset # New test index half way up in list 
        else:
            if curve[testIndex - 1] < targetValue: # Check if the previus index is smaller
                isLocated = True
                print(f"Target value ({targetValue}) was located between index {testIndex - 1} ({curve[testIndex - 1]}) and index {testIndex} ({curve[testIndex]})") 
                result[0] = testIndex - 1
                result[1] = testIndex

            offset = round(offset / 2)
            testIndex -= offset # New test index half way down in list

        counter += 1
        if counter == maxLoops:
            isLocated = True  
            print("Error: The value could not be located")

    return result
    

x1, x2 = FindPositionOnCurve(curve, 0.65)

print(curve[x1])
print(curve[x2])