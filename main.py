# python3
import heapq

def parallel_processing(n, m, data):
    threads = [(0, i) for i in range(n)] 
    heapq.heapify(threads)
    output = [] 
    for i in range(m):
        job_time = data[i] 
        thread = heapq.heappop(threads) 
        start_time = thread[0]
        output.append((thread[1], start_time))
        heapq.heappush(threads, (start_time + job_time, thread[1]))
    return output 


def main():
    n, m = map(int, input().split()) 
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data) 
    for i in range(m): 
        print(result[i][0], result[i][1]) 
    

if __name__ == "__main__":
    main()
