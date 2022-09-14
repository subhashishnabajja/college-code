class RR:
    time_quantam = 4

    def __init__(self, processes):
        self.FIFO = processes
  
        self.num_of_processes = len(processes)


    def schedule(self):
        
        burst = 0
        sum = 0
        while len(self.FIFO) > 0:
            process = self.FIFO.pop(0)
            print(f"Process {process.process_name} entered at {burst}")

            if process.burst_time > self.time_quantam:
                burst += self.time_quantam
                process.burst_time -= self.time_quantam
                self.FIFO.append(process)
                
            else:
                burst += process.burst_time

            sum += burst
            print(f"Process {process.process_name} exited at {burst}")
          
        

class Process:
    def __init__(self,process_name:str, burst_time:int):
        self.process_name = process_name
        self.burst_time = burst_time


if __name__ == "__main__":
    processes = [
        Process("1", 24),
        Process("2", 3),
        Process("3", 3)
    ]


    rr = RR(processes)
    rr.schedule()