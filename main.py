# а
print("а")
string = ""
for i in range(5):
    for j in range(5):
        if(i<=j):
            string += " * "
        else:
            string += " . "
    string += "\n"
print(string)

# б
print("б")
string = ""
for i in range(5):
    for j in range(5):
        if(i>=j):
            string += " * "
        else:
            string += " . "
    string += "\n"
print(string)

# в
print("в")
string = ""
for i in range(5):
    for j in range(5):
        if(j<5-i) and (i<=j):
            string += " * "
        else:
            string += " . "
    string += "\n"
print(string)

# г
print("г")
string = ""
for i in range(5):
    for j in range(5):
        if(j>=5-i-1) and (i>=j):
            string += " * "
        else:
            string += " . "
    string += "\n"
print(string)

# д
print("д")
string = ""
for i in range(5):
    for j in range(5):
        if(j>=5-i-1) and (i>=j) or (j<5-i) and (i<=j):
            string += " * "
        else:
            string += " . "
    string += "\n"
print(string)


# е
print("е")
string = ""
for i in range(5):
    for j in range(5):
        if(j<=5-i-1) and (i>=j) or (j>=5-i-1) and (i<=j):
            string += " * "
        else:
            string += " . "
    string += "\n"
print(string)

# ж
print("ж")
string = ""
for i in range(5):
    for j in range(5):
        if(j<=5-i-1) and (i>=j):
            string += " * "
        else:
            string += " . "
    string += "\n"
print(string)

# з
print("з")
string = ""
for i in range(5):
    for j in range(5):
        if(j>=5-i-1) and (i<=j):
            string += " * "
        else:
            string += " . "
    string += "\n"
print(string)

# и
print("и")
string = ""
for i in range(5):
    for j in range(5):
        if(5-j>i):
            string += " * "
        else:
            string += " . "
    string += "\n"
print(string)

# к
print("к")
string = ""
for i in range(5):
    for j in range(5):
        if(4-j>i):
            string += " . "
        else:
            string += " * "
    string += "\n"
print(string)