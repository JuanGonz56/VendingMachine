
class VendingMachine:
    def __init__(self):
        self.items = {
            'Water': {'A1': 8, 'A2': 8, 'A3': 8, 'A4': 8},
            'Energy-Drink': {'B1': 8, 'B2': 8, 'B3': 8, 'B4': 8},
            'Energy-Bar': {'C1': 8, 'C2': 8, 'C3': 8, 'C4': 8},
            'Chips': {'D1': 8, 'D2': 8, 'D3': 8, 'D4': 8},
            'Skittles': {'E1': 8, 'E2': 8, 'E3': 8, 'E4': 8},
            'Gummies': {'F1': 8, 'F2': 8, 'F3': 8, 'F4': 8}
        }
        self.prices ={'Water': 1.50, 'Energy Drink': 3.50, 'Energy Bar': 2.50, 'Chips': 2.50, 'Skittles': 2.50, 'Gummies': 1.50
        }
        self.purchase_history = []
        self.notes_to_restocker = []


    def display_items(self):
        for item, slots in self.items.items():
            print(f"{item}: {[''.join(slot)+'('+str(count)+')' for slot, count in slots.items()]}")


    def get_item_price(self, item_name):
        # Here we'll access the `prices` dictionary to get the price of the item
        return self.prices.get(item_name, "Item not found")


    
class Client:
    def __init__(self, vending_machine):
        self.vm = vending_machine

    def select_item(self, item_name, slot):
        # Assuming item names are formatted like 'Energy-Drink' and slots like 'A1'
        formatted_item_name = item_name.replace(' ', '-').capitalize()
        formatted_slot = slot.upper()

        if formatted_item_name in self.vm.items and formatted_slot in self.vm.items[formatted_item_name]:
            return True
        return False

    def make_payment(self, item_name, slot_key, price, payment_type):
        if payment_type.lower() == 'cash':
            cash_paid = float(input(f"Insert cash amount for {item_name} which costs ${price}: "))
            if cash_paid < price:
                print("Not enough cash inserted. Transaction cancelled.")
                return None  # Return None to indicate cancellation
            else:
                change = cash_paid - price
                print(f"Payment accepted. Dispensing {item_name}. Your change is ${change:.2f}")
                return change

        elif payment_type.lower() == 'card':
            print(f"Card payment processed for {item_name} which costs ${price}.")
            return 0  # No change for card payments

        else:
            print("Invalid payment type. Transaction cancelled.")
            return None

    def client_ui(self):
        self.vm.display_items()

        item_name = input("Enter the item you want to purchase: ")
        slot_number = input("Enter the slot number (e.g., 'A1' for Slot 1): ")

        if self.select_item(item_name, slot_number):
            item_name_formatted = item_name.capitalize()
            price = self.vm.get_item_price(item_name_formatted)
            if price == "Item not found":
                print("Sorry, the item you requested is not available.")
                return  # Return to main menu

            payment_type = input("Enter payment type (cash/card): ")
            change = self.make_payment(item_name_formatted, slot_number, price, payment_type)

            if change is not None:
                # Update the stock if payment is successful
                slot_key = slot_number  # Directly use the slot_number as the key
                self.vm.items[item_name_formatted][slot_key] -= 1
            else:
                print("Returning to the main menu.")



class Restocker:

    def __init__(self, vending_machine):
        self.vm = vending_machine

    def check_stock(self):
        low_stock_items = []
        for item, slots in self.vm.items.items():
            for slot, quantity in slots.items():
                if quantity <= 5:  # Assuming low stock is defined as 5 or fewer items
                    low_stock_items.append((item, slot, quantity))
        return low_stock_items

    def restock(self, item_name, slot, quantity):
        # Normalize the inputs to match the case used in the items dictionary
        normalized_item_name = item_name.replace(' ', '-').capitalize()
        normalized_slot = slot.upper()

        if normalized_item_name in self.vm.items and normalized_slot in self.vm.items[normalized_item_name]:
            self.vm.items[normalized_item_name][normalized_slot] += quantity
            print(f"Restocked {quantity} units of {normalized_item_name} in {normalized_slot}.")
        else:
            print("Invalid item or slot.")

    def update_item(self, item_name, new_price=None, new_slot=None):
        if item_name in self.vm.items:
            if new_price is not None:
                for slot in self.vm.items[item_name]:
                    self.vm.items[item_name][slot]['price'] = new_price
            if new_slot is not None:
                self.vm.items[item_name] = self.vm.items[item_name].move_to_slot(new_slot)
            print(f"Updated details for {item_name}.")
        else:
            print("Item not found.")

    def restocker_ui(self):
        while True:
            print("\nRestocker Menu:")
            print("1. Check stock levels")
            print("2. Restock item")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                low_stock_items = self.check_stock()
                print("Low stock items:")
                for item, slot, quantity in low_stock_items:
                    print(f"{item} in {slot} - {quantity} left")
            elif choice == '2':
                item_name = input("Enter the item name to restock: ")
                slot = input("Enter the slot: ")
                quantity = int(input("Enter the quantity to add: "))
                self.restock(item_name, slot, quantity)
            elif choice == '3':
                break
            else:
                print("Invalid choice.")


