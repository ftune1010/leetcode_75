class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            _ ,s = self.stack.pop()
            span += s
        self.stack.append((price, span))
        return span


if __name__ == "__main__":
    obj = StockSpanner()
    prices = [100,80,60,70,60,75,85]
    for price in prices:
        print(obj.next(price))