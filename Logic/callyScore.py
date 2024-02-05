import os
import math

#-------------------------------------scorecards ------------------------------------------------
DressForLess =  [4, 4, 5, 3, 4, 3, 5, 5, 5, 3, 4, 5, 4, 4, 5, 3, 6, 4] ### 76 - Logan and Preston
DriveNThriive = [4, 4, 6, 2, 4, 3, 5, 4, 4, 3, 3, 4, 4, 5, 4, 3, 4, 5] ### 71
Osama = [4, 4, 7, 3, 6, 3, 3, 5, 4, 4, 6, 4, 5, 6, 5, 3, 5, 5] ### 82 - Jordan and Jared
GG =            [5, 3, 5, 3, 5, 3, 6, 5, 4, 4, 4, 5, 5, 5, 3, 3, 4, 3] ### 75
DaddysMoney =   [4, 3, 5, 2, 3, 3, 4, 4, 4, 3, 5, 4, 4, 4, 4, 3, 4, 4]

#-------------------------------------scorecards ------------------------------------------------


#------------------------------------------------------------------------------
# Make this into a method? 
#Ask for the scores for each hole and append to scorecard ---  THIS WORKS
# hole = 1
# while hole <= 18:
#     userInput = int(input("Enter Score for Hole " + str(hole) + ": "))
#     scorecard.append(userInput)
#     hole += 1
#-------------------------------------------------------------------------------

# returns the last digit from the total score (ej: 82 - returns  2, 130 - returns 0)
def intSplit(total):
    list_of_digits = [int(i) for i in str(total)]
    # print("Last Digit of Score: " + str(list_of_digits[-1]))
    return list_of_digits[-1]

# use to determine if -2, -1, 0, +1, +2 --- This works 82 - 2
def handicapAdjustment(total):
    if intSplit(total) == 6 or intSplit(total) == 1:
        adjustment = -2
        return adjustment
    elif intSplit(total) == 7 or intSplit(total) == 2:
        adjustment = -1
        return adjustment
    elif intSplit(total) == 8 or intSplit(total) == 3:
        adjustment = 0
        return adjustment
    elif intSplit(total) == 9 or intSplit(total) == 4:
        adjustment = 1
        return adjustment
    elif intSplit(total) == 0 or intSplit(total) == 5:
        adjustment = 2
        return adjustment
    
