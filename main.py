# python3
def parallel_processing(n, m, data):
    threads = [(0, i) for i in range(n)] 
    output = [] 
    for i in range(m):
        job_time = data[i] 
        thread = min(threads) 
        start_time = thread[0]
        output.append((thread[1], start_time))
        threads.remove(thread) 
        threads.append((start_time + job_time, thread[1]))
    return output 


def main():
    n, m = map(int, input().split()) 
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data) 
    for i in range(m): 
        print(result[i][0], result[i][1]) 
    

if __name__ == "__main__":
    main()
