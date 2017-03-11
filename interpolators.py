import math

class LinearInterpolator:
    """Linearly interpolates between points in a given list of values."""    
    def __init__(self,*points):
        """Points should be in the form (position, value)
            Values can be any objects that can be added to each other and multiplied by floats
            Positions can be any float.
            Positions can overlap, and due to python's stable sorting, will order themselves along the line in their original ordering.
            This can be used for sharp changes"""
        if len(points)<2:
            raise ValueError("Not enough points")
        self.points = list(points)
        self.points.sort(key=lambda x: x[0])
        
    def __call__(self,val):
        """Retrieves a linearly interpolated value.
            Values outside the range will return the closest point"""
        if val<=self.points[0][0]:
            return self.points[0][1]
        if val>=self.points[-1][0]:
            return self.points[-1][1]
        for i in range(len(self.points)-1):
            if val == self.points[i][0]:
                return self.points[i][1]
            if val < self.points[i+1][0]:
                val -= self.points[i][0]
                val /= self.points[i+1][0]-self.points[i][0]
                return ((1-val)*self.points[i][1])+(val*self.points[i+1][1])
        return None

class CosineInterpolator:
    """Interpolates using cosines between points in a given list of values."""    
    def __init__(self,*points):
        """Points should be in the form (position, value)
            Values can be any objects that can be added to each other and multiplied by floats
            Positions can be any float.
            Positions can overlap, and due to python's stable sorting, will order themselves along the line in their original ordering.
            This can be used for sharp changes"""
        if len(points)<2:
            raise ValueError("Not enough points")
        self.points = list(points)
        self.points.sort(key=lambda x: x[0])
        
    def __call__(self,val):
        """Retrieves a cosine interpolated value.
            Values outside the range will return the closest point"""
        if val<=self.points[0][0]:
            return self.points[0][1]
        if val>=self.points[-1][0]:
            return self.points[-1][1]
        for i in range(len(self.points)-1):
            if val == self.points[i][0]:
                return self.points[i][1]
            if val < self.points[i+1][0]:
                val -= self.points[i][0]
                val /= self.points[i+1][0]-self.points[i][0]
                val = (1-math.cos(val*math.pi))/2
                return ((1-val)*self.points[i][1])+(val*self.points[i+1][1])
        return None


class CubicInterpolator:
    """Cubically interpolates between points in a given list of values."""    
    def __init__(self,*points):
        """Points should be in the form (position, value)
            Values can be any objects that can be added to each other and multiplied by floats
            Positions can be any float.
            Positions can overlap, and due to python's stable sorting, will order themselves along the line in their original ordering.
            This can be used for sharp changes"""
        if len(points)<2:
            raise ValueError("Not enough points")
        self.points = list(points)
        self.points.sort(key=lambda x: x[0])
        
    def __call__(self,val):
        """Retrieves a cubically interpolated value.
            Values outside the range will return the closest point"""
        if val<=self.points[0][0]:
            return self.points[0][1]
        if val>=self.points[-1][0]:
            return self.points[-1][1]
        for i in range(len(self.points)-1):
            if val == self.points[i][0]:
                return self.points[i][1]
            if val < self.points[i+1][0]:
                val -= self.points[i][0]
                val /= self.points[i+1][0]-self.points[i][0]
                y = [None,self.points[i][1],self.points[i+1][1],None]
                if i==0:
                    y[0] = self.points[i][1]
                else:
                    y[0] = self.points[i-1][1]
                if i+2==len(self.points):
                    y[3] = self.points[i+1][1]
                else:
                    y[3] = self.points[i+2][1]

                a = list()
                a.append(y[3]-y[2]-y[0]+y[1])
                a.append(y[0]-y[1]-a[0])
                a.append(y[2]-y[0])
                a.append(y[1])
                return a[0]*val**3+a[1]*val**2+a[2]*val+a[3]
        return None