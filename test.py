class SinglyLinkedNode(object):

    def __init__(self, item=None, next_link=None):
        super(SinglyLinkedNode, self).__init__()
        self._item = item
        self._next = next_link

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    def __repr__(self):
        return repr(self.item)


class SinglyLinkedList(object): 

    def __init__(self):
        super(SinglyLinkedList, self).__init__()
        self._head = None

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, head):
        self._head = SinglyLinkedNode(head)

    def __len__(self):
        length = 0
        current = self.head;
        while (current.next != None):
            length += 1
            current = current.next
        return length

    def __iter__(self):
        current = self.head
        print current.item
        while (current.item is not None):
            yield current.item
            current = current.next

    def __contains__(self, item):
        current = self.head
        for i in range(0,__len__()):
            if (current.item() == item):
                return True
            elif (current.next() is not None):
                current = current.next()
        return False

    def remove(self, item):
        previous = None
        current = self.head
        while (current.item is not None):
            if (current.item == item):
                if (previous is None):
                    self.head = current.next
                else: 
                    previous.next = current.next
                return True
            else:
                previous = current
                current = current.next
        return False

    def prepend(self, item):
        if (self.head is None):
            self.head = SinglyLinkedNode(item)
        else:
            temp = self.head
            self.head = item
            self.head.next = temp

    def __repr__(self):
        s = "List:" + "->".join([item for item in self])
        return s

def main():
    print "Testing"
    test = SinglyLinkedList()
    test.prepend(4)
    test.prepend(5)
    test.prepend(6)
    print test.__len__


if __name__ == '__main__':
    main()