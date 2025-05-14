class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        if 0 <= nota <= 100:
            self.notas.append(nota)

    def obtener_aprobadas(self):
        return [nota for nota in self.notas if nota >= 65]

    def obtener_no_aprobadas(self):
        return [nota for nota in self.notas if nota < 65]


class Curso:
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def promedio_grupal(self):
        total = sum(nota for alumno in self.alumnos for nota in alumno.notas)
        cantidad = sum(len(alumno.notas) for alumno in self.alumnos)
        return total / cantidad if cantidad > 0 else 0

    def mostrar_aprobadas(self):
        print("\nNotas aprobadas por alumno:")
        for alumno in self.alumnos:
            aprobadas = alumno.obtener_aprobadas()
            resultado = aprobadas if aprobadas else 'Ninguna nota aprobada'
            print(f"{alumno.nombre}: {resultado}")

    def mostrar_no_aprobadas(self):
        print("\nNotas NO aprobadas por alumno:")
        for alumno in self.alumnos:
            no_aprobadas = alumno.obtener_no_aprobadas()
            resultado = no_aprobadas if no_aprobadas else 'Todas las notas están aprobadas'
            print(f"{alumno.nombre}: {resultado}")

    def mostrar_promedio(self):
        promedio = self.promedio_grupal()
        print(f"\nEl promedio de notas del grupo es: {promedio:.2f}")


def solicitar_nombre(indice):
    while True:
        nombre = input(f"Ingrese el nombre del alumno #{indice + 1}: ").strip()
        if nombre:
            return nombre
        print("El nombre no puede estar vacío.")


def solicitar_nota(indice_alumno, indice_nota):
    while True:
        try:
            nota = float(input(f"Ingrese la nota #{indice_nota + 1} para el alumno #{indice_alumno + 1}: "))
            if 0 <= nota <= 100:
                return nota
            else:
                print("La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


def main():
    curso = Curso()

    for i in range(10):
        nombre = solicitar_nombre(i)
        alumno = Alumno(nombre)

        for j in range(10):
            nota = solicitar_nota(i, j)
            alumno.agregar_nota(nota)

        curso.agregar_alumno(alumno)

    while True:
        print("\nMenú de opciones:")
        print("1) Mostrar nombre y notas aprobadas para cada alumno.")
        print("2) Mostrar nombre y notas no aprobadas para cada alumno.")
        print("3) Mostrar el promedio de notas del grupo.")
        print("4) Salir del programa.")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            curso.mostrar_aprobadas()
        elif opcion == "2":
            curso.mostrar_no_aprobadas()
        elif opcion == "3":
            curso.mostrar_promedio()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
