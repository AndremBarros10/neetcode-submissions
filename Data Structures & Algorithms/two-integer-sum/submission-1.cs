public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int,int> prevDict = new Dictionary<int, int>();

        for(int i = 0; i < nums.Length; i++){
            int diff = target - nums[i];
            if(prevDict.ContainsKey(diff)){
                return new int[] { prevDict[diff], i };
            }
            prevDict[nums[i]] = i;
        }
        return new int[0];
    }
}
