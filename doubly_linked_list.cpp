struct DoublyNode {
    int data;
    DoublyNode *next, *prev;

    DoublyNode(int d) : data(d), next(nullptr), prev(nullptr) {}
};

class DoublyLinkedList {
public:
    DoublyNode* head;

    DoublyLinkedList() : head(nullptr) {}

    void append(int data) {
        DoublyNode* newNode = new DoublyNode(data);
        if (head == nullptr) {
            head = newNode;
        } else {
            DoublyNode* current = head;
            while (current->next != nullptr) {
                current = current->next;
            }
            current->next = newNode;
            newNode->prev = current;
        }
    }
};
