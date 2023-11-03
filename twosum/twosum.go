package twosum

/*
// Reference O(n^2) runtime implementation
func TwoSum(nums []int, target int) []int {
    for i := 0; i < len(nums); i++ {
        for j := i+1; j < len(nums); j++ {
            if nums[i] + nums[j] == target {
                return []int{i, j}
            }
        }
    }
    return []int{-1, -1}
}
*/

// Reference O(n) runtime implementation
func TwoSum(nums []int, target int) []int {
    indices := make(map[int]int)
    for i, n := range nums {
        if v, ok := indices[target-n]; ok {
            return []int{v, i}
        }
        indices[n] = i
    }
    return []int{-1, -1}
}
