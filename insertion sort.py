def insertionSort(ainstance):
   for index in range(1,len(ainstance)):

     currentvalue = ainstance[index]
     position = index

     while position>0 and ainstance[position-1]>currentvalue:
         ainstance[position]=ainstance[position-1]
         position = position-1

     ainstance[position]=currentvalue

ainstance = [54,26,93,17,77,31,44,55,20]
insertionSort(ainstance)
print(ainstance)