import math
import random

test_arr = []

#fills arrayb with random numbers 0-99
for i in range(0,100):
    test_arr.append(int(random.random()*100))


def countReverses(user_array):
    
    if(len(user_array)>1):
        
    
        mid = math.floor(len(user_array)/2)
        left = user_array[:mid]
        right = user_array[mid+1:]
        


        #recursive calls 
        left_count = countReverses(left)
        right_count= countReverses(right)
        
        if left_count != None and right_count != None:
            reverse_count = left_count + right_count
        elif (left_count == None and right_count != None):
            reverse_count = right_count
        elif right_count == None and left_count != None:
            reverse_count = left_count
        else:
            reverse_count = 0

        left_index=0
        right_index=0
        final_index = 0
        
        
        
        #copy data from 
        while(left_index<len(left) and right_index<len(right)):
            if(left[left_index]<=right[right_index]):
                user_array[final_index] = left[left_index]
                left_index+=1
                final_index += 1
                
            else:
                user_array[final_index] = right[right_index]
                right_index+=1                
                reverse_count+= (len(left)-left_index)
                final_index += 1
        while left_index <len(left):
            user_array[final_index] = left[left_index]
            left_index+=1                
            final_index+= 1
        while right_index <len(right):
            user_array[final_index] = right[right_index]
            right_index+=1                
            final_index+= 1
        return reverse_count


print(countReverses(test_arr))

    




    