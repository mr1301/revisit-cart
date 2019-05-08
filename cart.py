import datetime
import csv
#def few inputs
tax_rate = 0.06
transaction_time = datetime.datetime.now()

#def find_product finction
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

def find_product(product_id,my_products):
    match_products = [p for p in my_products if str(p["id"]) == str(product_id)]
    match_product = match_products[0]
    return match_product

if __name__=="__main__":

    products =[
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
        {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
        {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
        {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
        {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
        {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
        {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
        {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
        {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
        {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
        {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
        {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
        {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
        {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
        {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
        {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
        {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
    ] 
# based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017
#Information input from user

    total_price = 0
    selected_ids = [] 

    while True:
        selected_id = input("Please input a product identifier")  #9 is str
        if selected_id == "DONE":
            break
        else:
            selected_ids.append(selected_id)

#Call the find_function

for selected_id in selected_ids:
    match_products = find_product(selected_id,products)
    total_price = total_price + match_product["price"]


#Information Output*************************************************************

print("                             ")
print("                             ")
print("-----------------------------")
print("THE SOUP BOWL - GEORGETOWN   ")
print("202-997-0229", "WWW.TSB.COM  ")
print("TIME", now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), "AM")
print("-----------------------------")
print("SELECTED PRODUCTS:           ")
print("-----------------------------")

#print(selected_ids)


  
  print("- " + match_product["name"] + " " + "${0:.2f}".format(match_product["price"]))

print("-----------------------------")
print("SUB-TOTAL: ${0:.2f}".format(total_price))

print("TOTAL-TAX: ${0:.2f}".format(Tax))
Tax = (total_price* tax_rate)
Total_Pay = total_price + Tax
print("TOTAL-PAY: ${0:.2f}".format(Total_Pay))
print("-----------------------------")
print("THANK YOU,", "SEE YOU AGAIN SOON")
print("-----------------------------")