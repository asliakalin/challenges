package dcp2;

import org.junit.*;
import org.junit.Assert;

/**
 * Created by asliakalin on 10/3/18.
 */
public class dcp2Test {

    @Test
    public void testOneInput() {
        int[] test1 = {1,2,3,4,5};
        int[] result = dcp2.productI(test1);
        int[] expectedResult = {120,60,40,30,24};
        Assert.assertArrayEquals("Running the 1st test", expectedResult, result);
    }

    @Test
    public void testSecondInput() {
        int[] test1 = {3,2,1};
        int[] result = dcp2.productI(test1);
        int[] expectedResult = {2,3,6};
        Assert.assertArrayEquals("Running the 1st test", expectedResult, result);
    }
}
