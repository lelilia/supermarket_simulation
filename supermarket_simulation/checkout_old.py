from supermarket_simulation.utils.constants import TILE_SIZE

class Checkout:
    def __init__(self, id, cashier, x, y):
        self.id = id
        self.cashier = cashier
        self.end_of_queue = [x,y]
        self.current_customer = None

        self.time = 0

    def __repr__(self):
        return f'<Check-Out {self.current_customer}>'

    def remove_customer(self):
        self.current_customer = None

    def checkout_customer(self):
        if self.current_customer:
            if self.current_customer.items > 0:
                if self.time < self.cashier.speed_per_item * 20:
                    self.time += 1
                else:
                    self.current_customer.items -= 1
                    self.time = 0
            else:
                self.current_customer.is_checking_out = False
                self.current_customer.chosen_checkout = None
                self.current_customer.send_to_exit()
                self.current_customer = None




if __name__ == '__main__':
    from supermarket_simulation.customer_old import Customer
    from supermarket_simulation.cashier import Cashier

    chashier = Cashier(8, 8, 1)
    co = Checkout(1, cashier, 8, 9 )

    c = Customer(0)
    c.chosen_checkout = co

    print()

