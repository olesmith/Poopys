from os import environ
import os,sys

class CGI_GET():
    def CGI_GET_Read(self):
        if (not self.__Gets__):
            gets=self.CGI_ENV_Get("QUERY_STRING")
            if (not gets and len(sys.argv)>1):
                args=[]
                for i in range(1,len(sys.argv)):
                    args.append(sys.argv[i])
                    gets="&".join(args)

            gets=gets.split('&')
            
            self.__Gets__={}
            for get in gets:
                eqs=get.split('=')
                if ( len(eqs)>1 ):
                    self.__Gets__[ eqs[0] ]=eqs[1]

        return dict(self.__Gets__)
    
    def CGI_GET_Get(self,varname=None):
        if (not self.__Gets__):
            self.CGI_GET_Read()

        if (varname is not None):
            value=None
            if (self.__Gets__.has_key(varname) ):
                value=self.__Gets__[ varname ]
            
            return value
        else:
            return dict(self.__Gets__)
                
    
