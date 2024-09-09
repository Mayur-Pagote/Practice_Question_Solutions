class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {

        var length = nums.count // Variable length will store length of nums
        var index_list: [Int] = [] // Declaring empty array

        // This loop will help in comparing and appending index
        for i in 0..<length{
            for j in i+1..<length{
                if (nums[i]+nums[j] == target){
                    index_list.append(i)
                    index_list.append(j)
                }
            }
        }
        return index_list
    }
}
