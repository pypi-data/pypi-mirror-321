import time
import random
from tqdm import tqdm
from datetime import datetime

from dscope.utils import dscopeLogToVectorLog, dscopeLogDump

transaction_log = []

class LogicalClock:
    def __init__(self):
        self.time = 0
        return

    def increment(self):
        self.time += 1
        return self.time

    def update(self, received_time):
        self.time = max(self.time, received_time) + 1
        return self.time

class Process:
    def __init__(self, pid, nproc, p):
        self.pid = pid
        self.clock = LogicalClock()
        self.nproc = nproc
        self.p = p
        return

    def execute_transaction(self):
        if random.random() < self.p and self.nproc > 1:
            dst_host = random.choice([i for i in range(self.nproc) if i != self.pid])
            self.send_message(dst_host)
        else:
            self.internal_transaction()
        return

    def send_message(self, dst_host):
        current_time = self.clock.increment()
        log_entry = (datetime.now().strftime("%m/%d/%Y %H:%M:%S.%f")[:-3], "send", f"#{self.pid}", f"#{dst_host}", f"{self.pid} 发给 {dst_host}")
        transaction_log.append(log_entry)
        time.sleep(random.uniform(0.01, 0.1))
        processes[dst_host].receive_message(self.pid, current_time)
        return

    def receive_message(self, src_host, received_time):
        current_time = self.clock.update(received_time)
        log_entry = (datetime.now().strftime("%m/%d/%Y %H:%M:%S.%f")[:-3], "recv", f"#{src_host}", f"#{self.pid}", f"{src_host} 发给 {self.pid}")
        transaction_log.append(log_entry)
        return

    def internal_transaction(self):
        current_time = self.clock.increment()
        log_entry = (datetime.now().strftime("%m/%d/%Y %H:%M:%S.%f")[:-3], "none", f"#{self.pid}", f"#{self.pid}", f"{self.pid} 内部事务")
        transaction_log.append(log_entry)
        return

def simulate_distributed_system(nproc, steps, p):
    global processes
    processes = [Process(i, nproc, p) for i in range(nproc)]

    for step in tqdm(range(steps)):
        for process in processes:
            process.execute_transaction()

    return

def vector_clock_simulator():
    from dscope.settings import (
        VECTOR_CLOCK_NPROC,
        VECTOR_CLOCK_STEPS,
        VECTOR_CLOCK_P,
    )
    simulate_distributed_system(
        VECTOR_CLOCK_NPROC,
        VECTOR_CLOCK_STEPS,
        VECTOR_CLOCK_P,
    )
    vector_log = dscopeLogToVectorLog(transaction_log)

    res_log = []
    for temp_vector_log in vector_log:
        temp_res_log = (temp_vector_log[0], temp_vector_log[1], temp_vector_log[2], f"{temp_vector_log[3]}, 向量时钟为: {temp_vector_log[2]}")
        res_log.append(temp_res_log)

    dscopeLogDump(res_log, "vector_clock.log")
    return "Vector clock simulate successfully!"