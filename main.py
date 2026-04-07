def show_inventory(inventory):
    print("\nCurrent Inventory:")
    # ¿Es esta la forma correcta de iterar sobre el diccionario?
    for fruit, stock in inventory.items(): 
        print(f"{fruit}: {stock}")
    print()
# La forma correcta de iterar un diccionario es añadiendo el .items() al final del nombre de la
# colección, si lo que queremos es imprimir las llaves y sus valores a la vez

def add_fruit(inventory):
    fruit = input("Enter the name of the new fruit: ").strip()
    if fruit in inventory.keys():
        print(f"{fruit} already exists!\n")
    else:
        stock = input(f"Enter stock for {fruit}: ")
        # Algo está mal con la sintaxis aquí...
        inventory[fruit] = int(stock)
        print(f"{fruit} added with stock {stock}.\n")
# Para asignar un valor a la llave fruit unicamente se debe usar solo un =, el == se usa para comparar dos elementos

def update_stock(inventory):
    fruit = input("Enter the name of the fruit to update: ").strip()
    # ¿Es esta la forma correcta de iterar sobre el diccionario?
    if fruit in inventory:
        amount = int(input(f"Enter amount to add to {fruit}'s stock: "))
        # ¿Es esta operación válida?
        inventory[fruit] += amount
        print(f"{fruit} stock increased by {amount}.\n")
    else:
        print(f"{fruit} is not in inventory. Use option 2 to add it.\n")
#No se debe usar el método .items() si lo que queremos es iterar entre las llaves del diccionario
#La función input() por defecto interpreta las entradas como si fueran texto, por lo que se debe convertir
# la variable amount a un numero entero por medio de int()


def menu():
    print("Options:")
    print("1 - View inventory")
    print("2 - Add new fruit")
    print("3 - Update existing fruit stock")
    print("4 - Exit")

def run_program():
    # Puede haber un error de sintaxis aquí...
    inventory = {
        "apples": 10,
        "bananas": 20,
        "oranges": 15,
    }
#Los elementos del diccionario deben estar separados por comas (,)


    # FREEZE CODE BEGIN1

    print("Welcome to the Fruit Shop!\n")

    while True:
        menu()
        choice = input("Enter option number: ")

        if choice == "1":
            show_inventory(inventory)
        elif choice == "2":
            add_fruit(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.\n")
  
if __name__ == "__main__":
    run_program()
    # FREEZE CODE END