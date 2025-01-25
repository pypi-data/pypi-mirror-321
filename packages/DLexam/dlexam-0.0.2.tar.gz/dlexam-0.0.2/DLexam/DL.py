print('Use DL.help()')

def help():
    print('''
    Список ноутбуков по темам:
          
1)01_tensor_v1_0_blank (tens)
2)02_NN_blocks_backprop_v1 (blocks)
3)blank_03_autograd_optim_nn_datasets_3 (autD)
4) 3 ноутбука
          1. 04_1_cnn_image_classification (cnnClas)
          2. 04_2_cnn_pretrained (cnnPre)
          3. 04_3_cnn_1d (cnn1D)
5) 4 ноутбука
          1. 05_1_RL (RL)
          2. 05_2_QL (QL)
          3. 05_3_dqn (QDN)
          4. 05_4_policy_gradients (polGr)
6) 3 ноутбука
          1. 06_1_object_detection (obDet)
          2. 06_2_image_segmentation (imSeg)
          3. 06_4_lightning_deploy (ligDep)

Для обращения к ноутбукам используйте: DL."название_нотубука_info() для навигации по ноутбуку
''')
    

def tens_info():
    print('''
ЧТОБЫ ВЫЗВАТЬ КОД: используйте DL.tens_code("НОМЕР ЗАДАНИЯ")

1.1.1 Создайте двумерный тензор размера (8, 8). Используя как можно меньше операций, добейтесь расстановки кодов "шахматных фигур".
          
1.1.2 Средствами torch рассчитать произведения четных чисел от 2 до 20 на ближайшие к ним бОльшие нечетные числа.
          
1.1.3 Создать тензор размера 11x7 вида: [[1, 2, 3, ..., 7], [11, 12, 13, ..., 17], [21, 22, 23, ..., 27], ..., [101, 102, 103, ..., 107]]
          
1.1.4 Написать функцию, которая для целых значений n и m будет возвращать тензор размера nxm, заполненный текстурой размера 2x2, состоящей из следующих значений:
          
1.1.5 Сгенерировать двумерный тензор t размерности (4, 7), состоящий из случайных действительных чисел, равномерно распределенных в дипазоне от 0 до 20. 
Нормализовать значения массива с помощью преобразования вида  𝑎𝑥+𝑏  так, что после нормализации максимальный элемент масива будет равен 1.0, минимальный 0.0
          
1.1.6 Задать два двумерных тензора ar1 и ar2 размерности (4, 7), состоящих из случайных целых чисел в пределах от 0 до 10. 
Построить двумерный тензор размерности (4, 7), каждый элемент которого представляет собой максимум из двух значений, находящихся на аналогичной позиции в массивах ar1, ar2.
          
1.1.7 Создать тензор из 20 случайных целых чисел от 0 до 100. Получить второе сверху значение в тензоре. Определить индекс этого значения.
          
1.2.1 Создать тензор 11x7 вида: [[1, 2, 3, ..., 7], [11, 12, 13, ..., 17], [21, 22, 23, ..., 27], ..., [101, 102, 103, ..., 107]]. 
При решении задачи применить технику распространения.
          
1.2.2 Вычесть одномерный тензор b_1d из двухмерного тензора a_2d, так,
чтобы каждый элемент одномерного тензора вычитался из всех элементов соответствующих строк двумерного тензора.
          
1.3.1 Получить индексы, для которых элементы тензоров a и b совпадают.
          
1.3.2 Инвертировать порядок элементов в двумерном тензоре torch.arange(9).view(3,3).
          
1.3.3 Из входного тензора a получить только элементы, находящиеся в диапазоне от 5 до 10.
          
1.3.4 Поменять местами столбец 1 и 2 тензора np.arange(9).reshape(3,3)
          
1.3.5 Создать тензор 8 на 10 из случайных целых чисел из диапазона от 0 до 10 и найти в ней строку (ее индекс и вывести саму строку), в которой сумма значений минимальна.
          
1.3.6 Cоздать тензор из 20 случайных целых чисел от 0 до 100. 
Обрезать значения тензора (заменить значения, выходящие за диапазон, на крайние значения) снизу по значению 30, сверху по значению 70.
          
1.3.7 Создать два тензора размера 30 на 3 из случайных целых чисел из диапазона от 0 до 10 и найти все значения первого тензора, 
которые больше соответсвующих (по расположению) значений второго тензора. Подсчитать сумму этих значений.
          
1.3.8 При помощи прихотливого индексирования для двухмерного массива размерности (20, 20), 
состоящего из случайных целых чисел в пределах от 0 до 10 получить массив элементов находящихся на диагонали, проходящей над основной диагональю.
          
1.3.9 Задать два двухмерных тензора ar1 и ar2 размерности (5, 10), состоящих из случайных целых чисел в пределах от 0 до 10. 
Удвоить все значения ar1, которые совпадают со значениями ar2, расположенными на аналогичных позициях.
          
1.3.10 Заданы три двухмерных тензора ar1, ar2 и ar3 размерности (4, 7), состоящие из случайных целых чисел в пределах от 0 до 10. 
Обнулить все элементы ar1, которые больше соответствующих (находящихся в соответствующих позициях) элементов ar2 и меньше соответствующих элементов ar3.
          
1.3.11 Задан двумерный тензор `ar1` размерности (20, 5), состоящий из случайных целых чисел в пределах от 0 до 20. 
Определить, в каких столбцах не менее 5 раз встречается значение, максимальное по своей строке.
          
1.3.12 Задан двумерный тензор ar1 размерности (4, 7), состоящий из случайных чисел в пределах от 0 до 1. 
Обнулить все значения в массиве, расположенные строго правее и ниже максимального элемента массива.
          
1.3.13 Построить "one-hot encoding" для одномерного тензора, содержащего целые числа 
(длина вектора заранее неизвестна, набор значений заранее неизвестен, при этом в итоговой матрице 
должны присутствовать столбцы для всех натуральных чисел вплоть до максимального встречающегося в исходном массиве).
          
1.3.14 Создать тензор arr из 20 случайных целых чисел от 0 до 100. Найти самое частое значение в тензоре. 
Найти индексы в тензоре, соответствующие самому частому значению. 
Проверить, как работет алгоритм при двух значениях, имеющих наибольшую встречаемость, предложить приемлемое поведение алгоритма для этого случая.
          
1.4.1 Приблизительно (с погрешностью порядка 1%) рассчитать на какой части интервала от 0 до 10 значение функции x * sin(x) больше 0.5.
          
1.4.2 Найти все простые числа в пределах ста. (Для решения предлагается использовать Решето Эратосфена) Использовать не более 1 цикла (желательно).
          
1.4.3 Найти евклидово расстояние между двумя одномерными тензорами одинаковой размерности, не используя готовые решения из библиотек.
          
1.4.4 Создать двумерный тензор 20 на 3, содержащий случайные целые числа от 0 до 100.
Интерпретируя тензор как 20 векторов из 3х компонент, отсортировать его по длине векторов.
          
1.4.5 Найти "локальные максимумы" в одномерном тензоре (т.е. значения, большие предыдущего и последующего) 
torch.tensor([1, 3, 7, 1, 2, 6, 0, 1]) и вывести их индексы.
          
1.4.6 Задан произвольный массив numpy (например массив из 100 случайных числе от 0 до 1). Необходимо найти в нем число наиболее близкое к заданному.
          
1.4.7 Решить матричное уравнение A*X*B=-C - найти матрицу X. 
Где A = [[-1, 2, 4], [-3, 1, 2], [-3, 0, 1]], B=[[3, -1], [2, 1]], C=[[7, 21], [11, 8], [8, 4]].
          
1.4.8 Проверить, является ли система векторов a1 = (3; −3; 0; 7), a2 = (2; 2; 4; 7), a3 = (1; 2; 3; 4), a4 = (5; −4; 1; 3) линейно зависимой?

1.4.9 Сгенирировать тензор из 200 случайных целых чисел, нормально распрделенных cо стандартным отклонением  𝜎=10  и матожиданием  𝜇=0 . 
Построить тензор гистограммы с 20 бинами.
''')
    
def tens_code(st):
    print('import torch')
    if st == '1.1.1':
        print('''
chessboard = torch.zeros((8, 8))
chessboard
''')
    elif st == '1.1.2':
        print('''
tensor_even_numbers = torch.arange(2, 21, 2)
tensor_even_numbers
              
tensor_odd_numbers = tensor_even_numbers + 1
tensor_odd_numbers
              
res = tensor_even_numbers * tensor_odd_numbers
res
    ''')
    elif st == '1.1.3':
        print('''
t = torch.arange(1,111).view(11,10)
t
              
t = t[:, :7]
t
    ''')
    elif st == '1.1.4':
        print('''
def function_texture(n, m):
    t = torch.tensor([[0, 1],
                      [2, 3]])

    tensor = t.repeat((n, m))[:n, :m]
    return tensor
              
res = function_texture(4,5)
res
    ''')
    elif st == '1.1.5':
        print('''
t = torch.rand(4, 7) * 20

t_min = t.min()
t_max = t.max()
              

t_norm = (t - t_min) / (t_max - t_min)

#ax + b - линейное преобразование для масштабирования и сдвига значений ( в новый диапазон )
#a = 1/(t_max - t_min) - масштабирование
#b = -t_min/(t_max - t_min) - сдвиг
#x = t
              
t
              
t_norm
    ''')
    elif st == '1.1.6':
        print('''
array1 = torch.randint(0, 11, (4,7))
array2 = torch.randint(0, 11, (4,7))
array1, array2
              
res = torch.max(array1, array2)
res
    ''')
    elif st == '1.1.7':
        print('''
tens = torch.randint(0, 101, (20, ))
tens
              
sort_tens, indices = torch.sort(tens, descending = True)
sort_tens , indices
              
slv = sort_tens[1]
slv
              
index_of_slv = (tens == slv).nonzero(as_tuple = True)[0] #возвращает индексы тех элементов тензора, которые не равны нулю
index_of_slv
#as_tuple индексы в виде кортежа
    ''')
    elif st == '1.2.1':
        print('''
tens = torch.arange(1, 8)
tens
              
tens_o = torch.arange(0, 110, 10).unsqueeze(1)
tens_o
              
new_tens = tens + tens_o
new_tens
    ''')
    elif st == '1.2.2':
        print('''
a_2d = torch.tensor([[3,3,3],[4,4,4],[5,5,5]], dtype = torch.float)
b_1d = torch.tensor([1,2,3], dtype = torch.float)
              
b_1d_unsqueezed = b_1d.unsqueeze(0)
res = a_2d - b_1d
res
#unsqueeze меняет размерность
    ''')
    elif st == '1.3.1':
        print('''
a = torch.tensor([1,2,3,2,3,4,3,4,5,6])
b = torch.tensor([7,2,10,2,7,4,9,4,9,8])

tensor_match = (a == b)
tensor_match
              
index_of_match = (a == b).nonzero(as_tuple = True)
index_of_match
    ''')
    elif st == '1.3.2':
        print('''
tens = torch.arange(9).view(3, 3)
tens

inv_tens = torch.flip(tens, dims = [0,1])
inv_tens
    ''')
    elif st == '1.3.3':
        print('''
a = torch.tensor([2, 6, 1, 9, 10, 3, 27])
a
              
mask = a[(a >= 5) & (a <= 10)]
mask
    ''')
    elif st == '1.3.4':
        print('''
tens = torch.arange(9).reshape(3,3)
tens
            
tens[:, [0, 1]] = tens[:, [1, 0]]
tens
    ''')
    elif st == '1.3.5':
        print('''
tens = torch.randint(0, 11, (8, 10))
tens
              
row_s = torch.sum(tens, dim = 1)
row_s
    
min_s_index = torch.argmin(row_s) #минимальное значение
min_s_index
              
tens[min_s_index]
    ''')
    elif st == '1.3.6':
        print('''
tens = torch.randint(0, 101, (20, ))
tens
              
new_tens = torch.clamp(tens, min = 30, max= 70)
new_tens
    ''')
    elif st == '1.3.7':
        print('''
a = torch.randint(0, 11, (30, 3))
b = torch.randint(0, 11, (30, 3))
              
mask = a > b
mask
              
new = a[mask]
new
              
new.sum()
    ''')
    elif st == '1.3.8':
        print('''
tens = torch.randint(0, 10, (20, 20))
tens
        
tens.diagonal(offset = 1) #диагональные элеменнты, сдвиг относительно главное диагонали
    ''')
    elif st == '1.3.9':
        print('''
ar1 = torch.randint(0,11, (5, 10))
ar2 = torch.randint(0, 10, (5, 10))
ar1, ar2
              
mask = ar1 == ar2
mask
              
new = 2*ar1[mask]
new
    ''')
    elif st == '1.3.10':
        print('''
ar1 = torch.randint(0, 10, (4,7))
ar2 = torch.randint(0, 10, (4,7))
ar3 = torch.randint(0, 10, (4,7))
ar1, ar2, ar3
              
mask = (ar1 > ar2) & (ar1 < ar3)
              
ar1[mask] = 0
              
ar1
    ''')
    elif st == '1.3.11':
        print('''
ar1 = torch.randint(0, 21, (20, 5))
ar1
              
max_v, max_ind = ar1.max(dim = 1)
max_v, max_ind
              
#количество максимальных значений по столбцам
counts = torch.zeros(ar1.size(1), dtype=torch.int)
counts
              
for i in range(ar1.size(0)):
    counts[max_ind[i]] += 1
              
col = (counts >= 5).nonzero(as_tuple=True)[0]
col
    ''')
    elif st == '1.3.12':
        print('''
ar1 = torch.rand((4, 7))
ar1
              
max_v = ar1.max()
max_i = torch.nonzero(ar1 == max_v)
max_v, max_i
              
#если максимальный элемент найден, обнуляем значения
if max_i.size(0) > 0:
    row_index = max_i[0, 0].item()
    col_index = max_i[0, 1].item()

    # Обнуляем строки ниже максимального элемента
    ar1[row_index + 1:, :] = 0
    # Обнуляем столбцы правее максимального элемента
    ar1[row_index, col_index + 1:] = 0
              
ar1
    ''')
    elif st == '1.3.13':
        print('''
a = torch.tensor([2, 3, 2, 2, 2, 1])
a
              
max_v = a.max().item()
max_v
              
one_hot = torch.zeros((a.size(0), max_v), dtype=torch.float)
one_hot
              
one_hot[torch.arange(a.size(0)), a - 1] = 1
one_hot
    ''')
    elif st == '1.3.14':
        print('''
arr = torch.randint(0, 101, (20,))
arr
              
unique_v, counts = arr.unique(return_counts=True)
unique_v, counts
              
max_count_index = torch.argmax(counts)
most_common_value = unique_v[max_count_index]
most_common_count = counts[max_count_index]
              
ind = (arr == most_common_value).nonzero(as_tuple=True)[0]
ind
    ''')
    elif st == '1.4.1':
        print('''
def f(x):
    return x * torch.sin(x)
              
x_values = torch.linspace(0, 10, 1000)
y_values = f(x_values)
              
threshold = 0.5 #порог
              
count_above = (y_values > threshold).sum()
count_above
              
total_points = y_values.numel() #общее количество элементов в тензоре
fraction_above_threshold = count_above.item() / total_points
fraction_above_threshold
    ''')
    elif st == '1.4.2':
        print('''
n = 100
              
tens1 = torch.ones(n + 1, dtype=torch.bool)
tens1
              
# 0 и 1 не являются простыми числами
tens1[0] = False
tens1[1] = False
              
# Решето Эратосфена: помечаем составные числа
for i in range(2, int(n**0.5) + 1):
    if tens1[i]:
        tens1[i*i:n+1:i] = False  # Обнуляем все кратные i
              
primes = torch.nonzero(tens1).flatten() #преобразовать тензор индексов в одномерный
primes
#преобразования (выравнивания) многомерного тензора в одномерный тензор
    ''')
    elif st == '1.4.3':
        print('''
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])
              
if a.size(0) != b.size(0):
    raise ValueError("Тензоры должны иметь одинаковую размерность.")
              
distance = torch.sqrt(torch.sum((a - b) ** 2))
distance
    ''')
    elif st == '1.4.4':
        print('''
tensor = torch.randint(0, 101, (20, 3))
              
lengths = torch.sqrt(torch.sum(tensor**2, dim=1))

# Сортируем тензор по длинам векторов
sorted_tensor, sorted_indices = torch.sort(tensor, dim=0)  # В данном случае мы сортируем по индексу
              
tensor[sorted_indices]
    ''')
    elif st == '1.4.5':
        print('''
tensor = torch.tensor([1, 3, 7, 1, 2, 6, 0, 1])
              
local_maxima_indices = []
              
# Проверяем каждый элемент, начиная со второго и заканчивая предпоследним
for i in range(1, len(tensor) - 1):
    if tensor[i] > tensor[i - 1] and tensor[i] > tensor[i + 1]:
        local_maxima_indices.append(i)

local_maxima_indices
    ''')
    elif st == '1.4.6':
        print('''
import numpy as np
              
array = np.random.rand(100)
array
              
target_value = 0.5
              
# Находим индекс элемента, наиболее близкого к заданному числу
closest_index = np.argmin(np.abs(array - target_value)) #модуль
closest_index
              
# Получаем ближайшее значение
closest_value = array[closest_index]
closest_value
    ''')
    elif st == '1.4.7':
        print('''
A = np.array([[-1, 2, 4],
              [-3, 1, 2],
              [-3, 0, 1]])

B = np.array([[3, -1],
              [2, 1]])

C = np.array([[7, 21],
              [11, 8],
              [8, 4]])
A, B, C
              
# Находим обратные матрицы A и B
A_inv = np.linalg.inv(A)
B_inv = np.linalg.inv(B)
A_inv, B_inv
              
X = A_inv @ (-C) @ B_inv
X
    ''')
    elif st == '1.4.8':
        print('''
a1 = np.array([3, -3, 0, 7])
a2 = np.array([2, 2, 4, 7])
a3 = np.array([1, 2, 3, 4])
a4 = np.array([5, -4, 1, 3])
a1, a2, a3, a4
              
matrix = np.array([a1, a2, a3, a4])
matrix
              
rank = np.linalg.matrix_rank(matrix)
rank
              
# Проверяем линейную зависимость
if rank < matrix.shape[0]:  # matrix.shape[0] - количество векторов
    print("Векторы линейно зависимы.")
else:
    print("Векторы линейно независимы.")
    ''')
    elif st == '1.4.9':
        print('''
import matplotlib.pyplot as plt
              
mu = 0
sigma = 10
size = 200
              
tensor = torch.normal(mu, sigma, (size,))
tensor
              
# Преобразуем в целые числа
tensor_int = tensor.round().long() #тип данных
tensor_int
              
plt.hist(tensor_int.numpy(), bins=20, edgecolor='black', alpha=0.7)
plt.title('Гистограмма распределения случайных чисел')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(axis='y')
plt.show()
    ''')
    else:
        print('no such index')



def blocks_info():
    print('''
ЧТОБЫ ВЫЗВАТЬ КОД: используйте DL.blocks_code("НОМЕР ЗАДАНИЯ")
          
2.1.1. Используя операции над матрицами и векторами из библиотеки torch, реализовать нейрон с заданными весами weights и bias. 
Прогнать вектор inputs через нейрон и вывести результат.
          
2.1.2 Используя операции над матрицами и векторами из библиотеки torch, реализовать полносвязный слой с заданными весами weights и biases. 
Прогнать вектор inputs через слой и вывести результат.
          
2.1.3 Реализовать полносвязный слой из 2.1.2 таким образом, чтобы он мог принимать на вход матрицу (батч) с данными. 
Продемонстрировать работу. Результатом прогона сквозь слой должна быть матрица размера batch_size x n_neurons.
          
2.1.4 Используя операции над матрицами и векторами из библиотеки torch, реализовать полносвязный слой из n_neurons нейронов с n_features весами у каждого нейрона 
(инициализируются из стандартного нормального распределения). Прогнать вектор inputs через слой и вывести результат. 
Результатом прогона сквозь слой должна быть матрица размера batch_size x n_neurons.
          
2.1.5 Используя решение из 2.1.4, создать 2 полносвязных слоя и пропустить матрицу inputs последовательно через эти два слоя. 
Количество нейронов в первом слое выбрать произвольно, количество нейронов во втором слое выбрать так, чтобы результатом прогона являлась матрица (3x7).
          
2.2.1 Используя операции над матрицами и векторами из библиотеки torch, реализовать функцию активации ReLU:
Создать матрицу размера (4,3), заполненную числами из стандартного нормального распределения, и проверить работоспособность функции активации.
          
2.2.2 Используя операции над матрицами и векторами из библиотеки torch, реализовать функцию активации softmax:
Создать матрицу размера (4,3), заполненную числами из стандартного нормального распределения, и проверить работоспособность функции активации. 
Строки матрицы трактовать как выходы линейного слоя некоторого классификатора для 4 различных примеров.
          
2.2.3 Используя операции над матрицами и векторами из библиотеки torch, реализовать функцию активации ELU:
Создать матрицу размера (4,3), заполненную числами из стандартного нормального распределения, и проверить работоспособность функции активации.
          
2.3.1 Используя операции над матрицами и векторами из библиотеки torch, реализовать функцию потерь MSE:
Создать полносвязный слой с 1 нейроном, прогнать через него батч inputs и посчитать значение MSE, трактуя вектор y как вектор правильных ответов.
          
2.3.2 Используя операции над матрицами и векторами из библиотеки torch, реализовать функцию потерь Categorical Cross-Entropy:
Создать полносвязный слой с 3 нейронами и прогнать через него батч inputs. 
Полученный результат пропустить через функцию активации softmax. Посчитать значение CCE, трактуя вектор y как вектор правильных ответов.
          
2.3.3 Модифицировать 2.3.1, добавив L2-регуляризацию.
          
2.4.1 Используя один нейрон и SGD (1 пример за шаг), решите задачу регрессии
          
2.4.1.1 Реализуйте класс SquaredLoss
          
2.4.1.2. Модифицируйте класс Neuron из 2.1.1:
1) Сделайте так, чтобы веса нейрона инициализировались из стандартного нормального распределения
2) Реализуйте расчет градиента относительно весов weights и bias
          
2.4.1.3 Допишите цикл для настройки весов нейрона
SGD
          
2.4.2 Решите задачу 2.4.1, используя пакетный градиентный спуск
          
2.4.1.1 Модифицируйте класс MSELoss из 2.3.1, реализовав расчет производной относительно предыдущего слоя с учетом того, 
что теперь работа ведется с батчами, а не с индивидуальными примерами
          
2.4.2.2. Модифицируйте класс Neuron из 2.4.1.2:
1) Реализуйте метод forward таким образом, чтобы он мог принимать на вход матрицу (батч) с данными.
2) Реализуйте расчет градиента относительно весов weights и bias с учетом того, что теперь работа ведется с батчами, а не с индивидуальными примерами
          
2.4.2.3 Допишите цикл для настройки весов нейрона
          
2.4.3 Используя один полносвязный слой и пакетный градиетный спуск, решите задачу регрессии из 2.4.1
          
2.4.3.1 Модифицируйте класс Linear из 2.1.4. (вычисление градиентов)
          
2.4.3.2 Создайте слой с одним нейроном. Используя класс MSELoss из 2.4.2, убедитесь, что модель обучается
          
2.4.4 Используя наработки из 2.4, создайте нейросеть и решите задачу регрессии.
Предлагаемая архитектура:
Полносвязный слой с 10 нейронами
Активация ReLU
Полносвязный слой с 1 нейроном
''')
    
