def dec_to_hex(dec):
    result = ''
    rs = list()
    while dec > 16:
        dec = dec // 16
        rs.append(dec)
    rs.append(dec)

    def dth(d):
        if d == 0:
            h = '0'
        elif d == 1:
            h = '1'
        elif d == 2:
            h = '2'
        elif d == 3:
            h = '3'
        elif d == 4:
            h = '4'
        elif d == 5:
            h = '5'
        elif d == 6:
            h = '6'
        elif d == 7:
            h = '7'
        elif d == 8:
            h = '8'
        elif d == 9:
            h = '9'
        elif d == 10:
            h = 'a'
        elif d == 11:
            h = 'b'
        elif d == 12:
            h = 'c'
        elif d == 13:
            h = 'd'
        elif d == 14:
            h = 'e'
        elif d == 15:
            h = 'f'
        elif d == 16:
            h = '0'
        return h

    for i in range(len(rs)):
        hex = dth(rs[i])
        result = result + hex

    if not '1' in result and not '2' in result and not '3' in result and not '4' in result and not '5' in result and not '6' in result and not '7' in result and not '8' in result and not '9' in result:
        result = '1' + result

    return result

print(dec_to_hex(238))