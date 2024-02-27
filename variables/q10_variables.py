#Q10. Assume that obj already has a value of 42 when the code below starts running. Which of the subsequent statements 
# reassign the variable? Which statements mutate the value of the object that obj references? 
# Which statements do neither? If necessary, you can read the documentation.



obj = 42 

obj = 'ABcd' #re-assigns variable 
obj.upper() #Neither
obj = obj.lower() #re-assigns variable 
print(len(obj)) #Neither
obj = list(obj) #re-assigns variable 
obj.pop() #Mutates value of object
obj[2] = 'X' #Mutates value of object
obj.sort() #Mutates value of object (sort is a mutable method)
set(obj) #Neither
obj = tuple(obj) #re-assigns value of object
print(obj)
print(type(obj))
#obj = ('X' 'b' 'c' )