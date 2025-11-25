def fibonacci(n):
    """
    Calcula y muestra la serie de Fibonacci hasta el n-ésimo término
    
    Args:
        n (int): Número de términos de la serie a generar
        
    Returns:
        list: Lista con los n primeros números de Fibonacci
    """
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
    """Función para ejecutar desde el menú principal"""
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