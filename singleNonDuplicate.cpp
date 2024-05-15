#include <iostream>
#include <vector>
using namespace std;

class singleNonDuplicate {
public:
    int Solution(vector<int>& nums) {
        int uni=nums[0];
if(nums.size()==1)
return uni;
else{
for(int i=0;i<nums.size();i++){
            if(nums[i]==nums[i+1])
            i+=1;
            else if(i>=1&&nums[i]==nums[i-1])
                i++;
            
            else{
            uni=nums[i];
            break;
}

        }
}
return uni;
        
    }
};
int main()
{
    vector<int> ve={1,2,2,3,3};
    singleNonDuplicate ch;
    cout << ch.Solution(ve); 
    
}