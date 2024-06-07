#trying out the famous challenge of finding the two missing number in an array

import math

def findMissingNum(arr):
  #add 2 since there are two missing numbers
  correctLen = len(arr) + 2

  #formula to get sum of list of n numbers that increment by 1
  sumCorrectArr = (correctLen * (correctLen + 1)) / 2

  #use python's built in sum() function to get sum of array that needs to be checked
  sumMissingNumbers = sumCorrectArr - sum(arr)
  avgMissingNumbers = sumMissingNumbers / 2

  #avgMissingNumbers lies between the two missing numbers.
  #so we iterate through the array until avgMissingNumbers to find the first missing number.
  #we then subtract the first missing number found from sumMissingNumbers to get the second missing number

  n = math.ceil(avgMissingNumbers)
  #initialise missing number as 0
  firstMissing =0

  for i in range(n+1):
    a = arr[i]
    if (a != i+1):
      firstMissing+=i+1
      print(f"the first missng number is {firstMissing}")
      print(f"the second number is {sumMissingNumbers-firstMissing}")
      break

array = [1,2,3,4,5,7,8,9,10,11,13,14,15]
findMissingNum(array)
