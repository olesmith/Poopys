from os import environ
import os,sys,cgi,cgitb
####cgitb.enable()

from ENV import CGI_ENV
from HTTP import CGI_HTTP
from GET import CGI_GET
from POST import CGI_POST

class CGI(
        CGI_ENV,
        CGI_HTTP,
        CGI_GET,
        CGI_POST,
    ):
    __Gets__={}
    __Posts__={}
        
    def CGI_Is(self):
        res=False
        if (self.CGI_Host_Name()):
            res=True

        return res
    
    def CGI_Args_2_Str(self,args):
        url=[]
        for key in args.keys():
            url.append( key+"="+args[ key ] )
        
        return "&".join(url)
    
    def CGI_Args_2_Url(self,args,url=""):
        return url+"?"+self.CGI_Args_2_Str(args)
