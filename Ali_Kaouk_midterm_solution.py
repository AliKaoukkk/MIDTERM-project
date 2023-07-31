#positivr

special_list = []  # we use a global variable for special list


def adminAttempts():  # admin login attempts fnction
    attempts = 5
    while attempts != 0:
        user_name = input("Enter user name: ")
        user_password = input("Enter user password: ")
        if user_name == 'admin' and user_password == 'admin123123':
            print('Login successful.')
            return
        else:
            attempts -= 1
            print('Wrong username or/and password remaining attempts ', attempts)
    print('you exited')


# Admin display menu
def displayMenu():
    print(
        "1.Display Statistics\n2.Book a Ticket\n3.Display all Tickets\n4.Change Ticket’s Priority\n5.Disable Ticket\n6.Run Events\n7.Exit")


# user display menu
def secondMenu():
    print('1.Book a ticket\n2.Exit')


def importTickets(filename):  # here is a function to read from txt.file and import them to S.list
    with open(filename, 'r') as file:
        for line in file:
            ticket_information = line.strip().split(", ")
            ticket_id, event_id, username, date_1, priority =            ticket_information
            special_list.append({
                "ticket_id": ticket_id,
                "event_id": event_id,
                "username": username,
                "timestamp": timestamp,
                "priority": int(priority)
            })

def mergeSort(tickets): # A function to sort tickets by date and event ID
    if len(tickets) <= 1:
        return tickets
    mid = len(tickets) // 2 #using merge sort algor we divide the list into 3 parts , first is the (mid) of list
    first_half = tickets[:mid] #the second part of the list while using the mid as our center and now we got our right side 
    second_half = tickets[mid:] # and the left side using our mid as the center 
    second_half = mergeSort(second_half) # recurisvley called the function 
    first_half = mergeSort(first_half) # same as above
    return mergeSort(second_half, first_half)

def adminBook(): #2
    tikcet_id = "ticket"
    ticket_id = f"tick{len(special_list) + 1:03d}"  #:03d: This is a formatting specifier that specifies how the expression inside the curly braces should be formatted. In this case, :03d means that the expression should be formatted as an integer (d) with at least 3 digits. If the number has fewer than 3 digits, it will be left-padded with zeroes. https://stackoverflow.com/questions/6869999/fixed-width-number-formatting-python-3
    event_id = input('Enter event ID: ')
    username = input('Enter username: ')
    priority = int(input('Enter Priority: '))
    timestamp = input('Enter date of event (YYYYMMDD) in this format')
    special_list.append({
        "ticket_id": ticket_id,
        "event_id": event_id,
        "username": username,
        "timestamp": timestamp,
        "priority": priority
    })
    print('ticket successfully booked!')

def displayStats(): #1
    event_counts = {}
    for ticket in special_list:
        event_id = ticket["event_id"]
        event_counts[event_id] = event_counts.get(event_id, 0) + 1
    
    max_events = max(event_counts, key=event_counts.get)
    print(f"Event ID with the highest number of tickets: {max_events}")

def displayTickets(): #3
    today = input("Enter today's date (YYYYMMDD): ")
    sorted_tickets = mergeSort(special_list)
    for ticket in sorted_tickets:
        if ticket["timestamp"] >= today:
            print(f"Ticket ID: {ticket['ticket_id']}, Event ID: {ticket['event_id']}, "
                  f"Username: {ticket['username']}, Date: {ticket['timestamp']}, "
                  f"Priority: {ticket['priority']}")
          

def changePriority(): #4
    ticket_id = input('Enter Ticket ID: ')
    for ticket in special_list:
        if ticket['ticket_id'] == ticket_id:
            priority = int(input('Enter a new priority: '))
            ticket['priority'] = priority
            print('priority updated')
            return
    print('ticket was not found')


def disableTicket(): #5
    ticket_id = input('enter ticket ID')
    for tickets in special_list:
        if tickets['ticket_id'] == ticket_id:
            special_list.remove(tickets)
            print('ticket disabled')
            return
    print('ticket was not found')

def runEvents():
    today = input("Enter today's date (YYYYMMDD): ")
    today_events = []

    for ticket in special_list:
        if ticket["timestamp"] == today:
            today_events.append(ticket)

    # Sort today_events based on ticket priority using Merge Sort
    sorted_today_events = mergeSort(today_events)

    for ticket in sorted_today_events:
        print(f"Running Event: {ticket['event_id']}, Priority: {ticket['priority']}")
        special_list.remove(ticket)

def adminMenu():
    displayMenu()
    choice = input('enter a choice: ')
    while choice != '6':
        if choice == '1':
            displayStats()
            print('-' *40)
            displayMenu()
            choice = input('enter a choice: ')
        elif choice == '2':
            adminBook()
            print('-' *40)
            displayMenu()
            choice = input('enter a choice: ')
        elif choice == '3':
            displayTickets()
            print('-' *40)
            displayMenu()
            choice = input('enter a choice: ')
        elif choice == '4':
            changePriority()
            print('-' *40)
            displayMenu()
            choice = input('enter a choice: ')
        elif choice == '5':
            disableTicket()
            print('-' *40)
            displayMenu()
            choice = input('enter a choice: ')
        elif choice == '6':
            runEvents()
            print('-' *40)
            displayMenu()
            choice = input('enter a choice: ')
        else:
            print('thanks for using my program you exited')
            return


def userFunction():
    secondMenu()
    choice = input('enter a choice: ')
    if choice == '1':
        adminBook()
        secondMenu()
        choice = input('enter a choice: ')
    else:
        print('you exit')


def mainSystem():
    print('Welcome to the corrupted ticket system\nplease select a choice: ')
    choice_0 = input('1-login as admin 2-guest: ')
    if choice_0 == '1':
        adminAttempts()
        adminMenu()
    elif choice_0 == '2':
        userFunction()
    else:
        print('please enter a correct input')


mainSystem()
