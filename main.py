from fibonacci import ejecutar_fibonacci
from factorial import ejecutar_factorial

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
                print("\n[Primos - En desarrollo]")
                
            elif opcion == "4":
                print("\n[Números Perfectos - En desarrollo]")
                
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