import java.util.*;

class RegularExMat {
    int sl, pl; // Lengths of string s and pattern p

    // Recursive function to check if there is a match between s and p
    public boolean isMatch(int si, int pi, String s, String p, int[][] dp) {
        // If both strings have been exhausted, return true
        if (si >= sl && pi >= pl)
            return true;

        // If pattern is exhausted but string is not, return false
        if (si < sl && pi >= pl)
            return false;

        // If string is exhausted but pattern still has elements
        if (si >= sl && pi < pl) {
            // If remaining pattern consists of only '*' characters, return true
            pi++;
            while (pi < pl) {
                if (p.charAt(pi) != '*') return false;
                pi += 2;
            }
            if (p.charAt(pl - 1) != '*') return false;
            return true;
        }

        // If the result for current state (si, pi) is already computed, return it
        if (dp[si][pi] != -1)
            return dp[si][pi] == 1;

        // If the next character in pattern is '*', handle it
        if (pi < pl - 1 && p.charAt(pi + 1) == '*') {
            // Case 1: Don't use the '*' character
            boolean notUse = isMatch(si, pi + 2, s, p, dp);
            // Case 2: Use the '*' character
            boolean use = (s.charAt(si) == p.charAt(pi) || p.charAt(pi) == '.') && isMatch(si + 1, pi, s, p, dp);
            dp[si][pi] = (notUse || use) ? 1 : 0;
            return notUse || use;
        }
        // If the next character in pattern is '.' or matches the current character in string
        else if (p.charAt(pi) == '.' || s.charAt(si) == p.charAt(pi)) {
            boolean result = isMatch(si + 1, pi + 1, s, p, dp);
            dp[si][pi] = result ? 1 : 0;
            return result;
        }

        dp[si][pi] = 0;
        return false;
    }

    public boolean isMatch(String s, String p) {
        sl = s.length();
        pl = p.length();
        int[][] dp = new int[sl + 1][pl + 1]; // Memoization table
        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }
        return isMatch(0, 0, s, p, dp); // Start the recursive function
    }

    public static void main (String Args[]){
RegularExMat rm = new RegularExMat();
String s="a*";
String p="b*";
System.out.println(rm.isMatch(s,p));
    }
}