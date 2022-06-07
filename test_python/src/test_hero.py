import pydoc

import pytest



def inc(x):
    return x + 1



@pytest.mark.parametrize('a,b',[(10,20),(1,2),(3,4)])
def test_answer(a,b):
    assert inc(a) == b

@pytest.fixture()
def login():

    print('登录操作')
    name = 'Jerry'
    return name

class Testc:
    def test_a(self,login):
        print(f"a my name = {login}")

    def test_b(self):
        print('b')

    def test_c(self,login):
        print(f"c my name = {login}")

if __name__ == '__main__':
    pytest.main(['test_hero.py'])

