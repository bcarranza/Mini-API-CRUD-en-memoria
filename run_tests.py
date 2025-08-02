#!/usr/bin/env python3
"""
Script para ejecutar tests de la Mini API CRUD
Permite ejecutar diferentes tipos de tests de forma sencilla
"""

import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Ejecuta un comando y muestra el resultado"""
    print(f"\n{'='*50}")
    print(f"🚀 {description}")
    print(f"{'='*50}")
    print(f"Comando: {command}")
    print("-" * 50)
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("✅ Éxito!")
        if result.stdout:
            print("Salida:")
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("❌ Error!")
        if e.stdout:
            print("Salida estándar:")
            print(e.stdout)
        if e.stderr:
            print("Error:")
            print(e.stderr)
        return False

def main():
    """Función principal del script"""
    print("🧪 Ejecutor de Tests - Mini API CRUD")
    print("=" * 40)
    
    # Verificar que estamos en el directorio correcto
    if not Path("app/test").exists():
        print("❌ Error: No se encontró el directorio de tests")
        print("Asegúrate de ejecutar este script desde la raíz del proyecto")
        sys.exit(1)
    
    # Opciones de ejecución
    options = {
        "1": ("Tests básicos", "pytest app/test/test_main.py -v"),
        "2": ("Tests avanzados", "pytest app/test/test_advanced.py -v"),
        "3": ("Todos los tests", "pytest app/test/ -v"),
        "4": ("Tests con cobertura", "pytest app/test/ --cov=app --cov-report=term-missing"),
        "5": ("Tests con reporte HTML", "pytest app/test/ --cov=app --cov-report=html"),
        "6": ("Tests con más detalle", "pytest app/test/ -v -s"),
    }
    
    # Mostrar opciones
    print("\nOpciones disponibles:")
    for key, (description, _) in options.items():
        print(f"  {key}. {description}")
    
    print("\n0. Salir")
    
    # Obtener selección del usuario
    while True:
        try:
            choice = input("\nSelecciona una opción (0-6): ").strip()
            
            if choice == "0":
                print("👋 ¡Hasta luego!")
                break
            
            if choice in options:
                description, command = options[choice]
                success = run_command(command, description)
                
                if success:
                    print(f"\n✅ {description} completados exitosamente!")
                else:
                    print(f"\n❌ {description} fallaron!")
                
                # Preguntar si quiere continuar
                continue_choice = input("\n¿Ejecutar otro test? (s/n): ").strip().lower()
                if continue_choice not in ['s', 'si', 'sí', 'y', 'yes']:
                    print("👋 ¡Hasta luego!")
                    break
            else:
                print("❌ Opción inválida. Por favor selecciona un número del 0 al 6.")
                
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main() 