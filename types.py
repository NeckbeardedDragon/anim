class Color:
    """A 24-bit RGBA color that supports interpolation"""
    def __init__(self,r,g,b,a=255):
        """r, g, b, and a can be values outside of the range 0-255, but will be truncated before returning.
        Doing so will affect interpolation."""
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __add__(self,other):
        if type(other) is not type(self):
            raise NotImplemented
        return color(self.r+other.r,self.g+other.g,self.b+other.b,self.a+other.a)

    def __mul__(self,other):
        try:
            other = float(other)
        except TypeError:
            raise NotImplemented
        return color(self.r*other,self.g*other,self.b*other,self.a*other)

    @property
    def r_(self):
        return min(max(self.r,0),255)

    @property
    def g_(self):
        return min(max(self.g,0),255)

    @property
    def b_(self):
        return min(max(self.b,0),255)

    @property
    def a_(self):
        return min(max(self.a,0),255)

    @property
    def tuple(self):
        return (self.r_,self.g_,self.b_,self.a_)

    @property
    def rgba(self):
        return (self.r_<<24)+(self.g_<<16)+(self.b_<<8)+self.a_

    @property
    def rgb(self):
        return (self.r_<<16)+(self.g_<<8)+self.b_

    def __str__(self):
        return "".join(["#",hex(self.r_),hex(self.g_),hex(self.b_),hex(self.a_)])

    @property
    def rgbstr(self):
        return "".join(["#",hex(self.r_),hex(self.g_),hex(self.b_)])