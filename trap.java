class trap {
    public int Solution(int[] height) {
        int trap=0;
        for(int i=0;i<height.length;i++){
            
            int yet=height[i];
            for(int j=i;j<height.length;j++){
                if(height[j]<yet){
                    trap+=yet-height[j];
                }
            }    
                
          
        }
         
        return trap;
    }
}