#include <iostream>
#include <vector>

using namespace std;

class Ships {
public:
    int shipWithinDays(vector<int>& weights, int days) {
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
    Ships sh1;
    cout << "Example 1: " << sh1.shipWithinDays(weights1, days1) << endl;

    vector<int> weights2 = {3, 2, 2, 4, 1, 4};
    int days2 = 3;
    Ships sh2;
    cout << "Example 2: " << sh2.shipWithinDays(weights2, days2) << endl;

    vector<int> weights3 = {1, 2, 3, 1, 1};
    int days3 = 4;
    Ships sh3;
    cout << "Example 3: " << sh3.shipWithinDays(weights3, days3) << endl;

    return 0;
}
