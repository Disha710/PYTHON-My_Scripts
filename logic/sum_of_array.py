def sumofnum(num,target):
  seen = {}
  for i, val in enumerate(num):
    print(i,val)
    diff = target - val
    if diff in seen:
      return [seen[diff],i]
      
    seen[val] = i
    
result = sumofnum([1,2,7,11,15,-2],9)

print(result)


def sum_of_all_pairs(num, target):
    seen = {}
    all_results = []  
    
    for i, val in enumerate(num):
        diff = target - val
        
        if diff in seen:
            all_results.append([seen[diff], i])
            
        seen[val] = i
        
    return all_results 

result = sum_of_all_pairs([1, 2, 7, 11, 15, -2], 9)

print(f"All matching pairs: {result}")


#to check number appear more that one
def num_count(num):
  count = {}
  for i in num:
    count[i] = count.get(i,0) +1
    
  return count
nums = [7, 2, 3, 7, 2, 1]
result = num_count(nums)
print(result)


#print only the dublicate num
def dublicate(num):
  count = {}
  for i in num:
    count[i] = count.get(i,0)+1
  for key, val in count.items():
    if val > 1:
      print(f"{key} appears {val} times")
    
result = dublicate([44,44,55,55,66])
print(result)

l1 = [4,5,6,8,10,33]
even_sum = sum(i for i in l1 if i%2 ==0)
odd_sum = sum(i for i in l1 if i%2 !=0)



print(even_sum,odd_sum)

import numpy as np
l1 = [11,22,333,444,55,66,22,12,23,34,56]
arr = np.array(l1)
e_sum = arr[arr%2 == 0].sum
o_sum = arr[arr%2 != 0].sum
print(e_sum,o_sum)