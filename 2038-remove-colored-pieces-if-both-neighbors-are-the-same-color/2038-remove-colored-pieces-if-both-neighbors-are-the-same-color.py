class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        Alice = 0
        Bob = 0
        for i in range(2, len(colors)):
                if (colors[i-2] == colors[i-1] == colors[i]):
                    if colors[i] == 'A':
                        Alice +=1
                    else:
                        Bob +=1
        return Alice > Bob

                