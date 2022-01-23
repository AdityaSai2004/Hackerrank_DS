#using inbuilt functions
n=int(input())
li=list(map(int,input().split(' ')))
li.reverse()
for i in li:
    print(i,end=' ')

#def function
#separate code

def rev(li):
    return li[::-1]
