from SalesReceipt import SalesReceipt


print("OUTPUT 1")
sales1 = SalesReceipt("input1.txt")
sales1.calculatePrices()
sales1.Receipt()
print(f"Sales Taxes:{sales1.getTotalSalesTax()} Total Cost:{sales1.getTotalCost()}")

print("\nOUTPUT 2")
sales2 = SalesReceipt("input2.txt")
sales2.calculatePrices()
sales2.Receipt()
print(f"Sales Taxes:{sales2.getTotalSalesTax()} Total Cost:{sales2.getTotalCost()}")

print("\nOUTPUT 3")
sales2 = SalesReceipt("input3.txt")
sales2.calculatePrices()
sales2.Receipt()
print(f"Sales Taxes:{sales2.getTotalSalesTax()} Total Cost:{sales2.getTotalCost()}")