# Determine the Handicap deduction
def initDeduction(total, SC):

    # No Deduction - 72 and lower
    if total <= 72:
        adjustment = 0
        return adjustment
    
    # Half of worst hole - 73, 74, 75
    elif total > 72 and total <= 75:
        if total == 73:
            deduction = math.ceil((SC[0] / 2) - 2)
            return deduction
        elif total == 74:
            deduction = math.ceil((SC[0] / 2) - 1)
            return deduction
        elif total == 75:
            deduction = math.ceil(SC[0] / 2)
            return deduction

    # Full Hole Deduction - 76, 77, 78, 79, 80
    elif total > 75 and total <= 80:
        SC.pop(16)
        SC.pop(16)
        SC.sort(reverse = True)
        deduction = math.ceil(SC[0])
        return deduction

    # 1 1/2 Hole Deduction - 81, 82, 83, 84, 85
    elif total > 80 and total <= 85:
        SC.pop(16)
        SC.pop(16)
        SC.sort(reverse = True)     
        deduction = math.ceil(SC[0] + (SC[1] / 2))
        return deduction

    # 2 Hole Deduction - 86, 87, 88, 89, 90
    elif total > 85 and total <= 90:
        SC.pop(16)
        SC.pop(16)
        SC.sort(reverse = True)
        deduction = math.ceil(SC[0] + SC[1])
        return deduction

    # 2 1/2 Hole Deduction - 91, 92, 93, 94, 95
    elif total > 90 and total <= 95:
        SC.pop(16)
        SC.pop(16)
        SC.sort(reverse = True)
        deduction = math.ceil(SC[0] + SC[1] + (SC[2] / 2))
        return deduction

    # 3 Hole Deduction - 96, 97, 98, 99, 100
    elif total > 95 and total <= 100:
        SC.pop(16)
        SC.pop(16)
        SC.sort(reverse = True)
        deduction = math.ceil(SC[0] + SC[1] + SC[2])
        return deduction

    # 3 1/2 Hole Deduction - 101, 102, 103, 104, 105
    elif total > 100 and total <= 105:
        SC.pop(16)
        SC.pop(16)
        SC.sort(reverse = True)
        deduction = math.ceil(SC[0] + SC[1] + SC[2] + (SC[3] / 2))
        return deduction

    # 4 Hole Deduction - 106, 107, 108, 109, 110
    elif total > 105 and total <= 110:
        SC.pop(16)
        SC.pop(16)
        SC.sort(reverse = True)
        deduction = math.ceil(SC[0] + SC[1] + SC[2] + SC[3])
        return deduction

    # 4 1/2 Hole Deduction - 111, 112, 113, 114, 115
    elif total > 110 and total <= 115:
        SC.pop(16)
        SC.pop(16)
        SC.sort(reverse = True)
        deduction = math.ceil(SC[0] + SC[1] + SC[2] + SC[3] + (SC[4] / 2))
        return deduction

    # 5 Hole Deduction - 116, 117, 118, 119, 120
    elif total > 115 and total <= 120:
        SC.pop(16)
        SC.pop(16)
        SC.sort(reverse = True)
        deduction = int(math.ceil(SC[0] + SC[1] + SC[2] + SC[3] + SC[4]))
        return deduction

    # 5 1/2 Hole Deduction - 121, 122, 123, 124, 125
    elif total > 120 and total <= 125:
        SC.pop(16)
        SC.pop(16)
        SC.sort(reverse = True)
        deduction = math.ceil(SC[0] + SC[1] + SC[2] + SC[3] + SC[4] + (SC[5] / 2))
        return deduction

    # 6 Hole Deduction - 126, 127, 128, 129, 130
    elif total > 125 and total <= 130:
        SC.pop(16)
        SC.pop(16)
        SC.sort(reverse = True)
        deduction = math.ceil(SC[0] + SC[1] + SC[2] + SC[3] + SC[4] + SC[5])
        return deduction

    else:
        print("Your score is too high - Golf might not be for you!")


def main(scorecard):
    front9 = 0
    back9 = 0
    totalScore = 0

    for x in range(0, 18):
        if x <= 8:
            front9 += scorecard[x]
        elif x > 8 and x <= 18:
            back9 += scorecard[x]

    # Maybe the mostortant piece of the puzzle right here
    totalScore = front9 + back9

    # print(str(handicapAdjustment(totalScore)))

    # at or below par
    if totalScore < 72:
        print("Front 9: " + str(front9))
        print("Back 9: " + str(back9))
        print("Total Score: " + str(totalScore))
        Cally = totalScore - (initDeduction(totalScore, scorecard))
        print("Calloway Score: " + str(Cally))
    # in the tweener zone for calloway system
    elif totalScore > 72 and totalScore <= 75:
        print("Front 9: " + str(front9))
        print("Back 9: " + str(back9))
        print("Initial Score: " + str(totalScore))
        Cally = totalScore - (initDeduction(totalScore, scorecard))
        print("Calloway Score: " + str(Cally))
    elif totalScore > 75:
        print("Front 9: " + str(front9))
        print("Back 9: " + str(back9))
        print("Total Score: " + str(totalScore))

        # Deducitons P1
        cally1 = totalScore - (initDeduction(totalScore, scorecard) + handicapAdjustment(totalScore))
        print("Calloway Score: " + str(cally1))


# main(DriveNThriive)
main(Osama)
# main(DressForLess)
# main(GG)
# main(DaddysMoney)