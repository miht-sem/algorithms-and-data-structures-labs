#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int constOfHashCode = 1000003;

int generateHashCode(int num)
{
    return num % constOfHashCode;
}

int main()
{

    ifstream fileIn("set.in");
    ofstream fileOut("set.out");

    vector<vector<int> > hashTable(constOfHashCode);

    string command;
    int x;
    int key;

    while (fileIn >> command >> x)
    {
        key = generateHashCode(abs(x));
        if (command == "insert")
        {
            bool flagExist = false;
            for (int i = 0; i < hashTable[key].size(); i++)
                if (hashTable[key][i] == x)
                {
                    flagExist = true;
                    break;
                }
            if (flagExist == false) hashTable[key].push_back(x);
        }
        else if (command == "delete")
        {
            for (int i = 0; i < hashTable[key].size(); i++)
                if (hashTable[key][i] == x)
                {
                    hashTable[key].erase(hashTable[key].begin() + i);
                    break;
                }
        }
        else if (command == "exists")
        {
            bool flagExist = false;
            for (int i = 0; i < hashTable[key].size(); i++)

                if (hashTable[key][i] == x)
                {
                    flagExist = true;
                    break;
                }

            if (flagExist == true) fileOut << "true\n";
            else fileOut << "false\n";
        }
    }
    fileIn.close();
    fileOut.close();
}