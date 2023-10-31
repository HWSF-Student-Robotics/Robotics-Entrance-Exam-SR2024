import time
import asyncio
### You can use these imports or anything else within reason
# import math
# import threading
# import multiprocessing
# import numpy as np
# from numba import jit, cuda 

Limit = 15000

async def Example(Limit):
    PrimeNumbers = []
    StartNumber = 2

    while StartNumber <= Limit:
        DivideBy = 2
        Prime = True

        while DivideBy < (StartNumber-1):
            DivideBy += 1
            if(StartNumber%DivideBy) == 0: 
                Prime = False
        
        if Prime == True: 
            PrimeNumbers.append(StartNumber)
        
        StartNumber += 1

    return PrimeNumbers

async def YourCode(Limit):
    ### Your code goes here
    ### You can change stuff outside of this function within reason
    ### return the list of primes
    return [0, 1, 2, 3, 5, 7, 11, 13]

# Run Example
start = time.time()
ExamplePrimeNumbers = asyncio.run(Example(Limit))
end = time.time() - start
print("Number of primes in example", len(ExamplePrimeNumbers))
print("Previous function Time taken: ", end)

# Run YourCode
start = time.time()
PrimeNumbers = asyncio.run(YourCode(Limit))
end = time.time() - start
print("Number of primes in your code", len(PrimeNumbers))
print("New function Time taken: ", end)

# Compare primes found and return missing primes and numbers that are not prime
MissingPrimes = []
NotPrimes = []
for i in ExamplePrimeNumbers:
    if i not in PrimeNumbers:
        MissingPrimes.append(i)
for i in PrimeNumbers:
    if i not in ExamplePrimeNumbers:
        NotPrimes.append(i)

print("Missing primes: ", MissingPrimes)
print("Not primes: ", NotPrimes)