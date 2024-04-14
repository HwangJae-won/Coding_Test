#include <vector>
#include <iostream>
//연속된 숫자가 나오면 없애기 : 집합은 사용할 수 없음 

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    
    for (int i = 0; i < arr.size(); ++i) { //0부터 arr 배열까지 1씩 증가시키면서 반복문 수행 
        if (i == 0 || arr[i] != arr[i - 1]) { // 현재 숫자가 이전 숫자와 다른 경우에만 추가 , i=0은 이전 요소가 없어서 다룰 수 없으니까 
            answer.push_back(arr[i]); //파이썬 append 
        }
    }

    return answer;
}