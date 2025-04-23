def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is less than 20%, return the original price.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to apply.
    
    Returns:
    float: The final price after applying the discount or the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    if original_price < 0 or discount_percentage < 0:
        raise ValueError("Both price and discount percentage must be non-negative.")
    
    final_price = calculate_discount(original_price, discount_percentage)
    
    if final_price != original_price:
        print(f"The final price after applying a {discount_percentage}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")

except ValueError as e:
    print(e)