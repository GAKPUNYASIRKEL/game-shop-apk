print("Welcome to the Event System")


def menu():
    print("Choose the number from menu")
    print("1:Create Customer")
    print("2:Reserve a seat")
    print("3.Cancel the seat")
    print("4.Exit the Event System")
    option = input("put down the number")
    return option

def executingmenuinputchoice(option):
    if(option == 1):
        createcust()
    elif(option == 2):
        reserveseat()
    elif(option == 3):
        cancelseat()
    elif(option == 4):
        exit()
    else:
        print('you have chose a wrong option')
        menu()


def createcust():
    print('Provide Customer details')
    name = input('Full name? --> ')
    pno = input('phone number? -> ')
    email = input('Email Id? --> ')
    try:
        file = open("cust.txt", "r")
        lines = file.read().splitlines()
        last_lines = lines[-1]
        content = last_lines.split()
        refno = random.randint(10001, 99999)
        file.close()
        file = open("cust.txt", "a")
        file.write("\n"+" "+name+" "+pno+" "+email+" "+refno)
        file.close()
        print(refno + 'is your reference number')
        print('Added Customer to file')
    except IOError:
        print("File doesn't exist at location")
    except TypeError:
        print('input proper data')
    return createcust()
