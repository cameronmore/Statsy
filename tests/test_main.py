from src.statsy import summation

def simple_test_summation():
    value = summation(i=None,range=None,expression=lambda x: x*2,data=[[1,2,3]])
    assert value == 12

def complex_test_summation():
    value = summation(i=2,range=2,expression=lambda y, x, r: x*y*r,data=[[1,2,3],[4,5,6],[2,2,2]]) 
    assert value == 56


#def test_dummy():
#    pass