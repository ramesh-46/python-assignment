
#Given a sorted array of positive and negative numbers. You have to Square it and sort it. Constraint : Time complexity O(n) 

#Input: [-12, -8 , -7, -5, 2, 4, 5, 11, 15] 
#Output : [4, 16, 25, 25, 49, 56, 121, 144, 225] 







array= [-12, -8 , -7, -5, 2, 7, 5, 21, 15] 
array2=[]
for i in range(len(array)):
    array2.append(array[i]**2)

array2.sort()
print(array2)