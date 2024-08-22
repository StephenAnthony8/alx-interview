#!/usr/bin/python3
""" Utf-8 validation """


def validUTF8(data):
    """ validates data sets if they are in ut8 format """
    # count: holds the number of trailing bytes
    count = 0
    # loop in which values in data set are counted
    for x in data:
        # check if number is single byte or multi-byte
        if count == 0:
            # single byte
            if x in range(0, 127 + 1):
                continue
            # two byte
            elif x in range(194, 223 + 1):
                count = 1
            # three byte
            elif x in range(224, 239 + 1):
                count = 2
            # four byte
            elif x in range(240, 247 + 1):
                count = 3
            else:
                return (False)

        elif count > 0:
            # if not single byte, trailing bytes should be in given range
            if x in range(128, 191 + 1):
                count -= 1
            else:
                return (False)

    return (True)
