n = input()
s = input()
a  = s.count("A")
d  = s.count("D")
if a > d:
    print('Anton')
if a < d:
    print('Danik')
if a == d:
    print('Friendship')