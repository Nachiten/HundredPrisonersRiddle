import random

# Print list with spacing so that they align correctly on the console
def printList(_list):
    for i in range(100):
        value = _list[i]
        if value < 10:
            value = "  " + str(_list[i])
        elif value < 100:
            value = " " + str(_list[i])
        print(str(value) + ", ", end="")

totalWonAmount = 0
totalLostAmount = 0

# Select how many runs with this number
for runs in range(5000):

    # 100 boxes
    boxes = [i for i in range(1, 101)]
    peopleWon = [False for i in range(1, 101)]

    # printList(boxes)
    # print()

    random.shuffle(boxes)

    # printList(boxes)
    # print()

    # 100 people - Cycle strategy
    for playerNumber in range(1, 101):
        # print(f"Player {playerNumber} turn")
        boxNumber = playerNumber - 1
        # Each prisoner gets 50 tries to find his number
        for tries in range(50):
            # print(f"Searching box: {boxNumber + 1}")
            numberFound = boxes[boxNumber]

            # If the number is found, then this prisoner already won
            if numberFound == playerNumber:
                peopleWon[playerNumber - 1] = True
                # print(f'Person {playerNumber} found his number on box {boxNumber}')
                break

            # If the number is not found, then go look for the box with this number on it
            boxNumber = numberFound - 1

        # print(f'Person {playerNumber} could not find his number')

    # Count how many people won and lost
    # foundCount = sum(1 for value in peopleWon if value)
    # notFoundCount = sum(1 for value in peopleWon if not value)
    # print(f'\n{foundCount} DID found their number')
    # print(f'{notFoundCount} DID NOT find their number')

    # Only if everyone won, this run is won
    if all(peopleWon):
        totalWonAmount += 1
    else:
        totalLostAmount += 1

print("\n\nRuns finished. Printing results.\n")

print(f'Won {totalWonAmount} times')
print(f'Lost {totalLostAmount} times')
print(f"Win percent: {(totalWonAmount / totalLostAmount * 100):.2f}%")