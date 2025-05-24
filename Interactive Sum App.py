import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QLabel, QPushButton)
from PySide6.QtCore import QTimer, Qt

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interactive Sum App")
        self.setGeometry(100, 100, 400, 200)

        self.suma = 0


        # Widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Aplicar estilo Aero al widget central
        central_widget.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #E1E1E1, stop:1 #D3D3D3);
                border-radius: 10px;
            }
            QLabel {
                color: #333;
                padding: 5px;
                border: 1px solid #BBB;
                border-radius: 5px;
                background-color: rgba(255, 255, 255, 150);
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #F6F7FA, stop:1 #E8EBF2);
                border: 1px solid #D4D7DE;
                border-radius: 5px;
                padding: 5px 15px;
                color: #333;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #E8EBF2, stop:1 #D4D7DE);
            }
            QPushButton:pressed {
                background: #D4D7DE;
            }
            QPushButton:disabled {
                background: #F0F0F0;
                border-color: #CCC;
                color: #999;
            }
        """)

        # Layout principal
        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Etiqueta para mostrar la suma
        self.etiqueta_suma = QLabel(f"Numero: {self.suma}")
        self.etiqueta_suma.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.etiqueta_suma.setStyleSheet("font-size: 16pt; font-weight: bold;")
        main_layout.addWidget(self.etiqueta_suma, 0)

        # Frame para los botones (usando QWidget y QHBoxLayout)
        button_widget = QWidget()
        button_layout = QHBoxLayout(button_widget)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(button_widget, 0)


        # Botón Suma 1
        self.boton_suma_uno = QPushButton("Suma 1")
        self.boton_suma_uno.clicked.connect(self.sumar_uno)
        button_layout.addWidget(self.boton_suma_uno)

        # Botón Auto Suma
        self.boton_auto_suma = QPushButton("Auto Suma")
        self.boton_auto_suma.clicked.connect(self.iniciar_auto_suma)
        button_layout.addWidget(self.boton_auto_suma)

        # Botón Parar
        self.boton_parar = QPushButton("Parar")
        self.boton_parar.clicked.connect(self.parar_auto_suma)
        self.boton_parar.setEnabled(False) # Equivalent to state=tk.DISABLED
        button_layout.addWidget(self.boton_parar)

        # Botón Reiniciar
        self.boton_reiniciar = QPushButton("Reiniciar")
        self.boton_reiniciar.clicked.connect(self.reiniciar_suma)
        button_layout.addWidget(self.boton_reiniciar)

        # Botón Boom
        self.boton_boom = QPushButton("Boom")
        self.boton_boom.clicked.connect(self.boom_suma)
        button_layout.addWidget(self.boton_boom)

        # Temporizador para auto suma
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.auto_sumar)

    def sumar_uno(self):
        self.suma += 1
        self.etiqueta_suma.setText(f"Suma: {self.suma}")

    def iniciar_auto_suma(self):
        if not self.timer.isActive():
            self.timer.start(1) # Llama a auto_sumar cada 1 ms
            self.boton_auto_suma.setEnabled(False)
            self.boton_parar.setEnabled(True)
            self.boton_boom.setEnabled(False)

    def auto_sumar(self):
        self.sumar_uno()

    def parar_auto_suma(self):
        if self.timer.isActive():
            self.timer.stop()
            self.boton_auto_suma.setEnabled(True)
            self.boton_parar.setEnabled(False)
            self.boton_boom.setEnabled(True)

    def reiniciar_suma(self):
        if self.timer.isActive():
             self.timer.stop()
        self.suma = 0
        self.etiqueta_suma.setText(f"Suma: {self.suma}")
        self.boton_auto_suma.setEnabled(True)
        self.boton_parar.setEnabled(False)
        self.boton_boom.setEnabled(True)

    def boom_suma(self):
        if self.timer.isActive():
            self.timer.stop()
        self.etiqueta_suma.setText("∞")
        self.boton_auto_suma.setEnabled(False)
        self.boton_parar.setEnabled(False)
        self.boton_boom.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())