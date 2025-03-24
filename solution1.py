class Checkout:
    def __init__(self):
        self.prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
        self.dis = {'A': (3, 130), 'B': (2, 45)}
    
    def calculate_total(self, items):
        total = 0
        for item in set(items):
            count = items.count(item)
            if item in self.dis:
                qty, price = self.dis[item]
                total += (count // qty) * price + (count % qty) * self.prices[item]
            else:
                total += count * self.prices[item]
        return total

if __name__ == "__main__":
    checkout = Checkout()
    
    print(checkout.calculate_total(""))
    print(checkout.calculate_total("A"))
    print(checkout.calculate_total("AB"))
    print(checkout.calculate_total("CDBA"))
    print(checkout.calculate_total("AA"))
    print(checkout.calculate_total("AAA"))
    print(checkout.calculate_total("AAAA"))
    print(checkout.calculate_total("AAAAA"))
    print(checkout.calculate_total("AAAAAA"))
    print(checkout.calculate_total("AAAB"))
    print(checkout.calculate_total("AAABB"))
    print(checkout.calculate_total("AAABBD"))
    print(checkout.calculate_total("DABABA"))
