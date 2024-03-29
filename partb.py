import multiprocessing

def combinations_b(arr, sides):
    result = []
    n = len(arr)
    for i in range(1 << n):
        temp = []
        for j in range(n):
            if (i & (1 << j)) != 0:
                temp.append(arr[j])
        if len(temp) == sides:
            result.append(temp)
    return result

def combinations_a(arr, sides):
    result = []
    n = len(arr)
    for i in range(int(n ** sides)):
        temp = []
        t = i
        for j in range(sides):
            index = t % n
            temp.append(arr[index])
            t //= n
        result.append(temp)
    return result

def check_maps(possibles_a, possibles_b, map_probabilities):
    generated_probability = find_probabilities(possibles_a, possibles_b)
    return map_probabilities == generated_probability

def find_probabilities(dice_a, dice_b):
    result = {}
    for num1 in dice_a:
        for num2 in dice_b:
            sum_ = num1 + num2
            result[sum_] = result.get(sum_, 0) + 1
    return result

def worker(possibles_a_chunk, possibles_b, map_probabilities, result_queue):
    for p1 in possibles_a_chunk:
        for p2 in possibles_b:
            if check_maps(p1, p2, map_probabilities):
                result_queue.put((p1, p2))

def find_matching_pair_parallel(possibles_a, possibles_b, map_probabilities):
    num_processes = multiprocessing.cpu_count()
    chunk_size = len(possibles_a) // num_processes

    result_queue = multiprocessing.Queue()
    processes = []

    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_processes - 1 else len(possibles_a)
        process = multiprocessing.Process(target=worker, args=(possibles_a[start:end], possibles_b, map_probabilities, result_queue))
        processes.append(process)
        process.start()

    matching_pair = None

    for process in processes:
        process.join()

    while not result_queue.empty():
        matching_pair = result_queue.get()
        break  # Exit loop after getting the first pair

    return matching_pair

if __name__ == "__main__":
    num1 = [1, 2, 3, 4]
    num2 = [1, 2, 3, 4, 5, 6, 7, 8]
    sides = 6
    dice_a = [1, 2, 3, 4, 5, 6]
    dice_b = [1, 2, 3, 4, 5, 6]
    possibles_a = combinations_a(num1, sides)
    possibles_b = combinations_b(num2, sides)

    map_probabilities = find_probabilities(dice_a, dice_b)

    matching_pair = find_matching_pair_parallel(possibles_a, possibles_b, map_probabilities)

    if matching_pair:
        new_dice_a, new_dice_b = matching_pair
        print("Transformed Dice A:", new_dice_a)
        print("Transformed Dice B:", new_dice_b)
    else:
        print("No matching pair found.")
