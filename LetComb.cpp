#include <iostream>
#include <vector>
using namespace std;

class LetComb {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        
        vector<string> mapping = {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> result;
        result.push_back(""); // Start with an empty string in the result
        
        for (char digit : digits) {
            vector<string> temp;
            for (string combination : result) {
                for (char letter : mapping[digit - '0']) {
                    temp.push_back(combination + letter);
                }
            }
            result.swap(temp); // Update the result with the new combinations

        }
        
        return result;
    }
};

int main() {
    LetComb lc;
    vector<string> combinations = lc.letterCombinations("23");
    cout << "Letter combinations for \"23\":\n";
    for (const string& combo : combinations) {
        cout << combo << " ";
    }
    cout << endl;
    return 0;
}