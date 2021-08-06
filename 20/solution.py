'''
https://adventofcode.com/2020/day/20

Solution 1:
determines exterior tiles by looking for the ones with unique edges (makes assumption that exterior edges are always unique)
determines the four corners from exterior tiles by looking for tiles that have 2 exterior edges

Solution 2:
not implemented
'''

def loadData():
    data = {}
    with open('20.txt', 'rb') as f:
        temp = None
        tile = None
        for c,line in enumerate(f):
            if 'Tile' in line:
                if tile is not None:
                    data[tile] = parseBorders(temp)
                tile = int(line.split(' ')[-1].replace(':',''))
                temp = []
            elif line != '\n':
                temp.append(line.strip())
        # remember the last tile
        data[tile] = parseBorders(temp)

    return data

def parseBorders(data):
    left = ''.join([x[0] for x in data])
    right = ''.join([x[-1] for x in data])
    up = data[0]
    down = data[-1]
            
    return [left, right, up, down]


def solution(data):
    results = {}
    for k,v in data.items():
        for border in v:
            found = False
            if border in results:
                results[border] += 1
                found = True
            if border[::-1] in results:
                results[border[::-1]] += 1
                found = True 
            if found is  False:
                results[border] = 1
                results[border[::-1]] = 1

    # border of image, will be edges occuring exactly once
    # assuming edges are unique and do not occur more than once

    borders = []

    for k,v in results.items():
        if v == 1 and results[k[::-1]] == 1:
            borders.append(k)

    # corner tiles of image will have exactly 2 edges on the image border

    corners = []

    for k,v in data.items():
        count = 0
        for edge in v:
            if edge in borders or edge[::-1] in borders:
                count += 1
        if count == 2:
            corners.append(k)
    assert len(corners) == 4
    answer = corners[0]
    for x in corners[1:]:
        answer *= x
    return answer

if __name__ == "__main__":
    data = loadData()
    answer = solution(data)
    print(answer)