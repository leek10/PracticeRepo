# Python Badge Redo

# This is my attempt at re-trying the project Euler and some histogram problems
# Problem 1: Multiples of 3 or 5 (goal: 233168)
numList = [3, 5]
numMax = 1000
numSum = 0

for n in range(0, numMax):
    if n%3 == 0 or n%5 == 0:
        numSum += n
print('The sum of all the multiples of 3 or 5 below 1000 is', numSum)

# Problem 2: Even Fibonacci Numbers (goal: 46137632)
currTerm, prevTerm = 1, 1
numMax = 4000000
numSum = 0

while currTerm <= numMax:
    if currTerm%2 == 0:
        numSum += currTerm
    currTerm += prevTerm
    prevTerm = currTerm - prevTerm
print('The sum of the even-valued terms in the Fibonacci sequence below four million is', numSum)

# Problem 3: Largest Prime Factor (goal: 6875)
numMax = 600851475143
divisor = 2

while divisor * divisor < numMax: 
    while numMax%divisor == 0:
        numMax /= divisor
    divisor += 1
print('The largest prime factor of the number 600,851,475,143 is', numMax)

# Problem 4: Create a histogram of a normal distribution
    # Use a random number generator, numpy, and matplotlib

