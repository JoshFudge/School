contacts = {
    "Bob": ["bob@bestbobs.com", "709-555-5555"],
    "Alice": ["alice@blizzard.com", "709-555-5556"]
}
space = 20


emails = {}
emails["Bob"] = "bob@bestbobs.com"
emails["Alice"] = "alice@blizzard.com"


phonenum={}
phonenum["Bob"] = "709-555-5555"
phonenum["Alice"]= "709-555-5556"




print(f"Name                  Email                            Phone")
for people in  contacts:
    print(f"{people} {emails[people]:>{space+3}} {phonenum[people]:>{space+12}}")


