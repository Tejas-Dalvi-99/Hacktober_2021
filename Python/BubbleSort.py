#here I created this function for implementing Bubble sort using python language

def bubblesort(elements):

     # Looping from size of array from last index[-1] to index [0]
     for n in range(len(elements)-1, 0, -1):
         for i in range(n):
             if elements[i] > elements[i + 1]:
             # swapping data if the element is less than next element in the array
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
                print(elements)
                elements = []
             # taking size of array from user
     size = int(input("Enter How many number you want to sort:"))
     # taking array data from the user
     for i in range(size):
         value = int(input("Enter the element:"))
         elements.append(value)
     print("Array :", elements)
     bubblesort(elements)  #calling of function
     print("Sorted Array is, ")
     for i in range(size):
         print(elements[i], end =" ")
