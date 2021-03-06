import string
polymer = open("../input/day5_input.txt").readlines()


class Unit:
    def __init__(self, letter):
        self.letter = letter
        if letter.isupper():
            self.polar = True
        else:
            self.polar = False
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.still_reacting = True

    def add_list_item(self, item):
        if isinstance(item, Unit):
            if self.head is None:
                self.head = item
                item.previous = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.previous = self.tail
                self.tail = item

    def find_reaction(self):
        current = self.head
        reacted_this_cycle = False
        while True:
            if current == self.tail:
                if reacted_this_cycle == False:
                    self.still_reacting = False
                return
            if current.next.letter.lower() == current.letter.lower() and current.next.polar != current.polar:
                reacted_this_cycle = True
                if current == self.head:
                    self.head = current.next.next
                    self.head.previous = None
                elif current.next == self.tail:
                    self.tail = current.previous
                    self.tail.next = None
                else:
                    current.previous.next = current.next.next
                    current.next.next.previous = current.previous
                    current.next = current.next.next
            current = current.next

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.letter, end='')
            current = current.next

    def find_length(self):
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return length


letter_dict = {}
for letter in string.ascii_lowercase:
    print(letter)
    polymer_dll = DoubleLinkedList()
    new_polymer = [unit for unit in polymer[0] if unit.lower() != letter]
    for x in range(0, len(new_polymer)):
        next_unit = Unit(new_polymer[x])
        polymer_dll.add_list_item(next_unit)

    still_reacting = True
    while still_reacting:
        polymer_dll.find_reaction()
        if polymer_dll.still_reacting == False:
            break
    print("\n" + str(polymer_dll.find_length()))
    letter_dict[letter] = polymer_dll.find_length()

print(max(letter_dict.values()))
