from parent.a_subpackage import a_module


def b_function():
    print('b_function')
    a_module.a_function()


if __name__ == '__main__':
    b_function()
