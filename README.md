Solution 1

I created a Python program to calculate the total price of items, considering applicable discounts.  

The program uses two dictionaries:  
1. `pri` stores item prices.  
2. `dis` stores discount offers.  

The logic works as follows:  
- I iterate through each unique item in the input string using `set(items)`.  
- For each item, I count its total occurrences using `items.count(item)`.  
- If a discount is available, I calculate how many times the offer can be applied, and the remaining items are charged at the regular price.  
- If no discount applies, I multiply the count by the item's price.  
- I maintain a `total` variable initialized to 0 and keep adding the calculated price for each item.  

Finally, the function returns the total price.



Solution 2

I created a Python program using Object-Oriented Programming (OOPs) to calculate the total price of items, including applicable discounts.

The program has a Checkout class that contains:

prices dictionary to store the price of each item.
dis dictionary to store discount offers (like 3 A's for 130, 2 B's for 45).
In the calculate_total() method:

I looped through each unique item using set(items).
For every item, I counted its total occurrences.
If a discount is available, I applied it and calculated the remaining at normal price.
If no discount, I simply multiplied the count with the item price.
The total price is calculated and returned.
