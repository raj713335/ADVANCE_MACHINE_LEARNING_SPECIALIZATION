import math

string=str(input())

col=math.ceil(len(string)**0.5)
row=col-1

if row*col<len(string):
    row+=1


listx=[]

print(row,col)

iter=0
for i in range(0,row):
    listx.append(list(string[iter:iter+col]))
    iter+=col

# if len(listx[-1])<=col:
#     temp=col-len(listx[-1])-1
#     print(temp)
#     for i in range(temp,0,-1):
#         xx=listx[-(i+1)].pop()
#         print(xx)
#         listx[-(i)].insert(0,xx)
print(listx)
listx[-1]=[*listx[-1],*['' for x in range(col)]][:col]
output=''

for j in range(0,col):
    for i in range(0,row):
        output+=(listx[i][j])
    output+='0'

print(output)

print(listx)

for i in range(0,len(output)):

    if output[i]=='0':
        try:
            if output[i+1]!='0':
                print(' ',end='')
            else:
                pass
        except:
            pass
    else:
        print(output[i],end="")