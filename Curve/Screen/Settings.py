
class Curve_Screen_Settings():
    __Settings_Order__=[
        "Derivatives",
        ["R","dR","d2R","d3R",],
        "Frenet and Others",
        ["T","N","VN","RhoV",],
    ]
    
    __Settings__={
        "dR":{
            "Title": "1st Derivative",
            "Default": True,
        },
        "d2R":{
            "Title": "2nd Derivative",
            "Default": True,
        },
        "d3R":{
            "Title": "3rd Derivative",
            "Default": False,
        },
        "T":{
            "Title": "Unit Tangent",
            "Default": False,
        },
        "N":{
            "Title": "Unit Normal",
            "Default": False,
        },
        "VN":{
            "Title": "Velocity Normal",
            "Default": False,
        },
        "RhoV":{
            "Title": "Osculating Vector",
            "Default": False,
        },
        "Evolute":{
            "Title": "Evolute",
            "Default": False,
        },
        "dEvolute":{
            "Title": "Evolute Derivative",
            "Default": False,
        },
    }
    
      
    #!
    #! Generate the central curve screen parameters table.
    #!
    
    def Curve_Settings_Table(self):
        table=[self.H(4,"Drawing Options")]
        for settings in self.__Settings_Order__:
            if (settings.__class__.__name__!='list'):
                table.append(  self.H(5,setting)  )
                continue
            
            for setting in settings:
                value=self.CGI_POST_Get(setting)
                settingsdata=self.__Settings__[ setting ]
                
                row=[
                    self.B(setting)+":",
                    self.HTML_Radios(
                        setting,
                        [1,2],
                        value,
                        ["Show","Hide"]
                    )
                ]
                
                table.append(row)
        return table
                
        
