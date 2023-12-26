import numpy as np
import json
def read_json(file):
    with open(file, 'r') as f:
        a = json.load(f)
    return a
def make_list_from_expert(expert_list):
    eli = []
    elf = []
    position = 0
    for cluster in expert_list:
        if isinstance(cluster, int):
            cluster = [cluster]
        for value in cluster:
            eli.append(position)
            elf.append(value)
        position += 1
    return elf, eli
def make_matrix_from_expert(expert_list):
    elf, eli = make_list_from_expert(expert_list)
    matrix = [[0 for _ in range(len(elf))] for _ in range(len(elf))]
    for i in range(len(eli)):
        for j in range(len(eli)):
            if eli[elf.index(i + 1)] <= eli[
                elf.index(j + 1)]:
                matrix[i][j] = 1
    return matrix
def get_kernel_of_nonequal(matrix_1, matrix_2):
    matrix_1 = np.array(matrix_1)
    matrix_2 = np.array(matrix_2)
    kernel = np.multiply(matrix_1, matrix_2)
    kernel_T = np.multiply(matrix_1.T, matrix_2.T)
    kernel_res = np.logical_or(kernel, kernel_T).astype(np.int32)
    result = []
    for i in range(len(kernel_res)):
        for j in range(len(kernel_res[i])):
            if kernel_res[i][j] == 0:
                pair = sorted([i + 1, j + 1])
                if pair not in result:
                    result.append(pair)
    cres = []
    visited = [0 for _ in range(len(result))]
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            set_1 = set(result[i])
            set_2 = set(result[j])
            if set_1.intersection(set_2):
                visited[i] = 1
                visited[j] = 1
                cres.append(list(set_1.union(set_2)))
        if result[i] not in cres and visited[i] == 0:
            cres.append(result[i])
    print(cres)
    return cres
def _in_kernel(value, kernel):
    for cluster in kernel:
        if value in cluster:
            return (True, cluster)
    return (False, [])
def make_experted_res_general(expert_1, expert_2, kernel):
    elf_1, eli_1 = make_list_from_expert(expert_1)
    elf_2, eli_2 = make_list_from_expert(expert_2)
    result = []
    for i in range(len(elf_1)):
        if isinstance(expert_1[i], int):
            expert_1[i] = [expert_1[i]]
        for j in range(len(elf_2)):
            pass
def make_experted_res(expert_1, expert_2, kernel):
    result = []
    for i in range(len(expert_1)):
        if isinstance(expert_1[i], int):
            expert_1[i] = [expert_1[i]]
        for j in range(len(expert_2)):
            if isinstance(expert_2[j], int):
                expert_2[j] = [expert_2[j]]
            expert_1_set = set(expert_1[i])
            expert_2_set = set(expert_2[j])
            for value in expert_1[i]:
                flag, cluster = _in_kernel(value, kernel)
                if flag:
                    if cluster not in result:
                        result.append(cluster)
                        break
            inter = expert_1_set.intersection(expert_2_set)
            if inter and not flag:
                if len(inter) > 1:
                    result.append(list(inter))
                else:
                    result.append(inter.pop())
    print(result)
def task():
    expert_A = [[1], [2, 3, 4], [5, 6, 7], 8, 9,
                10]  # read_json(r'D:\SystemAnalysis_Fall2023\task5\Ранжировка  A.json')
    expert_B = [[1, 2, 3], [4, 5], 6, 7, 9,
                [8, 10]]  # read_json(r'D:\SystemAnalysis_Fall2023\task5\Ранжировка  B.json')
    expert_C = [1, 4, 3, 2, 6, [5, 7, 8], [9, 10]]  # read_json(r'D:\SystemAnalysis_Fall2023\task5\Ранжировка  C.json')
    matrix_A = make_matrix_from_expert(expert_A)
    matrix_B = make_matrix_from_expert(expert_B)
    matrix_C = make_matrix_from_expert(expert_C)
    kernel_AB = get_kernel_of_nonequal(matrix_A, matrix_B)
    kernel_BC = get_kernel_of_nonequal(matrix_B, matrix_C)
if __name__ == '__main__':
    task()