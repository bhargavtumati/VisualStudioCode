
#include <bits/stdc++.h>
using namespace std;

class stoneGameII  {
public:
    int dp[101][201];
    int help(int i,int M,vector<int>&piles){// gets difference of no of stones alice and bob playing optimally(best case) 
        if(i>=piles.size())// return 0 if null
        return 0;
        if(dp[i][M]!=-1)
        return dp[i][M];
        int tot=0;
        int ans=INT_MIN;
        for(int j=0;j<2*M;j++){
            if(i+j<piles.size())
            tot+=piles[i+j];
            ans=max(ans,tot-help(i+j+1,max(M,j+1),piles));//max of ans,tot picked-opponents total picked,
        }
        
        return dp[i][M]=ans;
    }
    int Solution(vector<int>& piles) {
        int sum=0;
        memset(dp,-1,sizeof dp); //memset() copies the value static_cast<unsigned char>(val) into each of the first num characters of the object pointed to by obj.
        for(auto a:piles)
        sum+=a;   //caluculating sum
        int diff=help(0,1,piles); //0 is start , 1 is max piles can be taken, piles.
        cout<<diff<<endl;//alice get 10 and bob gets 16 so diff =-6 
        return (sum+diff)/2;// 26-6/2==10 i.e no of stones alice gets

    }
};
int  main(){
    vector<int> ch={2,7,9,4,4};
    stoneGameII j;
    cout<<j.Solution(ch);

}