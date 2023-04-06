# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5
n = int(input("Введите количество элементов массива: "))
x = int(input("Введите число для сравнения с элементами массива: "))
#List = [int(input(f"Введите {i} элемент массива ")) for i in range(n)]#
List = []
for i in range(n):
    List.append(int(input(f"Введите {i} элемент массива: ")))
print(List) 
closest_number = set()
elem_min_diff = List[0]
min_diff = abs(List[0]-x)
for num in List[1:]:
    cur_diff = abs(num-x)
    if cur_diff < min_diff and num != x:
        elem_min_diff = num
        min_diff = cur_diff
        closest_number.clear()
        closest_number.add(elem_min_diff)
    elif cur_diff == min_diff and num != x:
        closest_number.add(num)
print(f"Самый близкий по величине элемент к числу {x} :")
print(*closest_number)