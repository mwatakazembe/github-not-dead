class Bank:
    def __init__(self):
        self.clients = {}
        self.accounts = {}
        self.next_account_id = 1

    def create_client(self, client_id, name):
        if client_id in self.clients:
            raise ValueError("client with this ID already exists")
        self.clients[client_id] = Client(client_id, name)

    def open_account(self, client_id, currency):
        if client_id not in self.clients:
            raise ValueError("client not found")
        
        client = self.clients[client_id]
        if currency in client.accounts:
            raise ValueError("account in this currency already exists")
        
        account_id = self.next_account_id
        self.next_account_id += 1
        
        account = Account(account_id, client_id, currency)
        client.accounts[currency] = account
        self.accounts[account_id] = account
        return account_id

    def close_account(self, client_id, currency):
        if client_id not in self.clients:
            raise ValueError("client not found")
        
        client = self.clients[client_id]
        if currency not in client.accounts:
            raise ValueError("account in this currency not found")
        
        account = client.accounts[currency]
        if account.balance != 0:
            raise ValueError("cannot close account with non-zero balance")
        
        del self.accounts[account.account_id]
        del client.accounts[currency]

    def deposit(self, account_id, amount):
        if account_id not in self.accounts:
            raise ValueError("account not found")
        if amount <= 0:
            raise ValueError("amount must be positive")
        
        self.accounts[account_id].balance += amount

    def withdraw(self, account_id, amount):
        if account_id not in self.accounts:
            raise ValueError("account not found")
        if amount <= 0:
            raise ValueError("amount must be positive")
        
        account = self.accounts[account_id]
        if account.balance < amount:
            raise ValueError("insufficient funds")
        
        account.balance -= amount

    def transfer(self, from_account_id, to_account_id, amount):
        if from_account_id not in self.accounts or to_account_id not in self.accounts:
            raise ValueError("one of the accounts not found")
        if amount <= 0:
            raise ValueError("amount must be positive")
        
        from_account = self.accounts[from_account_id]
        to_account = self.accounts[to_account_id]
        
        if from_account.balance < amount:
            raise ValueError("insufficient funds for transfer")
        
        from_account.balance -= amount
        to_account.balance += amount

    def get_client_accounts(self, client_id):
        if client_id not in self.clients:
            raise ValueError("client not found")
        return self.clients[client_id].accounts

class Client:
    def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name
        self.accounts = {}

class Account:
    def __init__(self, account_id, client_id, currency):
        self.account_id = account_id
        self.client_id = client_id
        self.currency = currency
        self.balance = 0.0

bank = Bank()

while True:
    print("\n--- banking system ---")
    print("1. create client")
    print("2. login")
    print("3. exit")
    
    choice = input("select action: ")
    
    try:
        if choice == '1':
            client_id = input("enter client ID: ")
            name = input("enter client name: ")
            bank.create_client(client_id, name)
            print("client created successfully")
            
        elif choice == '2':
            client_id = input("enter your client ID: ")
            if client_id not in bank.clients:
                print("client with this ID not found")
                continue
                
            current_client = bank.clients[client_id]
            
            while True:
                print("\n--- banking operations ---")
                print("1. open account")
                print("2. close account")
                print("3. deposit")
                print("4. withdraw")
                print("5. transfer")
                print("6. account statement")
                print("7. logout")
                
                operation = input("select operation: ")
                
                if operation == '1':
                    currency = input("enter account currency: ").upper()
                    account_id = bank.open_account(client_id, currency)
                    print(f"account opened, account ID: {account_id}")
                    
                elif operation == '2':
                    currency = input("enter account currency to close: ").upper()
                    bank.close_account(client_id, currency)
                    print("account closed successfully")
                    
                elif operation == '3':
                    currency = input("enter account currency: ").upper()
                    if currency not in current_client.accounts:
                        print("account in specified currency not found")
                        continue
                        
                    account_id = current_client.accounts[currency].account_id
                    amount = float(input("enter deposit amount: "))
                    bank.deposit(account_id, amount)
                    print("deposit successful")
                    
                elif operation == '4':
                    currency = input("enter account currency: ").upper()
                    if currency not in current_client.accounts:
                        print("account in specified currency not found")
                        continue
                        
                    account_id = current_client.accounts[currency].account_id
                    amount = float(input("enter withdrawal amount: "))
                    bank.withdraw(account_id, amount)
                    print("withdrawal successful")
                    
                elif operation == '5':
                    from_currency = input("enter source account currency: ").upper()
                    if from_currency not in current_client.accounts:
                        print("account in specified currency not found")
                        continue
                        
                    from_account_id = current_client.accounts[from_currency].account_id
                    to_account_id = int(input("enter recipient account ID: "))
                    amount = float(input("enter transfer amount: "))
                    
                    bank.transfer(from_account_id, to_account_id, amount)
                    print("transfer successful")
                    
                elif operation == '6':
                    filename = f"statement_{client_id}.txt"
                    with open(filename, 'w', encoding='utf-8') as f:
                        total_balance = 0.0
                        f.write(f"account statement for client {current_client.name} (ID: {client_id})\n")
                        f.write("=" * 50 + "\n")
                        
                        for currency, account in current_client.accounts.items():
                            balance = account.balance
                            total_balance += balance
                            f.write(f"account {account.account_id} ({currency}): {balance:.2f}\n")
                        
                        f.write("=" * 50 + "\n")
                        f.write(f"total balance: {total_balance:.2f}\n")
                    
                    print(f"statement saved to file: {filename}")
                    
                elif operation == '7':
                    print("logged out successfully")
                    break
                    
                else:
                    print("invalid operation, try again")
                    
        elif choice == '3':
            print("goodbye!")
            break
            
        else:
            print("invalid choice, try again")
            
    except Exception as e:
        print(f"error: {e}")