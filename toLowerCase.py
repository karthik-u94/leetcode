class Solution:
    def toLowerCase(self, str: str) -> str:
        l1 = [] # list to store lower case char

        for c in str:
            if "A" <= c <= "Z": # check whether the char is uppercase
                unicode = ord(c) + 32  # add 32 unicode value to it
                char = chr (unicode) # convert into Char
                l1.append(char)
            else:
                l1.append(c) # add to list as it is in lowercase
    
        return ( "".join( l1 ) )
