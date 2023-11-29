class Employee:
    def __init__(self, first_name, last_name, job, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.__salary = salary

    def get_salary(self):
        return round(self.__salary, 2)

    def set_salary(self, salary):
        min_salary = 40_000
        top_salary = 100_000
        if min_salary > salary:
            self.__salary = min_salary
        elif salary > top_salary:
            self.__salary = top_salary
        else:
            self.__salary = salary


worker = Employee('John', 'Doe', 'administrator', 54_000.575)
# Error
# print(worker.__salary)
print(worker.get_salary())
worker.set_salary(120_000)
print(worker.get_salary())


class Employee2:
    def __init__(self, first_name, last_name, job, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.__salary = salary

    @property
    def salary(self):
        return round(self.__salary, 2)

    @salary.setter
    def salary(self, salary):
        min_salary = 40_000
        top_salary = 100_000
        if min_salary > salary:
            self.__salary = min_salary
        elif salary > top_salary:
            self.__salary = top_salary
        else:
            self.__salary = salary

    @salary.deleter
    def salary(self):
        print('Salary deleted')
        del self.__salary


worker = Employee2('John', 'Doe', 'administrator', 54_000.575)
print(worker.salary)
worker.salary = 30000
print(worker.salary)
del worker.salary
# print(worker.salary)
