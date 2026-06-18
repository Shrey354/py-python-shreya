pwd = input("Enter your master password.")
def view():
    pass
def add():
    pass
while True:
    mode = input("Would you like to add a new password or view the existing one. Press 'q' to quit.")
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode")
        continue
