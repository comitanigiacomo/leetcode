import java.util.ArrayList;
import java.util.Stack;

class Solution {
    public int minLength(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++){
            char lettera = s.charAt(i);
            if (stack.size() > 0){
                char last = stack.peek();
                if ((last == 'A' && lettera == 'B') || (last == 'C' && lettera == 'D')){
                    stack.pop();
                }else{
                    stack.push(lettera);
                }
            }else{
                stack.push(lettera);
            }
        }
        return stack.size();
    }
}
