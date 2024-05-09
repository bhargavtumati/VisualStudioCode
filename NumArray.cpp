#include <iostream>
#include <vector>
using namespace std;

class NumArray {
private:
    vector<int> tree; // Segment tree
    int n; // Size of the input array

    // Build the segment tree
    void buildTree(vector<int>& nums) {
        for (int i = n; i < 2 * n; ++i) {
            tree[i] = nums[i - n];
        }
        for (int i = n - 1; i > 0; --i) {
            tree[i] = tree[2 * i] + tree[2 * i + 1];
        }
    }

public:
    NumArray(vector<int>& nums) {
        n = nums.size();
        tree.resize(2 * n);
        buildTree(nums);
    }

    void update(int index, int val) {
        index += n;
        tree[index] = val;
        while (index > 1) {
            index /= 2;
            tree[index] = tree[2 * index] + tree[2 * index + 1];
        }
    }

    int sumRange(int left, int right) {
        left += n;
        right += n;
        int sum = 0;
        while (left <= right) {
            if (left % 2 == 1) {
                sum += tree[left];
                ++left;
            }
            if (right % 2 == 0) {
                sum += tree[right];
                --right;
            }
            left /= 2;
            right /= 2;
        }
        return sum;
    }
};

int main() {
    vector<int> nums = {1, 3, 5};
    NumArray numArray(nums);
    cout << numArray.sumRange(0, 2) << endl; // Returns 9
    numArray.update(1, 2); // nums = [1, 2, 5]
    cout << numArray.sumRange(0, 2) << endl; // Returns 8
    return 0;
}
