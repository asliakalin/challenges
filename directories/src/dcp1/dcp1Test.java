package dcp1;

import org.junit.*;
import org.junit.Assert;

/**
 * Created by asliakalin on 10/3/18.
 */
public class dcp1Test {

    @Test
    public void testOneThing() {
        int[] test1 = {10, 15, 3, 7};
        int target = 17;
        boolean result = dcp1.sumsK(test1, target);
        boolean expectedResult = true;
        Assert.assertEquals("Running the 1st test", expectedResult, result);
    }
}