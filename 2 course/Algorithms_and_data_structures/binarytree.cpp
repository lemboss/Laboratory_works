#include <iostream>
#include <sstream>
#include <map>
using namespace std;

struct Node
{
    int data;
    Node* pLeft;
    Node* pRight;
    Node(int data = 0, Node* pLeft = nullptr, Node* pRight = nullptr)
    {
        this->data = data;
        this->pLeft = pLeft;
        this->pRight = pRight;
    }
};

void BuildTree(Node** root)
{
    int data;
    while (true)
    {
        cout << "Input num" << endl;
        cin >> data;
        if (data == 0) break;
        Node* node = new Node(data);
        if (*root == nullptr)
            *root = node;
        else
        {
            Node* tmp = *root;
            while (tmp->pLeft != nullptr || tmp->pRight != nullptr)
            {
                if (data > tmp->data)
                {
                    if (tmp->pRight != nullptr)
                        tmp = tmp->pRight;
                    else
                        break;
                }
                else if (data < tmp->data)
                {
                    if (tmp->pLeft != nullptr)
                        tmp = tmp->pLeft;
                    else
                        break;
                }
            }
            if (data > tmp->data)
                tmp->pRight = node;
            else if (data < tmp->data)
                tmp->pLeft = node;
        }
    }
}

Node* Search(Node* root, int key, int& counter)
{
    if (root->pLeft == nullptr && root->pRight == nullptr || key == root->data)
    {
        counter += 3;
        return root;
    }
    if (key < root->data)
    {
        counter++;
        return Search(root->pLeft, key, counter);
    }
    else
    {
        counter++;
        return Search(root->pRight, key, counter);
    }
}

void Print(map <int, string> &dict, Node* root, int stage = 0)
{
    if (root != nullptr)
    { 
        ostringstream temp;
        temp << root->data;
        string num = temp.str();

        dict[stage] += num + " ";
        Print(dict, root->pLeft, stage+=1);
        stage--;
        Print(dict, root->pRight, stage+=1);
        stage--;
    }
    if (stage == 0)
    {
        map <int, string> ::iterator it = dict.begin();
        while (it != dict.end())
        {
            cout << it->second << endl;
            it++;
        }

    }
}

Node* Search(Node* root, int key)
{
    if (root->pLeft == nullptr && root->pRight == nullptr || key == root->data)
        return root;
    if (key < root->data)
        return Search(root->pLeft, key);
    else
        return Search(root->pRight, key);
}

Node* SearchParent(Node* root, int key, Node* tmp = nullptr)
{
    if (root->pLeft == nullptr && root->pRight == nullptr || key == root->data)
        return tmp;
    if (key < root->data)
    {
        Node* tmp = root;
        return SearchParent(root->pLeft, key, tmp);
    }
    else
    {
        Node* tmp = root;
        return SearchParent(root->pRight, key, tmp);
    }
}

Node* SearchNext(Node* root, int key, int left, int right)
{
    if (root->data > left && root->data < right && root->pLeft == nullptr && root->pRight == nullptr)
        return root;
    if (key < root->data)
        return SearchNext(root->pLeft, key, left, right);
    else
        return SearchNext(root->pRight, key, left, right);
}

Node SetBarrier(Node** root, Node* barrier, int key)
{
    if ((*root)->pLeft == nullptr && (*root)->pRight == nullptr)
    {
        (*root)->pLeft = barrier;
        (*root)->pRight = barrier;
        return *(*root);
    }
    SetBarrier(&(*root)->pLeft, barrier, key);
    SetBarrier(&(*root)->pRight, barrier, key);
}

Node* SearchBarrier(Node* root, int key, int& counter)
{
    Node* barrier = new Node(key);
    SetBarrier(&root, barrier, key);
    if (key == root->data)
    {
        counter++;
        return root;
    }
    if (key < root->data)
    {
        counter++;
        return Search(root->pLeft, key, counter);
    }
    else
    {
        counter++;
        return Search(root->pRight, key, counter);
    }
    if (root->pLeft == barrier)
    {
        counter++;
        return root;
    }
}

void Insert(Node** root, int data)
{
    Node* tmp = *root;
    while (tmp->pLeft != nullptr || tmp->pRight != nullptr)
    {
        if (data > tmp->data)
        {
            if (tmp->pRight != nullptr)
                tmp = tmp->pRight;
            else
                break;
        }
        else if (data < tmp->data)
        {
            if (tmp->pLeft != nullptr)
                tmp = tmp->pLeft;
            else
                break;
        }
    }
    if (data > tmp->data)
        tmp->pRight = new Node(data);
    else
        tmp->pLeft = new Node(data);
}

void Delete(Node** root, int data)
{
    Node* tmp = Search(*root, data);
    if (tmp->pLeft != nullptr && tmp->pRight != nullptr)
    {
        Node* parent = SearchParent(*root, data);
        Node* newElem = SearchNext(tmp, data, tmp->pLeft->data, tmp->pRight->data);
        newElem->pLeft = tmp->pLeft;
        newElem->pRight = tmp->pRight;
        if (parent->pLeft == tmp)
            parent->pLeft = newElem;
        else
            parent->pRight = newElem;
    }
    else if (tmp->pLeft == nullptr || tmp->pRight == nullptr)
    {
        Node* parent = SearchParent(*root, data);
        if (parent->pLeft == tmp)
        {
            if (tmp->pLeft != nullptr)
                parent = tmp->pLeft;
            else
                parent = tmp->pRight;
        }
        else
        {
            if (tmp->pRight != nullptr)
                parent = tmp->pLeft;
            else
                parent = tmp->pRight;
        }
    }
    delete[] tmp;
    tmp = nullptr;
}

int main()
{
    Node* root = nullptr;
    int counter = 0;
    map <int, string> dict;
    BuildTree(&root);
    Print(dict, root);
    /*Node* a = Search(root, 8, counter);
    Node* p = SearchParent(root, 8);
    Delete(&root, 8);*/
    return 0;
}
