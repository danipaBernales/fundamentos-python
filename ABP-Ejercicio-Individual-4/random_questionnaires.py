"""
OPCIÓN 2
    
"""

import random, time

# Lista cuestionarios disponibles
def get_available_questionnaires():
    return ["Hábitos alimenticios", "Experiencia laboral", "Actividades recreativas", "Atletismo", "Natación", "Deportes en general"]

# Muestra aleatoria de cuestionarios
def choose_questionnaires(max_questionnaires):
    available_questionnaires = get_available_questionnaires()
    return random.sample(available_questionnaires, min(len(available_questionnaires), max_questionnaires))

# Distribuye cuestionarios
def distribute_questionnaires(people, max_questionnaires):
    for person in people:
        questionnaire_count = random.randint(1, max_questionnaires)
        sent_questionnaires = choose_questionnaires(questionnaire_count)
        yield person, sent_questionnaires

# Cuestionarios que una persona debe responder
def print_questionnaires(person, questionnaires):
    print(f"\n{person}:")
    print(f"Debes responder: {len(questionnaires)}")
    for idx, questionnaire in enumerate(questionnaires, start=1):
        print(f"Cuestionario {idx}: {questionnaire}")
        time.sleep(3)

# Personas que responden los cuestionarios
def get_people_names(max_people):
    people = []
    for i in range(1, max_people + 1):
        name = input(f"Tu ID asignado {1}. Ingresa tu nombre: ")
    while len(name) <= 3:
        print(f"Tu nombre debe tener a lo menos 3 caracteres. Inténtalo nuevamente...")
        name = input(f"Tu ID asignado {1}. Ingresa tu nombre: ")
    people.append(name)

# Programa de los cuestionarios
def main():
    max_people = 7
    max_questionnaires_per_person = 5

    print("Bienvenido al sistema de distribución de cuestionarios.\n")
    print("Los cuestionarios disponibles son:", ", ".join(get_available_questionnaires()))

    try:
        people = get_people_names(max_people)
        print("\nLos cuestionarios a responder por cada persona son:")
        for person, questionnaires in distribute_questionnaires(people, max_questionnaires_per_person):
            print_questionnaires(person, questionnaires)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}. Saliendo...")

if __name__ == "__main__":
    main()
