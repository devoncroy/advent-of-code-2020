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

if __name__ == "__main__":
    data = loadData()
    answer = solution(data)
    print(answer)