#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int generateHashCode(string &val, int &constOfHashCode)
{
    long long int code = 0;
    for(int i = 0; i < val.length(); ++i)
        code += val[i] * (i + 107);
    return code % constOfHashCode;
}

struct Map
{
    string key;
    string value;
};

int main()
{
    freopen("map.in", "r", stdin);
    freopen("map.out", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);


    int constOfHashCode = 1000003;
    vector<vector<Map> > hashTable(constOfHashCode);

    int index;
    string command;
    string key;
    string value;

    while (cin >> command >> key)
    {
        index = abs(generateHashCode(key, constOfHashCode));
        if (command == "put")
        {
            cin >> value;
            bool flagExist = false;
            for (int i = 0; i < hashTable[index].size(); i++)
                if (hashTable[index][i].key == key)
                {
                    flagExist = true;
                    hashTable[index][i].value = value;
                    break;
                }
            if (flagExist == false)
            {
                Map newValue;
                newValue.key = key;
                newValue.value = value;
                hashTable[index].push_back(newValue);
            }
        }
        else if (command == "delete")
        {
            for (int i = 0; i < hashTable[index].size(); i++)
                if (hashTable[index][i].key == key)
                {
                    hashTable[index].erase(hashTable[index].begin() + i);
                    break;
                }
        }
        else // "get"
        {
            bool flagExist = false;
            for (int i = 0; i < hashTable[index].size(); i++)
                if (hashTable[index][i].key == key)
                {
                    flagExist = true;
                    cout << hashTable[index][i].value << "\n";
                    break;
                }
            if (flagExist == false) cout << "none\n";
        }
    }
}

