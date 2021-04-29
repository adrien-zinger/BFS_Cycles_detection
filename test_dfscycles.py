import pytest
import dfscycles

#
#  1 --- 4 -- 10 -- 5 -- 11
#  |   / |     \   /    /
#  | /   |      \ /    /
#  2 --- 7       8 ---9
#   \     \     /
#    \     \   /
#     \     \ /
#      12 ---- 0
inputs = ['14', '1 4', '4 10', '10 5', '5 11', '4 2', '2 12', '12 0', '0 7', '7 4', '0 8', '8 10', '8 5', '8 9', '9 11']


#                 1 --- 4 -- 10 -- 5
#                 |     |     \   /
#                 |     |      \ /
#                 2 --- 7       8
#                        \     /
#      3 --- 6            \   /
#       \   /              \ /
#        \ /                0
#         9

# should find 4 shapes in two diferent graphs
inputs_complex = ['13', '4 10', '7 2', '2 1', '4 1', '8 10', '3 9', '6 3', '8 0', '7 4', '5 10', '9 6', '7 0', '8 5']

def _test_complex():
    class _s:
        o = ''
    def p(o): _s.o = o
    i = iter(inputs_complex)
    dfscycles.input = lambda: next(i)
    dfscycles.print = p
    dfscycles.run()
    assert _s.o == '2 4'

def _test_shapes():
    class _s:
        o = ''
    def p(o): _s.o = o
    i = iter(inputs)
    dfscycles.input = lambda: next(i)
    dfscycles.print = p
    dfscycles.run()
    assert _s.o == '1 6'


inputs_single = ['3', '1 2', '2 3', '3 1']
def _test_single():
    class _s:
        o = ''
    def p(o): _s.o = o
    i = iter(inputs_single)
    dfscycles.input = lambda: next(i)
    dfscycles.print = p
    dfscycles.run()
    assert _s.o == '1 1'

#    1 --- 4 -- 10 -- 5
#    |     |     \   /
#    |     |      \ /
#    2 --- 7       8
#           \     /
#            \   /
#             \ /
#              0

inputs_single2 = ['10', '4 10', '7 2', '2 1', '4 1', '8 10', '8 0', '7 4', '5 10', '7 0', '8 5']
def test_single2():
    class _s:
        o = ''
    def p(o): _s.o = o
    i = iter(inputs_single2)
    dfscycles.input = lambda: next(i)
    dfscycles.print = print
    dfscycles.run()
    assert _s.o == '1 3'