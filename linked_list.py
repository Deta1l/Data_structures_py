'''
stock_prices = [298, 305, 320, 301, 292]
#https://skillbox.ru/media/code/big-o-notation-chto-eto-takoe-i-kak-eye-poschitat/?ysclid=ldsxdn4oey460017674

# o(1)
a = int(input("vvedite den -> "))
a -= 1
print(stock_prices[a], "day nomber", a+1)

#o(n)
b = int(input("vvedite cenu -> "))
for i in range(len(stock_prices)):
    if stock_prices[i] == b:
        print("v den nomer -> ", i+1)
        break

stock_prices.insert(1, 284)
print(stock_prices)

stock_prices.pop(len(stock_prices) - 2)
print(stock_prices)

stock_prices[2] = stock_prices[2] - 10 
print(stock_prices)


stock_prices.append(34)
print(stock_prices)
stock_prices.remove(34)
print(stock_prices)

h = stock_prices.index(320)
stock_prices.insert(h+1, 34)
print(stock_prices)

stock_prices[1:3]=[434]
print(stock_prices)

stock_prices.sort()
print(stock_prices)
'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    

