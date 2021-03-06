class Solution {
    public int lengthOfLongestSubstring(String s) {
//         int[] chars = new int[128];
        
//         int left = 0;
//         int right = 0;
        
//         int res = 0;
//         while (right < s.length()) {
//             char s = s.charAt(right);
//             chars[r]++;
            
//             while (chars[r] > 1) {
//                 char l = s.charAt(left);
//                 chars[l]--;
//                 left++;
//             }
            
//             res = Math.max(res, right - left + 1);
            
//             right++;
//         }
//         return res;
        
        int n = s.length(), ans = 0;
        Map<Character, Integer> map = new HashMap<>();
        
        for (int j = 0, i = 0; j<n; j++){
            if (map.containsKey(s.charAt(j))) {
                i = Math.max(map.get(s.charAt(j)), i);
            }
            ans = Math.max(ans, j - i + 1);
            map.put(s.charAt(j), j + 1);
        }
        return ans;
    }
}