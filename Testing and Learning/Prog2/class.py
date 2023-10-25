from datetime import datetime
from abc import ABC, abstractmethod

class Employee:
    num_of_emps = 0
    raise_amount = 1.04 #methodon belül not defined hely megadása nélkül
    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + '.' + last + '@gmail.com'
        
        Employee.num_of_emps += 1 # konstans osztályérték, egységes (nem mint a self elméletben)

    # def fullname(self):
    #     return ('{} {}'.format(self.first, self.last))

    @property #method, de az accessben attribute, szóval továbbra is emp_1.email pl.
    def email(self):
        return f'{self.first}.{self.last}@email.com'
    
    @property
    def fullname(self): # kódban még lehet vhol meghívásként maradt, de nem helyes
        return ('{} {}'.format(self.first, self.last))
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"
    
    def __str__(self) -> str:
        return f"{self.fullname} - {self.email}"
    
    def __add__(self, other) -> str:
        return self.pay + other.pay
    
    @fullname.setter # be fogja állítani az alul megadott valuekat megfelelően (pl. first='Test', last='User')
    def fullname(self, name): 
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter #ez nem biztos hogy hasznos
    def fullname(self): 
        self.first = None
        self.last = None
    
    @classmethod
    def set_raise_amt(cls, amount): #nem self! osztályon hajt végre, míg egy normal method egy kért esetre fog
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-') #Test-User-60000
        return cls(first, last, pay) # létrehozás és visszatérés
    
    @staticmethod
    def is_workday(day): # nem használ instancet se classt, csak logikai kötődése van az osztályhoz
        if day.weekday() ==5 or day.weekday() == 6:
            return False
        return True
    
    @abstractmethod #itt jelen esetben method írása nem kell, de aki örökli, annak változtatásokat kell hoznia
    def must_implement(self):
        """Print if the method was implemented correctly in children."""
        pass
    
class Developer(Employee): # inheritance
    raise_amt = 1.10 # felülírja deveknek az employeeból örökölt valuet
    def __init__(self, first, last, pay, prog_lang) -> None:
        super().__init__(first, last, pay) #Employee.__init__(self, first, last, pay) is jó
        self.prog_lang = prog_lang
    def must_implement(self):
        return "Function implemented"

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None) -> None:
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
    
    def must_implement(self):
        return "Function implemented"

uinput = input("Futtatni szeretnéd a programot? Y/N: ")
#KOMMENTELGETÉS TESZTELÉSHEZ!
if uinput == 'Y':
    emp_1 = Employee('Test', 'User', 60000)

    # print('{} {}'.format(emp_1.first, emp_1.last)) #-> hosszú
    # print(emp_1.fullname) #-> memóriacím method

    # print(emp_1.fullname()) #-> meghívás, automatikus self behelyettesítés

    # Employee.fullname(emp_1) #-> ugyanaz, de arggal

    # print(emp_1.raise_amount) # konkrétan nincs meg neki, hanem örökli Employeetól (emp_1? ő nem tudja, kérdezd Employeet)
    # print(Employee.__dict__) # miket tartalmaz

    # Employee.raise_amount = 1.06 # átállítja mindenkinek
    # Employee.set_raise_amt(1.05) # mindegyiket updateli
    # emp_1.raise_amount = 1.04 # csak egy employeenál
    # emp_1.set_raise_amt(1.07) # mindegyiket updateli, mert classmethod egységes

    # print(Employee.num_of_emps) # 1

    # emp_str_2 = 'Steve-Smith-30000'
    # new_emp_2=Employee.from_string(emp_str_2)

    # my_date2= datetime.date(2016, 7, 10)
    # my_date1= datetime.date(2016, 7, 11) 

    # print(Employee.is_workday(my_date1)) #false
    # print(Employee.is_workday(my_date2)) #True

    dev_1 = Developer("Mate", "Runner", 50000, "C++")
    # print(dev_1.email)
    # print(help(Developer))

    # print(dev_1.pay) #50000
    # dev_1.apply_raise()
    # print(dev_1.pay) #52000 a dev raise_amt miatt

    mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
    # mgr_1.add_emp(emp_1)
    # mgr_1.print_emps()
    # mgr_1.remove_emp(emp_1)
    # mgr_1.print_emps()

    # print(isinstance(mgr_1, Manager)) # True, obj örököl a Classból
    # print(isinstance(mgr_1, Employee)) # True
    # print(isinstance(mgr_1, Developer)) # False
    # print(issubclass(Manager, Employee)) # True, Child-Parent
    # print(issubclass(Employee, Manager)) # False
    # print(issubclass(Manager, Developer)) # False

    print(emp_1.__repr__()) # programozóknak
    print(emp_1.__str__()) # felhasználóknak
    print(emp_1 + dev_1) # 110000 - egyébként meg add beépített, de megírás nélkül nem fogja összeadni a fizetéseket (arithmetic class method)
    print(emp_1.must_implement()) # None
    print(dev_1.must_implement()) # Function implemented