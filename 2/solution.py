def loadData():
    data = []
    with open('1.txt', 'rb') as f:
        for c,line in enumerate(f):
            temp = f.split(': ')
            rule = temp[0]
            password = temp[1]
            temp = {
                'rule':rule,
                'password':password
            }
            data.append(temp)
    return data

def solution():
    pass