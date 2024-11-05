class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result;
        int i=0,j=0; // Initialize two pointer i for word1 and j for word2
        while(i < word1.size() || j < word2.size()) // loop until the word size
        {
            if(i < word1.size()) // condition check and add the item into the result
            {
                result +=word1[i++];
            }
            if(j < word2.size())
            {
                result +=word2[j++];
            }
        }

        return result;

        
    }
};


// Full C++ Code 


#include <iostream>
#include <string>
using namespace std;
int main()
{
    string word1="1234";
    string word2="5678";
    string result;
    int i=0;
    while(i < word1.size() || i < word2.size())
    {
        if(i < word1.size())
        {
            result +=word1[i];

        }
        if(i < word2.size())
        {
            result +=word2[i];
        }
        i++;
    }
    cout<< "The merged alternative is "<<result;
}
