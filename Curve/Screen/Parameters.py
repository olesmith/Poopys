
class Curve_Screen_Parameters():
    __Settings_Order__=[
        ["R","dR","d2R","d3R",],
        ["T","N","VN","RhoV",],
    ]
    __Settings__={
        "R": {
            "Title": "Curve",
            "Default": True,
            "Curve": True,
            "Vector": False,
            "Function": False,
        },
        "dR":{
            "Title": "1st Derivative",
            "Default": True,
            "Curve": True,
            "Vector": True,
            "Function": False,
        },
        "d2R":{
            "Title": "2nd Derivative",
            "Default": True,
            "Curve": True,
            "Vector": True,
            "Function": False,
        },
        "d3R":{
            "Title": "3rd Derivative",
            "Default": False,
            "Curve": True,
            "Vector": True,
            "Function": False,
        },
        "T":{
            "Title": "Unit Tangent",
            "Default": False,
            "Curve": False,
            "Vector": True,
            "Function": False,
        },
        "N":{
            "Title": "Unit Normal",
            "Default": False,
            "Curve": False,
            "Vector": True,
            "Function": False,
        },
        "VN":{
            "Title": "Velocity Normal",
            "Default": False,
            "Curve": False,
            "Vector": True,
            "Function": False,
        },
        "RhoV":{
            "Title": "Osculating Vector",
            "Default": False,
            "Curve": False,
            "Vector": True,
            "Function": False,
        },
        "Evolute":{
            "Title": "Evolute",
            "Default": False,
            "Curve": True,
            "Vector": False,
            "Function": False,
        },
        "dEvolute":{
            "Title": "Evolute Derivative",
            "Default": False,
            "Curve": True,
            "Vector": False,
            "Function": False,
        },
    }
    
      
    #!
    #! Returns settings table titles.
    #!
    
    def Curve_Settings_Titles(self):
        return [
            "Componente","Numerical","Analytical"
        ]

    
    #!
    #! Returns setting select field options.
    #!
    
    def Curve_Setting_Select_Options(self,settings):
        soptions={}
        soptions[ "multiple" ]=""
        soptions[ "size" ]=10 #len(settings)

        return soptions
            
    #!
    #! Returns setting numerical select field.
    #!
    
    def Curve_Setting_Select_Num(self,ctype,settings):
        return self.HTML_Select(
            ctype+"_Num",
            settings,
            None,
            [],
            [],
            self.Curve_Setting_Select_Options(settings)
        )
    
    #!
    #! Returns setting analytical select field.
    #!
    
    def Curve_Setting_Select_Ana(self,ctype,settings):
        rsettings=[]
        for setting in settings:
            if (self.Curve_Type_Has_Analytical(setting)):
                rsettings.append(setting)
                
        return self.HTML_Select(
            ctype+"_Ana",
            rsettings,
            None,
            [],
            [],
            self.Curve_Setting_Select_Options(rsettings)
        )
    
    #!
    #! Generate typed (Curve, Vector, Function) settings table.
    #!
    
    def Curve_Settings_Typed_Table(self,ctype):
        table=[ self.H(3,ctype+"s") ]
        for settings in self.__Settings_Order__:
            rsettings=[]
            for setting in settings:
                if (self.__Settings__[ setting ][ ctype ]):
                    rsettings.append(setting)
            
            row=[
                self.B(ctype+":"),
                self.Curve_Setting_Select_Num(ctype,rsettings),
                self.Curve_Setting_Select_Ana(ctype,rsettings),
            ]
                    

            table.append(row)

        return table

    #!
    #! Generate the central curve screen parameters table.
    #!
    
    def Curve_Settings_Table(self):
        table=[]
        for ctype in ["Curve","Vector","Function"]:
            table=table+self.Curve_Settings_Typed_Table(ctype)

        return [
            self.H(4,"Components"),
            self.HTML_Table(
                table,
                self.Curve_Settings_Titles(),
                [],
                {"frame": 'border',}
            )
        ]
                
        
