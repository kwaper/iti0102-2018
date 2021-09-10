"""Store imitation."""


class ProductCannotBeSold(Exception):
    """You can not buy it yet."""

    def __init__(self, text):
        """Exception init."""
        a = text
        print(a)


class Product:
    """Represents product model."""

    def __init__(self, name: str, price: int) -> None:
        """
        Class constructor. Each product has name and price.

        :param name: product name
        :param price: product price
        """
        self.items = []
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """
        Product object representation in string format.

        :return: string
        """
        return f"Product: {self.name}, price: {self.price}"

    def __repr__(self) -> str:
        """
        Product object representation in object format.

        :return: string
        """
        return f"{self.name}"


class Customer:
    """Represents customer model."""

    def __init__(self, name: str, age: int, money: int) -> None:
        """
        Class constructor. Each customer has name, age and money when being created.

        Customer also has storage for bought items.
        :param name: customer's name
        :param age: customer's age
        :param money: customer's money
        """
        self.representation = ""
        self.items = {}
        self.name = name
        self.age = age
        self.money = money

    def add_item(self, product: Product, amount: int) -> None:
        """
        Add bought items to customer's items.

        :param product: product
        :param amount: amount
        """
        if product.name not in self.items:
            self.items[product.name] = amount
        else:
            self.items[product.name] += amount
        pass

    def pay(self, money_to_pay: int) -> None:
        """
        Check if customer has enough money to pay for the product.

        Returns nothing, but raises exception if customer has not enough money to pay.
        In other case reduces amount of customer's money.
        :param money_to_pay: money amount needed to be paid
        """
        if self.money >= money_to_pay:
            pass
        else:
            raise ProductCannotBeSold("You do not have enough money to pay for chosen product!")

    def __str__(self) -> str:
        """
        Customer object representation in string format.

        :return: string
        """
        for i in self.items:
            if len(self.representation) == 0:
                if self.items[i] == 1:
                    self.representation += f"{str(i)}"
                else:
                    self.representation += f"{str(i)}({self.items[i]})"
            if i not in self.representation:
                if self.items[i] == 1:
                    self.representation += f", {str(i)}"
                else:
                    self.representation += f", {str(i)}({self.items[i]})"
        return f"{str(self.name)}'s items: {str(self.representation)}; money: {self.money}."
        pass


class Store:
    """Represents store model."""

    def __init__(self) -> None:
        """Class constructor."""
        self.money = 0
        self.products = {}
        pass

    def buy(self, product: Product, amount: int, customer: Customer) -> str:
        """
        Represent how customer buys product.

        :param product: product the customer wants
        :param amount: pieces of product
        :param customer: customer who wants to buy
        :return: message
        """
        customer.pay(amount * product.price)
        if self.allowed_to_buy(product, customer) is True and self.check_product_availability(product, amount) is True:
            customer.add_item(product, amount)
            self.money += (product.price * amount)
            customer.money -= product.price * amount
            self.products[product] -= amount
            if self.products[product] == 0:
                self.products.pop(product)
            return f"Thank you for the purchase!"

    def allowed_to_buy(self, product: Product, customer: Customer):
        """
        Check if customer is allowed to buy some particular products.

        Permission depends on customer's age

        Customers under 18 are not allowed to buy beer and tobacco.
        Must raise exception if customer has no permission to buy chosen product.
        :param product: product to buy
        :param customer: customer who makes the purchase
        """
        if (product.name == "beer") or (product.name == "tobacco"):
            if product.name == "beer":
                if customer.age < 18:
                    raise ProductCannotBeSold("You are too young to buy beer!")
                else:
                    return True
            if product.name == "tobacco":
                if customer.age < 18:
                    raise ProductCannotBeSold("You are too young to buy tobacco!")
                else:
                    return True
        else:
            return True

    def check_product_availability(self, product: Product, amount: int):
        """
        Check if chosen amount of product is present in stock.

        Must raise exception if no product found or not enough in stock.
        :param product: product to be bought
        :param amount: amount of product
        """
        if product in self.products:
            if self.products[product] == 0:
                raise ProductCannotBeSold("Item not found!")
            else:
                if amount <= self.products[product]:
                    return True
                else:
                    raise ProductCannotBeSold("Item is not available in chosen amount!")
        else:
            raise ProductCannotBeSold("Item not found!")
        pass

    def add_product(self, product: Product) -> None:
        """
        Adding product to store.

        :param product:  product name
        """
        if product not in self.products:
            self.products[product] = 1
            product.items.append(product)
        elif product in self.products:
            self.products[product] += 1
            product.items.append(product)
        pass

    def __str__(self) -> str:
        """
        Store object representation in string format.

        :return: string
        """
        items = []
        for i in store.products.keys():
            items.append(i)
        return f"Store items: {items}; store money: {self.money}"
        pass


if __name__ == "__main__":
    john = Customer("John", 20, 300)
    bobby = Customer("Bobby", 17, 150)
    sandy = Customer("Sandy", 12, 100)

    store = Store()

    beer = Product("beer", 50)
    water = Product("water", 30)
    choco = Product("chocolate", 45)
    pretzel = Product("pretzel", 35)

    store.add_product(beer)
    store.add_product(water)
    for _ in range(3):
        store.add_product(choco)
        store.add_product(pretzel)
    print(store.products)

    print(store.buy(beer, 1, john))  # -> Thank you for the purchase!
    print(beer not in store.products)  # -> True
    print(john)  # -> John's items: beer; money: 250.
    print(type(john))

    store.buy(choco, 1, bobby)
    store.buy(water, 1, bobby)
    print(bobby)  # -> Bobby's items: chocolate(2), water; money: 30.
    store.buy(choco, 2, john)
    print(john)
    print(store.products)
    tobacco = Product("tobacco", 55)
    store.add_product(tobacco)
    print(store.buy(tobacco, 1, bobby))  # -> You are too young to buy tobacco!
