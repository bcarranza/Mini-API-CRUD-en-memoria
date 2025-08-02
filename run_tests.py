#!/usr/bin/env python3
"""
Script para ejecutar las pruebas de la Mini API CRUD
"""

import subprocess
import sys

def run_tests():
    """Ejecutar las pruebas con pytest"""
    try:
        print("🧪 Ejecutando pruebas de la Mini API CRUD...")
        print("=" * 50)
        
        # Ejecutar pytest con verbose
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "test_main.py", 
            "-v", 
            "--tb=short"
        ], capture_output=True, text=True)
        
        print(result.stdout)
        
        if result.stderr:
            print("Errores:")
            print(result.stderr)
        
        if result.returncode == 0:
            print("✅ Todas las pruebas pasaron exitosamente!")
        else:
            print("❌ Algunas pruebas fallaron.")
            
        return result.returncode
        
    except Exception as e:
        print(f"❌ Error ejecutando las pruebas: {e}")
        return 1

if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code) 