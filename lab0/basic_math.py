import numpy as np
import scipy as sc
from scipy.optimize import minimize_scalar
from scipy.stats import skew as scipy_skew
from scipy.stats import kurtosis as scipy_kurtosis


def matrix_multiplication(matrix_a, matrix_b):
    """
    Задание 1. Функция для перемножения матриц с помощью списков и циклов.
    Вернуть нужно матрицу в формате списка.
    """
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Число столбцов первой матрицы должно быть равно числу строк второй матрицы.")

    # Размерность результата
    result_rows = len(matrix_a)
    result_cols = len(matrix_b[0])

    result = [[0 for _ in range(result_cols)] for _ in range(result_rows)] # 0 матрица

    for i in range(result_rows):
        for k in range(result_cols):
            for j in range(len(matrix_b)):
                result[i][k] += matrix_a[i][j] * matrix_b[j][k]
    
    return result


def functions(a_1, a_2):
    """
    Задание 2. На вход поступает две строки, содержащие коэффициенты двух функций.
    Необходимо найти точки экстремума функции и определить, есть ли у функций общие решения.
    Вернуть нужно координаты найденных решения списком, если они есть. None, если их бесконечно много.
    """
    result = []
    a_1 = np.array(list(map(float, str(a_1).split())))
    a_2 = np.array(list(map(float, str(a_2).split())))

    coeffs_diff = a_1 - a_2

    first, second, third = coeffs_diff[0], coeffs_diff[1], coeffs_diff[2]

    temp = None

    def f(root, coeffs):
        val = np.polyval(coeffs, root)
        return val

    if np.isclose(first, 0):
        if np.isclose(second, 0):
            if np.isclose(third, 0):
                return temp
            else:
                empty_result = []
                return empty_result
        x = -third / second
        result.append((x, f(x, coeffs_diff)))
        return result

    deter = second ** 2 - 4 * first * third
    if det < 0:
        return []

    sqrt_det = np.sqrt(deter)
    x1 = (-second + sqrt_det) / (2 * first)
    x2 = (-second - sqrt_det) / (2 * first)

    if np.isclose(x1, x2):
        single_root = [(x1, f(x1, a_1))]
        return single_root
    else:
        result.append((x1, f(x1, a_1)))
        result.append((x2, f(x2, a_1)))
        return result
coeffs1 = "1 0 -4"
coeffs2 = "1 -2 0"

print(functions(coeffs1, coeffs2))
def skew(x):
    """
    Задание 3. Функция для расчета коэффициента асимметрии.
    Необходимо вернуть значение коэффициента асимметрии, округленное до 2 знаков после запятой.
    """
    return round(scipy_skew(x), 2)



def kurtosis(x):
    """
    Задание 3. Функция для расчета коэффициента эксцесса.
    Необходимо вернуть значение коэффициента эксцесса, округленное до 2 знаков после запятой.
    """
    return round(scipy_kurtosis(x), 2)

    
