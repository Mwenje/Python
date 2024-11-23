def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * 0.2
        final_price = price - discount
        return final_price
    else:
        return price


original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percent)


if final_price == original_price:
    print(f"No discount applied. The original price is: KES.{round(final_price,2)}")
else:
    print(f"The final price after applying the discount is: KES.{final_price:.2f}")
