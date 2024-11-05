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
