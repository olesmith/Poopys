import time

class HTML_Messages():
    def HTML_Exec_Time(self):
        mtime=int(time.time()-self.HTML_Start)
        return self.I(str(mtime)+" secs.")
    
    def HTML_Message_Init(self):
        self.HTML_Start=time.time()

    def HTML_Message_Add(self,msg):
        if (msg.__class__.__name__=="list"):
            msg=self.BR().join(msg)
            
        self.HTML_Messages.append(msg)
    
    def HTML_Messages_Show(self):
        mtime=int(time.time()-self.HTML_Start)

        html=[ self.B("Messages: ") ]
        html=html+[ self.HTML_List(self.HTML_Messages) ]
        html=html+[ self.HTML_Exec_Time() ]
        
        return html
