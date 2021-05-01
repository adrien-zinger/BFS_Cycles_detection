import pytest
import dfscycles

inputs_single2 = ['10', '4 10', '7 2', '2 1', '4 1', '8 10', '8 0', '7 4', '5 10', '7 0', '8 5']
def test_single2():
    class _s:
        o = ''
    def p(o):
        print(o)
        _s.o = o
    i = iter(inputs_single2)
    dfscycles.input = lambda: next(i)
    dfscycles.print = p
    dfscycles.run()
    assert _s.o == '1 3'

# should find 4 shapes in two diferent graphs
inputs_complex = ['13', '4 10', '7 2', '2 1', '4 1', '8 10', '3 9', '6 3', '8 0', '7 4', '5 10', '9 6', '7 0', '8 5']

def test_complex():
    class _s:
        o = ''
    def p(o): _s.o = o
    i = iter(inputs_complex)
    dfscycles.input = lambda: next(i)
    dfscycles.print = p
    dfscycles.run()
    assert _s.o == '2 4'