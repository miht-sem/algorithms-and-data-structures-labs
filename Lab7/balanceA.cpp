#include <iostream>
#include <vector>

using namespace std;


int main()
{
    freopen("balance.in", "r", stdin);
    freopen("balance.out", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    vector< vector<int> > tree;
    vector< int > indexes;

    cin >> n; 
    tree.resize(n + 1, vector<int>(5, 0));

    // 0 - value
    // 1 - left children
    // 2 - right children
    // 3 - balance 
    // 4 - height

    for (int i = 1; i < n + 1; i++)
        for (int j = 0; j < 3; j++)
            cin >> tree[i][j];

    for (int i = n; i > 0; i--)
    {
        if (tree[i][1] == 0 && tree[i][2] == 0)
        {
            tree[i][3] = 0;
            tree[i][4] = 0;
        }
        else if (tree[i][1] == 0)
        {
            tree[i][3] = tree[tree[i][2]][4] + 1;
            tree[i][4] = tree[tree[i][2]][4] + 1;
        }
        else if (tree[i][2] == 0)
        {
            tree[i][3] = -tree[tree[i][1]][4] - 1;
            tree[i][4] = tree[tree[i][1]][4] + 1;
        }
        else
        {
            tree[i][3] = tree[tree[i][2]][4] - tree[tree[i][1]][4];
            tree[i][4] = max(tree[tree[i][2]][4], tree[tree[i][1]][4]) + 1;
        }
    }

    for (int i = 1; i < n + 1; ++i)
    {
        cout << tree[i][3] << '\n';
    }

    return 0;
}