def blocks_code(st):
    print('import torch')
    if st == '2.1.1':
        print('''
class Neuron:
  def __init__(self, weights, bias):
    self.weights = weights
    self.bias = bias

  def forward(self, inputs):
    return inputs.dot(self.weights) + self.bias
              
inputs = torch.tensor([1.0, 2.0, 3.0, 4.0])
weights = torch.tensor([-0.2, 0.3, -0.5, 0.7])
bias = 3.14
weights.size()
              
n = Neuron(weights, bias)
res = n.forward(inputs)
res
    ''')
    elif st == '2.1.2':
        print('''
class Linear:
  def __init__(self, weights, biases):
    self.weights = weights
    self.bias = biases

  def forward(self, inputs):
    return self.weights.mv(inputs) + self.bias

# torch.mv(inputs, self) умножение матрицы на вектор
# в задании вектор, а не нейрон
              
inputs = torch.tensor([1.0, 2.0, 3.0, 4.0])
weights = torch.tensor([[-0.2, 0.3, -0.5, 0.7],
                        [0.5, -0.91, 0.26, -0.5],
                        [-0.26, -0.27, 0.17, 0.87]])

biases = torch.tensor([3.14, 2.71, 7.2])
              
l = Linear(weights, biases)
res = l.forward(inputs)
res
    ''')
    elif st == '2.1.3':
        print('''
class Linearbatch:
  def __init__(self, weights, biases):
    self.weights = weights
    self.bias = biases

  def forward(self, inputs):
    return self.weights.mm(inputs.T) + self.bias

# torch.mv(inputs, self)
#Т, чтоб матрица была размером inputs * butch
              
weights = torch.tensor([[-0.2, 0.3, -0.5, 0.7],
                        [0.5, -0.91, 0.26, -0.5],
                        [-0.26, -0.27, 0.17, 0.87]])

biases = torch.tensor([3.14, 2.71, 7.2])
              
inputs = torch.tensor([[1, 2, 3, 2.5],
                       [2, 5, -1, 2],
                       [-1.5, 2.7, 3.3, -0.8]])
              
l1 = Linearbatch(weights, biases)
res = l1.forward(inputs)
res
    ''')
    elif st == '2.1.4':
        print('''
class LinearS:
  def __init__(self, n_features, n_neurons):
    self.weights = torch.randn(n_features, n_neurons) #матрица
    self.bias = torch.randn(1, n_neurons) #вектор

  def forward(self, inputs):
    return inputs.mm(self.weights) + self.bias

#матричное умножение, где в inputs строки - батч сайз, столбцы - кол-во нейронов
              
inputs = torch.tensor([[1, 2, 3, 2.5],
                       [2, 5, -1, 2],
                       [-1.5, 2.7, 3.3, -0.8]])
              
l = LinearS(4, 3)
l.forward(inputs)
    ''')
    elif st == '2.1.5':
        print('''
inputs = torch.tensor([[1, 2, 3, 2.5],
                       [2, 5, -1, 2],
                       [-1.5, 2.7, 3.3, -0.8]])
              
l1 = LinearS(4,10) #4 входа, 10 нейронов
l2 = LinearS(10,7) #10 входов (из первого слоя), 7 нейронов

res1 = l1.forward(inputs)
res1.shape
              
res2 = l2.forward(res1)
res2.shape
              
res2
    ''')
    elif st == '2.2.1':
        print('''
#def replace(vector):
  #return [max(0,x) for x in vector]
              
#vector = [-5, 2, -10, -9, 6, 7, 0]
#replace(vector)
              
#Реализация Rectified Linear Unit
              
class ReLU:
    def forward(self, inputs):
        return torch.maximum(inputs, torch.tensor(0.0))  # Реализация ReLU
#берем максимум между каждым элементом тензора и 0
              
inputs = torch.randn(4, 3)
inputs
              
relu = ReLU()
              
go = relu.forward(inputs)
go
    ''')
    elif st == '2.2.2':
        print('''
class Softmax:
  def forward(self, inputs):
    values_exp = torch.exp(inputs)
    sum_exp = values_exp.sum(dim = 1, keepdim = True) # keepdim = True тензор будет иметь ту же размерность, что и входной, dim = 1 - сумма столбцов
    #для каждой строки
    return values_exp/sum_exp
              
inputs = torch.randn(4, 3)
inputs
              
softmax = Softmax()
              
go = softmax.forward(inputs)
go
    ''')
    elif st == '2.2.3':
        print('''
#Реализация Exponential Linear Unit
              
class ELU:
  def __init__(self, alpha):
    self.alpha = alpha

  def forward(self, inputs):
    return torch.where(inputs > 0, inputs, self.alpha * (torch.exp(inputs) - 1))
              
inputs = torch.randn(4, 3)
inputs
              
elu = ELU(alpha = 0.5)
go = elu.forward(inputs)
go
    ''')
    elif st == '2.3.1':
        print('''
class MSELoss:
  def forward(self, y_pred, y_true):
    return ((y_pred - y_true) ** 2).sum() / len(y_pred)
              
inputs = torch.tensor([[1, 2, 3, 2.5],
                       [2, 5, -1, 2],
                       [-1.5, 2.7, 3.3, -0.8]])

y = torch.tensor([2, 3, 4])
              
s = LinearS(4, 1)
go = s.forward(inputs)
go
              
y_pred = ReLU().forward(go)
y_pred
              
MSELoss().forward(y_pred = y_pred, y_true = y)
    ''')
    elif st == '2.3.2':
        print('''
class CategoricalCrossentropyLoss:
  def forward(self, y_pred, y_true):
    L = -(y_true*torch.log(y_pred)).sum()/len(y_pred)
    return L
              
inputs = torch.tensor([[1, 2, 3, 2.5],
                        [2, 5, -1, 2],
                        [-1.5, 2.7, 3.3, -0.8]])
y = torch.tensor([1, 0, 0])
              
s = LinearS(4, 3)
go = s.forward(inputs)
go
              
y_pred = Softmax().forward(go)
y_pred
              
CategoricalCrossentropyLoss().forward(y_pred = y_pred, y_true = y)
    ''')
    elif st == '2.3.3':
        print('''
#L2 регуляризация от переобучения
              
class MSELossL2:
  def __init__(self, lambda_ = 1):
    self.lambda_ = lambda_

  def data_loss(self, y_pred, y_true):
    return torch.sum((y_true - y_pred) ** 2) #подсчет первого слагаемого из формулы

  def reg_loss(self, layer):
    # используйте атрибуты объекта layer, в которых хранятся веса слоя
    # <подсчет второго слагаемого из формулы>
    return self.lambda_ * torch.sum(layer ** 2)

  def forward(self, y_pred, y_true, layer):
    return self.data_loss(y_pred, y_true) + self.reg_loss(layer)
              

y_pred = torch.tensor([-0.5, 1, 1.7])
y_true = torch.tensor([0, 0.6, 2.3])
layer = torch.normal(0, 5, (10, 1))
              
s = LinearS(4, 1)
go = s.forward(inputs)
go
              
mse2 = MSELossL2(0.4)
              
loss_value = mse2.forward(y_pred, y_true, layer)
loss_value
    ''')
    elif st == '2.4.1':
        print('''
learning_rate = 0.01  #шаг обучения
epochs = 1000
x_train = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y_train = torch.tensor([[3.0], [5.0], [7.0], [9.0]])
w = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)
#requires_grad=True градиент, изменение w b
              
def predict(x):
    return x * w + b

def mse_loss(y_pred, y_true):
    return ((y_pred - y_true) ** 2).mean()
              
for epoch in range(epochs):
    total_loss = 0

    for x, y in zip(x_train, y_train):
        y_pred = predict(x)
        loss = mse_loss(y_pred, y)

        loss.backward()  #вычисление градиентов

        #обновление весов
        with torch.no_grad():
            w -= learning_rate * w.grad
            b -= learning_rate * b.grad

        total_loss += loss.item() #накопление ошибки

    if epoch % 100 == 0:
      print(f'Epoch {epoch}, Loss: {total_loss / len(x_train)}')

print(f'Обученные весы: {w.item()}')
print(f'Обученное смещение: {b.item()}')
    ''')
    elif st == '2.4.1.1':
        print('''
class SquaredLoss:
  def forward(self, y_pred, y_true):
    return (y_pred-y_true)**2.  #реализовать логику MSE

  def backward(self, y_pred, y_true):
    self.dinput = 2*(y_pred-y_true)  #df/dy_pred
    ''')
    elif st == '2.4.1.2':
        print('''
def forward(self, weights, bias):
  self.weights = weights
  self.bias = bias

def backward(self, dvalue):
  dweights = dvalue * self.inputs
  dinputs = dvalue * self.weights
  dbias = 1 * dvalue
              
class Neuron:
    def __init__(self, n_inputs):
        self.w = torch.randn(n_inputs)
        self.b = torch.randn(1)

    def forward(self, inputs):
      self.inputs = inputs
      return inputs.dot(self.w) + self.b


    def backward(self, dvalue):
    # Градиент по весам (как сильно изменяется ошибка относительно каждого веса)
      self.dweights = dvalue * self.inputs  # dL/dW = dL/dy * dy/dW

    # Градиент по входам (как сильно изменяется ошибка относительно каждого входа)
      self.dinput = dvalue * self.w  # dL/dX = dL/dy * dy/dX

    # Градиент по смещению (как сильно изменяется ошибка относительно смещения)
      self.dbias = dvalue * 1  # dL/db = dL/dy * dy/db = dL/dy
    ''')
    elif st == '2.4.1.3':
        print('''
class Neuron:
    def __init__(self, n_inputs):
        self.w = torch.randn(n_inputs)
        self.b = torch.randn(1)

    def forward(self, inputs):
        self.inputs = inputs
        return inputs.dot(self.w) + self.b

    def backward(self, dvalue):
        self.dweights = dvalue * self.inputs
        self.dinput = dvalue * self.w
        self.dbias = dvalue * 1

class SquaredLoss:
    def forward(self, y_pred, y_true):
        return (y_pred - y_true) ** 2  # MSE loss

    def backward(self, y_pred, y_true):
        self.dinput = 2 * (y_pred - y_true)  # dL/dy
              
X = torch.tensor([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0]])
y = torch.tensor([2.0, 3.0, 4.0])

n_inputs = X.size()[1]
lr = 0.1  #ню
n_epoch = 100

neuron = Neuron(n_inputs)
loss = SquaredLoss()

losses = []
              
for epoch in range(n_epoch):
    for x_example, y_example in zip(X, y):
        #forward pass
        y_pred = neuron.forward(x_example)
        curr_loss = loss.forward(y_pred, y_example)
        losses.append(curr_loss)

        #backpropagation
        loss.backward(y_pred, y_example)
        neuron.backward(loss.dinput)

        # Шаг градиентного спуска
        neuron.w -= lr * neuron.dweights
        neuron.b -= lr * neuron.dbias
              
import matplotlib.pyplot as plt
plt.plot([tensor.item() for tensor in losses])
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.title('Loss over time')
plt.show()
    ''')
    elif st == '2.4.2':
        print('''
import torch
from sklearn.datasets import make_regression

class Neuron:
    def __init__(self, n_inputs):
        self.w = torch.randn(n_inputs, 1, requires_grad=True)
        self.b = torch.randn(1, requires_grad=True)

    def forward(self, inputs):
        return inputs.matmul(self.w) + self.b

class MSELoss:
    def forward(self, y_pred, y_true):
        self.y_pred = y_pred
        self.y_true = y_true
        return ((y_pred - y_true) ** 2).mean()

    def backward(self):
        return 2 * (self.y_pred - self.y_true) / len(self.y_pred)

# Генерация данных
X, y, coef = make_regression(n_features=4, n_informative=4, coef=True, bias=0.5)
X = torch.from_numpy(X).to(dtype=torch.float32)
y = torch.from_numpy(y).to(dtype=torch.float32).view(-1, 1)

neuron = Neuron(n_inputs=4)
loss_fn = MSELoss()

learning_rate = 0.01
n_epochs = 500
batch_size = 10
losses = []
              

for epoch in range(n_epochs):
    permutation = torch.randperm(X.size(0)) #получаем индексы для всех примеров

    for i in range(0, X.size(0), batch_size): #проходим по всем данным , разбиваем их на пакеты размера батч сайз
        indices = permutation[i:i + batch_size] #индексы для текущего батча
        X_batch, y_batch = X[indices], y[indices]

        y_pred = neuron.forward(X_batch)

        #функция потерь
        loss = loss_fn.forward(y_pred, y_batch)
        losses.append(loss.item()) #сохраняем значение

        #backpropagation
        loss_grad = loss_fn.backward()  #градиент функции потерь

        #вычисляем градиенты для весов и смещения
        loss_grad_w = X_batch.t() @ loss_grad #получаем градиенты по каждому весу
        loss_grad_b = loss_grad.mean() #Ср знач градиента потерь для обновления смещения (корректировать смещение в зависимости от  направления ошибки)

        with torch.no_grad():
            neuron.w -= learning_rate * loss_grad_w
            neuron.b -= learning_rate * loss_grad_b

    if epoch % 100 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')
              

plt.plot(losses)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss over time')
plt.show()
    ''')
    elif st == '2.4.2.1':
        print('''
class MSELoss:
    def forward(self, y_pred, y_true):
        # Вычисляем MSE для батча
        return ((y_pred - y_true) ** 2).mean()  # усредняем по всему батчу

    def backward(self, y_pred, y_true):
        # Градиент по y_pred для батча
        batch_size = len(y_pred)
        return 2 * (y_pred - y_true) / batch_size  # усредняем по батчу
              

y_true = torch.tensor([[2.0], [3.0], [4.0]])
y_pred = torch.tensor([[2.5], [2.8], [4.2]])

loss = MSELoss()

loss_value = loss.forward(y_pred, y_true)
print(f'Loss: {loss_value}')

gradients = loss.backward(y_pred, y_true)
gradients
    ''')
    elif st == '2.4.2.2':
        print('''
class Neuron:
  def __init__(self, n_inputs):
    self.w = torch.randn(n_inputs, 1)
    self.b = torch.randn(1)

  def forward(self, inputs):
    self.inputs = inputs
    return inputs.matmul(self.w) + self.b #производная

  def backward(self, dvalue):
    # dvalue - значение градиента, которое приходит нейрону от следующего слоя сети
    # в данном случае это будет градиент L по y^ (созданный методом backwards у объекта MSELoss)
    self.dweights = self.inputs.t().matmul(dvalue)  # df/dW
    self.dinput = dvalue.matmul(self.w.t())          # df/dX
    self.dbias = dvalue.sum(dim=0)# df/db
    ''')
    elif st == '2.4.2.3':
        print('''
class Neuron:
    def __init__(self, n_inputs):
        self.w = torch.randn(n_inputs, 1)
        self.b = torch.randn(1)

    def forward(self, inputs):
        self.inputs = inputs
        return inputs.matmul(self.w) + self.b

    def backward(self, dvalue):
        # Обратное распространение ошибки
        self.dweights = self.inputs.t().matmul(dvalue)  # df/dW
        self.dinput = dvalue.matmul(self.w.t())  # df/dX
        self.dbias = dvalue.sum(dim=0)  # df/db
              
class MSELoss:
    def forward(self, y_pred, y_true):
        return ((y_pred - y_true) ** 2).mean()  # Среднеквадратичная ошибка

    def backward(self, y_pred, y_true):
        return 2 * (y_pred - y_true) / y_true.size(0)  # Производная MSE
              
X = torch.tensor([[1.0, 2.0],
                  [3.0, 4.0],
                  [5.0, 6.0]], dtype=torch.float32)  # Батч из 3 примеров с 2 входами
y = torch.tensor([[1.0],
                  [2.0],
                  [3.0]], dtype=torch.float32)
              
n_inputs = X.size(1)
lr = 0.01
n_epochs = 100

neuron = Neuron(n_inputs)
loss_fn = MSELoss()
              

for epoch in range(n_epochs):
    total_loss = 0

    for x_example, y_example in zip(X, y):  # Проход по каждому примеру в батче
        y_pred = neuron.forward(x_example.unsqueeze(0))  # Прогон через нейрон
        curr_loss = loss_fn.forward(y_pred, y_example.unsqueeze(0))  #добавляем размерность
        total_loss += curr_loss.item()

        # Обратный проход
        dvalue = loss_fn.backward(y_pred, y_example.unsqueeze(0))  # Градиенты потерь
        neuron.backward(dvalue)  # Градиенты нейрона

        neuron.w -= lr * neuron.dweights
        neuron.b -= lr * neuron.dbias

    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {total_loss / len(X)}')

neuron.w
              

plt.figure(figsize=(10, 6))
plt.plot(losses, label='Training Loss', color='blue')
plt.title('Loss During Training')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid()
plt.show()
    ''')
    elif st == '2.4.3':
        print('''
import torch.nn as nn
import torch.optim as optim
              
n_inputs = X.size(1)
n_outputs = y.size(1)
lr = 0.01
n_epochs = 100
batch_size = 2
              
model = nn.Linear(n_inputs, n_outputs)  # Полносвязный слой
              
criterion = nn.MSELoss()  # Функция потерь: среднеквадратичная ошибка
optimizer = optim.SGD(model.parameters(), lr=lr)  #оптимизатор - стохастический градиентный спуск
              
losses = []
              
for epoch in range(n_epochs):
    total_loss = 0

    for i in range(0, len(X), batch_size):
        X_batch = X[i:i + batch_size]  #батч входных данных
        y_batch = y[i:i + batch_size]  #батч истинных значений

        #форвард пасс
        y_pred = model(X_batch)  # Прогон через полносвязный слой

        curr_loss = criterion(y_pred, y_batch)
        total_loss += curr_loss.item()

        curr_loss.backward()  #вычисление градиентов
        optimizer.step()  #обновление весов

    avg_loss = total_loss / (len(X) / batch_size)
    losses.append(avg_loss)

    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {avg_loss}')
              
model.weight.data
              

model.bias.data
    ''')
    elif st == '2.4.3.1':
        print('''
class Linear:
    def __init__(self, n_features, n_neurons):
        self.weights = torch.randn(n_features, n_neurons)
        self.biases = torch.zeros(1, n_neurons)

    def forward(self, inputs):
        self.inputs = inputs
        return inputs.matmul(self.weights) + self.biases

    def backward(self, dvalues):
        self.dweights = self.inputs.t().matmul(dvalues)  # df/dW = X^T * dL/dy
        self.dbiases = dvalues.sum(dim=0, keepdim=True)  # df/db = sum(dL/dy)
        self.dinputs = dvalues.matmul(self.weights.t())  # df/dX = dL/dy * W^T

        return self.dinputs  # Возвращаем градиенты для предыдущего слоя
              
    ''')
    elif st == '2.4.3.2':
        print('''
class MSELoss:
    def forward(self, y_pred, y_true):
        return ((y_pred - y_true) ** 2).sum() / len(y_pred)

    def backward(self, y_pred, y_true):
        # df/dy = 2*(y_pred - y_true) / N
        return 2 * (y_pred - y_true) / len(y_pred)
              
class Linear:
    def __init__(self, n_features, n_neurons):
        self.weights = torch.randn(n_features, n_neurons)
        self.biases = torch.zeros(1, n_neurons)

    def forward(self, inputs):
        self.inputs = inputs
        return inputs.matmul(self.weights) + self.biases

    def backward(self, dvalues):
        # df/dW = X^T * dL/dy
        self.dweights = self.inputs.t().matmul(dvalues)
        # df/db = sum(dL/dy)
        self.dbiases = dvalues.sum(dim=0, keepdim=True)
        # df/dX = dL/dy * W^T
        self.dinputs = dvalues.matmul(self.weights.t())
        return self.dinputs  # Возвращаем градиенты для предыдущего слоя
              

X = torch.tensor([[1.0, 2.0],
                  [3.0, 4.0],
                  [5.0, 6.0],
                  [7.0, 8.0]], dtype=torch.float32)  # Входные данные (4 примера, 2 признака)
y = torch.tensor([[1.0],
                  [2.0],
                  [3.0],
                  [4.0]], dtype=torch.float32)
              
n_features = X.size(1)
n_neurons = 1  # Количество выходов
lr = 0.01
n_epochs = 100
              
linear_layer = Linear(n_features, n_neurons)

loss_fn = MSELoss()

losses = []
              

for epoch in range(n_epochs):
    y_pred = linear_layer.forward(X)

    curr_loss = loss_fn.forward(y_pred, y)
    losses.append(curr_loss.item())

    dvalues = loss_fn.backward(y_pred, y)  # Вычисляем градиенты потерь
    linear_layer.backward(dvalues)  # Обратный проход через слой

    linear_layer.weights -= lr * linear_layer.dweights  #веса
    linear_layer.biases -= lr * linear_layer.dbiases  #смещения

    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {curr_loss.item()}')
              

linear_layer.weights.data
              
linear_layer.biases.data
              
plt.figure(figsize=(10, 6))
plt.plot(losses, label='Training Loss', color='blue')
plt.title('Loss During Training')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid()
plt.show()
    ''')
    elif st == '2.4.4':
        print('''
class MSELoss:
    def forward(self, y_pred, y_true):
        return ((y_pred - y_true) ** 2).sum() / len(y_pred)

    def backward(self, y_pred, y_true):
        return 2 * (y_pred - y_true) / len(y_pred)
              

class Linear:
    def __init__(self, n_features, n_neurons):
        self.weights = torch.randn(n_features, n_neurons) * 0.01  # Инициализация весов
        self.biases = torch.zeros(1, n_neurons)  # Инициализация смещений

    def forward(self, inputs):
        self.inputs = inputs
        return inputs.matmul(self.weights) + self.biases

    def backward(self, dvalues):
        self.dweights = self.inputs.t().matmul(dvalues)
        self.dbiases = dvalues.sum(dim=0, keepdim=True)
        self.dinputs = dvalues.matmul(self.weights.t())
        return self.dinputs
              
class ReLU:
    def forward(self, inputs):
        self.inputs = inputs
        return torch.maximum(inputs, torch.tensor(0.0))  # y = max(0, x)

    def backward(self, dvalues):
        self.dinputs = dvalues.clone()
        self.dinputs[self.inputs <= 0] = 0  # Производная ReLU
        return self.dinputs
              

X = torch.tensor([[1.0, 2.0],
                  [3.0, 4.0],
                  [5.0, 6.0],
                  [7.0, 8.0],
                  [9.0, 10.0],
                  [11.0, 12.0],
                  [13.0, 14.0],
                  [15.0, 16.0]], dtype=torch.float32)  # Входные данные (8 примеров, 2 признака)
y = torch.tensor([[2.0],
                  [4.0],
                  [6.0],
                  [8.0],
                  [10.0],
                  [12.0],
                  [14.0],
                  [16.0]], dtype=torch.float32)
              

n_features = X.size(1)
n_neurons_hidden = 10
n_neurons_output = 1  # Количество выходов (один нейрон)
lr = 0.01
n_epochs = 100


hidden_layer = Linear(n_features, n_neurons_hidden)
activation = ReLU()
output_layer = Linear(n_neurons_hidden, n_neurons_output)

loss_fn = MSELoss()

losses = []

for epoch in range(n_epochs):
    # Прямой проход
    hidden_output = hidden_layer.forward(X)
    activated_output = activation.forward(hidden_output)
    y_pred = output_layer.forward(activated_output)


    curr_loss = loss_fn.forward(y_pred, y)
    losses.append(curr_loss.item())


    dvalues = loss_fn.backward(y_pred, y)  # Вычисляем градиенты потерь
    dactivated = output_layer.backward(dvalues)  # Обратный проход через выходной слой
    dhidden = activation.backward(dactivated)  # Обратный проход через активацию
    hidden_layer.backward(dhidden)  # Обратный проход через скрытый слой


    output_layer.weights -= lr * output_layer.dweights  # Обновление весов выходного слоя
    output_layer.biases -= lr * output_layer.dbiases  # Обновление смещений выходного слоя
    hidden_layer.weights -= lr * hidden_layer.dweights  # Обновление весов скрытого слоя
    hidden_layer.biases -= lr * hidden_layer.dbiases  # Обновление смещений скрытого слоя

    # Вывод потерь через каждые 10 эпох
    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {curr_loss.item()}')

# Печать окончательных весов и смещения
print("Final weights (output layer):", output_layer.weights.data)
print("Final bias (output layer):", output_layer.biases.data)
print("Final weights (hidden layer):", hidden_layer.weights.data)
print("Final bias (hidden layer):", hidden_layer.biases.data)
              

plt.figure(figsize=(10, 6))
plt.plot(losses, label='Training Loss', color='blue')
plt.title('Loss During Training')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid()
plt.show()
              

X = torch.linspace(-1, 1, 100).view(-1, 1)
y = X.pow(2) + 0.2 * torch.rand(X.size())
              
class Linear:
    def __init__(self, n_features, n_neurons):
        self.weights = torch.randn(n_features, n_neurons)
        self.biases = torch.randn(1, n_neurons)

    def forward(self, inputs):
        self.inputs = inputs
        return inputs.matmul(self.weights) + self.biases

    def backward(self, dvalues):
        self.dweights = self.inputs.t().matmul(dvalues)  # Градиенты по весам
        self.dbiases = dvalues.sum(dim=0, keepdim=True)   # Градиенты по смещениям
        self.dinputs = dvalues.matmul(self.weights.t())    # df/dX
              

class MSELoss:
    def forward(self, y_pred, y_true):
        self.y_pred = y_pred
        self.y_true = y_true
        return ((y_pred - y_true) ** 2).sum() / len(y_pred)

    def backward(self):
        return 2 * (self.y_pred - self.y_true) / len(self.y_pred)
              

class Activation_ReLU:
  def forward(self, inputs):
    self.inputs = inputs
    self.output = inputs.clip(min=0)
    return self.output

  def backward(self, dvalues):
    self.dinputs = dvalues.clone()
    self.dinputs[self.inputs <= 0] = 0
              

import torch.nn as nn
              

fc1 = Linear(n_features=1, n_neurons=20)
# relu = Activation_ReLU()
relu= nn.Sigmoid()
fc2 = Linear(n_features=20, n_neurons=1)

# Параметры обучения
loss = MSELoss()
lr = 0.1
ys = []
losses = []
batch = 10
num_epochs = 2500  # Количество эпох

# Обучение нейросети
for epoch in range(num_epochs):
    # Перемешивание данных
    ind = torch.randperm(X.size(0))
    xn = X[ind]
    yn = y[ind]

    # Инициализация переменных для суммирования градиентов
    total_dweights_fc1 = 0
    total_dbiases_fc1 = 0
    total_dweights_fc2 = 0
    total_dbiases_fc2 = 0

    for i in range(0, X.size(0), batch):
        x_ex = xn[i:i + batch]
        y_ex = yn[i:i + batch]

        out1 = fc1.forward(x_ex)
        out2 = relu.forward(out1)
        y_pred = fc2.forward(out2)

        curr_loss = loss.forward(y_pred, y_ex)
        losses.append(curr_loss.item())

        dvalue = loss.backward()  # Градиенты потерь
        fc2.backward(dvalue)      # Градиенты для второго слоя
        relu.backward(fc2.dinputs) # Градиенты для активации ReLU
        fc1.backward(relu.dinputs) # Градиенты для первого слоя

        # Суммируем градиенты
        total_dweights_fc1 += fc1.dweights
        total_dbiases_fc1 += fc1.dbiases
        total_dweights_fc2 += fc2.dweights
        total_dbiases_fc2 += fc2.dbiases

    # Обновление весов и смещений после обработки всех батчей
    fc1.weights -= lr * total_dweights_fc1 / (X.size(0) // batch)
    fc1.biases -= lr * total_dbiases_fc1 / (X.size(0) // batch)
    fc2.weights -= lr * total_dweights_fc2 / (X.size(0) // batch)
    fc2.biases -= lr * total_dbiases_fc2 / (X.size(0) // batch)

    if epoch % 200 == 0:
        out1 = fc1.forward(X)
        out2 = relu.forward(out1)
        y_pred = fc2.forward(out2)
        data_loss = loss.forward(y_pred, y)
        print(f'Epoch {epoch} mean loss {data_loss.item()}')
        ys.append(y_pred.detach().clone())
              

fig, axs = plt.subplots(len(ys), 1, figsize=(10, 40))

for ax, y_, epoch in zip(axs, ys, range(0, len(ys) * 200, 200)):
    ax.scatter(X.numpy(), y.numpy(), color="orange", label="Истинные значения")
    ax.plot(X.numpy(), y_.numpy(), 'g-', lw=3, label=f"Предсказания на эпохе {epoch}")
    ax.set_xlim(-1.05, 1.5)
    ax.set_ylim(-0.25, 1.25)
    ax.set_title(f"Epoch {epoch}")
    ax.legend()

plt.tight_layout()
plt.show()
    ''')
    else:
        print('no such index')

def autD_info():
    print('''
ЧТОБЫ ВЫЗВАТЬ КОД: используйте DL.autD_code("НОМЕР ЗАДАНИЯ")
          
3.1.1 Воспользовавшись классами Neuron и SquaredLoss из задачи 2.4.1 и автоматическим дифференцированием, которое предоставляет torch, решить задачу регрессии. 
Для оптимизации использовать стохастический градиетный спуск.
          
3.1.2 Воспользовавшись классами Linear и MSELoss из задачи 2.1.4 и 2.3.1, ReLU из 2.2.1 и автоматическим дифференцированием, 
которое предоставляет torch, решить задачу регрессии. Для оптимизации использовать пакетный градиентный спуск. 
Вывести график функции потерь в зависимости от номера эпохи. Вывести на одном графике исходные данные и предсказанные значения.
          
3.2 Алгоритмы оптимизации в torch.optim
          
3.2.1 Решить задачу 3.1.1, воспользовавшись оптимизатором optim.SDG для применения стохастического градиентого спуска
          
3.2.2 Решить задачу 3.1.2, воспользовавшись оптимизатором optim.Adam для применения пакетного градиентого спуска. 
Вывести график функции потерь в зависимости от номера эпохи. Вывести на одном графике исходные данные и предсказанные значения.
          
3.3.1 Решить задачу регрессии, соблюдая следующие условия:
Оформить нейронную сеть в виде класса - наследника nn.Module
При создании сети использовать готовые блоки из torch.nn: слои, функции активации, функции потерь и т.д.
Для оптимизации использовать любой алгоритм оптимизации из torch.optim
          

3.3.2 Решить задачу регрессии, соблюдая следующие условия:
Оформить нейронную сеть в виде объекта nn.Sequential
При создании сети использовать готовые блоки из torch.nn: слои, функции активации, функции потерь и т.д.
Для оптимизации использовать любой алгоритм оптимизации из torch.optim
          
3.4. Datasets and dataloaders
          
3.4.1 Создать датасет, поставляющий данные из задачи 3.1.2.
Создать DataLoader на основе этого датасета и проверить работоспособность.
Воспользовавшись результатами 3.3.1 (или 3.3.2) обучите модель, пользуясь мини-пакетным градиентным спуском с размером пакета (batch_size) = 10
          

3.4.2.1 Создайте датасет на основе файла diamonds.csv.
Удалите все нечисловые столбцы
Целевой столбец (y) - price
Преобразуйте данные в тензоры корректных размер
          
3.4.2.2 Разбейте датасет на обучающий и тестовый датасет при помощи torch.utils.data.random_split.
          
3.4.2.3 Обучите модель для предсказания цен при помощи мини-пакетного градиентного спуска (batch_size = 256).
          
3.4.3 Модифицируйте метод __init__ датасета из 3.4.2 таким образом, чтобы он мог принимать параметр transform: callable. 
Реализуйте класс DropColsTransform для удаления нечисловых данных из массива. 
Реализуйте класс ToTensorTransorm для трансформации массива в тензор.
          
3.4.2.4 Выведите график функции потерь в зависимости от номера эпохи (значение потерь для эпохи рассчитывайте как среднее значение ошибок на каждом батче). 
Проверьте качество модели на тестовой выборке.
''')
    
