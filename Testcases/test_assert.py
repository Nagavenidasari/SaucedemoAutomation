import pytest

def add(a,b):
    return a+b


@pytest.mark.parametrize("a,b,output",[(5,6,11),(5,5,10),(8,8,16),(10,10,30)])
def test_calculate(a,b,output):
    result = add(a,b)
    assert output == result

#def test_add():
 #   result = add(10,30)
  #  assert 40==result

   # result = add(45,5)
    #assert 45==result
