'''
https://adventofcode.com/2020/day/1

Solution 1:
iterates through the list of numbers, checking if the comimentry number summing to 2020 is also present
takes advantage of dictionary datastructure to avoid iterating through all the numbers more than once

Solution 2
iterates through a sorted list of numbers in descending order
for each number x iterates through all the numbers less than x checking to see if the remainder of 2020 - x - y exists in the list
requires only n(n+1) / 2 iterations at worst case
'''

def loadData():
    with open('1.txt', 'rb') as f:
        data = {int(x.strip()):None for c,x in enumerate(f)}
    return data

def solution(data):
    for k,v in data.items():
        search = 2020 - k
        if search in data:
            return k * search
    return None

def solution2(data):
    numbers = list(data.keys())
    numbers.sort(reverse=True)
    total = len(data)
    for i,x in enumerate(numbers):
        search = 2020 - x
        if i < total:
            for y in numbers[i+1:]:
                search2 = search - y
                if search2 in data:
                    return x * y * search2
    return None

if __name__ == "__main__":
    data = loadData()
    answer = solution(data)
    print(answer)
    answer = solution2(data)
    print(answer)   