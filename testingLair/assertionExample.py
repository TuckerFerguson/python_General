#Author Tucker Ferguson
#param two even numbers
#testing assertion method to validate info passed into function and output by function
def spam(a,b) :
    assert(a % 2 == 0)
    a = a + b
    assert(a % 2 == 0)
    print('both are even %d %d'%(a,b))
spam(2,4)