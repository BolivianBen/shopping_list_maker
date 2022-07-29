

shopping_list = []



def add_item(item):
    shopping_list.append(item)
    print("added! there are {} items on your list".format(len(shopping_list)))


def show_help():
    print("what do you need at the store? ")
    print("""
Enter "DONE" to stop adding items
Enter "HELP" for some help
Enter "SHOW" to see the whole list
""")


def show_list():
    print("here is your list: ")
    for i in shopping_list:
        print(i)
    
show_help()

while True:
    new_item = input("> ")

    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue

    add_item(new_item)


show_list()
