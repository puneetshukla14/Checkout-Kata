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
