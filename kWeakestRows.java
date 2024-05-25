import java.util.*;
class kWeakestRows {
    public int[] Solution(int[][] mat, int k) {
        int matl[]=new int[k],count=0;
        ArrayList<Integer> al=new ArrayList<>();
        ArrayList<Integer> al2=new ArrayList<>();
        for (int i=0;i<mat.length;i++){
            count=0;
            for(int j=0;j<mat[0].length;j++){
                if(mat[i][j]==1)
                    count++; 
            }
            al.add(count);
            
        }
        al2.addAll(al);
        int h=0;
        Collections.sort(al2);
       for(int c:al2){
        for(int i=0;i<al.size();i++){
            if(c==al.get(i)&&h<k){
                
            matl[h++]=i;
            break;
            }
        }
       }
        return matl;
    }
    public static void main(String args[]){
kWeakestRows as=new kWeakestRows();
int[][] fh = {{1, 0}, {1, 0}, {1, 0}, {1, 1}}; 

int[] ch=as.Solution(fh, 4);
 
for(int c:ch){
System.out.print(c+" ");
}
    }
}