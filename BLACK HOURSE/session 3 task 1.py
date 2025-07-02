contacts={"mark": 748342 , "leo" : 786949 , "peter" : 743598}
print("contacts:")
for name in contacts :
    print(name)
search_name=input("enter a name to search:")
if search_name in contacts :
    print(f"{search_name}'s number is {contacts[search_name]}")
else:
    print("contact not found")