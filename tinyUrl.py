class Codec:
    dict={}
    i=0    

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.i+=1
        self.dict[self.i]=longUrl
        return "http://tinyurl.com/"+str(self.i)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        str=shortUrl.split('/')
        return self.dict[int(str[-1])]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
