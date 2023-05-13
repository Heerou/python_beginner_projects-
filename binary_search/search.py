# A function that takes a list and targets a parameter
# Multiple variables : middle, start, end
# Recursion or a while loop
# Increase steps each time the split is done
# Conditions to track the position
# Spanish explanation https://www.youtube.com/watch?v=wAmu0Ly5ook

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while start <= end:
        print("Steps", steps, ":", str(list[start:end + 1]))
        steps = steps + 1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1


the_list = [15,16,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
target = 2

binary_search(the_list, target)
