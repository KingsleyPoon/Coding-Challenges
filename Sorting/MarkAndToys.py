'''
CODING CHALLENGE

https://www.hackerrank.com/challenges/mark-and-toys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

Mark and Jane are very happy after having their first child. 
Their son loves toys, so Mark wants to buy some. T
here are a number of different toys lying in front of him, tagged with their prices. 
Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money.
Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.

Note Each toy can be purchased only once.

Example
Prices = [1,2,3,4]
k = 7

The budget is 7 in currency. He can buy items that cost [1,2,3] for 6 or [3,4] for 7. 
The maximum items is 3

Return the maximum number of toys
'''

def maximumToys(prices, k):
    prices = sorted(prices)
    
    numberItems = 0
    
    for index, value in enumerate(prices):
        if k - value > 0:
            numberItems += 1
            k -= value
        else:
            return numberItems

prices = [1,2,3,4]
k = 7

numberItems = maximumToys(prices,k)

print(numberItems)
