__author__ = "Jasmine Trillo Álvarez"
__name__ = "reservar"

from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import QDate
from ..vistas.vreservar import Ui_JTA_Reservar

class JTA_Reservar(QWidget, Ui_JTA_Reservar):
    """
    Clase que representa la ventana de reserva para un salón.
    
    Esta clase permite al usuario realizar una reserva o actualizarla para un salón
    específico, incluyendo los campos para rellenar su información.
    """
    def __init__(self, cursor, conexion, salon_id, nombre_salon):
        """
        Inicializa la ventana de reserva con los parámetros necesarios.
        
        :param cursor: El cursor para interactuar con la base de datos.
        :param conexion: La conexión a la base de datos.
        :param salon_id: El ID del salón para la reserva.
        :param nombre_salon: El nombre del salón seleccionado.
        """
        super().__init__()
        self.setupUi(self)
        self.cursor = cursor
        self.conexion = conexion
        self.salon_id = salon_id
        self.nombre_salon_seleccionado = nombre_salon
        
        self.JTA_dateEdit_fecha.setDate(QDate.currentDate())
        self.JTA_lineEdit_jornadas.setEnabled(False)
        self.JTA_checkBox_habnecesarias.setEnabled(False)
        self.JTA_label_habnecesarias.setEnabled(False)
        self.JTA_pushButton_actualizares.setEnabled(False)
        
        query = "SELECT nombre FROM tipos_reservas"
        self.cursor.execute(query)
        tipos_reserva = self.cursor.fetchall()
        self.JTA_comboBox_tipores.addItems(tipo[0] for tipo in tipos_reserva)
        
        query = "SELECT nombre FROM tipos_cocina"
        self.cursor.execute(query)
        tipos_cocina = self.cursor.fetchall()
        self.JTA_comboBox_tipococina.addItems(tipo[0] for tipo in tipos_cocina)
        
        self.JTA_comboBox_tipores.currentIndexChanged.connect(self.JTA_reserva_cambiada)
        self.JTA_pushButton_volver.clicked.connect(self.JTA_volver)
        self.JTA_pushButton_reservar.clicked.connect(self.JTA_crear_reserva)
        self.JTA_pushButton_actualizares.clicked.connect(self.JTA_actualizar_reserva)
        self.JTA_dateEdit_fecha.dateChanged.connect(self.JTA_fecha_cambiada)
        
    def JTA_crear_reserva(self):
        """
        Crea una nueva reserva en la base de datos con los datos ingresados.
        
        Verifica que todos los campos obligatorios estén completos antes de realizar la reserva.
        Si la reserva ya existe en la fecha seleccionada, habilita el botón de actualización.
        """
        JTA_fecha = self.JTA_dateEdit_fecha.date().toString("yyyy-MM-dd")
        JTA_nombre = self.JTA_lineEdit_nombre.text()
        JTA_telefono = self.JTA_lineEdit_telefono.text()
        JTA_tipo_reserva = self.JTA_comboBox_tipores.currentText()
        JTA_tipo_cocina = self.JTA_comboBox_tipococina.currentText()
        JTA_numpersonas = self.JTA_lineEdit_numpersonas.text()
        JTA_jornadas = self.JTA_lineEdit_jornadas.text()
        JTA_jornadas = JTA_jornadas if JTA_jornadas else 0
        JTA_num_habitaciones = JTA_numpersonas
        
        if not JTA_fecha or not JTA_nombre or not JTA_telefono or not JTA_tipo_reserva or not JTA_tipo_cocina or not JTA_numpersonas:
            QMessageBox.warning(self, "Aviso", "Por favor, complete todos los campos obligatorios.")
            return
        
        if JTA_fecha == "0" or JTA_nombre == "0" or JTA_telefono == "0" or JTA_tipo_reserva == "0" or JTA_tipo_cocina == "0" or JTA_numpersonas == "0":
            QMessageBox.warning(self, "Aviso", "Por favor, complete todos los campos obligatorios.")
            return

        if JTA_tipo_reserva == "Congreso" and not JTA_jornadas:
            QMessageBox.warning(self, "Aviso", "Por favor, complete los campos de congreso.")
            return
        
        if not self.JTA_verificar_disponibilidad(JTA_fecha, self.salon_id):
            QMessageBox.warning(self, "Aviso", f"La fecha {JTA_fecha} para el salón {self.nombre_salon_seleccionado} ya está reservada. Haga click en 'Actualizar reserva' para actualizarla.")
            self.JTA_pushButton_actualizares.setEnabled(True)
        else:
            query = """INSERT INTO reservas (tipo_reserva_id, salon_id, tipo_cocina_id, persona, telefono, fecha, ocupacion, jornadas, habitaciones) 
            VALUES ((SELECT tipo_reserva_id FROM tipos_reservas WHERE nombre = %s), %s, 
                    (SELECT tipo_cocina_id FROM tipos_cocina WHERE nombre = %s), %s, %s, %s, %s, %s, %s)
                    """

            values = (JTA_tipo_reserva, self.salon_id, JTA_tipo_cocina, JTA_nombre, JTA_telefono, JTA_fecha, JTA_numpersonas, JTA_jornadas, JTA_num_habitaciones)

            try:
                self.cursor.execute(query, values)
                self.conexion.commit()
                QMessageBox.information(self, "Éxito", "Reserva creada con éxito")

                self.JTA_dateEdit_fecha.setDate(QDate.currentDate())
                self.JTA_lineEdit_nombre.clear()
                self.JTA_lineEdit_telefono.clear()
                self.JTA_lineEdit_numpersonas.clear()
                self.JTA_lineEdit_jornadas.clear()
                self.JTA_checkBox_habnecesarias.setChecked(False)
                
                self.close()

            except Exception as e:
                QMessageBox.warning(self, "Error", f"Error al crear la reserva: {str(e)}")
    
    def JTA_verificar_disponibilidad(self, fecha, salon_id):
        """
        Verifica si hay disponibilidad para la fecha y salón seleccionados.
        
        :param fecha: La fecha para la que se quiere realizar la reserva.
        :param salon_id: El ID del salón para verificar disponibilidad.
        
        :return bool: 'True' si la fecha está disponible, 'False' si ya está reservada.
        """
        query = "SELECT COUNT(*) FROM reservas WHERE fecha = %s AND salon_id = %s"
        self.cursor.execute(query, (fecha, salon_id))
        count = self.cursor.fetchone()[0]
        return count == 0
    
    def JTA_reserva_cambiada(self):
        """
        Maneja el cambio de tipo de reserva seleccionado.
        
        Habilita o deshabilita los campos correspondientes cuando se selecciona "Congreso".
        """
        JTA_tipo_reserva_actual = self.JTA_comboBox_tipores.currentText()

        if JTA_tipo_reserva_actual == "Congreso":
            self.JTA_label_jornadas.setEnabled(True)
            self.JTA_lineEdit_jornadas.setEnabled(True)
            self.JTA_label_habnecesarias.setEnabled(True)
            self.JTA_checkBox_habnecesarias.setEnabled(True)
        else:
            self.JTA_label_jornadas.setEnabled(False)
            self.JTA_lineEdit_jornadas.setEnabled(False)
            self.JTA_label_habnecesarias.setEnabled(False)
            self.JTA_checkBox_habnecesarias.setEnabled(False)
    
    def JTA_actualizar_reserva(self):
        """
        Actualiza una reserva existente en la base de datos con los nuevos datos.
        
        Actualiza la reserva si los campos son correctos y la fecha es válida.
        """
        JTA_fecha = self.JTA_dateEdit_fecha.date().toString("yyyy-MM-dd")
        JTA_nombre = self.JTA_lineEdit_nombre.text()
        JTA_telefono = self.JTA_lineEdit_telefono.text()
        JTA_tipo_reserva = self.JTA_comboBox_tipores.currentText()
        JTA_tipo_cocina = self.JTA_comboBox_tipococina.currentText()
        JTA_numpersonas = self.JTA_lineEdit_numpersonas.text()
        JTA_jornadas = self.JTA_lineEdit_jornadas.text()
        JTA_jornadas = JTA_jornadas if JTA_jornadas else 0
        JTA_num_habitaciones = JTA_numpersonas

        query = """UPDATE reservas
                SET tipo_reserva_id = (SELECT tipo_reserva_id FROM tipos_reservas WHERE nombre = %s), 
                tipo_cocina_id = (SELECT tipo_cocina_id FROM tipos_cocina WHERE nombre = %s), 
                persona = %s, telefono = %s, ocupacion = %s, jornadas = %s, habitaciones = %s 
                WHERE salon_id = %s AND fecha = %s"""

        values = (JTA_tipo_reserva, JTA_tipo_cocina, JTA_nombre, JTA_telefono, JTA_numpersonas, JTA_jornadas, JTA_num_habitaciones, self.salon_id, JTA_fecha)
        
        try:
            self.cursor.execute(query, values)
            self.conexion.commit()
            QMessageBox.information(self, "Éxito", "Reserva actualizada con éxito")

            self.JTA_dateEdit_fecha.setDate(QDate.currentDate())
            self.JTA_lineEdit_nombre.clear()
            self.JTA_lineEdit_telefono.clear()
            self.JTA_lineEdit_numpersonas.clear()
            self.JTA_lineEdit_jornadas.clear()
            self.JTA_checkBox_habnecesarias.setChecked(False)
            self.JTA_pushButton_actualizares.setEnabled(False)
            
            self.close()
            
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al actualizar la reserva: {str(e)}")
            
    def JTA_fecha_cambiada(self):
        self.JTA_pushButton_actualizares.setEnabled(False)
    
    def JTA_volver(self):
        self.JTA_dateEdit_fecha.setDate(QDate.currentDate())
        self.JTA_lineEdit_nombre.clear()
        self.JTA_lineEdit_telefono.clear()
        self.JTA_lineEdit_numpersonas.clear()
        self.JTA_lineEdit_jornadas.clear()
        self.JTA_checkBox_habnecesarias.setChecked(False)
        self.close()