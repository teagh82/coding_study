#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    // 상근이가 가진 캬드 수
    int n;
    cin >> n;

    // 상근이 카드들
    vector<int> arr;
    for(int i=0; i<n; i++){
        int tmp;
        cin >> tmp;
        arr.push_back(tmp);
    }

    // 상근이가 가지고 있는지 확인할 카드 수
    int m;
    cin >> m;

    // 상근이가 가지고 있는지 확인할 카드들 
    vector<int> arr2;
    for(int i=0; i<m; i++){
        int tmp;
        cin >> tmp;

        arr2.push_back(tmp);
    }

    // 정렬
    sort(arr.begin(), arr.end());

    // 이진탐색 
    int bs(int t, vector<int> arr){
        int l = 0;
        int r = arr.size();
        while(1){
            
            mid = (l+r) / 2
        }
    }

    // 카드 가지고 있는지 확인
    vector<int> ans;
    for(int i=0; i<m; i++){
        
        if(arr2[i] < arr[arr.size()/2]){

        }


        ans.push_back(0);
        ans.push_back(1);
    }

}