# 1
# 2 3
# 4 5 6 
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# 22 23 24 25 26 27 28

rows=7
num=1
for i in range(rows):
    res=""
    for j in range(i+1):
        res+=str(num)+" "
        num+=1
    print(res)

# 1
# 2 3
# 4    6
# 7      10
# 11        15
# 16           21
# 22 23 24 25 26 27 28


rows=7
num=1
for i in range(1,rows+1):
    res=""
    for j in range(1,i+1):
        if j==1 or i==rows or i==j:
            res+=str(num)+" "
            num+=1
        else:
            num+=1
            res+=" "+"  "
    print(res)

#         *
#       * *
#     *   *
#   *     *
# * * * * *
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==rows or j==rows or i+j==rows+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)

#          *
#        * *
#      * * *
#    * * * *
#  * * * * *
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j<=rows-i:
            res+=" "+" "
        else:
            res+="*"+" "
    print(res)