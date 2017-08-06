def remove_dollar_sign(s):
    string = s
    r = string.replace('$','')
    return r
## s is the input string and r is the string after removed dollar sign

string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")

    
