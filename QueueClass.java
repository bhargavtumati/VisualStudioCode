import java.util.Queue;
import java.util.LinkedList;
import java.util.Iterator;
class QueueClass{
    public static void main(String args[]){
Queue<Integer> qu =new LinkedList<>();
Queue<Integer> qu2 =new LinkedList<>();
qu.add(4);
qu.add(9);
qu.add(10);
qu.add(80);

System.out.println("returns first element for queue  "+qu.peek());

System.out.println("removes the first element  "+qu.poll());


Iterator<Integer> value = qu.iterator();
System.out.println("queue elements: ");
while(value.hasNext()){
    System.out.print(value.next()+" ");
}
qu2.addAll(qu);//add elements of qu to qu2
qu.clear();//clears all elements;
    }
}