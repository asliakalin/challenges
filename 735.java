class Solution {
    int[] curr; 
    int size;
    int index;
    public int[] asteroidCollision(int[] asteroids) {
        curr = new int[asteroids.length];
        size = 0;
        index = 0;
        if (asteroids==null) {return curr;}
        if (asteroids.length == 1) {
            curr[0] = asteroids[0];
        } else {
            while (index <= asteroids.length-1) {
                curr[size] = asteroids[index];
                boolean neg = asteroids[index] < 0;
                while ((size>0) && neg && (curr[size-1]>0)) {
                    if (curr[size-1] + curr[size] > 0) {
                        curr[size] = 0;
                        neg = !neg;
                        size -= 1;
                    } else if (curr[size-1] + curr[size] < 0) {
                        curr[size-1] = curr[size];
                        curr[size]= 0;
                        size -=1;
                    } else {
                        curr[size-1] = 0;
                        curr[size]= 0;
                        size -= 2;
                        neg = !neg;
                    }
                }
                
                index += 1;
                size +=1;
                   
            }
            
        }
        if (size <= 0) {return new int[0];}
        curr = Arrays.copyOfRange(curr, 0, size);
        return curr;
    } 
}


/// Runtime: 2 ms, faster than 99.17% of Java online submissions for Asteroid Collision.
/// Memory Usage: 40 MB, less than 92.86% of Java online submissions for Asteroid Collision.



