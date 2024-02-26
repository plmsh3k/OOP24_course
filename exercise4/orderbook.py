class Task:
    id = 1
    def __init__(self, description, programmer, workload):
        self.id = Task.id
        Task.id += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

class OrderBook():
    def __init__(self):
        self.orders = []
        self.programmers_names = []

    def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))
        self.programmers_names.append(programmer)

    def all_orders(self):
        return self.orders
    
    def programmers(self):
        return list(set(self.programmers_names))
    
    def mark_finished(self, id):
        for order in self.orders:
            if order.id == id:
                order.mark_finished()

    def finished_orders(self):
        return [order for order in self.orders if order.is_finished()]

    def unfinished_orders(self):
        return [order for order in self.orders if not order.is_finished()]

class OrderBookApplication:
    def __init__(self):
        self.orders = OrderBook()

    def instructions(self):
        print("commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        description = input("description: ")
        programmer, workload = input("programmer and workload estimate: ").split(' ')
        self.orders.add_order(description, programmer, workload)

    def list_finished(self):
        for order in self.orders.finished_orders():
            print(order)
    
    def list_unfinished(self):
        for order in self.orders.unfinished_orders():
            print(order)

    def mark(self):
        id = input("id: ")
        self.orders.mark_finished(id)

    def programmers(self):
        for programmer in self.orders.programmers():
            print(programmer)

    def run(self):
        self.instructions()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
                print('added!')
            elif command == "2":
                self.list_finished()
            elif command == "3":
                self.list_unfinished()
            elif command == "4":
                self.mark()
                print('marked as finished!')
            elif command == "5":
                self.programmers()
            else:
                self.instructions()


if __name__ == '__main__':
    inp = int(input())
    match inp:
        case 0:
            t1 = Task("program hello world", "Eric", 3)
            print(t1.id, t1.description, t1.programmer, t1.workload)
            print(t1)
            print(t1.is_finished())
            t1.mark_finished()
            print(t1)
            print(t1.is_finished())

            t2 = Task("program webstore", "Adele", 10)
            t3 = Task("program mobile app for workload accounting", "Eric", 25)
            print(t2)
            print(t3)
        case 1:
            orders=OrderBook()
            orders.add_order("program webstore","Adele",10)
            orders.add_order("program mobile app for workload accounting","Eric",25)
            orders.add_order("program app for practising mathematics","Adele",100)
            for order in orders.all_orders():
                print(order)
            
            print()
            
            for programmer in orders.programmers():
                print(programmer)
        case 2:
            orders=OrderBook()
            orders.add_order("program webstore","Adele",10)
            orders.add_order("program mobile app for workload accounting","Eric",25)
            orders.add_order("program app for practising mathematics","Adele",100)

            orders.mark_finished(1)
            orders.mark_finished(2)

            for order in orders.all_orders():
                print(order)
        case 3:
            app = OrderBookApplication()
            app.run()