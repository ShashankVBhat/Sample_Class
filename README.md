# sampleclass

sampleclass package is used to claculate different mathematical operations like add, multiply, subtract, division of 2 numbers.
![Alt Colour Family](https://github.com/ShashankVBhat/Sample_Class/tree/master/images/lena.jpg)
## Installation

You can install the sampleclass from [PyPI]

    pip install sampleclass

## How to use

sampleclass has a class named Operators which consists of methods - add(), subtract(), multiply() & dividion().
It accepts integers & floating numbers.

Example of usage is shown below:

from sampleclass.sample_class import Operators

obj = Operators(5.0, 6.0)

print(obj.add())

print(obj.multiply())

print(obj.subtract())

print(obj.division())

Output:

11.0

30.0

-1.0

0.8333333333333334
