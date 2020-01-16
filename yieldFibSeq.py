#@Author Tucker Ferguson 12/28/2019
#Utilizing Generator for Fibonacci Sequence
seqLen = int(input()) 

def fibGen(seqLen):
    a,b = 0,1
    while(a < seqLen) :
        yield(a) 
        a,b = b,a+b

for i in fibGen(seqLen) :
    print(i)
