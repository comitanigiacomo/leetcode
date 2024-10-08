class Solution {
    public int minSwaps(String s) {
        int balance = 0;
        int max_imbalance = 0;
        for (int i = 0;  i < s.length(); i++){
            if (s.charAt(i) == ']') {
                balance--;
            }else{
                balance++;
            }
            if (balance < 0){
                max_imbalance = Math.max(max_imbalance, -balance);
            }
        }
        return (max_imbalance + 1)/2;
    }
}