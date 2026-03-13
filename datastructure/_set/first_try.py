# unordered collection of unique items
basket = {"apple","orange","apple","pear","orange",'banana'}

print(basket)

print('orange' in basket)


print('papaya' in basket)

basket.update({4,'not'})
print(basket)
basket.add('pear')
print(basket)
basket.remove(4)
print(basket)
print(basket.pop())
print(basket)

a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)

print(a-b) #letters in A but not in b
# always use &/| not and /or
print(a & b) #letters common to both

print(a | b)  #all letters 

print(a^b) #letters not shared by a,b

#set comprehension
c = {x for x in basket if len(x)>4}
print(c)