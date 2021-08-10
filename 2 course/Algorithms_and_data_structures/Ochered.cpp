#include<iostream>
#include<stdio.h>
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
void Push(Node** head, Node** tail) 
{
	int num = 0;
	while (num != 123)
	{
		cin >> num;
		Node* tmp = new Node(num);
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
}
void PrintQueue(Node* head) 
{
	Node* tmp = head;
	while (tmp->pNext != nullptr) 
	{
		cout << tmp->data << endl;
		tmp = tmp->pNext;
	}
	cout << tmp->data << endl;
}

void PopLeft(Node** head, Node** tail)
{
	Node* tempH = *head;
	Node* tempT = *tail;
	tempT = tempT->pPrev;
	//delete* head;
	tempH = tempH->pNext;
	*head = tempH;
	*tail = tempT;
}

const int SIZE = 5;
struct Queue
{
	int data[SIZE];
	int head, tail;
};

void Init(Queue* queue) 
{
	queue->head = 1;
	queue->tail = 0;
}

void Push(Queue* queue)
{
	int num = 0;
	cout << "Сколько элементов заполнить?" << endl;
	int count;
	cin >> count;
	for (int i = 0; i < count; i++)
	{
		cin >> num;
		if (queue->tail < SIZE-1)
		{
			queue->data[queue->tail] = num;
			queue->tail++;
		}
		else
		{
			cout << "Очередь полна" << endl;
			break;
		}
	}
}
int is_Empty(Queue* queue)
{
	if (queue->tail < queue->head)
		return 1;
	else
		return 0;
}
void PrintQueue(Queue* queue) 
{
	if (is_Empty(queue) == 1)
		cout << "Очередь пуста" << endl;
	else 
	{
		for (int i = 0; i < queue->tail; i++)
			cout << queue->data[i] << endl;
	}
}
void delete_q_s(Queue* queue) 
{
	int num;
	if (is_Empty(queue) == 1)
		cout << "Очередь пуста" << endl;
	else 
	{
		num = queue->data[queue->head];
		for (int i = 0; i < queue->tail; i++)
			queue->data[i] = queue->data[i + 1];
		queue->tail--;
	}
}
int main() {
	setlocale(LC_ALL, "ru");
	Node* head = nullptr;
	Node* tail = nullptr;
	Queue queue;
	//Push(&head, &tail);
	//PrintQueue(head);
	//PopLeft(&head, &tail);
	//PrintQueue(head);
	//PopLeft(&head, &tail);
	//PrintQueue(head);
	Init(&queue);
	Push(&queue);
	is_Empty(&queue);
	PrintQueue(&queue);
	delete_q_s(&queue);
	PrintQueue(&queue);
}