

for i in range(3):
    password = input("Ingrese una contraseña que empiece con un número: ")

    # Verificar que la contraseña empieza con un número
    if not password[0].isdigit():
        print("La contraseña debe empezar con un número.")
    else:
        # Pedir que se ingrese la contraseña nuevamente y verificar que coincida
        for j in range(2):
            password2 = input("Ingrese la contraseña nuevamente: ")
            if password == password2:
                print("Contraseña confirmada.")
                break
            else:
                print("Las contraseñas no coinciden.")
        else:
            print("Ha ingresado la contraseña incorrecta dos veces.")
        break
else:
    print("Ha ingresado la contraseña incorrecta tres veces. El programa se cerrará.")
    exit()

