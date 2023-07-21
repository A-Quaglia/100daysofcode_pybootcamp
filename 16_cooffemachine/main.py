from typing import Protocol
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# COIN_VALUES = {
#         "quarters": 0.25,
#         "dimes": 0.10,
#         "nickles": 0.05,
#         "pennies": 0.01
#     }

class MachineReport(Protocol):
    def report(self) -> None:
        ...

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

def report(*machines: MachineReport):
    for machine in machines:
        machine.report()

if __name__ == "__main__":
    is_on = True
    while is_on:
        options = menu.get_items()
        choice = input(f"What would you like? ({options})")

        if choice == "off":
            is_on=False
            break

        elif choice == "report":
            report(coffe_maker, money_machine)
            continue

        # check_if_has_sufficient_resources
        drink = menu.find_drink(choice)
        if not drink:
            continue
        
        has_resources = coffe_maker.is_resource_sufficient(drink)

        if has_resources:
            print(f"{drink.name} costs {drink.cost}.")
            payment = money_machine.make_payment(drink.cost)

            if payment:
                coffe_maker.make_coffee(drink)
