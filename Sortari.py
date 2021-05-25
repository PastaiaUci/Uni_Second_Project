class Sortari(object):
    def __init__(self):
        pass

    def SelectionSort(self, array, key1=None, key2=None, reverse=False, cmp=None):

        if key1 == None:
            def key1(x): return x.get_student_id()
        if key2 == None:
            def key2(x): return x.get_grup()

        def default_cmp(a, b, key1, key2):
            if key1(a) < key1(b):
                return True
            elif key1(a) == key1(b):
                if key2(a) < key2(b):
                    return True
            else:
                return False

        if cmp == None:
            cmp = default_cmp

        for i in range(len(array)):
            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i+1, len(array)):
                if cmp(array[j], array[min_idx], key1, key2):
                    min_idx = j

            # Swap the found minimum element with
            # the first element
            array[i], array[min_idx] = array[min_idx], array[i]

        if reverse == True:
            array.reverse()

        return array

    def ShakerSort(self, array, key1=None, key2=None, reverse=False, cmp=None):
        n = len(array)
        swapped = True
        start = 0
        end = n - 1

        if key1 == None:
            def key1(x): return x.get_student_id()
        if key2 == None:
            def key2(x): return x.get_grup()

        def default_cmp(a, b, key1, key2):
            if key1(a) < key1(b):
                return True
            elif key1(a) == key1(b):
                if key2(a) < key2(b):
                    return True
            else:
                return False

        if cmp == None:
            cmp = default_cmp

        while (swapped == True):

            # reset the swapped flag on entering the loop,
            # because it might be true from a previous
            # iteration.
            swapped = False

            # loop from left to right same as the bubble
            # sort
            for i in range(start, end):
                if cmp(array[i+1], array[i], key1, key2):
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True

            # if nothing moved, then array is sorted.
            if (swapped == False):
                break

            # otherwise, reset the swapped flag so that it
            # can be used in the next stage
            swapped = False

            # move the end point back by one, because
            # item at the end is in its rightful spot
            end = end-1

            # from right to left, doing the same
            # comparison as in the previous stage
            for i in range(end-1, start-1, -1):
                if cmp(array[i+1], array[i], key1, key2):
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True

            # increase the starting point, because
            # the last stage would have moved the next
            # smallest number to its rightful spot.
            start = start + 1

        if reverse == True:
            array.reverse()

        return array
