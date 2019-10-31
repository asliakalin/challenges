import java.util.Stack;
class Solution {
    Stack<Character> stack = new Stack<Character>();
    public boolean isValid(String s) {
        if (s == "") {return true;}
        char[] chars = s.toCharArray();
        for (int i=0; i< chars.length; i++) {
            char c = chars[i];
            if (!stack.empty()) {
                char compare = stack.peek();
                boolean match = ((compare == '(' && c == ')') || (compare == '{' && c == '}') || (compare == '[' && c == ']'))? true : false;
                if (match) {
                    stack.pop();
                } else {stack.push(c);}
            } else {
               stack.push(c);  
        }
    } return stack.empty();
    }
}


/// Runtime: 2 ms, faster than 61.12% of Java online submissions for Valid Parentheses.
/// Memory Usage: 34 MB, less than 100.00% of Java online submissions for Valid Parentheses.