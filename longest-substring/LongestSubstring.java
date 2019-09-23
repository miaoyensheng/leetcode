import java.util.HashMap;


// longest substring without repeating characters

class LongestSubstring{


    public static void main(String agrs[]){

        System.out.println(performLongestSubstring("bbbb"));

    }

    static int performLongestSubstring(String str){

        int strLength = str.length();
        int longest = 0, start = 0, end = 0;
        Set<Character> set = new HashSet<>();

        while(start < strLength & end < strLength){

            if(!set.contains(str.charAt(end))){

                set.add(str.charAt(end++));
                longest = Math.max(longest, end-start);
                
            }else{

                set.remove(str.charAt(start++));

            }
        }

        return longest;

        int ans = 0, n = str.length();

        Map<Character, Integer> map = new HashMap<>();

        for(int i = 0, j = 0; j < n; j++){

            if(map.contains(str.charAt(j))){
                i = Math.max(map.get(str.charAt(j)), i);
            }
            ans = Math.max(ans, j-i+1);            
            map.put(str.charAt(j), j+1);
        }

        return ans;
    }

}