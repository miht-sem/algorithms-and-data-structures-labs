#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

struct Node
{
    string value;
    Node *left;
    Node *right;
};

Node *addToTree(Node *root, string &num)
{
    if (root == nullptr)
    {
        Node *root = new Node();
        root->value = num;
        root->left = root->right = nullptr;
        return root;
    }

    if (num < root->value)
    {
        root->left = addToTree(root->left, num);
    }
    else if (num > root->value)
    {
        root->right = addToTree(root->right, num);
    }
    return root;
}

bool exists(Node *root, string &x)
{
    if (root == nullptr)
    {
        return false;
    }
    if (root->value == x)
    {
        return true;
    }
    else if (root->value > x)
    {
        return exists(root->left, x);
    }
    else
    {
        return exists(root->right, x);
    }
}

Node *minValue(Node *root)
{
    if (root->left == nullptr)
    {
        return root;
    }
    return minValue(root->left);
}

Node *deleteNode(Node *root, string &x)
{
    if (root == nullptr)
    {
        return root;
    }

    if (x < root->value)
    {
        root->left = deleteNode(root->left, x);
    }
    else if (x > root->value)
    {
        root->right = deleteNode(root->right, x);
    }
    else if (root->left != nullptr && root->right != nullptr)
    {
        root->value = minValue(root->right)->value;
        root->right = deleteNode(root->right, root->value);
    }
    else if (root->left != nullptr)
    {
        root = root->left;
    }
    else if (root->right != nullptr)
    {
        root = root->right;
    }
    else
    {
        root = nullptr;
    }

    return root;
}

void printTree(Node *node)
    {
        if (node != nullptr)
        {
            printTree(node->left);
            cout << " " << node->value;
            printTree(node->right);
        }
    }

struct Map
{
    string key = "";
    Node *values = nullptr;
    int size = 0;
};

class MultiMap
{
private:
    static const int sizeOfTable = 1007;
    vector<Map> multiMap[sizeOfTable]; 

public:
    static int generateHashCode(string &key)
    {
        int hash = 5381;
        for (int i = 0; i < key.length(); ++i)
        {
            hash = (((hash << 5) + hash) + int(key[i])) % sizeOfTable; // DJB Hash
        }
        return hash;
    }

    void get(string &key)
    {
        int hash = generateHashCode(key);

        bool existsKey = false;
        for (int i = 0; i < multiMap[hash].size(); ++i)
        {
            if (multiMap[hash][i].key == key)
            {
                cout << multiMap[hash][i].size;
                printTree(multiMap[hash][i].values);
                cout << "\n";
                existsKey = true;
                return;
            }
        }

        if (!existsKey)
        {
            cout << "0" << "\n";
        }
    }

    void put(string &key, string &value)
    {
        int index = generateHashCode(key);

        bool existsKey = false;
        for (int i = 0; i < multiMap[index].size(); ++i)
        {
            if (multiMap[index][i].key == key)
            {
                if(!exists(multiMap[index][i].values, value))
                {
                    multiMap[index][i].values = addToTree(multiMap[index][i].values, value);
                    multiMap[index][i].size += 1;
                }
                existsKey = true;
                break;
            }
        }

        if (!existsKey)
        {
            Map newNode;
            newNode.key = key;
            newNode.size = 1;
            newNode.values = addToTree(newNode.values, value);

            multiMap[index].emplace_back(newNode);
        }
    }

    void deleteKey(string &key, string &value)
    {
        int index = generateHashCode(key);

        for (int i = 0; i < multiMap[index].size(); ++i)
        {
            if (multiMap[index][i].key == key)
            {
                if(exists(multiMap[index][i].values, value))
                {
                    multiMap[index][i].values = deleteNode(multiMap[index][i].values, value);
                    multiMap[index][i].size -= 1;
                }
                break;
            }
        }
    }

    void deleteAll(string &key)
    {
        int index = generateHashCode(key);
        auto new_end = remove_if(multiMap[index].begin(), multiMap[index].end(), [&key](const Map &p)
                                 { return p.key == key; });
        multiMap[index].erase(new_end, multiMap[index].end());
    }
};

int main()
{
    freopen("multimap.in", "r", stdin);
    freopen("multimap.out", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string command, key, value;
    MultiMap multiMap;

    while (cin >> command >> key)
    {
        if (command == "put")
        {
            cin >> value;
            multiMap.put(key, value);
        }
        else if (command == "get")
            multiMap.get(key);
        else if (command == "delete")
        {
            cin >> value;
            multiMap.deleteKey(key, value);
        }
        else if (command == "deleteall")
            multiMap.deleteAll(key);
    }
}