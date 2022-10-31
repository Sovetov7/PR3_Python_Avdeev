import multiprocessing
from multiprocessing import Process
from random import randint
from typing import List
from RandomWordGenerator import RandomWord
import os


def total(name_file: str):
    file = open(name_file, 'r')
    ttl = 0
    for line in file:
        for ch in line:
            if ch != '\n':
                ttl += len(ch)
    file.close()
    return ttl


def length_max(name_file: str):
    file = open(name_file, 'r')
    lenmax: int = -1
    for line in file:
        line = line.replace("\n", "")
        if line != '':
            if lenmax == -1:
                lenmax = len(line)
            else:
                if lenmax < len(line):
                    lenmax = len(line)
    file.close()
    return lenmax


def length_min(name_file: str):
    file = open(name_file, 'r')
    lenmin: int = -1
    for line in file:
        line = line.replace("\n", "")
        if line != '':
            if lenmin == -1:
                lenmin = len(line)
            else:
                if lenmin > len(line):
                    lenmin = len(line)
    file.close()
    return lenmin


def file_length(name_file):
    file = open(name_file, 'r')
    f = 0
    for line in file:
        f += 1
    file.close()
    return f


def length_mid(name_file: str):
    lenmid: float = total(name_file) / file_length(name_file)
    return lenmid


def glasn(name_file: str):
    file = open(name_file, 'r')
    vow: int = 0
    for line in file:
        for ch in line:
            if ch in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']:
                vow += 1
            else:
                pass
    file.close()
    return vow


def soglasn(name_file: str):
    file = open(name_file, 'r')
    soglasn: int = 0
    for line in file:
        for ch in line:
            if ch in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y', '\n', ' ']:
                pass
            else:
                soglasn += 1
    file.close()
    return soglasn


def repeats(name_file: str):
    file = open(name_file, 'r')
    dict_rep: dict = dict()
    for line in file:
        line = line.replace("\n", "")
        if line != '':
            if len(line) in dict_rep:
                dict_rep[len(line)] += 1
            else:
                dict_rep[len(line)] = 1
    dict_sorted = {}
    keys_sorted = sorted(dict_rep.keys())
    for w in keys_sorted:
        dict_sorted[w] = dict_rep[w]
    dict_rep = dict_sorted.copy()
    rep: str = ""
    for key in dict_rep:
        rep += f"   * {key} симв. >> {dict_rep[key]} повторений.\n"
    file.close()
    return rep


def analytics(name_file: str):
    t: str = ""
    for i in range(55):
        t += '*'
    print(t + f"\n" + f"Аналитика для файла {name_file}" + f"\n" + t + f"\n" +
          f"1. Всего символов --> {total(name_file)}\n" +
          f"2. Максимальная длина слова --> {length_max(name_file)}\n" +
          f"3. Минимальная длина слова --> {length_min(name_file)}\n" +
          f"4. Средняя длина слова --> {length_mid(name_file)}\n" +
          f"5. Количество гласных --> {glasn(name_file)}\n" +
          f"6. Количество согласных --> {soglasn(name_file)}\n" +
          "7. Количество повторений слов с одинаковой длиной:\n" +
          f"{repeats(name_file)} \n")


def file_create(num: int, quantity: int):
    random = RandomWord()
    random.constant_word_size = False
    ospid: int = os.getpid()
    name: str = f'./result_files/Process-{num}-{ospid}.txt'
    file = open(name, 'a')
    for q in range(quantity):
        file.write(f'{random.generate()}\n')
    file.close()
    analytics(name)


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    list_process: List[Process] = []
    for i in range(multiprocessing.cpu_count()):
        name_pr: str = f"pr{i}"
        quant: int = randint(1, 11)
        pr: Process = Process(target=file_create, args=(i + 1, quant), name=name_pr)
        list_process.append(pr)
        pr.start()
    for i in range(multiprocessing.cpu_count()):
        list_process[i].join()
