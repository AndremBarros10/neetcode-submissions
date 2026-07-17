class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        let duplicateSet = new Set<number>();
        
        for (let num of nums) {
            if (duplicateSet.has(num)) {
                return true;
            }
            duplicateSet.add(num);
        }
        return false;
    }
}
