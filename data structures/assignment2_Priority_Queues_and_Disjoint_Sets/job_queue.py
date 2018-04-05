# python3

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

    def CompareWorker(self, worker1, worker2):
        if worker1[1] != worker2[1]:
            return worker1[1] < worker2[1]
        else:
            return worker1[0] < worker2[0]

    def SiftDown(self,i):
        minIndex=i
        left=2*i+1
        if left<self.num_workers and self.CompareWorker(next_free_time[left],next_free_time[minIndex]):
            minIndex=left
        right=2*i+2
        if right<self.num_workers and self.CompareWorker(next_free_time[right],next_free_time[minIndex]):
            minIndex=right
        if i!=minIndex:
            next_free_time[i], next_free_time[minIndex] = next_free_time[minIndex], next_free_time[i]
            self.SiftDown(minIndex)

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        global next_free_time
        next_free_time = [[i,0] for i in range(self.num_workers)]
        for i in range(len(self.jobs)):
          #
          self.assigned_workers[i] = next_free_time[0][0]
          self.start_times[i] = next_free_time[0][1]
          next_free_time[0][1]+= self.jobs[i]
          self.SiftDown(0)



    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

