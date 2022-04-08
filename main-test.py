
from main import ADD
mkdir .circleci
touch .circleci/config.yml
def TestAdd():
    assert ADD(2,3) == 5
    assert ADD(2,3) == 9
    print("Add works !!!")

if __name__ == '__main__':
    TestAdd()