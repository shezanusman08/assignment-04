def main():
    fruits ={"apple":2,"watermelon":1.5,"banana":5,"kiwi":1,"kolachi":4,"mango":3}
    total_cost = 0

    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount = int(input("How many (" +fruit_name + ") you want to buy? "))
        total_cost += (price * amount)
        
    print("Your total cost is $"+ str(total_cost) )

if __name__ == "__main__":
    main()