

class HTML_Table():
    ##!
    ##! Generate table THEAD section: 
    ##!
    
    ##!def HTML_Table_Head(self,titles,indent,troptions,thoptions={}):
    ##!    return self.HTML_Table_Row(
    ##!        titles,
    ##!        ["THEAD","TR"],
    ##!        "TH",
    ##!        troptions,
    ##!        thoptions
    ##!    )
    
    ##!
    ##! Generate one table row.
    ##!
    
    def HTML_Table_Row(self,row,width,trtag,tdtag,troptions,tdoptions):
        html=[]
        html=html+[ self.XML_Tag_Start(trtag,troptions) ]
        html=html+[ self.HTML_Table_Row_Cells(row,width,tdtag,tdoptions) ]
        html=html+[ self.XML_Tag_End(trtag) ]

        return html
    
    
    ##!
    ##! Generate TD (tdtag) cells for one row.
    ##!
    
    def HTML_Table_Row_Cells(self,row,width,tdtag,options):
        html=[]
        c=1
        for cell in row:
            roptions=dict(options)
            if (c==len(row) and c<width):
                roptions[ "colspan" ]=width-c+1
            html.append( self.XML_Tags(tdtag,cell,roptions) )

            c+=1

        return html
        
    ##!
    ##! Find max table width
    ##!
    
    def HTML_Table_Width(self,rows,titles=[]):
        width=len(titles)
        for row in rows:
            if (row.__class__.__name__!='list'): continue
            
            if (len(row)>width): width=len(row)

        return width
   
    ##!
    ##! Generate HTML table. 
    ##!
    
    def HTML_Table(self,rows,titles=[],tails=[],options={},troptions={},tdoptions={},thoptions={},tailoptions={}):
        
        repeattitles=len(rows)+1
        if (options.has_key("repeat")):
            repeattitles=options[ "repeat" ]
            del options[ "repeat" ]

        width=self.HTML_Table_Width(rows,titles)
        
        html=[]
        html=html+[ self.XML_Tag_Start("TABLE",options) ]

        titlerow=[]
        if ( len(titles)>0 ):
            titlerow=[ self.HTML_Table_Row(titles,width,"TR","TH",troptions,thoptions) ]
        
        for i in range( len(rows) ):
            if ( len(titles)>0 and (i % repeattitles)==0 ):
                html.append(titlerow)

            if (rows[i].__class__.__name__=='str'):
                rows[i]=[ rows[i] ]
                
            html.append([ self.HTML_Table_Row(rows[i],width,"TR","TD",troptions,tdoptions) ])
            
        html=html+[ self.XML_Tag_End("TABLE") ]

        return html
    
    
