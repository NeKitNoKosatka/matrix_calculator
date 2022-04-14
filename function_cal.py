import numpy as np          # import modules
# import numpy.random as rand
from PySide6.QtWidgets import *

"""
Addition function
"""


def sum(matrices):
    global matrix_3
    try:
            matrix_3 = matrices[0] + matrices[1]
            # print(matrix_3)
    except TypeError:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("The matrix cells must be filled with numbers")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
    except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("The matrix cells must be filled with numbers")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
    return matrix_3


"""
Subtraction function
"""


def sub(matrices):
    global matrix_3
    try:
        matrix_3 = matrices[0] - matrices[1]
        # print(matrix_3)
    except TypeError:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("The matrix cells must be filled with numbers")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    except ValueError:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("The matrix cells must be filled with numbers")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    return matrix_3


"""
Multiplying function
"""


def multiply(matrices):
    global matrix_3
    try:
        matrix_3 = np.dot(matrices[0], matrices[1])
        # print(matrix_3)
    except TypeError:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("The matrix cells must be filled with numbers")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    except ValueError:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("The matrix cells must be filled with numbers")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    return matrix_3


"""
Dividing function
"""


def divide(matrices):
    global matrix_3
    try:
        matrix_3 = np.round(matrices[0] / matrices[1], 3)
        # print(matrix_3)
    except TypeError:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("The matrix cells must be filled with numbers")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    except ValueError:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("The matrix cells must be filled with numbers")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    return matrix_3


"""
Transpose function
"""


def transpose(matrices):
    global matrix_t
    try:
        matrix_t = matrices[0].transpose()
        # print(matrix_t)
    except AttributeError:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("The matrix cells must be filled with numbers")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    except TypeError:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("The matrix cells must be filled with numbers")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    except ValueError:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("The matrix cells must be filled with numbers")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    return matrix_t


"""
Find the determinant function
"""


def det(matrices):
    try:
        matrix_d = np.linalg.det(matrices[0])
        msg = QMessageBox()
        msg.setWindowTitle("Deterninant")
        text_message = "Determinant is " + str(int(np.rint(matrix_d)))
        msg.setText(text_message)
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        # print(int(np.rint(matrix_d)))
    except np.linalg.LinAlgError:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("The matrix cells must be filled with numbers")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    except TypeError:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("The matrix cells must be filled with numbers")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    except ValueError:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("The matrix cells must be filled with numbers")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    # return int(np.rint(matrix_d))


"""
Inverse function
"""


def inverse(matrices):
    global matrix_i
    try:
        matrix_i = np.round(np.linalg.inv(matrices[0]), 2)
        # print(matrix_i)
    except TypeError:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("The matrix cells must be filled with numbers")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    except ValueError:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("The matrix cells must be filled with numbers")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    except np.linalg.LinAlgError:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("The determinant is zero. There is no inverse matrix.")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    return matrix_i


"""
Multiplying on number function
"""


def multiply_on(matrix, number):
    global matrix_3
    try:
        matrix_3 = np.round(matrix * number, 3)
        # print(matrix_3)
    except TypeError:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("The matrix cells must be filled with numbers")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    except ValueError:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("The matrix cells must be filled with numbers")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    return matrix_3


"""
matrix_1 = rand.random_integers(0, 9, (3, 3))   # creating a matrix
print(matrix_1, "\n")
matrix_2 = rand.random_integers(0, 9, (3, 3))
print(matrix_2, "\n")

print("Addition function")
print(sum(matrix_1, matrix_2), "\n")
print("Subtraction function")
print(sub(matrix_1, matrix_2), "\n")
print("Multiplying function")
print(multiply(matrix_1, matrix_2), "\n")
print("Dividing function ")
print(divide(matrix_1, matrix_2), "\n")
print("Transpose function ")
print(transpose(matrix_1), "\n")
print("Inverse function ")
print(inverse(matrix_1), "\n")
print("Find the determinant function ")
print(det(matrix_1), "\n")
"""
