#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

vector<vector <int> > arrayOfNodes(200000, vector<int>(3, 0));

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

int heightOfTree(Node *root)
{
    if (root == nullptr) return 0;
    return max(heightOfTree(root->left), heightOfTree(root->right)) + 1;
}

int main()
{
    ifstream fileIn("height.in");
    ofstream fileOut("height.out");

    int n;
    fileIn >> n;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < 3; j++)
            fileIn >> arrayOfNodes[i][j];

    Node *tree = nullptr;

    for (int i = 0; i < n; i++)
        tree = addToTree(tree, i);

    fileOut << heightOfTree(tree);
    return 0;
}