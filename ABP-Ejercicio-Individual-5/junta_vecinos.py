import datetime

#Lista para guardar los diccionarios de usuarios
jjvv = []

#Valida ingreso de usuario
def validate_input(prompt, validator, error_message):
    while True:
        user_input = input(prompt).strip()  #Elimina espacios en blanco al principio y al final
        if user_input and validator(user_input):
            return user_input
        else:
            print(error_message)

#Valida nombre de usuario
def validate_username(username):
    return len(username) > 0 and not any(char.isdigit() for char in username)

#Valida edad de usuario
def validate_age(age_str):
    try:
        age = int(age_str)
        return age >= 0
    except ValueError:
        return False

#Valida genero del usuario
def validate_gender(gender):
    return gender.lower() in ['hombre', 'mujer']

#Agregar nuevo usuario
def add_user():
    print("Ingresa la información del usuario por favor: ")
    username = validate_input("Ingresa el nombre del usuario: ", validate_username, "Nombre de usuario inválido. El nombre de usuario no puede estar vacío ni contener números.")
    age = validate_input("Ingresa la edad: ", validate_age, "Edad inválida. Ingresa una edad real por favor.")
    gender = validate_input("Ingresa el género, puede ser Hombre o Mujer: ", validate_gender, "Género inválido. Por favor ingresa 'Hombre' o 'Mujer'.")
    #Agregar caracteristicas
    user_data = {
        'nombre_usuario': username,
        'edad': int(age),
        'género': gender,
        'id_unico': len(jjvv) + 1, 
        'antigüedad': 0,
        'fecha_incorporación': datetime.datetime.now().strftime("%Y-%m-%d")  #  Fecha actual
    }
    jjvv.append(user_data)
    print("Usuario ingresado exitosamente. Regresas al Menu.")

#Mostrar datos de usuario
def print_users():
    for user in jjvv:
        print("Informacion del usuario:")
        print("Nombre de usuario:", user['nombre_usuario'])
        print("Edad:", user['edad'])
        print("Género:", user['género'])
        print("ID Único:", user['id_unico'])
        print("Antigüedad:", str(user['antigüedad']) + " años de antigüedad. Usuario recientemente registrado.")
        print("Fecha de incorporación:", user['fecha_incorporación'])
        print()

#Editar usuario
def edit_user():
    print_users()
    if not jjvv:
        print("No hay usuarios registrados para editar.")
        return

    user_id = input("Ingresa el ID del usuario que deseas editar: ")
    if not user_id.isdigit():
        print("ID inválido. Ingresa un ID válido por favor.")
        return
    user_id = int(user_id)
    if 1 <= user_id <= len(jjvv):
        user = jjvv[user_id - 1]
        print("Editando usuario: ", user['nombre_usuario'])
        age = validate_input("Ingresa nueva edad: ", validate_age, "Edad inválida. Ingresa una edad real por favor.")
        gender = validate_input("Ingresa el nuevo género, puede ser Hombre o Mujer: ", validate_gender, "Género inválido. Por favor ingresa 'Hombre' o 'Mujer'.")
        user['edad'] = int(age)
        user['género'] = gender
        print("Usuario editado exitosamente!")
    else:
        print("ID de usuario invalido.")

#Eliminar usuario
def delete_user():
    print_users()
    user_id = int(input("Ingresa el ID del usuario que deseas eliminar: "))
    if 1 <= user_id <= len(jjvv):
        deleted_user = jjvv.pop(user_id - 1)
        print("Eliminaste el usuario: ", deleted_user['nombre_usuario'])
        print("Usuario eliminado exitosamente!")
    else:
        print("Usuario invalido")

#Guardar datos de usuario en un archivo
def save_users_to_file():
    with open('usuarios.txt', 'w') as f:
        for user in jjvv:
            f.write(f"{user['nombre_usuario']},{user['edad']},{user['género']},{user['id_unico']},{user['antigüedad']},{user['fecha_incorporación']}\n")

#Cargar datos de usuario desde un archivo
def load_users_from_file():
    with open('usuarios.txt') as f:
        for line in f:
            username, age, gender, id_unico, antiguedad, fecha_incorporacion = line.strip().split(',')
            user_data = {
                'nombre_usuario': username,
                'edad': int(age),
                'género': gender,
                'id_unico': int(id_unico),
                'antigüedad': int(antiguedad),
                'fecha_incorporación': fecha_incorporacion
            }
            jjvv.append(user_data)
    print("Datos de usuario cargados exitosamente desde el archivo.")

#Menu para interactuar
def main():
    load_users_from_file()
    while True:
        print("\nMenu:")
        print("1. Agregar usuario")
        print("2. Editar un usuario registrado")
        print("3. Eliminar un usuario registrado")
        print("4. Mostrar detalles de todos los usuarios registrados")
        print("5. Guardar usuarios en un archivo")
        print("6. Salir")
        choice = input("Ingresa una opcion del 1 al 6: ")
        if choice == '1':
            add_user()
        elif choice == '2':
            edit_user()
        elif choice == '3':
            delete_user()
        elif choice == '4':
            print_users()
        elif choice == '5':
            save_users_to_file()
            print("Datos de usuario guardados exitosamente...")
        elif choice == '6':
            break
        else:
            print("Seleccion invalida. Por favor ingresa un numero del 1 al 6 segun la opcion del Menu")

if __name__ == "__main__":
    main()
