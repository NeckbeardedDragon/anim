class LinearInterpolator:
    """Linearly interpolates between segments in a given list of values."""    
    def __init__(self,*segments):
        """Segments should be in the form (start value,length,end value)
            start value,end value - objects to be interpolated. Must be of types that can be added with the other values and multiplied by floats
            length - a float denoting how "long" the segment is. 0 length segments are allowed, but will never have their values chosen."""
        self.segments = segments[:]
        self.sum = sum(map(lambda x: x[1],self.segments))
        
    def __call__(self,val):
        """Retrieves an interpolated value.
            Finds the segment val is contained within, and interpolates between the start and end values.
            Values outside the range will extrapolate.
            If val is exactly on the border of two segment, it will return the second segment's start value."""
        while val < 0:
            val += self.sum
        while val >= self.sum:
            val -= self.sum
        for segment in self.segments:
            if val == 0:
                return segment[0]
            if val<segment[1]:
                v = val/segment[1]
                return ((1-v)*segment[0])+(v*segment[2])
            val -= segment[1]
        return segment[0]

def modulo(value):
    """Returns a LinearInterpolator object that acts as a float modulo function."""
    return LinearInterpolator((0,value,value))
