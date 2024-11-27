l1 = list(1,2,3,4,5,6,7,8,9)
sum = 0
for(i in l1){
    if(i %% 2 ==0){
        sum =  sum + i
    }
}
print(sum)
