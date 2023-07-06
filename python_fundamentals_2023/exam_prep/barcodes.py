import re

pattern = r"^b@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$"
# ^ -> begins with
# $ -> ends with
regex = re.compile(pattern)
digit_regex = re.compile(r"\d")
# makes it faster, instead of compiling it every iteration of the loop

3
n = int(input())

for _ in range(n):

    raw_data = input()
    if regex.match(raw_data):
        digits = digit_regex.findall(raw_data)
        # product_group = "".join(digits) if digits else "00"
        if digits:
            product_group = "".join(digits)
        else:
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
