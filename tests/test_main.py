from statsy import summation

def simple_test_summation():
    assert summation(i=None,range=None,expression=lambda x: x*2,data=[[1,2,3]]) == 12

def complex_test_summation():
    assert summation(i=2,range=2,expression=lambda y, x, r: x*y*r,data=[[1,2,3],[4,5,6],[2,2,2]]) == 56
