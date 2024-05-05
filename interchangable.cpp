/*Number of Pairs of Interchangeable Rectangles
Medium
Topics
Companies
Hint
You are given n rectangles represented by a 0-indexed 2D integer array rectangles, where rectangles[i] = [widthi, heighti] denotes the width and height of the 
*/
#include <bits/stdc++.h>
using namespace std;

class interchangable {
public:
    int interchangeableRectangles(vector<vector<int>>& rectangles) {
        int counts = 0;
        unordered_map<double, int> st;

        for (const vector<int>& rect : rectangles) {
            double ratio = static_cast<double>(rect[0]) / rect[1];
            if (st.find(ratio) == st.end()) {
                st[ratio] = 0;
            } else {
                counts += st[ratio] + 1;
                st[ratio]++;
            }
        }

        return counts;
    }
};

int main() {
    // Example usage:
    interchangable sol;
    vector<vector<int>> rectangles = {{4, 8}, {3, 6}, {10, 20}, {15, 30}};
    cout << "Interchangeable pairs: " << sol.interchangeableRectangles(rectangles) << endl;
    return 0;
}
