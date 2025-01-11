from collections import defaultdict
from bisect import insort
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = defaultdict(int) # losses

        for winner, loser in matches:
            players[winner] += 0
            players[loser] += 1
        
        no_losses = []
        one_loss = []
        for player, losses in players.items():
            if losses == 0:
                insort(no_losses, player)
            elif losses == 1:
                insort(one_loss, player)
        
        return [no_losses, one_loss]
