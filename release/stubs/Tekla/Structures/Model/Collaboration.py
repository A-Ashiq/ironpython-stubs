# encoding: utf-8
# module Tekla.Structures.Model.Collaboration calls itself Collaboration
# from Tekla.Structures.Model, Version=2017.0.0.0, Culture=neutral, PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ReferenceModelObjectAttribute(object):
    # no doc
    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ReferenceModelObjectAttribute) -> str

"""

    Extrusion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Extrusion(self: ReferenceModelObjectAttribute) -> Vector

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ReferenceModelObjectAttribute) -> str

"""

    ObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectType(self: ReferenceModelObjectAttribute) -> str

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Origin(self: ReferenceModelObjectAttribute) -> Point

"""

    ProfileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileName(self: ReferenceModelObjectAttribute) -> str

Set: ProfileName(self: ReferenceModelObjectAttribute) = value
"""

    xDir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: xDir(self: ReferenceModelObjectAttribute) -> Vector

"""


    AttributeTypeEnum = None


class IFC2X3_ParametricObject_CircleHollowProfile(ReferenceModelObjectAttribute):
    # no doc
    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: IFC2X3_ParametricObject_CircleHollowProfile) -> float

"""

    WallThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WallThickness(self: IFC2X3_ParametricObject_CircleHollowProfile) -> float

"""



class IFC2X3_ParametricObject_CircleProfile(ReferenceModelObjectAttribute):
    # no doc
    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: IFC2X3_ParametricObject_CircleProfile) -> float

"""



class IFC2X3_ParametricObject_CShapeProfile(ReferenceModelObjectAttribute):
    # no doc
    Depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Depth(self: IFC2X3_ParametricObject_CShapeProfile) -> float

"""

    Girth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Girth(self: IFC2X3_ParametricObject_CShapeProfile) -> float

"""

    InternalFilletRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalFilletRadius(self: IFC2X3_ParametricObject_CShapeProfile) -> float

"""

    WallThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WallThickness(self: IFC2X3_ParametricObject_CShapeProfile) -> float

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: IFC2X3_ParametricObject_CShapeProfile) -> float

"""



class IFC2X3_ParametricObject_EllipseProfile(ReferenceModelObjectAttribute):
    # no doc
    SemiAxis1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SemiAxis1(self: IFC2X3_ParametricObject_EllipseProfile) -> float

"""

    SemiAxis2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SemiAxis2(self: IFC2X3_ParametricObject_EllipseProfile) -> float

"""



class IFC2X3_ParametricObject_IShapeProfile(ReferenceModelObjectAttribute):
    # no doc
    FilletRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilletRadius(self: IFC2X3_ParametricObject_IShapeProfile) -> float

"""

    FlangeThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlangeThickness(self: IFC2X3_ParametricObject_IShapeProfile) -> float

"""

    OverallDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OverallDepth(self: IFC2X3_ParametricObject_IShapeProfile) -> float

"""

    OverallWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OverallWidth(self: IFC2X3_ParametricObject_IShapeProfile) -> float

"""

    WebThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WebThickness(self: IFC2X3_ParametricObject_IShapeProfile) -> float

"""



class IFC2X3_ParametricObject_LShapeProfile(ReferenceModelObjectAttribute):
    # no doc
    Depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Depth(self: IFC2X3_ParametricObject_LShapeProfile) -> float

"""

    EdgeRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeRadius(self: IFC2X3_ParametricObject_LShapeProfile) -> float

"""

    FilletRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilletRadius(self: IFC2X3_ParametricObject_LShapeProfile) -> float

"""

    LegSlope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegSlope(self: IFC2X3_ParametricObject_LShapeProfile) -> float

"""

    Thickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Thickness(self: IFC2X3_ParametricObject_LShapeProfile) -> float

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: IFC2X3_ParametricObject_LShapeProfile) -> float

"""



class IFC2X3_ParametricObject_RectangleHollowProfile(ReferenceModelObjectAttribute):
    # no doc
    InnerFilletRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerFilletRadius(self: IFC2X3_ParametricObject_RectangleHollowProfile) -> float

