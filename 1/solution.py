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