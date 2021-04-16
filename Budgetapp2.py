database = { }

class Budget():
    def __init__(seld, category, amount):
        self.category = category
        self.amount = amount

    def deposit(amount, bal):
        bal += amount
        return bal

    def withdrawl(user, amount, bal):
        bal -= amount
        return bal

    def balance(db):
        for categ, bal in db.items():
            print(categ, bal)

    def transfer(db, optional, amount, option2):
        value1 = db[option1]
        value2 = db[option2]

        db[option1] = int(value1) - amount
        db[otion2] = int(value2) + amount 
        return db


    def init():
        try:

            user = int(input('\n===****what would you like to do?**** ===\nPress (1) To create a new budget\nPress(2) To deposit into the account\n'))
        except:
            print('Invalid option')
            menu()

        if (user == 1):
            new budget()
        elif(user == 2):
            credit()
    def new_budget():
        print('\n==== ***Creating a New Budget****\n')
        
        budget_title = input('Enter budget name \n')
        try:
            amount = int(input('Enter your budget amoumt \n$'))
        except:
            print('\nInvalid input')
            new_budget()
        budget = Budget(budget_title, amount)
        database[budget_title] = amount
        print('')
        print(f'Budget (budget_title) was setup with $(amount)')
        menu()

    def debit():
        print('=== ****Withdraw from a created budget**** ===\n')
        print('**** Available Budgets ****')

        for key, value in database.items():
            print(f'- {key}')
        
        pick = int(input('\nPress (1) To continue with your debit transaction\nPress (2) To stop debit transaction\n'))
        if (pick == 1):
            user = input('\n**** Select one of budget(s) aforementioned****\n')
            if user in database:
                print('Note: You can not withdraw all your budget, at least $1 must remain.')
                amt = int(input('Enter amount \n$'))
                