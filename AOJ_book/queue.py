import sys


class Queue:
    def __init__(self):
        self.Q = []

    def isEmpty(self):
        return len(self.Q) == 0

    def enqueue(self, x):
        self.Q.append(x)

    def dequeue(self):
        if self.isEmpty():
            sys.exit("Empty")
        else:
            return self.Q.pop(0)


# ローカルチェック用
# process_list = [('p1',150),('p2',80),('p3',200),('p4',350),('p5',20)]
# power= 100

n, power = map(int, raw_input().split(" "))
process_list = [map(str, raw_input().split(" ")) for i in range(n)]
process_list = [(p[0], int(p[1])) for p in process_list]

q = Queue()
for p in process_list:
    q.enqueue(p)
elapsed_time = 0
while not q.isEmpty():
    process = q.dequeue()
    if process[1] > power:
        elapsed_time += power
        q.enqueue((process[0], process[1] - power))
    else:
        elapsed_time += process[1]
        print(str(process[0]) + " " + str(elapsed_time))
