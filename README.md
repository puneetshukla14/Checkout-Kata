# Solution 1st
I make a pyth prgmram to calculate total price of items with discounts.
lets me explain the code
I created two dictionaries  1st is pri stores item prices and 2nd one is dis stores discount offers 
I loop through each unique item in the input string using set( items  )
For each item i counted its total occurrences using items.count( item)
If the item has a discount i calculated how many times the offer can be applied and remaining items were charged at the normal price
If no discount is available i multiplied the count with the item price.
I kept adding the total for each item usnigg keep total 0
and at the lasst the function returns the total price.
