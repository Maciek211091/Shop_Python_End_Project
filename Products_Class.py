from abc import ABC
import Custom_Exceptions


class Clothing(ABC):

    def __init__(self, sex: str, size: str, num_of_elements: int):
        self.sex = sex
        self.size = size
        self.num_of_elements = num_of_elements

    def get_num_of_el(self):
        return self.num_of_elements

    def get_sex(self):
        return self.sex

    def get_size(self):
        return self.size

    def add_stock(self, quantity):
        self.num_of_elements += quantity

    def reduce_stock(self, quantity):
        if self.num_of_elements >= quantity:
            self.num_of_elements -= quantity
        else:
            raise Custom_Exceptions.Less_Than_Zero_Exception


class T_Shirt(Clothing):

    def __init__(self, sex: str, size: str, num_of_elements: int, cl_type: str):
        super().__init__(sex, size, num_of_elements)
        self.cl_type = cl_type

    def __str__ (self):
        return f"{self.sex} T-Shirt, size {self.size}, current stock {self.num_of_elements}"





