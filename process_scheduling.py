import itertools


class Process():
    def __init__(self, name=None, burst=None,
                 arrival_time=None, priority=None,
                 time_slice=None, waiting_time=None,
                 turnaround_time=None):
        self.name = name
        self.burst = burst
        self.arrival_time = arrival_time
        self.priority = priority
        self.time_slice = time_slice
        self.waiting_time = waiting_time
        self.turnaround_time = turnaround_time


process1 = Process('P1', 10, 0, 5, 6)
process2 = Process('P2', 29, 0, 1, 6)
process3 = Process('P3', 3, 0, 3, 6)
process4 = Process('P4', 7, 0, 4, 6)
process5 = Process('P5', 12, 0, 2, 6)

processes1 = [process1, process2, process3, process4, process5]

process6 = Process('P1', 2, 0, 2, 2)
process7 = Process('P2', 1, 0, 1, 2)
process8 = Process('P3', 8, 0, 4, 2)
process9 = Process('P4', 4, 0, 2, 2)
process10 = Process('P5', 5, 0, 3, 2)

processes2 = [process6, process7, process8, process9, process10]


def fcfs(processes):
    processes.sort(key=lambda process: process.arrival_time)
    current_time = processes[0].arrival_time
    for process in processes:
        if process.arrival_time > current_time:
            current_time = process.arrival_time
        process.waiting_time = current_time - process.arrival_time
        current_time += process.burst
        process.turnaround_time = current_time - process.arrival_time
    average_waiting_time = sum(
        process.waiting_time for process in processes) / len(processes)
    for process in processes:
        print('process name: ', process.name, ' burst time: ', process.burst, ' arrival time: ', process.arrival_time,
              ' priority: ', process.priority, ' waiting time: ', process.waiting_time, ' turnaround time: ', process.turnaround_time)
    print('FCFS average waiting time: ', average_waiting_time)


def rr(processes):
    processes.sort(key=lambda process: process.arrival_time)
    for i in range(len(processes)):
        processes[i].remaining_burst = processes[i].burst
    current_time = processes[0].arrival_time
    for i in itertools.cycle(range(len(processes))):
        if all(process.remaining_burst == 0 for process in processes):
            break
        if processes[i].arrival_time > current_time or processes[i].remaining_burst == 0:
            continue
        current_burst = min(
            processes[i].remaining_burst, processes[i].time_slice)
        processes[i].remaining_burst -= current_burst
        current_time += current_burst
        if processes[i].remaining_burst == 0:
            processes[i].completion_time = current_time
    for i in range(len(processes)):
        processes[i].waiting_time = processes[i].completion_time - \
            processes[i].arrival_time - processes[i].burst
        processes[i].turnaround_time = processes[i].completion_time - \
            processes[i].arrival_time
    average_waiting_time = sum(
        process.waiting_time for process in processes) / len(processes)
    for process in processes:
        print('process name: ', process.name, ' burst time: ', process.burst, ' arrival time: ', process.arrival_time,
              ' priority: ', process.priority, ' waiting time: ', process.waiting_time, ' turnaround time: ', process.turnaround_time)
    print('RR average waiting time: ', average_waiting_time)


def sjf(processes):
    processes.sort(key=lambda process: process.burst)
    current_time = processes[0].arrival_time

    for process in processes:
        if process.arrival_time > current_time:
            current_time = process.arrival_time
        process.waiting_time = current_time - process.arrival_time
        current_time += process.burst
        process.turnaround_time = current_time - process.arrival_time
    average_waiting_time = sum(
        process.waiting_time for process in processes) / len(processes)
    for process in processes:
        print('process name: ', process.name, ' burst time: ', process.burst, ' arrival time: ', process.arrival_time,
              ' priority: ', process.priority, ' waiting time: ', process.waiting_time, ' turnaround time: ', process.turnaround_time)
    print('SJF average waiting time: ', average_waiting_time)


def priority(processes):
    processes.sort(key=lambda process: process.priority)
    current_time = processes[0].arrival_time
    for process in processes:
        if process.arrival_time > current_time:
            current_time = process.arrival_time
        process.waiting_time = current_time - process.arrival_time
        current_time += process.burst
        process.turnaround_time = current_time - process.arrival_time
    average_waiting_time = sum(
        process.waiting_time for process in processes) / len(processes)
    for process in processes:
        print('process name: ', process.name, ' burst time: ', process.burst, ' arrival time: ', process.arrival_time,
              ' priority: ', process.priority, ' waiting time: ', process.waiting_time, ' turnaround time: ', process.turnaround_time)
    print('Priority average waiting time: ', average_waiting_time)


# fcfs(processes1)
# fcfs(processes2)
# rr(processes1)
# rr(processes2)
# rr(processes2)
# sjf(processes1)
# sjf(processes2)
# priority(processes1)
priority(processes2)
