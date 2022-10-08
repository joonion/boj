a = ['one', 'two', 'three', 'four', 'five', 
     'six', 'seven', 'eight', 'nine', 'ten', 
     'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 
     'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']

def solve(h, m):
    if m == 0:
        print(f"{a[h-1]} o' clock")
    elif m <= 20:
        print(f"{a[m-1]} past {a[h-1]}")
    elif m < 30:
        print(f"twenty {a[m-21]} past {a[h-1]}")
    elif m == 30:
        print(f"half past {a[h-1]}")
    elif m < 40:
        print(f"twenty {a[39-m]} to {a[h%12]}")
    else:
        print(f"{a[59-m]} minutes to {a[h%12]}")
    
h, m = int(input()), int(input())
solve(h, m)