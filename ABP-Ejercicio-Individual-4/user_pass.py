"""
OPCIÓN 1
    
"""
    
# Genera un mensaje indicando los criterios necesarios para una contraseña válida.
def criterios_requeridos():
    mensaje = "Hola! La contraseña que ingreses debe cumplir con los siguientes criterios:\n"
    mensaje += "- Debe tener al menos 8 caracteres.\n"
    mensaje += "- Contar con al menos una letra minúscula.\n"
    mensaje += "- Al menos una letra mayúscula.\n"
    mensaje += "- A lo menos un dígito."
    return mensaje

#Valida la contraseña según los criterios necesarios
def validar_password(password):
    # Longitud de contraseña
    if len(password) < 8:
        return False
    
    # Criterios de validación
    criterios = [
        any(char.islower() for char in password),  # Al menos una minúscula
        any(char.isupper() for char in password),  # Al menos una mayúscula
        any(char.isdigit() for char in password)   # Al menos un dígito
    ]
    
    # Verifica si se cumple con todos los criterios
    return all(criterios)

# Mostrar los criterios requeridos
print(criterios_requeridos())

# Ingreso de usuario y verificación de contraseña
while True:
    contrasena = input("Ingresa tu contraseña: ")
    if validar_password(contrasena):
        print("La contraseña es válida.")
        break
    else:
        print("La contraseña no cumple con los criterios necesarios. Intentalo nuevamente.")