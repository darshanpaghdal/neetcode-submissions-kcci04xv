class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(str(len(s))))
            encoded_str += str(len(s))
            
            for ch in s:
                encoded_str += chr((ord(ch) + 11) % 256) 

        return encoded_str 


        

    def decode(self, s: str) -> List[str]:
        list_of_str= []
        current_sub_str = ""
        
        i=0
        while i<len(s):
            list_of_str.append(s[i + int(s[i]) + 1: i + int(s[i])  + 1 + int(s[i + 1 : i+1 + int(s[i])]) ])
            i = i + int(s[i])  + 1 + int(s[i + 1 : i+1 + int(s[i])])
    
        result = []
        for s in list_of_str:
            decoded_str = ""
            for ch in s:
                decoded_str += chr((ord(ch) - 11) % 256)

            result.append(decoded_str)

        return result   
 

