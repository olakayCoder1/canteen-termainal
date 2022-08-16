class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None
    

    def pre_prepend(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return


    def print_nodes(self):
        if self.head == None :
            return None
        current_node = self.head
        while current_node.next_node != None :
            print(current_node.data)
            current_node = current_node.next_node
        if current_node.data != None:
            print(current_node.data)
            return


    def append_node(self,data):
        new_node = Node(data)
        if self.head == None :
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node != None :
            current_node = current_node.next_node
        current_node.next_node = new_node


    def insert_node_after(self, data , node ):
        new_node = Node(data)
        if self.head == None:
            return
        current_node = self.head
        while current_node.data != node :
            if current_node.next_node != None:
                current_node = current_node.next_node
            else:
                return f'No node with the given data : {node}'
        if current_node.next_node != None:
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
            return
        else:
            current_node.next_node = new_node
        return


    def insert_node_before(self, data , node ):
        new_node = Node(data)
        prev_node = None
        if self.head == None:
            return
        current_node = self.head
        while current_node.data != node :
            if current_node.next_node != None:
                prev_node = current_node
                current_node = current_node.next_node
            else:
                return f'No node with the given data : {node}'
        if prev_node != None:
            prev_node.next_node = new_node
            new_node.next_node = current_node
            return
        else:
            new_node.next_node = current_node
        return
        


    def delete_node(self, data):
        if self.head == None :
            return
        current_node = self.head
        prev_node = None
        while current_node.data != data :
            if current_node.next_node != None:
                prev_node = current_node
                current_node = current_node.next_node
            else:
                return
        if prev_node != None:
            prev_node.next_node = current_node.next_node
        else:
            self.head = current_node.next_node
        return

    def cascade_list(self):
        self.head = None
        return


class Food:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.id = 0
        self.next_food = None


class FoodList:
    def __init__(self):
        self.head = None
    

    def length_foods(self):
        if self.head == None :
            return 0
        current_node = self.head
        length = 0
        while current_node.next_food != None :
            length += 1
            current_node = current_node.next_food
        length += 1
        return length


    def add_new_spice(self,name, price):
        new_food = Food(name, int(price))
        if self.head == None:
            new_food.id = self.length_foods() + 1
            self.head = new_food 
            return
        current_node = self.head
        while current_node.next_food != None :
            current_node = current_node.next_food
        current_node.next_food = new_food
        new_food.id = self.length_foods()


    def find_food_price(self,id):
        if self.head == None:
            return
        current_node = self.head
        while current_node.next_food != None :
            if current_node.id == id :
                return current_node.price
            current_node = current_node.next_food
        if current_node.id == id :
            return current_node.price
        return 0


    def find_food_detail(self,id):
        if self.head == None:
            return
        current_node = self.head
        while current_node.next_food != None :
            if current_node.id == id :
                return (current_node.name , current_node.price)
            current_node = current_node.next_food
        if current_node.id == id :
            return (current_node.name , current_node.price )
        return

    

    def print_foods(self):
        if self.head == None :
            return None
        current_node = self.head
        while current_node.next_food != None :
            print(f'{current_node.name} -> {current_node.price}$ -> {current_node.id}' )
            current_node = current_node.next_food
        print(f'{current_node.name} -> {current_node.price}$ -> {current_node.id}' )
        return


foods = FoodList()
foods.add_new_spice('Amala',1000)
foods.add_new_spice('Rice',1040)
foods.add_new_spice('Beans',300)
foods.add_new_spice('Bread',600)
foods.add_new_spice('Spaghetti',1200)
foods.add_new_spice('Bragonni',500)
foods.add_new_spice('Indomie sauce',800)

class Customer:
    def __init__(self,bonus=5000,money_box=0):
        self.bonus = bonus
        self.money_box = money_box
    def add_money_to_box(self,price):
        current_balance = self.money_box
        if current_balance != None :
            if int(price) > 0 :
                self.money_box = int(self.money_box) + int(price)
            else :
                return "Negative value not allowed"
        else:
            self.money_box = int(price)
    def check_balance(self):
        return int(self.bonus) + int(self.money_box)


def canteen():
    print('Good day')
    ask = input('Would you like to go Meal Mall? Yes or No : ')
    if ask == 'Yes' or ask=='yes':
        new_customer = Customer()
        print(F'Congratulation, you have been given a bonus of {new_customer.bonus}$ for coming to our Canteen')
        print('What will you like to order from the list bellow')
        foods.print_foods()
        ask = input('Select the spices you want using their equivalent number eg 1 for Amala 5 for Spaghetti. For multiple spice enter with comma separated eg 1,6 for Amala and Bragonni\n :::::  ')
        if len(ask) > 0 :
            selected_foods = []
            for val in ask:
                if val == ' ' or val == ',' or val == '':
                    pass
                else:
                    selected_foods.append(val)
            price_accumulation = 0
            if len(selected_foods) > 0:
                for val in selected_foods:
                    price_accumulation += foods.find_food_price(int(val))
            if int(price_accumulation) > new_customer.check_balance():
                print('Insufficient fund')
                return
            else:
                receipt = []
                for food in selected_foods:
                    receipt.append(foods.find_food_detail(int(food)))
                print('Thanks for patronizing us. Your order details :')
                for detail in receipt :
                    print(detail)
    else:
        print('Thanks for your response')
        return


if __name__ == "__main__":
    canteen()
