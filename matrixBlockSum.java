
class matrixBlockSum  {
    public int[][] Solution (int[][] mat, int k) {
        int[][] result=new int[mat.length][mat[0].length];
       for(int i=0;i<mat.length;i++){
        for(int j=0;j<mat[0].length;j++){
            int rs=Integer.max(0,i-k);
            int re=Integer.min(mat.length-1,i+k);
            int cs=Integer.max(0,j-k);
            int ce=Integer.min(mat[0].length-1,j+k);
            int sum=0;
for(int l=rs;l<=re;l++){
    for(int m=cs;m<=ce;m++){
       sum+=mat[l][m];
    }
}
result[i][j]=sum;
System.out.print(result[i][j]+" ");
        }
        System.out.println();
       }
       return result;
    }
    public static void main(String args[]){
        int[][] mat={{1,2,3},{4,5,6},{7,8,9}};
        int k=1;
        matrixBlockSum m = new matrixBlockSum();
       m.Solution(mat, k);
    }
}