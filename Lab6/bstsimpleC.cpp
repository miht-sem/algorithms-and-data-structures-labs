#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

ifstream fileIn("bstsimple.in");
ofstream fileOut("bstsimple.out");

struct Node
{
    int value;
    Node *left;
    Node *right;
};

Node *addToTree(Node *root, int num)
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

bool exists(Node *root, int x)
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

Node *next(Node *root, int x, Node *ans)
{
    if (root == nullptr)
    {
        return ans;
    }
    if (x < root->value)
    {
        ans = root;
        return next(root->left, x, ans);
    }
    else
    {
        return next(root->right, x, ans);
    }
}

Node *prev(Node *root, int x, Node *ans)
{
    if (root == nullptr)
    {
        return ans;
    }
    if (x > root->value)
    {
        ans = root;
        return prev(root->right, x, ans);
    }
    else
    {
        return prev(root->left, x, ans);
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

Node *deleteNode(Node *root, int x)
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

int main()
{
    Node *tree = nullptr;

    while (fileIn)
    {
        string comand;
        int x;
        fileIn >> comand >> x;

        tree = (comand == "insert" ? addToTree(tree, x) : tree);
        tree = (comand == "delete" ? deleteNode(tree, x) : tree);

        if (comand == "exists")
        {
            fileOut << (exists(tree, x) ? "true\n" : "false\n");
        }
        else if (comand == "next")
        {
            Node *node = next(tree, x, nullptr);
            fileOut << (node == nullptr ? "none\n" : to_string(node->value) + "\n");
        }
        else if (comand == "prev")
        {
            Node *node = prev(tree, x, nullptr);
            fileOut << (node == nullptr ? "none\n" : to_string(node->value) + "\n");
        }
    }

    return 0;
}