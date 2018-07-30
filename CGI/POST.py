import re,sys,cgi

class CGI_POST():
    ##!
    ##! Read POST environment - but only once
    ##!
    
    def CGI_POST_Read(self):
        args=sys.argv

        cli=False
        if (args[0]=="python"):
            cli=True
            
        if (not self.__Posts__ and not cli):
            self.__Posts__={}

            form = cgi.FieldStorage()
            for key in form.keys():
                self.__Posts__[ key ]=form.getvalue(key)

        return self.__Posts__

    ##!
    ##! Read POST var value, read POST env, if unread.
    ##!
    
    def CGI_POST_Get(self,varname=None):
        if (not self.__Posts__):
            self.CGI_POST_Read()
        
        if (varname is not None):
            value=""
            if (self.__Posts__.has_key(varname) ):
                value=self.__Posts__[ varname ]
            
            return value
        else:
            return dict(self.__Posts__)
    
    ##!
    ##! Read POST var value as int.
    ##!
    
    def CGI_POST_Int(self,key):
        return int( self.CGI_POST(key) )
