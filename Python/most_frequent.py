def most_frequent(arr):
    elements = {}
    for el in arr:
        if el in elements:
            elements[el] += 1
        else:
            elements[el] = 1
    max = 0
    max_el = ''
    for key in elements:
        if elements[key] > max:
            max = elements[key]
            max_el = key
        elif elements[key] == max:
            max_el += key
    return max_el

print(most_frequent('paulina'))