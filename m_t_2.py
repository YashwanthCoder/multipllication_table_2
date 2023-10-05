table=int(input("enter desired table ="))
times=int(input("how many times want to multiply ="))
count=0
for i in range(1,times+1):
    count=count+1
    i=i*table
    print(table, "*" , count ,"="  , i)
