#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node* pNext;
    Node* pPrev;

    Node(int data = 0, Node* pNext = nullptr, Node* pPrev = nullptr)
    {
        this->data = data;
        this->pNext = pNext;
        this->pPrev = pPrev;
    }
};

bool IsEmpty(Node* head)
{
    if (head == nullptr)
        return 1;
    else
        return 0;
}

void Push(Node** head, Node** tail, int data)
{
    Node* tmp = new Node(data);
    if (*head == nullptr)
    {
        *head = tmp;
        *tail = tmp;
    }
    else
    {
        Node* ttt = *tail;
        tmp->pPrev = *tail;
        ttt->pNext = tmp;
        ttt = tmp;
        *tail = ttt;
        
    }
}

void PrintH(Node* head)
{
    Node* tmp = head;
    while (tmp->pNext != nullptr)
    {
        cout << tmp->data << endl;
        tmp = tmp->pNext;
    }
    cout << tmp->data << endl;
}
void PrintT(Node* tail)
{
    Node* tmp = tail;
    while (tmp->pPrev != nullptr)
    {
        cout << tmp->data << endl;
        tmp = tmp->pPrev;
    }
    cout << tmp->data << endl;
}

void Insert(Node** head, int data, int index)
{
    if (index == 0)
    {
        *head = new Node(data, *head);
    }
    else
    {
        Node* prev = *head;
        for (int i = 0; i < index - 1; i++)
            prev = prev->pNext;
        Node* node = new Node(data, prev->pNext);
        prev->pNext = node;
    }
}

void PopFront(Node** head)
{
    Node* tmp = head[0];
    head[0] = head[0]->pNext;
    delete tmp;
}

void PrintList(Node* head)
{
    if (head != nullptr)
    {
        Node* current = head;
        while (current->pNext != nullptr)
        {
            cout << current->data << endl;
            current = current->pNext;
        }
        cout << current->data << endl;
    }
}

void Clear(Node** head)
{
    while (*head != nullptr)
        PopFront(&head[0]);
}

struct list
{
    int* data;
    int size;
};

void Init(list* lst)
{
    lst->size = 0;
}

bool IsEmpty(list* list)
{
    if (list->size == 0)
        return 1;
    else
        return 0;
}

void push(list* lst, int data)
{
    if (lst->size == 0)
    {
        lst->data = new int[lst->size + 1];
        lst->data[0] = data;
        lst->size++;
    }
    else
    {
        const int SIZE = lst->size + 1;
        int* tmp = new int[SIZE];
        for (int i = 0; i < lst->size; i++)
            tmp[i] = lst->data[i];
        tmp[SIZE - 1] = data;
        lst->data = new int[SIZE];
        for (int i = 0; i < SIZE; i++)
            lst->data[i] = tmp[i];
        lst->size++;
        delete[] tmp;
    }
}

void insert(list* lst, int data, int index)
{
    if (index == 0)
    {
        const int SIZE = lst->size + 1;
        int* tmp = new int[SIZE];
        tmp[0] = data;
        for (int i = 0; i < SIZE; i++)
            tmp[i] = lst->data[i];
        lst->data = new int[SIZE];
        for (int i = 0; i < SIZE; i++)
            lst->data[i] = tmp[i];
    }
    else
    {
        const int SIZE = lst->size + 1;
        int* tmp = new int[SIZE];
        for (int i = 0; i < index; i++)
            tmp[i] = lst->data[i];
        tmp[index] = data;
        for (int i = index; i < SIZE; i++)
            tmp[i] = lst->data[i];
        lst->data = new int[SIZE];
        for (int i = 0; i < SIZE; i++)
            lst->data[i] = tmp[i];
        lst->size++;
        delete[] tmp;
    }
}

void popfront(list* lst)
{
    
    const int SIZE = lst->size - 1;
    int* tmp = new int[SIZE];
    for (int i = 1; i < SIZE; i++)
        tmp[i-1] = lst->data[i];
    lst->data = new int[SIZE];
    for (int i = 0; i < SIZE; i++)
        lst->data[i] = tmp[i];
    lst->size--;
    delete[] tmp;
}

void printlist(list* lst)
{
    for (int i = 0; i < lst->size; i++)
        cout << lst->data[i] << '\t';
    cout << endl;
}

void clear(list* lst)
{
    while (lst)
        popfront(lst);
}

int main()
{
    Node* head = nullptr;
    Node* tail = nullptr;
    Push(&head, &tail, 3);
    Push(&head, &tail, 2);
    Push(&head, &tail, 4);
    PrintH(head);
    PrintT(tail);


    /*Insert(&head, 0, 1);
    PrintList(head);
    PopFront(&head);
    PrintList(head);
    Clear(&head);
    PrintList(head);*/

    /*list lst;
    Init(&lst);
    push(&lst, 3);
    push(&lst, 2);
    push(&lst, 4);*/
    return 0;
}
