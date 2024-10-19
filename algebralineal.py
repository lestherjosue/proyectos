import sys
import numpy as np
import ast
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QComboBox
import matplotlib.pyplot as plt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Operaciones con Matrices y Sistemas de Ecuaciones")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.inversa_btn = QPushButton("Encontrar la Inversa de una Matriz", self)
        self.inversa_btn.setFixedHeight(50)
        self.inversa_btn.clicked.connect(self.abrirInversa)
        layout.addWidget(self.inversa_btn)

        self.multiplicacion_btn = QPushButton("Multiplicación de Matrices", self)
        self.multiplicacion_btn.setFixedHeight(50)
        self.multiplicacion_btn.clicked.connect(self.abrirMultiplicacion)
        layout.addWidget(self.multiplicacion_btn)

        self.sistemas_btn = QPushButton("Resolver Sistemas de Ecuaciones", self)
        self.sistemas_btn.setFixedHeight(50)
        self.sistemas_btn.clicked.connect(self.abrirSistemas)
        layout.addWidget(self.sistemas_btn)

        self.setLayout(layout)

    def abrirInversa(self):
        self.inversa_window = InversaWindow()
        self.inversa_window.show()

    def abrirMultiplicacion(self):
        self.multiplicacion_window = MultiplicacionWindow()
        self.multiplicacion_window.show()

    def abrirSistemas(self):
        self.sistemas_window = SistemasWindow()
        self.sistemas_window.show()

class InversaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Inversa de una Matriz")
        layout = QVBoxLayout()

        self.label = QLabel("Introduce la matriz (ejemplo: [[1, 2], [3, 4]]):")
        layout.addWidget(self.label)

        self.matriz_input = QLineEdit(self)
        layout.addWidget(self.matriz_input)

        self.result_btn = QPushButton("Calcular Inversa", self)
        self.result_btn.clicked.connect(self.calcularInversa)
        layout.addWidget(self.result_btn)

        self.result_label = QLabel("Resultado:")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calcularInversa(self):
        try:
            matriz = np.array(ast.literal_eval(self.matriz_input.text()))
            inversa = np.linalg.inv(matriz)
            self.result_label.setText(f"Inversa: \n{inversa}")
        except np.linalg.LinAlgError:
            self.result_label.setText("La matriz no tiene inversa.")
        except Exception as e:
            self.result_label.setText(f"Error: {str(e)}")

class MultiplicacionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Multiplicación de Matrices")
        layout = QVBoxLayout()

        self.label1 = QLabel("Introduce la primera matriz (ejemplo: [[1, 2], [3, 4]]):")
        layout.addWidget(self.label1)

        self.matriz1_input = QLineEdit(self)
        layout.addWidget(self.matriz1_input)

        self.label2 = QLabel("Introduce la segunda matriz (ejemplo: [[5, 6], [7, 8]]):")
        layout.addWidget(self.label2)

        self.matriz2_input = QLineEdit(self)
        layout.addWidget(self.matriz2_input)

        self.result_btn = QPushButton("Multiplicar", self)
        self.result_btn.clicked.connect(self.multiplicarMatrices)
        layout.addWidget(self.result_btn)

        self.result_label = QLabel("Resultado:")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def multiplicarMatrices(self):
        try:
            matriz1 = np.array(ast.literal_eval(self.matriz1_input.text()))
            matriz2 = np.array(ast.literal_eval(self.matriz2_input.text()))
            producto = np.dot(matriz1, matriz2)
            self.result_label.setText(f"Producto: \n{producto}")
        except ValueError:
            self.result_label.setText("Error: Las matrices deben ser compatibles para la multiplicación.")
        except Exception as e:
            self.result_label.setText(f"Error: {str(e)}")

class SistemasWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Resolver Sistemas de Ecuaciones")
        layout = QVBoxLayout()

        self.label = QLabel("Selecciona el método:")
        layout.addWidget(self.label)

        self.metodo_combo = QComboBox(self)
        self.metodo_combo.addItem("Gauss-Jordan")
        self.metodo_combo.addItem("Regla de Cramer")
        layout.addWidget(self.metodo_combo)

        self.matriz_label = QLabel("Matriz de coeficientes (ejemplo: [[2, 1], [1, 2]]):")
        layout.addWidget(self.matriz_label)

        self.matriz_input = QLineEdit(self)
        layout.addWidget(self.matriz_input)

        self.vector_label = QLabel("Vector de términos independientes (ejemplo: [5, 5]):")
        layout.addWidget(self.vector_label)

        self.vector_input = QLineEdit(self)
        layout.addWidget(self.vector_input)

        self.result_btn = QPushButton("Resolver", self)
        self.result_btn.clicked.connect(self.resolverSistema)
        layout.addWidget(self.result_btn)

        self.result_label = QLabel("Resultado:")
        layout.addWidget(self.result_label)

        self.graficar_btn = QPushButton("Graficar", self)
        self.graficar_btn.clicked.connect(self.graficarSistema)
        layout.addWidget(self.graficar_btn)

        self.setLayout(layout)

    def resolverSistema(self):
        metodo = self.metodo_combo.currentText()
        try:
            matriz = np.array(ast.literal_eval(self.matriz_input.text()))
            vector = np.array(ast.literal_eval(self.vector_input.text()))

            if metodo == "Gauss-Jordan":
                self.result_label.setText(self.resolverGaussJordan(matriz, vector))
            elif metodo == "Regla de Cramer":
                self.result_label.setText(self.resolverCramer(matriz, vector))
        except ValueError as ve:
            self.result_label.setText(f"Error en los valores: {str(ve)}")
        except Exception as e:
            self.result_label.setText(f"Error en la entrada: {str(e)}")

    def resolverGaussJordan(self, A, b):
        try:
            augmented_matrix = np.column_stack((A, b))
            n = len(b)
            for i in range(n):
                augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i][i]
                for j in range(n):
                    if i != j:
                        augmented_matrix[j] = augmented_matrix[j] - augmented_matrix[j][i] * augmented_matrix[i]
            return f"Solución: {augmented_matrix[:, -1]}"
        except Exception as e:
            return f"Error: {str(e)}"

    def resolverCramer(self, A, b):
        try:
            det_A = np.linalg.det(A)
            if det_A == 0:
                return "El sistema no tiene solución única."
            n = len(b)
            soluciones = []
            for i in range(n):
                Ai = A.copy()
                Ai[:, i] = b
                soluciones.append(np.linalg.det(Ai) / det_A)
            return f"Solución: {soluciones}"
        except Exception as e:
            return f"Error: {str(e)}"

    def graficarSistema(self):
        try:    
            A = np.array(ast.literal_eval(self.matriz_input.text()))
            b = np.array(ast.literal_eval(self.vector_input.text()))

            if A.shape[0] == 2 and A.shape[1] == 2 and b.shape[0] == 2:  # 2x2
                x_vals = np.linspace(-10, 10, 400)
                y1_vals = (b[0] - A[0, 0] * x_vals) / A[0, 1]
                y2_vals = (b[1] - A[1, 0] * x_vals) / A[1, 1]

                plt.figure()
                plt.plot(x_vals, y1_vals, label="Ecuación 1")
                plt.plot(x_vals, y2_vals, label="Ecuación 2")
                plt.axhline(0, color='black', linewidth=0.5)
                plt.axvline(0, color='black', linewidth=0.5)
                plt.grid()
                plt.legend()
                plt.title("Gráfica de Sistema de Ecuaciones 2x2")
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.show()

            else:
                self.result_label.setText("El sistema debe ser 2x2 para graficarlo.")

        except Exception as e:
            self.result_label.setText(f"Error en la entrada o en la ejecución: {str(e)}")
            print(f"Detalle del error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())