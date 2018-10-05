package dcp1;
import java.util.Arrays;
/**
 * Created by asliakalin on 10/3/18.
 */


/**
 *  Given an array of numbers, return whether any two sums to K.
 For example, given [10, 15, 3, 7] and K of 17, return true since 10 + 7 is 17.
 * */
public class dcp1 {
    public static void main(String[] args) {
        System.out.println("Given an array of numbers, return whether any two sums to K");
    }

    public static boolean sumsK(int[] nums, int t) {
        if (t == 0) {
            return true;
        } else if ((nums == null) & (t != 0)) {
            return false;
        } else if (nums == null) {
            return true;
        } else {
            int[] newArray;
            if (nums.length != 1) {
                newArray = Arrays.copyOfRange(nums, 1, nums.length);
            } else {
                newArray = null;
            }
            return sumsK(newArray, t) || sumsK(newArray, t-nums[0]);
        }
    }

}
