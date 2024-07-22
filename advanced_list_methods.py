submitted = ["Alice","Bob", "Charlie", "David"]
attended = ["Alice","Charlie", "Eve", "Frank"]


if ("Alice") in submitted and ("Alice") in attended:
    print("Alice attened class and subbimtted her assignment")  
elif ("Alice") in submitted and ("Alice") not in attended:
    print("Alice submitted her assignment but did not attend class")
elif ("Alice") in attended and ("Alice") not in submitted:
    print("Alice attended class but did not submit her assignment")
else:
    print("Alice is not a great student")