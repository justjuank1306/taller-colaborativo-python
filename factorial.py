def factorial(n):
    """
    Calcula el factorial de un número
    
    Args:
        n (int): Número para calcular el factorial
        
    Returns:
        int: Factorial de n
    """
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
    """Función para ejecutar desde el menú principal"""
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