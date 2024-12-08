from turtle import st


def intToStr(i):
    if i < 0:
        return "0"
    digits = "0123456789"
    result = ""
    while i > 0:
        result = digits[i % 10] + result

        i = i // 10

    return result


print(intToStr(1213))

# binary search


def binary_search(arr, el):
    start_index = 0
    end_index = len(arr) - 1
    while start_index <= end_index:
        el_index = (start_index + end_index) // 2
        el_value = arr[el_index]
        if el_value == el:
            return el_index
        elif el_value < el:
            start_index = start_index + el_index
        elif el_value > el:
            end_index = end_index - el_index


arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 7))
