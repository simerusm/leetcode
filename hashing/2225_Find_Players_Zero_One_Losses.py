from collections import defaultdict
from bisect import insort
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        player_losses = defaultdict(int) # losses

        for winner, loser in matches:
            player_losses[winner] += 0
            player_losses[loser] += 1
        
        no_losses = []
        one_loss = []
        for player, losses in player_losses.items():
            if losses == 0:
                insort(no_losses, player)
            elif losses == 1:
                insort(one_loss, player)
        
        return [no_losses, one_loss]
