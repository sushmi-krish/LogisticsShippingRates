#Shipping Cost Calculator

#Input Package weight and shipping rate
weight=float(input("Enter the Package Weight in Kilograms:"))
rate =float(input("Enter the shipping rate per Kilograms:"))

#calculate the shipping cost 
shipping_cost = weight * rate

#Display the result 
print(f"shipping cost:{shipping_cost}USD")