def autD_code(st):
    print('''
import torch
import numpy as np
from matplotlib import pyplot as plt
''')
    if st == '3.1.1':
        print('''
from sklearn.datasets import make_regression

X, y, coef = make_regression(n_features=4, n_informative=4, coef=True, bias=0.5)
X = torch.from_numpy(X).to(dtype=torch.float32)
y = torch.from_numpy(y).to(dtype=torch.float32)
              
class Neuron:
    def __init__(self, n_inputs: int):
        self.weights = torch.randn(n_inputs, 1, requires_grad=True)
        self.bias = torch.randn(1, requires_grad=True)

    def __call__(self, inputs: torch.Tensor):
        return inputs @ self.weights + self.bias

  ## def backward(self):
  ##     self.dweights = self.weights.grad
  ##     self.dbias = self.bias.grad
              

## класс squared loss - разница истинных значений с предсказанными
class SquaredLoss:
    def __call__(self, predictions: torch.Tensor, targets: torch.Tensor):
        return torch.mean((predictions - targets) ** 2)
              

def train(model, loss_fn, X, y, lr=0.01, epochs=1000):
    for epoch in range(epochs):


        pred = model(X)  #call из класса Neuron
        loss = loss_fn(pred, y)


        loss.backward()



        with torch.no_grad():
            model.weights -= lr * model.weights.grad
            model.bias -= lr * model.bias.grad


            model.weights.grad.zero_() #зануляем градиенты, тк они накапливаются
            model.bias.grad.zero_()


        if epoch % 100 == 0:
            print(f'Epoch {epoch}, Loss: {loss.item()}')
              

##train(neuron, loss_fn, X, y, lr = 0.1, epochs = 1000)
              

neuron = Neuron(n_inputs=X.shape[1])
loss_fn = SquaredLoss()

train(neuron, loss_fn, X, y, lr = 0.01, epochs = 100)
              

neuron = Neuron(X.shape[1])
criterion = SquaredLoss()
lr = 0.01


for epoch in range(100):
    for x_example, y_example in zip(X, y):
        y_pred = neuron(x_example)
        loss = criterion(y_pred, y_example)
        loss.backward()
        with torch.no_grad():
            neuron.weights -= lr * neuron.weights.grad
            neuron.bias -= lr * neuron.bias.grad
        neuron.weights.grad.zero_()
        neuron.bias.grad.zero_()
    if epoch % 10 == 0:
        print(f"Epoch: {epoch} | Loss: {loss.item()}")
              

neuron.weights, coef
''')
    elif st == '3.1.2':
        print('''
X = torch.linspace(0, 1, 100).view(-1, 1)
y = torch.sin(2 * np.pi * X) + 0.5 * torch.rand(X.size())
              

class Linear:
  def __init__(self, n_inputs: int, n_outputs: int):
    self.weights = torch.randn(n_inputs, n_outputs, requires_grad = True)
    self.bias = torch.randn(n_outputs, requires_grad = True)

  def __call__(self, inputs: torch.Tensor):
    return inputs @ self.weights + self.bias


class ReLU:
  def __call__(self, x: torch.Tensor):
    return torch.maximum(torch.zeros_like(x), x)


class MSE:
  def __call__(self, predictions: torch.Tensor, targets: torch.Tensor):
    return torch.mean((predictions - targets) ** 2)


class Model:
  def __init__(self):
    self.linear = Linear(n_inputs = 4, n_outputs = 1)
    self.relu = ReLU()

  def __call__(self, x: torch.Tensor):
    x = self.linear(x)
    return self.relu(x)
              


def train(model, loss_fn, X, y, lr = 0.01, epochs = 1000):
  losses = []

  for epoch in range(epochs):
    predictions = model(X)
    loss = loss_fn(predictions, y)
    losses.append(loss.item())



    loss.backward()


    with torch.no_grad():
      model.linear.weights -= lr * model.linear.weights.grad
      model.linear.bias -= lr * model.linear.bias.grad


      model.linear.weights.zero_()
      model.linear.bias.zero_()

    if epoch % 100 == 0:
      print(f'epoch {epoch}, loss {loss}')

  return losses
              


import matplotlib.pyplot as plt

def plot_loss(losses):
    plt.plot(losses)  # Построение графика потерь
    plt.title('Loss vs Epochs')  # Заголовок графика
    plt.xlabel('Epoch')  # Метка оси X
    plt.ylabel('Loss')  # Метка оси Y
    plt.grid()  # Добавление сетки
    plt.show()  # Отображение графика
              

def plot_predictions(X, y, model):
    with torch.no_grad():
        predictions = model(X)  # Получаем предсказанные значения

    plt.scatter(X[:, 0], y, label='True Values', color='blue')  # Истинные значения
    plt.scatter(X[:, 0], predictions, label='Predictions', color='red')  # Предсказанные значения
    plt.legend()  # Легенда
    plt.title('True Values vs Predictions')  # Заголовок графика
    plt.xlabel('Input Feature')  # Метка оси X
    plt.ylabel('Output Value')  # Метка оси Y
    plt.grid()  # Добавление сетки
    plt.show()  # Отображение графика
              


from sklearn.datasets import make_regression


X, y, coef = make_regression(n_features=4, n_informative=4, noise=10, coef=True, bias=0.5)


X = torch.from_numpy(X).to(dtype=torch.float32)
y = torch.from_numpy(y).to(dtype=torch.float32).view(-1, 1)


model = Model()
loss_fn = MSE()


losses = train(model, loss_fn, X, y, lr=0.01, epochs=1000)


plot_loss(losses)
plot_predictions(X, y, model)
              


class Linear():
    def __init__(self,n_f,n_n):
        self.weights = torch.randn(n_f,n_n, requires_grad=True)
        self.bias = torch.randn(1, n_n, requires_grad=True)
    def __call__(self, inputs: torch.Tensor):
        output = inputs @ self.weights + self.bias
        return output
class MSELoss:
    def __call__(self,
                 y_pred: torch.Tensor,
                 y_true: torch.Tensor):
        return torch.mean((y_true - y_pred) ** 2)
class Relu:
    def __call__(self,x):
        x[x<0]=0
        return x
              


import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np

# Создание синтетического датасета
X = torch.linspace(0, 1, 100).view(-1, 1)  # 100 примеров, 1 признак
y = torch.sin(2 * np.pi * X) + 0.1 * torch.randn(X.size())  # Целевые значения с добавлением шума

# Определение модели
class RegressionModel(nn.Module):
    def __init__(self):
        super(RegressionModel, self).__init__()
        self.fc1 = nn.Linear(1, 20)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(20, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Инициализация модели, функции потерь и оптимизатора
model = RegressionModel()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Списки для хранения значений потерь
losses = []
epochs = 2000  # Количество эпох

# Обучение модели
for epoch in range(epochs):
    model.train()  # Установка модели в режим обучения
    optimizer.zero_grad()  # Обнуление градиентов

    # Прямой проход
    y_pred = model(X)

    # Вычисление потерь
    loss = criterion(y_pred, y)
    losses.append(loss.item())  # Сохранение потерь

    # Обратный проход и обновление параметров
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:  # Вывод информации каждые 100 эпох
        print(f'Epoch {epoch}, Loss: {loss.item()}')

# Визуализация потерь
plt.figure(figsize=(10, 5))
plt.plot(losses, label='Training Loss')
plt.title('Loss per Epoch')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Визуализация предсказанных значений
model.eval()  # Установка модели в режим оценки
with torch.no_grad():
    y_pred = model(X)

plt.figure(figsize=(10, 5))
plt.scatter(X.numpy(), y.numpy(), label='True Data', color='blue')
plt.scatter(X.numpy(), y_pred.numpy(), label='Predicted Data', color='red')
plt.title('True vs Predicted Data')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
    ''')
    elif st == '3.2':
        print('''
import torch.optim as optim
import torch.nn as nn
              
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# Пример данных
X = torch.randn(100, 4)  # 100 примеров с 4 признаками
y = torch.randn(100, 1)  # 100 истинных значений

# Определяем модель
model = nn.Sequential(
    nn.Linear(4, 20),  # Изменили на 4, так как входные данные имеют 4 признака
    nn.ReLU(),
    nn.Linear(20, 10),
    nn.ReLU(),
    nn.Linear(10, 1)
)

# Оптимизатор и функция потерь
optim = torch.optim.SGD(model.parameters(), lr=0.01)
criterion = nn.MSELoss()

# Список для хранения потерь
los = []

# Цикл обучения
for epoch in range(20000):
    # Прямой проход (предсказание)
    y_pred = model(X)

    # Вычисление потерь
    loss = criterion(y_pred, y)

    # Обратное распространение
    loss.backward()

    # Шаг оптимизации
    optim.step()

    # Обнуление градиентов
    optim.zero_grad()

    # Запоминаем потери для графика
    los.append(loss.item())

    # Выводим информацию каждые 100 эпох
    if epoch % 100 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')

# Построение графика функции потерь
plt.plot(los)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss over Time')
plt.show()

# Предсказание на тех же данных для визуализации
with torch.no_grad():
    predicted = model(X)

# Визуализация данных и предсказаний
plt.scatter(X[:, 0].numpy(), y.numpy(), label='True Data')
plt.scatter(X[:, 0].numpy(), predicted.numpy(), label='Predictions', color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.title('True Data and Model Predictions')
plt.legend()
plt.show()
''')
    elif st == '3.2.1':
        print('''
class Neuron:


  def __init__(self, n_inputs: int):
    self.weights = torch.randn(n_inputs, 1, requires_grad = True)
    self.bias = torch.randn(1, 1, requires_grad = True)

  def __call__(self, inputs: torch.Tensor):
    output = inputs @ self.weights + self.bias
    return output


class SquaredLoss:

  def __call__(self, y_pred: torch.Tensor, y_true: torch.Tensor):
    return ((y_pred - y_true) ** 2).mean()
              

X, y, coef = make_regression(n_features=4, n_informative=4, coef=True, bias=0.5)
X = torch.from_numpy(X).to(dtype=torch.float32)
y = torch.from_numpy(y).to(dtype=torch.float32).view(-1, 1)
              

def train(model, loss_fn, X, y, epochs= 10000, lr = 0.01):
  optimizer = torch.optim.SGD([model.weights, model.bias], lr = lr)


  for epoch in range(epochs):

    pred = model(X)

    loss = loss_fn(pred, y)

    loss.backward()

    optimizer.step()

    optimizer.zero_grad()

    if epoch % 100 == 0:
      print(f'epoch {epoch}, loss {loss}')
              

neuron = Neuron(n_inputs = X.shape[1])
loss_fn = SquaredLoss()

train(neuron, loss_fn, X, y, epochs = 1000, lr = 0.01)
    ''')
    elif st == '3.2.2':
        print('''
X, y, coef = make_regression(n_features=1, n_informative=1, noise=10, coef=True, bias=0.5)
X = torch.from_numpy(X).float()
y = torch.from_numpy(y).float().view(-1, 1)
              
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt


class RegressionModel(nn.Module):
    def __init__(self):
        super(RegressionModel, self).__init__()
        self.fc1 = nn.Linear(1, 20)
        self.fc2 = nn.Linear(20, 10)
        self.fc3 = nn.Linear(10, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x


model = RegressionModel()


criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)



losses = []

for epoch in range(1000):
    y_pred = model(X)

    loss = criterion(y_pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()



    losses.append(loss.item())

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item()}")


plt.plot(losses)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss over Time')
plt.show()


with torch.no_grad():
    predicted = model(X)

plt.scatter(X.numpy(), y.numpy(), label='True Data')
plt.plot(X.numpy(), predicted.numpy(), label='Predictions', color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.title('True Data and Model Predictions')
plt.legend()
plt.show()
    ''')
    elif st == '3.3.1':
        print('''
import torch.nn as nn              

class mymodel(nn.Module):
    def __init__(self,n_f):
        super(mymodel,self).__init__()
        self.fc1= nn.Linear(n_f,20)
        self.fc12= nn.Linear(20,30)
        self.fc2= nn.Linear(30,1)
        self.relu = nn.ReLU()
    def __call__(self,x):
        return self.fc2(self.relu(self.fc12(self.relu(self.fc1(x)))))
              
X = torch.linspace(0, 1, 100).view(-1, 1)
y = torch.sin(2 * np.pi * X) + 0.1 * torch.rand(X.size())
              
import torch.optim as optim
              

# my= mymodel(1)
my = nn.Sequential(
                nn.Linear(X.shape[1], 20),
                nn.ReLU(),
                nn.Linear(20, 30),
                nn.ReLU(),
                nn.Linear(30, 1))
opt= optim.SGD(my.parameters(),lr=0.01)
criterion = nn.MSELoss()
los = []

for epoch in range(20000):
        y_pred = my(X)
        loss = criterion(y_pred, y)
        loss.backward()
        opt.step()
        opt.zero_grad()
        los.append(loss.item())
        if epoch % 1000 == 0:
            print(f"Epoch: {epoch} | Loss: {loss.item()}")
              

plt.plot(X.detach(),y_pred.detach())
plt.scatter(X, y,color="r");
    ''')
    elif st == '3.3.2':
        print('''
X = torch.linspace(0, 1, 100).view(-1, 1)
y = torch.sin(2 * np.pi * X) + 0.1 * torch.rand(X.size())
              

model = nn.Sequential(
    nn.Linear(1, 20),
    nn.ReLU(),
    nn.Linear(20, 10),
    nn.ReLU(),
    nn.Linear(10, 1)
)


criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr = 0.01)


losses = []
epochs = 2000


for epoch in range(epochs):
  y_pred = model(X)

  loss = criterion(y_pred, y)

  optimizer.zero_grad()
  loss.backward()
  optimizer.step()


  losses.append(loss.item())

if epoch % 100 == 0:
  print(f'epoch {epoch}, loss {loss}')



plt.plot(losses)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss over time')
plt.show()

# Визуализация предсказанных значений и исходных данных
with torch.no_grad():  # Отключение градиентов для визуализации
    predicted = model(X)

# Построение графика предсказанных значений и исходных данных
plt.scatter(X.numpy(), y.numpy(), label='True Data')
plt.plot(X.numpy(), predicted.numpy(), label='Predictions', color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.title('True Data and Model Predictions')
plt.legend()
plt.show()
    ''')
    elif st == '3.4':
        print('''
from torch.utils.data import Dataset, DataLoader, TensorDataset
import numpy as np
              
X = torch.linspace(0, 1, 100).view(-1, 1)
y = torch.sin(2 * np.pi * X) + 0.1 * torch.rand(X.size())

dataset = TensorDataset(X, y)
dataloader= DataLoader(dataset,20,shuffle=True)
              

my = nn.Sequential(
                nn.Linear(X.shape[1], 20),
                nn.ReLU(),
                nn.Linear(20, 30),
                nn.ReLU(),
                nn.Linear(30, 1))
opt= optim.SGD(my.parameters(),lr=0.01)
criterion = nn.MSELoss()
los = []

for epoch in range(1000):
        for i, (x, y_) in enumerate(dataloader):
            y_pred = my(x)
            loss = criterion(y_pred, y_)
            loss.backward()
            opt.step()
            opt.zero_grad()
            los.append(loss.item())
            print(f"epoch {epoch}--Batch {i}: Loss: {loss.item()}")
            # if epoch % 1000 == 0:
            #     print(f"Epoch: {epoch} | Loss: {loss.item()}")
''')
    elif st == '3.4.1':
        print('''
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
import matplotlib.pyplot as plt


class SinusoidalDataset(Dataset):
    def __init__(self):
        self.X = torch.linspace(0, 1, 100).view(-1, 1)
        self.y = torch.sin(2 * np.pi * self.X) + 0.1 * torch.rand(self.X.size())

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]



batch_size = 10
dataset = SinusoidalDataset()
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)



model = nn.Sequential(
    nn.Linear(1, 20),
    nn.ReLU(),
    nn.Linear(20, 10),
    nn.ReLU(),
    nn.Linear(10, 1)
)


criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)



losses = []
epochs = 2000


for epoch in range(epochs):
    epoch_loss = 0.0  #для сохранения общей потери за эпоху

    for batch_X, batch_y in dataloader:
        y_pred = model(batch_X)


        loss = criterion(y_pred, batch_y)


        optimizer.zero_grad()
        loss.backward()
        optimizer.step()


        epoch_loss += loss.item() #потери за каждый батч


    epoch_loss / len(dataloader)
    losses.append(epoch_loss)


    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {epoch_loss:.4f}')


plt.plot(losses)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss over epochs')
plt.show()


with torch.no_grad():
    predicted = model(dataset.X)


plt.scatter(dataset.X.numpy(), dataset.y.numpy(), label='True Data')
plt.plot(dataset.X.numpy(), predicted.numpy(), label='Predictions', color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.title('True Data and Model Predictions')
plt.legend()
plt.show()
    ''')
    elif st == '3.4.2.1':
        print('''
import pandas as pd
import torch
              
df = pd.read_csv('/content/diamonds.csv')
df
              
df_num = df.select_dtypes(['float64', 'int64'])
df_num
              
y = df_num['price'].values
y
              

X = df_num.drop(columns = ['price']).values
X
              

X_tens = torch.tensor(X, dtype = torch.float32)
y_tens = torch.tensor(y, dtype = torch.float32).view(-1, 1)
X_tens, y_tens
              

X_tens.size()
              

y_tens.size()
    ''')
    elif st == '3.4.2.2':
        print('''
from torch.utils.data import random_split
              
train_size = int(0.8 * len(df))
test_size = len(dataset) - train_size

train_df, test_df = random_split(dataset, [train_size, test_size])
    ''')
    elif st == '3.4.2.3':
        print('''
model = nn.Sequential(
    nn.Linear(1, 128),  # почему x.shape[1] не работает
    nn.ReLU(),
    nn.Linear(128, 64),
    nn.ReLU(),
    nn.Linear(64, 1)
)




batch_size = 256
train_loader = DataLoader(train_df, batch_size = batch_size, shuffle = True)
test_loader = DataLoader(test_df, batch_size = batch_size, shuffle = False)


criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr = 0.01)


losses = []
epochs = 100


for epoch in range(epochs):
    running_loss = 0.0
    for batch_X, batch_y in train_loader:
        optimizer.zero_grad()
        y_pred = model(batch_X)
        loss = criterion(y_pred, batch_y)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    avg_loss = running_loss / len(train_loader)
    losses.append(avg_loss)

    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {avg_loss}')
    ''')
    elif st == '3.4.3':
        print('''
from torch.utils.data import Dataset


class DropColsTransform:
    def __call__(self, df):
        return df.select_dtypes(include=[float, int])


class ToTensorTransform:
    def __call__(self, df):
        return torch.tensor(df.values, dtype=torch.float32)


class MyDataset(Dataset):
    def __init__(self, df, transform=None):
        if transform:
            df = transform(df)
        self.df = df


    def __len__(self):
        return len(self.df)


    def __getitem__(self, idx):
        data = self.df.iloc[idx] #извлечение данных

        X = data.drop('price').values
        y = data['price']

        return torch.tensor(X, dtype=torch.float32), torch.tensor(y, dtype=torch.float32)


drop_transform = DropColsTransform()
to_tensor_transform = ToTensorTransform()
dataset = MyDataset(df, transform=drop_transform)



for idx in range(5):
    x, y = dataset[idx]
    print(f'Features: {x}, Target: {y}')

    ''')
    elif st == '3.4.2.4':
        print('''
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import TensorDataset

# Загрузка и подготовка данных

dataset = df.select_dtypes(include=[np.number])  # Удаление нечисловых столбцов

# Проверяем длину исходного набора данных
print(f'Length of original dataset: {len(dataset)}')

X = dataset.drop('price', axis=1).values  # Все столбцы, кроме 'price'
y = dataset['price'].values  # Целевой столбец

# Разделение на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание TensorDataset
train_df = TensorDataset(torch.FloatTensor(X_train), torch.FloatTensor(y_train))
test_df = TensorDataset(torch.FloatTensor(X_test), torch.FloatTensor(y_test))

# Проверяем длину обучающего и тестового наборов
print(f'Length of train dataset: {len(train_df)}')
print(f'Length of test dataset: {len(test_df)}')

              

print(f'Length of train dataset: {len(train_df)}')
print(f'Length of test dataset: {len(test_df)}')
              


from torch.utils.data import DataLoader

batch_size = 256
train_loader = DataLoader(train_df, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_df, batch_size=batch_size, shuffle=False)
              

import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score  # для вычисления R^2

model = nn.Sequential(
    nn.Linear(X.shape[1], 128),  # Убедитесь, что размер входа соответствует количеству признаков
    nn.ReLU(),
    nn.Linear(128, 64),
    nn.ReLU(),
    nn.Linear(64, 1)
)

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

epochs = 100
train_losses = []
test_losses = []

for epoch in range(epochs):
    run_loss = 0.0
    model.train()

    for batch_X, batch_y in train_loader:
        optimizer.zero_grad()
        y_pred = model(batch_X)
        loss = criterion(y_pred, batch_y)
        loss.backward()
        optimizer.step()

        run_loss += loss.item()

    average_train_loss = run_loss / len(train_loader)
    train_losses.append(average_train_loss)

    model.eval()
    test_loss = 0.0

    all_preds = []  # Список для сохранения всех предсказанных значений на тестовом наборе
    all_targets = []  # Список для сохранения всех истинных значений на тестовом наборе

    with torch.no_grad():
        for batch_X, batch_y in test_loader:
            y_pred = model(batch_X)
            loss = criterion(y_pred, batch_y)
            test_loss += loss.item()

            all_preds.append(y_pred)
            all_targets.append(batch_y)

    average_test_loss = test_loss / len(test_loader)
    test_losses.append(average_test_loss)

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Train Loss: {average_train_loss:.4f}, Test Loss: {average_test_loss:.4f}")

# Построение графика функции потерь
plt.figure(figsize=(10, 5))
plt.plot(train_losses, label='Train Loss')
plt.plot(test_losses, label='Test Loss')
plt.title('Train and Test Loss per Epoch')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Рассчитаем R^2
# Объединим все батчи в один тензор
all_preds = torch.cat(all_preds).cpu().numpy()  # Предсказанные значения
all_targets = torch.cat(all_targets).cpu().numpy()  # Истинные значения

# Вычисляем R^2
r2 = r2_score(all_targets, all_preds)
print(f'R^2 on test set: {r2:.4f}')

              


from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from torch.utils.data import DataLoader, TensorDataset

batch_size = 256
train_loader = DataLoader(train_df, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_df, batch_size=batch_size, shuffle=False)

# Нормализация X и y
scaler_X = StandardScaler()
scaler_y = StandardScaler()

X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y.reshape(-1, 1))  # y в форме (n_samples, 1)

# Создание TensorDataset и DataLoader
train_dataset = TensorDataset(torch.tensor(X_scaled, dtype=torch.float32), torch.tensor(y_scaled, dtype=torch.float32))
test_dataset = TensorDataset(torch.tensor(X_scaled, dtype=torch.float32), torch.tensor(y_scaled, dtype=torch.float32))

train_loader = DataLoader(train_dataset, batch_size=256, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=256, shuffle=False)

# Модель
model = nn.Sequential(
    nn.Linear(X_scaled.shape[1], 128),
    nn.ReLU(),
    nn.Linear(128, 64),
    nn.ReLU(),
    nn.Linear(64, 1)  # Последний слой должен выдавать одно предсказание для каждого объекта
)

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

epochs = 100
train_losses = []
test_losses = []

# Тренировка модели
for epoch in range(epochs):
    run_loss = 0.0
    model.train()

    for batch_X, batch_y in train_loader:
        optimizer.zero_grad()
        y_pred = model(batch_X)
        y_pred = y_pred.view(-1)  # Преобразуем предсказания в одномерный вектор
        batch_y = batch_y.view(-1)  # Преобразуем целевые значения в одномерный вектор
        loss = criterion(y_pred, batch_y)
        loss.backward()
        optimizer.step()
        run_loss += loss.item()

    average_train_loss = run_loss / len(train_loader)
    train_losses.append(average_train_loss)

    model.eval()
    test_loss = 0.0
    all_preds = []
    all_targets = []

    with torch.no_grad():
        for batch_X, batch_y in test_loader:
            y_pred = model(batch_X)
            y_pred = y_pred.view(-1)  # Преобразуем предсказания в одномерный вектор
            batch_y = batch_y.view(-1)  # Преобразуем целевые значения в одномерный вектор
            loss = criterion(y_pred, batch_y)
            test_loss += loss.item()
            all_preds.append(y_pred)
            all_targets.append(batch_y)

    average_test_loss = test_loss / len(test_loader)
    test_losses.append(average_test_loss)

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Train Loss: {average_train_loss:.4f}, Test Loss: {average_test_loss:.4f}")

# График ошибки по эпохам
plt.figure(figsize=(10, 5))
plt.plot(train_losses, label='Train Loss')
plt.plot(test_losses, label='Test Loss')
plt.title('Train and Test Loss per Epoch')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Объединение всех предсказаний и истинных значений в один массив
all_preds = torch.cat(all_preds).cpu().numpy()
all_targets = torch.cat(all_targets).cpu().numpy()

# Восстановление предсказанных и целевых значений в исходный масштаб
all_preds_rescaled = scaler_y.inverse_transform(all_preds.reshape(-1, 1))  # Преобразуем в форму (n_samples, 1)
all_targets_rescaled = scaler_y.inverse_transform(all_targets.reshape(-1, 1))


r2 = r2_score(all_targets_rescaled, all_preds_rescaled)
print(f'R^2 on test set: {r2:.4f}')
              


plt.figure(figsize=(10, 5))
plt.scatter(all_targets_rescaled, all_preds_rescaled, alpha=0.5, label='Предсказанные значения')
plt.plot([all_targets_rescaled.min(), all_targets_rescaled.max()],
         [all_targets_rescaled.min(), all_targets_rescaled.max()],
         'r--', linewidth=2, label='Идеальное предсказание (y=x)')
plt.title('Истинные значения vs Предсказанные значения')
plt.xlabel('Истинные значения')
plt.ylabel('Предсказанные значения')
plt.legend()
plt.show()
    ''')
        
def cnnClas_info():
    print('''
ЧТОБЫ ВЫЗВАТЬ КОД: используйте DL.cnnClas_code("НОМЕР ЗАДАНИЯ")
          
1. Создайте датасет CatBreeds на основе данных из архива cat_breeds_4.zip. 
Используя преобразования torchvision, приведите картинки к размеру 300х300 и нормализуйте значения интенсивности пикселей 
(рассчитайте статистику для нормализации отдельно). 
Выведите на экран количество картинок в датасете, размер одной картинки, количество уникальных классов. 
Разбейте датасет на обучающее и тестовое множество в соотношении 80 на 20%.
          
2. Решите задачу классификации на основе датасета из предыдущего задания, не используя сверточные слои. 
Постройте график изменения значения функции потерь на обучающем множестве в зависимости от номера эпохи, 
графики изменения метрики accuracy на обучающем и тестовом множестве в зависимости от эпохи. 
Выведите на экран итоговое значение метрики accuracy на обучающем и тестовом множестве. Выведите на экран количество параметров модели.
          
3. Напишите функцию, которая выбирает несколько изображений из переданного набора данных и выводит их на экран в виде сетки с указанием над 
ними названия правильного класса и класса, предсказанного моделью. 
Воспользовавшись данной функцией, выведите прогнозы итоговой модели из предыдущей задачи по 6 случайным картинкам.
          
4. Решите задачу классификации на основе датасета из первого задания, используя сверточные слои. 
Постройте график изменения значения функции потерь на обучающем множестве в зависимости от номера эпохи, графики изменения метрики 
accuracy на обучающем и тестовом множестве в зависимости от эпохи. 
Выведите на экран итоговое значение метрики accuracy на обучающем и тестовом множестве. 
Выведите на экран количество параметров модели.
Воспользовавшись функцией из предыдущего задания, выведите прогнозы итоговой модели по 6 случайным картинкам.
          
5. Проанализируйте обученную в предыдущей задаче модель, исследовав обученные ядра сверточных слоев. 
Выберите одно изображение из тестового набора данных и пропустите через первый сверточный слой модели. 
Визуализируйте полученные карты признаков.
''')
    
def cnnClas_code(st):
    if st == '1':
        print('''
!unzip cat_breeds_4.zip
              

zip_file_path = '/content/cat_breeds_4.zip'
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall()  # Распаковываем архив
              

transform = transforms.Compose([
    transforms.Resize((300, 300)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  #значения пикселей [-1, 1]
])
              

dataset = ImageFolder(root = 'cat_breeds_4', transform = transform)
dataset
              

num_images = len(dataset)
num_images
              

image_size = dataset[0][0].size()
image_size
              

num_classes = len(dataset.classes) #количество папок
num_classes
              

train_size = int(0.8 * num_images)
test_size = num_images - train_size
              
train_dataset, test_dataset = random_split(dataset, [train_size, test_size]) #рандомно делим датасет на тест и обуч
              
len(train_dataset)
              
len(test_dataset)
''')
    elif st == '2':
        print('''
train_loader = DataLoader(train_dataset, batch_size = 32, shuffle = True)
test_loader = DataLoader(test_dataset, batch_size = 32, shuffle = False)
              
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
              

#Архитектура модели + количество параметров
              
class CNN(nn.Module):
  def __init__(self, num_classes):
    super(CNN, self).__init__()

    self.flatten = nn.Flatten() #изображение в вектор

    self.fc1 = nn.Linear(3 * 300 * 300, 1024)

    self.bn1 = nn.BatchNorm1d(1024)

    self.fc2 = nn.Linear(1024, 256)

    self.bn2 = nn.BatchNorm1d(256)

    self.fc3 = nn.Linear(256, 64)

    self.dropout = nn.Dropout(0.5)

    self.fc4 = nn.Linear(64, num_classes)


  def forward(self, x):

    x = self.flatten(x)

    x = torch.relu(self.bn1(self.fc1(x)))

    x = torch.relu(self.bn2(self.fc2(x)))

    x = torch.relu(self.fc3(x))

    x = self.dropout(x)

    x = self.fc4(x)

    return x

num_classes = len(dataset.classes)
model = CNN(num_classes).to(device)
              
num_params = sum(p.numel() for p in model.parameters())
num_params
              

#Обучение модели
              
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr = 0.001)
              

def train(model, loader, optimizer, criterion):
    model.train()
    total_loss, correct = 0, 0

    for images, labels in loader:

        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()  #backpropogation накапливает градиенты => cбрасываем, чтоб градиенты не смешивались между батчами

        outputs = model(images)  #forward pass (predictions)

        loss = criterion(outputs, labels)  #отличие предсказаний модели от исходных меток

        loss.backward()

        optimizer.step()

        total_loss += loss.item()  #потери текущего батча
        correct += (outputs.argmax(1) == labels).sum().item()

    avg_loss = total_loss / len(loader)
    accuracy = correct / len(loader.dataset)  #точность на обучающем множестве
    return avg_loss, accuracy


def evaluate(model, loader, criterion):
  model.eval()

  total_loss, correct = 0, 0

  with torch.no_grad():
    for images, labels in loader:

      images, labels = images.to(device), labels.to(device)

      outputs = model(images)

      loss = criterion(outputs, labels)

      total_loss += loss.item()
      correct += (outputs.argmax(1) == labels).sum().item() #подсчет правильных предсказаний

  avg_loss = total_loss / len(loader)
  accuracy = correct / len(loader.dataset)
  return avg_loss, accuracy
              
#with torch.no_grad() отключает подсчет градиентов для снижения время обучения и объема памяти
#train() - обучает модель = ОБНОВЛЯЕТ ВЕСА (тут включается dropout, он обнуляет рандомно часть нейронов)
#eval() - оцениваем, насколько хорошо работает модель на тестовом множестве(отключает dropout для более лучших результатов), не обновляет веса
              
epochs = 10
train_losses, test_losses = [], []
train_accuracies, test_accuracies = [], []
for epoch in range(epochs):

    train_loss, train_acc = train(model, train_loader, optimizer, criterion)
    test_loss, test_acc = evaluate(model, test_loader, criterion)

    train_losses.append(train_loss)
    test_losses.append(test_loss)
    train_accuracies.append(train_acc)
    test_accuracies.append(test_acc)

    print(f"Эпоха {epoch+1}/{epochs}, "
          f"Потеря: {train_loss:.4f}, Точность: {train_acc:.4f}, "
          f"Тестовая точность: {test_acc:.4f}")
''')
    elif st == '3':
        print('''
def show_examples(model, subset, original_dataset, k=6):
    model.eval()

    indices = np.random.choice(len(subset), k, replace=False)

    fig, axes = plt.subplots(1, k, figsize=(15, 5))

    with torch.no_grad():
        for i, idx in enumerate(indices):
            image, label = subset[idx]
            output = model(image.unsqueeze(0).to(device))
            predicted_label = output.argmax(1).item()

            #меняем формат изображения для Matplotlib (CHW -> HWC)
            axes[i].imshow(image.permute(1, 2, 0).numpy())
            axes[i].axis('off')

            true_class = original_dataset.classes[label]
            pred_class = original_dataset.classes[predicted_label]
            axes[i].set_title(f'True: {true_class}\nPred: {pred_class}', fontsize=10)

    plt.show()
              

show_examples(model, test_dataset, dataset, k=6)
''')
    elif st == '4':
        print('''
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
              
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])
              

dataset = ImageFolder(root='cat_breeds_4', transform=transform)
              

train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])
              

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
              

#Архитектура модели
              
class CNN(nn.Module):
    def __init__(self, num_classes):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(32 * 56 * 56, 64)
        self.fc2 = nn.Linear(64, num_classes)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)


        x = x.view(x.size(0), -1) #flatten
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

#на входе 224, затем два пулинг слоя -> 56, out_channels = 16 , out_channels = 32
              

num_classes = len(dataset.classes)
model = CNN(num_classes)
              

optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()
              

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)
              

#Обучение модели
              
def train(model, loader, optimizer, criterion):
    model.train()
    total_loss, correct = 0, 0
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()


        total_loss += loss.item()
        correct += (outputs.argmax(1) == labels).sum().item()

    avg_loss = total_loss / len(loader)
    accuracy = correct / len(loader.dataset)
    return avg_loss, accuracy

def evaluate(model, loader, criterion):
    model.eval()
    total_loss, correct = 0, 0
    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)
            total_loss += loss.item()
            correct += (outputs.argmax(1) == labels).sum().item()

    avg_loss = total_loss / len(loader)
    accuracy = correct / len(loader.dataset)
    return avg_loss, accuracy
              

#Обучение + оценка
              
epochs = 10
train_losses, test_losses = [], []
train_accuracies, test_accuracies = [], []

for epoch in range(epochs):
    train_loss, train_acc = train(model, train_loader, optimizer, criterion)
    test_loss, test_acc = evaluate(model, test_loader, criterion)


    train_losses.append(train_loss)
    test_losses.append(test_loss)
    train_accuracies.append(train_acc)
    test_accuracies.append(test_acc)

    print(f"Эпоха {epoch + 1}/{epochs}, Потеря: {train_loss:.4f}, "
          f"Точность: {train_acc:.4f}, Тестовая точность: {test_acc:.4f}")
              

#Точность + вывод
train_accuracies[-1]
              
test_accuracies[-1]
              
num_params = sum(p.numel() for p in model.parameters())
num_params
              

# Визуализация результатов
              
def show_examples(model, dataset, k=6):
    model.eval()
    indices = random.sample(range(len(dataset)), k)
    images, labels = zip(*[dataset[i] for i in indices])

    #изображения в тензоры
    images = torch.stack(images).to(device)

    with torch.no_grad():
        outputs = model(images)
        _, preds = torch.max(outputs, 1)


    plt.figure(figsize=(10, 10))
    for i in range(k):
        plt.subplot(3, 2, i + 1)
        plt.imshow(np.transpose(images[i].cpu().numpy(), (1, 2, 0)))
        plt.title(f'Правильный класс: {dataset.classes[labels[i]]}\nПредсказанный класс: {dataset.classes[preds[i]]}')
        plt.axis('off')
    plt.show()
              
show_examples(model, dataset, k=6)
''')
    elif st == '5':
        print('''
model.to(device)
              
def visualize_feature_maps(model, image):
    image = image.unsqueeze(0).to(device)


    conv1 = model.conv1


    with torch.no_grad():
        feature_maps = conv1(image)


    feature_maps = feature_maps.cpu()


    num_feature_maps = feature_maps.shape[1]


    plt.figure(figsize=(15, 15))
    for i in range(num_feature_maps):
        plt.subplot(4, 4, i + 1)
        plt.imshow(feature_maps[0, i].numpy(), cmap='gray')
        plt.axis('off')
        plt.title(f'Feature Map {i+1}')
    plt.show()
              

image, label = test_dataset[random.randint(0, len(test_dataset) - 1)]  #случайное изображение
visualize_feature_maps(model, image)
''')

