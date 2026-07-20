class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
        isAnagram(s: string, t: string): boolean {
        if (s.length !== t.length) {
            return false;
        }
        
        let sMap = new Map<string, number>();
        for (let i = 0; i < s.length; i++) {
            sMap.set(s[i], (sMap.get(s[i]) || 0) + 1);
        }
        for (let j = 0; j < t.length; j++) {
            sMap.set(t[j], (sMap.get(t[j]) || 0) - 1);
        }
        for (let value of sMap.values()) {
            if (value !== 0) {
                return false;
            }
        }
        return true;
    }
}
