package twosum

import (
    "sort"
    "testing"
)

func BenchmarkTwoSum(b *testing.B) {
    for n := 2; n < b.N; n++ {
        nums := make([]int, n)
        nums[n/2] = 1
        nums[n-1] = 1
        TwoSum(nums, 2)
    }
}

func TestTwoSum(t *testing.T) {
    tests := []struct{
        name string
        nums []int
        target int
        want []int
    }{
        {
            name: "Nominal Case 1",
            nums: []int{1, 4, 6, 2, 3},
            target: 9,
            want: []int{2, 4},
        },
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got := TwoSum(tt.nums, tt.target)
            sort.Ints(got)
            if got[0] != tt.want[0] || got[1] != tt.want[1] {
                t.Errorf("GOT: %v, EXPECTED: %v\n", got, tt.want)
            }
        })
    }
}

