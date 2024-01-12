#Greeting by name and welcoming into an OS
import platform
name = input("What's your name? Type here: ")
current_system=platform.system()
if current_system=="Linux":
    with open("/etc/os-release", "r") as file:
        os_about = file.readline()
    print(f"Hello {name}, welcome to {current_system}. Here is the OS information: {os_about}")
else:
    print(f"Hello {name}, welcome to {current_system}.")
