#include <bits/stdc++.h>
using namespace std;

class  countPoints{
public:
    std::vector<int> Solution(std::vector<std::vector<int>>& points, std::vector<std::vector<int>>& queries) {

        std::vector<std::array<int, 2>> pts;
        for(int i = 0; i < points.size(); i++)
        {
            pts.push_back({points[i][0], points[i][1]});
        }
        std::sort(pts.begin(), pts.end());

        int n = queries.size();
        std::vector<int> res(n);
        for(int i = 0; i < n; i++)
        {
            int x = queries[i][0];
            int y = queries[i][1];
            int r = queries[i][2];
            auto it = std::lower_bound(pts.begin(), pts.end(), std::array<int, 2>({x - r, 0}));

            for(; it != pts.end() && (*it)[0] <= x + r; it++) {
                int dx = (*it)[0] - x;
                int dy = (*it)[1] - y;
                if(dx * dx + dy * dy <= r * r)
                {
                    res[i]++;
                }
            }
        }
        return res;
    }
};
    int main(){
    vector<vector<int>> quieries={{2,3,1},{4,3,1},{1,1,2}};
    vector<vector<int>> points={{1,3},{3,3},{5,3},{2,2}};
    countPoints c ;
    vector<int> noofp=c.Solution(points,quieries);
    for(int c:noofp)
    cout<< c<<" ";
    
    }

