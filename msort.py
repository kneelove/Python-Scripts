import time #import time package for timer function
def mergeSort(input_list):

   

   if len(input_list)>1:               #checks whether the list doesnt have a single value
       middle = len(input_list)//2
       left = input_list[:middle]      #divides the list into two halves
       right = input_list[middle:]

                                       #recursion for both the parts
       mergeSort(left)
       mergeSort(right)

       i=0                             #counters get initialised 
       j=0
       k=0

       while i < len(left) and j < len(right): #length check condition
           if left[i] < right[j]:              #checks for length of halves
               input_list[k]=left[i]            
               i=i+1
           else:
               input_list[k]=right[j]
               j=j+1
           k=k+1

       while i < len(left):      #left half operation
           input_list[k]=left[i]
           i=i+1
           k=k+1

       while j < len(right):     #right half operation
           input_list[k]=right[j]
           j=j+1
           k=k+1
print('################MERGE_SORT##################\n')
print('Please enter numbers to be sorted separated by space and press enter \n')
input_list = [int(x) for x in input().split()] #user input
start = time.time()                          #timer starts
mergeSort(input_list)
print(input_list)
end = time.time()                            #timer stops
print(str(end - start)+'  seconds')          
input("Press ENTER to exit")
