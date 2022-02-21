name = "Joshua"

ord_name = {}

for letter in name:
    ord_value = ord(letter)   
    ord_name[letter] = ord_value


print(ord_name)

    
        
new_name =chr(ord_name["J"])+chr(ord_name["o"])+chr(ord_name["s"])+chr(ord_name["h"])+chr(ord_name["u"])+chr(ord_name["a"])


print(new_name)