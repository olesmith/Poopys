import os,datetime,time,re,glob

from time import *

from System import *

Chmod_Command="/bin/chmod"
Chown_Command="/bin/chown"
SoftLink_Command="/bin/ln -s"

file_types={
    "py": {
        "Text":     'Python',
        "Function": 'def',
        "Self":     'self\.',
        "Comments": ['#.*',]
    },
    "php": {
        "Text":     'PHP',
        "Function": 'function',
        "Self":     '\$this->',
        "Comments": ['#.*','/\*.*\*/','//.*']
    },
    "css": {
        "Text":     'CSS',
        "Function": None,
        "Self":     None,
        "Comments": ['/\*.*\*/']
    },
    "html": {
        "Text":     'HTML',
        "Comments": ['<!--.*-->'],
        "Self":     None,
        "Function": None,
    },
    "svg": {
        "Text":     'SVG',
        "Comments": ['<!--.*-->'],
        "Self":     None,
        "Function": None,
    },
    "tex": {
        "Text":     'LaTeX',
        "Function": None,
        "Comments": ['%.*'],
        "Self":     None,
    },
}


class File():
    
    def File_Path_Create(self,fname):
        paths=fname.split('/')
        paths.pop()

        self.Path_Create( "/".join(paths) )

    def File_BaseName(self,fname):
        paths=fname.split('/')

        return paths.pop()

    def File_Is(self,fname):
        return os.path.isfile(fname)

    def File_Exists(self,fname):
        return os.path.isdir(fname) or os.path.isfile(fname) or os.path.islink(fname)

    def Entry_Exists(self,fname):
        return os.path.isdir(fname) or os.path.isfile(fname) or os.path.islink(fname)

    def File_MTime(self,fname):

        mtime=os.path.getmtime(fname)
     
        return mtime

    def Files_MTimes(self,files):
        mtimes=[]
        for fname in files:
            mtimes.append( self.File_MTime(fname) )
        
        return mtimes

    def Files_MTime(self,files):
        mtimes=self.Files_MTimes(files)

        mtime=0
        if ( len(mtimes)>0 ):
            mtime=max(mtimes)
            
        return mtime

    def Time_Show(self,mtime):
        info=localtime(mtime)
    
        return strftime("%d %b %Y, %H:%M:%S",info)

    def File_Path(self,file):
        paths=file.split('/')
        paths.pop()

        return "/".join(paths)

    def File_Read(self,fname):
        if (fname.__class__.__name__=='list'):
            fname="/".join(fname)
            
        f=open(fname,"r" )
        lines=f.read()

        f.close()

        return lines

    def File_Read_Lines(self,fname):
        lines=self.File_Read(fname)

        return lines.split("\n")

    
    def File_Grep(self,fname,regex):
        lines=self.File_Read_Lines(fname)
        rlines=[]
        for line in lines:
            if ( re.search(regex,line) ):
                rlines.append(line)

        return rlines

    def File_Write(self,fname,lines,tell=False):        
        if (fname.__class__.__name__=='list'):
            fname="/".join(fname)

        while (lines and not lines[ len(lines)-1 ]):
            lines.pop(len(lines)-1)
            
        self.File_Path_Create(fname)
        f=open(fname,"w" )
        size=0
        for line in lines:
            f.write("%s\n" % line)
            size+=len(line)

        if (tell):
            if (tell!=True):
                fname=tell
            else:
                comps=fname.split('/')
                #fname=comps.pop( len(comps)-1 )
                print "\t"+fname+" ("+str(size)+" bytes)"
            
        f.close()

        return True

    def Link_Exists(self,fname):
        return os.path.islink(fname)

    ##!
    ##! Makes sure path exists, if not tries to create it.
    ##!
    
    def Path_Create(self,path):
        paths=path.split('/')

        spath=""
        for i in range( len(paths) ):
            spath+=paths[i]+"/"
            try:
                os.stat(spath)
            except:
                print "Creating directory:",spath
                os.mkdir(spath)
                
    ##!
    ##! Returns True if path exists, false elsewise.
    ##!
    
    def Path_Exists(self,path):
        return os.path.isdir(path)
    
    def Path_Is(self,path):
        return os.path.isdir(path)
    
    def File_Type(self,filename,field="Text"):
        ftype="None"
        prereg='(?i)'
        for file_type in file_types:
            if (re.search(prereg+'\.'+file_type+'$',filename)):
                ftype=file_types[ file_type ][ field ]
                break

        return ftype
    
    def File_Read_Remove_Comments(self,filename):
        comments=self.File_Type(filename,"Comments")
        lines=File_Read(filename)
        for i in range( len(lines) ):
            for comment in comments:
                lines[i]=re.sub(comment,"",lines[i])
                
        return lines
    

