import collections
import random

import networkx as nx
import numpy as np


# TODO 1. Оценить асимптотическую сложность приведенного ниже алгоритма:

# def test_1():
#     """Самый сложный - это цикл, поэтому и написал O(log(N))"""
#     a = len(arr) - 1  # O(1)
#     out = list()  # O(1)
#     while a > 0:  #
#         out.append(arr[a])  # O(log(N))
#         a = a // 1.7  #
#     out.merge_sort()  # O(1) - вот это меня смущает :( НЕ пойму, какой у этой строки смысл...
#     # если это сортировка, то log(N). Цикл сложнее, ответ O(log(N))


# TODO 2. Считалочка Дано N человек, считалка из K слогов. Считалка начинает считать с первого человека.
#  Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает.
#  Игра происходит до тех пор, пока не останется последний человек.
#  Для данных N и К дать номер последнего оставшегося человека.

def task_2(n_people: int, k_syllable: int):
    count = list(range(1, n_people + 1))
    print(count)
    stop = False
    first_out = 0
    while not stop:
        if len(count) == 1:
            stop = True
            print(f'Winner: {count[0]}')
        else:
            if k_syllable > n_people:
                del_n_people = k_syllable - n_people - 1 + first_out
                if del_n_people >= len(count):
                    while del_n_people >= len(count):
                        del_n_people = del_n_people - len(count)
            else:
                del_n_people = k_syllable - 1 + first_out
                while len(count) <= del_n_people:
                    del_n_people = del_n_people - len(count)
            del count[del_n_people]
            first_out = del_n_people
            if first_out > len(count):
                first_out = first_out - len(count) - 1
            print(count)


# TODO 3. Назовем связным такой граф, в котором есть путь от любой вершины к любой другой вершине.
#  Дан граф, состоящий из 2+ связных подграфов, которые не связаны между собой.
#  Задача: посчитать число компонент связности графа, т.е. количество таких подграфов.
#  В графе на картинке – три подграфа, т.е. число компонент связности = 3.

def task_3(graph, start_node):
    all_visits = []
    visited = []
    connection_rate = 0
    queue = [start_node]
    while all_visits != graph.nodes:
        queue.append(start_node)
        for node in queue:
            d = graph.adj[node]
            visited.append(node)
            for k in d:
                if k not in visited and k not in queue:
                    queue.append(k)

        all_visits.extend(visited)
        temp_lst = list(set(graph.nodes) - set(all_visits))
        connection_rate += 1
        if not temp_lst:
            return connection_rate
        start_node = temp_lst[0]


# TODO 4. Навигатор на сетке...

def task_4(cost: list):
    coords = [(0, 0)]

    for j in range(1, len(cost[0])):
        cost[0][j] += cost[0][j - 1]

    for i in range(1, len(cost)):
        cost[i][0] += cost[i - 1][0]

    for i in range(1, len(cost)):
        for j in range(1, len(cost[0])):
            cost[i][j] += min(cost[i][j - 1], cost[i - 1][j])
            if cost[i][j - 1] <= cost[i - 1][j] and (i, j - 1) != coords[-1]:
                coords.append((i, j - 1))
            elif (i - 1, j) != coords[-1]:
                coords.append((i - 1, j))

    coords.append((len(cost) - 1, len(cost) - 1))

    print(cost[-1][-1])
    print(coords)


# TODO 5. Задача консенсуса DNA ридов...

def task_5(word):
    temp_str = ''
    temp_str_2 = ''
    cons_string = ''
    for index, i in enumerate(range(len(word[0]))):
        for j in word:
            temp_str += j[index]
        d = {i: temp_str.count(i) for i in temp_str}
        max_res = 0
        for k, v in d.items():
            if v > max_res:
                max_res = v
                temp_str_2 += k
        cons_string += temp_str_2[-1]
    return cons_string


# TODO  6. Аренда ракет...

def task_6(list_order: list, new_list: list):
    rocket = True
    for first_rocket in list_order:
        start_time = first_rocket[0]
        finish_time = first_rocket[1]
        time = range(start_time, finish_time)
        for second_rocket in list_order:
            if first_rocket != second_rocket and second_rocket not in new_list:
                if second_rocket[0] == start_time:
                    rocket = False
                if second_rocket[1] in time:
                    rocket = False
                if second_rocket[0] in time:
                    rocket = False
                if start_time in range(second_rocket[0], second_rocket[1] + 1):
                    rocket = False
        new_list.append(first_rocket)

        if rocket:
            print('Достаточно первой ракеты')
        else:
            print('Не хватает первой ракеты')


# TODO  7. Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
#  Задача: отсортировать массив наиболее эффективным способом

def task_7(a: int, b: int):
    array = [x + a for x in (range(b - a))] * 2
    random.shuffle(array)
    print(array)

    numbers = np.full(b - a, 0)
    for x in array:
        numbers[x - a] += 1
    result = np.array([], dtype=int)
    for i in range(b - a):
        result = np.concatenate((result, np.full(numbers[i], a + i, dtype=int)))
    print(np.array(result))


if __name__ == '__main__':

    task_2(5, 2)

    g = nx.Graph()
    g.add_nodes_from("ABCDEFG")
    g.add_edges_from(
        [
            ("A", "B"),
            ("B", "C"),
            ("B", "D"),
            ("C", "D"),
            ("G", "F")
        ]
    )
    print("Компонент связанности графа: ", task_3(g, "F"))

    print('__________')

    price = [
        [2, 5, 6],
        [7, 1, 9],
        [6, 4, 2]
    ]
    task_4(price)

    print('__________')

    test = ["ATTA", "ACTA", "AGCA", "ACAA"]

    print("Консенсус-строка: ", task_5(test))

    print('__________')

    orders_received = [(4, 1), (7, 9), (5, 2), (9, 11)]
    list_ = []
    task_6(orders_received, list_)

    print('__________')

    test_a = 15
    test_b = 25
    task_7(test_a, test_b)
