#include <iostream>
#include <vector>
#include <fstream>
#include <math.h>

using namespace std;

vector<vector <int> > arrayOfNodes(200000, vector<int>(3, 0));
ifstream fileIn("check.in");
ofstream fileOut("check.out");

struct Node
{
    int value;
    Node *left;
    Node *right;
};

Node *initNode(int val)
{
    Node *node = new Node();

    node->value = val;
    node->left = nullptr;
    node->right = nullptr;

    return node;
}

Node *addToTree(Node *root, int i)
{
    if (i != -1)
    {
        if (root == nullptr)
        {
            root = initNode(arrayOfNodes[i][0]);
            root->left = addToTree(root->left, arrayOfNodes[i][1] - 1);
            root->right = addToTree(root->right, arrayOfNodes[i][2] - 1);
        }
        return root;
    }
    return nullptr;
}

bool checkIfBinaryTree(Node *root, int left, int right)
{
    if (root == nullptr)
        return true;
    
    if (root->value <= left || root->value >= right)
    {
        fileOut << "NO";
        exit(0);
    }
    return checkIfBinaryTree(root->left, left, root->value) 
        && checkIfBinaryTree(root->right, root->value, right);
}

int main()
{
    int n;
    fileIn >> n;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < 3; j++)
            fileIn >> arrayOfNodes[i][j];

    Node *tree = nullptr;

    for (int i = 0; i < n; i++)
        tree = addToTree(tree, i);

    if (checkIfBinaryTree(tree, pow(-10, 9), pow(10, 9)) || n == 0) {
        fileOut << "YES";
    }

    return 0;
}