#!/usr/bin/python3
for a in range(0, 100):
    
    print("{},".format(str(a).zfill(2)), end=' ') 
    if a == 99:
        print("\b\b ")
  