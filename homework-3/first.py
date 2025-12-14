"""
მოცემული გვაქვს სტრიქონი “azcbobobegghakl”. ვიპოვოთ ყველაზე გრძელი
ქვესტრიქონი, რომელიც ანბანის მიხედვით იქნება დალაგებლი (ერთმანეთის ტოლი
სიმბოლოები ითვლება.
"""

string = "azcbobobegghakl"
max_str = string[0]
curr_str = string[0]
max_len = 0

for c in string[1:]:
    if c >= curr_str[-1]:
        curr_str += c
        if len(curr_str) > len(max_str):
            max_str = curr_str
    else:
        curr_str = c

print(f"The maximum substring is '{max_str}'")
