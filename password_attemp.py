

for i in range(3):
    password = input("Ingrese una contraseña que empiece con un número: ") # Enter a password that starts with a number

    # Verificar que la contraseña empieza con un número / Verify that the password starts with a number
    if not password[0].isdigit():
        print("La contraseña debe empezar con un número.") # The password must start with a number.
    else:
        # Pedir que se ingrese la contraseña nuevamente y verificar que coincida / Ask to enter the password again and verify that it matches
        for j in range(2):
            password2 = input("Ingrese la contraseña nuevamente: ") # Enter the password again
            if password == password2:
                print("Contraseña confirmada.") # Password confirmed.
                break
            else:
                print("Las contraseñas no coinciden.") # Passwords do not match.
        else:
            print("Ha ingresado la contraseña incorrecta dos veces.") #You have entered the wrong password twice.
        break
else:
    print("Ha ingresado la contraseña incorrecta tres veces. El programa se cerrará.") #You have entered the wrong password three times. The program will close.
    exit()

