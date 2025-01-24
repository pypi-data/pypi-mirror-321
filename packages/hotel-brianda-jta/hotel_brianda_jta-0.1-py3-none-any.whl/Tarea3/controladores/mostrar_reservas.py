__author__ = "Jasmine Trillo Álvarez"
__name__ = "mostrar_reservas"

from PySide6.QtWidgets import QListWidgetItem, QMainWindow, QTableWidgetItem
from ..vistas.vmostrar_reservas import Ui_JTA_MostrarReservas
from ..controladores import reservar, mysql

class JTA_MostrarReservas(QMainWindow, Ui_JTA_MostrarReservas):
    """
    Clase que gestiona la ventana principal para mostrar y gestionar reservas de salones.

    Hereda de QMainWindow y de la clase generada por Qt Designer (Ui_JTA_MostrarReservas).
    Proporciona la funcionalidad para cargar los salones, mostrar las reservas asociadas
    y gestionar la apertura de la ventana de reservas.
    """
    
    def __init__(self):
        """
        Inicializa la ventana principal, configurando los componentes de la interfaz
        y deshabilitando inicialmente los botones de acción.
        """
        super().__init__()
        self.setupUi(self)

        self.JTA_pushButton_res.setEnabled(False)
        self.JTA_pushButton_refr.setEnabled(False)
        self.JTA_cargar_salones()

    def JTA_cargar_salones(self):
        """
        Carga la lista de salones desde la base de datos y los muestra en el QListWidget.

        También conecta los eventos necesarios para la interacción con los salones.
        """
        self.conexion, self.cursor = mysql.conectar()
        query = "SELECT nombre FROM salones"
        self.cursor.execute(query)
        salones = self.cursor.fetchall()

        for salon in salones:
            nombre_salon = salon[0]
            item = QListWidgetItem(nombre_salon)
            self.JTA_listWidget_salones.addItem(item)

        self.JTA_listWidget_salones.itemClicked.connect(self.JTA_cargar_reservas)
        self.JTA_pushButton_refr.clicked.connect(self.JTA_actualizar_reservas)

    def JTA_cargar_reservas(self, index):
        """
        Carga y muestra las reservas asociadas al salón seleccionado.

        :param idex: Elemento seleccionado en el QListWidget (nombre del salón).
        """
        self.JTA_pushButton_res.setEnabled(True)  
        self.JTA_pushButton_refr.setEnabled(True)
        self.JTA_tableWidget_res.setRowCount(0) 
        nombre_salon = index.text() 

        query_salon = "SELECT salon_id FROM salones WHERE nombre = %s"
        self.cursor.execute(query_salon, (nombre_salon,))
        salon_id = self.cursor.fetchone()[0]

        query = """SELECT r.fecha, r.persona, r.telefono, tr.nombre AS evento 
                FROM reservas r 
                JOIN tipos_reservas tr ON r.tipo_reserva_id = tr.tipo_reserva_id 
                WHERE r.salon_id = %s 
                ORDER BY r.fecha ASC
                """
        self.cursor.execute(query, (salon_id,))
        reservas = self.cursor.fetchall()

        num_columnas = len(reservas[0]) if reservas else 0
        self.JTA_tableWidget_res.setColumnCount(num_columnas)

        JTA_nombres_columnas = ["Fecha", "Persona", "Teléfono", "Evento"]
        self.JTA_tableWidget_res.setHorizontalHeaderLabels(JTA_nombres_columnas)

        self.ventana_reservar = reservar.JTA_Reservar(cursor=self.cursor, conexion=self.conexion, salon_id=salon_id, nombre_salon=nombre_salon)
        self.JTA_pushButton_res.clicked.connect(self.JTA_abrir_ventana_reservar)

        for reserva in reservas:
            rowPosition = self.JTA_tableWidget_res.rowCount()
            self.JTA_tableWidget_res.insertRow(rowPosition)
            fecha, persona, telefono, evento = reserva
            self.JTA_tableWidget_res.setItem(rowPosition, 0, QTableWidgetItem(str(fecha)))
            self.JTA_tableWidget_res.setItem(rowPosition, 1, QTableWidgetItem(str(persona)))
            self.JTA_tableWidget_res.setItem(rowPosition, 2, QTableWidgetItem(str(telefono)))
            self.JTA_tableWidget_res.setItem(rowPosition, 3, QTableWidgetItem(str(evento)))

            for i in range(num_columnas):
                self.JTA_tableWidget_res.setColumnWidth(i, self.JTA_tableWidget_res.width() // num_columnas)

    def JTA_actualizar_reservas(self):
        """
        Actualiza la tabla de reservas para el salón seleccionado.

        Si no hay un salón seleccionado, no realiza ninguna acción.
        """
        selected_item = self.JTA_listWidget_salones.currentItem()
        if selected_item:
            self.JTA_cargar_reservas(selected_item)
            
    def JTA_abrir_ventana_reservar(self):
        """
        Abre la ventana para realizar una nueva reserva en el salón seleccionado.
        """
        self.ventana_reservar.show()