package leet1;
import org.junit.*;
import org.junit.Assert;

/**
 * Created by asliakalin on 10/3/18.
 */
public class leet1Test {

    @Test
    public void testOneThing() {
        int[] test1 = {1,2,3,4,5,6};
        int target = 8;
        int[] result = leet1.twoSums(test1, target);
        int [] expectedResult = {1,5};
        Assert.assertArrayEquals("Running the 1st test",expectedResult, result);
    }

    @Test
    public void testAnotherThing() {
        int[] test1 = {2,7,13,24,5,1};
        int target = 6;
        int[] result = leet1.twoSums(test1, target);
        int [] expectedResult = {4,5};
        Assert.assertArrayEquals("Running the 2nd test.",expectedResult, result);
    }


}
