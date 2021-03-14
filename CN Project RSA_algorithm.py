def isPrime (no):
        flag = True
        for i in range (2, no // 2 + 1):
                if no % i == 0:
                        flag = False
                        break
        return flag

def gcd (a, b): 
    if b == 0: 
        return a 
    else: 
        return gcd (b, a % b)

def encoder(string):
	encodedList=[]
	for c in string:
		encodedList.append(ord(c))
	return encodedList

def listToString(List):
	string=''
	for var in List:
		string=string+str(var)
	return string

def decoder(encodedList):
	decoded=''
	for c in encodedList:
		decoded=decoded+chr(c)
	return decoded

from random import *

ept = input("Enter text message:")

encodedList = encoder(ept)
print('Encoded Text:',listToString(encodedList))

primes = [2]
for i in range(3, 100, 2):
        if isPrime(i):
                primes.append(i)

p = choice ( primes )
q = choice ( primes )
        
n = p * q
fi = (p - 1) * (q - 1)

for e in range (2, fi):
        if gcd (e, fi) == 1:
                break

for i in range(1,10):
        x = 1 + i*fi
        if x % e == 0:
                d = x // e
                break

ct = []
dpt1 = []
for k in range(0,len(encodedList)):
        
        tempCt = encodedList[k] ** e % n
        tempDpt = tempCt ** d % n
        ct.append(tempCt)
        dpt1.append(tempDpt)

dpt = decoder(dpt1)
print("Cipher Text:",listToString(ct))
print('Decrypted Text:',listToString(dpt1))
print("Decoded Text:",dpt)
input()
