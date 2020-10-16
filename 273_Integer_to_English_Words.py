class Solution:
    def numberToWords(self, num: int) -> str:
        d = {1:"One",
             2:"Two",
             3:"Three",
             4:"Four",
             5:"Five",
             6:"Six",
             7:"Seven",
             8:"Eight",
             9:"Nine",
             10:"Ten",
             11:"Eleven",
             12:"Twelve",
             13:"Thirteen",
             14:"Fourteen",
             15:"Fifteen",
             16:"Sixteen",
             17:"Seventeen",
             18:"Eighteen",
             19:"Nineteen",
             20:"Twenty",
             30:"Thirty",
             40:"Forty",
             50:"Fifty",
             60:"Sixty",
             70:"Seventy",
             80:"Eighty",
             90:"Ninety",
             100:"Hundred",
             1000:"Thousand",
             1000000:"Million",
             1000000000:"Billion"
            }
        
        # get into each 3 number tuple to name it 
        def helper(i:int)->str:
            # from 0-20
            if i<=20:
                return d[i]
            
            # from 20-100
            elif i<100:
                if i%10>0:
                    # need to search 20-100 so need to *10 here 
                    return d[i//10*10] + " " + d[i%10]
                else:
                    return d[i//10*10]
            
            # from 100-1000
            elif i<1000:
                if i%100>0:
                    return d[i//100] + " Hundred " + helper(i%100)
                else:
                    return d[i//100] + " Hundred"
        

        # first divide whole number to tuples of each 3 number, then use helper to             each tuple and conquer 
        res = []
        
        # edge case 
        if num ==0:
            return "Zero"
        
        if num >= 1000000000:
            res.append(d[num//1000000000])
            res.append(str(d[1000000000]))
            num%=1000000000
        
        if num>=1000000:
            res.append(helper(num//1000000))
            res.append(str(d[1000000]))
            num%=1000000
        
        if num>=1000:
            res.append(helper(num//1000))
            res.append(str(d[1000]))
            num%=1000
        
        if num>0:
            res.append(helper(num))
        
        
        # output is string, not list 
        return " ".join([str(elem) for elem in res]) 
        
        
# Time: O(n)
# Space:O(1)   
        
        
        