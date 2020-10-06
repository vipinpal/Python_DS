class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                print(data, 'is found')
                return True
            current = current.next
        print(data, 'not found')
        return False
    
    def length(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        print('lenght = ', count)
        return count

    def sum(self):
        sum = 0
        current = self.head
        while current != None:
            sum += current.data
            current = current.next
        print('sum is =', sum)
        return sum

    def isSortedDesc(self):
        current = self.head
        while current.next != None:
            if current.data < current.next.data:
                print('is not desc sorted')
                return False
            current = current.next
        print('is desc sorted')
        return True

if __name__ == '__main__':
    llist = LinkedList() 
  
    ''' Use push() to construct below list 
        14->21->11->30->10 '''
    llist.push(10) 
    llist.push(1)
    llist.push(11)
    llist.push(30)

    ''' search Node in Linked List'''
    llist.search(21)

    ''' Find Lenght of Linked List'''
    llist.length()

    '''Sum of All Node of Linked List'''
    llist.sum()

    ''' is desc sorted '''
    llist.isSortedDesc()





    