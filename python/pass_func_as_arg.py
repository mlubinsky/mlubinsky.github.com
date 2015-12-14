"""
https://www.snip2code.com/Snippet/44738/Decide-which-algorithm-to-use-from-the-o
decide which algorithm to use from the outside
"""

def compute(op, a, b, c):

    def foo():
        # some awfully complicated calculation...
        return (a+b)/c

    def bar():
        # another awfully complicated calculation...
        return a+c

    def baz():
        # yet another complicated calculation...
        return a*b

    def error():
        raise Exception("Big mistake! There's no '{0}' algorithm".format(op))

    if callable(op):
        result = op(a, b, c)
        algorithm = op.func_name
    else:
        result = locals().get(op, error)()
        algorithm = op

    print "for algorithm", algorithm,
    # you do the long, boring common stuff here
    result += c
    result /= 100.
    return result


if __name__ == "__main__":

    print "The result is..."
    print compute("foo", 1,2,3)
    print compute("bar", 1,2,3)
    # extra external algorithm
    def foobar(a, b, c):
        return a/(b + c)
    print compute(foobar, 1,2,3)
    # no such algorithm
    print compute("baZ", 1,2,3)
