# python3
from collections import deque
class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = deque([])

    def Process(self, request):
        # write your code here
        if not self.finish_time_:
            self.finish_time_.append(request.process_time+request.arrival_time)
            return (Response(False, request.arrival_time))
        if request.arrival_time>=self.finish_time_[0]:
            i=0
            while self.finish_time_[i]<=request.arrival_time:
                self.finish_time_.popleft()
                i+=1
                if i>len(self.finish_time_)-1:
                    break
            if self.finish_time_:
                added_time=self.finish_time_[-1]
            if not self.finish_time_:
                added_time=0
            if request.arrival_time>= added_time:
                self.finish_time_.append(request.process_time+request.arrival_time)
                return (Response(False, request.arrival_time))
            else:
                self.finish_time_.append(request.process_time+added_time)
                return (Response(False, added_time))
        if len(self.finish_time_)==self.size:
            return (Response(True, -1))
        if len(self.finish_time_)<self.size:
            added_time=self.finish_time_[-1]
            self.finish_time_.append(request.process_time+added_time)
            return (Response(False, added_time))



def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))

    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
