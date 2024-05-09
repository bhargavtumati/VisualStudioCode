/*Gram and the string
In a picturesque village, Gram, the revered elder, received a magical string named "s." The village, filled with avid letter collectors, eagerly anticipated Gram's ingenuity. With a quest to create a unique and lexicographically ordered sequence, Gram carefully crafted an algorithm. Duplicates vanished, and the string transformed into a captivating tale of linguistic elegance.

The village celebrated Gram as the guardian of lexicographical order, and the magical string "s" became a symbol of their commitment to precision. The story resonated through the hills, inspiring generations to unravel the mysteries of letters and strings.

Input:
A string s of length between 1 and 10,000.

Output:
Return the smallest lexicographical order string after removing duplicates.

Example 1:
Input:

s = "bcabc"

Output:
"abc"

Example2:
Input:
s = "cbacdcbc"

Output:
"acdb"

Constraints:
The length of the input string s is within the range [1, 10,000].
The string s consists of lowercase English letters.*/
#include <iostream>


using namespace std;
class removeDuplicateLetters {
    public:
        string Solution (string s) {
        
        int cnt[26] = {0};
        int vis[26] = {0};
        int n = s.size();
    
        for (int i = 0; i < n; i++){
            cnt[s[i] - 'a']++;
cout<< s[i]-'a'<<" "<<s[i]<<"\n";
        }
    
        string res = "";
        for (int i = 0; i < n; i++) {
            cnt[s[i] - 'a']--;
            if (!vis[s[i] - 'a']) {
                while (res.size() > 0 && res.back() > s[i] && cnt[res.back() - 'a'] > 0) {
                    vis[res.back() - 'a'] = 0;
                    res.pop_back();
                }
                res += s[i];
                vis[s[i] - 'a'] = 1;
            }
        }
    
        return res;
    }
         
    };
    int main(){
        removeDuplicateLetters cp;
        cout << cp.Solution("cabc");
    }