def cnnPre_info():
    print('''
ЧТОБЫ ВЫЗВАТЬ КОД: используйте DL.cnnPre_code("НОМЕР ЗАДАНИЯ")
          
1. Используя реализацию из torchvision, cоздайте модель vgg16 и загрузите предобученные веса IMAGENET1K_V1. 
Выведите на экран структуру модели, количество слоев и количество настраиваемых (requires_grad==True) параметров модели.
          
2. Создайте датасет CatBreeds на основе данных из архива cat_breeds_4.zip. Разбейте датасет на обучающее и тестовое множество в соотношении 80 на 20%.
К обучающему датасету примените следующее преобразование: приведите картинки к размеру 256x256, 
затем обрежьте по центру с размером 224х224, затем переведите изображения в тензор и нормализуйте значения интенсивности пикселей 
(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)).
К тестовому датасету примените преобразование VGG16_Weights.IMAGENET1K_V1.transforms.
          
3. Заморозьте все веса модели из предыдущего задания. Замените последний слой Linear классификатора на новый слой, соответствующий задаче. 
После изменения последнего слоя выведите на экран количество настраиваемых (requires_grad==True) параметров модели. 
Решите задачу, используя модель с замороженными весами и изменнным последним слоем.
Постройте график изменения значения функции потерь на обучающем множестве в зависимости от номера эпохи, 
графики изменения метрики accuracy на обучающем и тестовом множестве в зависимости от эпохи. 
Выведите на экран итоговое значение метрики accuracy на обучающем и тестовом множестве.
          
4. Повторите решение предыдущей задачи, заморозив все сверточные слои, кроме последнего (слои классификатора не замораживайте). 
Сравните качество полученного решения и решения из предыдущей задачи, а также время, затраченное на обучения моделей. 
Перед началом работы создайте модель заново.
          
5. Повторите решение задачи 3, расширив обучающий набор данных при помощи преобразований из torchvision, изменяющих изображение 
(повороты, изменение интенсивности пикселей, обрезание и т.д.). 
При оценке модели на тестовой выборке данные преобразования применяться не должны. 
Решение о том, сколько и каких слоев модели будет обучаться, примите самостоятельно. 
Перед началом работы создайте модель заново.
''')
def cnnPre_code(st):
    print('''
import torch
from torchvision import models
import os
import zipfile
import torch
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader, random_split
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import time
''')
    if st == '1':
        print('''
model = models.vgg16(weights=models.VGG16_Weights.IMAGENET1K_V1)
              
model
              
num_layers = len(list(model.features)) + len(list(model.classifier))
num_layers
              
num_train_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
num_train_params
''')
    elif st == '2':
        print('''
zip_file_path = '/content/cat_breeds_4.zip'
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall()
              
extracted_dir = '/content/cat_breeds_4'
              
train_transforms = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))
])
              
test_transforms = models.VGG16_Weights.IMAGENET1K_V1.transforms()
              
data_dir = extracted_dir
              
#готовый датасет
full_dataset = datasets.ImageFolder(root = data_dir, transform = train_transforms)
              
train_size = int(0.8 * len(full_dataset))
test_size = len(full_dataset) - train_size
train_dataset, test_dataset = random_split(full_dataset, [train_size, test_size])
              
test_dataset.dataset.transforms = test_transforms #переопределяем преобразования
              
train_loader = DataLoader(train_dataset, batch_size = 32, shuffle = True)
test_loader = DataLoader(test_dataset, batch_size = 32, shuffle = False)
              
model = models.vgg16(weights=models.VGG16_Weights.IMAGENET1K_V1)
model = model.to(DEVICE)
#загрузка предобученной модели VGG16
              
len(train_dataset)
              
len(test_dataset)
''')
    elif st == '3':
        print('''
#заморозка всех параметров
for param in model.parameters():
  param.requires_grad = False #отключение автоматического дифференцирования
              
num_classes = len(train_dataset.dataset.classes) #меняем последний слой классификатора
model.classifier[6] = nn.Linear(4096, num_classes) #меняем последний слой с нужным числом ыходов
#4096 - количество нейронов в классификаторе
#VGG16 обучалась на датасете ImageNet, где 1000 классов, поэтому последний слой в оригинальной модели — nn.Linear(4096, 1000)
              
num_trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
num_trainable_params
              
model = model.to(DEVICE)
              
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.classifier[6].parameters(), lr = 0.001)
              
epochs = 10
train_loss_history = []
train_acc_history = []
test_acc_history = []

def calculate_accuracy(loader, model):
    correct = 0
    total = 0
    model.eval()
    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(DEVICE), labels.to(DEVICE)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    return correct / total
              

train_loss_history = []
train_acc_history = []
test_acc_history = []

for epoch in range(epochs):
    model.train()
    running_loss = 0.0
    correct_train = 0
    total_train = 0

    for images, labels in train_loader:
        images, labels = images.to(DEVICE), labels.to(DEVICE)


        outputs = model(images) #forward
        loss = criterion(outputs, labels)


        optimizer.zero_grad() #backward
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        total_train += labels.size(0)
        correct_train += (predicted == labels).sum().item()


    train_loss_history.append(running_loss / len(train_loader))
    train_acc = correct_train / total_train
    train_acc_history.append(train_acc)


    test_acc = calculate_accuracy(test_loader, model)
    test_acc_history.append(test_acc)

    print(f"Эпоха [{epoch + 1}/{epochs}], Потери: {running_loss / len(train_loader):.4f}, Точность на обучении: {train_acc:.4f}, Точность на тесте: {test_acc:.4f}")

              
plt.figure(figsize=(10, 5))
plt.plot(range(1, epochs + 1), train_loss_history, label="Train Loss")
plt.xlabel("Эпоха")
plt.ylabel("Функция потерь")
plt.title("Изменение функции потерь на обучающем множестве")
plt.legend()
plt.show()
              

plt.figure(figsize=(10, 5))
plt.plot(range(1, epochs + 1), train_acc_history, label="Train Accuracy")
plt.plot(range(1, epochs + 1), test_acc_history, label="Test Accuracy")
plt.xlabel("Эпоха")
plt.ylabel("Точность")
plt.title("Изменение точности (accuracy) на обучающем и тестовом множествах")
plt.legend()
plt.show()
              
train_acc_history[-1]
              
test_acc_history[-1]
''')
    elif st == '4':
        print('''
from torchvision import models
vgg16 = models.vgg16(weights="IMAGENET1K_V1")
print(vgg16.features)
              
model = models.vgg16(weights=models.VGG16_Weights.IMAGENET1K_V1)
              
for name, param in model.features.named_parameters():
    if "28" not in name:
        param.requires_grad = False
              
for param in model.classifier.parameters(): #классификатор обучаемый
    param.requires_grad = True
              
num_classes = len(train_dataset.dataset.classes) #последний слой заменяем на новый
model.classifier[6] = nn.Linear(4096, num_classes)
              
model = model.to(DEVICE)
              
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(filter(lambda p: p.requires_grad, model.parameters()), lr=0.001)
              
#Подсчет точности
              
epochs = 10
train_loss_history = []
train_acc_history = []
test_acc_history = []

start_time = time.time()

def calculate_accuracy(loader, model):
    correct = 0
    total = 0
    model.eval()
    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(DEVICE), labels.to(DEVICE)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    return correct / total
              
for epoch in range(epochs):
    model.train()
    running_loss = 0.0
    correct_train = 0
    total_train = 0

    for images, labels in train_loader:
        images, labels = images.to(DEVICE), labels.to(DEVICE)


        outputs = model(images) #forward
        loss = criterion(outputs, labels)


        optimizer.zero_grad() #backward
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        total_train += labels.size(0)
        correct_train += (predicted == labels).sum().item()


    train_loss_history.append(running_loss / len(train_loader))
    train_acc = correct_train / total_train
    train_acc_history.append(train_acc)


    test_acc = calculate_accuracy(test_loader, model)
    test_acc_history.append(test_acc)

    print(f"Эпоха [{epoch + 1}/{epochs}], Потери: {running_loss / len(train_loader):.4f}, Точность на обучении: {train_acc:.4f}, Точность на тесте: {test_acc:.4f}")

#early stop

#за 10 эпох не обучается модель
              
training_time = time.time() - start_time
training_time
              
final_train_acc = train_acc_history[-1]
final_test_acc = test_acc_history[-1]
final_train_acc
              

final_test_acc
              

plt.figure(figsize=(10, 5))
plt.plot(range(1, epochs + 1), train_loss_history, label="Train Loss")
plt.xlabel("Эпоха")
plt.ylabel("Функция потерь")
plt.title("Изменение функции потерь на обучающем множестве")
plt.legend()
plt.show()
              

plt.figure(figsize=(10, 5))
plt.plot(range(1, epochs + 1), train_acc_history, label="Train Accuracy")
plt.plot(range(1, epochs + 1), test_acc_history, label="Test Accuracy")
plt.xlabel("Эпоха")
plt.ylabel("Точность")
plt.title("Изменение точности на обучающем и тестовом множествах")
plt.legend()
plt.show()
''')
    elif st == '5':
        print('''
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
              
train_transforms = transforms.Compose([
    transforms.RandomResizedCrop(224),
    transforms.RandomHorizontalFlip(),    #случайное горизонтальное отражение
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),  # Изменение интенсивности пикселей
    transforms.ToTensor(),
    transforms.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))])


test_transforms = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))
])
              
train_dataset = datasets.ImageFolder(root='/content/cat_breeds_4', transform=train_transforms)
test_dataset = datasets.ImageFolder(root='/content/cat_breeds_4', transform=test_transforms)


train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
              
model = models.vgg16(weights='IMAGENET1K_V1')


for param in model.features.parameters():
    param.requires_grad = False


num_classes = len(train_dataset.classes)
model.classifier[6] = nn.Linear(4096, num_classes)

model = model.to(DEVICE)
              
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
              

num_epochs = 10
train_loss_history = []
train_acc_history = []
test_acc_history = []

def calculate_accuracy(loader, model):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(DEVICE), labels.to(DEVICE)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    return correct / total
              

for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    correct_train = 0
    total_train = 0

    for images, labels in train_loader:
        images, labels = images.to(DEVICE), labels.to(DEVICE)

        outputs = model(images)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        total_train += labels.size(0)
        correct_train += (predicted == labels).sum().item()

    train_loss_history.append(running_loss / len(train_loader))
    train_acc = correct_train / total_train
    train_acc_history.append(train_acc)

    test_acc = calculate_accuracy(test_loader, model)
    test_acc_history.append(test_acc)

    print(f"Эпоха [{epoch + 1}/{num_epochs}], Потери: {running_loss / len(train_loader):.4f}, "
          f"Точность на обучении: {train_acc:.4f}, Точность на тесте: {test_acc:.4f}")
              

plt.figure(figsize=(10, 5))
plt.plot(range(1, num_epochs + 1), train_loss_history, label="Train Loss")
plt.xlabel("Эпоха")
plt.ylabel("Функция потерь")
plt.title("Изменение функции потерь на обучающем множестве")
plt.legend()
plt.show()
              

plt.figure(figsize=(10, 5))
plt.plot(range(1, num_epochs + 1), train_acc_history, label="Train Accuracy")
plt.plot(range(1, num_epochs + 1), test_acc_history, label="Test Accuracy")
plt.xlabel("Эпоха")
plt.ylabel("Точность")
plt.title("Изменение точности на обучающем и тестовом множестве")
plt.legend()
plt.show()
''')
    else:
        print('no such index')

def cnn1D_info():
    print('''
ЧТОБЫ ВЫЗВАТЬ КОД: используйте DL.cnn1D_code("НОМЕР ЗАДАНИЯ")
          
1. Загрузите данные из файла ts.csv. 
Используя модель, состоящую из одного одномерного сверточного слоя, решите задачу предсказания  𝑦𝑡  по k предыдущим точкам временного ряда  𝑥𝑡−𝑘...𝑥𝑡−1 . 
Исследуйте значения  𝑘∈[1,7] . Для каждого  𝑘  выведите на экран итоговое значение функции потерь и веса ядра свертки. 
Визуализируйте исходный временной ряд и полученные прогнозы.
          
2. Загрузите файл PV_Elec_Gas2.csv. Опишите класс ElectricityDataset, который разбивает данные на окна в соответствии со следующей схемой:
          
3. Решите задачу предсказания столбца Gas_mxm на основе столбцов cum_power и Elec_kW с использованием одномерных сверток. 
Для оптимизации используйте мини-пакетный градиентный спуск с использованием DataLoader. 
Обратите внимание, что при создании DataLoader вы не можете перемешивать данные.
Постройте график изменения значения функции потерь на обучающем и тестовом множестве в зависимости от номера эпохи. 
Визуализируйте на одном графике прогнозы модели и предсказываемый временной ряд.
''')
def cnn1D_code(st):
    print('''
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
import matplotlib.pyplot as plt
''')
    if st == '1':
        print('''
data = pd.read_csv('ts.csv')
x_series = data['x'].values
y_series = data['y'].values
data
              
def create_dataset(x, y, k):
    X, Y = [], []
    for i in range(k, len(x)):
        X.append(x[i-k:i])
        Y.append(y[i])
    return torch.tensor(X, dtype=torch.float32), torch.tensor(Y, dtype=torch.float32)
              
class ConvModel(nn.Module):
    def __init__(self, k):
        super(ConvModel, self).__init__()
        self.conv = nn.Conv1d(in_channels=1, out_channels=1, kernel_size=k, padding=k-1)

    def forward(self, x):
        x = self.conv(x)
        return x[:, :, -1].view(-1)
              
learning_rate = 0.01
epochs = 100

losses = {}
kernels = {}

for k in range(1, 8):
    X, Y = create_dataset(x_series, y_series, k)
    X = X.unsqueeze(1)
    dataset = TensorDataset(X, Y)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

    model = ConvModel(k)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(epochs):
        for X_batch, Y_batch in dataloader:
            optimizer.zero_grad()
            predictions = model(X_batch)
            loss = criterion(predictions, Y_batch)
            loss.backward()
            optimizer.step()

    losses[k] = loss.item()
    kernels[k] = model.conv.weight.detach().numpy()

    print(f"k={k}: Итоговая функция потерь = {loss.item():.4f}")
    print(f"Вес ядра свертки для k={k}:\n{kernels[k]}\n")
              
plt.figure(figsize=(14, 7))
plt.plot(y_series, label="Исходный временной ряд y", color='blue')

best_k = min(losses, key=losses.get)
X_test, Y_test = create_dataset(x_series, y_series, best_k)
X_test = X_test.unsqueeze(1)
predicted = model(X_test).detach().numpy()

plt.plot(range(best_k, len(y_series)), predicted, label=f"Прогноз при k={best_k}", color='red')
plt.legend()
plt.xlabel("Время")
plt.ylabel("Значение")
plt.title("Исходный временной ряд и прогнозы")
plt.show()
''')
    elif st == '2':
        print('''
from datetime import datetime
from torch.utils.data import Dataset, DataLoader


data = pd.read_csv('PV_Elec_Gas2.csv', parse_dates=['Unnamed: 0'])
data = data.rename(columns={'Unnamed: 0': 'Date'})

train_data = data[data['Date'].dt.year < 2019]
test_data = data[data['Date'].dt.year == 2019]

# Класс для создания оконных данных
class ElectricityDataset(Dataset):
    def __init__(self, df, window_size):
        self.data = df
        self.window_size = window_size

    def __len__(self):
        return len(self.data) - self.window_size

    def __getitem__(self, idx):
        x = self.data.iloc[idx:idx + self.window_size][['cum_power', 'Elec_kW']].values
        y = self.data.iloc[idx + self.window_size]['Gas_mxm']
        return torch.tensor(x, dtype=torch.float32), torch.tensor(y, dtype=torch.float32)

# Устновка окна
window_size = 30  # можно менять по задаче
train_dataset = ElectricityDataset(train_data, window_size)
test_dataset = ElectricityDataset(test_data, window_size)
''')
    elif st == '3':
        print('''
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
from torch.optim.lr_scheduler import ReduceLROnPlateau

# Гиперпараметры
window_size = 30
batch_size = 32
learning_rate = 0.001
num_epochs = 70

# Определение модели с дополнительными слоями
class EnhancedConvModel(nn.Module):
    def __init__(self, window_size):
        super(EnhancedConvModel, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=2, out_channels=32, kernel_size=3)
        self.bn1 = nn.BatchNorm1d(32)
        self.conv2 = nn.Conv1d(in_channels=32, out_channels=64, kernel_size=3)
        self.bn2 = nn.BatchNorm1d(64)
        self.pool = nn.MaxPool1d(2)
        self.fc1 = nn.Linear(64 * ((window_size - 4) // 2), 64)  # Подбираем размер
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)

    def forward(self, x):
        x = torch.relu(self.bn1(self.conv1(x)))
        x = torch.relu(self.bn2(self.conv2(x)))
        x = self.pool(x)
        x = x.view(x.size(0), -1)  # Flatten
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x.view(-1)

# Подготовка данных
train_dataset = ElectricityDataset(train_data, window_size)
test_dataset = ElectricityDataset(test_data, window_size)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# Инициализация модели, функции потерь и оптимизатора
model = EnhancedConvModel(window_size)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Планировщик для динамического изменения learning rate
scheduler = ReduceLROnPlateau(optimizer, 'min', patience=2, factor=0.5, verbose=True)

# Обучение модели
train_losses = []
test_losses = []

for epoch in range(num_epochs):
    model.train()
    train_loss = 0.0
    for x_batch, y_batch in train_loader:
        x_batch = x_batch.permute(0, 2, 1)  # Преобразование размера для Conv1d
        optimizer.zero_grad()
        outputs = model(x_batch)
        loss = criterion(outputs.squeeze(), y_batch)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()

    train_losses.append(train_loss / len(train_loader))

    # Оценка на тестовой выборке
    model.eval()
    test_loss = 0.0
    with torch.no_grad():
        for x_batch, y_batch in test_loader:
            x_batch = x_batch.permute(0, 2, 1)
            outputs = model(x_batch)
            loss = criterion(outputs.squeeze(), y_batch)
            test_loss += loss.item()

    test_losses.append(test_loss / len(test_loader))

    # Обновление learning rate
    scheduler.step(test_loss)

    print(f'Epoch {epoch+1}, Train Loss: {train_losses[-1]:.4f}, Test Loss: {test_losses[-1]:.4f}')

# График потерь
plt.figure(figsize=(10, 5))
plt.plot(train_losses, label="Train Loss")
plt.plot(test_losses, label="Test Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.title("Loss over epochs")
plt.show()

# Прогноз и визуализация результатов
model.eval()
predictions = []
real_values = []

with torch.no_grad():
    for x_batch, y_batch in test_loader:
        x_batch = x_batch.permute(0, 2, 1)
        outputs = model(x_batch)
        predictions.extend(outputs.squeeze().tolist())
        real_values.extend(y_batch.tolist())

plt.figure(figsize=(12, 6))
plt.plot(real_values, label="Real Gas_mxm", color='blue')
plt.plot(predictions, label="Predicted Gas_mxm", color='red')
plt.xlabel("Time")
plt.ylabel("Gas_mxm")
plt.legend()
plt.title("Real vs Predicted Gas_mxm")
plt.show()
''')
    else:
        print('no such index')
def RL_info():
    print('''
ЧТОБЫ ВЫЗВАТЬ КОД: используйте DL.RL_code("НОМЕР ЗАДАНИЯ")
          
1. Создайте окружение Blackjack-v1. Сыграйте N=10000 игр, выбирая действие случайным образом. Посчитайте и выведите на экран долю выигранных игр.
          
2. Создайте окружение Blackjack-v1. Предложите стратегию, которая позволит, в среднем, выигрывать чаще, чем случайный выбор действия. 
Реализуйте эту стратегию и сыграйте N=10000 игр, выбирая действие согласно этой стратегии. Посчитайте и выведите на экран долю выигранных игр.
          
3. Создайте окружение для игры в крестики-нолики, реализовав интерфейс gym.Env. Решение должно удовлетворять следующим условиям:
для создания пространства состояний используется spaces.Box;
для создания пространства действий используется spaces.MultiDiscrete;
игра прекращается, если:
нет возможности сделать ход;
игрок пытается отметить уже выбранную ячейку.
после каждого хода игрок получает награду:
0, если игра не закончена;
1, если игрок выиграл;
-1, если игрок проиграл.
стратегию выбора действия для второго игрока (машины) определите самостоятельно.
Стратегия поведения машины является частью окружения и должна быть реализована внутри него. Сделайте все соответствующие переменные и методы приватными (названия всех переменных начинаются с __), подчеркнув, что у пользователя не должно быть к ним доступа извне.
Сыграйте одну игру, выбирая действия случайным образом. Выведите на экран состояние окружения после каждого хода и итоговую награду пользователя за сессию.
          
4. Предложите стратегию (в виде алгоритма без использования методов машинного обучения), которая позволит, 
в среднем, выигрывать в крестики-нолики чаще, чем случайный выбор действия. 
Реализуйте эту стратегию и сыграйте игру, выбирая действия согласно этой стратегии. 
Выведите на экран состояние окружения после каждого хода и итоговую награду пользователя за сессию.
          
5. Создайте окружение MountainCar-v0. Проиграйте 10 эпизодов и сохраните на диск файл с записью каждого пятого эпизода. 
Для записи видео воспользуйтесь обёрткой RecordVideo. Вставьте скриншот, на котором видно, что файлы были созданы.
''')
    
