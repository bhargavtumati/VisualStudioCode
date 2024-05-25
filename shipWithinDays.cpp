#include <iostream>
#include <vector>

using namespace std;

class shipWithinDays {
public:
    int Solution(vector<int>& weights, int days) {
        int start = 0, end = 0;
        for (int weight : weights) {
            start = max(start, weight);
            end += weight;
        }

        while (start < end) {
            int mid = start + (end - start) / 2;
            int currWeight = 0, currDays = 1;

            for (int weight : weights) {
                if (currWeight + weight <= mid) {
                    currWeight += weight;
                } else {
                    currWeight = weight;
                    currDays++;
                }
            }

            if (currDays > days) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }

        return end;
    }
};

int main() {
    vector<int> weights1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int days1 = 5;
    shipWithinDays sh1;
    cout << "Example 1: " << sh1.Solution(weights1, days1) << endl;

    vector<int> weights2 = {3, 2, 2, 4, 1, 4};
    int days2 = 3;
    shipWithinDays sh2;
    cout << "Example 2: " << sh2.Solution(weights2, days2) << endl;

    vector<int> weights3 = {1, 2, 3, 1, 1};
    int days3 = 4;
    shipWithinDays sh3;
    cout << "Example 3: " << sh3.Solution(weights3, days3) << endl;

    return 0;
}