def Link_Exists(name):
    return File().File_Exists(name)
    
def File_BaseName(name):
    return File().File_BaseName(name)
    
def File_Is(name):
    return File().File_Is(name)
    
def File_Type(name,key="Text"):
    return File().File_Type(name,key)
    
def File_Type_Function(name):
    return File().File_Type(name,"Function")
    
def File_Exists(name):
    return File().File_Exists(name)
    
def Entry_Exists(name):
    return File().Entry_Exists(name)

def File_Read(name):
    return File().File_Read_Lines(name)

def File_Read_Lines(name):
    return File().File_Read_Lines(name)

def File_Read_Remove_Comments(name):
    return File().File_Read_Remove_Comments(name)

def File_MTime(file):
    return File().File_MTime(file)

def Files_MTime(files):
    return File().Files_MTime(files)

def File_Write(name,lines,tell=False):
    return File().File_Write(name,lines,tell)
    
def File_Grep(name,regex):
    return File().File_Grep(name,regex)

def Path_Create(path):
    return File().Path_Create(path)

def Path_Is(path):
    return File().Path_Is(path)

def File_Owner_Set(filename,owner,group=None):
    if (not group): group=owner

    Command_Exec([
        Chown_Command,
        owner+":"+group,
        filename
    ])
    
def File_Permissions_Set(filename,permissions):
    Command_Exec([
        Chmod_Command,
        permissions,
        filename
    ])
def File_SoftLink_Create(source,target):
    if (not Link_Exists(target) and not File_Exists(target)):
        Command_Exec([
            SoftLink_Command,
            source,
            target
        ])

def Path_Current():
    return os.getcwd()

##!
##! All entries in path.
##!
    
def Path_Entries(path):
    entries=glob.glob(path+"/*")
    entries=sorted(entries)
    
    return entries

    
##!
##! All subdir entries in path. Full path
##!
    
def Path_Subdirs(path,withfile=None):
    paths=[]
    for entry in Path_Entries(path):
        if (os.path.isdir(entry)):
            if (withfile):
                file=os.path.join(entry,withfile)
                if (os.path.isfile(file)):
                    paths.append(entry)
            else:
                paths.append(entry)
                    
    paths.sort()
    
    return paths

##!
##! Subdir (short) dir names in path
##!
    
def Path_Dirs(path,withfile=None):
    rpaths=Path_Subdirs(path,withfile)

    subdirs=[]
    for rpath in rpaths:
        comps=rpath.split("/");
        subdirs.append( comps.pop() )
            
    return subdirs

##!
##! 
##!
    
def Path_Files(path,regex=None):
    files={}
    for filename in Path_Entries(path):
        if (os.path.isfile(filename)):
            if (regex!=None):
                if (re.search(regex,filename)):
                    files[ filename ]=True
            else:
                files[ filename ]=True
    files=files.keys()
    files.sort()

    return files

##!
##! path subdirs whose names are numbered, ie statrs with a number (For easy sorting).
##!
    
def Path_Subdirs_Num(path):
    paths=[]
    for rpath in Path_Subdirs(path):
        comps=rpath.split('/')
        rpath=comps.pop()
        if (re.match('^-?[\d\.]+$',rpath)):
            paths.append(rpath)

    return paths

    
##!
##! Detect path tree of subdirs. Recursive.
##!
    
def Path_Tree(path,regex=""):
    tree={}
    for subdir in Path_Dirs(path):
        rpath=path+"/"+subdir
        if (regex and (not re.match(regex,subdir)) ):
            continue
        tree[ subdir ]=Path_Tree(rpath,regex)

    return tree
    
