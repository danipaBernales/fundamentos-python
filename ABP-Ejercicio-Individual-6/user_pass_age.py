import time, re

#Almacenar los datos del usuario
user_data = []

#Nombre de usario válido
def validate_username(username):
    if not re.match("^[a-zA-Z0-9_]{3,20}$", username):
        return False
    else:
        return True

#Contraseña válida
def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search("[a-zA-Z]", password) or not re.search("[0-9]", password):
        return False
    if " " in password:
        return False 
    else:
        return True

#Solicita edad y devuelve la ingresada por el usuario
def get_age():
    while True:
        age_str = input("Ingresa tu edad chore: ")
        if not age_str:
            print("Error! Debes ingresar tu edad!")
            continue
        try:
            age = int(age_str)
            if age < 0:
                print("Error! La edad no puede ser negativa oe!")
                continue
            return age
        except ValueError:
            print("Error! Ingresa tu edad real!")

#Solicita una contraseña válida y devuelve la ingresada por el usuario
def get_valid_password():
    while True:
        password = input("Ingresa y crea tu pass: ")
        if not password:
            print("Error! Debes crear una pass real o no podras ingresar!")
            continue
        if validate_password(password):
            return password
        print("Ups! Necesitas una pass fooerte. Debe tener al menos 8 caracteres, incluyendo letras y números y sin espacios!")
        
#Solicita un nombre de usuario válido y devuelve el ingresado por el usuario
def get_valid_username():
    while True:
        username = input("Ingresa tu nombre de usuario (entre 3 y 20 caracteres alfanuméricos y guiones bajos para separar): ")
        if not validate_username(username):
            print("Error! Debes ingresar tu nombre de usuario!")
            continue
        return username

#Imprimir datos de usuario que contiene el diccionario
def print_user_data(user):
    print(f"Usuario: {user['username']}")
    print(f"Pass: {'*' * len(user['password'])}")
    print(f"Edad: {user['age']}\n")

def main():
    global user_data

    while True:
        username = get_valid_username()
        if username.lower() == 'salir':
            break
        
        #Obtener contraseña del usuario
        password = get_valid_password()
        
        #Obtener edad del usuario
        user_age = get_age()

        #Almacenar los datos de usuario en el diccionario
        user_data.append({'username': username, 'password': password, 'age': user_age})

        #Imprimir datos del usuario
        print("Registrando tu usuario...")
        time.sleep(5) #Retraso 5 seg
        print_user_data(user_data[-1])

    #Mostrar todos los datos del usuario al finalizar el programa
    print("\nTodos tus datos:")
    for user in user_data:
        print_user_data(user)

if __name__ == "__main__":
    main()
