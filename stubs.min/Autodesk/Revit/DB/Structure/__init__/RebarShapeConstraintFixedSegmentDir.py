class RebarShapeConstraintFixedSegmentDir(RebarShapeConstraint, IDisposable):
    """
    A constraint that can be applied to a RebarShapeSegment and fixes the
       direction of the segment in UV-space.
    
    RebarShapeConstraintFixedSegmentDir(dir: UV)
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeConstraint, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeConstraint, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, dir):
        """ __new__(cls: type, dir: UV) """
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The direction of the RebarShapeSegment in UV-space.

Get: Direction(self: RebarShapeConstraintFixedSegmentDir) -> UV

Set: Direction(self: RebarShapeConstraintFixedSegmentDir) = value
"""

