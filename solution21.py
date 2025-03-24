def checkout(items):
    pri = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    dis = {'A': (3, 130), 'B': (2, 45)}
    
    total = 0
    for item in set(items):
        count = items.count(item)
        if item in dis:
            qty, price = dis[item]
            total += (count // qty) * price + (count % qty) * pri[item]
        else:
            total += count * pri[item]
    
    return total

print(checkout(""))         
print(checkout("A"))        
print(checkout("AB"))       
print(checkout("CDBA"))     
print(checkout("AA"))       
print(checkout("AAA"))      
print(checkout("AAAA"))     
print(checkout("AAAAA"))    
print(checkout("AAAAAA"))   
print(checkout("AAAB"))     
print(checkout("AAABB"))    
print(checkout("AAABBD"))   
print(checkout("DABABA"))   
