class Account:
    def __init__(self,name,surname,password,age,user_id,phone_number,email,account_type,created_date,account_status,balance=0,address=None):
        self.name=name
        self.surname=surname
        self.age=age
        self.user_id=user_id
        self.phone_number=phone_number
        self.email=email
        self.address=address
        self.account_type=account_type
        self.balance=balance
        self.account_type=account_type
        self.created_date=created_date
        self.account_status=account_status
        self.password=password
        

        
    def check_age(self)->str:
        if self.age<17 or self.age>65:
            return "You cannot create bank account"
        
        else:
            return "You can create bank account"
    def deposit(self,amount):
        if amount>0:
         self.balance+amount
        else:
            return None
    def transfer_to(self,other_account,amount):
        if other_account is None:
         return "Invalid account"
        elif not isinstance(other_account, Account):
              return "Invalid account type"
        elif  other_account.account_status != "Active":
                return "Recipient account is not active"
        elif other_account.user_id == self.user_id:
          return "Cannot transfer to your own account"
        elif self.balance < amount:
          return "Insufficient funds"

        else:
         self.balance -= amount
         other_account.balance += amount
         return f"Transferred {amount} to {other_account.name}"


 
        
    def withdraw(self,amount):
        if(amount>self.balance):
            return "Please as much as possible increase your balance"
        else:
           self.balance-amount
    def get_balance(self):
        return self.balance
    def display_info(self):
     account_info = {
    "name": self.name,
    "surname": self.surname,
    "age": self.age,
    "user_id": self.user_id,
    "phone_number": self.phone_number,
    "email": self.email,
    "address": self.address,
    "account_type": self.account_type,
    "balance": self.balance,
    "created_date": self.created_date,
    "account_status": self.account_status,
    "password":self.password
}
     return account_info
   
        
        
    def close_account(self):
        self.account_status=False
        self.balance=0
    def apply_interest(self):
        self.balance+=self.balance*0.09 
    def change_password(self,new_pin) :
        self.password=new_pin
    def update_contact_info(self,phone,email):
        self.phone_number=phone
        self.email=email
        
        
        
