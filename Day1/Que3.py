'''
c3) The Smart Printer Queue (Priority Queue)
An office printer handles jobs in order, BUT jobs marked URGENT must be printed before normal jobs Design a system using two queues one for urgent, one for normal-and always drain urgent first
'''

class PrinterQueue:
    def __init__(self):
        self.urgent_queue = []
        self.normal_queue = []

    def add_job(self, job, priority):
        if priority.lower() == "urgent":
            self.urgent_queue.append(job)
        else:
            self.normal_queue.append(job)

    def print_job(self):
        if self.urgent_queue:
            print("Printing Urgent Job:", self.urgent_queue.pop(0))
        elif self.normal_queue:
            print("Printing Normal Job:", self.normal_queue.pop(0))
        else:
            print("No jobs to print.")

    def display(self):
        print("Urgent Queue:", self.urgent_queue)
        print("Normal Queue:", self.normal_queue)


# Driver Code
printer = PrinterQueue()

printer.add_job("Document1", "Normal")
printer.add_job("Report", "Urgent")
printer.add_job("Invoice", "Normal")
printer.add_job("Project", "Urgent")

printer.display()

printer.print_job()
printer.print_job()
printer.print_job()
printer.print_job()
printer.print_job()