def RL_code(st):
    if st == '1':
        print('''
!pip install gymnasium
              
import gymnasium as gym #библиотека для обучения с подкреплением
import numpy as np
import gym
from gym import spaces
              
#задаем окружение
#cимуляция игры, где агент взаимодействует со средой
#render_mode=None - визуализация игры отключена ( видим только результат )
env = gym.make("Blackjack-v1", render_mode=None)

N = 10000  #кол-во игр , 10тыс , чтоб результаты были статистически значимыми
wins = 0   #счетчик выигрышей

# Игровой цикл
for _ in range(N):
    observation, _ = env.reset()  #окружение в нач состояние ( раздает карты )
    done = False #флаг, который становится true, когда игра завершится

    while not done:
        action = env.action_space.sample()  #случайное действие: 0 - stay, 1 - берем карту
        observation, reward, done, _, _ = env.step(action)  #вып действие и возвращает s , r

    if reward > 0:
        wins += 1


win_rate = wins / N
print(f"Доля выигранных игр: {win_rate:.4f}")
env.close()
''')
    elif st == '2':
        print('''
env = gym.make("Blackjack-v1", render_mode=None)
N = 10000
wins = 0


def blackjack_strategy(player_sum, dealer_card, usable_ace):
  #player_sum — это сумма карт игрока
  #dealer_card — это карта, которую показывает дилер
  #usable_ace — туз, который можно считать как 1 или 11.

    if player_sum < 14:
        return 1  #берем
    else:
        return 0  #остановка


for _ in range(N):
    observation, _ = env.reset()  # Сбрасываем окружение
    done = False

    while not done:
        player_sum, dealer_card, usable_ace = observation

        #стратегия решает: взять карту или остановиться
        action = blackjack_strategy(player_sum, dealer_card, usable_ace)


        #выполняем действие и получаем r, s', done ?
        observation, reward, done, _, _ = env.step(action)


    if reward > 0:
        wins += 1


win_rate = wins / N
print(f"Доля выигранных игр (стратегия): {win_rate:.4f}")
env.close()
''')
    elif st =='3':
        print('''
class TicTacToeEnv(gym.Env):
  def __init__(self):
    super(TicTacToeEnv, self).__init__()

    #Игровое поле: 0 - пусто, 1 - игрок, 2 - машина
    self.__state = np.zeros((3,3), dtype=int)
    self.__current_player = 1 #первым ходит игрок

    #пространсво состояний и действий
    self.observation_space = spaces.Box(low=0, high=2, shape=(3,3), dtype=int) #всевозможные состояния на поле
    self.action_space = spaces.MultiDiscrete([3,3]) #игрок может выбирать любую клетку на поле

  #обновляем игру
  def reset(self):
    self.__state = np.zeros((3,3), dtype=int) #игровое поле снова становится пустым
    self.__current_player = 1 #игрок начинает первым
    return self.__state


  #Проверка победителя
  def __is_winner(self, player):
    for i in range(3):
      #проверяем, занята ли одна строка и столбец полностью крестиками (1) или ноликами (2).
      if np.all(self.__state[i, :] == player) or np.all(self.__state[:, i] == player):
        return True

      #проверяем заняты ли диагонали
    if np.all(np.diag(self.__state) == player) or np.all(np.diag(np.fliplr(self.__state)) == player):
      return True
    return False

  #Стратения машины
  #Машина сначала проверяет, может ли она выиграть.
  #Если не может выиграть, она блокирует победу игрока.
  #Если и это не получается, она занимает центр.
  #Если центр занят, машина выбирает угол.
  #Если углы тоже заняты, машина ходит в первую свободную клетку.

  def __machine_move(self):
        """
        Стратегия машины: побеждает, блокирует, иначе случайный ход.
        """
        # 1. Победный ход для машины
        for i in range(3):
            for j in range(3):
                if self.__state[i, j] == 0: #свободна ли клетка
                    self.__state[i, j] = 2
                    if self.__is_winner(2): #выиграет ли машина
                        return #если победный ход , то прекращаем
                    self.__state[i, j] = 0

        # 2. Блокировка хода игрока
        for i in range(3):
            for j in range(3):
                if self.__state[i, j] == 0:
                    self.__state[i, j] = 1 #ставим Х
                    if self.__is_winner(1):
                        self.__state[i, j] = 2 #если игрок может выиграть ставим 0 и блокируем
                        return
                    self.__state[i, j] = 0

        # 3. Выбор центра
        if self.__state[1, 1] == 0: #свободен ли центр
            self.__state[1, 1] = 2
            return

        # 4. Выбор углов
        for i, j in [(0, 0), (0, 2), (2, 0), (2, 2)]: #перебираем координаты углов
            if self.__state[i, j] == 0:
                self.__state[i, j] = 2
                return

        # 5. Любая доступная клетка
        for i in range(3):
            for j in range(3):
                if self.__state[i, j] == 0:
                    self.__state[i, j] = 2
                    return

  def step(self, action):
        """
        Выполняет ход игрока и машины.
        """
        row, col = action
        #action — это ход игрока

        # Проверка на корректность хода
        #Если клетка уже занята, игрок получает наказание -1, и игра заканчивается.
        if self.__state[row, col] != 0:
            return self.__state, -1, True, {}  # Наказание за некорректный ход

        # Игрок делает ход
        #Игрок делает ход (ставит 1 в выбранную клетку).
        self.__state[row, col] = 1

        # Проверка на победу игрока
        if self.__is_winner(1): #проверяет строки, столбцы и диагонали на наличие одинаковых символов
            return self.__state, 1, True, {}  # Игрок победил

        # Проверка на ничью
        if not np.any(self.__state == 0): #если на доске не осталось 0
            return self.__state, 0, True, {}  # Ничья

        # Машина делает ход
        self.__machine_move()

        # Проверка на победу машины
        if self.__is_winner(2):
            return self.__state, -1, True, {}  # Игрок проиграл

        # Проверка на ничью
        if not np.any(self.__state == 0):
            return self.__state, 0, True, {}

        #ни одна из проверок не сработала -> продолжаем игру
        return self.__state, 0, False, {}

  def render(self):
        """
        Отображает текущее состояние игры.
        """
        symbols = {0: ".", 1: "X", 2: "O"}
        for row in self.__state:
            print(" ".join(symbols[cell] for cell in row))
        print()
              

# Игровой цикл
env = TicTacToeEnv()
state = env.reset() #сбрасывает игровое поле
done = False
total_reward = 0

print("Начальное состояние:")
env.render()

while not done:
    # Ход игрока (направленный выбор: выбираем первую свободную клетку)
    action = None
    for i in range(3):
        for j in range(3):
            if state[i, j] == 0:
                action = (i, j)
                break
        if action:
            break

    state, reward, done, _ = env.step(action)

    print("Текущее состояние:")
    env.render()
    total_reward = reward

# Итоговый вывод
if total_reward == 1:
    print("Поздравляем! Вы победили!")
    print('reward = 1')
elif total_reward == -1:
    print("Машина победила. Удачи в следующий раз!")
    print('reward = -1')
else:
    print("Игра закончилась вничью.")
    print('reward = 0')
''')
    elif st == '4':
        print('''
class TicTacToeEnv(gym.Env):
    """
    Окружение для игры в крестики-нолики.
    """
    def __init__(self):
        super(TicTacToeEnv, self).__init__()
        self.__state = np.zeros((3, 3), dtype=int)  # Поле 3x3: 0 - пусто, 1 - игрок, 2 - машина
        self.__current_player = 1  # Игрок начинает первым

        self.observation_space = spaces.Box(low=0, high=2, shape=(3, 3), dtype=int) #всевозможные состояния на поле
        self.action_space = spaces.MultiDiscrete([3, 3]) #игрок выбирает любое место для хода

    def reset(self):
        """Сбрасывает состояние игры."""
        self.__state = np.zeros((3, 3), dtype=int)
        self.__current_player = 1
        return self.__state

    def is_winner(self, player):  # Публичный метод
        """Проверка победы игрока."""
        for i in range(3):
            if np.all(self.__state[i, :] == player) or np.all(self.__state[:, i] == player):
                return True
        if np.all(np.diag(self.__state) == player) or np.all(np.diag(np.fliplr(self.__state)) == player):
            return True
        return False

    def __machine_move(self):
        """Стратегия машины: победа -> блокировка -> первый свободный ход."""
        for i in range(3):
            for j in range(3):
                if self.__state[i, j] == 0:
                    # Победный ход
                    self.__state[i, j] = 2
                    if self.is_winner(2):
                        return
                    self.__state[i, j] = 0

        for i in range(3):
            for j in range(3):
                if self.__state[i, j] == 0:
                    # Блокировка игрока
                    self.__state[i, j] = 1
                    if self.is_winner(1):
                        self.__state[i, j] = 2
                        return
                    self.__state[i, j] = 0

        # Любой доступный ход
        #если нет победных или блокирующих ходов , машина занимает любую клетку
        for i in range(3):
            for j in range(3):
                if self.__state[i, j] == 0:
                    self.__state[i, j] = 2
                    return

    def step(self, action):
        """Выполняет шаг игрока и машины."""
        row, col = action
        if self.__state[row, col] != 0:
            return self.__state, -1, True, {}  # Некорректный ход: проигрыш

        self.__state[row, col] = 1  # Ход игрока
        if self.is_winner(1):
            return self.__state, 1, True, {}  # Победа игрока
        if not np.any(self.__state == 0):
            return self.__state, 0, True, {}  # Ничья

        self.__machine_move()  # Ход машины
        if self.is_winner(2):
            return self.__state, -1, True, {}  # Победа машины
        if not np.any(self.__state == 0):
            return self.__state, 0, True, {}  # Ничья

        return self.__state, 0, False, {}

    def render(self):
        """Отображение текущего состояния игры."""
        symbols = {0: ".", 1: "X", 2: "O"}
        for row in self.__state:
            print(" ".join(symbols[cell] for cell in row))
        print()

def optimal_player_move(state, env):
    """
    Реализация оптимальной стратегии игрока.
    """
    # Победный ход
    for i in range(3):
        for j in range(3):
            if state[i, j] == 0:
                state[i, j] = 1
                if env.is_winner(1):
                    state[i, j] = 0
                    return (i, j)
                state[i, j] = 0

    # Блокировка победы машины
    for i in range(3):
        for j in range(3):
            if state[i, j] == 0:
                state[i, j] = 2
                if env.is_winner(2):
                    state[i, j] = 0
                    return (i, j)
                state[i, j] = 0

    # Центр
    if state[1, 1] == 0:
        return (1, 1)

    # Углы
    for i, j in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if state[i, j] == 0:
            return (i, j)

    # Любой доступный ход
    for i in range(3):
        for j in range(3):
            if state[i, j] == 0:
                return (i, j)
              

# Игровой цикл с оптимальной стратегией
env = TicTacToeEnv()
state = env.reset()
done = False
print("Начальное состояние:")
env.render()

while not done:
    action = optimal_player_move(state, env)
    state, reward, done, _ = env.step(action)
    env.render()

if reward == 1:
    print("Поздравляем! Вы победили!")
elif reward == -1:
    print("Машина победила. Удачи в следующий раз!")
else:
    print("Игра закончилась вничью.")
''')
    elif st == '5':
        print('''
from google.colab import drive
drive.mount('/content/drive')
              
import gymnasium as gym
from gymnasium.wrappers import RecordVideo
import os


video_folder = "./videos"  #папка для хранения видео
os.makedirs(video_folder, exist_ok=True)

env = gym.make("MountainCar-v0", render_mode="rgb_array")  #окружение
env = RecordVideo(env, video_folder=video_folder, episode_trigger=lambda x: x % 5 == 0) #видео записываетс для каждого пятого эпизода


num_episodes = 10
for episode in range(num_episodes):
    state, _ = env.reset() #новое состояние для каждого эпизода
    done = False
    total_reward = 0
    while not done:
        action = env.action_space.sample()  #выбирается случайное действие из множества возможных действий
        state, reward, done, truncated, _ = env.step(action)
        total_reward += reward
    print(f"Эпизод {episode + 1} завершён с наградой: {total_reward}")

env.close()

# Проверяем файлы в папке
print(f"Видео сохранены в папке: {video_folder}")
print("Список файлов в папке:", os.listdir(video_folder))
    
a = '/content/videos/rl-video-episode-0.mp4'
a
''')
def QL_info():
    print('''
ЧТОБЫ ВЫЗВАТЬ КОД: используйте DL.QL_code("НОМЕР ЗАДАНИЯ")

1. Обучите агента для игры в блэкджек (окружение Blackjack-v1), используя алгоритм Q-learning. 
Для создания таблицы Q-функции выясните размеры пространства состояния игры и количество возможных действий игрока и выведите эти значения на экран. 
Во время обучения несколько раз вычислите статистику за print_every последних эпизодов: количество выигранных и проигранных сессий. 
После завершения обучения визуализируйте полученные данные. Изучите, как выглядит Q-функция (в каких состояниях игрок будет брать карту, в каких - нет). 
Cыграйте N=10000 игр, применяя стратегию, выведенную из обученной Q-функции, посчитайте и выведите на экран долю выигранных игр.
Cтратегия для выбора действия:
𝑎𝑡+1(𝑠𝑡)=𝑎𝑟𝑔𝑚𝑎𝑥𝑎𝑄(𝑠𝑡,𝑎) 

2. Повторите решение предыдущей задачи, используя алгоритм  𝜖 -greedy Q-learning. 
Исследуйте, как гиперпараметры и способ инициализации значений Q-функции влияют на результат.
Cтратегия для выбора действия:
Сгенерировать число  𝑝  из  𝑈(0,1) ;
Если  𝑝<𝜖 , то выбрать действие случайным образом;
В противном случае  𝑎𝑡+1(𝑠𝑡)=𝑎𝑟𝑔𝑚𝑎𝑥𝑎𝑄(𝑠𝑡,𝑎) .
              
3. Повторите решение задачи 1, используя алгоритм double Q-learning.
Cтратегия для выбора действия:
Сгенерировать число  𝑝  из  𝑈(0,1) ;
Если  𝑝<𝜖 , то выбрать действие случайным образом;
В противном случае  𝑎𝑡+1(𝑠𝑡)=𝑎𝑟𝑔𝑚𝑎𝑥𝑎((𝑄𝐴𝑡+𝑄𝐵𝑡)(𝑠𝑡,𝑎))) .
Правило обновления Q-функции:
𝑄𝐴𝑡+1(𝑠𝑡,𝑎𝑡)=𝑄𝐴𝑡(𝑠𝑡,𝑎𝑡)+𝛼𝑡(𝑠𝑡,𝑎𝑡)(𝑟𝑡+𝛾𝑄𝐵𝑡(𝑠𝑡+1,𝑎𝑟𝑔 𝑚𝑎𝑥𝑎𝑄𝐴𝑡(𝑠𝑡+1,𝑎))−𝑄𝐴𝑡(𝑠𝑡,𝑎𝑡)) 
𝑄𝐵𝑡+1(𝑠𝑡,𝑎𝑡)=𝑄𝐵𝑡(𝑠𝑡,𝑎𝑡)+𝛼𝑡(𝑠𝑡,𝑎𝑡)(𝑟𝑡+𝛾𝑄𝐴𝑡(𝑠𝑡+1,𝑎𝑟𝑔 𝑚𝑎𝑥𝑎𝑄𝐵𝑡(𝑠𝑡+1,𝑎))−𝑄𝐵𝑡(𝑠𝑡,𝑎𝑡)) 

4. Обучите агента для управления машиной (окружение MountainCar-v0) при помощи любого из рассмотренных вариантов алгоритма Q-learning. 
Для перехода от непрерывного пространства состояний к конечному разбейте пространство состояний на окна (количество окон выберите сами). 
Для определения минимальных и максимальных значений координат воспользуйтесь информацией об окружении. 
Во время обучения несколько раз вычислите среднее значение наград за эпизод за несколько последних эпизодов и количество успешных сессий за последние эпизоды. 
После завершения обучения визуализируйте полученные данные.
Сделайте несколько промежуточных видео с записью работы агента во время обучения.
''')
def QL_code(st):
    if st == '1':
        print('''
pip install gymnasium
              
import gymnasium as gym
import numpy as np
from tqdm import tqdm
from dataclasses import dataclass
import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from gymnasium.wrappers import RecordVideo
import shutil
              
#класс для хранения гиперпараметров
@dataclass
class Config:
    discount: float = 0.95
    lr: float = 0.005
    n_episodes: int = 10_000
    print_every: int = 5000
              
class Agent:
    def __init__(self, env: gym.Env, config: Config) -> None:
        self.env = env
        self.cfg = config
        self._create_q_table()

##############################################################
    def _create_q_table(self):
        self.q_table = np.zeros((32, 11, 2, 2))

#############################################################

    #e-жадная стратегия
    def get_action(self, state: tuple) -> int:
        if np.random.rand() < 0.1:
            return self.env.action_space.sample()
        player_sum, dealer_card, usable_ace = state
        return np.argmax(self.q_table[player_sum, dealer_card, int(usable_ace)]) # => Q_0 Q_1

#########################################################################

    def update_q_table(self, state: tuple, new_state: tuple, reward: float, action: int, done: bool) -> None:
        player_sum, dealer_card, usable_ace = state
        player_sum_new, dealer_card_new, usable_ace_new = new_state

        current_q = self.q_table[player_sum, dealer_card, int(usable_ace), action]
        future_q = 0 if done else np.max(self.q_table[player_sum_new, dealer_card_new, int(usable_ace_new)])

        #TD
        self.q_table[player_sum, dealer_card, int(usable_ace), action] = \
            current_q + self.cfg.lr * (reward + self.cfg.discount * future_q - current_q)

#########################################################################

    def run_episode(self) -> float:
        done = False
        state, _ = self.env.reset()
        while not done:
            action = self.get_action(state)
            new_state, reward, terminated, truncated, _ = self.env.step(action)
            done = terminated or truncated
            self.update_q_table(state, new_state, reward, action, done)
            state = new_state
        return reward

###################################################################

    def train(self):
        ep_rewards = []
        stats = {"wins": 0, "losses": 0, "draws": 0}

        for ep in tqdm(range(self.cfg.n_episodes)):
            reward = self.run_episode()
            ep_rewards.append(reward)

            if reward > 0:
                stats["wins"] += 1
            elif reward < 0:
                stats["losses"] += 1
            else:
                stats["draws"] += 1

            if (ep + 1) % self.cfg.print_every == 0:
                print(f"Эпизод {ep + 1}: Побед: {stats['wins']}, Поражений: {stats['losses']}, Ничьих: {stats['draws']}")

        return ep_rewards, stats
#инициализирем
#прогоняем цикл по количеству эпизодов
#возвращаем список наград и статистику
              
state_space = (32, 11, 2)
action_space = 2
state_space, action_space
              
env = gym.make("Blackjack-v1")
cfg = Config(n_episodes=50000, lr=0.005, discount=0.95, print_every=1000)
agent = Agent(env, cfg)
rewards, stats = agent.train()
              
player_sum = np.arange(1, 22)
dealer_card = np.arange(1, 11)
usable_ace = [0, 1]

for ace in usable_ace:
    strategy = np.argmax(agent.q_table[1:22, :, ace, :], axis=2)
    plt.imshow(strategy, cmap="coolwarm", interpolation="nearest")
    plt.colorbar(label="Действие (0: взять карту, 1: оставить)")
    plt.title(f"Стратегия с тузом = {bool(ace)}")
    plt.xlabel("Открытая карта дилера")
    plt.ylabel("Сумма игрока")
    plt.show()
              
wins = 0
n_games = 10000

for _ in range(n_games):
    state, _ = env.reset()
    done = False
    while not done:
        action = agent.get_action(state)
        state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
    if reward > 0:
        wins += 1

win_rate = wins / n_games
win_rate
''')
    elif st == '2':
        print('''
@dataclass
class Config:
    discount: float = 0.95
    lr: float = 0.005
    n_episodes: float = 100_000
    epsilon: float = 1.0
    final_epsilon: float = 0.3
    print_every: int = 5000
              
class Agent:
    def __init__(self, env: gym.Env, config: Config):
        self.env = env
        self.config = config
        self._create_q_table()
        self.epsilon = config.epsilon

#######################################################

    def _create_q_table(self):
        obs_space = (32, 11, 2)
        action_space = self.env.action_space.n
        self.q_table = np.zeros(obs_space + (action_space,))

#############################################################

    def get_action(self, state: tuple) -> int:
        if np.random.rand() < self.epsilon:
            return self.env.action_space.sample()
        else:
            return np.argmax(self.q_table[state])

############################################################

    def update_q_table(self, state, new_state, reward, action, done):
        current_q = self.q_table[state][action]
        max_future_q = 0 if done else np.max(self.q_table[new_state])
        td_target = reward + self.config.discount * max_future_q
        self.q_table[state][action] = (1 - self.config.lr) * current_q + self.config.lr * td_target

##############################################################

    def decay_epsilon(self, episode: int):
        epsilon_decay = (self.config.epsilon - self.config.final_epsilon) / self.config.n_episodes
        self.epsilon = max(self.config.final_epsilon, self.config.epsilon - epsilon_decay * episode)

#################################################################

    def run_episode(self):
        state, _ = self.env.reset()
        done = False
        total_reward = 0

        while not done:
            action = self.get_action(state)
            new_state, reward, terminated, truncated, _ = self.env.step(action)
            done = terminated or truncated


            self.update_q_table(state, new_state, reward, action, done)
            state = new_state
            total_reward += reward

        return total_reward

####################################################################

    def train(self):
        rewards = []
        win_count = 0

        for episode in tqdm(range(self.config.n_episodes)):
            reward = self.run_episode()
            rewards.append(reward)

            if reward > 0:
                win_count += 1

            if (episode + 1) % self.config.print_every == 0:
                win_rate = win_count / self.config.print_every
                print(f"Эпизод {episode + 1}: Win rate = {win_rate:.2f}")
                win_count = 0


            self.decay_epsilon(episode)

        return rewards

########################################################################

    def evaluate(self, n_games=10_000):
        wins = 0
        for _ in range(n_games):
            state, _ = self.env.reset()
            done = False

            while not done:
                action = np.argmax(self.q_table[state])
                new_state, reward, terminated, truncated, _ = self.env.step(action)
                done = terminated or truncated
                state = new_state

            if reward > 0:
                wins += 1

        return wins / n_games
              
env = gym.make("Blackjack-v1")
config = Config()
agent = Agent(env, config)


print("Обучение агента...")
rewards = agent.train()
print("Оценка стратегии агента...")
win_rate = agent.evaluate()
print(f"Доля выигранных игр: {win_rate:.2f}")
''')
    elif st=='3':
        print('''
@dataclass
class Config:
    discount: float = 0.95
    lr: float = 0.005
    n_episodes: int = 100_000
    epsilon: float = 1.0
    final_epsilon: float = 0.3
    print_every: int = 5000
              

class DoubleQLearningAgent:
    def __init__(self, env: gym.Env, config: Config):
        self.env = env
        self.config = config
        self._create_q_tables()
        self.epsilon = config.epsilon

############################################################

    def _create_q_tables(self):
        obs_space = (32, 11, 2)
        action_space = self.env.action_space.n
        self.q_table_a = np.zeros(obs_space + (action_space,))
        self.q_table_b = np.zeros(obs_space + (action_space,))

############################################################

    def get_action(self, state: tuple) -> int:
        if np.random.rand() < self.epsilon:
            return self.env.action_space.sample()
        else:
            q_sum = self.q_table_a[state] + self.q_table_b[state]
            return np.argmax(q_sum)

    def update_q_tables(self, state, new_state, reward, action, done):
        if np.random.rand() < 0.5:
            current_q = self.q_table_a[state][action]
            max_action = np.argmax(self.q_table_a[new_state])
            target_q = reward + self.config.discount * self.q_table_b[new_state][max_action] * (not done)
            self.q_table_a[state][action] += self.config.lr * (target_q - current_q)

        else:
            current_q = self.q_table_b[state][action]
            max_action = np.argmax(self.q_table_b[new_state])
            target_q = reward + self.config.discount * self.q_table_a[new_state][max_action] * (not done)
            self.q_table_b[state][action] += self.config.lr * (target_q - current_q)

#################################################

    def decay_epsilon(self, episode: int):
        epsilon_decay = (self.config.epsilon - self.config.final_epsilon) / self.config.n_episodes
        self.epsilon = max(self.config.final_epsilon, self.config.epsilon - epsilon_decay * episode)

###################################################

    def run_episode(self):
        state, _ = self.env.reset()
        done = False
        total_reward = 0

        while not done:
            action = self.get_action(state)
            new_state, reward, terminated, truncated, _ = self.env.step(action)
            done = terminated or truncated

            self.update_q_tables(state, new_state, reward, action, done)
            state = new_state
            total_reward += reward

        return total_reward

#########################################################

    def train(self):
        rewards = []
        win_count = 0

        for episode in tqdm(range(self.config.n_episodes)):
            reward = self.run_episode()
            rewards.append(reward)

            if reward > 0:
                win_count += 1

            if (episode + 1) % self.config.print_every == 0:
                win_rate = win_count / self.config.print_every
                print(f"Эпизод {episode + 1}: Win rate = {win_rate:.2f}")
                win_count = 0

            # Уменьшение epsilon
            self.decay_epsilon(episode)

        return rewards

###############################################################

    def evaluate(self, n_games=10_000):
        wins = 0
        for _ in range(n_games):
            state, _ = self.env.reset()
            done = False

            while not done:
                q_sum = self.q_table_a[state] + self.q_table_b[state]
                action = np.argmax(q_sum)
                new_state, reward, terminated, truncated, _ = self.env.step(action)
                done = terminated or truncated
                state = new_state

            if reward > 0:
                wins += 1

        return wins / n_games
              

env = gym.make("Blackjack-v1")
config = Config()
agent = DoubleQLearningAgent(env, config)


print("Обучение агента...")
rewards = agent.train()
print("Оценка стратегии агента...")
win_rate = agent.evaluate()
print(f"Доля выигранных игр: {win_rate:.2f}")
''')
    elif st=='4':
        print('''
class Discretizer:
    def __init__(self, low, high, bins):
        self.bins = bins
        self.bin_width = (high - low) / bins
        self.low = low

    def discretize(self, value): #значение в индекс
        return np.floor((value - self.low) / self.bin_width).astype(int)

    def transform(self, state):
        return tuple(self.discretize(state))

##############################################################

class QLearningAgent:
    """
    Класс агента для управления машиной на основе Q-learning.
    """
    def __init__(self, env, n_bins, learning_rate=0.1, discount=0.99, epsilon=1.0, final_epsilon=0.1, n_episodes=10_000):
        self.env = env
        self.n_bins = n_bins
        self.learning_rate = learning_rate
        self.discount = discount
        self.epsilon = epsilon
        self.final_epsilon = final_epsilon
        self.n_episodes = n_episodes

        # Дискретизация пространства состояний
        obs_space = env.observation_space
        self.discretizer = Discretizer(low=obs_space.low, high=obs_space.high, bins=n_bins)


        self.q_table = np.zeros((n_bins, n_bins, env.action_space.n))

######################################################################

    def get_action(self, state):
        if np.random.rand() < self.epsilon:
            return self.env.action_space.sample()
        else:
            return np.argmax(self.q_table[state])

#######################################################

    def update_q_table(self, state, action, reward, new_state, done):
        max_future_q = 0 if done else np.max(self.q_table[new_state])
        current_q = self.q_table[state][action]
        new_q = current_q + self.learning_rate * (reward + self.discount * max_future_q - current_q)
        self.q_table[state][action] = new_q

#####################################################

    def decay_epsilon(self, episode):
        epsilon_decay = (self.epsilon - self.final_epsilon) / self.n_episodes
        self.epsilon = max(self.final_epsilon, self.epsilon - epsilon_decay * episode)

#######################################################

    def train(self):
        rewards = []
        success_count = 0

        for episode in tqdm(range(self.n_episodes)):
            state, _ = self.env.reset()
            state = self.discretizer.transform(state) #нач сост в дискретное
            total_reward = 0
            done = False

            while not done:
                action = self.get_action(state)
                new_state, reward, terminated, truncated, _ = self.env.step(action)
                new_state = self.discretizer.transform(new_state)
                done = terminated or truncated

                self.update_q_table(state, action, reward, new_state, done)
                state = new_state
                total_reward += reward

            rewards.append(total_reward)
            if total_reward >= -199:
                success_count += 1

            if (episode + 1) % 1000 == 0:
                avg_reward = np.mean(rewards[-1000:])
                print(f"Эпизод {episode + 1}: Средняя награда = {avg_reward:.2f}, Успехи = {success_count}/1000")
                success_count = 0

            self.decay_epsilon(episode)

        return rewards


#########################################################################

    def evaluate(self, n_games=100):
        rewards = []
        for _ in range(n_games):
            state, _ = self.env.reset()
            state = self.discretizer.transform(state)
            done = False
            total_reward = 0

            while not done:
                action = np.argmax(self.q_table[state])
                new_state, reward, terminated, truncated, _ = self.env.step(action)
                new_state = self.discretizer.transform(new_state)
                done = terminated or truncated
                state = new_state
                total_reward += reward

            rewards.append(total_reward)

        avg_reward = np.mean(rewards)
        print(f"Средняя награда за {n_games} игр: {avg_reward:.2f}")
        return avg_reward

# Создание окружения
env = gym.make("MountainCar-v0", render_mode="rgb_array")

# Путь для сохранения видео в Colab
video_folder = "/content/videos"
video_env = RecordVideo(env, video_folder=video_folder, episode_trigger=lambda x: x % 5000 == 0)

# Параметры агента
agent = QLearningAgent(env, n_bins=20, learning_rate=0.1, discount=0.99, epsilon=1.0, final_epsilon=0.01, n_episodes=20_000)

# Обучение
print("Обучение...")
agent.train()

# Оценка
print("Оценка стратегии...")
agent.evaluate()

# Упаковка видео для скачивания
shutil.make_archive("/content/mountaincar_videos", 'zip', video_folder)

# Закрытие окружений
env.close()
video_env.close()

print("Видео сохранены и упакованы в архив: /content/mountaincar_videos.zip. Вы можете скачать его.")
              
import gym
import numpy as np
from gym.wrappers import RecordVideo
from tqdm import tqdm

class Discretizer:
    """
    Класс для дискретизации пространства состояний.
    """
    def __init__(self, low, high, bins):
        self.bins = bins
        self.bin_width = (high - low) / bins
        self.low = low

    def discretize(self, value):
        """
        Дискретизация значения.
        """
        return np.floor((value - self.low) / self.bin_width).astype(int)

    def transform(self, state):
        """
        Преобразование состояния (позиции и скорости).
        """
        # Преобразуем в индексы
        discretized_state = tuple(self.discretize(state))

        # Ограничиваем индексы, чтобы они не выходили за пределы
        discretized_state = tuple(np.clip(discretized_state, 0, self.bins - 1))

        return discretized_state

class QLearningAgent:
    """
    Класс агента для управления машиной на основе Q-learning.
    """
    def __init__(self, env, n_bins, learning_rate=0.1, discount=0.99, epsilon=1.0, final_epsilon=0.1, n_episodes=10_000):
        self.env = env
        self.n_bins = n_bins
        self.learning_rate = learning_rate
        self.discount = discount
        self.epsilon = epsilon
        self.final_epsilon = final_epsilon
        self.n_episodes = n_episodes

        # Дискретизация пространства состояний
        obs_space = env.observation_space
        self.discretizer = Discretizer(low=obs_space.low, high=obs_space.high, bins=n_bins)

        # Создание Q-таблицы
        self.q_table = np.zeros((n_bins, n_bins, env.action_space.n))

    def get_action(self, state):
        """
        Выбор действия: epsilon-жадная стратегия.
        """
        if np.random.rand() < self.epsilon:
            return self.env.action_space.sample()
        else:
            return np.argmax(self.q_table[state])

    def update_q_table(self, state, action, reward, new_state, done):
        """
        Обновление Q-таблицы по правилу Q-learning.
        """
        max_future_q = 0 if done else np.max(self.q_table[new_state])
        current_q = self.q_table[state][action]
        new_q = current_q + self.learning_rate * (reward + self.discount * max_future_q - current_q)
        self.q_table[state][action] = new_q

    def decay_epsilon(self, episode):
        """
        Постепенное уменьшение epsilon.
        """
        epsilon_decay = (self.epsilon - self.final_epsilon) / self.n_episodes
        self.epsilon = max(self.final_epsilon, self.epsilon - epsilon_decay * episode)

    def train(self):
        """
        Обучение агента.
        """
        rewards = []
        success_count = 0

        for episode in tqdm(range(self.n_episodes)):
            state, _ = self.env.reset()
            state = self.discretizer.transform(state)
            total_reward = 0
            done = False

            while not done:
                action = self.get_action(state)
                new_state, reward, done, info = self.env.step(action)  # Исправлено: 4 возвращаемых значения
                new_state = self.discretizer.transform(new_state)
                total_reward += reward

                self.update_q_table(state, action, reward, new_state, done)
                state = new_state

            rewards.append(total_reward)
            if total_reward >= -199:  # Успех: машина достигла вершины
                success_count += 1

            # Вывод статистики каждые 1000 эпизодов
            if (episode + 1) % 1000 == 0:
                avg_reward = np.mean(rewards[-1000:])
                print(f"Эпизод {episode + 1}: Средняя награда = {avg_reward:.2f}, Успехи = {success_count}/1000")
                success_count = 0

            self.decay_epsilon(episode)

        return rewards

    def evaluate(self, n_games=100):
        """
        Оценка агента.
        """
        rewards = []
        for _ in range(n_games):
            state, _ = self.env.reset()
            state = self.discretizer.transform(state)
            done = False
            total_reward = 0

            while not done:
                action = np.argmax(self.q_table[state])  # Выбор оптимального действия
                new_state, reward, done, info = self.env.step(action)  # Исправлено: 4 возвращаемых значения
                new_state = self.discretizer.transform(new_state)
                total_reward += reward
                state = new_state

            rewards.append(total_reward)

        avg_reward = np.mean(rewards)
        print(f"Средняя награда за {n_games} игр: {avg_reward:.2f}")
        return avg_reward

# Создание окружения с режимом рендеринга для записи видео
env = gym.make("MountainCar-v0", render_mode="rgb_array")

# Обертка для записи видео
video_env = RecordVideo(env, video_folder="./videos", episode_trigger=lambda x: x % 5000 == 0)

# Параметры агента
agent = QLearningAgent(env, n_bins=20, learning_rate=0.1, discount=0.99, epsilon=1.0, final_epsilon=0.01, n_episodes=20_000)

# Обучение
print("Обучение...")
agent.train()

# Оценка
print("Оценка стратегии...")
agent.evaluate()

# Закрытие окружения
env.close()
video_env.close()
''')
    else:
        print('no such index')

def QDN_info():
    print('''
ЧТОБЫ ВЫЗВАТЬ КОД: используйте DL.QDN_code("НОМЕР ЗАДАНИЯ")
          
1. Допишите класс ReplayMemory для хранения переходов между состояниями.
          
2. Допишите класс DQN для моделирования Q-функции.
          
3. Допишите классы PolicyConfig для настроек политики агента и Policy для реализации политики.
          
4. Напишите функцию plot_metrics, которая будет использоваться для визуализации процесса обучения: суммарной награды за каждый эпизод и 
максимальное значение x-координаты машины за эпизод. Для реализации можете воспользоваться wandb или любым другим удобным инструментом.
          
5. Допишите классы TrainConfig для настроек обучения и Trainer для реализации процесса обучения.
          
6. Настройте модель для управления машиной в окружении MountainCar-v0. Для преобразования векторов состояний в тензоры используйте обертку 
TransformObservation. Выведите на экран график с информацией о процессе обучения. При необходимости вставьте скриншоты этих графиков.
''')
    
