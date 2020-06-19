#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
O(1) A constant runtime. If the input size ever got bigger than n, then the code won't run.
So as long as the input is smaller than n, it wont affect the runtime or space used

b)
O(n) Linear. If the input increases, looping within the range will also increase.

c) O(1) Consant runtime. for every input > 0, we will perform 1 function execution

## Exercise II

#Broke if thrown off floor >= f
#not Broken if thrown off < f

1 - I would determine the total floor count
2 - Go to the middle of the floor
Case 1: If 1 egg breaks from the middle, then floor f is lower than the middle.
Case 2: If 1 egg does not break then f is higher than the middle.

if case 1, I will find the middle of the lower half of the first half and throw an egg. If it breaks,
that means the f floor is in the lower part of the lower floor. I would keep repeating these steps till I find f.

If case 2, I will find the middle in the upper half of the building. From there, throw the egg and if it does not break then,
f would be higher or will be on it. I will then check the floor directly above to see if the egg breaks. If it does then f is 1 floor below.

runtime is O(log n)
