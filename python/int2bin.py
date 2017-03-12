for an_int in range(0, 256 + 1):
    print an_int, "takes", an_int.bit_length(), "bits to represent,",
    print "and equals", bin(an_int), "in binary"

