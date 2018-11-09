def searchForRow(arr, target):
    r = len(arr) // 2
    if not arr:
        return 0
    row = arr[r]
    if row[0] == target or row[-1] == target:
        return 1
    if row[0] < target and row[-1] > target:
        return searchInRow(row, target)
    elif row[0] > target:
        return searchForRow(arr[:r], target)
    elif row[-1] < target:
        return searchForRow(arr[(r + 1):], target)


def searchInRow(row, target):
    el = len(row) // 2

    if len(row) == 0:
        return 0
    if row[el] == target:
        return 1

    elif row[el] < target:
        return searchInRow(row[(el + 1):], target)
    elif row[el] > target:
        return searchInRow(row[:el], target)

def search(A,B):
    return searchForRow(A,B)

arr = [
  [2, 2, 5, 5, 8],
  [9, 14, 15, 15, 17],
  [18, 19, 19, 20, 20],
  [28, 32, 36, 37, 38],
  [39, 39, 39, 45, 48],
  [48, 51, 52, 55, 57],
  [60, 62, 65, 66, 68],
  [68, 71, 71, 74, 75],
  [76, 76, 76, 76, 84],
  [92, 93, 93, 95, 100]
]
print(search(arr,63))