#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int generateHashCode(string &val, int &constOfHashCode)
{
    int hash = 5381;
    for (int i = 0; i < val.length(); ++i) {
        hash = (((hash << 5) + hash) + int(val[i])) % constOfHashCode; // DJB hash :)))))
    }
    return hash;
}

struct Map
{
    string key;
    string value;
    Map *prev = nullptr;
    Map *next = nullptr;
};

int main()
{
    freopen("linkedmap.in", "r", stdin);
    freopen("linkedmap.out", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int constOfHashCode = 100003;
    vector<vector<Map> > hashTable(constOfHashCode);

    int index;
    string command;
    string key;
    string value;
    Map *prev = nullptr;

    while (cin >> command >> key)
    {
        index = generateHashCode(key, constOfHashCode) % constOfHashCode;
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
                if (hashTable[index].size() == 0)
                    hashTable[index].reserve(10);
                Map newValue;
                newValue.key = key;
                newValue.value = value;
                newValue.prev = prev;
                newValue.next = nullptr;
                hashTable[index].push_back(newValue);
                if(prev != NULL) 
                    prev->next = &hashTable[index][hashTable[index].size() - 1];
                prev = &hashTable[index][hashTable[index].size() - 1];
            }
        }
        else if (command == "delete")
        {
            for (int i = 0; i < hashTable[index].size(); i++)
                if (hashTable[index][i].key == key)
                {
                    if (hashTable[index][i].next == NULL) prev = hashTable[index][i].prev;
                    else hashTable[index][i].next->prev = hashTable[index][i].prev;

                    if (hashTable[index][i].prev != NULL) hashTable[index][i].prev->next = hashTable[index][i].next;
                    hashTable[index][i].value = hashTable[index][i].key = "";
                    hashTable[index][i].next = hashTable[index][i].prev = nullptr;
                    break;
                }
        }
        else if (command == "get")
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
        else if (command == "prev")
        {
            bool flagExist = false;
            for (int i = 0; i < hashTable[index].size(); i++)
                if (hashTable[index][i].key == key && hashTable[index][i].prev != nullptr)
                {
                    flagExist = true;
                    cout << hashTable[index][i].prev->value << "\n";
                    break;
                }
            if (flagExist == false) cout << "none\n";
        }
        else if (command == "next")
        {
            bool flagExist = false;
            for (int i = 0; i < hashTable[index].size(); i++)
                if (hashTable[index][i].key == key && hashTable[index][i].next != nullptr)
                {
                    flagExist = true;
                    cout << hashTable[index][i].next->value << "\n";
                    break;
                }
            if (flagExist == false) cout << "none\n";
        }
    }
}
