from notes import add_notes, view_notes, delete_notes

def show_menu():
    print("\n====CLI NOTES MANAGER====")
    print("1. Add Note")
    print("2. View Note")
    print("3. Delete Note")
    print("4. Exit")
def main():
    while True:
	show_menu()
	choice = input("Enter your choice: ")
	if choice == "1":
	    add_notes()
	elif choice == "2":
	    view_notes()
	elif choice == "3":
	    delete_notes()
	elif choice == "4":
	    print("You Exited the program!")
	    break
	else:
	    print("Invaild Choice! try again ")
if __name__ == "__main__":
    main()


