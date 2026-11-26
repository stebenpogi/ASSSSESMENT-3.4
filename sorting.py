
def build_unsorted(name):

    arr = []
    for ch in name.upper():
        if ch.isalpha() and ch not in arr:
            arr.append(ch)
    return arr


def insertion_sort(arr):
    result = arr.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
        print(f"  Pass {i} (insert {key}):", result)
    return result