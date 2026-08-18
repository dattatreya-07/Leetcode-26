from collections import deque

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        deck.sort(reverse=True)      
        queue = deque()
        for card in deck:
            if queue:
                queue.appendleft(queue.pop())
            queue.appendleft(card)
        return list(queue)
