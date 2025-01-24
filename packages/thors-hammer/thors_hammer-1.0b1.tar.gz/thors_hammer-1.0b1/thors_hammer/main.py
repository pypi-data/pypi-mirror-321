from random import choice
import string
import json
from sys import platform
from os import system

def clear() -> None:
    """
    Clear the terminal
    """
    if platform == "win32":
        system("cls")
    else:
        system("clear")

def write_config_to_file(config: dict) -> None:
    """
    Self-explanatory
    """
    with open("config.json", "w") as temp:
        json.dump(config, temp, ensure_ascii = False, indent = 4)

def isInt(input: str) -> bool:
    """
    Return True if input is an integer, else return False
    """
    try:
        int(input)
        return True
    except ValueError:
        return False

def PasswordGenerator(password_length: int, charlist: list) -> str:
    """
    Generate password with length equals to password_length and characters takes from charlist
    """
    output = ""
    while len(output) < password_length:
        output += choice(charlist)
    return output

def check_config() -> None:
    """
    Check if config is valid or not, reset the config to default if the config file is not valid, create a new config file if missing
    """
    def_config = {
        "passwordLength": 8,
        "isUppercaseLettersEnabled": True,
        "isNumberEnabled": True,
        "isSpecialCharactersEnabled": True
    }
    with open("config.json", "w") as temp:
        temp.write("{}")
    with open("config.json") as temp:
        config = json.load(temp)
    if len(config) != len(def_config):
        with open("config.json", "w") as temp:
            json.dump(def_config, temp, ensure_ascii = False, indent = 4)
        return config    

def main() -> None:
    """
    The main function
    """
    check_config()
    with open("config.json") as temp:
        config = json.load(temp)

    clear()
    while True:
        count = 0
        cmd = input("1. Generate passwords. \n2. Config. \n3. Exit. \nYour input: ").strip()
        clear()
        if cmd == "3":
            exit(0)
        elif not cmd:
            print("Invalid input: Empty input. \n")
            continue
        elif cmd not in [*"12"]:
            print("Invalid input: Command does not exist. \n")
            continue
        
        while cmd == "2":
            option = input(f"""Config password generation.
1. Config password length.
2. Generate uppercase alphabetical characters: {config["isUppercaseLettersEnabled"]}.
3. Generate numbers: {config["isNumberEnabled"]}.
4. Generate special characters: {config["isSpecialCharactersEnabled"]}.
5. Menu.
Toggle: """).strip()
            clear()
            if option == "2": config["isUppercaseLettersEnabled"] = not config["isUppercaseLettersEnabled"]
            elif option == "3": config["isNumberEnabled"] = not config["isNumberEnabled"]
            elif option == "4": config["isSpecialCharactersEnabled"] = not config["isSpecialCharactersEnabled"]
            elif not option: print("Invalid input: Empty input. \n")
            elif option == "1":
                while True:
                    print(f"Password length: {config["passwordLength"]}.")
                    p_len = input("Enter the length of your password (Enter / to cancel): ").strip()
                    clear()
                    if p_len == "/":
                        break
                    elif not p_len:
                        print("Invalid input: Empty input. \n")
                    elif not isInt(p_len):
                        print("Invalid input: Input have to be an integer. \n")
                    elif int(p_len) <= 0:
                        print("Invalid input: Password length cannot be 0 or less. \n")
                    else:
                        config["passwordLength"] = int(p_len)
            else: print("Invalid input: Option does not exist. \n")
            write_config_to_file(config)

        password_chars = [*string.ascii_lowercase]
        if config["isUppercaseLettersEnabled"]: password_chars += [*string.ascii_uppercase]
        if config["isNumberEnabled"]: password_chars += [*string.digits]
        if config["isSpecialCharactersEnabled"]: password_chars += [*string.punctuation.replace("|", "")]

        if cmd == "1":
            password = PasswordGenerator(config["passwordLength"], password_chars)
        while cmd == "1":
            print(f"Output: {password} \n")
            regen = input("Do you want to regenerate your password? [Y/N]: ").strip().upper()
            clear()
            if regen == "N":
                break
            elif not regen or regen == "Y":
                password = PasswordGenerator(config["passwordLength"], password_chars)
            else:
                print("Invalid input: Option does not exist. \n")

if __name__ == "__main__":
    main()