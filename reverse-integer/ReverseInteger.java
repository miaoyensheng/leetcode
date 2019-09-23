class ReverseInteger{

    public static void main(String args[]){
        System.out.println(reverse(-123));
    }

    public static int reverse(int x) {
        
        int num = Math.abs(x);
        int rev = 0;
        
        while(num > 0){
            int mod = num%10;
            rev = rev*10 + mod;
            num = num/10;
        }

        if(x < 0){
            return rev*-1;
        }else{
            return rev;
        }

    }

}