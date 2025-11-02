import threading
​
def task_master(arr):
    results = [0] * len(arr)
    threads = []
    
    def worker(func, index):
        results[index] = func()
        
    for i, func in enumerate(arr):
        thread = threading.Thread(target=worker, args=(func, i))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return sum(results)