def QDN_code(st):
    if st == '1':
        print('''
import torch as th
import torch.nn as nn
from collections import namedtuple, deque
import random
import math
import gymnasium as gym
from dataclasses import dataclass
import wandb
from tqdm import tqdm
from gymnasium.wrappers import RecordVideo
import numpy as np
              
wandb.login()
              
device = th.device("cpu")
device
              
#сохраняем информацию о каждом переходе обучения
Transition = namedtuple(
    'Transition',
    ('state', 'action', 'next_state', 'reward', 'done')
)

class ReplayMemory(object):
    def __init__(self, capacity):
        """capacity - максимальный размер хранилища"""
        self.memory = deque([], maxlen=capacity) #добавляем и удаляеем элементы с обеих сторон


    #добавляем новый переход в память
    def push(self, *args):
        """Сохраняет переход. При нехватке места в хранилище самые старые записи удаляются."""
        #добавляем созданный переход в память
        self.memory.append(Transition(*args))

    def sample(self, batch_size):
        """Возвращает batch_size случайно выбранных переходов"""
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)
''')
    elif st == '2':
        print('''
class DQN(nn.Module):
    """Нейронная сеть для моделирования Q-функции."""
    def __init__(self, n_observations, n_actions):
      #n_observations: количество наблюдений (функций состояния)
        super().__init__()
        self.layer_1 = nn.Linear(n_observations, 32)
        self.layer_2 = nn.Linear(32, 32) #глубина модели для извлечения сложных признаков
        self.layer_3 = nn.Linear(32, n_actions) #ожидаемая награда для каждого слоя
        self.relu = nn.ReLU()

    def forward(self, x):
        """Для каждого состояния должны получать n_actions чисел."""
        x = self.relu(self.layer_1(x))
        x = self.relu(self.layer_2(x))
        out = self.layer_3(x)
        return out
''')
    elif st == '3':
        print('''
@dataclass
class PolicyConfig:
    """Содержит настройки для Policy: размерность пространства наблюдений, кол-во действий,
    устройство, на котором будет располагаться модели; ε и т.д."""
    n_observations: int = 2
    n_actions: int = 3
    epsilon: float = 1.0 #начальное значение епсилон для е-жадной стратегии
    final_epsilon: float = 0.01
    epsilon_decay: float = 0.001 #скорость уменьшения е
    device: th.device = th.device("cpu")
              

class Policy:
    def __init__(self, env: gym.Env, policy_cfg: PolicyConfig) -> None:
        self.cfg = policy_cfg
        self.env = env
        self.action_space = env.action_space
        self.policy_network = DQN(
            policy_cfg.n_observations, policy_cfg.n_actions
        ).to(policy_cfg.device) # эту версию используем для обучения на каждом шаге

        self.target_network = DQN(
            policy_cfg.n_observations, policy_cfg.n_actions
        ).to(policy_cfg.device) # эту версию используем для прогноза на каждом шаге


        self.sync_models()
        self.steps_done = 0

    def sync_models(self) -> None:
        # загрузка весов из модели self.policy_network в self.target_network , чтобы обе сети начинали с одинаковых параметров
        self.target_network.load_state_dict(self.policy_network.state_dict())

    def get_best_action(self, state: th.Tensor) -> int:
        # ε-жадная стратегия выбора
        # выбирает лучшее действие на основе текущего состояния state. Сначала вычисляется текущее значение ε,
        # которое уменьшает вероятность случайных действий по мере обучения агента
        epsilon_th = self.cfg.final_epsilon + (self.cfg.epsilon - self.cfg.final_epsilon) * \
            math.exp(-1 * self.steps_done * self.cfg.epsilon_decay)
        self.steps_done += 1


        #Если случайное число больше ε, агент выбирает действие, максимизирующее оценку от policy_network.
        # В противном случае он выполняет случайное действие для исследования
        if random.random() > epsilon_th:
            with th.no_grad():
                return th.argmax(self.policy_network(state)).item()
        else:
            return self.action_space.sample()

    def save(self) -> None:
        # метод для сохранения моделей на диск
        th.save(self.policy_network.state_dict(), "policy_weights.pth")
        th.save(self.target_network.state_dict(), "target_weights.pth")

    def load(self) -> None:
        # метод для сохранения моделей с диска
        self.policy_network.load_state_dict(th.load("policy_weights.pth", weights_only=True))
        self.target_network.load_state_dict(th.load("target_weights.pth", weights_only=True))

''')
    elif st == '4':
        print('''
def plot_metrics(reward, max_x_coord, loss):
    wandb.log({
        "Reward Sum": reward,
        "Max X-coord": max_x_coord,
        "SmoothL1Loss": loss,
    })
              

#   loss(x) = 0.5 * (x^2)   if |x| < 1
            # |x| - 0.5
#гладкая ф-ия , менее чувствительная , чем L1
''')
    elif st=='5':
        print('''
@dataclass
class TrainConfig:
    """Содержит настройки для процесса обучения: к-т дисконтирования, скорость обучения,
    количество эпизодов для обучения, размер батча и т.д."""
    lr: float = 0.001
    batch_size: int = 64
    num_episodes: int = 100
    capacity: int = 10000 #вместимость
    gamma: float = 0.99
    sync_frequency: int = 20
              
class Trainer:
    def __init__(self, env: gym.Env, train_config: TrainConfig, policy: Policy):
        self.cfg = train_config
        self.env = env
        self.memory = ReplayMemory(self.cfg.capacity)
        self.policy = policy
        self.optimizer = th.optim.Adam(policy.policy_network.parameters(), lr=self.cfg.lr)
        self.loss_func = nn.SmoothL1Loss()

    def train(self):
        max_x_coord = -100

        wandb.init(project="08-03-dqn", name="train-5")

        # - итерация по эпизодам (run_episode)
        with tqdm(total=self.cfg.num_episodes, desc="Episode") as pbar:
            for episode in range(self.cfg.num_episodes):
                ep_max_x_coord, ep_reward, ep_loss = self.run_episode(env.reset()[0])

                # - сохранение модели при улучшении качества (максимального значения по оси x, которого удалось достичь)
                if ep_max_x_coord.item() > max_x_coord:
                    max_x_coord = ep_max_x_coord.item()
                    self.policy.save()
                    print(f"Current Max X: {ep_max_x_coord}, Episode: {episode + 1}")

                # - синхронизация моделей (policy и target) - не обязательно на каждом шаге
                if episode % self.cfg.sync_frequency == 0:
                    self.policy.sync_models()

                pbar.set_postfix(
                    {"Ep_Max_X": f"{ep_max_x_coord.item():.4f}",
                      "Reward": f"{ep_reward.item():.4f}",
                      "Loss": f"{ep_loss.item():.4f}",
                      "Abs_Max_X": f"{max_x_coord:.4f}",
                     })
                pbar.set_description(f"Episode {episode + 1}")
                pbar.update(1)

                # - визуализация
                # - сохранение метрик за эпизод
                plot_metrics(ep_reward, ep_max_x_coord, ep_loss)

        wandb.finish()

    def run_episode(self, start_state: th.Tensor):
        # метод для прогона эпизода
        # - генерация переходов и их сохранение
        done = False
        ep_reward = 0
        ep_x_coords = []
        ep_losses = []
        state = start_state

        while not done:
            action = self.policy.get_best_action(state=state)
            next_state, reward, terminated, truncated, _ = env.step(action)
            ep_x_coords.append(next_state[0])

            update_reward = reward + abs(state[0] - next_state[0]) * 10
            if next_state[0] > 0.5:
                update_reward += 20
            ep_reward += update_reward

            self.memory.push(state, action, next_state, update_reward, terminated or truncated)

            # - запуск генерации батча и обучения (generate_batch_and_fit)
            if len(self.memory) >= self.cfg.batch_size:
                loss = self.generate_batch_and_fit()
                ep_losses.append(loss.item())

            state = next_state
            done = terminated or truncated

        return max(ep_x_coords), ep_reward, np.mean(ep_losses)

    def generate_batch_and_fit(self):
        # генерируем батч на основе хранилища
        transitions = self.memory.sample(self.cfg.batch_size)

        # получаем набор текущих состояний и следующих состояний
        states = th.stack([t.state for t in transitions])
        next_states = th.stack([t.next_state for t in transitions])

        # получаем прогнозы для текущих состояний и следующих состояний
        targets = self.policy.policy_network(states)
        next_state_targets = self.policy.target_network(next_states)

        # модифицируем targets: если сессия закончена, то targets[t.action] = t.reward
        # если нет, то targets[t.action] = t.reward + gamma * max(next_state_targets[i])
        # t - переход из батча с номером i
        for i, t in enumerate(transitions):
            if transitions[i].done:
                targets[transitions[i].action] = transitions[i].reward
            else:
                targets[transitions[i].action] = transitions[i].reward + self.cfg.gamma * max(next_state_targets[i])

        return self.fit_policy_network(states, targets)

    def fit_policy_network(self, X, y):
        # X - батч состояний (batch_size x 2)
        # y - набор Q-значений (batch_size x 3)
        self.optimizer.zero_grad()
        y_pred = self.policy.policy_network(X)
        loss = self.loss_func(y_pred, y)
        loss.backward()
        self.optimizer.step()
        return loss
''')
    elif st == '6':
        print('''
class TransformObservation(gym.ObservationWrapper):
    def __init__(self, env, device):
        self.device = device
        super(TransformObservation, self).__init__(env)

    def observation(self, observation):
        return th.tensor(observation, device=device, dtype=th.float32)

env = gym.make("MountainCar-v0", render_mode="rgb_array")
env = RecordVideo(env,
                  video_folder="videos_MountainCar_DQN",
                  episode_trigger=lambda x: True,
                  name_prefix="rl-MountainCar")
env = TransformObservation(env, device)
              

tr = Trainer(env, TrainConfig(num_episodes=500), Policy(env, PolicyConfig()))
tr.train()
              

# Тест

test_env = gym.make("MountainCar-v0", render_mode="rgb_array")
test_env = RecordVideo(
    test_env,
    video_folder="test_videos_MountainCar_DQN",
    episode_trigger=lambda x: True,
    name_prefix="test-run-MountainCar"
)

policy = Policy(test_env, PolicyConfig())
policy.load()

num_episodes = 50

for episode in range(num_episodes):
    state = test_env.reset()[0]
    done = False
    total_reward = 0

    while not done:
        action = th.argmax(policy.policy_network(th.tensor(state, device=device))).item()
        state, reward, terminated, truncated, _ = test_env.step(action)
        total_reward += reward
        done = terminated or truncated

    print(f"Episode {episode + 1}: Total reward = {total_reward}")

test_env.close()
''')
def polGr_info():
    print('''
ЧТОБЫ ВЫЗВАТЬ КОД: используйте DL.polGr_code("НОМЕР ЗАДАНИЯ")
              
 1. Допишите классы Policy для реализации модели политики и Trainer для реализации процесса обучения модели при помощи алгоритма REINFORCE. 
Настройте агента для игры в окружении CartPole-v1. Визуализируйте динамику значений награды на эпизод в процессе обучения. 
Сыграйте эпизод, используя обученного агента, и убедитесь, что агент выучивается, как стабилизировать шест.
𝐿𝑃𝐺=−∑𝑖𝑅𝑖log𝑝(𝑎𝑖|𝑠𝑖) 
𝑅𝑡=∑𝑘=0∞𝛾𝑘𝑟𝑡+𝑘 
       
2. Повторите решение задачи 1, делая шаг обучения не после одного эпизода, а по результату прогонов нескольких эпизодов.
Обратите внимание, что после обновления весов модели все старые данные для обучения становятся неактуальными и должны быть удалены.
          
3. Повторите решение задачи 1, реализовав алгоритм REINFONCE с baseline.
𝐿𝑃𝐺=−∑𝑖𝐴𝑖log𝑝(𝑎𝑖|𝑠𝑖) 
𝐴𝑖=𝑅𝑖−𝑉(𝑠𝑖) 
𝑅𝑡=∑𝑘=0∞𝛾𝑘𝑟𝑡+𝑘 
где  𝑟𝑡  - награда за шаг  𝑡 .
𝑝(𝑎𝑖|𝑠𝑖)  и  𝑉(𝑠𝑖)  моделируются при помощи двух независимых сетей. 
Сеть для политики настраивается аналогично задаче 1 и 2 при помощи функции потерь  𝐿𝑃𝐺 . 
Сеть для оценки базы настраивается в процессе решения задачи регрессии:  𝐿𝑉=∑𝑖(𝑉(𝑠𝑖)−𝑅𝑖)2 . 
Настройка весов обеих моделей происходит после каждого эпизода.
          
4. Повторите решение задачи 1, реализовав алгоритм Actor-Critic
𝐿𝑃𝐺=−∑𝑖𝐴𝑖log𝑝(𝑎𝑖|𝑠𝑖) 
𝐴𝑖=𝑅𝑖−𝑉(𝑠𝑖) 
𝑅𝑡=∑𝑘=0∞𝛾𝑘𝑟𝑡+𝑘 
где  𝑟𝑡  - награда за шаг  𝑡 .
𝑝(𝑎𝑖|𝑠𝑖)  и  𝑉(𝑠𝑖)  моделируются при помощи одной сети в двумя головами. 
Голова для политики настраивается аналогично задаче 1 и 2 при помощи функции потерь  𝐿𝑃𝐺 . 
Голова для оценки базы настраивается в процессе решения задачи регрессии: 𝐿𝑉=∑𝑖(𝑉(𝑠𝑖)−𝑅𝑖)2 . 
Итоговая функции потерь для настройки представляет из себя сумму функций потерь для голов: 𝐿=𝐿𝑃𝐺+𝐿𝑉 .
          
''')
def polGr_code(st):
    if st == '1':
        print('''
!pip install gymnasium
              
import torch
import gymnasium as gym
import torch.nn as nn
from torch.distributions import Categorical
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
import torch as th
import torch.nn as nn
import torch.optim as optim
from dataclasses import dataclass
import numpy as np
import gymnasium as gym
import matplotlib.pyplot as plt
              

@dataclass
class PolicyConfig:
    n_state: int #4 состояния
    n_action: int #2 (лево , право )
    n_hidden: int #128
              

@dataclass
class TrainConfig:
    gamma: float = 0.99
    learning_rate: float = 0.001
    episode_num: int = 400
              

#берет состояние тележки (вектор из 4) и вычисляет вероятности действий

class PolicyNetwork(nn.Module):
    def __init__(self, policy_config: PolicyConfig):
        super().__init__()
        self.cfg = policy_config
        self.model = nn.Sequential(
            nn.Linear(self.cfg.n_state, self.cfg.n_hidden),
            nn.ReLU(),
            nn.Linear(self.cfg.n_hidden, self.cfg.n_action),
            nn.Softmax(dim=-1)
        )

    def forward(self, s: th.Tensor) -> th.Tensor:
        return self.model(s) #состояние в вероятности

    def get_action(self, s: th.Tensor) -> tuple[int, float]:
        probs = self.forward(s)
        action_dist = th.distributions.Categorical(probs)
        action = action_dist.sample()
        log_prob = action_dist.log_prob(action) #log для функции ошибки
        return action.item(), log_prob
              

class Trainer:
    def __init__(self, env_name: str, policy_config: PolicyConfig, train_config: TrainConfig):
        self.env = gym.make(env_name)
        self.policy = PolicyNetwork(policy_config)
        self.optimizer = optim.Adam(self.policy.parameters(), lr=train_config.learning_rate)
        self.gamma = train_config.gamma
        self.episode_num = train_config.episode_num
        self.rewards_history = []  # Для визуализации

###############################################################

    def train(self):
        for episode in range(self.episode_num):
            log_probs = []
            rewards = []

            state, _ = self.env.reset()
            state = th.tensor(state, dtype=th.float32)

            done = False
            while not done:
                action, log_prob = self.policy.get_action(state)
                log_probs.append(log_prob)


                next_state, reward, done, _, _ = self.env.step(action)
                rewards.append(reward)


                state = th.tensor(next_state, dtype=th.float32)


            discounted_rewards = self.compute_discounted_rewards(rewards)

            loss = self.update_policy(log_probs, discounted_rewards)

            # Логирование
            total_reward = sum(rewards)
            self.rewards_history.append(total_reward)
            print(f"Эпизод {episode + 1}/{self.episode_num}, Награда: {total_reward:.2f}, Потеря: {loss:.4f}")

#######################################################################

    def compute_discounted_rewards(self, rewards: list) -> list:
        discounted_rewards = []
        R = 0
        for reward in reversed(rewards):
            R = reward + self.gamma * R
            discounted_rewards.insert(0, R)
        return discounted_rewards

 #######################################################################

    def update_policy(self, log_probs: list, rewards: list) -> float:
        rewards = th.tensor(rewards, dtype=th.float32) #награды к тензору
        rewards = (rewards - rewards.mean()) / (rewards.std() + 1e-8)


        #gradient policy
        loss = -th.stack([log_prob * reward for log_prob, reward in zip(log_probs, rewards)]).sum()


        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        return loss.item()

###############################################################################

    def plot_rewards(self):
        plt.plot(self.rewards_history)
        plt.xlabel('Эпизод')
        plt.ylabel('Суммарная награда')
        plt.title('Динамика награды на эпизод')
        plt.show()

 ################################################################

    def evaluate(self):
        state, _ = self.env.reset()
        state = th.tensor(state, dtype=th.float32) #приводим состояние к тензору
        done = False
        total_reward = 0

        while not done:
            self.env.render() #визуализируем окружение (насколько хорошо агент обучился)
            action, _ = self.policy.get_action(state)
            next_state, reward, done, _, _ = self.env.step(action)
            state = th.tensor(next_state, dtype=th.float32)
            total_reward += reward

        print(f"Суммарная награда в эпизоде: {total_reward:.2f}")
        self.env.close()
              

env1 = gym.make("CartPole-v1")
              

env1.reset()
              

env1.action_space.n
              

env1.step(1)
              

env1.close()
              

env = gym.make("CartPole-v1")
policy_config = PolicyConfig(n_state=env.observation_space.shape[0], n_action=env.action_space.n, n_hidden=128)
policy_network = PolicyNetwork(policy_config)
train_config = TrainConfig()
              

trainer = Trainer(env, policy_network, train_config)
rewards = trainer.train()
              

plt.plot(rewards)
plt.xlabel('Episode')
plt.ylabel('Total Reward')
plt.title('Training Progress');
              

env = gym.make("CartPole-v1", render_mode='rgb_array')
env = gym.wrappers.RecordVideo(env, 'result1', episode_trigger=lambda x: True)
              

state, _ = env.reset()
state = torch.tensor(state, dtype=torch.float32)
done = False
total_reward = 0
while not done:
    action, _ = policy_network.get_action(state)
    next_state, reward, done, _, _ = env.step(action)
    total_reward += reward
    state = torch.tensor(next_state, dtype=torch.float32)
env.close()
              

total_reward
''')
    elif st == '2':
        print('''
class TrainConfig2:
    gamma: float = 0.99
    learning_rate: float = 0.005
    episode_num: int = 500
    episode_step: int = 10
              

class Trainer:
    def __init__(self, env_name: str, policy_config: PolicyConfig, train_config: TrainConfig, batch_size: int = 10):
        self.env = gym.make(env_name)
        self.policy = PolicyNetwork(policy_config)
        self.optimizer = optim.Adam(self.policy.parameters(), lr=train_config.learning_rate)
        self.gamma = train_config.gamma
        self.episode_num = train_config.episode_num
        self.batch_size = batch_size  # Количество эпизодов в одной обучающей итерации
        self.rewards_history = []

################################################

    def train(self):
        batch_log_probs = []
        batch_rewards = []

        for episode in range(self.episode_num):
            log_probs = []
            rewards = []


            state, _ = self.env.reset()
            state = th.tensor(state, dtype=th.float32)

            done = False
            while not done:
                action, log_prob = self.policy.get_action(state)
                log_probs.append(log_prob)

                next_state, reward, done, _, _ = self.env.step(action)
                rewards.append(reward)


                state = th.tensor(next_state, dtype=th.float32)

           #сохраняем данные
            batch_log_probs.extend(log_probs)
            batch_rewards.append(rewards)

            # Логирование награды
            total_reward = sum(rewards)
            self.rewards_history.append(total_reward)

            print(f"Эпизод {episode + 1}/{self.episode_num}, Награда: {total_reward:.2f}")


            if (episode + 1) % self.batch_size == 0:
                self.update_policy(batch_log_probs, batch_rewards)

                #очищаем данные
                batch_log_probs = []
                batch_rewards = []

##############################################################

    def compute_discounted_rewards(self, rewards: list) -> list:
        discounted_rewards = []
        R = 0
        for reward in reversed(rewards):
            R = reward + self.gamma * R
            discounted_rewards.insert(0, R)
        return discounted_rewards

###################################################################

    def update_policy(self, batch_log_probs: list, batch_rewards: list) -> None:
        all_discounted_rewards = []
        for rewards in batch_rewards:
            discounted_rewards = self.compute_discounted_rewards(rewards)
            all_discounted_rewards.extend(discounted_rewards)


        rewards_tensor = th.tensor(all_discounted_rewards, dtype=th.float32)
        rewards_tensor = (rewards_tensor - rewards_tensor.mean()) / (rewards_tensor.std() + 1e-8)


        loss = -th.stack([log_prob * reward for log_prob, reward in zip(batch_log_probs, rewards_tensor)]).sum()

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        print(f"Обновление модели. Потеря: {loss.item():.4f}")

###########################################################################

    def plot_rewards(self):
        plt.plot(self.rewards_history)
        plt.xlabel('Эпизод')
        plt.ylabel('Суммарная награда')
        plt.title('Динамика награды на эпизод')
        plt.show()

############################################################

    def evaluate(self):
        state, _ = self.env.reset()
        state = th.tensor(state, dtype=th.float32)
        done = False
        total_reward = 0

        while not done:
            self.env.render()
            action, _ = self.policy.get_action(state)
            next_state, reward, done, _, _ = self.env.step(action)
            state = th.tensor(next_state, dtype=th.float32)
            total_reward += reward

        print(f"Суммарная награда в эпизоде: {total_reward:.2f}")
        self.env.close()

##################################################################

# Параметры конфигурации
policy_cfg = PolicyConfig(n_state=4, n_action=2, n_hidden=128)  # CartPole-v1
train_cfg = TrainConfig(gamma=0.99, learning_rate=0.001, episode_num=400)

# Создание и обучение модели
trainer = Trainer(env_name="CartPole-v1", policy_config=policy_cfg, train_config=train_cfg, batch_size=10)
trainer.train()

# Построение графика
trainer.plot_rewards()

# Тестирование
trainer.evaluate()
              

env2 = gym.make("CartPole-v1")
policy_config2 = PolicyConfig(n_state=env.observation_space.shape[0], n_action=env.action_space.n, n_hidden=128)
policy_network2 = PolicyNetwork(policy_config2)
train_config2 = TrainConfig2()
              

trainer2 = Trainer(env2, policy_network2, train_config2)
rewards2 = trainer2.train()
              

plt.plot(rewards2)
plt.xlabel('Episode')
plt.ylabel('Total Reward')
plt.title('Training Progress');
              

env2test = gym.make("CartPole-v1", render_mode='rgb_array')
env2test = gym.wrappers.RecordVideo(env2test, 'result2', episode_trigger=lambda x: True)
              

state, _ = env2test.reset()
state = torch.tensor(state, dtype=torch.float32)
done = False
total_reward = 0
while not done:
    action, _ = policy_network2.get_action(state)
    next_state, reward, done, _, _ = env2test.step(action)
    total_reward += reward
    state = torch.tensor(next_state, dtype=torch.float32)
env2test.close()
              

total_reward
''')
    elif st == '3':
        print('''
@dataclass
class PolicyConfig:
    n_state: int
    n_action: int
    n_hidden: int

#################################################

class PolicyNetwork(nn.Module):
    def __init__(self, policy_config: PolicyConfig):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(policy_config.n_state, policy_config.n_hidden),
            nn.ReLU(),
            nn.Linear(policy_config.n_hidden, policy_config.n_action),
            nn.Softmax(dim=-1)
        )

    def forward(self, s: th.Tensor) -> th.Tensor:
        return self.model(s)

    def get_action(self, s: th.Tensor) -> tuple[int, float]:
        probs = self.forward(s)
        action_dist = th.distributions.Categorical(probs)
        action = action_dist.sample()
        log_prob = action_dist.log_prob(action)
        return action.item(), log_prob

#########################################################
class ValueNetwork(nn.Module):
    def __init__(self, n_state: int, n_hidden: int):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(n_state, n_hidden),
            nn.ReLU(),
            nn.Linear(n_hidden, 1) #оценка v(s)
        )

    def forward(self, s: th.Tensor) -> th.Tensor:
        return self.model(s).squeeze(-1) #(batch_size ,)

######################################################
@dataclass
class TrainConfig:
    gamma: float = 0.99
    learning_rate: float = 0.001
    episode_num: int = 400

#####################################################
class Trainer:
    def __init__(self, env_name: str, policy_config: PolicyConfig, train_config: TrainConfig):
        self.env = gym.make(env_name)
        self.policy = PolicyNetwork(policy_config)
        self.value = ValueNetwork(policy_config.n_state, policy_config.n_hidden)
        self.policy_optimizer = optim.Adam(self.policy.parameters(), lr=train_config.learning_rate)
        self.value_optimizer = optim.Adam(self.value.parameters(), lr=train_config.learning_rate)
        self.gamma = train_config.gamma
        self.episode_num = train_config.episode_num
        self.rewards_history = []
##############################################

    def train(self):
        for episode in range(self.episode_num):
            state, _ = self.env.reset()
            log_probs = []
            rewards = []
            values = []

            done = False
            while not done:
                state_tensor = th.tensor(state, dtype=th.float32)
                action, log_prob = self.policy.get_action(state_tensor)
                value = self.value(state_tensor)

                next_state, reward, done, _, _ = self.env.step(action)
                log_probs.append(log_prob)
                rewards.append(reward)
                values.append(value)

                state = next_state

            returns = self.compute_returns(rewards) # вычисляем накопленные награды с учетом дисконтирования
            advantages = [r - v.item() for r, v in zip(returns, values)] #преимущество

            policy_loss = -th.stack([log_prob * adv for log_prob, adv in zip(log_probs, advantages)]).mean() #PG
            self.policy_optimizer.zero_grad()
            policy_loss.backward()
            self.policy_optimizer.step()

            # Обновляем оценку базы
            returns_tensor = th.tensor(returns, dtype=th.float32)
            values_tensor = th.stack(values)
            value_loss = nn.functional.mse_loss(values_tensor, returns_tensor) #L_v
            self.value_optimizer.zero_grad()
            value_loss.backward()
            self.value_optimizer.step()

            # Логируем и визуализируем
            total_reward = sum(rewards)
            self.rewards_history.append(total_reward)
            print(f"Episode {episode + 1}/{self.episode_num}, Reward: {total_reward:.2f}")

        self.plot_rewards()
####################################################################
    def compute_returns(self, rewards: list[float]) -> list[float]:
        returns = []
        g = 0
        for reward in reversed(rewards):
            g = reward + self.gamma * g
            returns.insert(0, g)
        return returns
########################################################

    def plot_rewards(self):
        plt.plot(self.rewards_history)
        plt.xlabel("Episode")
        plt.ylabel("Total Reward")
        plt.title("Training Progress")
        plt.show()


              
env3 = gym.make("CartPole-v1")
policy_network3 = PolicyNetwork(policy_config)
value_network = ValueNetwork(policy_config)
              

trainer3 = Trainer(env3, policy_network3, value_network, train_config)
rewards3 = trainer3.train()
              

plt.plot(rewards3)
plt.xlabel('Episode')
plt.ylabel('Total Reward')
plt.title('Training Progress');
              

env3test = gym.make("CartPole-v1", render_mode='rgb_array')
env3test = gym.wrappers.RecordVideo(env3test, 'result3', episode_trigger=lambda x: True)
              

state, _ = env3test.reset()
state = torch.tensor(state, dtype=torch.float32)
done = False
total_reward = 0
while not done:
    action, _ = policy_network3.get_action(state)
    next_state, reward, done, _, _ = env3test.step(action)
    total_reward += reward
    state = torch.tensor(next_state, dtype=torch.float32)
env3test.close()
              

total_reward
''')
    elif st == '4':
        print('''
class ActorCriticNetwork(nn.Module):
    def __init__(self, policy_config: PolicyConfig):
        super(ActorCriticNetwork, self).__init__()
        self.cfg = policy_config
        self.shared = nn.Sequential(
            nn.Linear(self.cfg.n_state, self.cfg.n_hidden),
            nn.ReLU()
        )

        self.policy_head = nn.Linear(self.cfg.n_hidden, self.cfg.n_action)

        self.value_head = nn.Linear(self.cfg.n_hidden, 1)

    def forward(self, s: torch.Tensor):
        shared_out = self.shared(s)

        policy_probs = torch.softmax(self.policy_head(shared_out), dim=-1)

        value = self.value_head(shared_out)

        return policy_probs, value

    def get_action(self, s: torch.Tensor) -> tuple[int, float]:
        policy_probs, _ = self.forward(s)
        dist = Categorical(policy_probs)
        action = dist.sample()
        log_prob = dist.log_prob(action)
        return action.item(), log_prob
              

import os
@dataclass
class ActorCriticConfig:
    n_state: int
    n_action: int
    n_hidden: int
    gamma: float
    learning_rate: float
    episode_num: int
###################################################################

class ActorCriticNetwork(nn.Module):
    def __init__(self, config: ActorCriticConfig):
        super().__init__()
        self.shared_layers = nn.Sequential( #извлекаем признаки из состояния
            nn.Linear(config.n_state, config.n_hidden),
            nn.ReLU()
        )
        self.actor_head = nn.Sequential( #p действий
            nn.Linear(config.n_hidden, config.n_action),
            nn.Softmax(dim=-1)
        )
        self.critic_head = nn.Linear(config.n_hidden, 1)  #V(s)



    def forward(self, state: th.Tensor):
        shared_output = self.shared_layers(state)
        policy_probs = self.actor_head(shared_output)
        state_value = self.critic_head(shared_output)
        return policy_probs, state_value

#####################################################
class ActorCriticTrainer:
    def __init__(self, env_name: str, config: ActorCriticConfig):
        self.env = gym.make(env_name)
        self.config = config
        self.model = ActorCriticNetwork(config)
        self.optimizer = optim.Adam(self.model.parameters(), lr=config.learning_rate)
        self.gamma = config.gamma
        self.episode_num = config.episode_num
        self.rewards_history = []


##################################################

    def train(self):
        for episode in range(self.episode_num):
            state, _ = self.env.reset()
            state = th.tensor(state, dtype=th.float32)

            log_probs = []
            values = []
            rewards = []

            done = False
            while not done:

                policy_probs, state_value = self.model(state)
                action_dist = th.distributions.Categorical(policy_probs)
                action = action_dist.sample()

                log_prob = action_dist.log_prob(action)
                log_probs.append(log_prob)
                values.append(state_value)


                next_state, reward, done, _, _ = self.env.step(action.item())
                rewards.append(reward)

                state = th.tensor(next_state, dtype=th.float32)

            # Вычисление функции потерь и обновление параметров
            self.update_policy_and_value(log_probs, values, rewards)

            # Логирование
            total_reward = sum(rewards)
            self.rewards_history.append(total_reward)
            print(f"Эпизод {episode + 1}/{self.episode_num}, Награда: {total_reward:.2f}")
####################################################################################

    def update_policy_and_value(self, log_probs, values, rewards):
        rewards = self.compute_discounted_rewards(rewards)
        rewards = th.tensor(rewards, dtype=th.float32)

        log_probs = th.stack(log_probs)
        values = th.cat(values).squeeze()

        # Вычисление функций потерь
        advantages = rewards - values.detach()
        policy_loss = -(log_probs * advantages).mean()  # L_PG
        value_loss = nn.functional.mse_loss(values, rewards)  # L_V

        loss = policy_loss + value_loss


        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

#########################################################################

    def compute_discounted_rewards(self, rewards):
        discounted_rewards = []
        R = 0
        for reward in reversed(rewards):
            R = reward + self.gamma * R
            discounted_rewards.insert(0, R)
        return discounted_rewards

#############################################################################
    def plot_rewards(self):
        plt.plot(self.rewards_history)
        plt.xlabel('Эпизод')
        plt.ylabel('Суммарная награда')
        plt.title('Динамика награды на эпизод')
        plt.show()


env4 = gym.make("CartPole-v1")
actor_critic_network = ActorCriticNetwork(policy_config)
              

trainer4 = Trainer(env4, actor_critic_network, train_config)
rewards4 = trainer4.train()
              

plt.plot(rewards4)
plt.xlabel('Episode')
plt.ylabel('Total Reward')
plt.title('Training Progress');
              

env4test = gym.make("CartPole-v1", render_mode='rgb_array')
env4test = gym.wrappers.RecordVideo(env4test, 'result4', episode_trigger=lambda x: True)
              

state, _ = env4test.reset()
state = torch.tensor(state, dtype=torch.float32)
done = False
total_reward = 0
while not done:
    action, _ = actor_critic_network.get_action(state)
    next_state, reward, done, _, _ = env4test.step(action)
    total_reward += reward
    state = torch.tensor(next_state, dtype=torch.float32)
env4test.close()
              


total_reward
''')
        
def obDet_info():
    print('''
ЧТОБЫ ВЫЗВАТЬ КОД: используйте DL.obDet_code("НОМЕР ЗАДАНИЯ")          

1. Напишите функцию parse_xml, которая читает xml-файл с разметкой изображения из архива animals.zip и возвращает словарь, содержащий три ключа:
{
        "raw": # словарь с ключами xmin, ymin, xmax, ymax
        "scaled": # словарь с ключами xmin, ymin, xmax, ymax
        "obj_name": # строка
}
В этом словаре row - абсолютные значения координат вершин bounding box, а scaled - относительные (нормированные на ширину и высоту изображения). 
Примените функцию к файлу cat.0.xml и выведите результат на экран.
          
2. Опишите датасет AnimalDetectionDataset на основе архива animals.zip. Реализуйте __getitem__ таким образом, чтобы он возвращал три элемента: 
тензор с изображением, словарь с координатами bounding box и метку объекта. 
Предусмотрите возможность передавать извне при создании датасета набор преобразований для изображений, преобразование для метки объекта 
(для кодирования) и флаг, показывающий, нужно ли возвращать исходные или нормированные координаты bounding box.
          
3. Создайте объект класса AnimalDetectionDataset без применения преобразований и со значением return_scaled=False. 
Напишите функцию show_image_with_bounding_box для визуализации изображения с добавлением на него bounding box и подписи объекта. 
Продемонстрируйте работу функцию на изображении собаки и кошки.
          
4. Напишите модель для решения задачи выделения объектов. 
Реализуйте двухголовую сеть, одна голова которой предсказывает метку объекта (задача классификации), а вторая голова 
предсказывает 4 координаты вершин bounding box (задача регрессии). В качестве backbone используйте модель resnet50 из пакета torchvision.
          
5. Разбейте набор данных на обучающее и валидационное множество. Обучите модель, описанную в задаче 4. 
При создании датасета не забудьте указать преобразования, соответствующие модели ResNet.
Используйте сумму MSELoss (для расчета ошибки на задаче регрессии) и CrossEntropyLoss (для расчета ошибки на задачи классификации) для настройки весов модели.
Для ускорения процесса обучения слои backbone можно заморозить. Во время обучения выводите на экран значения функции потерь на обучающем и валидационном множестве. 
Используя обученную модель, получите предсказания для изображения кошки и собаки и отрисуйте их. 
Выполните процедуру, обратную нормализации, чтобы корректно отобразить фотографии.
          
6. Найдите в сети несколько изображений котов и собак. 
Используя любой инструмент для разметки (например, CVAT), выделите котов и собак на изображениях. 
Вставьте скриншот экспортированного файла с разметкой. 
Используя полученные изображения, визуализируйте разметку и bounding boxes, полученные при помощи модели.
          
7*. Повторите решение предыдущей задачи, используя модель fasterrcnn_resnet50_fpn. 
Замените слой для предсказания bounding box на FastRCNNPredictor с нужным количеством классов.
''')
    
