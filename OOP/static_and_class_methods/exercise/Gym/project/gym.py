from project.subscription import Subscription
from project.exercise_plan import ExercisePlan
from project.equipment import Equipment
from project.trainer import Trainer
from project.customer import Customer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        cust = [c.email for c in self.customers if c.email == customer.email]
        if len(cust) == 0:
            self.customers.append(customer)


    def add_trainer(self, trainer: Trainer):
        train = [t.name for t in self.trainers if t.name == trainer.name]
        if len(train) == 0:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        equip = [e for e in self.equipment if e.name == equipment.name]
        if len(equip) == 0:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        ex_plan = [p for p in self.plans if p.trainer_id == plan.trainer_id and p.equipment_id == plan.equipment_id]
        if len(ex_plan) == 0:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        sub = [s for s in self.subscriptions if s.date == subscription.date and s.customer_id == subscription.customer_id]
        if len(sub) == 0:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):

        subs = [sub for sub in self.subscriptions if sub.id == subscription_id][0]
        cust = [c for c in self.customers if c.id == subs.customer_id][0]
        train = [t for t in self.trainers if t.id == subs.trainer_id][0]
        pl = [p for p in self.plans if p.id == subs.exercise_id][0]
        equip = [e for e in self.equipment if e.id == pl.equipment_id][0]

        return f"{subs}\n{cust}\n{train}\n{equip}\n{pl}"



