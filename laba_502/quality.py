import pytest
import mol1, mol2, mol3, mol4
# import Eratosthenes1

class Test:
    pass

test11 = [[4,4,3,3],[-2,-2,-3,-3]]
test12 = [[4,4,3,3],[-2,-2,3,3]]
test21 = [[7,7,3,3],[1,1,3,3]]

@pytest.mark.parametrize("mol1", [mol1, mol2])
def test_speed_before(mol1):
    o = Test()
    o.points = [[1,1,3,3], [1,1,-3,-3]]
    mol1.update(o)
    #print(o.points)
    assert o.points == test11

    mol1.update(o)
    #print(o.points)
    assert o.points == test21

@pytest.mark.parametrize("mol1", [mol3, mol4])
def test_speed_after(mol1):
    o = Test()
    o.points = [[1,1,3,3], [1,1,-3,-3]]
    mol1.update(o)
    #print(o.points)
    assert o.points == test12

    mol1.update(o)
    #print(o.points)
    assert o.points == test21

    # e = Eratosthenes1.Eratosthenes
    # assert e.is_prime(5) == True
    # assert e.is_prime(6) == False

# test(mol1)
# test(mol2)
# test(mol3)
# test(mol4)