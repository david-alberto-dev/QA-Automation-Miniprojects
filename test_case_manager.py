# setup
test_cases = []
used_ids = []

# functions
def show_menu():
    print("""
    ----- Test Case Management -----
    1. Add test case
    2. View test cases
    3. Delete test case
    4. Update test case status
    5. Quit program
    ---------------------------------
    What would you like to do?
    """)

def add_test_case():
    print("Alright, let's add a test case.")

    test_case_id = input("Enter test case id: ").strip()
    if not test_case_id:
        print("IDs cannot be empty.")
    if test_case_id in used_ids:
        print("IDs must be unique.")
        return
    used_ids.append(test_case_id)

    title = input("Enter test case title: ").strip()
    if not title:
        print("You must enter a test case title.")
        return

    expected_result = input("Enter test case expected result: ").strip()
    if not expected_result:
        print("You must enter a test case expected result.")
        return

    actual_result = input("Enter test case actual result: ").strip()
    if not actual_result:
        print("You must enter a test case actual result.")
        return

    status = input("Enter test case status: ").strip()
    if not status:
        status = "Pending"

    notes = input("(Optional) Enter test case notes: ").strip()
    if not notes:
        notes = "User didn't add any notes."

    test_case = {
        "test_case_id": test_case_id,
        "title": title,
        "expected_result": expected_result,
        "actual_result": actual_result,
        "status": status,
        "notes": notes
    }

    test_cases.append(test_case)
    print("Test case added!")

def view_test_cases():
    if not test_cases:
        print("There are no test cases.")
    else:
        for i, tc in enumerate(test_cases, start=1): # tc = test_case
            print(f"{i}.")
            print(f"ID: {tc['test_case_id']}")
            print(f"Title: {tc['title']}")
            print(f"Expected result: {tc['expected_result']}")
            print(f"Actual result: {tc['actual_result']}")
            print(f"Status: {tc['status']}")
            print(f"Notes: {tc['notes']}")
            print("=" * 10)

def delete_test_case():
    if not test_cases: # check if empty
        print("There are no test cases, so you can't remove anything.")
        return
    else:
        view_test_cases() # show test cases
        try:
            choice = int(input("Enter the index of what you want to delete: "))
        except ValueError:
            print("Must be an integer.") # in case user doesn't enter a num
            return
        if choice < 1:
            print("Index must not be less than 1.")
            return
        if choice > len(test_cases):
            print("Index must not be greater than the number of test cases.")
            return
        else:
            choice -= 1  # get real index
            used_ids.remove(test_cases[choice]["test_case_id"])
            test_cases.pop(choice)
            print("Test case deleted!")

def update_test_case():
    if not test_cases: # check if empty
        print("There are no test cases, so you can't update anything.")
        return
    else:
        view_test_cases()
        try:
            index_to_update = int(input("Enter index of the test case status you want to update: "))
            if not index_to_update:
                print("You must enter a test case status.") # can't be empty
                return
        except ValueError:
            print("Must be an integer.")
            return
        if index_to_update < 1:
            print("Index must not be less than 1.")
            return
        if index_to_update > len(test_cases):
            print("Index must not be greater than the number of test cases.")
            return

        updated_status = input("Enter test case status: ").strip()
        if not updated_status:
            print("You must enter a test case status.")
            return
        else:
            real_index = index_to_update - 1
            test_cases[real_index]["status"] = updated_status
            print("Test case status updated!")


def quit_program():
    option = input("Do you want to quit? (y/n) ").strip().lower()
    if option == "y":
        print("Quitting...")
        exit()

# main
while True:
    show_menu()
    choice = input("Enter your choice: ").strip()
    match choice:
        case "1" | "one":
            add_test_case()
            continue
        case "2" | "two":
            view_test_cases()
            continue
        case "3" | "three":
            delete_test_case()
            continue
        case "4" | "four":
            update_test_case()
            continue
        case "5" | "five":
            quit_program()
            continue
        case _:
            print("Invalid choice, try entering a number from 1 to 5.")
            continue