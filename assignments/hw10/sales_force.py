"""
Name: Patrick Puckhaber
sales_force.py

Problem: Builds data on the sales staff

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from sales_person import SalesPerson


class SalesForce:
    """Creates a list of sales people and their stats"""

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):

        # id, name, sale amt, sale amt...
        for line in open(file_name, "r"):
            eid, name, sales = line.split(", ")
            sales_person = SalesPerson(eid, name)
            sales = sales.replace("\n", "")
            sales = sales.split(" ")
            for sale in sales:
                sales_person.enter_sale(sale)
            self.sales_people.append(sales_person)

    def quota_report(self, quota):
        # returns list of lists [int, string, float, bool]
        report = []

        for sales_person in self.sales_people:
            employee = [sales_person.get_id(), sales_person.get_name(),
                        sales_person.total_sales(), sales_person.met_quota(quota)]
            report.append(employee)
        return report

    def top_seller(self):
        place_holder = SalesPerson(000, "none")
        place_holder.enter_sale(1)
        top_sell = [place_holder]
        for sales in self.sales_people:
            if sales.compare_to(top_sell[0]) == 1:
                top_sell = [sales]
            elif sales.compare_to(top_sell[0]) == 0:
                top_sell.append(sales)

        return top_sell

    def individual_sales(self, employee_id):
        sales_people = self.sales_people
        staff = {}
        for people in sales_people:
            staff[people.get_id()] = people
        return staff.get(employee_id, None)
