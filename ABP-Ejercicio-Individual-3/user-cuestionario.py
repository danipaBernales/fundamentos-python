def obtener_cuestionarios(edad, afinidad_deportes, latinoamerica):
    cuestionarios = []

    if latinoamerica:
        cuestionarios.append("habitos alimenticios")

        if 18 <= edad <= 29:
            cuestionarios.append("empleabilidad")
        elif 30 <= edad <= 59:
            cuestionarios.append("experiencia laboral")
        elif edad >= 60:
            cuestionarios.append("actividades recreativas")

        if afinidad_deportes.lower() == "si" and edad < 60:
            cuestionarios.append("atletismo")
        elif afinidad_deportes.lower() == "si" and edad >= 60:
            cuestionarios.append("natación")
        elif afinidad_deportes.lower() == "no":
            cuestionarios.append("Deportes en General")
    else:
        if 18 <= edad <= 29:
            cuestionarios.append("empleabilidad")

        if afinidad_deportes.lower() == "si" and edad < 60:
            cuestionarios.append("atletismo")
        elif afinidad_deportes.lower() == "si" and edad >= 60:
            cuestionarios.append("natación")
        elif afinidad_deportes.lower() == "no":
            cuestionarios.append("Deportes en General")

    return cuestionarios

def obtener_edad():
    while True:
        edad = input("Ingresa tu edad: ")
        if edad.isdigit():
            return int(edad)
        else:
            print("Ingresa una edad legible por favor :)")

def obtener_respuesta_afinidad_deportes():
    while True:
        respuesta = input("¿Te gusta el deporte y sientes afinidad por ellos? (Responde si o no): ").lower()
        if respuesta in ["si", "no"]:
            return respuesta
        else:
            print("Por favor responde con un SI o con un NO para que seas parte de nuestra Tribu")

def main():
    print("Hola! Este programa determina los cuestionarios que debes responder si quieres formar parte de nuestra Tribu y convertirte en un loquillo internacional!!!")

    latinoamerica = input("¿Eres latinoamericano? Porfa responde si o no: ").lower() == "si"
    edad = obtener_edad()
    afinidad_deportes = obtener_respuesta_afinidad_deportes()

    cuestionarios = obtener_cuestionarios(edad, afinidad_deportes, latinoamerica)

    print("¿Quieres ser parte de nuestra Tribu? Porque estos son los cuestionarios que debes responder: ")
    for cuestionario in cuestionarios:
        cantidad_cuestionarios = len(cuestionarios)
        print(f"- {cuestionario}")
        print(f"Es decir, debes responder solo {cantidad_cuestionarios}")

if __name__ == "__main__":
    main()
