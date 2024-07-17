class Solution:
    def reorganizeString(self, s: str) -> str:
        dic = {}
        max_value=None
        max_key=None
        for i in s:
            dic[i] = dic.get(i,0)+1     
            if max_value is None or dic[i] > max_value:
                max_value = dic[i]
                max_key = i

        if max_value > ((len(s)+1)//2):
            return ""

        res = (len(s)) * ['']
        idx = 0
        while(max_value):
            res[idx] = max_key
            idx+=2
            max_value-=1

        for key, value in dic.items():
            if key not in res:
                val = value
                while(value):
                    if idx >= len(s):
                        idx=1
                    res[idx] = key
                    idx+=2
                    value-=1
        return "".join(res)
        
if __name__ == "__main__":
    solution = Solution()
    input_string = "vvloogfhgdjgfhtrhg"
    result = solution.reorganizeString(input_string)
    print(f"Reorganized string: {result}")