import java.util.*;
class findAndReplacePattern {
   public List<String> Solution (List<String> li, String pattern) {
   List<String> result = new ArrayList<>();

   for(String word:li){
       if(matches(word,pattern)){
           result.add(word);
       }
   }
   return result;
   }
   private boolean matches(String word, String pattern){
       char[] patternToWord = new char[26];
       char[] wordToPattern = new char[26];

       for(int index =0;index<word.length();index++){
           char wordChar = word.charAt(index);
           char patternChar = pattern.charAt(index);

           if(patternToWord[patternChar - 'a']==0){
               patternToWord[patternChar-'a']=wordChar;
           }
           if(wordToPattern[wordChar-'a']==0){
               wordToPattern[wordChar-'a']=patternChar;
           }
           if(patternToWord[patternChar - 'a']!=wordChar || wordToPattern[wordChar - 'a'] != patternChar){
               return false;
           }
           

       }
       return true;
   }
   public static void main(String args[]){
      String[] hm = {"abc","deq","mee","aqq","dkd","ccc"};
      List<String> li = new ArrayList<>();
      for(String s: hm){
         li.add(s);

      }
      String word = "abb";
      findAndReplacePattern f = new findAndReplacePattern();
      System.out.println(f.Solution(li,word));


   }
}