def obDet_code(st):
    if st == '1':
        print('''
import os
import xml.etree.ElementTree as ET #модуль для работы с хмл
import torch
import torch.nn as nn
from torch.utils.data import Dataset #класс пайторч для работы с наборами данных
from torchvision.models import resnet50
from torchvision import transforms as T
from PIL import Image
import matplotlib.pyplot as plt
import torchvision.transforms as T #импортируем трансформ
from torch.utils.data import DataLoader #импортируем даталоадер для загрузки данных в батчи
import matplotlib.patches as patches #модуль патчес для создания бб
from torchvision.transforms import ToPILImage #тензор в пил картинку
import torchvision
from torchvision import models
from torchvision.transforms import ToTensor, Normalize, Compose
from torch.utils.data import DataLoader, random_split
from torchvision.transforms import Resize
import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torch.utils.data import DataLoader, Dataset
from torchvision.transforms.functional import hflip, rotate
import zipfile
              

zip_file_path = '/content/Asirra- cat vs dogs 2.zip'
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall()
              

def parse_xml(file_path):

    #читаем хмл файл с использованием пути файла
    #результат - ElementTree со структурой хмл дока
    tree = ET.parse(file_path)

    root = tree.getroot() #получаем корневой элемент



 #############################################
    #РАЗМЕРЫ ИЗОБРАЖЕНИЯ
    #size внутри корневого элемента ищем сайз
    size = root.find("size")

    #находим внутри сайз видз и хейт извлекаем и делаем интеджером
    img_width = int(size.find("width").text)
    img_height = int(size.find("height").text)



############################################
    #BOUNDING BOX
    #ищем обджект который содержит инфу кто на картинке (кот, собака)
    obj = root.find("object")

    #ищем баундинг бокс который содержит инфу о координатах
    bndbox = obj.find("bndbox")

    #левый верхний и правый нижний углы и делаем флоатом
    xmin = float(bndbox.find("xmin").text)
    ymin = float(bndbox.find("ymin").text)
    xmax = float(bndbox.find("xmax").text)
    ymax = float(bndbox.find("ymax").text)



########################################
    #КООРДИНАТЫ
    #абсолютные координаты (инфа о баундинг бокс взятая из хмл)
    #подходят для визуализации бб на самом изображении
    raw = {"xmin": xmin, "ymin": ymin, "xmax": xmax, "ymax": ymax}

    #нормированные координаты (масштабированные в диапазоне 0-1 [абсолютные/width or height])
    #важны, потому что если модель будет обучаться на абсолютных координатах и размер изображения поменяется
    #модель не сможет нормально обучиться (определять объекты) на картинках другого размера
    scaled = {
        "xmin": xmin / img_width,
        "ymin": ymin / img_height,
        "xmax": xmax / img_width,
        "ymax": ymax / img_height,
    }


######################################
    #извлекаем имя объекта
    obj_name = obj.find("name").text

    return {
        "raw": raw,
        "scaled": scaled,
        "obj_name": obj_name,
    }


######################################
xml_file_path = '/content/Asirra- cat vs dogs/cat.0.xml'
result = parse_xml(xml_file_path)
result
''')
    elif st == '2':
        print('''
class AnimalDetectionDataset(Dataset):
    def __init__(self, root_dir, transform=None, label_transform=None, return_scaled=False):

       #КОНСТРУКТОР КЛАССА
        self.root_dir = root_dir

        #конструктор класса (transfrom, label_transform по умолчанию None)
        self.transform = transform
        self.label_transform = label_transform

        #return_scaled (True - нормированные координаты, False - абсолютные [по умолчанию фолс])
        self.return_scaled = return_scaled

        #для каждог jpg есть свой xml
        self.image_files = sorted(
            [f for f in os.listdir(root_dir) if f.endswith(".jpg")]
        )
        self.annotation_files = sorted(
            [f for f in os.listdir(root_dir) if f.endswith(".xml")]
        )
######################################################

    #РАЗМЕР ДАТАСЕТА
    def __len__(self):
        return len(self.image_files)

####################################################

    def __getitem__(self, idx):
      #возвращает один образец данных (изображение, бб, лэйбл) по заданному индексу
        #изображение
        img_path = os.path.join(self.root_dir, self.image_files[idx])
        image = Image.open(img_path).convert("RGB") #загружает изобр и конвертирует в РГБ

        #аннотация
        xml_path = os.path.join(self.root_dir, self.annotation_files[idx])
        annotation = parse_xml(xml_path) #выдает нормированные, абсолютные координаты и кто на кратинке

        #координаты выбираются в зависимости от значения self.returned_scaled
        bbox = annotation["scaled"] if self.return_scaled else annotation["raw"]
        label = annotation["obj_name"]

        #преобразования (transform)
        if self.transform:
            image = self.transform(image)
        if self.label_transform:
            label = self.label_transform(label)

        return image, bbox, label
              


transform = T.Compose([ #компоуз принимает список преобразований и приеняет их последовательно
    T.Resize((224, 224)),
    T.ToTensor() #из ПИЛ в торч тензор
])

#функция - метка в число (индекс)
def label_transform(label):
    label_map = {"cat": 0, "dog": 1}
    return label_map[label]
              

root_dir = "/content/Asirra: cat vs dogs"


dataset = AnimalDetectionDataset(
    root_dir=root_dir,
    transform=transform,
    label_transform=label_transform,
    return_scaled=True
)

len(dataset)
              

data_loader = DataLoader(dataset, batch_size=4, shuffle=True)

for images, bboxes, labels in data_loader:
    print("Batch of images shape:", images.shape)
    print("Bounding boxes:", bboxes)
    print("Labels:", labels)
    break
''')
    elif st == '3':
        print('''
def show_image_with_bounding_box(image, bbox, label):

    #ПРОВЕРЯЕМ КЛАСС
    #isinstance проверяет является ли объект отпределенного класса или нет
    if isinstance(image, torch.Tensor):
        image = ToPILImage()(image)

    fig, ax = plt.subplots(1)
    ax.imshow(image)

######################################
    #ДОБАВЛЯЕМ ББ
    rect = patches.Rectangle(
        (bbox['xmin'], bbox['ymin']), #верхний левый угол , берем из файла хмл
        bbox['xmax'] - bbox['xmin'],
        bbox['ymax'] - bbox['ymin'],
        linewidth=2, edgecolor='r', facecolor='none'
    )
    ax.add_patch(rect)

    #подпись
    ax.text(
        bbox['xmin'], bbox['ymin'] - 10, label,
        color='red', fontsize=12, bbox=dict(facecolor='white', alpha=0.5)
    )

    plt.axis('off')
    plt.show()
              


dataset = AnimalDetectionDataset(
    root_dir='/content/Asirra: cat vs dogs',
    transform=None,
    label_transform=None,
    return_scaled=False #абсолютные координаты, потому что не нужно обучать
)

################################
cat_image, cat_bbox, cat_label = dataset[0]
show_image_with_bounding_box(cat_image, cat_bbox, cat_label)

dog_image, dog_bbox, dog_label = dataset[666]
show_image_with_bounding_box(dog_image, dog_bbox, dog_label)
''')
    elif st == '4':
        print('''
class TwoHeadedObjectDetectionModel(nn.Module):
    def __init__(self, num_classes=2):  # num_classes: количество классов (например, cat и dog)
        super(TwoHeadedObjectDetectionModel, self).__init__()

        # Используем ResNet50 в качестве backbone
        resnet50 = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)  # Используем параметр 'weights'

        # Удаляем последний fully connected слой (fc)
        self.backbone = nn.Sequential(*list(resnet50.children())[:-2])

        # Для классификации (предсказание метки объекта)
        self.classification_head = nn.Linear(2048 * 7 * 7, num_classes)

        # Для регрессии (предсказание координат bounding box)
        self.bbox_head = nn.Linear(2048 * 7 * 7, 4)  # 4 координаты bounding box (xmin, ymin, xmax, ymax)

        # Выравнивание выхода перед подачей в полносвязные слои
        self.flatten = nn.Flatten(start_dim=1)

    def forward(self, x):
        # Пропускаем вход через backbone
        x = self.backbone(x)

        # Печать размеров выходных данных из backbone
        print("Shape after backbone:", x.shape)

        # Применяем выравнивание (flatten) для получения одномерного вектора
        x = self.flatten(x)

        # Печать размеров после flatten
        print("Shape after flatten:", x.shape)

        # Получаем предсказания для классификации
        class_preds = self.classification_head(x)

        # Получаем предсказания для bounding box
        bbox_preds = self.bbox_head(x)

        return class_preds, bbox_preds

# Пример создания модели
model = TwoHeadedObjectDetectionModel(num_classes=2)  # Например, 2 класса (cat и dog)

# Пример входа (батч из 4 изображений размером 3x224x224)
example_input = torch.randn(4, 3, 224, 224)

# Получаем предсказания
class_preds, bbox_preds = model(example_input)

# Выводим результаты
print("Class predictions shape:", class_preds.shape)  # [batch_size, num_classes]
print("Bounding box predictions shape:", bbox_preds.shape)  # [batch_size, 4]
              


class ImprovedObjectDetectionModel(nn.Module):
    def __init__(self, num_classes=2): #конструктор, два класса кошка собака
        super(ImprovedObjectDetectionModel, self).__init__()

        #BACKBONE
        resnet50 = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
        self.backbone = nn.Sequential(*list(resnet50.children())[:-2]) #последние 2 исп для классификации


##################################################
        #ДОПОЛНИТЕЛЬНЫЕ СВЕРТОЧНЫЕ СЛОИ
        #уменьшают размерность признаков + извлекают более специфичные признаки
        #kernel матрица весов * на подматрицу входного тензора
        #in_channels = 2048 - кол-во каналов на выходе бэкбон
        self.extra_conv1 = nn.Conv2d(2048, 1024, kernel_size=3, stride=1, padding=1)

        self.extra_bn1 = nn.BatchNorm2d(1024)
        #нормализация данных в батче по каждому каналу (mean и std)
        #централизация значений (значения активации центрируются вокруг нуля[activation - mean_channel])
        #нормализация (activation - mean_channel)/std_channel , нормализует act => var = 0
        #масштабирование и сдвиг (после normalization act масштаб с gamma и сдвиг с beta), модель учится на опт масшт и сдвигу на каждом channel

        self.extra_conv2 = nn.Conv2d(1024, 512, kernel_size=3, stride=1, padding=1)

        self.extra_bn2 = nn.BatchNorm2d(512)

        self.extra_conv3 = nn.Conv2d(512, 256, kernel_size=3, stride=1, padding=1)

        self.extra_bn3 = nn.BatchNorm2d(256)


###################################################
        #GLOBAL AVERAGE POOLING
        #карта признаков в тензор для полносвязного слоя
        #AdaptiveAvgPool2d вычисляет средннее по width и height
        self.global_pool = nn.AdaptiveAvgPool2d((1, 1))
        self.flatten = nn.Flatten()


###################################################
        #CLASSIFICATION HEAD
        self.classification_head = nn.Sequential(
            #y = xw + b (w = 512 * 256, b = 512 * 1)
            nn.Linear(256, 512),

            #inplace = True - не создается новый тензор для записи результатов
            nn.ReLU(inplace=True),
            nn.BatchNorm1d(512),
            #зануляет некоторые градиенты
            nn.Dropout(0.5),
            nn.Linear(512, num_classes)
        )


##################################################
        #REGRESSION HEAD
        self.bbox_head = nn.Sequential(
            nn.Linear(256, 512),
            nn.ReLU(inplace=True),
            nn.BatchNorm1d(512),
            nn.Dropout(0.5),

            #4 тк xmin, ymin, xmax, ymax
            nn.Linear(512, 4)
        )



################################################
    #FORWARD PASS
    def forward(self, x):

        x = self.backbone(x)

        #дополнительные сверточные слои
        x = nn.ReLU(inplace=True)(self.extra_bn1(self.extra_conv1(x)))
        x = nn.ReLU(inplace=True)(self.extra_bn2(self.extra_conv2(x)))
        x = nn.ReLU(inplace=True)(self.extra_bn3(self.extra_conv3(x)))

        #GA + flatten
        x = self.global_pool(x)
        x = self.flatten(x)

        #result
        class_preds = self.classification_head(x)
        bbox_preds = self.bbox_head(x)
        return class_preds, bbox_preds

###############################################
    #ФУНКЦИЯ ПОТЕРЬ
    def compute_loss(self, class_preds, bbox_preds, labels, bboxes):
        #кросс энтропия для классификации
        criterion_class = nn.CrossEntropyLoss()
        loss_class = criterion_class(class_preds, labels)

        #смус1 лос для регрессии
        criterion_bbox = nn.SmoothL1Loss()
        loss_bbox = criterion_bbox(bbox_preds, bboxes)

        #общая потеря
        return loss_class + loss_bbox


#Для каждого примера в батче, CrossEntropyLoss вычисляется как: -sum(yi) * logpi
#smoothloss
# это функция потерь, используемая для задач регрессии, особенно когда нужно предсказать координаты
#(например, для bounding box в задачах детекции объектов). Она сочетает в себе лучшие качества L1 и L2 потерь, что делает
#её менее чувствительной к выбросам, чем L2 Loss (среднеквадратичная ошибка).
#loss = 0.5 * x^2    if |x| < 1
#loss = |x| - 0.5    if |x| >= 1
''')
    elif st == '5':
        print('''
transform = Compose([
    Resize((224, 224)),
    ToTensor(),
    Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))
])


##############################################
root_dir = "/content/Asirra- cat vs dogs"
dataset = AnimalDetectionDataset(root_dir=root_dir, transform=transform, return_scaled=True)


##############################################
#обучающая и валидационная выборка
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])


##############################################
#DataLoader
#collate_fn=lambda x: tuple(zip(*x) для структурирования данных
train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True, collate_fn=lambda x: tuple(zip(*x)))
val_loader = DataLoader(val_dataset, batch_size=4, shuffle=False, collate_fn=lambda x: tuple(zip(*x)))
              


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = ImprovedObjectDetectionModel(num_classes=2).to(device)


###################################################
#замораживаем слои backbone, так как используем предобученные веса
for param in model.backbone.parameters():
    param.requires_grad = False


###################################################
#оптимизатор для обновления параметров модели
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)


###################################################
#функции потерь
criterion_class = nn.CrossEntropyLoss()
criterion_bbox = nn.MSELoss()
              


model
              


for name, param in model.state_dict().items():
    print(f"{name}: {param.shape}")
              

#веса для первого слоя модели
print(model.state_dict()['backbone.0.weight'])
              

# Создаем экземпляр модели
model = ImprovedObjectDetectionModel()

# Получаем количество классов из последнего линейного слоя
def get_num_classes(model):
    # Последний слой в classification_head должен быть Linear
    last_layer = list(model.classification_head.children())[-1]
    if isinstance(last_layer, nn.Linear):
        return last_layer.out_features
    else:
        raise ValueError("Не удалось определить количество классов: последний слой не является nn.Linear")

num_classes = get_num_classes(model)
print(f"Количество классов: {num_classes}")
              

label_map = {"cat": 0, "dog": 1}  # Пример маппинга: cat -> 0, dog -> 1
              

def train_epoch(model, loader, optimizer, device):
    #МОДЕЛЬ В РЕЖИМ ОБУЧЕНИЯ
    #drop out случайным образом отключает нейроны
    #batchnorm вычисляет mean и std активаций по батчу + накапливает mean и var по всем батчам
    model.train()
    epoch_loss = 0
    for images, bboxes, labels in loader:
        #объединяет изображения (уже существующие тензоры) в один тензор -> на устройство
        images = torch.stack(images).to(device)

        #словари координат в тензор -> на устройство
        bboxes = torch.tensor([list(b.values()) for b in bboxes]).to(device)

        #список текстовых меток в тензор численных значений
        labels = torch.tensor([label_map[label] for label in labels]).to(device)

        #изображения в модель => preds
        class_preds, bbox_preds = model(images)

        #потеря
        loss_class = criterion_class(class_preds, labels)
        loss_bbox = criterion_bbox(bbox_preds, bboxes)
        loss = loss_class + loss_bbox

        #шаг
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()

    return epoch_loss / len(loader) #средняя потеря за эпоху


############################################################
#МОДЕЛЬ В РЕЖИМ ВАЛИДАЦИИ
#drop out отключается, все нейроны участвуют
#batchnorm использует накопленные std и var для дальнейшей нориализации (центрирование, масштабирование и смешщение)
def validate_epoch(model, loader, device):
    model.eval()
    epoch_loss = 0
    with torch.no_grad():
        for images, bboxes, labels in loader:

            images = torch.stack(images).to(device)
            bboxes = torch.tensor([list(b.values()) for b in bboxes]).to(device)

            labels = torch.tensor([label_map[label] for label in labels]).to(device)  # Преобразование строк в числа

            class_preds, bbox_preds = model(images)

            loss_class = criterion_class(class_preds, labels)
            loss_bbox = criterion_bbox(bbox_preds, bboxes)
            loss = loss_class + loss_bbox
            epoch_loss += loss.item()

    return epoch_loss / len(loader)


############################################################
num_epochs = 50
for epoch in range(num_epochs):
    train_loss = train_epoch(model, train_loader, optimizer, device)
    val_loss = validate_epoch(model, val_loader, device)
    print(f"Epoch {epoch+1}/{num_epochs}, Train Loss: {train_loss:.4f}, Val Loss: {val_loss:.4f}")
              

#ДЕНОРМАЛИЗАЦИЯ ИЗОБРАЖЕНИЙ
#обратное формуле normalized_image = (image - mean) / std для каждого канала
def denormalize_image(image, mean, std):
    for c in range(3):
        image[c] = image[c] * std[c] + mean[c]
    return image


############################################################
#ОТОБРАЖЕНИЕ ИЗОБРАЖЕНИЙ
def show_image(image):
    image = denormalize_image(image, mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))
    #делаем формат h w c для matplotlib , pytorch c h w
    plt.imshow(image.permute(1, 2, 0).numpy())
    plt.axis('off')
    plt.show()
              

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import torch

# Денормализация bounding box (обратная операция нормализации)
def denormalize_bbox(bbox, width, height):
    """Денормализует bounding box на основе ширины и высоты изображения."""
    x_min, y_min, x_max, y_max = bbox
    x_min = x_min * width
    y_min = y_min * height
    x_max = x_max * width
    y_max = y_max * height
    return [x_min, y_min, x_max, y_max]

# Денормализация изображения
def denormalize_image(image, mean, std):
    for c in range(3):
        image[c] = image[c] * std[c] + mean[c]
    return image

# Отображение изображения
def show_image(image):
    image = denormalize_image(image, mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))
    # преобразуем формат (c, h, w) в (h, w, c) для matplotlib
    plt.imshow(image.permute(1, 2, 0).numpy())
    plt.axis('off')
    plt.show()

# Визуализация предсказаний модели
def visualize_predictions(model, loader, device, num_examples=10):
    model.eval()
    class_map = {0: 'cat', 1: 'dog'}

    fig, axes = plt.subplots(5, 2, figsize=(16, 20))
    axes = axes.flatten()
    images_shown = 0

    with torch.no_grad():
        for images, bboxes, labels in loader:
            images = torch.stack(images).to(device)
            bboxes = torch.tensor([list(b.values()) for b in bboxes]).to(device)
            labels = torch.tensor([label_map[label] for label in labels]).to(device)

            class_preds, bbox_preds = model(images)

            images = images.cpu()
            bboxes = bboxes.cpu()
            labels = labels.cpu()
            class_preds = class_preds.cpu()
            bbox_preds = bbox_preds.cpu()

            for i in range(images.size(0)):
                if images_shown >= num_examples:
                    break

                ax = axes[images_shown]

                image = images[i].permute(1, 2, 0).numpy()
                true_bbox = bboxes[i].numpy()
                true_label = labels[i].item()
                pred_bbox = bbox_preds[i].numpy()
                pred_label_idx = torch.argmax(class_preds[i]).item()
                pred_label = class_map[pred_label_idx]
                true_label_str = class_map[true_label]

                # Получаем размеры изображения
                height, width = image.shape[:2]

                # Денормализуем bounding boxes
                true_bbox = denormalize_bbox(true_bbox, width, height)
                pred_bbox = denormalize_bbox(pred_bbox, width, height)

                ax.imshow(image)

                # Рисуем bounding box для истинных координат
                rect_true = patches.Rectangle(
                    (true_bbox[0], true_bbox[1]), true_bbox[2] - true_bbox[0],
                    true_bbox[3] - true_bbox[1], linewidth=2, edgecolor='green', facecolor='none'
                )
                ax.add_patch(rect_true)

                # Рисуем bounding box для предсказанных координат
                rect_pred = patches.Rectangle(
                    (pred_bbox[0], pred_bbox[1]), pred_bbox[2] - pred_bbox[0],
                    pred_bbox[3] - pred_bbox[1], linewidth=2, edgecolor='red', facecolor='none'
                )
                ax.add_patch(rect_pred)

                # Добавляем текстовые метки
                ax.text(
                    true_bbox[0], true_bbox[1] - 10,
                    f"True: {true_label_str}", color='green', fontsize=10,
                    bbox=dict(facecolor='white', alpha=0.5, edgecolor='none')
                )
                ax.text(
                    pred_bbox[0], pred_bbox[1] - 10,
                    f"Pred: {pred_label}", color='red', fontsize=10,
                    bbox=dict(facecolor='white', alpha=0.5, edgecolor='none')
                )

                ax.axis('off')
                images_shown += 1

            if images_shown >= num_examples:
                break

        plt.tight_layout()
        plt.show()

# Визуализируем предсказания
visualize_predictions(model, val_loader, device, num_examples=10)
''')
    elif st == '6':
        print('''
zip_file_path = '/content/labels_dl 2.zip'
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall()
              
xml_file_path = '/content/labels_dl 2/cat2.xml'
result = parse_xml(xml_file_path)
result
              

transform = T.Compose([
    T.Resize((224, 224)),
    T.ToTensor()
])


############################################
root_dir = "/content/labels_dl 2"


############################################
dataset = AnimalDetectionDataset(
    root_dir=root_dir,
    transform=transform,
    label_transform=label_transform,
    return_scaled=False
)

len(dataset)
              


data_loader = DataLoader(dataset, batch_size=4, shuffle=True)


######################################################
for images, bboxes, labels in data_loader:
    print("Batch of images shape:", images.shape)
    print("Bounding boxes:", bboxes)
    print("Labels:", labels)
    break
              


dataset = AnimalDetectionDataset(
    root_dir="/content/labels_dl 2",
    transform=None,
    label_transform=None,
    return_scaled=False
)


##########################################################
cat_image, cat_bbox, cat_label = dataset[0]
show_image_with_bounding_box(cat_image, cat_bbox, cat_label)


dog_image, dog_bbox, dog_label = dataset[-1]
show_image_with_bounding_box(dog_image, dog_bbox, dog_label)
''')
    elif st == '7':
        print('''
# Парсинг XML-аннотации
def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    bboxes = []
    labels = []
    for obj in root.findall("object"):
        name = obj.find("name").text.strip()
        bbox = obj.find("bndbox")
        xmin = float(bbox.find("xmin").text)
        ymin = float(bbox.find("ymin").text)
        xmax = float(bbox.find("xmax").text)
        ymax = float(bbox.find("ymax").text)

        # Проверка валидности bounding box
        if xmax > xmin and ymax > ymin:
            bboxes.append([xmin, ymin, xmax, ymax])
            labels.append(name)
    return {"bboxes": bboxes, "labels": labels}

# Класс датасета для Faster R-CNN
class AnimalDetectionDataset(Dataset):
    def __init__(self, root_dir, transform=None, augment=False):
        self.root_dir = root_dir
        self.image_files = sorted([f for f in os.listdir(root_dir) if f.endswith(".png")])
        self.annotation_files = sorted([f for f in os.listdir(root_dir) if f.endswith(".xml")])
        self.transform = transform
        self.augment = augment
        self.label_map = {"cat": 1, "dog": 2}  # 1: кошка, 2: собака

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        img_path = os.path.join(self.root_dir, self.image_files[idx])
        xml_path = os.path.join(self.root_dir, self.annotation_files[idx])

        image = Image.open(img_path).convert("RGB")
        annotation = parse_xml(xml_path)
        bboxes = torch.tensor(annotation["bboxes"], dtype=torch.float32)
        labels = torch.tensor([self.label_map[label] for label in annotation["labels"]], dtype=torch.int64)

        if self.augment:
            # Применяем простые аугментации
            if torch.rand(1).item() > 0.5:
                image = hflip(image)
                bboxes[:, [0, 2]] = image.width - bboxes[:, [2, 0]]  # Корректировка боксов
            if torch.rand(1).item() > 0.5:
                angle = torch.randint(-30, 30, (1,)).item()
                image = rotate(image, angle)

        if self.transform:
            image = self.transform(image)

        target = {"boxes": bboxes, "labels": labels}
        return image, target

# Преобразования для изображений
transform = T.Compose([
    T.ToTensor(),
])

# Путь к данным
root_dir = "/content/labels_dl 2"
dataset = AnimalDetectionDataset(root_dir=root_dir, transform=transform, augment=True)
data_loader = DataLoader(dataset, batch_size=2, shuffle=True, collate_fn=lambda x: tuple(zip(*x)))

# Инициализация модели Faster R-CNN
num_classes = 3  # Кошка, собака и фон
model = fasterrcnn_resnet50_fpn(pretrained=True)
in_features = model.roi_heads.box_predictor.cls_score.in_features
model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

# Оптимизатор
optimizer = torch.optim.Adam(model.parameters(), lr=0.0001, weight_decay=1e-4)

# Обучение модели
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

epoch_losses = []
num_epochs = 20

for epoch in range(num_epochs):
    model.train()
    epoch_loss = 0
    for images, targets in data_loader:
        images = [img.to(device) for img in images]
        targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

        optimizer.zero_grad()
        loss_dict = model(images, targets)
        losses = sum(loss for loss in loss_dict.values())
        losses.backward()
        optimizer.step()

        epoch_loss += losses.item()

    epoch_losses.append(epoch_loss)
    print(f"Epoch {epoch + 1}/{num_epochs}, Total Loss: {epoch_loss:.4f}, Components: {loss_dict}")

# График функции потерь
plt.plot(range(1, num_epochs + 1), epoch_losses, marker='o')
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss")
plt.show()

# Визуализация предсказаний
def visualize_predictions(model, dataset, idx):
    model.eval()
    image, target = dataset[idx]
    with torch.no_grad():
        prediction = model([image.to(device)])[0]

    image = image.permute(1, 2, 0).cpu().numpy()
    plt.imshow(image)
    ax = plt.gca()

    for bbox, label in zip(target["boxes"], target["labels"]):
        xmin, ymin, xmax, ymax = bbox.tolist()
        rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                                 linewidth=2, edgecolor="r", facecolor="none")
        ax.add_patch(rect)
        ax.text(xmin, ymin - 10, f"True: {label.item()}", color="red", fontsize=12)

    for bbox, label, score in zip(prediction["boxes"], prediction["labels"], prediction["scores"]):
        if score > 0.5:
            xmin, ymin, xmax, ymax = bbox.tolist()
            rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                                     linewidth=2, edgecolor="blue", facecolor="none", linestyle="--")
            ax.add_patch(rect)
            ax.text(xmin, ymax + 10, f"Pred: {label.item()} ({score:.2f})", color="blue", fontsize=12)

    plt.axis("off")
    plt.show()

# Пример визуализации
visualize_predictions(model, dataset, idx=0)
''')
    else:
        print('no such index')
def imSeg_info():
    print('''
ЧТОБЫ ВЫЗВАТЬ КОД: используйте DL.imSeg_code("НОМЕР ЗАДАНИЯ")    

1. Опишите датасет ClothesSegmentationDataset. Реализуйте __getitem__ таким образом, чтобы он возвращал два элемента: тензор с изображением и тензор с маской. 
Маска должна быть представлена трехмерным тензором целых чисел. 
Предусмотрите возможность передавать извне при создании датасета набор преобразований для изображений и масок. 
Создайте объект датасета и выведите на экран форму и типы одного изображения и его маски.   
          
2. Напишите функцию show_image_with_mask, которая выводит рядом два изображения: фотографию и маску. 
Продемонстрируйте работу функции, взяв один пример из созданного датасета.
          
3. Реализуйте архитектуру U-Net. Реализуйте модель таким образом, чтобы на выходе для каждого изображения получался 
тензор размера n_classes x h x w, где n_classes - количество уникальных значений в масках, а h и w - размер исходного изображения. 
Возьмите один пример из набора данных и пропустите его через сеть. Выведите форму полученного результата на экран.
          
4. Разбейте набор данных на обучающее и валидационное множество. Обучите модель U-Net для сегментации изображения. 
Во время обучения выводите на экран значения функции потерь и точности прогнозов на обучающем и валидационном множестве. Обратите внимание, что выборка является несбалансированной. При расчете функции потерь примените любую известную вам технику для работы с несбалансированными выборками.
При создании датасета допускается использовать преобразования, уменьшающие размер изображений (для ускорения процесса обучения).
Используя обученную модель, получите предсказания для нескольких изображений и отрисуйте их.
          
5. Обучите модуль SegformerForSemanticSegmentation из пакета transformers для сегментации изображения. 
Во время обучения выводите на экран значения функции потерь и точности прогнозов на обучающем и валидационном множестве.
Для оптимизации используйте значение функции потерь, которое возвращает вам модель.
Используя обученную модель, получите предсказания для нескольких изображений и отрисуйте их.
''')
def imSeg_code(st):
    if st == '1':
        print('''
import os
from PIL import Image
import torch
from torch.utils.data import Dataset
from torchvision import transforms
import kagglehub
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, random_split
from torchvision import transforms
from torch.utils.data import Dataset
import numpy as np
import torch
from transformers import SegformerForSemanticSegmentation, SegformerImageProcessor
from torch.utils.data import DataLoader, Dataset
from torchvision.transforms import Compose, ToTensor, Normalize
import numpy as np
from torch.optim import AdamW
from tqdm import tqdm
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader, Subset
import torchvision
              

import kagglehub

# Download latest version
path = kagglehub.dataset_download("rajkumarl/people-clothing-segmentation")

print("Path to dataset files:", path)
              

print("Файлы и папки в директории:", os.listdir(path))
              

print("Файлы в png_images:", os.listdir(os.path.join(path, "png_images"))[:5])
print("Файлы в png_masks:", os.listdir(os.path.join(path, "png_masks"))[:5])
              

# Проверяем содержимое папок IMAGES и MASKS
images_subdir = os.path.join(path, "png_images", "IMAGES")
masks_subdir = os.path.join(path, "png_masks", "MASKS")

print("Файлы в IMAGES:", os.listdir(images_subdir)[:5])
print("Файлы в MASKS:", os.listdir(masks_subdir)[:5])
              

path = kagglehub.dataset_download("rajkumarl/people-clothing-segmentation")
print("Path to dataset files:", path)

# Пути к изображениям и маскам
image_dir = os.path.join(path, "png_images/IMAGES")
mask_dir = os.path.join(path, "png_masks/MASKS")
              


class ClothesSegmentationDataset(Dataset):
  #КОНСТРУКТОР КЛАССА
    def __init__(self, image_dir, mask_dir, image_transform=None, mask_transform=None):

        self.image_dir = image_dir
        self.mask_dir = mask_dir
        self.image_transform = image_transform
        self.mask_transform = mask_transform

        #СООТНОШЕНИЕ МЕЖДУ ИЗОБРАЖЕНИЯМИ И МАСКАМИ ПО ИНДЕКСАМ
        self.images = sorted(os.listdir(image_dir))
        self.masks = sorted(os.listdir(mask_dir))

        #проверка что количество изображений и масок совпадает
        assert len(self.images) == len(self.masks), "Количество изображений и масок должно совпадать"


##############################################################
#РАЗМЕР ДАТАСЕТА
    def __len__(self):
        return len(self.images)


################################################################
#возвращает картинку и маску
    def __getitem__(self, idx):
        #находим изображение и маску по пути и индексу
        image_path = os.path.join(self.image_dir, self.images[idx])
        mask_path = os.path.join(self.mask_dir, self.masks[idx])


        #открываем + форматируем в РГБ(только картинку)
        image = Image.open(image_path).convert("RGB")
        mask = Image.open(mask_path)


        #применяем преобразования
        if self.image_transform:
            image = self.image_transform(image)
        if self.mask_transform:
            mask = self.mask_transform(mask)

        mask = torch.from_numpy(np.array(mask)).long() #маска в тензор

        return image, mask
              

#ТРАНСФОРМ ДЛЯ ИЗОБР
image_transform = transforms.Compose([
    transforms.Resize((256, 256)),
    #пил изобр в тензор
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.2, 0.2, 0.2]),
])

mask_transform = transforms.Compose([
    #interpolation используем интерполяцию ближайшего соседа,
    #обрабатываются пиксели , принимаю значения 0 или 1
    transforms.Resize((256, 256), interpolation=transforms.InterpolationMode.NEAREST),
])


###################################################################

dataset = ClothesSegmentationDataset(image_dir, mask_dir, image_transform, mask_transform)


image, mask = dataset[0]
print(f"Форма изображения: {image.shape}, тип: {image.dtype}")
print(f"Форма маски: {mask.shape}, тип: {mask.dtype}")
''')
    elif st == '2':
        print('''
def show_image_with_mask(image, mask):

    #изменяем порядок с с h w для torch на h w c для matplotlib
    image = image.permute(1, 2, 0).cpu().numpy()
    mask = mask.cpu().numpy()


    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(image)
    axes[0].set_title('Image')
    axes[0].axis('off')

    axes[1].imshow(mask, cmap='jet')
    axes[1].set_title('Mask')
    axes[1].axis('off')

    plt.show()


################################################
image, mask = dataset[7]
show_image_with_mask(image, mask)
''')
    elif st =='3':
        print('''
def crop_tensor(tensor, target_tensor):
    _, _, h, w = target_tensor.shape
    tensor = torchvision.transforms.functional.center_crop(tensor, (h, w))
    return tensor
              

class UNet(nn.Module):
    def __init__(self, in_channels, n_classes):
        super(UNet, self).__init__()

        #ENCODER
        #in_channels = 3 , для rgb
        self.enc1 = self.conv_block(in_channels, 64)
        self.pool1 = nn.MaxPool2d(2, 2)

        self.enc2 = self.conv_block(64, 128)
        self.pool2 = nn.MaxPool2d(2, 2)

        self.enc3 = self.conv_block(128, 256)
        self.pool3 = nn.MaxPool2d(2, 2)



##################################################################
        #DECODER
        #nn.ConvTranspose2d увеличиваются размерность карты признаков
        #kernel_size = 2, stride=2 увеличивает карту признаков вдвое
        self.upconv3 = nn.ConvTranspose2d(256, 128, kernel_size=2, stride=2)
        self.dec3 = self.conv_block(256, 128)

        self.upconv2 = nn.ConvTranspose2d(128, 64, kernel_size=2, stride=2)
        self.dec2 = self.conv_block(128, 64)

        self.final_conv = nn.Conv2d(64, n_classes, kernel_size=1)


#######################################################################
    #СВЕРТОЧНЫЕ СЛОИ
    def conv_block(self, in_channels, out_channels):
        return nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
        )


######################################################################
    #FORWARD PASS
    def forward(self, x):
      # encoder
      #х состоит из двух сверточных слоев с релу
      x1 = self.enc1(x)
      x1_pooled = self.pool1(x1)

      x2 = self.enc2(x1_pooled)
      x2_pooled = self.pool2(x2)

      #высокоуровневое, но низкоразмерное рзображение
      x3 = self.enc3(x2_pooled)
      x3_pooled = self.pool3(x3)

      #decoder со skip connections
      #upconv удваивает h и w карты признаков
      #decoder со skip connections
      x3_up = self.upconv3(x3_pooled)
      x3_up_cropped = crop_tensor(x3_up, x2)  # Выравнивание размера
      x3_cat = torch.cat((x3_up_cropped, x2), dim=1)
      x3_decoded = self.dec3(x3_cat)

      x2_up = self.upconv2(x3_decoded)
      x2_up_cropped = crop_tensor(x2_up, x1)  # Выравнивание размера
      x2_cat = torch.cat((x2_up_cropped, x1), dim=1)
      x2_decoded = self.dec2(x2_cat)



      #применяем ядро 1*1 чтоб получить карту сегментации
      output = self.final_conv(x2_decoded)
      return output


##############################################################################
in_channels = 3
n_classes = 59  # Количество классов для сегментации
model = UNet(in_channels=in_channels, n_classes=n_classes)


############################################################################
#unsqueeze(0) добавляет размер батча
image = dataset[0][0].unsqueeze(0)
output = model(image)
print("Форма выходного тензора:", output.shape)  # Ожидаемый: [1, n_classes, h, w]
''')
    elif st == '4':
        print('''
#делим на тестовую и обучающую выборки
indices = list(range(len(dataset)))
#test_size=0.2 20% валидационная выборка
train_indices, val_indices = train_test_split(indices, test_size=0.2, random_state=42)

#subset подмножество исходного набора данных, используя индексы
train_subset = Subset(dataset, train_indices)
val_subset = Subset(dataset, val_indices)
              

train_loader = DataLoader(train_subset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_subset, batch_size=32, shuffle=False)
              

import torch

# Установка устройства: GPU, если доступно, иначе CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
              

#ФУНКЦИЯ ПОТЕРЬ И ОПТИМИЗАТОР
#первый вес задан 0.1 (например фон), а остальные веса генерируются случайно [2,3]
class_weights = torch.tensor([0.1] + [torch.rand(1).item() * (3 - 1) + 2 for _ in range(58)]).to(device)
criterion = nn.CrossEntropyLoss(weight=class_weights)
optimizer = optim.Adam(model.parameters(), lr=1e-3)

#Первый элемент весов фиксирован: 0.1. Это может быть связано с тем, что класс с индексом 0
#сильно представлен в данных (например, фон), и его значение уменьшают, чтобы модель не уделяла ему слишком много внимания.
#Для остальных 58 классов веса генерируются случайно в диапазоне от 2 до 3

#Вычисляет разницу между предсказанным распределением вероятностей (логиты модели) и истинным классом.
#В данном случае она использует веса классов, чтобы учитывать дисбаланс данных.
              

class_weights
              

model
              

# Получение количества классов из модели
num_classes = model.final_conv.out_channels
print("Количество классов в модели:", num_classes)
              

#INTERSEСTION OVER UNION
#насколько хорошо segmentation mask pred ture mask в задачах сегментации


#пересечение/объединение
#пиксели, которые модель правильно предсказала как принадлежащие классу i /
#все пиксели, которые принадлежат либо предсказанному классу i, либо реальному классу i
#Если модель идеально предсказывает объект, то пересечение и объединение совпадают, и IoU=1. Если модель плохо предсказывает, IoU будет меньше

# Функция для расчета IoU
def iou(pred, target, n_classes):
    iou_list = []
    pred = pred.view(-1)
    target = target.view(-1)
    for i in range(n_classes):
        intersection = ((pred == i) & (target == i)).sum().item()
        union = ((pred == i) | (target == i)).sum().item()
        iou_list.append(intersection / union if union != 0 else float('nan'))
    return iou_list
              


# Тренировочный цикл

#обучаются параметры модели (веса и смещения в слоях). Они обновляются при помощи градиентного спуска (реализованного через optimizer.step())
#параметры задаются в конструкторе модели UNet (например, nn.Conv2d, nn.ReLU, nn.MaxPool2d)
num_epochs = 200
for epoch in range(num_epochs):
    model.train()
    train_loss = 0
    train_iou = []
    #считаем количество правильно предсказанных пикселей и общее количество пикселей для вычисления точности
    correct_train = 0
    total_train = 0
    for images, masks in train_loader:
        images, masks = images.to(device), masks.to(device)


#Перед обратным проходом (backpropagation) градиенты обнуляются, чтобы избежать их накопления
        optimizer.zero_grad()


#Вход: изображения из train_loader. Выход: предсказания (outputs)
        outputs = model(images)

        loss = criterion(outputs, masks)
        loss.backward()
        optimizer.step()

        train_loss += loss.item()

        # IoU

#Для каждого пикселя берем индекс класса с максимальной вероятностью. Это предсказание модели
#Считаем метрику IoU для каждого класса с помощью заранее написанной функции
        pred = torch.argmax(outputs, dim=1)
        iou_values = iou(pred, masks, n_classes)
        train_iou.append(iou_values)

        correct_train += (pred == masks).sum().item()
        total_train += masks.numel()

    avg_train_loss = train_loss / len(train_loader)
    avg_train_iou = [sum(iou_val) / len(iou_val) for iou_val in zip(*train_iou)]
    train_accuracy = correct_train / total_train

    print(f"Epoch [{epoch+1}/{num_epochs}]")
    print(f"Train Loss: {avg_train_loss:.4f}, Train Accuracy: {train_accuracy:.4f}")
    print(f"Train IoU: {avg_train_iou}")
              

model = UNet(in_channels=in_channels, n_classes=n_classes).to(device)
              

images, masks = images.to(device), masks.to(device)
              

import torch
import matplotlib.pyplot as plt

# Функция для вывода изображений, масок и предсказаний
def show_images_with_predictions(images, masks, predictions, num_classes):
    num_images = len(images)
    fig, axes = plt.subplots(num_images, 3, figsize=(18, 6 * num_images))

    for i in range(num_images):
        image = images[i].permute(1, 2, 0).cpu().numpy()  # Преобразование в numpy
        mask = masks[i].cpu().numpy()
        prediction = predictions[i].cpu().numpy()

        # Отображение изображения
        axes[i, 0].imshow(image)
        axes[i, 0].set_title(f'Image {i+1}')
        axes[i, 0].axis('off')

        # Отображение маски
        axes[i, 1].imshow(mask, cmap='jet')
        axes[i, 1].set_title(f'Ground Truth Mask {i+1}')
        axes[i, 1].axis('off')

        # Отображение предсказания
        axes[i, 2].imshow(prediction, cmap='jet')
        axes[i, 2].set_title(f'Predicted Mask {i+1}')
        axes[i, 2].axis('off')

    plt.show()

# Загружаем несколько изображений и масок из датасета (например, из train_loader или другого источника)
# Для примера, используем первые 3 изображения и маски:
images, masks = next(iter(train_loader))  # Если у вас есть train_loader
images = images[:3].to(device)  # Загружаем первые 3 изображения
masks = masks[:3].to(device)    # Загружаем соответствующие маски

# Переводим модель в режим оценки (eval)
model.eval()

# Прогнозируем маски для этих изображений
with torch.no_grad():
    outputs = model(images)  # Прогнозируем для всех 3 изображений
    preds = torch.argmax(outputs, dim=1)  # Получаем предсказания

# Выводим изображения, маски и предсказания
show_images_with_predictions(images, masks, preds, n_classes)
''')
    elif st == '5':
        print('''
!pip install datasets

              
from torchvision.transforms import InterpolationMode

#Размер 224x224 чаще используется в задачах классификации (например, ResNet, VGG),
#где нужно только распознать объект на изображении, но не важно его точное расположение.
#Для сегментации такие маленькие размеры приводят к потере важных пространственных деталей.

#Segformer работает с изображениями высокого разрешени

image_transform = transforms.Compose([
    transforms.Resize((512, 512)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.2, 0.2, 0.2]),
])
mask_transform = transforms.Compose([
    #Изменяет размер маски до 512x512 пикселей, используя ближайшего соседа для интерполяции.
    transforms.Resize((512, 512), interpolation=InterpolationMode.NEAREST),
])

# Создаем датасет
dataset_HF = ClothesSegmentationDataset(
    image_dir=image_dir,
    mask_dir=mask_dir,
    image_transform=image_transform,
    mask_transform=mask_transform
)
              


indices = list(range(len(dataset_HF)))

# Разбиваем на обучающую и валидационную выборки (80% для обучения, 20% для валидации)
train_indices, val_indices = train_test_split(indices, test_size=0.2, random_state=42)

# Создаем подмножества для train и val
train_subset = torch.utils.data.Subset(dataset_HF, train_indices)
val_subset = torch.utils.data.Subset(dataset_HF, val_indices)

# Создаем DataLoader'ы
train_loader_HF = torch.utils.data.DataLoader(train_subset, batch_size=2, shuffle=True)
val_loader_HF = torch.utils.data.DataLoader(val_subset, batch_size=2, shuffle=False)
              

model_name = "nvidia/segformer-b0-finetuned-ade-512-512"
model = SegformerForSemanticSegmentation.from_pretrained(
    model_name,
    ignore_mismatched_sizes=True,  # Для изменения числа классов
#Этот параметр игнорирует несоответствия в размерах слоев при загрузке модели,
#если в вашем случае размерность модели отличается от той, с которой она была обучена
    num_labels=59,
).to(device)
processor = SegformerImageProcessor.from_pretrained(model_name)
              

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class_weights = torch.tensor([0.1] + [torch.rand(1).item() * (3 - 1) + 2 for _ in range(58)]).to(device)

criterion = nn.CrossEntropyLoss(weight=class_weights)

optimizer = optim.Adam(model.parameters(), lr=1e-3)
              

import torch.nn.functional as F
import torch.optim as optim

def train_epoch(model, loader, optimizer):
    model.train()
    epoch_loss = 0
    correct = 0
    total = 0

    for images, masks in tqdm(loader):
        images = images.to(device)  # [B, 3, H, W]
        masks = masks.to(device)    # [B, H, W]

        optimizer.zero_grad()
        outputs = model(pixel_values=images).logits  # [B, num_labels, H_out, W_out]

        # Приведение масок к размеру выходного тензора
        masks_resized = F.interpolate(
            masks.unsqueeze(1).float(), size=outputs.shape[2:], mode="nearest"
        ).squeeze(1).long()

        loss = criterion(outputs, masks_resized)
        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()

        preds = torch.argmax(outputs, dim=1)  # [B, H_out, W_out]
        correct += (preds == masks_resized).sum().item()
        total += masks_resized.numel()

    accuracy = correct / total
    return epoch_loss / len(loader), accuracy


def validate_epoch(model, loader):
    model.eval()
    epoch_loss = 0
    correct = 0
    total = 0

    with torch.no_grad():
        for images, masks in tqdm(loader):
            images = images.to(device)
            masks = masks.to(device)

            outputs = model(pixel_values=images).logits
            masks_resized = F.interpolate(
                masks.unsqueeze(1).float(), size=outputs.shape[2:], mode="nearest"
            ).squeeze(1).long()

            loss = criterion(outputs, masks_resized)
            epoch_loss += loss.item()

            preds = torch.argmax(outputs, dim=1)
            correct += (preds == masks_resized).sum().item()
            total += masks_resized.numel()

    accuracy = correct / total
    return epoch_loss / len(loader), accuracy

num_epochs = 75
for epoch in range(num_epochs):
    train_loss, train_acc = train_epoch(model, train_loader_HF, optimizer)
    val_loss, val_acc = validate_epoch(model, val_loader_HF)

    print(f"Epoch {epoch + 1}/{num_epochs}")
    print(f"Train Loss: {train_loss:.4f}, Train Accuracy: {train_acc:.4f}")
    print(f"Val Loss: {val_loss:.4f}, Val Accuracy: {val_acc:.4f}")
              

import torch
import torch.nn.functional as F
import torch.optim as optim
from tqdm import tqdm

# Определение класса для ранней остановки
class EarlyStopping:
    def __init__(self, patience=10, delta=0, verbose=False):
      #verbose=False: Если установлено в True, то при каждом улучшении будет выводиться сообщение о том, что произошли изменения
        """
        patience: количество эпох, в течение которых должны происходить улучшения на валидационном наборе,
                  прежде чем обучение будет остановлено.
        delta: минимальное изменение в показателе, чтобы считалось улучшением.
        verbose: если True, то будет выводиться сообщение при каждом улучшении.
        """
        self.patience = patience
        self.delta = delta
        self.verbose = verbose
        self.counter = 0
        self.best_loss = None
        self.early_stop = False

    def __call__(self, val_loss):
        if self.best_loss is None:
            self.best_loss = val_loss
        elif val_loss > self.best_loss + self.delta:
            self.counter += 1
            if self.verbose:
                print(f"Validation loss did not improve for {self.counter} epochs.")
            if self.counter >= self.patience:
                self.early_stop = True
                if self.verbose:
                    print("Early stopping triggered!")
        else:
            self.best_loss = val_loss
            self.counter = 0

# Функция обучения
def train_epoch(model, loader, optimizer, criterion, device):
    model.train()
    epoch_loss = 0
    correct = 0
    total = 0

#данные на устройтво
    for images, masks in tqdm(loader):
        images = images.to(device)  # [B, 3, H, W]
        masks = masks.to(device)    # [B, H, W]

        optimizer.zero_grad()
        outputs = model(pixel_values=images).logits  # [B, num_labels, H_out, W_out]
        #Прогоняем изображения через модель. Результатом являются логиты (непреобразованные предсказания),
        #которые позже будут переданы в функцию потерь.

        # Приведение масок к размеру выходного тензора outputs
        masks_resized = F.interpolate(
            masks.unsqueeze(1).float(), size=outputs.shape[2:], mode="nearest"
        ).squeeze(1).long()

        loss = criterion(outputs, masks_resized)
        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()

        preds = torch.argmax(outputs, dim=1)  # [B, H_out, W_out]
        correct += (preds == masks_resized).sum().item()
        total += masks_resized.numel()

    accuracy = correct / total
    return epoch_loss / len(loader), accuracy


# Функция валидации на одной эпохе
def validate_epoch(model, loader, criterion, device):
    model.eval()
    epoch_loss = 0
    correct = 0
    total = 0

    with torch.no_grad():
        for images, masks in tqdm(loader):
            images = images.to(device)
            masks = masks.to(device)

            outputs = model(pixel_values=images).logits
            masks_resized = F.interpolate(
                masks.unsqueeze(1).float(), size=outputs.shape[2:], mode="nearest"
            ).squeeze(1).long()

            loss = criterion(outputs, masks_resized)
            epoch_loss += loss.item()


            #argmax Эта функция находит индекс максимального значения вдоль указанной размерности (dim).
            #В данном случае, dim=1 означает, что argmax ищет максимальное значение вдоль размерности классов (C).
            #Для каждого пикселя (h, w) в каждом изображении b argmax выбирает класс c с наибольшей вероятностью.

            preds = torch.argmax(outputs, dim=1)
            correct += (preds == masks_resized).sum().item()
            total += masks_resized.numel()

    accuracy = correct / total
    return epoch_loss / len(loader), accuracy


# Основной цикл обучения
num_epochs = 75
patience = 10  # Количество эпох без улучшения для ранней остановки
early_stopping = EarlyStopping(patience=patience, delta=0.001, verbose=True)


for epoch in range(num_epochs):
    # Обучение
    train_loss, train_acc = train_epoch(model, train_loader_HF, optimizer, criterion, device)

    # Валидация
    val_loss, val_acc = validate_epoch(model, val_loader_HF, criterion, device)

    # Вывод статистики
    print(f"Epoch {epoch + 1}/{num_epochs}")
    print(f"Train Loss: {train_loss:.4f}, Train Accuracy: {train_acc:.4f}")
    print(f"Val Loss: {val_loss:.4f}, Val Accuracy: {val_acc:.4f}")

    # Ранняя остановка
    early_stopping(val_loss)
    if early_stopping.early_stop:
        print(f"Training stopped early at epoch {epoch + 1}")
        break
              

import matplotlib.pyplot as plt
import torch

def plot_predictions(model, loader, device, num_samples=5):
    model.eval()
    with torch.no_grad():
        sample_count = 0
        for images, masks in loader:
            images = images.to(device)
            masks = masks.to(device)

            outputs = model(pixel_values=images).logits  # [B, num_labels, H_out, W_out]
            preds = torch.argmax(outputs, dim=1)  # [B, H_out, W_out]

            # Отображаем предсказания
            for i in range(images.size(0)):  # Проходим по батчу
                if sample_count >= num_samples:
                    return
                fig, axs = plt.subplots(1, 3, figsize=(12, 4))
                axs[0].imshow(images[i].cpu().numpy().transpose(1, 2, 0))  # Исходное изображение
                axs[0].set_title('Input Image')
                axs[0].axis('off')

                axs[1].imshow(masks[i].cpu().numpy(), cmap='gray')  # Истинная маска
                axs[1].set_title('True Mask')
                axs[1].axis('off')

                axs[2].imshow(preds[i].cpu().numpy(), cmap='gray')  # Предсказанная маска
                axs[2].set_title('Predicted Mask')
                axs[2].axis('off')

                plt.show()

                sample_count += 1

              
# Вызываем функцию для вывода предсказаний
plot_predictions(model, val_loader_HF, device, num_samples=5)  # num_samples - сколько изображений отобразить
''')
def ligDep_info():
    print('''
ЧТОБЫ ВЫЗВАТЬ КОД: используйте DL.ligDep_code("НОМЕР ЗАДАНИЯ")    
          
1. Опишите датасет AnimalDetectionDataset на основе архива animals.zip. Реализуйте __getitem__ таким образом, чтобы он возвращал три элемента: тензор с 
изображением, словарь с координатами bounding box и метку объекта. Предусмотрите возможность передавать извне при создании датасета набор преобразований 
для изображений, преобразование для метки объекта (для кодирования) и флаг, показывающий, нужно ли возвращать исходные или нормированные координаты bounding box. 
Разбейте набор данных на обучающее и валидационное множество. При создании датасета не забудьте указать преобразования, соответствующие модели ResNet.
          
2. Напишите модель для решения задачи выделения объектов в виде объекта lightning.LightningModule. Реализуйте двухголовую сеть, 
одна голова которой предсказывает метку объекта (задача классификации), а вторая голова предсказывает 4 координаты вершин bounding box (задача регрессии). 
В качестве backbone используйте модель resnet50 из пакета torchvision. В качестве функции потерь используйте сумму MSELoss (для расчета ошибки на задаче регрессии) и CrossEntropyLoss (для расчета ошибки на задачи классификации).
Реализуйте следующий функционал при помощи lightning и torchmetrics:
для каждого батча во время обучения рассчитывается значение функции потерь и точности прогнозов, по завершению эпохи метрики усредняются;
для каждого батча во время валидации рассчитывается значение функции потерь и точности прогнозов, по завершению эпохи метрики усредняются;
если значение функции потерь не улучшалось в течении 5 эпох, происходит ранняя остановка;
при создании модель на экран выводится сводка по модели с указанием размерностей выходов слоев;
для визуализации процесса обучения используется tensorboard.
Используя обученную модель, получите предсказания для изображения кошки и собаки и отрисуйте их. 
Выполните процедуру, обратную нормализации, чтобы корректно отобразить фотографии.
          
3. Загрузите чекпоинт обученной модели и переведите модель в режим оценки. Допишите функцию transform_image и route predict. 
Запустите сервер flask и сделайте POST-запрос к соответствующему эндпоинту.
При работе в Google Colab вы можете воспользоваться инструментом ngrok для проброса локального адреса или запустить сервер Flask в отдельном потоке.
''')
    
