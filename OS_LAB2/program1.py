import threading
import time

TASKS = [
    ("Task 1", 1),
    ("Task 2", 1),
    ("Task 3", 1),
]

def do_task(task_name, waiting_time):
    thread_id = threading.get_ident()

    print(f"{task_name} STARTED || Thread ID = {thread_id}")
    time.sleep(waiting_time)
    print(f"{task_name} FINISHED || Thread ID = {thread_id}")

def single_threaded():
    print("\n========= SINGLE-THREADED ==========")

    start_time = time.perf_counter()
    for task_name, waiting_time in TASKS:
        do_task(task_name, waiting_time)

    end_time = time.perf_counter()
    elapsed = end_time - start_time

    print(f"Single-threaded time = {elapsed:2f}seconds.")
    return elapsed

def multi_threaded():
    print("\n========= MULTI-THREADED ==========")
    
    start_time = time.perf_counter()
    threads = []

    for task_name, waiting_time in TASKS:
        thread = threading.Thread(target=do_task, args=(task_name, waiting_time))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.perf_counter()
    elapsed = end_time - start_time

    print(f"Multi-threaded time = {elapsed:2f}seconds.")
    return elapsed


def demo():
    single_threaded()
    multi_threaded()

demo()