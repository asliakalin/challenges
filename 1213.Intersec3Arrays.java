
// intersection of three sorted arrays

class Solution {
    public List<Integer> arraysIntersection(int[] arr1, int[] arr2, int[] arr3) {
        int one = 0;
        int two = 0;
        int t = 0;
        List<Integer> res = new ArrayList<Integer>();
        while ((one<arr1.length) && (two < arr2.length )&& (t < arr3.length)) {
            int biggest = java.lang.Math.max(java.lang.Math.max(arr1[one], arr2[two]), arr3[t]);
            while (arr1[one] < biggest) {
                one ++;
                if (one == arr1.length) {return res;}
            }
            while (arr2[two] < biggest) {
                two ++;
                if (two == arr2.length) {return res;}
            }
            while (arr3[t] < biggest) {
                t ++;
                if (t == arr3.length) {return res;}
            }
            if ((arr1[one] == arr2[two]) && (arr2[two] == arr3[t])) {
                res.add(arr1[one]);
                one++;
                two++;
                t++;
            }
        }
        return res;
    }
}