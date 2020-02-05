import math
import random

test_arr = []

#fills arrayb with random numbers 0-99
for i in range(0,100):
    test_arr.append(int(random.random()*100))

print(test_arr)

def countReverses(user_array):
    reverse_count = 0 
    if(len(user_array)==1):
        return user_array
    else:
        mid = math.floor(len(user_array)/2)
        left = user_array[:mid]
        right= user_array[mid+1:]
        


        #recursive calls 
        countReverses(left)
        countReverses(right)

        left_index=0
        right_index=0
        final_index =0 

        #copy data from 
        while(left_index<len(left) and right_index<len(right)):
            if(left[left_index]<right[right_index]):
                user_array[final_index] = left[left_index]
                left_index+=1
                final_index+=1
            else:
                user_array[final_index] = right[right_index]
                right_index+=1
                final_index+=1
                reverse_count+=1
    return reverse_count






    