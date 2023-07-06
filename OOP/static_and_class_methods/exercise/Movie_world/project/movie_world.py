from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = [cust for cust in self.customers if cust.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return f"DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = [cust for cust in self.customers if cust.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        else:
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        res = ''
        cust_res = '\n'.join([f"{cust}" for cust in self.customers])
        res += cust_res + '\n'
        dvds_res = '\n'.join([f"{dvd}" for dvd in self.dvds])
        res += dvds_res
        return res


