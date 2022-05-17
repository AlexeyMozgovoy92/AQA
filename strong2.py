class Department:
    class BudgetError(ValueError):
        pass

    def __init__(
            self, name: str, employees: typing.Dict[str, float], budget: int
            ):
        self.name = name
        self.employees = employees
        self.budget = budget

    def get_budget_plan(self) -> float:
        budget_plan = self.budget
        salary = sum(self.employees.values())

        if budget_plan < salary:
            raise self.BudgetError

        return budget_plan - salary

    @property
    def average_salary(self) -> float:
        return round(sum(self.employees.values()) / len(self.employees), 2)

    @classmethod
    def merge_departments(cls, *departments):
        new_list_of_deps = sorted(
            departments, key=lambda dep: (-dep.average_salary, dep.name)
        )

        new_name = []
        new_employees = {}
        new_budget = 0

        for department in new_list_of_deps:
            new_name.append(department.name)
            new_employees.update(department.employees)
            new_budget += department.budget
        new_name = ' - '.join(new_name)

        new_department = Department(new_name, new_employees, new_budget)
        new_department.get_budget_plan()

        return new_department

    def __add__(self, other):
        return self.merge_departments(self, other)

    def __str__(self):
        return "{} ({} - {}, {})".format(
            self.name, len(self.employees), self.average_salary, self.budget
        )

    def __or__(self, other):
        if self.get_budget_plan() < other.get_budget_plan():
            return other

        return self
