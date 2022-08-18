from parent.a_subpackage import a_module
from parent.a_subpackage import a2_module


def b_function():
    print('b_function')
    a_module.a_function()
    a2_module.a2_function()


if __name__ == '__main__':
    b_function()
