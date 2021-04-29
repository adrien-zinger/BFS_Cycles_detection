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
inputs2 = ['13', '4 10', '7 2', '2 1', '4 1', '8 10', '3 9', '6 3', '8 0', '7 4', '5 10', '9 6', '7 0', '8 5']
def _test_basic():
    class _s:
        o = ''
    def p(o): _s.o = o
    i = iter(inputs)
    dfscycles.input = lambda: next(i)
    dfscycles.print = p
    dfscycles.dfscycle()
    assert _s.o is 3

def test_edges():
    class _s:
        o = ''
    def p(o): _s.o = o
    i = iter(inputs)
    dfscycles.input = lambda: next(i)
    dfscycles.print = p
    dfscycles.dfsedges()
    assert _s.o is 6