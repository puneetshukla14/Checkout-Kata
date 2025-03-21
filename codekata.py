class Checkout:
    def __init__(self):
        self.prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
        self.discounts = {'A': (3, 130), 'B': (2, 45)}

    def total_price(self, items):
        from collections import Counter
        item_count = Counter(items)
        total = 0
        for item, count in item_count.items():
            if item in self.discounts:
                qty_for_discount, discount_price = self.discounts[item]
                num_discounts = count // qty_for_discount
                remaining = count % qty_for_discount
                total += num_discounts * discount_price + remaining * self.prices[item]
            else:
                total += count * self.prices[item]
        return total
if __name__ == "__main__":
    checkout = Checkout()
    test_cases = ["", "A", "AB", "CDBA", "AA", "AAA", "AAAA", "AAAAA",
                  "AAAAAA", "AAAB", "AAABB", "AAABBD", "DABABA"]
    for case in test_cases:
        print(f'INPUT: "{case}" ➔ OUTPUT: {checkout.total_price(case)}')
