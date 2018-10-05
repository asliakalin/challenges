package leet1;

/**
 * Created by asliakalin on 10/3/18.
 */


/**
 * Given an array of integers, return indices of the two numbers such that they add up to a specific target.
 * */
public class leet1 {
    public static void main(String[] args) {
        System.out.println("Challenge 1:");
        System.out.println("Given an array of integers, return indices of the two numbers such that they add up to a specific target.");
    }

    public static int[] twoSums(int[] nums, int t) {
        int[] indices = new int[2];
        for (int i = 0; i < nums.length-1; i++) {
            indices = new int[2];
            indices[0] = i;
            for (int j = i+1; j < nums.length; j++) {
                if (nums[i] + nums[j] == t) {
                    indices[1] = j;
                    return indices;
                }
            }

        }
        return indices;
    }

}
