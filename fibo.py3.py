#py3
#write a prorgram to print 'n' terms of fibonnaci series using iteration"

nterms=int(input("how many terms"))
#first two terms
n1,n2=0,1
count=0
#check if the numbers of terms is valid
if nterms<=0:
    print("please enter the positive number")
#if there is only one term,return n1
elif nterms==1:
    print("Fibonnaci series upyo",nterms)
    print(n1)
else:
    print("Fibonnaci sequence:")
    while count<nterms:
        print(n1,end=" ")
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