"""

    OuterFilletRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OuterFilletRadius(self: IFC2X3_ParametricObject_RectangleHollowProfile) -> float

"""

    WallThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WallThickness(self: IFC2X3_ParametricObject_RectangleHollowProfile) -> float

"""

    XDim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XDim(self: IFC2X3_ParametricObject_RectangleHollowProfile) -> float

"""

    YDim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YDim(self: IFC2X3_ParametricObject_RectangleHollowProfile) -> float

"""



class IFC2X3_ParametricObject_RectangleProfile(ReferenceModelObjectAttribute):
    # no doc
    XDim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XDim(self: IFC2X3_ParametricObject_RectangleProfile) -> float

"""

    YDim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YDim(self: IFC2X3_ParametricObject_RectangleProfile) -> float

"""



class IFC2X3_ParametricObject_TShapeProfile(ReferenceModelObjectAttribute):
    # no doc
    Depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Depth(self: IFC2X3_ParametricObject_TShapeProfile) -> float

"""

    FilletRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilletRadius(self: IFC2X3_ParametricObject_TShapeProfile) -> float

"""

    FlangeEdgeRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlangeEdgeRadius(self: IFC2X3_ParametricObject_TShapeProfile) -> float

"""

    FlangeSlope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlangeSlope(self: IFC2X3_ParametricObject_TShapeProfile) -> float

"""

    FlangeThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlangeThickness(self: IFC2X3_ParametricObject_TShapeProfile) -> float

"""

    FlangeWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlangeWidth(self: IFC2X3_ParametricObject_TShapeProfile) -> float

"""

    WebEdgeRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WebEdgeRadius(self: IFC2X3_ParametricObject_TShapeProfile) -> float

"""

    WebSlope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WebSlope(self: IFC2X3_ParametricObject_TShapeProfile) -> float

"""

    WebThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WebThickness(self: IFC2X3_ParametricObject_TShapeProfile) -> float

"""



class IFC2X3_ParametricObject_UShapeProfile(ReferenceModelObjectAttribute):
    # no doc
    Depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Depth(self: IFC2X3_ParametricObject_UShapeProfile) -> float

"""

    EdgeRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeRadius(self: IFC2X3_ParametricObject_UShapeProfile) -> float

"""

    FilletRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilletRadius(self: IFC2X3_ParametricObject_UShapeProfile) -> float

"""

    FlangeSlope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlangeSlope(self: IFC2X3_ParametricObject_UShapeProfile) -> float

"""

    FlangeThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlangeThickness(self: IFC2X3_ParametricObject_UShapeProfile) -> float

"""

    FlangeWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlangeWidth(self: IFC2X3_ParametricObject_UShapeProfile) -> float

"""

    WebThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WebThickness(self: IFC2X3_ParametricObject_UShapeProfile) -> float

"""



class IFC2X3_ParametricObject_ZShapeProfile(ReferenceModelObjectAttribute):
    # no doc
    Depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Depth(self: IFC2X3_ParametricObject_ZShapeProfile) -> float

"""

    EdgeRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeRadius(self: IFC2X3_ParametricObject_ZShapeProfile) -> float

"""

    FilletRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilletRadius(self: IFC2X3_ParametricObject_ZShapeProfile) -> float

"""

    FlangeThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlangeThickness(self: IFC2X3_ParametricObject_ZShapeProfile) -> float

"""

    FlangeWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlangeWidth(self: IFC2X3_ParametricObject_ZShapeProfile) -> float

"""

    WebThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WebThickness(self: IFC2X3_ParametricObject_ZShapeProfile) -> float

"""



class ParametricObject_CustomProfile(ReferenceModelObjectAttribute):
    # no doc

class ParametricObject_ObjectBoundingBox(ReferenceModelObjectAttribute):
    # no doc
    yDir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: yDir(self: ParametricObject_ObjectBoundingBox) -> Vector

"""



class ReferenceModelObjectAttributeEnumerator(object):
    """ ReferenceModelObjectAttributeEnumerator(RMO: ReferenceModelObject) """
    def MoveNext(self):
        """ MoveNext(self: ReferenceModelObjectAttributeEnumerator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: ReferenceModelObjectAttributeEnumerator) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, RMO):
        """ __new__(cls: type, RMO: ReferenceModelObject) """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: ReferenceModelObjectAttributeEnumerator) -> object

"""



