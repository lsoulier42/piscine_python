class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1
        print("The account {}-{} has been created".format(self.id, self.name))

    def transfer(self, amount):
        self.value += amount
        print("The account {}-{} has been transfered {} and the contains now {}".format(self.id, self.name, amount, self.value))


class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []
        print("A bank has been created")

    def add(self, account):
        self.accounts.append(account)
        print("The account {} has been added to the bank".format(account.id))

    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest: int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occurred
        """
        if self.__verify_account_info(origin) \
            and self.__verify_account_info(dest) \
            and self.__verify_amount_value(amount):
            origin_account = self.get_account(origin)
            dest_account = self.get_account(dest)
            if origin_account and dest_account \
                and self.__verify_account_attributes(origin_account) \
                and self.__verify_account_attributes(dest_account) \
                and origin_account.value >= amount:
                dest_account.transfer(amount)
                origin_account.transfer(amount * -1.0)
                print("{} has been transferred from account {} to account {}".format(amount, origin_account.id, dest_account.id))
                return True
            elif origin_account.value < amount:
                print("The origin account doesn't have enough money to proceed")
            elif not self.__verify_account_attributes(origin_account):
                self.fix_account(origin)
                self.transfer(origin, dest, amount)
            elif not self.__verify_account_attributes(dest_account):
                self.fix_account(dest)
                self.transfer(origin, dest, amount)
            else:
                print("The account has not been found in the bank or is corrupted")
        else:
            print("The account info or the amount is invalid")
        return False

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return True if success, False if an error occurred
        """
        if self.__verify_account_info(account):
            account_instance = self.get_account(account)
            self.__fix_mandatory(account_instance)
            self.__fix_b_starting(account_instance)
            self.__fix_address(account_instance)
            self.__fix_even_attributes(account_instance)
            print("The account {} has been fixed".format(account_instance.id))
            return True
        else:
            print("The account info or the amount is invalid")
        return False

    def get_account(self, account_info):
        for a in self.accounts:
            if (type(account_info) == int and a.id == account_info) \
                    or (type(account_info) == str and a.name == account_info):
                return a

    @staticmethod
    def __verify_account_info(account_info):
        return (type(account_info) == int and account_info > 0) or (type(account_info) == str and account_info)

    @staticmethod
    def __verify_amount_value(amount):
        return (type(amount) == float or type(amount) == int) and amount >= 0

    @staticmethod
    def __verify_attributes_names(attributes):
        return (not any(a[0] == 'b' for a in attributes)) \
            and Bank.__verify_starting_zip(attributes) \
            and Bank.__verify_starting_addr(attributes)

    @staticmethod
    def __verify_existing_attributes(attributes):
        return 'name' in attributes and 'id' in attributes and 'value' in attributes

    @staticmethod
    def __verify_starting_zip(attributes):
        return any(a.startswith('zip') for a in attributes)

    @staticmethod
    def __verify_starting_addr(attributes):
        return any(a.startswith('addr') for a in attributes)

    @staticmethod
    def __build_attribute_list(account):
        return [a for a in dir(account) if not a.startswith("__") and a != 'ID_COUNT' and a != 'transfer']

    @staticmethod
    def __verify_account_attributes(account):
        if type(account) == Account:
            attributes = Bank.__build_attribute_list(account)
            return len(attributes) % 2 == 1 \
                and Bank.__verify_attributes_names(attributes) \
                and Bank.__verify_existing_attributes(attributes)
        else:
            print("Object is not an account")
        return False

    @staticmethod
    def __fix_mandatory(account_instance):
        attributes = Bank.__build_attribute_list(account_instance)
        if 'name' not in attributes:
            account_instance.name = ""
        if 'id' not in attributes:
            account_instance.id = Account.ID_COUNT
            Account.ID_COUNT += 1
        if 'value' not in attributes:
            account_instance.value = 0

    @staticmethod
    def __fix_b_starting(account_instance):
        attributes = Bank.__build_attribute_list(account_instance)
        for a in attributes:
            if a.startswith('b'):
                delattr(account_instance, a)

    @staticmethod
    def __fix_address(account_instance):
        attributes = Bank.__build_attribute_list(account_instance)
        if not any(a.startswith('zip') for a in attributes):
            account_instance.zip_code = ""
        if not any(a.startswith('addr') for a in attributes):
            account_instance.addr_home = ""

    @staticmethod
    def __fix_even_attributes(account_instance):
        attributes = Bank.__build_attribute_list(account_instance)
        if len(attributes) % 2 == 0:
            mandatory_attributes = ['name', 'id', 'value']
            for a in attributes:
                if a not in mandatory_attributes \
                and not a.startswith('zip') and not a.startswith('addr'):
                    delattr(account_instance, a)
                    break

if __name__ == "__main__":
    bank = Bank()
    account1 = Account("louise")
    account1.value = 100.0
    account1.zip = "92210"
    account1.addr = "124 bde de la republique"
    account2 = Account("coraline")
    account2.value = 100.0
    account2.zip = "67000"
    account2.addr = "7 rue adolf seyboth"
    account3 = Account("bidule")
    account3.bidule = "truc"
    bank.add(account1)
    bank.add(account2)
    bank.add(account3)
    bank.transfer(2, 1, 100.0)
    bank.transfer(2, 1, 200.0)
    bank.transfer(1, 3, 100.0)