def ligDep_code(st):
    if st == '1':
        print('''
!pip install pytorch_lightning
!pip install torchinfo
!pip install pyngrok

import matplotlib.pyplot as plt
from torchvision import datasets, transforms
from torchvision.transforms.functional import to_pil_image
import torchvision
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader, random_split
import torch.nn.functional as F
import torchvision.models as models
from tqdm.auto import tqdm
from sklearn import metrics
import seaborn as sns
import pandas as pd
import zipfile
from tqdm import tqdm
from PIL import Image
from sklearn.metrics import confusion_matrix
import random
import matplotlib.patches as patches
import kagglehub
import os
import numpy as np
from collections import Counter
import pytorch_lightning as pl
from torchmetrics.classification import Accuracy
from torchvision import models
from torch.utils.data import DataLoader
import torchmetrics
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)
              

from google.colab import drive
drive.mount('/content/drive')
              
zip_path = '/content/drive/MyDrive/глубокое обучение/animals.zip'

extracted_dir = './animals'
with zipfile.ZipFile(zip_path, 'r') as zf:
    for file in tqdm(zf.infolist()):
        zf.extract(file, extracted_dir)
              

import xml.etree.ElementTree as ET
import os

def parse_xml(xml_file):
    tree = ET.parse(xml_file) #путь файла хмл
    root = tree.getroot()


    size = root.find("size") #размеры изображения
    width = float(size.find("width").text)
    height = float(size.find("height").text)

    #координаты баундинг бокс
    bndbox = root.find(".//bndbox")
    xmin = float(bndbox.find("xmin").text)
    ymin = float(bndbox.find("ymin").text)
    xmax = float(bndbox.find("xmax").text)
    ymax = float(bndbox.find("ymax").text)


    #абсолютные и нормализованные координаты
    raw = {"xmin": xmin, "ymin": ymin, "xmax": xmax, "ymax": ymax}
    scaled = {
        "xmin": xmin / width,
        "ymin": ymin / height,
        "xmax": xmax / width,
        "ymax": ymax / height,
    }


    obj_name = root.find(".//object/name").text


    return {"raw": raw, "scaled": scaled, "obj_name": obj_name}

##############
file_name = 'cat.0.xml'
extracted_dir = './animals/Asirra: cat vs dogs'

#полный путь к XML файлу внутри извлеченной папки
xml_file_path = os.path.join(extracted_dir, file_name)

try:
    #открываем и парсим файл
    result = parse_xml(xml_file_path)
    print("Результат:")
    print(result)
except FileNotFoundError:
    print(f"Файл '{file_name}' не найден в папке '{extracted_dir}'.")
              

class AnimalDetectionDataset(Dataset):
    def __init__(self, root, transforms=None, target_transform=None, return_scaled=True):
        """
        Инициализация датасета для детекции объектов.

        :param root: Путь к архиву с изображениями и XML файлами
        :param transforms: Преобразования для изображений
        :param target_transform: Преобразования для метки объекта
        :param return_scaled: Флаг, нужно ли возвращать нормированные координаты bounding box
        """
        self.root = root
        self.transforms = transforms
        self.target_transform = target_transform
        self.return_scaled = return_scaled

        # Извлечение содержимого архива
        self.image_dir = './animals/Asirra: cat vs dogs'
        with zipfile.ZipFile(self.root, 'r') as zf:
            zf.extractall(self.image_dir)

        # Множество для предотвращения дублирования XML файлов
        self.xml_files = set()  # Используем множество для хранения уникальных путей
        seen_files = set()  # Множество для проверки уже добавленных файлов по их именам

        for root_dir, dirs, files in os.walk(self.image_dir):
            for file in files:
                if file.endswith('.xml'):
                    # Нормализуем путь для файла
                    normalized_path = os.path.normpath(os.path.join(root_dir, file))

                    if file not in seen_files:
                        seen_files.add(file)
                        self.xml_files.add(normalized_path)

        # Преобразуем множество обратно в список (если нужно)
        self.xml_files = list(self.xml_files)

        print(f"Найдено XML файлов: {len(self.xml_files)}")

        if len(self.xml_files) == 0:
            print("Ошибка: XML файлы не найдены.")

    def __len__(self):
        """Возвращает количество элементов в датасете"""
        return len(self.xml_files)

    def __getitem__(self, idx):
        """Получение элемента датасета по индексу"""
        # Загружаем XML файл
        xml_file = self.xml_files[idx]
        image_file_name = xml_file.replace('.xml', '.jpg')  # Предполагаем, что изображение с таким же именем
        image_file_path = image_file_name

        # Чтение XML файла для получения bounding box и метки объекта с помощью функции parse_xml
        result = parse_xml(xml_file)

        # Извлекаем bbox и label из словаря, возвращаемого parse_xml
        bbox = result['scaled'] if self.return_scaled else result['raw']
        label = result['obj_name']

        # Преобразуем bbox в тензор
        bbox = torch.tensor([bbox['xmin'], bbox['ymin'], bbox['xmax'], bbox['ymax']], dtype=torch.float32)

        # Преобразуем метку в числовой формат
        label_map = {'cat': 0, 'dog': 1}  # Преобразование строк в числа
        label = torch.tensor(label_map[label], dtype=torch.long)

        # Загружаем изображение
        image = Image.open(image_file_path).convert('RGB')

        # Применяем преобразования для изображения
        if self.transforms:
            image = self.transforms(image)

        # Преобразуем метку, если задано target_transform
        if self.target_transform:
            label = self.target_transform(label)

        return image, bbox, label

#################################################################################
zip_path = '/content/drive/MyDrive/глубокое обучение/animals.zip'


transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])


dataset = AnimalDetectionDataset(root=zip_path, transforms=transform, return_scaled=True)

#
if len(dataset) > 0:
    image, bbox, label = dataset[0]
    print(f"Image shape: {image.shape}, BBox: {bbox}, Label: {label}")
else:
    print("Датасет пуст.")
              

def split_dataset(dataset, val_split=0.2):
    """
    Разделение датасета на обучающую и валидационную части.
    """
    dataset_size = len(dataset)
    val_size = int(val_split * dataset_size)
    train_size = dataset_size - val_size
    return random_split(dataset, [train_size, val_size])

train_dataset, val_dataset = split_dataset(dataset)
len(train_dataset), len(val_dataset)
''')
    elif st == '2':
        print('''
class DualHeadModel(pl.LightningModule):
    def __init__(self, train_dataset, val_dataset, num_classes=2):
        super(DualHeadModel, self).__init__()


        self.resnet = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)

        # Убираем последний слой (классификатор) и сохраняем до слоя avgpool
        self.resnet = nn.Sequential(*list(self.resnet.children())[:-1])

        # Количество выходных признаков после слоя AdaptiveAvgPool2d
        self.in_features = 2048  # Для ResNet-50 это всегда 2048

        # Классификационная голова
        self.classification_head = nn.Linear(self.in_features, num_classes)

        # Голова для регрессии (предсказание координат BBox)
        self.regression_head = nn.Linear(self.in_features, 4)

        # Метрическая точность для бинарной классификации
        self.classification_accuracy = Accuracy(task='binary', num_classes=num_classes)

        # Метрическая ошибка для регрессии (MSE)
        self.regression_mse = torchmetrics.MeanSquaredError()

        # Датасеты для тренировки и валидации
        self.train_dataset = train_dataset
        self.val_dataset = val_dataset

    def forward(self, x):
        features = self.resnet(x).view(x.size(0), -1)  # Преобразуем в вектор
        classification_output = self.classification_head(features)
        regression_output = self.regression_head(features)
        return classification_output, regression_output

    def training_step(self, batch, batch_idx):
        images, bboxes, labels = batch
        class_preds, bbox_preds = self(images)

        # Для классификации берем индекс с максимальной вероятностью (логита)
        class_preds_max = torch.argmax(class_preds, dim=1)

        # Потери для классификации
        classification_loss = nn.CrossEntropyLoss()(class_preds, labels)

        # Потери для регрессии
        regression_loss = nn.MSELoss()(bbox_preds, bboxes)

        # Суммарная потеря
        total_loss = classification_loss + regression_loss

        # Логирование метрик
        self.log('train_loss', total_loss)
        self.log('train_classification_accuracy', self.classification_accuracy(class_preds_max, labels))
        self.log('train_regression_mse', self.regression_mse(bbox_preds, bboxes))

        return total_loss

    def validation_step(self, batch, batch_idx):
        images, bboxes, labels = batch
        class_preds, bbox_preds = self(images)

        # Для классификации берем индекс с максимальной вероятностью (логита)
        class_preds_max = torch.argmax(class_preds, dim=1)

        # Потери для классификации
        classification_loss = nn.CrossEntropyLoss()(class_preds, labels)

        # Потери для регрессии
        regression_loss = nn.MSELoss()(bbox_preds, bboxes)

        # Суммарная потеря
        total_loss = classification_loss + regression_loss

        # Логирование метрик
        self.log('val_loss', total_loss)
        self.log('val_classification_accuracy', self.classification_accuracy(class_preds_max, labels))
        self.log('val_regression_mse', self.regression_mse(bbox_preds, bboxes))

        return total_loss

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=1e-4)
        return optimizer

    def on_epoch_end(self):
        # Логируем итоговые метрики по завершению эпохи
        self.log('train_classification_accuracy_epoch', self.classification_accuracy.compute())
        self.log('train_regression_mse_epoch', self.regression_mse.compute())

        # Сбрасываем метрики для следующей эпохи
        self.classification_accuracy.reset()
        self.regression_mse.reset()

    # Методы для загрузки данных
    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=32, shuffle=True)

    def val_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=32, shuffle=False)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

model = DualHeadModel(train_dataset=train_dataset, val_dataset=val_dataset)

# Сводка по модели
summary(model, input_size=(1, 3, 256, 256))  # Печатает сводку для входного изображения размером 256x256 с 3 каналами
              
logger = TensorBoardLogger("tb_logs", name="dual_head_model")
early_stop_callback = EarlyStopping(monitor="val_loss", patience=5, verbose=True)

checkpoint_callback = ModelCheckpoint(
    monitor="val_loss",   # Мы сохраняем веса, когда минимизируются валидационные потери
    filename="best_model",  # Имя файла для сохранения модели
    save_top_k=1,           # Сохраняем только лучший чекпоинт
    mode="min",             # Минимизируем потери
    save_weights_only=True, # Сохраняем только веса
    verbose=True
)

trainer = pl.Trainer(
    max_epochs=50,
    logger=logger,
    callbacks=[early_stop_callback, checkpoint_callback],
    devices=1,  # Если у вас один GPU
    accelerator="gpu",  # Если нужно использовать GPU
)

trainer.fit(model)
              

model.eval()

# Смотрим на первый пример из val_dataset
img, bbox, label = val_dataset[15]

# Выполняем преобразования, которые были использованы на тренировке (обратная нормализация)
mean = torch.tensor([0.485, 0.456, 0.406])
std = torch.tensor([0.229, 0.224, 0.225])

# Обратная нормализация
img = img * std[:, None, None] + mean[:, None, None]

# Преобразуем в формат, подходящий для отображения
img = img.permute(1, 2, 0)  # Переупорядочиваем каналы для отображения

# Получаем размеры изображения
height, width, _ = img.shape

# Визуализируем изображение
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(img)
ax.axis('off')  # Убираем оси

# Преобразуем bounding box в реальные пиксельные значения
bbox = torch.tensor(bbox)
scaling_factors = torch.tensor([width, height, width, height])

# Расчет координат bbox в пикселях
true_xmin, true_ymin, true_xmax, true_ymax = bbox * scaling_factors

# Рисуем настоящий bounding box (ground truth) красным цветом
ax.add_patch(plt.Rectangle((true_xmin, true_ymin), true_xmax - true_xmin, true_ymax - true_ymin,
                           linewidth=2, edgecolor='r', facecolor='none', label='Ground Truth'))

# Добавляем текст с лейблом для настоящего bounding box
class_label = 'Cat' if label == 0 else 'Dog'
ax.text(true_xmin, true_ymin - 10, f'True: {class_label}', color='r', fontsize=12, weight='bold')

# Преобразуем изображение в формат [channels, height, width]
img = img.permute(2, 0, 1)  # Переупорядочиваем обратно для модели

# Получаем предсказания модели
with torch.no_grad():
    class_preds, bbox_preds = model(img.unsqueeze(0))  # Добавляем batch dimension
    bbox_preds = bbox_preds.squeeze(0)  # Убираем batch dimension

# Преобразуем предсказанный bbox в реальные пиксельные значения
pred_xmin, pred_ymin, pred_xmax, pred_ymax = bbox_preds * scaling_factors

# Рисуем предсказанный bounding box зеленым цветом
ax.add_patch(plt.Rectangle((pred_xmin, pred_ymin), pred_xmax - pred_xmin, pred_ymax - pred_ymin,
                           linewidth=2, edgecolor='g', facecolor='none', label='Prediction'))

# Добавляем текст с лейблом для предсказанного bounding box
pred_class_label = 'Cat' if class_preds.argmax() == 0 else 'Dog'
ax.text(pred_xmin, pred_ymin - 10, f'Pred: {pred_class_label}', color='g', fontsize=12, weight='bold')

# Выводим текст за пределами изображения с информацией о bounding boxes
ax.text(0.5, -0.05, 'Red box: Ground Truth, Green box: Prediction', ha='center', va='center',
        transform=ax.transAxes, fontsize=12, color='black', bbox=dict(facecolor='white', alpha=0.7))

# Показываем изображение
plt.show()
              

model.eval()

# Смотрим на первый пример из val_dataset
img, bbox, label = val_dataset[14]

# Выполняем преобразования, которые были использованы на тренировке (обратная нормализация)
mean = torch.tensor([0.485, 0.456, 0.406])
std = torch.tensor([0.229, 0.224, 0.225])

# Обратная нормализация
img = img * std[:, None, None] + mean[:, None, None]

# Преобразуем в формат, подходящий для отображения
img = img.permute(1, 2, 0)  # Переупорядочиваем каналы для отображения

# Получаем размеры изображения
height, width, _ = img.shape

# Визуализируем изображение
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(img)
ax.axis('off')  # Убираем оси

# Преобразуем bounding box в реальные пиксельные значения
bbox = torch.tensor(bbox)
scaling_factors = torch.tensor([width, height, width, height])

# Расчет координат bbox в пикселях
true_xmin, true_ymin, true_xmax, true_ymax = bbox * scaling_factors

# Рисуем настоящий bounding box (ground truth) красным цветом
ax.add_patch(plt.Rectangle((true_xmin, true_ymin), true_xmax - true_xmin, true_ymax - true_ymin,
                           linewidth=2, edgecolor='r', facecolor='none', label='Ground Truth'))

# Добавляем текст с лейблом для настоящего bounding box
class_label = 'Cat' if label == 0 else 'Dog'
ax.text(true_xmin, true_ymin - 10, f'True: {class_label}', color='r', fontsize=12, weight='bold')

# Преобразуем изображение в формат [channels, height, width]
img = img.permute(2, 0, 1)  # Переупорядочиваем обратно для модели

# Получаем предсказания модели
with torch.no_grad():
    class_preds, bbox_preds = model(img.unsqueeze(0))  # Добавляем batch dimension
    bbox_preds = bbox_preds.squeeze(0)  # Убираем batch dimension

# Преобразуем предсказанный bbox в реальные пиксельные значения
pred_xmin, pred_ymin, pred_xmax, pred_ymax = bbox_preds * scaling_factors

# Рисуем предсказанный bounding box зеленым цветом
ax.add_patch(plt.Rectangle((pred_xmin, pred_ymin), pred_xmax - pred_xmin, pred_ymax - pred_ymin,
                           linewidth=2, edgecolor='g', facecolor='none', label='Prediction'))

# Добавляем текст с лейблом для предсказанного bounding box
pred_class_label = 'Cat' if class_preds.argmax() == 0 else 'Dog'
ax.text(pred_xmin, pred_ymin - 10, f'Pred: {pred_class_label}', color='g', fontsize=12, weight='bold')

# Выводим текст за пределами изображения с информацией о bounding boxes
ax.text(0.5, -0.05, 'Red box: Ground Truth, Green box: Prediction', ha='center', va='center',
        transform=ax.transAxes, fontsize=12, color='black', bbox=dict(facecolor='white', alpha=0.7))

# Показываем изображение
plt.show()
''')
    elif st == '3':
        print('''
extracted_dir = './animals/Asirra: cat vs dogs'

# Получаем список файлов в папке
files = os.listdir(extracted_dir)

image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png'))]
print(image_files)
              

from PIL import Image
import io
from torchvision.transforms import v2 as T
import torch
from flask import Flask
# from flask_ngrok import run_with_ngrok
from flask import Flask, request, jsonify
import threading
              

checkpoint_path = 'tb_logs/dual_head_model/version_0/checkpoints/best_model.ckpt'

# Загружаем модель из чекпоинта
model2 = DualHeadModel.load_from_checkpoint(checkpoint_path, train_dataset=train_dataset, val_dataset=val_dataset)

summary(model2, input_size=(1, 3, 256, 256))
              


model2.eval()

# Flask приложение
app = Flask(__name__)
              


def bytes_to_pil(image_bytes: bytes) -> Image:
    return Image.open(io.BytesIO(image_bytes))

def transform_image(image: Image) -> torch.Tensor:
    """Преобразует PIL.Image в тензор, который можно подать в модель"""
    transform = transforms.Compose([
        transforms.Resize((256, 256)),  # Тот же размер, что использовался при обучении
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Обратная нормализация
    ])
    image_tensor = transform(image)
    return image_tensor
              

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Получаем файл изображения из запроса
        file = request.files.get("file")
        if file is None or file.filename == "":
            return jsonify({"error": "no file"})

        if not allowed_file(file.filename):
            return jsonify({"error": "format not supported"})

        try:
            # Читаем изображение в байтах
            img_bytes = file.read()
            image = bytes_to_pil(img_bytes)

            # Преобразуем изображение в тензор
            tensor = transform_image(image)

            # Получаем предсказания от модели
            with torch.no_grad():
                class_preds, bbox_preds = model2(tensor.unsqueeze(0))  # Добавляем batch dimension
                class_preds = class_preds.squeeze(0)
                bbox_preds = bbox_preds.squeeze(0)

            # Преобразуем результаты в подходящий формат для ответа
            class_preds = torch.argmax(class_preds, dim=0).item()  # Преобразуем в метку класса
            bbox_preds = bbox_preds.tolist()  # Преобразуем в список

            # Возвращаем результат
            data = {
                "label": class_preds,
                "bbox": bbox_preds
            }
            return jsonify(data)

        except Exception as e:
            return jsonify({"error": f"Error during prediction: {e}"})

def run_app():
    app.run(debug=True, use_reloader=False)

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run()).start()
    # app.run()
              

from pyngrok import ngrok
              

!ngrok authtoken 2pUu4KzSHKbV3WJgfd5Nosy88V9_3eyhVN2DGKskYdozP5sv5
              

public_url = ngrok.connect(5000)
print(f" * Flask app is running at: {public_url}")
              

import requests

filename = 'cat.3715.jpg'
file_path = os.path.join(extracted_dir, filename)

resp = requests.post(
    "http://127.0.0.1:5000/predict",  # Или используй публичный URL от ngrok
    files={"file": open(file_path, "rb")}
)

response_json = resp.json()

response_json
              

image = Image.open(file_path)
bbox = response_json.get('bbox', [])
label = response_json.get('label', None)
bbox
              

# Преобразуем нормализованные координаты bbox в пиксельные
width, height = image.size
xmin, ymin, xmax, ymax = [
    int(bbox[0] * width),
    int(bbox[1] * height),
    int(bbox[2] * width),
    int(bbox[3] * height)
]

# Открываем картинку и рисуем на ней bounding box
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(image)
ax.axis('off')  # Убираем оси

# Рисуем bounding box (красный для истинного значения)
ax.add_patch(plt.Rectangle(
    (xmin, ymin), xmax - xmin, ymax - ymin,
    linewidth=2, edgecolor='r', facecolor='none', label='Prediction'
))

# Добавляем текст для метки (label)
labels_map = {0: 'Cat', 1: 'Dog'}  # Сопоставление меток
label_name = labels_map.get(label, 'Unknown')
ax.text(xmin, ymin - 10, label_name, color='red', fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

# Показываем изображение
plt.show()
''')