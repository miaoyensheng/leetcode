// Given an array of integers, return indices of two numbers that they add up to specific target

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.lang.IllegalArgumentException;

public class twoSum{

    int[] input_array;
    int target;

    twoSum(int[] input_array, int target){
        this.input_array = input_array;
        this.target = target;
    }

    public static void main(String arg[]){
        int[] input_array = {2, 7, 11, 15};
        twoSum ts = new twoSum(input_array, 9);
        System.out.println(Arrays.toString(ts.performTwoSum1()));
        System.out.println(Arrays.toString(ts.performTwoSum2()));
        System.out.println(Arrays.toString(ts.performTwoSum3()));
    }

    // Brute force
    int[] performTwoSum1(){

        for(int i = 0; i < input_array.length; i++){
            for(int j = i+1; j < input_array.length; j++){
                if((target-input_array[i]) == input_array[j]){
                    return new int[] {i, j};
                }
            }
        }

        throw new IllegalArgumentException("no solution");

    }

    int[] performTwoSum2(){

        Map<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < input_array.length; i++){
            map.put(input_array[i], i);
        }

        for(int i = 0; i < input_array.length; i++){
            int complement = target-input_array[i];
            if(map.containsKey(complement) && map.get(complement) != i){
                return new int[] {i, map.get(complement)};
            }
        }

        throw new IllegalArgumentException("no solution");
    }

    int[] performTwoSum3(){

        Map<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < input_array.length; i++){
            int complement = target-input_array[i];
            if(map.containsKey(complement)){
                return new int[] {map.get(complement), i};
            }
            map.put(input_array[i], i);
        }

        throw new IllegalArgumentException("no solution");
    }
}
