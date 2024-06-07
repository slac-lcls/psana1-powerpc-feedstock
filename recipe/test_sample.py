""" run it as
    pytest psana/psana/tests/ # in your git root directory or
    pytest test_sample.py
"""

def func(x):
    return x + 1

def test_answer():
    print('test_answer provides true assert')
    assert func(3) == 4

#test_answer()

# EOF
