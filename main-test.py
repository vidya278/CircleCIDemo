
from main import ADD
def TestAdd():
    assert ADD(2,3) == 5
    assert ADD(6,3) == 9
    print("Add works !!!")

if __name__ == '__main__':
    TestAdd()