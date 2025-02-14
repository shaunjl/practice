"""

Recursive divide and conquer, guaranteed O(n log(n)) time complexity, stable sort

Only stable guaranteed O(n log(n)) sort. Uses more space than quicksort, though

the basic idea of merge sort is:
 - split up a list until it's a bunch of lists of size 1
 - each list of size 1 is by definition ordered
 - merge the lists back together by taking two at a time and iterating through both, creating one ordered list out of the two ordered lists

"""

def merge_sort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        # split it in half
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        # sort each side
        merge_sort(lefthalf)
        merge_sort(righthalf)

        # merge the two sides by picking the smaller of the two values 
        # across each list from left to right
        i=0 # left list index
        j=0 # right list index
        k=0 # alist index
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i+=1
            else:
                alist[k]=righthalf[j]
                j+=1
            k+=1

        # add any left from the left half to the list
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i+=1
            k+=1

        # add any left from the right half to the list
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j+=1
            k+=1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
merge_sort(alist)
print(alist)
