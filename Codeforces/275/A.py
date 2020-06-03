x11 , x12 , x13 =  map(int,input().split())
x21 , x22 , x23 =  map(int,input().split())
x31 , x32 , x33 =  map(int,input().split())
print(("1" if (x11 + x12 + x21) % 2 == 0 else "0"),
        ("1" if (x11 + x12 + x13 + x22) % 2 == 0 else "0"),
            ("1" if (x12 + x13 + x23) % 2 == 0 else "0"),sep="")
print(("1" if (x11 + x21 + x22 + x31) % 2 == 0 else "0"),
        ("1" if (x12 + x21 + x22 + x23 + x32) % 2 == 0 else "0"),
            ("1" if (x13 + x22 + x23 + x33) % 2 == 0 else "0"),sep="")
print(("1" if (x21 + x31 + x32) % 2 == 0 else "0"),
        ("1" if (x22 + x31 + x32 + x33) % 2 == 0 else "0"),
            ("1" if(x23 + x32 + x33) % 2 == 0 else "0"),sep="")
