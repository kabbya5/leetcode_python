from collections import  Counter
def countDistinctColors(limit, queries):
    ans = []
    ballToColor = {}
    colorCount = Counter()

    for ball, color in queries:
      if ball in ballToColor:
        prevColor = ballToColor[ball]
        colorCount[prevColor] -= 1
        if colorCount[prevColor] == 0:
          del colorCount[prevColor]
      ballToColor[ball] = color
      colorCount[color] += 1
      ans.append(len(colorCount))

    return ans

limit = 4
queries = [[1,4],[2,5],[1,3],[3,4]]
print(countDistinctColors(limit, queries));