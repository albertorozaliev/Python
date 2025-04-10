import random
import multiprocessing
import psutil



def split_array(array, numProcesses):
    a = len(array) // numProcesses
    b = len(array) % numProcesses
    result = []
    start = 0

    for i in range(numProcesses):
        end = start + a + (1 if i < b else 0)
        result.append(array[start:end])
        start = end

    return result

def bubble(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def sort(arr, output, index):
    sorted_part = bubble(arr)
    output[index] = sorted_part

def merge_sorted_chunks(chunks):
    result = []
    indices = [0] * len(chunks)

    while True:
        min_val = None
        min_chunk = -1

        for i, chunk in enumerate(chunks):
            if indices[i] < len(chunk):
                if min_val is None or chunk[indices[i]] < min_val:
                    min_val = chunk[indices[i]]
                    min_chunk = i

        if min_val is None:
            break

        result.append(min_val)
        indices[min_chunk] += 1

    return result

def save(result, filename="result.txt"):
    with open(filename, "w") as a:
        for item in result:
            a.write(f"{item}")

if __name__ == "__main__":
    array = []
    print("Выберите количество элементов в массиве")
    numElements = int(input())
    for _ in range(numElements):
        array.append(random.randint(0,1000))
    print(array)

    cores = multiprocessing.cpu_count()

    current_cpu_usage = psutil.cpu_percent(interval=1)

    available_cores = int(cores * (1 - current_cpu_usage / 100))

    print(f"Доступно: {available_cores}\n")

    while True:
        print("Выберите количество ядер")
        numProcesses = int(input())
        if numProcesses>available_cores or numProcesses>len(array):
            print("Слишком много")
        else:
            break

    littleArray = split_array(array, numProcesses)

    for i in range(len(littleArray)):
        chunk = littleArray[i]
        print(f"{i + 1}: {chunk}")

    manager = multiprocessing.Manager()
    output = manager.dict()

    processes = []

    for i in range(numProcesses):
        pro = multiprocessing.Process(target=sort, args=(littleArray[i], output, i))
        processes.append(pro)
        pro.start()

    for pro in processes:
        pro.join()

    sorted_chunks = [output[i] for i in range(numProcesses)]

    for i, part in enumerate(sorted_chunks):
        print(f"{i + 1}: {part}")

    final_array = merge_sorted_chunks(sorted_chunks)

    print(final_array)

    save_process = multiprocessing.Process(target=save, args=(final_array,))
    save_process.start()
    save_process.join()
