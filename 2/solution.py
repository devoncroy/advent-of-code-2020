def loadData():
    data = []
    with open('2.txt', 'rb') as f:
        for c,line in enumerate(f):
            temp = line.split(': ')
            rule = temp[0]
            password = temp[1]
            temp = {
                'rule':rule,
                'password':password
            }
            data.append(temp)
    return data

def solution(data):
    count = 0

    for item in data:
        total = len(item['password'])
        temp = item['rule'].split(' ')
        character = temp[-1]
        temp = temp[0].split('-')
        minimum = int(temp[0].strip())
        maximum =int(temp[1].strip())
        total -= len(item['password'].replace(character, ''))
        if minimum <= total <= maximum:
            count += 1

    return count

if __name__ == "__main__":
    data = loadData()
    answer = solution(data)
    print(answer)