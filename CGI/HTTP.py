from os import environ

class CGI_HTTP():
    def CGI_HTTP_Header(self,content="text/html\n"):
        html="Content-Type: "+content
        
        return html
    
    def CGI_HTTP_Header_Print(self,content="text/html\n"):
        print  self.CGI_HTTP_Header(content)


