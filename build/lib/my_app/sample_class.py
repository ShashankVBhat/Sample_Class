import sys


class Operators:
    def __init__(self, operand_1, operand_2):
        self.operand_1 = operand_1
        self.operand_2 = operand_2
        self.self_check(self)

    @staticmethod
    def self_check(self):
        if not isinstance(self.operand_2, (int, float, list)) or not isinstance(
                self.operand_1, (int, float, list)):
            print("Kindly enter integer.")
            sys.exit()

    def add(self):
        return self.operand_1 + self.operand_2

    def multiply(self):
        return self.operand_1 * self.operand_2

    def subtract(self):
        return self.operand_1 - self.operand_2

    def division(self):
        if self.operand_2 == 0:
            return "Cant divide a number by zero."
        else:
            return self.operand_1 / self.operand_2


if __name__ == "__main__":
    obj = Operators(5.0, 6.0)
    print(obj.add())
    print(obj.multiply())
    print(obj.subtract())
    print(obj.division())


