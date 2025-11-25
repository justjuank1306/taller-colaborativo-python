def fibonacci(n):
    """Calcula la serie de Fibonacci"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    serie = [0, 1]
    for i in range(2, n):
        siguiente = serie[i-1] + serie[i-2]
        serie.append(siguiente)
    return serie

def ejecutar_fibonacci():
    """Función para ejecutar desde el menú"""
    print("\n--- CÁLCULO DE FIBONACCI ---")
    try:
        n = int(input("¿Cuántos términos de Fibonacci desea calcular?: "))
        if n <= 0:
            print("❌ Por favor ingrese un número positivo.")
            return
        resultado = fibonacci(n)
        print(f"\n✅ Serie de Fibonacci con {n} términos:")
        print(resultado)
        print(f"\nÚltimo término: {resultado[-1]}")
    except ValueError:
        print("❌ Error: Debe ingresar un número entero válido.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def factorial(n):
    """Calcula el factorial de un número"""
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

def ejecutar_factorial():
    """Función para ejecutar desde el menú"""
    print("\n--- CÁLCULO DE FACTORIAL ---")
    try:
        n = int(input("Ingrese un número para calcular su factorial: "))
        if n < 0:
            print("❌ El factorial no está definido para números negativos.")
            return
        resultado = factorial(n)
        print(f"\n✅ El factorial de {n} es: {resultado}")
        if n <= 10:
            calculo = " × ".join(str(i) for i in range(1, n + 1)) if n > 0 else "1"
            print(f"Cálculo: {calculo} = {resultado}")
    except ValueError:
        print("❌ Error: Debe ingresar un número entero válido.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def es_primo(n):
    """Verifica si un número es primo"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def ejecutar_primos():
    """Función para ejecutar desde el menú"""
    print("\n--- VERIFICAR NÚMERO PRIMO ---")
    try:
        n = int(input("Ingrese un número para verificar si es primo: "))
        if n < 0:
            print("❌ Los números negativos no se consideran primos.")
            return
        if es_primo(n):
            print(f"\n✅ El número {n} ES PRIMO")
        else:
            print(f"\n❌ El número {n} NO es primo")
            if n > 1:
                for i in range(2, n):
                    if n % i == 0:
                        print(f"   (Es divisible por {i})")
                        break
    except ValueError:
        print("❌ Error: Debe ingresar un número entero válido.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def es_perfecto(n):
    """Verifica si un número es perfecto"""
    if n < 1:
        return False, []
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    suma_divisores = sum(divisores)
    return suma_divisores == n, divisores

def generar_perfectos(cantidad):
    """Genera los primeros N números perfectos"""
    perfectos = []
    numero = 1
    limite_busqueda = 10000 if cantidad <= 3 else 100000
    while len(perfectos) < cantidad and numero < limite_busqueda:
        es_perf, divisores = es_perfecto(numero)
        if es_perf:
            perfectos.append((numero, divisores))
        numero += 1
    return perfectos

def ejecutar_perfectos():
    """Función para ejecutar desde el menú"""
    print("\n--- NÚMEROS PERFECTOS ---")
    print("Nota: Los números perfectos son escasos. Esto puede tardar un momento...")
    try:
        n = int(input("\n¿Cuántos números perfectos desea generar? (Recomendado: 1-3): "))
        if n <= 0:
            print("❌ Por favor ingrese un número positivo.")
            return
        if n > 3:
            print("⚠️  Advertencia: Buscar más de 3 puede tardar mucho.")
            confirmar = input("¿Continuar? (s/n): ")
            if confirmar.lower() != 's':
                return
        print(f"\n🔍 Buscando los primeros {n} números perfectos...")
        perfectos = generar_perfectos(n)
        if len(perfectos) < n:
            print(f"\n⚠️  Solo se encontraron {len(perfectos)} números.")
        else:
            print(f"\n✅ Se encontraron {len(perfectos)} números perfectos:")
        for i, (num, divisores) in enumerate(perfectos, 1):
            print(f"\n{i}. Número perfecto: {num}")
            print(f"   Divisores: {divisores}")
            print(f"   Suma: {sum(divisores)} = {num}")
    except ValueError:
        print("❌ Error: Debe ingresar un número entero válido.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def mostrar_menu():
    """Muestra el menú principal del programa"""
    print("\n" + "="*50)
    print("   PROGRAMA DE FUNCIONES MATEMÁTICAS")
    print("="*50)
    print("1. Calcular Fibonacci")
    print("2. Calcular Factorial")
    print("3. Verificar si es Primo")
    print("4. Generar Números Perfectos")
    print("5. Salir")
    print("="*50)

def main():
    """Función principal que ejecuta el menú"""
    while True:
        mostrar_menu()
        try:
            opcion = input("\nSeleccione una opción (1-5): ")
            
            if opcion == "1":
                ejecutar_fibonacci()
            elif opcion == "2":
                ejecutar_factorial()
            elif opcion == "3":
                ejecutar_primos()
            elif opcion == "4":
                ejecutar_perfectos()
            elif opcion == "5":
                print("\n¡Gracias por usar el programa!")
                break
            else:
                print("\n❌ Opción inválida. Por favor seleccione 1-5.")
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido por el usuario!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()