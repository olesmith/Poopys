
class Curve_Screen_Components():
    __Colors__={
        #"red":       "#ff0000",
        #"green":     "#00ff00",
        #"blue":      "#0000ff",
        #"black":     "#000000",
        #"white":     "#ffffff",
        #"orange":    "#009954",
        #"cyan":      "#337799",
        #"yellow":    "#123456",
    }

    __Components_Order__=[
        "R","dR","d2R","d3R",
        "T","N","VN","RhoV",
        "Evolute","dEvolute"
    ]
    __Components__={
        "R": {
            "Title": "Curve",
            "SVG": "r",
            "Color": {
                "Num": 'blue',
                "Ana": 'blue',
                "Points": "yellow",
                "Rolling": "brown",
            }
        },
        "dR":{
            "Title": "1st Derivative",
            "SVG": "r'",
            "Color":  {
                "Num": 'brown',
                "Ana": 'brown',
                "Thick": 3,
            },
        },
        "d2R":{
            "Title": "2nd Derivative",
            "SVG": "r''",
            "Color":  {
                "Num": 'green',
                "Ana": 'green',
                "Thick": 3,
            },
        },
        "d3R":{
            "Title": "3rd Derivative",
            "SVG": "r'''",
            "Color":  {
                "Num": 'cyan',
                "Ana": 'cyan',
                "Thick": 3,
            },
        },
        "T":{
            "Title": "Unit Tangent",
            "SVG": "t",
            "Color":  {
                "Num": 'darkgreen',
                "Ana": 'darkgreen',
                "Thick": 3,
            },
        },
        "N":{
            "Title": "Unit Normal",
            "SVG": "n",
            "Color":  {
                "Num": 'darkgreen',
                "Ana": 'darkgreen',
                "Thick": 3,
            },
        },
        "VN":{
            "Title": "Velocity Normal",
            "SVG": "r'_n",
            "Color":  {
                "Num": 'cyan',
                "Ana": 'cyan',
                "Thick": 3,
            },
        },
        "RhoV":{
            "Title": "Osculating Vector",
            "SVG": "&#961;",
            "Color":  {
                "Num": 'green',
                "Ana": 'green',
                "Thick": 3,
            }
        },
        "Evolute":{
            "Title": "Evolute",
            "SVG": "c",
            "Color":  {
                "Num": 'orange',
                "Ana": 'orange',
                "Points": "yellow",
            },
        },
        "dEvolute":{
            "Title": "Evolute Derivative",
            "SVG": "c'",
            "Color":  {
                "Num": 'red',
                "Ana": 'red',
                "Thick": 3,
            },
        },

        #Functions
        "v":{
            "Title": "Velocity",
            "SVG": "v",
            "Color":  {
                "Num": 'orange',
                "Ana": 'orange',
            },
        },
        "S":{
            "Title": "Velocity",
            "SVG": "s",
            "Color":  {
                "Num": 'magenta',
                "Ana": 'magenta',
            },
        },
        "v2":{
            "Title": "Squared Velocity",
            "SVG": "v2",
            "Color":  {
                "Num": 'blue',
                "Ana": 'blue',
            },
        },
        "dv2":{
            "Title": "Squared Velocity Derivative",
            "SVG": "v2'",
            "Color":  {
                "Num": 'darkblue',
                "Ana": 'darkblue',
            },
        },
        "Det":{
            "Title": "Determinant",
            "SVG": "D",
            "Color":  {
                "Num": 'red',
                "Ana": 'red',
            },
        },
        "dDet":{
            "Title": "Determinant Derivative",
            "SVG": "D'",
            "Color":  {
                "Num": 'darkred',
                "Ana": 'darkred',
            },
        },
        "Kappa":{
            "Title": "Curvature",
            "SVG": "&#954;",
            "Color":  {
                "Num": 'orange',
                "Ana": 'orange',
            },
        },
        "dKappa":{
            "Title": "Curvature",
            "SVG": "&#954;",
            "Color":  {
                "Num": 'darkorange',
                "Ana": 'darkorange',
            },
        },
        "Rho":{
            "Title": "Curvature Ratio",
            "SVG": "&#961;",
            "Color":  {
                "Num": 'gray',
                "Ana": 'gray',
            },
        },
        "dRho":{
            "Title": "Curvature Ratio",
            "SVG": "&#961;'",
            "Color":  {
                "Num": 'darkgray',
                "Ana": 'darkgray',
            },
        },
        "Phi":{
            "Title": "Curvature Factor",
            "SVG": "&#966;",
            "Color":  {
                "Num": 'green',
                "Ana": 'green',
            }
        },
        "dPhi":{
            "Title": "Curvature Factor",
            "SVG": "&#966;'",
            "Color":  {
                "Num": 'darkgreen',
                "Ana": 'darkgreen',
            }
        },
        "Psi":{
            "Title": "Oscullating Factor",
            "SVG": "&#968;",
            "Color":  {
                "Num": 'brown',
                "Ana": 'brown',
            }
        },
        "dPsi":{
            "Title": "Oscullating Factor",
            "SVG": "&#968;'",
            "Color":  {
                "Num": 'darkbrown',
                "Ana": 'darkbrown',
            }
        },
        "Frenet":{
            "Title": "Frenet System",
            "SVG": "ACS",
            "Color":  {
                "Num": 'black',
                "Ana": 'black',
                "Thick": 2,
            },
        },
    }
    
      
    #!
    #! Returns settings table titles.
    #!
    
    def Curve_Components_Titles(self):
        return [
            "Componente","Numerical","Analytical"
        ]

    
    #!
    #! Returns setting numerical select field.
    #!
    
    def Curve_Component_Get(self,comptype,component="Color",ctype=None):
        if (comptype=="d1R"): comptype="dR"
        
        value=None
        if (ctype==None):
            if (self.__Components__[ comptype ][ component ].__class__.__name__=='dict'):
                ctype="Num"

            else:
                return self.__Components__[ comptype ][ component ]
            
        return self.__Components__[ comptype ][ component ][ ctype ]
     
    #!
    #! Returns setting numerical select field.
    #!
    
    def Curve_Component_Color(self,comptype,ctype=None):
        if (comptype=="d1R"): comptype="dR"
        
        return self.Curve_Component_Get(comptype,"Color",ctype)
     
    #!
    #! Returns setting numerical select field.
    #!
    
    def Curve_Component_Field_Num(self,comptype,component):
        return self.HTML_Color(
            comptype+"_"+component+"_Num",
            self.Curve_Component_Get(component,comptype,"Num")
        )
    
    #!
    #! Returns setting analytical select field.
    #!
    
    def Curve_Component_Field_Ana(self,comptype,component):
        field=""
        if (self.Curve_Type_Has_Analytical(component)):
            field=self.HTML_Color(
                comptype+"_"+component+"_Ana",
                self.Curve_Component_Get(component,comptype,"Ana")
            )

        return field
    
    #!
    #! Generate typed (Curve, Vector, Function) settings row.
    #!
    
    def Curve_Component_Row(self,comptype,component):
        return [
            self.B(component+":"),
            self.Curve_Component_Field_Num(comptype,component),
            self.Curve_Component_Field_Ana(comptype,component),
        ]

    #!
    #! Generate typed (Curve, Vector, Function) settings row.
    #!
    
    def Curve_Components(self,comptype):
        components=[]
        for component in self.__Components_Order__:
            if (self.__Components__[ component ].has_key(comptype)):
                    components.append(component)
                    
        return components
        
    #!
    #! Generate typed (Curve, Vector, Function) settings row.
    #!
    
    def Curve_Components_Table(self,comptype):
        table=[
            self.H(3,comptype+"s"),
            self.B(self.Curve_Components_Titles())
        ]
        
        for component in self.Curve_Components(comptype):
            table.append(
                self.Curve_Component_Row(comptype,component)
            )
            
        return table

    
    #!
    #! Generate the central curve screen parameters table.
    #!
    
    def Curve_Components_Table_HTML(self):
        table=[self.H(2,"Components")]
        for comptype in ["Curve","Vector","Function"]:
            table=table+self.Curve_Components_Table(comptype)

        return [
            self.HTML_Table(
                table,
                [],
                [],
                {"frame": 'border',}
            )
        ]
                
        
