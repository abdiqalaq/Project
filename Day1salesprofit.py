cost_of_item = float(input("Enter the initial cost: "))
selling_price = float(input("Enter the selling price: "))
no_of_units = float(input("Enter the number of units sold: "))

def profit_computation(buying,selling,units):
  profit = (selling_price - cost_of_item)* no_of_units
  return profit



print(profit_computation(cost_of_item, selling_price, no_of_units))