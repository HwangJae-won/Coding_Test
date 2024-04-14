#include <vector>
#include <unordered_set> //집합 STL

using namespace std;

int solution(vector<int> nums) {
    int max_species = nums.size() / 2; // 선택하려는 수 
    unordered_set<int> species_set(nums.begin(), nums.end()); // 집합, nums의 모든 요소 포함
    int unique_species = species_set.size(); // 중복 제거된 종류의 폰켓몬 수

    // N/2 보다 작은 종류의 폰켓몬이 있다면, 그 종류의 수가 답이 됨
    if (unique_species <= max_species) {
        return unique_species;
    }
    // N/2 보다 큰 종류의 폰켓몬이 있다면, 최대값은 N/2 이므로 답은 N/2가 됨
    else {
        return max_species;
    }
}