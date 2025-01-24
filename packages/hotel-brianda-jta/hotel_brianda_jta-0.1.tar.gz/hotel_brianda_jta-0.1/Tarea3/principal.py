__author__ = "Jasmine Trillo Álvarez"

import sys
from PySide6.QtWidgets import QApplication
from .controladores.mostrar_reservas import JTA_MostrarReservas

class MainApp(QApplication):
    """
    Clase principal de la aplicación que hereda de QApplication.
    
    Esta clase inicializa la ventana de reservas (JTA_MostrarReservas) y la muestra cuando
    se ejecuta la aplicación.
    """
    def __init__(self, sys_argv):
        """
        Inicializa la aplicación y la ventana de reservas.
        
        :param sys_argv: Lista de argumentos de la línea de comandos.
        """
        super().__init__(sys_argv)
        self.ventana_reservas = JTA_MostrarReservas()  
        self.ventana_reservas.show()  

if __name__ == "__main__":
    """
    Punto de entrada principal de la aplicación.
    
    Crea la aplicación, instancia la ventana de reservas y ejecuta el ciclo de eventos.
    """
    app = QApplication(sys.argv)
    ventana = JTA_MostrarReservas()
    ventana.show()
    sys.exit(app.exec())