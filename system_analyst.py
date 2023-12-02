
class Analyst:
    def __init__(self, vending_machine):
        self.vm = vending_machine
    
    
    def get_analytics(self):
        # Assuming the VendingMachine class has a method get_purchase_history()
        # that returns a list of purchase records.
        purchase_history = self.vm.get_purchase_history()
        total_revenue = sum(purchase['price'] * purchase['quantity'] for purchase in purchase_history)
        sold_items = [purchase['item'] for purchase in purchase_history]

        most_sold_item = max(set(sold_items), key=sold_items.count) if sold_items else None
        least_sold_item = min(set(sold_items), key=sold_items.count) if sold_items else None

        return {
            'Total Revenue': total_revenue,
            'Most Sold Item': most_sold_item,
            'Least Sold Item': least_sold_item
        }


    def update_prices(self, item, new_price):
        # Capitalize the first letter of the item name
        formatted_item = item.capitalize()
        
        # Check if the formatted item is in the vending machine's price list
        if formatted_item in self.vm.prices:
            # Update the price
            self.vm.prices[formatted_item] = new_price
            print(f"Updated price for {formatted_item} to {new_price}$")
        else:
            print("Item not found in vending machine.\n")

    def leave_note_for_restocker(self, note):
        self.vm.notes_to_restocker.append(note)
        print("Note added for the restocker.\n")

    def admin_ui(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Analytics")
            print("2. Update Price")
            print("3. Write Note")
            print("4. Exit")
            choice = input("Enter the number of the action you want to perform: ")

            if choice == '1':
                analytics = self.get_analytics()
                print(f"Total Revenue: {analytics['Total Revenue']}")
                print(f"Most Sold Item: {analytics['Most Sold Item']}")
                print(f"Least Sold Item: {analytics['Least Sold Item']}")
            elif choice == '2':
                item_name = input("Enter the item name to update its price: ")
                new_price = float(input("Enter the new price: "))
                self.update_prices(item_name, new_price)
            elif choice == '3':
                note = input("Enter the note for the restocker: ")
                self.leave_note_for_restocker(note)
            elif choice == '4':
                print("Exiting admin menu.")
                break
            else:
                print("Invalid input, please try again.")