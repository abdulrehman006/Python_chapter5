"""
Use a list of lists to solve the following problem. A company has four salespeople (1
to 4) who sell five different products (1 to 5). Once a day, each salesperson passes in a
slip for each differ- ent type of product sold. Each slip contains:
a) The salesperson number.
b) The product number.
c) The number of that product sold that day.
Thus, each salesperson passes in between 0 and 5 sales slips per day. Assume that the
information from all of the slips for last month is available. Write a program that will read
all this information for last month’s sales and summarise the total sales by salesperson
by product. All totals should be stored in list sales. After processing all the information
for last month, display the results in tabu- lar format, with each of the columns
representing a particular salesperson and each of the rows rep- resenting a particular
product. Cross-total each row to get the total sales of each product for last month;
cross-total each column to get the total sales by salesperson for last month. Your tabular
print out should include these cross-totals to the right of the totaled rows and at the
bottom of the totaled columns.
"""



def user_sales(persons,products,sales):
    for i in range(persons):
        for j in range(products):
            person_number = int(input("Enter salesperson number "))
            if person_number == -1:
                return sales
            else:
                product_number = int(input("Enter product number"))
                sale_amount = int(input("Enter sale amount"))
                if(person_number<=persons)and(product_number<=products):
                    sales[person_number-1][product_number-1]=sale_amount
    return sales
def total_person_sale(persons,products,sales):
    sum = 0
    total=[]
    # finding the row sum
    for i in range(persons):
        # Reset the sum
        sum = 0
        for j in range(products):
            # Add the element
            sum += sales[i][j]
        total.append(sum)

        # Print the row sum
    return total
def total_sale_products(persons,products,sales):
    sum = 0
    total=[]
    # finding the row sum
    for i in range(products):
        # Reset the sum
        sum = 0
        for j in range(persons):
            # Add the element
            sum += sales[j][i]
        total.append(sum)

        # Print the row sum
    return total




persons=4
products=5
sales_array= [[0 for x in range(products)] for y in range(persons)]
sales=user_sales(persons,products,sales_array)
print ("{:<15} {:<10} {:<10}{:<10}{:<10}{:<10}{:<10}".format("Persons","Product-1","Product-2","Product-3","Product-4","Product-5","Total"))
sale_persons=["Saleperson-1","Saleperson-2","Saleperson-3","Saleperson-4"]
counter = 0

total_products = total_sale_products(persons,products,sales)
total_sales = total_person_sale(persons,products,sales)

for v in sales:
    prod1, prod2, prod3, prod4, prod5= v
    print ("{:<15}{:<10} {:<10} {:<10}{:<10}{:<10}{:<10}".format(sale_persons[counter], prod1, prod2, prod3, prod4, prod5,total_sales[counter]))
    counter += 1
row_format ="{:<10}" * (len(total_products) + 1)
print(row_format.format("total         ", *total_products))
