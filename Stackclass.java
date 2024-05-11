import java.util.*;
class Stackclass{
    public static void main(String args[]){
        Stack<Integer> st =new Stack<>();
       st.push(23);//0
       st.push(6);//1
       st.push(0);//2
       st.push(80);//3

       System.out.println("removed this element:  "+st.pop());

///inbuilt but can be built by yourself..

       System.out.println("The first element is: " + st.firstElement());

       System.out.println("view this last inserted element:  "+st.peek());

       int removedElement = st.remove(0);
        System.out.println("Removed element: " + removedElement);

        int targetValue=6;
        for (int i = 0; i < st.size(); i++) {
         if (st.get(i) == targetValue) {
             // Remove the element at index i
             
             System.out.println("Removed element: " + st.remove(i));
             break; // Stop iterating after removal
         }
        }

        int newElement =90, targetIndex =0;
        st.insertElementAt(newElement, targetIndex);

       Iterator<Integer> value = st.iterator();
       System.out.println("stack values are: ");
       while(value.hasNext()){
        
           System.out.print(value.next()+" ");
       }
      
    
    }
       
    }
