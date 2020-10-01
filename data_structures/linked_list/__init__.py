class Node:        #Class to creat node
    def __init__(self, item, next):   #structure
        self.item = item              #node item(data) part
        self.next = next              #node next(adress) part 


class LinkedList:
    def __init__(self):               #creating head of linked list
        self.head = None
        self.size = 0

    def add(self, item):             #creating 1st node
        self.head = Node(item, self.head)       #storing address of 1st node in head
        self.size += 1

    def remove(self):                #function to remove  node
        if self.is_empty():          # if there is no any node then it will return None
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            self.size -= 1
            return item

    def is_empty(self):              #This function use to check Linked list is empty or not
        return self.head is None

    def __len__(self):
        """
        >>> linked_list = LinkedList()
        >>> len(linked_list)
        0
        >>> linked_list.add("a")
        >>> len(linked_list)
        1
        >>> linked_list.add("b")
        >>> len(linked_list)
        2
        >>> _ = linked_list.remove()
        >>> len(linked_list)
        1
        >>> _ = linked_list.remove()
        >>> len(linked_list)
        0
        """
        return self.size
