from os import environ

class CGI_ENV():
    
    def CGI_ENV_Get(self,varname):
        value=""
        if (environ.has_key(varname)):
            value=environ[ varname ]
            
        return value
                
    def CGI_Host_Name(self):
        return self.CGI_ENV_Get("SERVER_NAME")
