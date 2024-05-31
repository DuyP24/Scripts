from netmiko import ConnectHandler
from getpass import getpass

def display_menuA():
    print('1. Configure by Command Line (SSH)')
    print('2. Show Info')

def display_menuA_1():
    print('1. Show IP table')
    print('2. Show IP Route')

def display_menu1():
    print("1. Network Device")
    print("2. Server")

def display_menu2_a():
    print("1. Router")
    print("2. Switch")
    print("3. Firewall")

def display_menu3_a():
    print("1. Main Router")
    print("2. Secondary Router")

def display_menu4_a():
    print("1. Core Switch")
    print("2. Layer 2 Switch")

def display_menu5_a():
    print("1. Main Firewall")
    print("2. Secondary Firewall")

def display_menu6_a():
    print("1. Core 1")
    print("2. Core 2")

def display_menu7_a():
    print("1. Switch 1")
    print("2. Switch 2")

def display_menu2_b():
    print("1. Server Data")
    print("2. Server Web")

def main():
    while True:
        display_menu1()
        choice = int(input("Enter your choice (1 or 2): "))

        if choice == 1:
            while True:
                display_menu2_a()
                sub_choice1 = int(input("Enter your choice (1 to 3): "))

                if sub_choice1 == 1:
                    print("You selected Router")
                    while True:
                        display_menu3_a()
                        sub_choice2 = int(input("Enter your choice (1 or 2): "))

                        if sub_choice2 == 1:
                            print("You select Main Router")
                            while True:
                                display_menuA()
                                sub_choice3 = int(input("Enter your choice (1 or 2): "))

                                if sub_choice3 == 1:
                                    print("Log In SSH credential")
                                    from netmiko import ConnectHandler
                                    from getpass import getpass
                                    # Prompt for username
                                    username = input("Enter username: ")

                                    # Prompt for password securely
                                    password = getpass()

                                    # Establish SSH connection
                                    net_connect = ConnectHandler(
                                        host="192.168.183.133",
                                        username=username,
                                        password=password,
                                    )

                                    # Find device prompt
                                    print(net_connect.find_prompt())

                                    # Send a sample command (replace with your desired command)
                                    output = net_connect.send_command("show hostname")
                                    print(output)

                                    # Always close the connection
                                    net_connect.disconnect()
                                elif sub_choice3 == 2:
                                    print("What do you want to know? ")
                                    display_menuA_1()
                                    sub_choice4 = int(input("Enter your choice (1 or 2): "))

                                    if sub_choice4 == 1:
                                        print("Show IP Table")
                                        # Define the device info
                                        device = {
                                                "host": "192.168.183.133",
                                                "username": "duyp",
                                                "password": "duyp",
                                                }
                                        #Define command
                                        command = "show ip table"
                                        #Connect SSH
                                        net_connect = ConnectHandler(**device)
                                        #Send command
                                        output = net_connect.send_command("show ip int brief")
                                        #Print Output
                                        print(output)
                                        #Logout SSH
                                        net_connect.disconnect()
                                        break
                                    elif sub_choice4 == 2:
                                        print("Show IP Route")
                                        # Define the device info
                                        device = {
                                                "host": "192.168.183.133",
                                                "username": "duyp",
                                                "password": "duyp",
                                                }
                                        #Define command
                                        command = "show ip route"
                                        #Connect SSH
                                        net_connect = ConnectHandler(**device)
                                        #Send command
                                        output = net_connect.send_command("show ip route")
                                        #Print Output
                                        print(output)
                                        #Logout SSH
                                        net_connect.disconnect()
                                        break
                                    else:
                                        print("Enter valid option")
                                        continue
                                else:
                                    print("Enter valid option")
                                    continue
                            break
                        elif sub_choice2 == 2:
                            print("You select Secondary Router")
                            break
                        else:
                            print("Enter valid option")
                            continue
                    break

main()