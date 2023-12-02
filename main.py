from client_restocker import VendingMachine, Client, Restocker
from system_analyst import Analyst


if __name__ == "__main__":
    vending_machine = VendingMachine()

    while True:
        user_input = input("Enter 'client', 'restocker', or 'admin' to proceed or 'exit' to leave: ")
        print("\n")

        if user_input.lower() == 'client':
            client = Client(vending_machine)  # Create an instance of the Client class
            client.client_ui()  # Call the client_ui method on the client instance
            print("\n")


        elif user_input.lower() == 'restocker':
            restocker = Restocker(vending_machine) 
            restocker.restocker_ui() # Call the restocker_ui methid on the restocker instance
            print("\n")

            pass

        elif user_input.lower() == 'admin':
            admin = Analyst(vending_machine)
            admin.admin_ui() # Call the admin_ui method on the admin instance 
            print("\n")
            pass

        elif user_input.lower() == 'exit':
            break

        else:
            print("Invalid input, please try again.")
            print("\n")


