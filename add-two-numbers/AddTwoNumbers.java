import java.util.LinkedList;
import java.lang.Math;


class AddTwoNumbers{
 
    public static void main(String agrs[]){

        LinkedList<Integer> ll1 = new LinkedList<>();
        LinkedList<Integer> ll2 = new LinkedList<>();

        ll1.add(2);
        ll1.add(4);
        ll1.add(5);
        ll1.add(null);

        ll2.add(5);
        ll2.add(6);
        ll2.add(4);

        System.out.println(ll1.get(3) == null);

    }

    LinkedList<Integer> performAddTwoNumbers(LinkedList<Integer> ll1, LinkedList<Integer> ll2){
    
        int maxSize = Math.max(ll1.size(), ll2.size());


        for(int i = 0; i < maxSize; i++){
            try{
                ll1.get(i);
            }

        }





        int carry;



        return null;
    }
}