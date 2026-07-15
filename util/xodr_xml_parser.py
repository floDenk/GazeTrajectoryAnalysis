from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union


@dataclass
class OpenDriveElement:
    class Meta:
        name = "_OpenDriveElement"


class EAccessRestrictionType(Enum):
    SIMULATOR = "simulator"
    AUTONOMOUS_TRAFFIC = "autonomousTraffic"
    PEDESTRIAN = "pedestrian"
    PASSENGER_CAR = "passengerCar"
    BUS = "bus"
    DELIVERY = "delivery"
    EMERGENCY = "emergency"
    TAXI = "taxi"
    THROUGH_TRAFFIC = "throughTraffic"
    TRUCK = "truck"
    BICYCLE = "bicycle"
    MOTORCYCLE = "motorcycle"
    NONE = "none"
    TRUCKS = "trucks"
    HOV = "HOV"


class EBorderType(Enum):
    CONCRETE = "concrete"
    CURB = "curb"
    PAINT = "paint"


class EBridgeType(Enum):
    CONCRETE = "concrete"
    STEEL = "steel"
    BRICK = "brick"
    WOOD = "wood"


class EConnectionType(Enum):
    DEFAULT = "default"
    VIRTUAL = "virtual"


class EContactPoint(Enum):
    START = "start"
    END = "end"


class ECountryCodeDeprecated(Enum):
    OPEN_DRIVE = "OpenDRIVE"
    AUSTRIA = "Austria"
    BRAZIL = "Brazil"
    CHINA = "China"
    FRANCE = "France"
    GERMANY = "Germany"
    ITALY = "Italy"
    SWITZERLAND = "Switzerland"
    USA = "USA"


class EDataQualityRawDataPostProcessing(Enum):
    RAW = "raw"
    CLEANED = "cleaned"
    PROCESSED = "processed"
    FUSED = "fused"


class EDataQualityRawDataSource(Enum):
    SENSOR = "sensor"
    CADASTER = "cadaster"
    CUSTOM = "custom"


class EDirection(Enum):
    SAME = "same"
    OPPOSITE = "opposite"


class EElementDir(Enum):
    PLUS_SIGN = "+"
    HYPHEN_MINUS = "-"


class EJunctionGroupType(Enum):
    """
    :cvar ROUNDABOUT:
    :cvar UNKNOWN:
    :cvar COMPLEX_JUNCTION: for example junctions with slip lanes
    :cvar HIGHWAY_INTERCHANGE: for example clover leaf interchange
    """

    ROUNDABOUT = "roundabout"
    UNKNOWN = "unknown"
    COMPLEX_JUNCTION = "complexJunction"
    HIGHWAY_INTERCHANGE = "highwayInterchange"


class EJunctionSegmentType(Enum):
    JOINT = "joint"
    LANE = "lane"


class EJunctionType(Enum):
    """
    :cvar DEFAULT: Common junction, used if no value is specified
    :cvar VIRTUAL: Virtual junction, e.g. driveways and entries to
        parking lots
    :cvar DIRECT: Direct junction, e.g. entries and exits
    :cvar CROSSING: Unconnected crossing, e.g. railroad or pedestrian
    """

    DEFAULT = "default"
    VIRTUAL = "virtual"
    DIRECT = "direct"
    CROSSING = "crossing"


class ELaneAdvisory(Enum):
    """
    :cvar BOTH: May be used by traffic from both adjacent lanes as an
        advisory lane.
    :cvar INNER: May be used by traffic from the inner lane as an
        advisory lane.
    :cvar NONE: May not be used as an advisory lane.
    :cvar OUTER: May be used by traffic from the outer lane as an
        advisory lane.
    """

    BOTH = "both"
    INNER = "inner"
    NONE = "none"
    OUTER = "outer"


class ELaneType(Enum):
    """The lane type is defined per lane.

    A lane type defines the main purpose of a lane and its corresponding
    traffic rules.

    :cvar SHOULDER: Soft border at the edge of the road.
    :cvar BORDER: Hard border at the edge of the road. It has the same
        height as the adjacent drivable lane.
    :cvar DRIVING: Normal drivable road that is not one of the other
        types.
    :cvar STOP: Hard shoulder on motorways for emergency stops.
    :cvar NONE: Space on the outermost edge of the road. A none lane
        does not have actual content. Its only purpose is for
        applications to register that ASAM OpenDRIVE is still present in
        case the (human) driver leaves the road.
    :cvar RESTRICTED: Lane on which cars should not drive. The lane has
        the same height as drivable lanes. Typically, the lane is
        separated with lines and often contains dotted lines as well.
    :cvar PARKING: Lane with parking spaces.
    :cvar MEDIAN: Lane that sits between driving lanes that lead in
        opposite directions. It is typically used to separate traffic in
        towns on large roads.
    :cvar BIKING: Lane that is reserved for cyclists.
    :cvar SHARED: Shared by all traffic participants. For shared
        walking/biking lanes use &lt;access&gt;.
    :cvar SIDEWALK: Use walking instead
    :cvar CURB: Curb at the edge of the road. Curb stones have a
        different height than the adjacent drivable lanes.
    :cvar EXIT: Lane that is used for sections that are parallel to the
        main road and lead to an exit from the main road. It is mainly
        used for deceleration lanes.
    :cvar ENTRY: Lane that is used for sections that are parallel to the
        main road and merge into the main road. It is mainly used for
        acceleration lanes.
    :cvar ON_RAMP: Ramp leading to a motorway from rural or urban roads.
    :cvar OFF_RAMP: Ramp leading away from a motorway and onto rural
        urban roads.
    :cvar CONNECTING_RAMP: Ramp that connects two motorways, for
        example, motorway junctions.
    :cvar BIDIRECTIONAL: This lane type has two use cases: a) only
        driving lane on a narrow road which may be used in both
        directions; b) continuous two-way left turn lane on multi-lane
        roads – US road networks Use @direction instead
    :cvar SPECIAL1: deprecated
    :cvar SPECIAL2: deprecated
    :cvar SPECIAL3: deprecated
    :cvar ROAD_WORKS:
    :cvar TRAM: Lane used by trams only.
    :cvar RAIL: Lane used by trains only.
    :cvar BUS: Use &lt;access&gt; instead
    :cvar TAXI: Use &lt;access&gt; instead
    :cvar HOV: High-occupancy vehicle / carpool vehicle. Use
        &lt;access&gt; instead
    :cvar MWY_ENTRY: deprecated, use entry instead
    :cvar MWY_EXIT: deprecated, use exit instead
    :cvar WALKING: Lane on which pedestrians can walk.
    :cvar SLIP_LANE: On a slip lane a driver can change roads without
        driving into the main intersection.
    """

    SHOULDER = "shoulder"
    BORDER = "border"
    DRIVING = "driving"
    STOP = "stop"
    NONE = "none"
    RESTRICTED = "restricted"
    PARKING = "parking"
    MEDIAN = "median"
    BIKING = "biking"
    SHARED = "shared"
    SIDEWALK = "sidewalk"
    CURB = "curb"
    EXIT = "exit"
    ENTRY = "entry"
    ON_RAMP = "onRamp"
    OFF_RAMP = "offRamp"
    CONNECTING_RAMP = "connectingRamp"
    BIDIRECTIONAL = "bidirectional"
    SPECIAL1 = "special1"
    SPECIAL2 = "special2"
    SPECIAL3 = "special3"
    ROAD_WORKS = "roadWorks"
    TRAM = "tram"
    RAIL = "rail"
    BUS = "bus"
    TAXI = "taxi"
    HOV = "HOV"
    MWY_ENTRY = "mwyEntry"
    MWY_EXIT = "mwyExit"
    WALKING = "walking"
    SLIP_LANE = "slipLane"


class ELaneDirection(Enum):
    """
    :cvar BOTH: Bidirectional, both directions are valid.
    :cvar REVERSED: Directly opposite to the standard direction.
    :cvar STANDARD: Direction is determined by the combination of
        &lt;left&gt; or &lt;right&gt; lane grouping and the values LHT
        or RHT of the @rule attribute of a road.
    """

    BOTH = "both"
    REVERSED = "reversed"
    STANDARD = "standard"


class EMaxSpeedString(Enum):
    NO_LIMIT = "no limit"
    UNDEFINED = "undefined"


class EObjectType(Enum):
    """
    :cvar NONE: All other objects, that don't fit into existing
        categories or unknown.
    :cvar OBSTACLE: An obstacle is an object on or beside the road that
        cannot be passed.
    :cvar CAR: deprecated
    :cvar POLE: A pole is a thin long object.
    :cvar TREE: A tree object is a single vegetational object with a
        trunk.
    :cvar VEGETATION: A vegetation object is a single vegetational
        object without a trunk or an area of vegetation.
    :cvar BARRIER: A barrier is a continuous roadside object, which
        cannot be passed.
    :cvar BUILDING: A building is a closed object, which cannot be
        passed.
    :cvar PARKING_SPACE: A parkingSpace is an object on a lane on which
        vehicles are parked.
    :cvar PATCH: use roadSurface instead
    :cvar RAILING: use barrier instead
    :cvar TRAFFIC_ISLAND: A trafficIsland object is on the road and
        should not be passed by vehicles.
    :cvar CROSSWALK: A crosswalk is an object on the road that can be
        passed. It is recommended to be defined as &lt;crossPath&gt;
        within a junction for pedestrian/bicycle simulation. If the
        crosswalk is defined as an object only, it will not be used for
        pedestrian/bicycle simulation.
    :cvar STREET_LAMP: use pole instead
    :cvar GANTRY: A gantry is an object above a road on which
        &lt;signals&gt; are placed.
    :cvar SOUND_BARRIER: use barrier instead
    :cvar VAN:
    :cvar BUS: deprecated
    :cvar TRAILER: deprecated
    :cvar BIKE: deprecated
    :cvar MOTORBIKE: deprecated
    :cvar TRAM: deprecated
    :cvar TRAIN: deprecated
    :cvar PEDESTRIAN: deprecated
    :cvar WIND: deprecated, use pole instead
    :cvar ROAD_MARK: A roadMark object is painted on the road and can be
        passed.
    :cvar ROAD_SURFACE: A roadSurface object is on the road and can be
        passed.
    """

    NONE = "none"
    OBSTACLE = "obstacle"
    CAR = "car"
    POLE = "pole"
    TREE = "tree"
    VEGETATION = "vegetation"
    BARRIER = "barrier"
    BUILDING = "building"
    PARKING_SPACE = "parkingSpace"
    PATCH = "patch"
    RAILING = "railing"
    TRAFFIC_ISLAND = "trafficIsland"
    CROSSWALK = "crosswalk"
    STREET_LAMP = "streetLamp"
    GANTRY = "gantry"
    SOUND_BARRIER = "soundBarrier"
    VAN = "van"
    BUS = "bus"
    TRAILER = "trailer"
    BIKE = "bike"
    MOTORBIKE = "motorbike"
    TRAM = "tram"
    TRAIN = "train"
    PEDESTRIAN = "pedestrian"
    WIND = "wind"
    ROAD_MARK = "roadMark"
    ROAD_SURFACE = "roadSurface"


class EOrientation(Enum):
    PLUS_SIGN = "+"
    HYPHEN_MINUS = "-"
    NONE = "none"


class EOutlineFillType(Enum):
    GRASS = "grass"
    CONCRETE = "concrete"
    COBBLE = "cobble"
    ASPHALT = "asphalt"
    PAVEMENT = "pavement"
    GRAVEL = "gravel"
    SOIL = "soil"
    PAINT = "paint"


class EParamPoly3PRange(Enum):
    ARC_LENGTH = "arcLength"
    NORMALIZED = "normalized"


class ERoadMarkColor(Enum):
    """The known keywords for the road mark color information are:

    :cvar STANDARD: equivalent to "white"
    :cvar BLUE:
    :cvar GREEN:
    :cvar RED:
    :cvar WHITE:
    :cvar YELLOW:
    :cvar BLACK:
    :cvar ORANGE:
    :cvar VIOLET:
    """

    STANDARD = "standard"
    BLUE = "blue"
    GREEN = "green"
    RED = "red"
    WHITE = "white"
    YELLOW = "yellow"
    BLACK = "black"
    ORANGE = "orange"
    VIOLET = "violet"


class ERoadMarkRule(Enum):
    NO_PASSING = "no passing"
    CAUTION = "caution"
    NONE = "none"


class ERoadMarkType(Enum):
    """The known keywords for the simplified road mark type information are:

    :cvar NONE:
    :cvar SOLID:
    :cvar BROKEN:
    :cvar SOLID_SOLID: For double solid line
    :cvar SOLID_BROKEN: From inside to outside, exception: center lane –
        from left to right
    :cvar BROKEN_SOLID: From inside to outside, exception: center lane –
        from left to right
    :cvar BROKEN_BROKEN: From inside to outside, exception: center lane
        – from left to right
    :cvar BOTTS_DOTS:
    :cvar GRASS: Meaning a grass edge
    :cvar CURB:
    :cvar CUSTOM: If detailed description is given in child tags
    :cvar EDGE: Describing the limit of usable space on a road
    """

    NONE = "none"
    SOLID = "solid"
    BROKEN = "broken"
    SOLID_SOLID = "solid solid"
    SOLID_BROKEN = "solid broken"
    BROKEN_SOLID = "broken solid"
    BROKEN_BROKEN = "broken broken"
    BOTTS_DOTS = "botts dots"
    GRASS = "grass"
    CURB = "curb"
    CUSTOM = "custom"
    EDGE = "edge"


class ERoadMarkWeight(Enum):
    STANDARD = "standard"
    BOLD = "bold"


class ERoadType(Enum):
    """The known keywords for the road type information are:"""

    UNKNOWN = "unknown"
    RURAL = "rural"
    MOTORWAY = "motorway"
    TOWN = "town"
    LOW_SPEED = "lowSpeed"
    PEDESTRIAN = "pedestrian"
    BICYCLE = "bicycle"
    TOWN_EXPRESSWAY = "townExpressway"
    TOWN_COLLECTOR = "townCollector"
    TOWN_ARTERIAL = "townArterial"
    TOWN_PRIVATE = "townPrivate"
    TOWN_LOCAL = "townLocal"
    TOWN_PLAY_STREET = "townPlayStreet"


class ERoadLanesLaneSectionLcrLaneRoadMarkLaneChange(Enum):
    INCREASE = "increase"
    DECREASE = "decrease"
    BOTH = "both"
    NONE = "none"


class ERoadLanesLaneSectionLrLaneAccessRule(Enum):
    ALLOW = "allow"
    DENY = "deny"


class ERoadLinkElementType(Enum):
    ROAD = "road"
    JUNCTION = "junction"


class ERoadObjectsObjectParkingSpaceAccess(Enum):
    ALL = "all"
    CAR = "car"
    WOMEN = "women"
    HANDICAPPED = "handicapped"
    BUS = "bus"
    TRUCK = "truck"
    ELECTRIC = "electric"
    RESIDENTS = "residents"


class ERoadRailroadSwitchPosition(Enum):
    DYNAMIC = "dynamic"
    STRAIGHT = "straight"
    TURN = "turn"


class ERoadSignalsDisplayType(Enum):
    """
    :cvar LED: Full LED boards
    :cvar MONOCHROM_GRAPHIC: Yellow or white text as lights on black
        background
    :cvar ROTATING_PRISM_HORIZONTAL: No lights. Horizontal rotating
        metal prism.
    :cvar ROTATING_PRISM_VERTICAL: No lights. Vertical rotating metal
        prism.
    :cvar SIMPLE_MATRIX: Outside is fixed, content inside changes.
    :cvar OTHER: All other display types that do not fit into current
        categories
    """

    LED = "LED"
    MONOCHROM_GRAPHIC = "monochromGraphic"
    ROTATING_PRISM_HORIZONTAL = "rotatingPrismHorizontal"
    ROTATING_PRISM_VERTICAL = "rotatingPrismVertical"
    SIMPLE_MATRIX = "simpleMatrix"
    OTHER = "other"


class ERoadSignalsSignalReferenceElementType(Enum):
    OBJECT = "object"
    SIGNAL = "signal"


class ERoadSurfaceCrgMode(Enum):
    """
    :cvar ATTACHED: ASAM OpenCRG reference line: is discarded. Total
        height: ASAM OpenDRIVE height + OpenCRG height
    :cvar ATTACHED0: ASAM OpenCRG reference line: is discarded. Total
        height: OpenCRG height only
    :cvar GENUINE: ASAM OpenCRG reference line: shifted and rotated so
        beginning of reference line matches position given in ASAM
        OpenDRIVE. Total height: OpenCRG height only
    :cvar GLOBAL: ASAM OpenCRG reference line: taken unmodified. Total
        height: OpenCRG height only
    """

    ATTACHED = "attached"
    ATTACHED0 = "attached0"
    GENUINE = "genuine"
    GLOBAL = "global"


class ERoadSurfaceCrgPurpose(Enum):
    ELEVATION = "elevation"
    FRICTION = "friction"


class ESideType(Enum):
    LEFT = "left"
    RIGHT = "right"
    FRONT = "front"
    REAR = "rear"


class ESignalsSemanticsLane(Enum):
    NO_OVERTAKE_CARS = "noOvertakeCars"
    NO_OVERTAKE_CARS_END = "noOvertakeCarsEnd"
    NO_OVERTAKE_TRUCKS = "noOvertakeTrucks"
    NO_OVERTAKE_TRUCKS_END = "noOvertakeTrucksEnd"
    PRIORITY_OVER_ONCOMING = "priorityOverOncoming"
    ROUNDABOUT = "roundabout"
    YIELD_FOR_ONCOMING = "yieldForOncoming"


class ESignalsSemanticsPriority(Enum):
    VALUE_4WAY = "4way"
    KEEP_CLEAR_LINE = "keepClearLine"
    NO_PARKING_LINE = "noParkingLine"
    NO_TURN_ON_RED = "noTurnOnRed"
    PRIORITY_ROAD = "priorityRoad"
    PRIORITY_ROAD_END = "priorityRoadEnd"
    PRIORITY_TO_THE_RIGHT_RULE = "priorityToTheRightRule"
    STOP = "stop"
    STOP_LINE = "stopLine"
    TURN_ON_RED_ALLOWED = "turnOnRedAllowed"
    TRAFFIC_LIGHT = "trafficLight"
    WAITING_LINE = "waitingLine"
    YIELD = "yield"


class ESignalsSemanticsSpeed(Enum):
    MAXIMUM = "maximum"
    MAXIMUM_END = "maximumEnd"
    MINIMUM = "minimum"
    MINIMUM_END = "minimumEnd"
    RECOMMENDED = "recommended"
    RECOMMENDED_END = "recommendedEnd"
    ZONE = "zone"
    ZONE_END = "zoneEnd"


class ESignalsSemanticsSupplementaryDistance(Enum):
    FOR = "for"
    IN = "in"


class ESignalsSemanticsSupplementaryEnvironment(Enum):
    FOG = "fog"
    RAIN = "rain"
    SNOW = "snow"


class ESignalsSemanticsSupplementaryTime(Enum):
    DAY = "day"
    TIME = "time"


class EStationPlatformSegmentSide(Enum):
    LEFT = "left"
    RIGHT = "right"


class EStationType(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class EStripMode(Enum):
    """
    :cvar INDEPENDENT: height values due to cross section surfaces are
        calculated independent of the inner strip
    :cvar RELATIVE: height values due to cross section surfaces are
        added to the height values of the outer edge of the inner strip
    """

    INDEPENDENT = "independent"
    RELATIVE = "relative"


class ETrafficRule(Enum):
    RHT = "RHT"
    LHT = "LHT"


class ETunnelType(Enum):
    """
    :cvar STANDARD:
    :cvar UNDERPASS: i.e. sides are open for daylight
    """

    STANDARD = "standard"
    UNDERPASS = "underpass"


class EUnit(Enum):
    M = "m"
    KM = "km"
    FT = "ft"
    MILE = "mile"
    M_S = "m/s"
    MPH = "mph"
    KM_H = "km/h"
    KG = "kg"
    T = "t"
    PERCENT_SIGN = "%"


class EUnitDistance(Enum):
    M = "m"
    KM = "km"
    FT = "ft"
    MILE = "mile"


class EUnitSpeed(Enum):
    M_S = "m/s"
    MPH = "mph"
    KM_H = "km/h"


class TBool(Enum):
    TRUE = "true"
    FALSE = "false"


@dataclass
class TDataQualityError:
    """
    Describes the error range, given in [m], of measurement data that is integrated
    into the ASAM OpenDRIVE file.

    :ivar xy_absolute: Absolute error of the road data in x/y direction
    :ivar xy_relative: Relative error of the road data between adjacent
        element entries in x/y direction.
    :ivar z_absolute: Absolute error of the road data in z direction
    :ivar z_relative: Relative error of the road data between adjacent
        element entries in z-direction.
    """

    class Meta:
        name = "t_dataQuality_Error"

    xy_absolute: Optional[float] = field(
        default=None,
        metadata={
            "name": "xyAbsolute",
            "type": "Attribute",
            "required": True,
        },
    )
    xy_relative: Optional[float] = field(
        default=None,
        metadata={
            "name": "xyRelative",
            "type": "Attribute",
            "required": True,
        },
    )
    z_absolute: Optional[float] = field(
        default=None,
        metadata={
            "name": "zAbsolute",
            "type": "Attribute",
            "required": True,
        },
    )
    z_relative: Optional[float] = field(
        default=None,
        metadata={
            "name": "zRelative",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class THeaderGeoReference:
    """Spatial reference systems are standardized by the European Petroleum Survey
    Group Geodesy (EPSG) and are defined by parameters describing the geodetic
    datum.

    A geodetic datum is a coordinate reference system for a collection
    of positions that are relative to an ellipsoid model of the earth. A
    geodetic datum is described by a projection string according to
    PROJ, that is, a format for the exchange of data between two
    coordinate systems. This data shall be marked as CDATA, because it
    may contain characters that interfere with the XML syntax of an
    element’s attribute.
    """

    class Meta:
        name = "t_header_GeoReference"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class TInclude:
    """
    Provides information about additional files that should be included while
    processing the ASAM OpenDRIVE file.

    :ivar file: Location of the file that is to be included
    """

    class Meta:
        name = "t_include"

    file: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TUserData:
    """
    Describes any additional information or data that is needed by an application
    for a specific reason.

    :ivar any_element:
    :ivar code: Code for the user data. Free text, depending on
        application.
    :ivar value: User data. Free text, depending on application.
    """

    class Meta:
        name = "t_userData"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class TYesNo(Enum):
    YES = "yes"
    NO = "no"


@dataclass
class TDataQualityRawData:
    """
    Describes some basic metadata containing information about the raw data.

    :ivar date: Date of the delivery of raw data, to be given in ISO
        8601 notification (YYYY-MM-DDTHH:MM:SS). Time-of-day may be
        omitted
    :ivar post_processing: Information about the kind of data handling
        before exporting data into the ASAM OpenDRIVE file
    :ivar post_processing_comment: Comments concerning the post
        processing attribute. Free text, depending on the application
    :ivar source: Source that has been used for retrieving the raw data;
        further sources to be added in upcoming versions
    :ivar source_comment: Comments concerning the @source . Free text,
        depending on the application
    """

    class Meta:
        name = "t_dataQuality_RawData"

    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    post_processing: Optional[EDataQualityRawDataPostProcessing] = field(
        default=None,
        metadata={
            "name": "postProcessing",
            "type": "Attribute",
            "required": True,
        },
    )
    post_processing_comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "postProcessingComment",
            "type": "Attribute",
        },
    )
    source: Optional[EDataQualityRawDataSource] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    source_comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceComment",
            "type": "Attribute",
        },
    )


@dataclass
class TJunction(OpenDriveElement):
    """
    Junctions model intersections between roads.

    :ivar id: ID of the junction to which the road belongs, for example
        connecting roads, cross paths, and roads of a junction boundary.
        Use -1 for none.
    :ivar name: Name of the junction. May be chosen freely.
    """

    class Meta:
        name = "t_junction"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TDataQuality:
    """
    Describes the quality and accuracy of measurement data that is integrated into
    the ASAM OpenDRIVE file.
    """

    class Meta:
        name = "t_dataQuality"

    error: Optional[TDataQualityError] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    raw_data: Optional[TDataQualityRawData] = field(
        default=None,
        metadata={
            "name": "rawData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TControllerControl(OpenDriveElement):
    """
    Provides information about a single signal within a signal group controlled by
    the corresponding controller.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar signal_id: ID of the controlled signal
    :ivar type_value: Type of control. Free Text, depends on the
        application.
    """

    class Meta:
        name = "t_controller_control"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    signal_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "signalId",
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class THeaderOffset(OpenDriveElement):
    """To avoid large coordinates, an offset of the whole dataset may be applied
    using the &lt;offset&gt; element.

    It enables inertial relocation and re-orientation of datasets. The
    dataset is first translated by @x, @y, and @z. Afterwards, it is
    rotated by @hdg around the new origin. Rotation around the z-axis
    should be avoided.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar hdg: Heading offset (rotation around resulting z-axis)
    :ivar x: Inertial x offset
    :ivar y: Inertial y offset
    :ivar z: Inertial z offset
    """

    class Meta:
        name = "t_header_Offset"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    hdg: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    z: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TJunctionGroupJunctionReference(OpenDriveElement):
    """
    References to existing &lt;junction&gt; elements.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar junction: ID of the junction
    """

    class Meta:
        name = "t_junctionGroup_junctionReference"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    junction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TJunctionBoundarySegment(OpenDriveElement):
    """
    Segments run counter clockwise around the junction and form a closed junction
    boundary.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar road_id: ID of the road used for the segment
    """

    class Meta:
        name = "t_junction_boundary_segment"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    road_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadId",
            "type": "Attribute",
        },
    )


@dataclass
class TJunctionConnectionLaneLink(OpenDriveElement):
    """Provides information about the lanes that are linked between an incoming
    road and a connecting road.

    It is strongly recommended to provide this element. It is deprecated
    to omit the &lt;laneLink&gt; element.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar from_value: ID of the incoming lane
    :ivar overlap_zone: Specifies the length of the area where traffic
        from both overlapping lanes shares the space. It is defined in s
        length relative to the position of the junction. Intended for
        direct junctions only. Default is 100.
    :ivar to: ID of the connection lane
    """

    class Meta:
        name = "t_junction_connection_laneLink"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    from_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
            "required": True,
        },
    )
    overlap_zone: Optional[float] = field(
        default=None,
        metadata={
            "name": "overlapZone",
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )
    to: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TJunctionController(OpenDriveElement):
    """
    Lists the controllers that should be grouped in a sychronization group (limited
    to that particular junction).

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: ID of the controller
    :ivar sequence: Sequence number (priority) of this controller with
        respect to other controllers in the same junction
    :ivar type_value: Type of control for this junction. Free text,
        depending on the application.
    """

    class Meta:
        name = "t_junction_controller"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    sequence: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class TJunctionCrossPathLaneLink(OpenDriveElement):
    """
    Define the links between the lanes of the &lt;crossPath&gt; to the lanes of
    other roads.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar from_value: Lane ID of either @roadAtEnd for
        &lt;endLaneLink&gt; or @roadAtStart for &lt;startLaneLink&gt;
    :ivar s: s-coordinate of either start or end point in linked road.
    :ivar to: Lane ID of @crossingRoad
    """

    class Meta:
        name = "t_junction_crossPath_laneLink"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    from_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    to: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TJunctionElevationGridElevation(OpenDriveElement):
    """
    Defines the z-values at the regular grid points along the junction reference
    line.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar center: List of defined z-values.
    :ivar left: List of defined z-values from inside to outside.
    :ivar right: List of defined z-values from inside to outside.
    """

    class Meta:
        name = "t_junction_elevationGrid_elevation"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    center: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    left: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    right: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TJunctionPredecessorSuccessor(OpenDriveElement):
    """Provides detailed information about the predecessor / successor road of a
    virtual connection.

    Currently, only the @elementType “road” is allowed.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar element_dir: Direction, relative to the s-direction, of the
        connection on the preceding / succeeding road
    :ivar element_id: ID of the linked element
    :ivar element_s: s-coordinate where the connection meets the
        preceding / succeeding road.
    :ivar element_type: Type of the linked element. Currently only
        "road" is allowed.
    """

    class Meta:
        name = "t_junction_predecessorSuccessor"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    element_dir: Optional[EElementDir] = field(
        default=None,
        metadata={
            "name": "elementDir",
            "type": "Attribute",
        },
    )
    element_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "elementId",
            "type": "Attribute",
            "required": True,
        },
    )
    element_s: Optional[float] = field(
        default=None,
        metadata={
            "name": "elementS",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    element_type: str = field(
        init=False,
        default="road",
        metadata={
            "name": "elementType",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TJunctionPriority(OpenDriveElement):
    """The junction priority record provides information about the priority of one
    road over another road that are part of this junction.

    It is only required if priorities cannot be derived from signs or
    signals in a junction or on tracks leading to a junction.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar high: ID of the prioritized road
    :ivar low: ID of the road with lower priority
    """

    class Meta:
        name = "t_junction_priority"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    high: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    low: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TJunctionRoadSection(OpenDriveElement):
    """
    Define the s range of the crossing roads with possible crossing traffic.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: Unique ID within the junction
    :ivar road_id: ID of the road of this roadSection element
    :ivar s_end: End position of the crossing junction in the road
        reference line coordinate system. This attribute is mandatory
        for crossing junctions.
    :ivar s_start: Start position of the crossing junction in the road
        reference line coordinate system. This attribute is mandatory
        for crossing junctions.
    """

    class Meta:
        name = "t_junction_roadSection"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    road_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadId",
            "type": "Attribute",
        },
    )
    s_end: Optional[float] = field(
        default=None,
        metadata={
            "name": "sEnd",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    s_start: Optional[float] = field(
        default=None,
        metadata={
            "name": "sStart",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )


@dataclass
class TLicense(OpenDriveElement):
    """
    Licensing information about the OpenDRIVE file.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar name: The full name of the license. Informational only.
    :ivar resource: Link to an URL where the full license text can be
        found.
    :ivar spdxid: The identifier of the license from the SPDX license
        list. Can also be an SPDX License Expression, which is also
        applicable to custom licenses (LicenseRef-...).
    :ivar text: The full license text.
    """

    class Meta:
        name = "t_license"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    resource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    spdxid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TRoadElevationProfileElevation(OpenDriveElement):
    """Defines an elevation element at a given position on the road reference line.

    Elements shall be defined in ascending order along the reference
    line. The s length does not change with the elevation.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar a: Polynom parameter a, elevation at @s (ds=0)
    :ivar b: Polynom parameter b
    :ivar c: Polynom parameter c
    :ivar d: Polynom parameter d
    :ivar s: s-coordinate of start position
    """

    class Meta:
        name = "t_road_elevationProfile_elevation"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    a: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    c: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    d: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )


@dataclass
class TRoadLanesLaneOffset(OpenDriveElement):
    """
    Lane offsets shift the center lane away from the road reference line.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar a: Polynom parameter a, offset at @s (ds=0)
    :ivar b: Polynom parameter b
    :ivar c: Polynom parameter c
    :ivar d: Polynom parameter d
    :ivar s: s-coordinate of start position
    """

    class Meta:
        name = "t_road_lanes_laneOffset"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    a: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    c: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    d: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )


@dataclass
class TRoadLanesLaneSectionLcrLaneLinkPredecessorSuccessor(OpenDriveElement):
    """
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: ID of the preceding / succeeding linked lane
    """

    class Meta:
        name = "t_road_lanes_laneSection_lcr_lane_link_predecessorSuccessor"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadLanesLaneSectionLcrLaneRoadMarkExplicitLine(OpenDriveElement):
    """
    Specifies a single line in an explicit road mark definition.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar length: Length of the visible line
    :ivar rule: Rule that must be observed when passing the line from
        inside, that is, from the lane with the lower absolute ID to the
        lane with the higher absolute ID
    :ivar s_offset: Offset of start position of the &lt;line&gt;
        element, relative to the @sOffset  given in the &lt;roadMark&gt;
        element
    :ivar t_offset: Lateral offset from the lane border. If &lt;sway&gt;
        element is present, the lateral offset follows the sway.
    :ivar width: Line width. This attribute supersedes the definition in
        the &lt;roadMark&gt; element.
    """

    class Meta:
        name = "t_road_lanes_laneSection_lcr_lane_roadMark_explicit_line"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
        },
    )
    rule: Optional[ERoadMarkRule] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    s_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "sOffset",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    t_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "tOffset",
            "type": "Attribute",
            "required": True,
        },
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )


@dataclass
class TRoadLanesLaneSectionLcrLaneRoadMarkSway(OpenDriveElement):
    """Relocates the lateral reference position for the following (explicit) type
    definition and thus defines an offset.

    The sway offset is relative to the nominal reference position of the
    lane marking, meaning the lane border.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar a: Polynom parameter a, sway value at @s (ds=0)
    :ivar b: Polynom parameter b
    :ivar c: Polynom parameter c
    :ivar d: Polynom parameter d
    :ivar ds: s-coordinate of start position of the &lt;sway&gt;
        element, relative to the @sOffset given in the &lt;roadMark&gt;
        element
    """

    class Meta:
        name = "t_road_lanes_laneSection_lcr_lane_roadMark_sway"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    a: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    c: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    d: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ds: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )


@dataclass
class TRoadLanesLaneSectionLcrLaneRoadMarkTypeLine(OpenDriveElement):
    """A road mark may consist of one or more elements.

    Multiple elements are usually positioned side-by-side. A line
    definition is valid for a given length of the lane and will be
    repeated automatically.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar color: Line color. If given, this attribute supersedes the
        definition in the &lt;roadMark&gt; element.
    :ivar length: Length of the visible part
    :ivar rule: Rule that must be observed when passing the line from
        inside, for example, from the lane with the lower absolute ID to
        the lane with the higher absolute ID
    :ivar s_offset: Initial longitudinal offset of the line definition
        from the start of the road mark definition
    :ivar space: Length of the gap between the visible parts
    :ivar t_offset: Lateral offset from the lane border. If &lt;sway&gt;
        element is present, the lateral offset follows the sway.
    :ivar width: Line width
    """

    class Meta:
        name = "t_road_lanes_laneSection_lcr_lane_roadMark_type_line"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    color: Optional[ERoadMarkColor] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    rule: Optional[ERoadMarkRule] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    s_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "sOffset",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    space: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    t_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "tOffset",
            "type": "Attribute",
            "required": True,
        },
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )


@dataclass
class TRoadLanesLaneSectionLrLaneAccessRestriction(OpenDriveElement):
    """Defines access restrictions for certain types of road users.

    Each restriction element defines one type that is either allowed or
    denied according to the parent access element.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar type_value: Identifier of the participant to whom the
        restriction applies
    """

    class Meta:
        name = "t_road_lanes_laneSection_lr_lane_access_restriction"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[EAccessRestrictionType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class TRoadLanesLaneSectionLrLaneBorder(OpenDriveElement):
    """Lane borders set the width of lanes.

    Lane borders describe the outer limits of lanes, independent of the
    parameters of their inner borders. In this case, inner lanes are
    defined as lanes which have the same sign for their ID as the lane
    currently defined, but with a smaller absolute value for their ID.
    Especially when road data is derived from automatic measurements,
    this type of definition is easier than specifying the lane width
    because it avoids creating many lane sections. Lane width and lane
    border elements are mutually exclusive within the same lane group.
    If both width and lane border elements are present for a lane
    section in the ASAM OpenDRIVE file, the application shall use the
    information from the &lt;width&gt; elements.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar a: Polynom parameter a, border position at @s (ds=0)
    :ivar b: Polynom parameter b
    :ivar c: Polynom parameter c
    :ivar d: Polynom parameter d
    :ivar s_offset: s-coordinate of start position of the &lt;border&gt;
        element , relative to the position of the preceding
        &lt;laneSection&gt; element
    """

    class Meta:
        name = "t_road_lanes_laneSection_lr_lane_border"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    a: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    c: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    d: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    s_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "sOffset",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )


@dataclass
class TRoadLanesLaneSectionLrLaneHeight(OpenDriveElement):
    """Lane heights elevate lanes along the h-coordinate within a lane section
    independent from the road elevation.

    Lane height is used to implement small-scale elevation such as
    raising pedestrian walkways. Lane height is specified as offset from
    the road (including elevation, superelevation, shape, cross section
    surface) in h-direction.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar inner: Inner offset from road level
    :ivar outer: Outer offset from road level
    :ivar s_offset: s-coordinate of start position, relative to the
        position of the preceding &lt;laneSection&gt; element
    """

    class Meta:
        name = "t_road_lanes_laneSection_lr_lane_height"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    inner: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    outer: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    s_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "sOffset",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )


@dataclass
class TRoadLanesLaneSectionLrLaneMaterial(OpenDriveElement):
    """Stores information about the material of lanes.

    Each element is valid until a new element is defined. If multiple
    elements are defined, they must be listed in ascending order.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar friction: Friction coefficient
    :ivar roughness: Roughness, for example, for sound and motion
        systems
    :ivar s_offset: s-coordinate of start position, relative to the
        position of the preceding &lt;laneSection&gt; element
    :ivar surface: Surface material code, depending on application
    """

    class Meta:
        name = "t_road_lanes_laneSection_lr_lane_material"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    friction: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    roughness: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    s_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "sOffset",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    surface: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TRoadLanesLaneSectionLrLaneRule(OpenDriveElement):
    """
    Used to add rules that are not covered by any of the other lane attributes that
    are described in this specification.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar s_offset: s-coordinate of start position, relative to the
        position of the preceding &lt;laneSection&gt; element
    :ivar value: Free text; currently recommended values are "no
        stopping at any time" "disabled parking" "car pool"
    """

    class Meta:
        name = "t_road_lanes_laneSection_lr_lane_rule"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    s_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "sOffset",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadLanesLaneSectionLrLaneSpeed(OpenDriveElement):
    """Defines the maximum allowed speed on a given lane.

    Each element is valid in direction of the increasing s-coordinate
    until a new element is defined.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar max: Maximum allowed speed. If the attribute unit is not
        specified, m/s is used as default.
    :ivar s_offset: s-coordinate of start position, relative to the
        position of the preceding &lt;laneSection&gt; element
    :ivar unit: Unit of the attribute max
    """

    class Meta:
        name = "t_road_lanes_laneSection_lr_lane_speed"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    max: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    s_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "sOffset",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    unit: Optional[EUnitSpeed] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TRoadLanesLaneSectionLrLaneWidth(OpenDriveElement):
    """Lane widths widen or narrow lanes along the t-coordinate within lane
    sections.

    Lane width and lane border elements are mutually exclusive within
    the same lane group. If both width and lane border elements are
    present for a lane section in the ASAM OpenDRIVE file, the
    application must use the information from the &lt;width&gt;
    elements.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar a: Polynom parameter a, width at @s (ds=0)
    :ivar b: Polynom parameter b
    :ivar c: Polynom parameter c
    :ivar d: Polynom parameter d
    :ivar s_offset: s-coordinate of start position of the &lt;width&gt;
        element, relative to the position of the preceding
        &lt;laneSection&gt; element
    """

    class Meta:
        name = "t_road_lanes_laneSection_lr_lane_width"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    a: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    c: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    d: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    s_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "sOffset",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )


@dataclass
class TRoadLateralProfileCrossSectionSurfaceCoefficients(OpenDriveElement):
    """Defines the coefficients of a cubic polynomial in s-direction.

    The first &lt;coefficients&gt; element shall start at the beginning
    of the road reference line with @s="0".

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar a: Polynomial parameter a. If the attribute is not specified,
        the value is 0.
    :ivar b: Polynomial parameter b. If the attribute is not specified,
        the value is 0.
    :ivar c: Polynomial parameter c. If the attribute is not specified,
        the value is 0.
    :ivar d: Polynomial parameter d. If the attribute is not specified,
        the value is 0.
    :ivar s: s-coordinate of start position
    """

    class Meta:
        name = "t_road_lateralProfile_crossSectionSurface_coefficients"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    a: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    c: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    d: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )


@dataclass
class TRoadLateralProfileShape(OpenDriveElement):
    """Defined as the road section’s surface relative to the reference plane.

    There may be several shape definitions at one s-position that have
    different t-values, thereby describing the curvy shape of the road.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar a: Polynom parameter a, relative height at @t (dt=0)
    :ivar b: Polynom parameter b
    :ivar c: Polynom parameter c
    :ivar d: Polynom parameter d
    :ivar s: s-coordinate of start position
    :ivar t: t-coordinate of start position
    """

    class Meta:
        name = "t_road_lateralProfile_shape"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    a: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    c: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    d: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    t: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadLateralProfileSuperelevation(OpenDriveElement):
    """Superelevation specifies the transverse slope along the road reference line.

    Superelevation is constant in each cross section and can vary in
    road reference line direction. Elements must be defined in ascending
    order along the reference line. The parameters of an element are
    valid until the next element starts or the road reference line ends.
    Per default, the superelevation of a road is zero.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar a: Polynom parameter a, superelevation at @s (ds=0)
    :ivar b: Polynom parameter b
    :ivar c: Polynom parameter c
    :ivar d: Polynom parameter d
    :ivar s: s-coordinate of start position
    """

    class Meta:
        name = "t_road_lateralProfile_superelevation"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    a: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    c: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    d: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )


@dataclass
class TRoadLinkPredecessorSuccessor(OpenDriveElement):
    """Successors and predecessors can be junctions or roads.

    For each, different attribute sets shall be used.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar contact_point: Contact point of link on the linked element
    :ivar element_dir: To be provided when elementS is used for the
        connection definition. Indicates the direction on the
        predecessor from which the road is entered.
    :ivar element_id: ID of the linked element
    :ivar element_s: Alternative to contactPoint for virtual junctions.
        Indicates a connection within the predecessor, meaning not at
        the start or end of the predecessor. Shall only be used for
        elementType "road"
    :ivar element_type: Type of the linked element
    """

    class Meta:
        name = "t_road_link_predecessorSuccessor"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    contact_point: Optional[EContactPoint] = field(
        default=None,
        metadata={
            "name": "contactPoint",
            "type": "Attribute",
        },
    )
    element_dir: Optional[EElementDir] = field(
        default=None,
        metadata={
            "name": "elementDir",
            "type": "Attribute",
        },
    )
    element_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "elementId",
            "type": "Attribute",
            "required": True,
        },
    )
    element_s: Optional[float] = field(
        default=None,
        metadata={
            "name": "elementS",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    element_type: Optional[ERoadLinkElementType] = field(
        default=None,
        metadata={
            "name": "elementType",
            "type": "Attribute",
        },
    )


@dataclass
class TRoadObjectsObjectLaneValidity(OpenDriveElement):
    """
    Lane validities restrict signals and objects to specific lanes.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar from_lane: Minimum ID of the lanes for which the object is
        valid
    :ivar to_lane: Maximum ID of the lanes for which the object is valid
    """

    class Meta:
        name = "t_road_objects_object_laneValidity"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    from_lane: Optional[int] = field(
        default=None,
        metadata={
            "name": "fromLane",
            "type": "Attribute",
            "required": True,
        },
    )
    to_lane: Optional[int] = field(
        default=None,
        metadata={
            "name": "toLane",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadObjectsObjectMarkingsMarkingCornerReference(OpenDriveElement):
    """
    Specifies a point by referencing an existing outline point.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: Identifier of the referenced outline point
    """

    class Meta:
        name = "t_road_objects_object_markings_marking_cornerReference"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadObjectsObjectMaterial(OpenDriveElement):
    """Describes the material properties of objects, for example, patches that are
    part of the road surface but deviate from the standard road material.

    Supersedes the material specified in the &lt;road material&gt;
    element and is valid only within the outline of the parent road
    object.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar friction: Friction value, depending on application
    :ivar road_mark_color: Color of the painted road mark.
    :ivar roughness: Roughness, for example, for sound and motion
        systems, depending on application
    :ivar surface: Surface material code, depending on application
    """

    class Meta:
        name = "t_road_objects_object_material"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    friction: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    road_mark_color: Optional[ERoadMarkColor] = field(
        default=None,
        metadata={
            "name": "roadMarkColor",
            "type": "Attribute",
        },
    )
    roughness: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    surface: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TRoadObjectsObjectOutlinesOutlineCornerLocal(OpenDriveElement):
    """Used to describe complex forms of objects.

    Defines a corner point on the object outline relative to the object
    pivot point in local u/v-coordinates. The insertion point and the
    orientation of the object are given by the @s, @t, @zOffset and @hdg
    attributes of the  element.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar height: Height of the object at this corner, along the z-axis
    :ivar id: ID of the outline point. Shall be unique within one
        outline.
    :ivar u: Local u-coordinate of the corner
    :ivar v: Local v-coordinate of the corner
    :ivar z: Local z-coordinate of the corner
    """

    class Meta:
        name = "t_road_objects_object_outlines_outline_cornerLocal"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    height: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    u: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    v: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    z: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadObjectsObjectOutlinesOutlineCornerRoad(OpenDriveElement):
    """
    Defines a corner point on the object’s outline in road coordinates.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar dz: dz of the corner relative to road reference line
    :ivar height: Height of the object at this corner, along the z-axis
    :ivar id: ID of the outline point. Must be unique within one outline
    :ivar s: s-coordinate of the corner
    :ivar t: t-coordinate of the corner
    """

    class Meta:
        name = "t_road_objects_object_outlines_outline_cornerRoad"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    dz: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    height: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    t: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadObjectsObjectParkingSpace(OpenDriveElement):
    """
    Details for a parking space may be added to the &lt;object&gt; element.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar access: Access definitions for the parking space. Parking
        spaces tagged with "women" and "handicapped" are vehicles of
        type car.
    :ivar restrictions: Free text, depending on application
    """

    class Meta:
        name = "t_road_objects_object_parkingSpace"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    access: Optional[ERoadObjectsObjectParkingSpaceAccess] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    restrictions: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TRoadObjectsObjectRepeat(OpenDriveElement):
    """To avoid lengthy XML code, objects of the same type may be repeated.

    Attributes of the repeated object shall overrule the attributes from
    the original object. If attributes are omitted in the repeated
    objects, the attributes from the original object apply.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar detach_from_reference_line: If true, the start and end
        positions are connected as a straight line which does not follow
        the road reference line. The default is false
    :ivar distance: Distance between two instances of the object; If
        this value is zero, then the object is treated like a continuous
        feature, for example, a guard rail, a wall, etc.
    :ivar height_end: Height of the object at @s + @length
    :ivar height_start: Height of the object at @s
    :ivar length: Length of the repeat area, along the road reference
        line in s-direction.
    :ivar length_end: Length of the object at @s + @length
    :ivar length_start: Length of the object at @s
    :ivar radius_end: Radius of the object at @s + @length
    :ivar radius_start: Radius of the object at @s
    :ivar s: s-coordinate of start position, overrides the corresponding
        argument in the original &lt;object&gt; record
    :ivar t_end: Lateral offset of object's reference point at @s +
        @length
    :ivar t_start: Lateral offset of objects reference point at @s
    :ivar width_end: Width of the object at @s + @length
    :ivar width_start: Width of the object at @s
    :ivar z_offset_end: z-offset of the object at @s + @length, relative
        to the elevation of the road reference line
    :ivar z_offset_start: z-offset of the object at @s, relative to the
        elevation of the road reference line
    """

    class Meta:
        name = "t_road_objects_object_repeat"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    detach_from_reference_line: Optional[TBool] = field(
        default=None,
        metadata={
            "name": "detachFromReferenceLine",
            "type": "Attribute",
        },
    )
    distance: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    height_end: Optional[float] = field(
        default=None,
        metadata={
            "name": "heightEnd",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    height_start: Optional[float] = field(
        default=None,
        metadata={
            "name": "heightStart",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    length_end: Optional[float] = field(
        default=None,
        metadata={
            "name": "lengthEnd",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    length_start: Optional[float] = field(
        default=None,
        metadata={
            "name": "lengthStart",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    radius_end: Optional[float] = field(
        default=None,
        metadata={
            "name": "radiusEnd",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    radius_start: Optional[float] = field(
        default=None,
        metadata={
            "name": "radiusStart",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    t_end: Optional[float] = field(
        default=None,
        metadata={
            "name": "tEnd",
            "type": "Attribute",
            "required": True,
        },
    )
    t_start: Optional[float] = field(
        default=None,
        metadata={
            "name": "tStart",
            "type": "Attribute",
            "required": True,
        },
    )
    width_end: Optional[float] = field(
        default=None,
        metadata={
            "name": "widthEnd",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    width_start: Optional[float] = field(
        default=None,
        metadata={
            "name": "widthStart",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    z_offset_end: Optional[float] = field(
        default=None,
        metadata={
            "name": "zOffsetEnd",
            "type": "Attribute",
            "required": True,
        },
    )
    z_offset_start: Optional[float] = field(
        default=None,
        metadata={
            "name": "zOffsetStart",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadObjectsObjectSkeletonPolylineVertexLocal:
    """Defines a vertex point on the object polyline relative to the object pivot
    point in local u/v-coordinates.

    The insertion point and the orientation of the object are given by
    the @s, @t, @zOffset and @hdg attributes of the element.
    &lt;vertexLocal&gt; can use either radius or length/width within one
    &lt;polyline&gt; element.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: ID of the vertex point. Must be unique within one
        polyline.
    :ivar intersection_point: Vertex point is intersecting the ground.
        "false" is used as default.
    :ivar radius: Local radius of the object at this vertex point, along
        the polyline
    :ivar u: Local u-coordinate of the vertex point
    :ivar v: Local v-coordinate of the vertex point
    :ivar z: Local z-coordinate of the vertex point
    """

    class Meta:
        name = "t_road_objects_object_skeleton_polyline_vertexLocal"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    intersection_point: Optional[TBool] = field(
        default=None,
        metadata={
            "name": "intersectionPoint",
            "type": "Attribute",
        },
    )
    radius: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    u: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    v: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    z: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TRoadObjectsObjectSkeletonPolylineVertexRoad:
    """Defines a point on the object’s polyline in road coordinates.

    &lt;vertexRoad&gt; can use either radius or length/width within one
    &lt;polyline&gt; element.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar dz: dz of the polyline point relative to road reference line
        parallel to z.
    :ivar id: ID of the vertex point. Must be unique within one
        polyline.
    :ivar intersection_point: Vertex point is intersecting the ground.
        "false" is used as default.
    :ivar radius: Local radius of the object at this vertex point, along
        the polyline
    :ivar s: s-coordinate of the corner
    :ivar t: t-coordinate of the corner
    """

    class Meta:
        name = "t_road_objects_object_skeleton_polyline_vertexRoad"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    dz: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    intersection_point: Optional[TBool] = field(
        default=None,
        metadata={
            "name": "intersectionPoint",
            "type": "Attribute",
        },
    )
    radius: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    t: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TRoadObjectsObjectSurfaceCrg(OpenDriveElement):
    """
    Elevation data described in {GLO_VAR_STA_ASAM_OpenCRG} are represented by the
    &lt;CRG&gt; element within the &lt;surface&gt; element.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar file: Name of the file containing the CRG data.
    :ivar hide_road_surface_crg: Determines if the object CRG hides the
        road surface CRG. Default is true.
    :ivar z_scale: z-scale factor for the surface description (default =
        1.0).
    """

    class Meta:
        name = "t_road_objects_object_surface_CRG"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    file: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    hide_road_surface_crg: Optional[TBool] = field(
        default=None,
        metadata={
            "name": "hideRoadSurfaceCRG",
            "type": "Attribute",
        },
    )
    z_scale: Optional[float] = field(
        default=None,
        metadata={
            "name": "zScale",
            "type": "Attribute",
        },
    )


@dataclass
class TRoadPlanViewGeometryArc(OpenDriveElement):
    """
    Arcs describe road reference lines with constant curvature.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar curvature: Constant curvature throughout the element. Positive
        curvature: left curve (counter-clockwise motion) Negative
        curvature: right curve (clockwise motion)
    """

    class Meta:
        name = "t_road_planView_geometry_arc"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    curvature: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadPlanViewGeometryLine(OpenDriveElement):
    """A straight line is the simplest geometry element.

    It contains no further attributes.
    """

    class Meta:
        name = "t_road_planView_geometry_line"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadPlanViewGeometryParamPoly3(OpenDriveElement):
    """
    A parametric cubic curve describing the road reference line.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar a_u: Polynom parameter a for u
    :ivar a_v: Polynom parameter a for v
    :ivar b_u: Polynom parameter b for u
    :ivar b_v: Polynom parameter b for v
    :ivar c_u: Polynom parameter c for u
    :ivar c_v: Polynom parameter c for v
    :ivar d_u: Polynom parameter d for u
    :ivar d_v: Polynom parameter d for v
    :ivar p_range: Range of parameter p. - Case arcLength: p in [0,
        @length of &lt;geometry&gt;] - Case normalized: p in [0, 1]
        (Values of polynom paremeters have no unit)
    """

    class Meta:
        name = "t_road_planView_geometry_paramPoly3"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    a_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "aU",
            "type": "Attribute",
            "required": True,
        },
    )
    a_v: Optional[float] = field(
        default=None,
        metadata={
            "name": "aV",
            "type": "Attribute",
            "required": True,
        },
    )
    b_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "bU",
            "type": "Attribute",
            "required": True,
        },
    )
    b_v: Optional[float] = field(
        default=None,
        metadata={
            "name": "bV",
            "type": "Attribute",
            "required": True,
        },
    )
    c_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "cU",
            "type": "Attribute",
            "required": True,
        },
    )
    c_v: Optional[float] = field(
        default=None,
        metadata={
            "name": "cV",
            "type": "Attribute",
            "required": True,
        },
    )
    d_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "dU",
            "type": "Attribute",
            "required": True,
        },
    )
    d_v: Optional[float] = field(
        default=None,
        metadata={
            "name": "dV",
            "type": "Attribute",
            "required": True,
        },
    )
    p_range: Optional[EParamPoly3PRange] = field(
        default=None,
        metadata={
            "name": "pRange",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadPlanViewGeometryPoly3(OpenDriveElement):
    """
    A cubic polynom describing the road reference line.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar a: Polynom parameter a
    :ivar b: Polynom parameter b
    :ivar c: Polynom parameter c
    :ivar d: Polynom parameter d
    """

    class Meta:
        name = "t_road_planView_geometry_poly3"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    a: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    c: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    d: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadPlanViewGeometrySpiral(OpenDriveElement):
    """Spirals or more specifically Euler spirals also known as clothoids.

    They describe road reference lines with constantly changing
    curvatures.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar curv_end: Curvature at the end of the element. Positive
        curvature: left curve (counter-clockwise motion) Negative
        curvature: right curve (clockwise motion)
    :ivar curv_start: Curvature at the start of the element. Positive
        curvature: left curve (counter-clockwise motion) Negative
        curvature: right curve (clockwise motion)
    """

    class Meta:
        name = "t_road_planView_geometry_spiral"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    curv_end: Optional[float] = field(
        default=None,
        metadata={
            "name": "curvEnd",
            "type": "Attribute",
            "required": True,
        },
    )
    curv_start: Optional[float] = field(
        default=None,
        metadata={
            "name": "curvStart",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadRailroadSwitchMainTrack(OpenDriveElement):
    """
    Main tracks form the primary course for rail bound traffic.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar dir: direction, relative to the s-direction, on the main track
        for entering the side track via the switch
    :ivar id: Unique ID of the main track, that is, the &lt;road&gt;
        element. Must be consistent with parent containing this
        &lt;railroad&gt; element.
    :ivar s: s-coordinate of the switch, that is, the point where main
        track and side track meet
    """

    class Meta:
        name = "t_road_railroad_switch_mainTrack"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    dir: Optional[EElementDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )


@dataclass
class TRoadRailroadSwitchPartner(OpenDriveElement):
    """
    Partner switches are two consistently set switches linked by a side track.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: Unique ID of the partner switch
    :ivar name: Unique name of the partner switch
    """

    class Meta:
        name = "t_road_railroad_switch_partner"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TRoadRailroadSwitchSideTrack(OpenDriveElement):
    """
    Side tracks connect two switches that are placed on main tracks.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar dir: direction, relative to the s-direction, on the side track
        for after entering it via the switch
    :ivar id: Unique ID of the side track, that is, the &lt;road&gt;
        element
    :ivar s: s-coordinate of the switch on the side track
    """

    class Meta:
        name = "t_road_railroad_switch_sideTrack"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    dir: Optional[EElementDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )


@dataclass
class TRoadSignalsDisplayArea(OpenDriveElement):
    """A display area is the recommended position of the signal to be visualized in
    the simulation.

    A display area is specified in the `&lt;displayArea&gt;` element. A
    `&lt;displayArea&gt;` element is defined in the local coordinate
    system of the `&lt;signal&gt;` element. The @index attribute can be
    used in ASAM OpenSCENARIO to reference the display area. In ASAM
    OpenSCENARIO a different local display area position may be
    specified.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar height: Height of the &lt;displayArea&gt;
    :ivar index: Index of the &lt;displayArea&gt;
    :ivar v: Local v-coordinate of the &lt;displayArea&gt; on the board
    :ivar width: Width of the &lt;displayArea&gt;
    :ivar z: Local z-coordinate of the &lt;displayArea&gt; on the board
    """

    class Meta:
        name = "t_road_signals_displayArea"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    v: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    z: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TRoadSignalsSignalDependency(OpenDriveElement):
    """Signal dependencies limit or extend the validity of one signal by an
    additional signal.

    For example, a speed limit sign of 60 km/h that is only valid for
    trucks, specified by a supplementary sign. One signal may have
    multiple dependencies.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: ID of the controlling signal
    :ivar type_value: Type of the dependency, Free text, depending on
        application
    """

    class Meta:
        name = "t_road_signals_signal_dependency"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class TRoadSignalsSignalPositionInertial(OpenDriveElement):
    """Describes the reference point of the physical position in inertial
    coordinates in cases where it deviates from the logical position.

    Defines the inertial position.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar hdg: Heading of the signal, relative to the inertial system
    :ivar pitch: Pitch angle of the signal after applying heading,
        relative to the inertial system (x’y’-plane)
    :ivar roll: Roll angle of the signal after applying heading and
        pitch, relative to the inertial system (x’’y’’-plane)
    :ivar x: x-coordinate
    :ivar y: y-coordinate
    :ivar z: z-coordinate
    """

    class Meta:
        name = "t_road_signals_signal_positionInertial"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    hdg: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    pitch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    roll: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    z: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadSignalsSignalPositionRoad(OpenDriveElement):
    """Describes the reference point of the physical position road coordinates in
    cases where it deviates from the logical position.

    Defines the position on the road.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar h_offset: Heading offset of the signal (relative to
        @orientation)
    :ivar pitch: Pitch angle of the signal after applying hOffset,
        relative to the inertial system (x’y’-plane)
    :ivar road_id: Unique ID of the referenced road
    :ivar roll: Roll angle of the signal after applying hOffset and
        pitch, relative to the inertial system (x’’y’’-plane)
    :ivar s: s-coordinate
    :ivar t: t-coordinate
    :ivar z_offset: z offset from road level to bottom edge of the
        signal
    """

    class Meta:
        name = "t_road_signals_signal_positionRoad"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    h_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "hOffset",
            "type": "Attribute",
            "required": True,
        },
    )
    pitch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    road_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadId",
            "type": "Attribute",
            "required": True,
        },
    )
    roll: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    t: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    z_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "zOffset",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadSignalsSignalReference2(OpenDriveElement):
    """Signal references link a signal to another signal or object.

    One signal may have multiple signal references. The signal reference
    term should not to be confused with the `&lt;signalReference&gt;`
    element that is used to link a signal to multiple roads.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar element_id: Unique ID of the linked element
    :ivar element_type: Type of the linked element
    :ivar type_value: Type of the linkage Free text, depending on
        application
    """

    class Meta:
        name = "t_road_signals_signal_reference"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    element_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "elementId",
            "type": "Attribute",
            "required": True,
        },
    )
    element_type: Optional[ERoadSignalsSignalReferenceElementType] = field(
        default=None,
        metadata={
            "name": "elementType",
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class TRoadSurfaceCrg(OpenDriveElement):
    """
    Links road surface data defined according to ASAM OpenCRG format.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar file: Name of the file containing the CRG data
    :ivar h_offset: Heading offset between CRG center line and reference
        line of the road (only allowed for mode genuine, default = 0.0).
    :ivar mode: Attachment mode for the surface data, see specification.
    :ivar orientation: Orientation of the CRG data set relative to the
        parent &lt;road&gt; element. Only allowed for mode attached and
        attached0.
    :ivar purpose: Physical purpose of the data contained in the CRG
        file; if the attribute is missing, data will be interpreted as
        elevation data.
    :ivar s_end: End of the application of CRG (s-coordinate)
    :ivar s_offset: s-offset between CRG center line and reference line
        of the road (default = 0.0)
    :ivar s_start: Start of the application of CRG data (s-coordinate)
    :ivar t_offset: t-offset between CRG center line and reference line
        of the road (default = 0.0)
    :ivar z_offset: z-offset between CRG center line and reference line
        of the road (default = 0.0). Only allowed for purpose elevation.
    :ivar z_scale: z-scale factor for the surface description (default =
        1.0). Only allowed for purpose elevation.
    """

    class Meta:
        name = "t_road_surface_CRG"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    file: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    h_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "hOffset",
            "type": "Attribute",
        },
    )
    mode: Optional[ERoadSurfaceCrgMode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    orientation: Optional[EDirection] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    purpose: Optional[ERoadSurfaceCrgPurpose] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    s_end: Optional[float] = field(
        default=None,
        metadata={
            "name": "sEnd",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    s_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "sOffset",
            "type": "Attribute",
        },
    )
    s_start: Optional[float] = field(
        default=None,
        metadata={
            "name": "sStart",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    t_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "tOffset",
            "type": "Attribute",
        },
    )
    z_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "zOffset",
            "type": "Attribute",
        },
    )
    z_scale: Optional[float] = field(
        default=None,
        metadata={
            "name": "zScale",
            "type": "Attribute",
        },
    )


@dataclass
class TRoadTypeSpeed(OpenDriveElement):
    """
    Defines the default maximum speed allowed in conjunction with the specified
    road type.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar max: Maximum allowed speed. Given as string (only "no limit" /
        "undefined") or numerical value in the respective unit (see
        attribute unit). If the attribute unit is not specified, m/s is
        used as default.
    :ivar unit: Unit of the attribute max. For values, see chapter
        “units”.
    """

    class Meta:
        name = "t_road_type_speed"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    max: Optional[Union[float, EMaxSpeedString]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    unit: Optional[EUnitSpeed] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TSignalGroupVmsBoardReference(OpenDriveElement):
    """
    Variable message board references list all variable message boards that belong
    to the same gantry.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar group_index: groupIndex the index of the grouped boards shall
        be unique within the &lt;vmsGroup&gt;
    :ivar signal_id: Id of the signal that has a &lt;vmsBoard&gt;
        assigned
    :ivar vms_index: vmsIndex, the index of the &lt;vmsBoard&gt;
    """

    class Meta:
        name = "t_signalGroup_vmsBoardReference"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    group_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "groupIndex",
            "type": "Attribute",
        },
    )
    signal_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "signalId",
            "type": "Attribute",
        },
    )
    vms_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "vmsIndex",
            "type": "Attribute",
        },
    )


@dataclass
class TSignalsSemanticsLane(OpenDriveElement):
    """
    Specifies lane regulations.
    """

    class Meta:
        name = "t_signals_semantics_lane"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[ESignalsSemanticsLane] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class TSignalsSemanticsParking(OpenDriveElement):
    """
    Specifies parking regulations.
    """

    class Meta:
        name = "t_signals_semantics_parking"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TSignalsSemanticsPriority(OpenDriveElement):
    """
    Specifies priority regulations.
    """

    class Meta:
        name = "t_signals_semantics_priority"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[ESignalsSemanticsPriority] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class TSignalsSemanticsProhibited(OpenDriveElement):
    """Specifies that certain types of traffic participants are not allowed to
    enter.

    Signal semantics for traffic participants in {THIS_STANDARD} are
    currently not defined because traffic participants are not
    harmonized for all standards.
    """

    class Meta:
        name = "t_signals_semantics_prohibited"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TSignalsSemanticsRouting(OpenDriveElement):
    """
    Specifies routing information.
    """

    class Meta:
        name = "t_signals_semantics_routing"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TSignalsSemanticsSpeed(OpenDriveElement):
    """
    Specifies speed regulations.
    """

    class Meta:
        name = "t_signals_semantics_speed"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[ESignalsSemanticsSpeed] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    unit: Optional[EUnitSpeed] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TSignalsSemanticsStreetname(OpenDriveElement):
    """
    Specifies the name of a street.
    """

    class Meta:
        name = "t_signals_semantics_streetname"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TSignalsSemanticsSupplementaryAllows(OpenDriveElement):
    """This signal semantic has no meaning on its own.

    It specifies the type of the traffic participant an exception is
    made for. Signal semantics for traffic participants in
    {THIS_STANDARD} are currently not specified because traffic
    participants are not harmonized for all standards.
    """

    class Meta:
        name = "t_signals_semantics_supplementaryAllows"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TSignalsSemanticsSupplementaryDistance(OpenDriveElement):
    """This signal semantic has no meaning on its own.

    It specifies the distance after a sign becomes valid or the range in
    which the sign is valid.
    """

    class Meta:
        name = "t_signals_semantics_supplementaryDistance"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[ESignalsSemanticsSupplementaryDistance] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    unit: Optional[EUnitDistance] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TSignalsSemanticsSupplementaryEnvironment(OpenDriveElement):
    """This signal semantic has no meaning on its own.

    It specifies under which environmental conditions a sign is valid.
    """

    class Meta:
        name = "t_signals_semantics_supplementaryEnvironment"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[ESignalsSemanticsSupplementaryEnvironment] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class TSignalsSemanticsSupplementaryExplanatory(OpenDriveElement):
    """This signal semantic has no meaning on its own.

    It specifies explanations for a sign.
    """

    class Meta:
        name = "t_signals_semantics_supplementaryExplanatory"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TSignalsSemanticsSupplementaryProhibits(OpenDriveElement):
    """This signal semantic has no meaning on its own.

    It specifies the type of the traffic participant a restriction is
    made for. Signal semantics for traffic participants in
    {THIS_STANDARD} are currently not specified because traffic
    participants are not harmonized for all standards.
    """

    class Meta:
        name = "t_signals_semantics_supplementaryProhibits"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TSignalsSemanticsSupplementaryTime(OpenDriveElement):
    """This signal semantic has no meaning on its own.

    It specifies the time or date a sign is valid.
    """

    class Meta:
        name = "t_signals_semantics_supplementaryTime"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[ESignalsSemanticsSupplementaryTime] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TSignalsSemanticsTourist(OpenDriveElement):
    """
    Specifies tourist information.
    """

    class Meta:
        name = "t_signals_semantics_tourist"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TSignalsSemanticsWarning(OpenDriveElement):
    """
    Specifies warnings for traffic participant.
    """

    class Meta:
        name = "t_signals_semantics_warning"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TStationPlatformSegment(OpenDriveElement):
    """Segments are parts of platforms.

    Each &lt;platform&gt; element is valid on one or more track
    segments. The &lt;segment&gt; element must be specified.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar road_id: Unique ID of the &lt;road&gt; element (track) that
        accompanies the platform
    :ivar s_end: Maximum s-coordiante on &lt;road&gt; element that has
        an adjacent platform
    :ivar side: Side of track on which the platform is situated when
        going from sStart to sEnd
    :ivar s_start: Minimum s-coordinate on &lt;road&gt; element that has
        an adjacent platform
    """

    class Meta:
        name = "t_station_platform_segment"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    road_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadId",
            "type": "Attribute",
            "required": True,
        },
    )
    s_end: Optional[float] = field(
        default=None,
        metadata={
            "name": "sEnd",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    side: Optional[EStationPlatformSegmentSide] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    s_start: Optional[float] = field(
        default=None,
        metadata={
            "name": "sStart",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )


@dataclass
class TController(OpenDriveElement):
    """Controllers provide a signal program for a traffic signal or a signal group.

    The mapping of traffic signals to a signal group is done in
    t_controller. Dynamic content like the signal program itself is
    specified outside of this standard (i.e. in OpenSCENARIO).

    :ivar control:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: Unique ID within database
    :ivar name: Name of the controller. May be chosen freely.
    :ivar sequence: Sequence number (priority) of this controller with
        respect to other controllers of same logical level
    """

    class Meta:
        name = "t_controller"

    control: List[TControllerControl] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sequence: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TJunctionGroup(OpenDriveElement):
    """Junction groups indicate for routing that the grouped junctions belong to
    the same node and are commonly seen as one big junction, for example
    roundabouts or highway interchanges.

    The &lt;junctionGroup&gt; element is split into a header element and
    a series of member elements.

    :ivar junction_reference:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: Unique ID within database
    :ivar name: Name of the junction group. May be chosen freely.
    :ivar type_value: Type of junction group
    """

    class Meta:
        name = "t_junctionGroup"

    junction_reference: List[TJunctionGroupJunctionReference] = field(
        default_factory=list,
        metadata={
            "name": "junctionReference",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[EJunctionGroupType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TJunctionBoundarySegmentJoint(TJunctionBoundarySegment):
    """
    A segment element with @type="joint" is perpendicular to the start or end of
    the given road.

    :ivar contact_point: Contact point on the road
    :ivar joint_lane_end: ID of the lane crossed by the segment. If
        missing all lanes are crossed by the segment.
    :ivar joint_lane_start: ID of the lane crossed by the segment. If
        missing all lanes are crossed by the segment.
    :ivar transition_length: Length of the transition area where local
        height is interpolated between road data and the
        &lt;elevationGrid&gt; in order to ensure a smooth transition.
        The default is 0.
    :ivar type_value: Type of the segment
    """

    class Meta:
        name = "t_junction_boundary_segment_joint"

    contact_point: Optional[Union[float, EContactPoint]] = field(
        default=None,
        metadata={
            "name": "contactPoint",
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )
    joint_lane_end: Optional[int] = field(
        default=None,
        metadata={
            "name": "jointLaneEnd",
            "type": "Attribute",
        },
    )
    joint_lane_start: Optional[int] = field(
        default=None,
        metadata={
            "name": "jointLaneStart",
            "type": "Attribute",
        },
    )
    transition_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "transitionLength",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    type_value: Optional[EJunctionSegmentType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class TJunctionBoundarySegmentLane(TJunctionBoundarySegment):
    """A segment element with @type="lane" goes along @boundaryLane for the given s
    range.

    It is the outmost edge of the lane  relative to the center of the
    junction.

    :ivar boundary_lane: ID of the lane of which the outer edge is the
        segment
    :ivar s_end: End of the segment (s-coordinate, begin, end)
    :ivar s_start: Start of the segment (s-coordinate, begin, end)
    :ivar type_value: Type of the segment
    """

    class Meta:
        name = "t_junction_boundary_segment_lane"

    boundary_lane: Optional[int] = field(
        default=None,
        metadata={
            "name": "boundaryLane",
            "type": "Attribute",
        },
    )
    s_end: Optional[Union[float, EContactPoint]] = field(
        default=None,
        metadata={
            "name": "sEnd",
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )
    s_start: Optional[Union[float, EContactPoint]] = field(
        default=None,
        metadata={
            "name": "sStart",
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )
    type_value: Optional[EJunctionSegmentType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class TJunctionConnection(OpenDriveElement):
    """
    Provides information about a single connection within a junction.

    :ivar lane_link:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar contact_point: Contact point on the @connectingRoad or
        @linkedRoad. Required for all junction types except virtual.
    :ivar id: Unique ID within the junction
    :ivar incoming_road: ID of the incoming road. Required for all
        junction types except virtual.
    """

    class Meta:
        name = "t_junction_connection"

    lane_link: List[TJunctionConnectionLaneLink] = field(
        default_factory=list,
        metadata={
            "name": "laneLink",
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    contact_point: Optional[EContactPoint] = field(
        default=None,
        metadata={
            "name": "contactPoint",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    incoming_road: Optional[str] = field(
        default=None,
        metadata={
            "name": "incomingRoad",
            "type": "Attribute",
        },
    )


@dataclass
class TJunctionCrossPath:
    """Cross paths are intended for pedestrian crossings and are junctions elements
    where traffic of a lane can cross other lanes and continue on a different lane
    of the same or a different road.

    The cross path itself is a separate road.

    :ivar start_lane_link:
    :ivar end_lane_link:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar crossing_road: ID of road defining the cross path.
    :ivar id: Unique ID within the junction
    :ivar road_at_end: ID of road at end point of the crossing road
    :ivar road_at_start: ID of road at start point of the crossing road
    """

    class Meta:
        name = "t_junction_crossPath"

    start_lane_link: Optional[TJunctionCrossPathLaneLink] = field(
        default=None,
        metadata={
            "name": "startLaneLink",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    end_lane_link: Optional[TJunctionCrossPathLaneLink] = field(
        default=None,
        metadata={
            "name": "endLaneLink",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    crossing_road: Optional[str] = field(
        default=None,
        metadata={
            "name": "crossingRoad",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    road_at_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadAtEnd",
            "type": "Attribute",
        },
    )
    road_at_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadAtStart",
            "type": "Attribute",
        },
    )


@dataclass
class TJunctionElevationGrid(OpenDriveElement):
    """An elevation grid is a coarse square grid with z-values at evenly spaced
    points.

    Elevation grids do not replace OpenCRG.
    """

    class Meta:
        name = "t_junction_elevationGrid"

    elevation: List[TJunctionElevationGridElevation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    grid_spacing: Optional[str] = field(
        default=None,
        metadata={
            "name": "gridSpacing",
            "type": "Attribute",
        },
    )
    s_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "sStart",
            "type": "Attribute",
        },
    )


@dataclass
class TRoadElevationProfile(OpenDriveElement):
    """
    Road elevation specifies the elevation along the road reference line, that is
    in s-direction.
    """

    class Meta:
        name = "t_road_elevationProfile"

    elevation: List[TRoadElevationProfileElevation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadLanesLaneSectionLcrLaneLink(OpenDriveElement):
    """For links between lanes with an identical road reference line, the lane
    predecessor and successor information provide the IDs of lanes on the preceding
    or following lane section.

    For links between lanes with different road reference line,  the
    lane predecessor and successor information provide the IDs of lanes
    on the first or last lane section of the other road reference line
    depending on the contact point of the road linkage. This element may
    only be omitted, if lanes end at a junction or have no physical
    link.
    """

    class Meta:
        name = "t_road_lanes_laneSection_lcr_lane_link"

    predecessor: List[TRoadLanesLaneSectionLcrLaneLinkPredecessorSuccessor] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
    )
    successor: List[TRoadLanesLaneSectionLcrLaneLinkPredecessorSuccessor] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadLanesLaneSectionLcrLaneRoadMarkExplicit(OpenDriveElement):
    """Irregular road markings that cannot be described by repetitive line patterns
    may be described by individual road marking elements.

    These explicit definitions also contain &lt;line&gt; elements for
    the line definition, however, these lines will not be repeated
    automatically as in repetitive road marking types. In ASAM
    OpenDRIVE, irregular road marking types and lines are represented by
    &lt;explicit&gt; elements within elements. The line definitions are
    contained in &lt;line&gt; elements within the &lt;explicit&gt;
    element. The &lt;explicit&gt; element should specifically be used
    for measurement data.
    """

    class Meta:
        name = "t_road_lanes_laneSection_lcr_lane_roadMark_explicit"

    line: List[TRoadLanesLaneSectionLcrLaneRoadMarkExplicitLine] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadLanesLaneSectionLcrLaneRoadMarkType(OpenDriveElement):
    """
    Each type definition shall contain one or more line definitions with additional
    information about the lines that the road mark is composed of.

    :ivar line:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar name: Name of the road mark type. May be chosen freely.
    :ivar width: Accumulated width of the road mark. In case of several
        &lt;line&gt; elements this @width is the sum of all @width of
        &lt;line&gt; elements and spaces in between, necessary to form
        the road mark. This attribute supersedes the definition in the
        &lt;roadMark&gt; element.
    """

    class Meta:
        name = "t_road_lanes_laneSection_lcr_lane_roadMark_type"

    line: List[TRoadLanesLaneSectionLcrLaneRoadMarkTypeLine] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
        },
    )


@dataclass
class TRoadLanesLaneSectionLrLaneAccess(OpenDriveElement):
    """Defines access restrictions for certain types of road users.

    Each element is valid in direction of the increasing s coordinate
    until a new element is defined. If multiple elements are defined,
    they shall be listed in ascending order.

    :ivar restriction:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar restriction_attribute: Identifier of the participant to whom
        the restriction applies
    :ivar rule: Specifies whether the participant given in the attribute
        @restriction is allowed or denied access to the given lane
    :ivar s_offset: s-coordinate of start position, relative to the
        position of the preceding &lt;laneSection&gt; element
    """

    class Meta:
        name = "t_road_lanes_laneSection_lr_lane_access"

    restriction: List[TRoadLanesLaneSectionLrLaneAccessRestriction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    restriction_attribute: Optional[EAccessRestrictionType] = field(
        default=None,
        metadata={
            "name": "restriction",
            "type": "Attribute",
        },
    )
    rule: Optional[ERoadLanesLaneSectionLrLaneAccessRule] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    s_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "sOffset",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )


@dataclass
class TRoadLateralProfileCrossSectionSurfaceStripConstant(OpenDriveElement):
    """
    Defines in t a constant height of the surface.
    """

    class Meta:
        name = "t_road_lateralProfile_crossSectionSurface_strip_constant"

    coefficients: List[TRoadLateralProfileCrossSectionSurfaceCoefficients] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadLateralProfileCrossSectionSurfaceStripCubic(OpenDriveElement):
    """
    Defines in t a cubic height of the surface.
    """

    class Meta:
        name = "t_road_lateralProfile_crossSectionSurface_strip_cubic"

    coefficients: List[TRoadLateralProfileCrossSectionSurfaceCoefficients] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadLateralProfileCrossSectionSurfaceStripLinear(OpenDriveElement):
    """
    Defines in t a linear height of the surface.
    """

    class Meta:
        name = "t_road_lateralProfile_crossSectionSurface_strip_linear"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    coefficients: List[TRoadLateralProfileCrossSectionSurfaceCoefficients] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )
    )


@dataclass
class TRoadLateralProfileCrossSectionSurfaceStripQuadratic(OpenDriveElement):
    """
    Defines in t a quadratic height of the surface.
    """

    class Meta:
        name = "t_road_lateralProfile_crossSectionSurface_strip_quadratic"

    coefficients: List[TRoadLateralProfileCrossSectionSurfaceCoefficients] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadLateralProfileCrossSectionSurfaceStripWidth(OpenDriveElement):
    """
    Defines the width of the inner strip.
    """

    class Meta:
        name = "t_road_lateralProfile_crossSectionSurface_strip_width"

    coefficients: List[TRoadLateralProfileCrossSectionSurfaceCoefficients] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadLateralProfileCrossSectionSurfaceTOffset(OpenDriveElement):
    """
    A t offset shifts all strips relative to the road reference line in
    t-direction.
    """

    class Meta:
        name = "t_road_lateralProfile_crossSectionSurface_tOffset"

    coefficients: List[TRoadLateralProfileCrossSectionSurfaceCoefficients] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadLink(OpenDriveElement):
    """Follows the road header if the road is linked to a successor or a
    predecessor.

    Isolated roads may omit this element.
    """

    class Meta:
        name = "t_road_link"

    predecessor: Optional[TRoadLinkPredecessorSuccessor] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    successor: Optional[TRoadLinkPredecessorSuccessor] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadObjectsBridge(OpenDriveElement):
    """Bridges are modeled as objects in ASAM OpenDRIVE.

    The road with the bridge object leads over a bridge. Bridges are
    valid for a road’s complete cross section unless a lane validity
    record with further restrictions is provided as child element.

    :ivar validity:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: Unique ID within database
    :ivar length: Length of the bridge (in s-direction)
    :ivar name: Name of the bridge. May be chosen freely.
    :ivar s: s-coordinate
    :ivar type_value: Type of bridge
    """

    class Meta:
        name = "t_road_objects_bridge"

    validity: List[TRoadObjectsObjectLaneValidity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    type_value: Optional[EBridgeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadObjectsObjectReference(OpenDriveElement):
    """An object reference refers to one identical object from multiple roads.

    The referenced objects require a unique ID. The
    &lt;objectReference&gt; element consists of a main element and an
    optional lane validity element.

    :ivar validity:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: Unique ID of the referred object within the database
    :ivar orientation: "+" = valid in positive s-direction "-" = valid
        in negative s-direction "none" = valid in both directions
    :ivar s: s-coordinate
    :ivar t: t-coordinate
    :ivar valid_length: Validity of the object along s-axis (0.0 for
        point object)
    :ivar z_offset: z offset relative to the elevation of the road
        reference line
    """

    class Meta:
        name = "t_road_objects_objectReference"

    validity: List[TRoadObjectsObjectLaneValidity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    orientation: Optional[EOrientation] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    t: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    valid_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "validLength",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    z_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "zOffset",
            "type": "Attribute",
        },
    )


@dataclass
class TRoadObjectsObjectBordersBorder(OpenDriveElement):
    """
    Specifies a border along certain outline points.

    :ivar corner_reference:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar outline_id: ID of the outline to use
    :ivar type_value: Appearance of border
    :ivar use_complete_outline: Use all outline points for border.
        “true” is used as default.
    :ivar width: Border width
    """

    class Meta:
        name = "t_road_objects_object_borders_border"

    corner_reference: List[
        TRoadObjectsObjectMarkingsMarkingCornerReference
    ] = field(
        default_factory=list,
        metadata={
            "name": "cornerReference",
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    outline_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "outlineId",
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[EBorderType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    use_complete_outline: Optional[TBool] = field(
        default=None,
        metadata={
            "name": "useCompleteOutline",
            "type": "Attribute",
        },
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )


@dataclass
class TRoadObjectsObjectMarkingsMarking(OpenDriveElement):
    """
    Specifies a marking that is either attached to one side of the object bounding
    box or referencing outline points.

    :ivar corner_reference:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar color: Color of the marking
    :ivar line_length: Length of the visible part
    :ivar side: Side of the bounding box described in &lt;object&gt;
        element in the local coordinate system u/v
    :ivar space_length: Length of the gap between the visible parts
    :ivar start_offset: Lateral offset in u-direction from start of
        bounding box side where the first marking starts
    :ivar stop_offset: Lateral offset in u-direction from end of
        bounding box side where the marking ends
    :ivar weight: Optical "weight" of the marking
    :ivar width: Width of the marking
    :ivar z_offset: Height of road mark above the road, i.e. thickness
        of the road mark
    """

    class Meta:
        name = "t_road_objects_object_markings_marking"

    corner_reference: List[
        TRoadObjectsObjectMarkingsMarkingCornerReference
    ] = field(
        default_factory=list,
        metadata={
            "name": "cornerReference",
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    color: Optional[ERoadMarkColor] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    line_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "lineLength",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
        },
    )
    side: Optional[ESideType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    space_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "spaceLength",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    start_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "startOffset",
            "type": "Attribute",
            "required": True,
        },
    )
    stop_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "stopOffset",
            "type": "Attribute",
            "required": True,
        },
    )
    weight: Optional[ERoadMarkWeight] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )
    z_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "zOffset",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )


@dataclass
class TRoadObjectsObjectOutlinesOutline(OpenDriveElement):
    """Defines a series of corner points, including the height of the object
    relative to the road reference line.

    For areas, the points should be listed in counter-clockwise order.
    The inner area of the described outline may be filled with a filling
    type, such as grass, concrete, asphalt, or pavement. An element
    shall be followed by two or more &lt;cornerRoad&gt; elements or by
    two or more &lt;cornerLocal&gt; elements. ASAM OpenDRIVE 1.4 outline
    definitions (without &lt;outlines&gt; parent element) shall still be
    supported.

    :ivar corner_road:
    :ivar corner_local:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar closed: If true, the outline describes an area, not a linear
        feature
    :ivar fill_type: Type used to fill the area inside the outline
    :ivar id: ID of the outline. Must be unique within one object.
    :ivar lane_type: Describes the lane type of the outline
    :ivar outer: Defines if outline is an outer outline of the object
    """

    class Meta:
        name = "t_road_objects_object_outlines_outline"

    corner_road: List[TRoadObjectsObjectOutlinesOutlineCornerRoad] = field(
        default_factory=list,
        metadata={
            "name": "cornerRoad",
            "type": "Element",
            "namespace": "",
        },
    )
    corner_local: List[TRoadObjectsObjectOutlinesOutlineCornerLocal] = field(
        default_factory=list,
        metadata={
            "name": "cornerLocal",
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    closed: Optional[TBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fill_type: Optional[EOutlineFillType] = field(
        default=None,
        metadata={
            "name": "fillType",
            "type": "Attribute",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lane_type: Optional[ELaneType] = field(
        default=None,
        metadata={
            "name": "laneType",
            "type": "Attribute",
        },
    )
    outer: Optional[TBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TRoadObjectsObjectSkeletonPolyline:
    """Defines a series of points relative to the road reference line.

    An &lt;polyline&gt; element shall be followed by either two or more
    &lt;vertexRoad&gt; elements or by two or more &lt;vertexLocal&gt;
    elements.

    :ivar vertex_road:
    :ivar vertex_local:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: ID of the polyline. Must be unique within one object.
    """

    class Meta:
        name = "t_road_objects_object_skeleton_polyline"

    vertex_road: List[TRoadObjectsObjectSkeletonPolylineVertexRoad] = field(
        default_factory=list,
        metadata={
            "name": "vertexRoad",
            "type": "Element",
            "namespace": "",
        },
    )
    vertex_local: List[TRoadObjectsObjectSkeletonPolylineVertexLocal] = field(
        default_factory=list,
        metadata={
            "name": "vertexLocal",
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TRoadObjectsObjectSurface(OpenDriveElement):
    """
    Used to describe the road surface elevation of an object.
    """

    class Meta:
        name = "t_road_objects_object_surface"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    crg: Optional[TRoadObjectsObjectSurfaceCrg] = field(
        default=None,
        metadata={
            "name": "CRG",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadObjectsTunnel(OpenDriveElement):
    """Tunnels are modeled as objects in ASAM OpenDRIVE.

    The road with the tunnel object defines the part of the road that is
    the tunnel or the underpass. Tunnels are valid for the complete
    cross section of a road unless a lane validity element with further
    restrictions is provided as child element

    :ivar validity:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar daylight: Degree of daylight intruding the tunnel. Depends on
        the application.
    :ivar id: Unique ID within database
    :ivar length: Length of the tunnel (in s-direction)
    :ivar lighting: Degree of artificial tunnel lighting. Depends on the
        application.
    :ivar name: Name of the tunnel. May be chosen freely.
    :ivar s: s-coordinate
    :ivar type_value: Type of tunnel
    """

    class Meta:
        name = "t_road_objects_tunnel"

    validity: List[TRoadObjectsObjectLaneValidity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    daylight: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    lighting: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    type_value: Optional[ETunnelType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadPlanViewGeometry(OpenDriveElement):
    """
    :ivar line:
    :ivar spiral:
    :ivar arc:
    :ivar poly3:
    :ivar param_poly3:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar hdg: Start orientation (inertial heading)
    :ivar length: Length of the element's reference line
    :ivar s: s-coordinate of start position
    :ivar x: Start position (x inertial)
    :ivar y: Start position (y inertial)
    """

    class Meta:
        name = "t_road_planView_geometry"

    line: Optional[TRoadPlanViewGeometryLine] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    spiral: Optional[TRoadPlanViewGeometrySpiral] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    arc: Optional[TRoadPlanViewGeometryArc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    poly3: Optional[TRoadPlanViewGeometryPoly3] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    param_poly3: Optional[TRoadPlanViewGeometryParamPoly3] = field(
        default=None,
        metadata={
            "name": "paramPoly3",
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    hdg: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadRailroadSwitch(OpenDriveElement):
    """Switches change the tracks for rail-bound vehicles.

    Switches guide the vehicles into two directions only.

    :ivar main_track:
    :ivar side_track:
    :ivar partner:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: Unique ID of the switch; preferably an integer number, see
        uint32_t
    :ivar name: Unique name of the switch
    :ivar position: Either a switch can be operated (dynamic) or it is
        in a static position
    """

    class Meta:
        name = "t_road_railroad_switch"

    main_track: Optional[TRoadRailroadSwitchMainTrack] = field(
        default=None,
        metadata={
            "name": "mainTrack",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    side_track: Optional[TRoadRailroadSwitchSideTrack] = field(
        default=None,
        metadata={
            "name": "sideTrack",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    partner: Optional[TRoadRailroadSwitchPartner] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    position: Optional[ERoadRailroadSwitchPosition] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadSignalsBoard(OpenDriveElement):
    """Signals are not always separate signs on a single sheet of metal.

    Several signs can be coupled on one board.
    """

    class Meta:
        name = "t_road_signals_board"

    validity: List[TRoadObjectsObjectLaneValidity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    dependency: List[TRoadSignalsSignalDependency] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    reference: List[TRoadSignalsSignalReference2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadSignalsSignalReference1(OpenDriveElement):
    """Refers to the same, that is, identical signal from multiple roads.

    The referenced signals require a unique ID. The
    &lt;signalReference&gt; element consists of a main element and an
    optional lane validity element.

    :ivar validity:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: Unique ID of the referenced signal within the database
    :ivar orientation: "+" = valid in positive s-direction "-" = valid
        in negative s-direction "none" = valid in both directions
    :ivar s: s-coordinate
    :ivar t: t-coordinate
    """

    class Meta:
        name = "t_road_signals_signalReference"

    validity: List[TRoadObjectsObjectLaneValidity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    orientation: Optional[EOrientation] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    t: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadSurface(OpenDriveElement):
    """
    Contains a series of elements describing a surface.
    """

    class Meta:
        name = "t_road_surface"

    crg: List[TRoadSurfaceCrg] = field(
        default_factory=list,
        metadata={
            "name": "CRG",
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadType(OpenDriveElement):
    """A road type element is valid for the entire cross section of a road.

    It is valid until a new road type element is provided or until the
    road ends.

    :ivar speed:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar country: Country code of the road, see ISO 3166-1, alpha-2
        codes.
    :ivar s: s-coordinate of start position
    :ivar type_value: Type of the road defined as enumeration
    """

    class Meta:
        name = "t_road_type"

    speed: Optional[TRoadTypeSpeed] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    country: Optional[Union[str, ECountryCodeDeprecated]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Z]{2}",
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    type_value: Optional[ERoadType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TSignalGroupVmsGroup(OpenDriveElement):
    """On a gantry there can be one large variable message board or several smaller
    variable message boards.

    ASAM OpenSCENARIO requires to treat a gantry that has one large
    variable message board or several smaller variable message boards
    the same way. Therefore variable message boards that are on the same
    gantry shall be grouped and their indexes shall be redefined if not
    unique.

    :ivar vms_board_reference:
    :ivar open_drive_element:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: Unique id of the &lt;vmsGroup&gt;
    """

    class Meta:
        name = "t_signalGroup_vmsGroup"

    vms_board_reference: List[TSignalGroupVmsBoardReference] = field(
        default_factory=list,
        metadata={
            "name": "vmsBoardReference",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    open_drive_element: Optional[OpenDriveElement] = field(
        default=None,
        metadata={
            "name": "_OpenDriveElement",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TSignalsSemantics(OpenDriveElement):
    """Semantics are limited to traffic behavior that is specified just by signals
    in ASAM OpenDRIVE.

    Each traffic behavior is specified by a specific element.
    """

    class Meta:
        name = "t_signals_semantics"

    speed: List[TSignalsSemanticsSpeed] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    lane: List[TSignalsSemanticsLane] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    priority: List[TSignalsSemanticsPriority] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    prohibited: List[TSignalsSemanticsProhibited] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    warning: List[TSignalsSemanticsWarning] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    routing: List[TSignalsSemanticsRouting] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    streetname: List[TSignalsSemanticsStreetname] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    parking: List[TSignalsSemanticsParking] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    tourist: List[TSignalsSemanticsTourist] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    supplementary_time: List[TSignalsSemanticsSupplementaryTime] = field(
        default_factory=list,
        metadata={
            "name": "supplementaryTime",
            "type": "Element",
            "namespace": "",
        },
    )
    supplementary_allows: List[TSignalsSemanticsSupplementaryAllows] = field(
        default_factory=list,
        metadata={
            "name": "supplementaryAllows",
            "type": "Element",
            "namespace": "",
        },
    )
    supplementary_prohibits: List[TSignalsSemanticsSupplementaryProhibits] = (
        field(
            default_factory=list,
            metadata={
                "name": "supplementaryProhibits",
                "type": "Element",
                "namespace": "",
            },
        )
    )
    supplementary_distance: List[TSignalsSemanticsSupplementaryDistance] = (
        field(
            default_factory=list,
            metadata={
                "name": "supplementaryDistance",
                "type": "Element",
                "namespace": "",
            },
        )
    )
    supplementary_environment: List[
        TSignalsSemanticsSupplementaryEnvironment
    ] = field(
        default_factory=list,
        metadata={
            "name": "supplementaryEnvironment",
            "type": "Element",
            "namespace": "",
        },
    )
    supplementary_explanatory: List[
        TSignalsSemanticsSupplementaryExplanatory
    ] = field(
        default_factory=list,
        metadata={
            "name": "supplementaryExplanatory",
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TStationPlatform(OpenDriveElement):
    """Platforms are essential parts of stations for passengers to enter and leave
    rail-bound vehicles.

    One or more railroad tracks reference one platform.

    :ivar segment:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: Unique ID within database
    :ivar name: Name of the platform. May be chosen freely.
    """

    class Meta:
        name = "t_station_platform"

    segment: List[TStationPlatformSegment] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class THeaderRoadRegulation(OpenDriveElement):
    """
    Defines the default regulations for different road types.
    """

    class Meta:
        name = "t_header_roadRegulation"

    open_drive_element: Optional[OpenDriveElement] = field(
        default=None,
        metadata={
            "name": "_OpenDriveElement",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    semantics: Optional[TSignalsSemantics] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[ERoadType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class THeaderSignalRegulation(OpenDriveElement):
    """
    Defines the default regulations for signs in different countries, for example,
    if it is allowed to turn right when a red traffic light appears.
    """

    class Meta:
        name = "t_header_signalRegulation"

    open_drive_element: Optional[OpenDriveElement] = field(
        default=None,
        metadata={
            "name": "_OpenDriveElement",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    semantics: Optional[TSignalsSemantics] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    subtype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class TJunctionBoundary(OpenDriveElement):
    """Junction boundaries enclose the area intended for traffic.

    This also includes the sidewalks for pedestrians.
    """

    class Meta:
        name = "t_junction_boundary"

    segment: List[
        Union[
            TJunctionBoundarySegment,
            TJunctionBoundarySegmentLane,
            TJunctionBoundarySegmentJoint,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TJunctionConnectionCommon(TJunctionConnection):
    """
    Provides information about a single connection within a common junction.

    :ivar connecting_road: ID of the connecting road. Only to be used
        for junctions of @type="default".
    """

    class Meta:
        name = "t_junction_connection_common"

    connecting_road: Optional[str] = field(
        default=None,
        metadata={
            "name": "connectingRoad",
            "type": "Attribute",
        },
    )


@dataclass
class TJunctionConnectionDirect(TJunctionConnection):
    """
    Provides information about a single connection within a direct junction.

    :ivar linked_road: ID of the directly linked road. Only to be used
        for junctions of @type="direct".
    """

    class Meta:
        name = "t_junction_connection_direct"

    linked_road: Optional[str] = field(
        default=None,
        metadata={
            "name": "linkedRoad",
            "type": "Attribute",
        },
    )


@dataclass
class TJunctionConnectionVirtual(TJunctionConnection):
    """Virtual connections indicate possible connections between two roads or one
    or more lanes of two roads.

    Virtual connections do not specify connecting roads.

    :ivar predecessor:
    :ivar successor:
    :ivar connecting_road:
    :ivar type_value: Type of the connection. Regular connections are
        @type=“default” . This attribute is mandatory for virtual
        connections.
    """

    class Meta:
        name = "t_junction_connection_virtual"

    predecessor: Optional[TJunctionPredecessorSuccessor] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    successor: Optional[TJunctionPredecessorSuccessor] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    connecting_road: Optional[str] = field(
        default=None,
        metadata={
            "name": "connectingRoad",
            "type": "Attribute",
        },
    )
    type_value: Optional[EConnectionType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class TJunctionConnectionVirtualDefault(TJunctionConnection):
    """
    Provides information about a single connection within a virtual junction.

    :ivar connecting_road:
    :ivar type_value: Type of the connection. Regular connections are
        @type=“default” . This attribute is mandatory for virtual
        connections.
    """

    class Meta:
        name = "t_junction_connection_virtual_default"

    connecting_road: Optional[str] = field(
        default=None,
        metadata={
            "name": "connectingRoad",
            "type": "Attribute",
        },
    )
    type_value: Optional[EConnectionType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class TRoadLanesLaneSectionLcrLaneRoadMark(OpenDriveElement):
    """Defines the style of the line at the outer border of a lane.

    The style of the center line that separates left and right lanes is
    determined by the road mark element for the center lane.

    :ivar sway:
    :ivar type_value:
    :ivar explicit:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar color: Color of the road mark
    :ivar height: Height of road mark above the road, i.e. thickness of
        the road mark
    :ivar lane_change: Allows a lane change in the indicated direction,
        taking into account that lanes are numbered in ascending order
        from right to left. If the attribute is missing, “both” is used
        as default.
    :ivar material: Material of the road mark. Identifiers to be defined
        by the user, use "standard" as default value.
    :ivar s_offset: s-coordinate of start position of the
        &lt;roadMark&gt; element, relative to the position of the
        preceding &lt;laneSection&gt; element
    :ivar type_attribute: Type of the road mark
    :ivar weight: Weight of the road mark. This attribute is optional if
        detailed definition is given below.
    :ivar width: Width of the road mark. This attribute is optional if
        detailed definition is given by &lt;line&gt; element.
    """

    class Meta:
        name = "t_road_lanes_laneSection_lcr_lane_roadMark"

    sway: List[TRoadLanesLaneSectionLcrLaneRoadMarkSway] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[TRoadLanesLaneSectionLcrLaneRoadMarkType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "",
        },
    )
    explicit: Optional[TRoadLanesLaneSectionLcrLaneRoadMarkExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    color: Optional[ERoadMarkColor] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    height: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )
    lane_change: Optional[ERoadLanesLaneSectionLcrLaneRoadMarkLaneChange] = (
        field(
            default=None,
            metadata={
                "name": "laneChange",
                "type": "Attribute",
            },
        )
    )
    material: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    s_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "sOffset",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    type_attribute: Optional[ERoadMarkType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    weight: Optional[ERoadMarkWeight] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )


@dataclass
class TRoadLateralProfileCrossSectionSurfaceStrip(OpenDriveElement):
    """
    A strip defines the lateral profile in t- and s-direction.

    :ivar width:
    :ivar constant:
    :ivar linear:
    :ivar quadratic:
    :ivar cubic:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: 1 for the inner left strip, -1 for the inner right strip,
        2 for the outer left strip, -2 for the outer right strip
    :ivar mode: Can only be defined for an outer strip.
    """

    class Meta:
        name = "t_road_lateralProfile_crossSectionSurface_strip"

    width: Optional[TRoadLateralProfileCrossSectionSurfaceStripWidth] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    constant: Optional[TRoadLateralProfileCrossSectionSurfaceStripConstant] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
    )
    linear: Optional[TRoadLateralProfileCrossSectionSurfaceStripLinear] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
    )
    quadratic: Optional[
        TRoadLateralProfileCrossSectionSurfaceStripQuadratic
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    cubic: Optional[TRoadLateralProfileCrossSectionSurfaceStripCubic] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mode: Optional[EStripMode] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TRoadObjectsObjectBorders(OpenDriveElement):
    """Object borders are frames with a defined width, for example, to describe
    traffic islands.

    Different border types are available.
    """

    class Meta:
        name = "t_road_objects_object_borders"

    border: List[TRoadObjectsObjectBordersBorder] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadObjectsObjectMarkings(OpenDriveElement):
    """
    Object markings are road markings of any objects, for example, crosswalks,
    stopping-lines, and parking spaces.
    """

    class Meta:
        name = "t_road_objects_object_markings"

    marking: List[TRoadObjectsObjectMarkingsMarking] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadObjectsObjectOutlines(OpenDriveElement):
    """Wrapper for the different outline entries of an object, that can contain
    multiple outline definitions.

    If &lt;outlines&gt; is not used, an object can have only a single
    &lt;outline&gt; entry.
    """

    class Meta:
        name = "t_road_objects_object_outlines"

    outline: List[TRoadObjectsObjectOutlinesOutline] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadObjectsObjectSkeleton:
    """
    Wrapper for the object polylines, that can be used to describe the actual shape
    inside the bounding box more closely.
    """

    class Meta:
        name = "t_road_objects_object_skeleton"

    polyline: List[TRoadObjectsObjectSkeletonPolyline] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadPlanView(OpenDriveElement):
    """
    Contains geometry elements that define the layout of the road reference line in
    the x/y-plane (plan view).
    """

    class Meta:
        name = "t_road_planView"

    geometry: List[TRoadPlanViewGeometry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadRailroad(OpenDriveElement):
    """Container for all railroad definitions that shall be applied along a road.

    The available set of railroad elements is currently limited to the
    definition of switches. All other entries shall be covered with the
    existing elements, for example, track definition by &lt;road&gt;,
    signal definition by &lt;signal&gt;, etc. Railroad-specific elements
    are defined against the background of streetcar applications.
    """

    class Meta:
        name = "t_road_railroad"

    switch: List[TRoadRailroadSwitch] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadSignalsSignal(OpenDriveElement):
    """
    A signal along the road or on a static board.

    :ivar validity:
    :ivar dependency:
    :ivar reference:
    :ivar position_inertial:
    :ivar position_road:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar semantics:
    :ivar country: Country code of the road, see ISO 3166-1, alpha-2
        codes.
    :ivar country_revision: Defines the year of the applied traffic
        rules
    :ivar dynamic: Indicates whether the signal is dynamic or static.
        Example: traffic light is dynamic
    :ivar height: Height of the signal, measured from bottom edge of the
        signal.
    :ivar h_offset: Heading offset of the signal (relative to
        @orientation, if orientation is equal to “+” or “-“) Heading
        offset of the signal (relative to road reference line, if
        orientation is equal to “none” )
    :ivar id: Unique ID of the signal within the OpenDRIVE file
    :ivar length: Length of the signal's bounding box. @length is
        defined in the local coordinate system u/v along the u-axis
    :ivar name: Name of the signal. May be chosen freely.
    :ivar orientation: "+" = valid in positive s- direction "-" = valid
        in negative s- direction "none" = valid in both directions
    :ivar pitch: Pitch angle of the signal, relative to the inertial
        system (xy-plane)
    :ivar roll: Roll angle of the signal after applying pitch, relative
        to the inertial system (x’’y’’-plane)
    :ivar subtype: Subtype identifier according to country code or "-1"
        / "none"
    :ivar text: Additional text associated with the signal, for example,
        text on city limit "City\\nBadAibling"
    :ivar type_value: Type identifier according to country code or "-1"
        / "none". See extra document.
    :ivar unit: Unit of @value
    :ivar value: Value of the signal, if value is given, unit is
        mandatory
    :ivar width: Width of the signal's bounding box. @width is defined
        in the local coordinate system u/v along the v-axis
    """

    class Meta:
        name = "t_road_signals_signal"

    validity: List[TRoadObjectsObjectLaneValidity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    dependency: List[TRoadSignalsSignalDependency] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    reference: List[TRoadSignalsSignalReference2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    position_inertial: Optional[TRoadSignalsSignalPositionInertial] = field(
        default=None,
        metadata={
            "name": "positionInertial",
            "type": "Element",
            "namespace": "",
        },
    )
    position_road: Optional[TRoadSignalsSignalPositionRoad] = field(
        default=None,
        metadata={
            "name": "positionRoad",
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    semantics: Optional[TSignalsSemantics] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    country: Optional[Union[str, ECountryCodeDeprecated]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Z]{2}",
        },
    )
    country_revision: Optional[str] = field(
        default=None,
        metadata={
            "name": "countryRevision",
            "type": "Attribute",
        },
    )
    dynamic: Optional[TYesNo] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    height: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    h_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "hOffset",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    orientation: Optional[EOrientation] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    pitch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    roll: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    subtype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    unit: Optional[EUnit] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )


@dataclass
class TRoadSignalsVmsBoard(TRoadSignalsBoard):
    """Variable message boards can change their values during the simulation in
    ASAM OpenSCENARIO.

    Variable message boards are switched off if they are not specified
    in ASAM OpenSCENARIO.

    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar display_area:
    :ivar display_height: Height of the display
    :ivar display_type: Functional type of the display
    :ivar display_width: Width of the display
    :ivar v: Local v-coordinate of the board
    :ivar z: Local z-coordinate of the board
    """

    class Meta:
        name = "t_road_signals_vmsBoard"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    display_area: List[TRoadSignalsDisplayArea] = field(
        default_factory=list,
        metadata={
            "name": "displayArea",
            "type": "Element",
            "namespace": "",
        },
    )
    display_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "displayHeight",
            "type": "Attribute",
        },
    )
    display_type: Optional[ERoadSignalsDisplayType] = field(
        default=None,
        metadata={
            "name": "displayType",
            "type": "Attribute",
        },
    )
    display_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "displayWidth",
            "type": "Attribute",
        },
    )
    v: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    z: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TStation(OpenDriveElement):
    """Stations are places on the rail network where passengers enter and leave
    rail-bound vehicles at platforms.

    May refer to multiple tracks and is therefore defined on the same
    level as junctions.

    :ivar platform:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: Unique ID within database
    :ivar name: Unique name of the station
    :ivar type_value: Type of station. Free text, depending on the
        application. e.g.: small, medium, large
    """

    class Meta:
        name = "t_station"

    platform: List[TStationPlatform] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[EStationType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class THeaderDefaultRegulations(OpenDriveElement):
    """Defines the default regulations.

    In each country there are different speed limits to a rural road.
    For example a rural road has a speed limit of 100km/h in Germany and
    80km/h in the Netherlands. In some countries, one is allowed to turn
    right at a red traffic light; in others, one is not. Instead of
    writing this for each road or each signal, the default regulations
    can be specified once in the header for the entire {THIS_STANDARD}
    file. The default driving regulations can be overwritten with road,
    lane, or signal definitions.
    """

    class Meta:
        name = "t_header_defaultRegulations"

    road_regulations: List[THeaderRoadRegulation] = field(
        default_factory=list,
        metadata={
            "name": "roadRegulations",
            "type": "Element",
            "namespace": "",
        },
    )
    signal_regulations: List[THeaderSignalRegulation] = field(
        default_factory=list,
        metadata={
            "name": "signalRegulations",
            "type": "Element",
            "namespace": "",
        },
    )
    open_drive_element: Optional[OpenDriveElement] = field(
        default=None,
        metadata={
            "name": "_OpenDriveElement",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadLanesLaneSectionCenterLane:
    """Center lane element with ID zero.

    Has no width attribute. Mainly used for road marks.

    :ivar link:
    :ivar road_mark:
    :ivar id: ID of the lane
    :ivar level:
    :ivar type_value:
    """

    class Meta:
        name = "t_road_lanes_laneSection_center_lane"

    link: Optional[TRoadLanesLaneSectionLcrLaneLink] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    road_mark: List[TRoadLanesLaneSectionLcrLaneRoadMark] = field(
        default_factory=list,
        metadata={
            "name": "roadMark",
            "type": "Element",
            "namespace": "",
        },
    )
    id: int = field(
        init=False,
        default=0,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    level: Optional[TBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[ELaneType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class TRoadLanesLaneSectionLrLane(OpenDriveElement):
    """Lane elements are included in left/center/right elements.

    Lane elements should represent the lanes from left to right, that
    is, with descending ID.

    :ivar link:
    :ivar border:
    :ivar width:
    :ivar road_mark:
    :ivar material:
    :ivar speed:
    :ivar access:
    :ivar height:
    :ivar rule:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar advisory: If true, lane can be used also by a neighboring
        lane. Advisory lane has priority, for example a bike lane, that
        can also be used by cars. If not specified, default value is
        none.
    :ivar direction: If not specified, direction is determined by the
        combination of &lt;left&gt; or &lt;right&gt; lane grouping and
        the values LHT or RHT of the @rule attribute of a road. The
        standard direction can be overwritten with this attribute.
    :ivar dynamic_lane_direction: If true, lane direction can be changed
        dynamically by the scenario during the simulation. If not
        specified, default boolean value is false.
    :ivar dynamic_lane_type: If true, lane type can be changed
        dynamically by the scenario during the simulation. Typical
        example is a stop lane that can be changed by VMS boards to a
        driving lane. If not specified, default boolean value is false.
    :ivar level: "true" = keep lane on level, that is, do not apply
        superelevation; "false" = apply superelevation to this lane
        (default, also used if attribute level is missing)
    :ivar road_works: If true, lane is under construction.
    :ivar type_value: Type of the lane
    """

    class Meta:
        name = "t_road_lanes_laneSection_lr_lane"

    link: Optional[TRoadLanesLaneSectionLcrLaneLink] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    border: List[TRoadLanesLaneSectionLrLaneBorder] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    width: List[TRoadLanesLaneSectionLrLaneWidth] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    road_mark: List[TRoadLanesLaneSectionLcrLaneRoadMark] = field(
        default_factory=list,
        metadata={
            "name": "roadMark",
            "type": "Element",
            "namespace": "",
        },
    )
    material: List[TRoadLanesLaneSectionLrLaneMaterial] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    speed: List[TRoadLanesLaneSectionLrLaneSpeed] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access: List[TRoadLanesLaneSectionLrLaneAccess] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    height: List[TRoadLanesLaneSectionLrLaneHeight] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    rule: List[TRoadLanesLaneSectionLrLaneRule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    advisory: Optional[ELaneAdvisory] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    direction: Optional[ELaneDirection] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dynamic_lane_direction: Optional[TBool] = field(
        default=None,
        metadata={
            "name": "dynamicLaneDirection",
            "type": "Attribute",
        },
    )
    dynamic_lane_type: Optional[TBool] = field(
        default=None,
        metadata={
            "name": "dynamicLaneType",
            "type": "Attribute",
        },
    )
    level: Optional[TBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    road_works: Optional[TBool] = field(
        default=None,
        metadata={
            "name": "roadWorks",
            "type": "Attribute",
        },
    )
    type_value: Optional[ELaneType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadLateralProfileCrossSectionSurfaceSurfaceStrip(OpenDriveElement):
    """
    Surface strips contains the strips.
    """

    class Meta:
        name = "t_road_lateralProfile_crossSectionSurface_surfaceStrip"

    strip: List[TRoadLateralProfileCrossSectionSurfaceStrip] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 4,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadObjectsObject(OpenDriveElement):
    """Objects influence a road by expanding, delimiting, or supplementing its
    course. Objects are elements that form the environment, for example, buildings,
    guard rails, poles, and trees. Objects do not influence the behavior of traffic
    directly, unlike signals.

    There are two ways to describe the bounding box of objects.
    - For an angular object: definition of the width, length and height.
    - For a circular object: definition of the radius and height.

    :ivar repeat:
    :ivar outline:
    :ivar outlines:
    :ivar material:
    :ivar validity:
    :ivar parking_space:
    :ivar markings:
    :ivar borders:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar surface:
    :ivar skeleton:
    :ivar dynamic: Indicates whether the object is dynamic or static,
        default value is “no” (static). Dynamic object cannot change its
        position.
    :ivar hdg: Heading angle of the object relative to road direction
    :ivar height: Height of the object's bounding box. @height is
        defined in the local coordinate system u/v along the z-axis
    :ivar id: Unique ID within database
    :ivar length: Length of the object's bounding box, alternative to
        @radius. @length is defined in the local coordinate system u/v
        along the u-axis
    :ivar name: Name of the object. May be chosen freely.
    :ivar orientation: "+" = valid in positive s-direction "-" = valid
        in negative s-direction "none" = valid in both directions (does
        not affect the heading)
    :ivar perp_to_road: Alternative to @pitch and @roll. If true, the
        object is vertically perpendicular to the road surface at all
        points and @pitch and @roll are ignored. Default is false.
    :ivar pitch: Pitch angle relative to the x/y-plane
    :ivar radius: radius of the circular object's bounding box,
        alternative to @length and @width. @radius is defined in the
        local coordinate system u/v
    :ivar roll: Roll angle relative to the x/y-plane
    :ivar s: s-coordinate of object's origin
    :ivar subtype: Variant of a type
    :ivar t: t-coordinate of object's origin
    :ivar type_value: Type of object. For a parking space, the
        &lt;parkingSpace&gt; element may be used additionally.
    :ivar valid_length: Validity of object along s-axis (0.0 for point
        object)
    :ivar width: Width of the object's bounding box, alternative to
        @radius. @width is defined in the local coordinate system u/v
        along the v-axis
    :ivar z_offset: z-offset of object's origin relative to the
        elevation of the road reference line
    """

    class Meta:
        name = "t_road_objects_object"

    repeat: List[TRoadObjectsObjectRepeat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    outline: Optional[TRoadObjectsObjectOutlinesOutline] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    outlines: Optional[TRoadObjectsObjectOutlines] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    material: List[TRoadObjectsObjectMaterial] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    validity: List[TRoadObjectsObjectLaneValidity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    parking_space: Optional[TRoadObjectsObjectParkingSpace] = field(
        default=None,
        metadata={
            "name": "parkingSpace",
            "type": "Element",
            "namespace": "",
        },
    )
    markings: Optional[TRoadObjectsObjectMarkings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    borders: Optional[TRoadObjectsObjectBorders] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    surface: Optional[TRoadObjectsObjectSurface] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    skeleton: Optional[TRoadObjectsObjectSkeleton] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    dynamic: Optional[TYesNo] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    hdg: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    height: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    orientation: Optional[EOrientation] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    perp_to_road: Optional[TBool] = field(
        default=None,
        metadata={
            "name": "perpToRoad",
            "type": "Attribute",
        },
    )
    pitch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    radius: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )
    roll: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    subtype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    t: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[EObjectType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    valid_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "validLength",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    z_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "zOffset",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadSignalsBoardSign(TRoadSignalsSignal):
    """A &lt;sign&gt; element on a static board defined in the local coordinate
    system of the &lt;signal&gt; element.

    A &lt;sign&gt; element may have all attributes and child elements of
    a signal.

    :ivar v: Local v-coordinate of the sign on the board
    :ivar z: Local z-coordinate of the sign on the board
    """

    class Meta:
        name = "t_road_signals_board_sign"

    v: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    z: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class THeader(OpenDriveElement):
    """
    Contains general information about the ASAM OpenDRIVE file.

    :ivar geo_reference:
    :ivar offset:
    :ivar license:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar default_regulations:
    :ivar date: Time/date of database creation according to ISO 8601
        (preference: YYYY-MM-DDThh:mm:ss)
    :ivar east: Maximum inertial x value
    :ivar name: Database name
    :ivar north: Maximum inertial y value
    :ivar rev_major: Major revision number of OpenDRIVE format
    :ivar rev_minor: Minor revision number of OpenDRIVE format; 6 for
        OpenDrive 1.6
    :ivar south: Minimum inertial y value
    :ivar vendor: Vendor name
    :ivar version: Version of this road network
    :ivar west: Minimum inertial x value
    """

    class Meta:
        name = "t_header"

    geo_reference: Optional[THeaderGeoReference] = field(
        default=None,
        metadata={
            "name": "geoReference",
            "type": "Element",
            "namespace": "",
        },
    )
    offset: Optional[THeaderOffset] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    license: Optional[TLicense] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    default_regulations: Optional[THeaderDefaultRegulations] = field(
        default=None,
        metadata={
            "name": "defaultRegulations",
            "type": "Element",
            "namespace": "",
        },
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    east: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    north: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rev_major: int = field(
        init=False,
        default=1,
        metadata={
            "name": "revMajor",
            "type": "Attribute",
            "required": True,
        },
    )
    rev_minor: Optional[int] = field(
        default=None,
        metadata={
            "name": "revMinor",
            "type": "Attribute",
            "required": True,
        },
    )
    south: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vendor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    west: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TRoadLanesLaneSectionCenter(OpenDriveElement):
    """
    Contains the center lane, which must be defined for all roads.
    """

    class Meta:
        name = "t_road_lanes_laneSection_center"

    lane: Optional[TRoadLanesLaneSectionCenterLane] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadLanesLaneSectionLeftLane(TRoadLanesLaneSectionLrLane):
    """
    Left lanes numbered with positive IDs in ascending order from center lane to
    left border.

    :ivar id: ID of the lane
    """

    class Meta:
        name = "t_road_lanes_laneSection_left_lane"

    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadLanesLaneSectionRightLane(TRoadLanesLaneSectionLrLane):
    """
    Right lanes numbered with negative IDs in descending order from center lane to
    right border.

    :ivar id: ID of the lane
    """

    class Meta:
        name = "t_road_lanes_laneSection_right_lane"

    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TRoadLateralProfileCrossSectionSurface(OpenDriveElement):
    """A cross section surface defines the lateral profile by means of constant,
    linear, quadratic, and cubic polynomials in t-direction.

    A cross section surface is valid for the full length of the road.
    """

    class Meta:
        name = "t_road_lateralProfile_crossSectionSurface"

    t_offset: Optional[TRoadLateralProfileCrossSectionSurfaceTOffset] = field(
        default=None,
        metadata={
            "name": "tOffset",
            "type": "Element",
            "namespace": "",
        },
    )
    surface_strips: Optional[
        TRoadLateralProfileCrossSectionSurfaceSurfaceStrip
    ] = field(
        default=None,
        metadata={
            "name": "surfaceStrips",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadObjects(OpenDriveElement):
    """
    Container for all objects along a road.
    """

    class Meta:
        name = "t_road_objects"

    object_value: List[TRoadObjectsObject] = field(
        default_factory=list,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
        },
    )
    object_reference: List[TRoadObjectsObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "objectReference",
            "type": "Element",
            "namespace": "",
        },
    )
    tunnel: List[TRoadObjectsTunnel] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    bridge: List[TRoadObjectsBridge] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadSignalsStaticBoard(TRoadSignalsBoard):
    """A &lt;signal&gt; element that contains a &lt;staticBoard&gt; element.

    The signs that are displayed on a static board are defined as
    separate &lt;sign&gt; elements.
    """

    class Meta:
        name = "t_road_signals_staticBoard"

    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    sign: List[TRoadSignalsBoardSign] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TJunctionCommon(TJunction):
    """
    Common junctions are the default type of junction in ASAM OpenDRIVE and specify
    areas where drivable lanes may overlap and traffic may cross.

    :ivar connection:
    :ivar cross_path:
    :ivar priority:
    :ivar controller:
    :ivar surface:
    :ivar plan_view:
    :ivar objects:
    :ivar boundary:
    :ivar elevation_grid:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar type_value: Common junctions are of type "default". If the
        attribute is not specified, the junction type is "default". This
        attribute is mandatory for all other junction types.
    """

    class Meta:
        name = "t_junction_common"

    connection: List[TJunctionConnectionCommon] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    cross_path: List[TJunctionCrossPath] = field(
        default_factory=list,
        metadata={
            "name": "crossPath",
            "type": "Element",
            "namespace": "",
        },
    )
    priority: List[TJunctionPriority] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    controller: List[TJunctionController] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    surface: Optional[TRoadSurface] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    plan_view: Optional[TRoadPlanView] = field(
        default=None,
        metadata={
            "name": "planView",
            "type": "Element",
            "namespace": "",
        },
    )
    objects: Optional[TRoadObjects] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    boundary: Optional[TJunctionBoundary] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    elevation_grid: Optional[TJunctionElevationGrid] = field(
        default=None,
        metadata={
            "name": "elevationGrid",
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[EJunctionType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class TJunctionCrossing(TJunction):
    """Crossings are junctions without connecting roads.

    They define sections where crossing traffic can appear. Traffic does
    not change roads at crossings, for example, at railway crossings.

    :ivar road_section:
    :ivar priority:
    :ivar controller:
    :ivar surface:
    :ivar plan_view:
    :ivar objects:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar type_value: Common junctions are of type "default". If the
        attribute is not specified, the junction type is "default". This
        attribute is mandatory for all other junction types.
    """

    class Meta:
        name = "t_junction_crossing"

    road_section: List[TJunctionRoadSection] = field(
        default_factory=list,
        metadata={
            "name": "roadSection",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    priority: List[TJunctionPriority] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    controller: List[TJunctionController] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    surface: Optional[TRoadSurface] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    plan_view: Optional[TRoadPlanView] = field(
        default=None,
        metadata={
            "name": "planView",
            "type": "Element",
            "namespace": "",
        },
    )
    objects: Optional[TRoadObjects] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[EJunctionType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class TJunctionDirect(TJunction):
    """
    Direct junctions are intended to model entries and exits where drivable lanes
    may overlap to split or merge, but traffic does not cross.

    :ivar connection:
    :ivar priority:
    :ivar controller:
    :ivar surface:
    :ivar plan_view:
    :ivar objects:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar type_value: Common junctions are of type "default". If the
        attribute is not specified, the junction type is "default". This
        attribute is mandatory for all other junction types.
    """

    class Meta:
        name = "t_junction_direct"

    connection: List[TJunctionConnectionDirect] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    priority: List[TJunctionPriority] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    controller: List[TJunctionController] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    surface: Optional[TRoadSurface] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    plan_view: Optional[TRoadPlanView] = field(
        default=None,
        metadata={
            "name": "planView",
            "type": "Element",
            "namespace": "",
        },
    )
    objects: Optional[TRoadObjects] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[EJunctionType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class TJunctionVirtual(TJunction):
    """
    Virtual junctions manage connections within an uninterrupted road, for example,
    entries and exits to parking lots, and pedestrian crossings.

    :ivar connection:
    :ivar cross_path:
    :ivar priority:
    :ivar controller:
    :ivar surface:
    :ivar plan_view:
    :ivar objects:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar main_road: The main road from which the connecting roads of
        the virtual junction branch off. This attribute is mandatory for
        virtual junctions and shall not be specified for other junction
        types.
    :ivar orientation: Defines the relevance of the virtual junction
        according to the driving direction. This attribute is mandatory
        for virtual junctions and shall not be specified for other
        junction types. The enumerator "none" specifies that the virtual
        junction is valid in both directions.
    :ivar s_end: End position of the virtual junction in the reference
        line coordinate system. This attribute is mandatory for virtual
        junctions.
    :ivar s_start: Start position of the virtual junction in the
        reference line coordinate system. This attribute is mandatory
        for virtual junctions.
    :ivar type_value: Common junctions are of type "default". If the
        attribute is not specified, the junction type is "default". This
        attribute is mandatory for all other junction types.
    """

    class Meta:
        name = "t_junction_virtual"

    connection: List[
        Union[
            TJunctionConnection,
            TJunctionConnectionVirtual,
            TJunctionConnectionVirtualDefault,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    cross_path: List[TJunctionCrossPath] = field(
        default_factory=list,
        metadata={
            "name": "crossPath",
            "type": "Element",
            "namespace": "",
        },
    )
    priority: List[TJunctionPriority] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    controller: List[TJunctionController] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    surface: Optional[TRoadSurface] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    plan_view: Optional[TRoadPlanView] = field(
        default=None,
        metadata={
            "name": "planView",
            "type": "Element",
            "namespace": "",
        },
    )
    objects: Optional[TRoadObjects] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    main_road: Optional[str] = field(
        default=None,
        metadata={
            "name": "mainRoad",
            "type": "Attribute",
        },
    )
    orientation: Optional[EOrientation] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    s_end: Optional[float] = field(
        default=None,
        metadata={
            "name": "sEnd",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    s_start: Optional[float] = field(
        default=None,
        metadata={
            "name": "sStart",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    type_value: Optional[EJunctionType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class TRoadLanesLaneSectionLeft(OpenDriveElement):
    """
    Contains all lanes left to the center lane.
    """

    class Meta:
        name = "t_road_lanes_laneSection_left"

    lane: List[TRoadLanesLaneSectionLeftLane] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadLanesLaneSectionRight(OpenDriveElement):
    """
    Contains all lanes right to the center lane.
    """

    class Meta:
        name = "t_road_lanes_laneSection_right"

    lane: List[TRoadLanesLaneSectionRightLane] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadLateralProfile(OpenDriveElement):
    """Contains a series of lateral elevation elements that define the
    characteristics of the road surfaces banking along the road reference line.

    The lateral profile is defined relative to the elevation of the road
    reference line.
    """

    class Meta:
        name = "t_road_lateralProfile"

    superelevation: List[TRoadLateralProfileSuperelevation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    shape: List[TRoadLateralProfileShape] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    cross_section_surface: Optional[TRoadLateralProfileCrossSectionSurface] = (
        field(
            default=None,
            metadata={
                "name": "crossSectionSurface",
                "type": "Element",
                "namespace": "",
            },
        )
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadSignalsSignalRoad(TRoadSignalsSignal):
    """Used to provide information about signals along a road.

    Consists of a main element and an optional lane validity element.
    The element for a signal is &lt;signal&gt;.

    :ivar static_board:
    :ivar vms_board:
    :ivar s: s-coordinate
    :ivar t: t-coordinate
    :ivar z_offset: z-offset of signal's origin relative to the
        elevation of the road reference line
    """

    class Meta:
        name = "t_road_signals_signal_road"

    static_board: List[TRoadSignalsStaticBoard] = field(
        default_factory=list,
        metadata={
            "name": "staticBoard",
            "type": "Element",
            "namespace": "",
        },
    )
    vms_board: List[TRoadSignalsVmsBoard] = field(
        default_factory=list,
        metadata={
            "name": "vmsBoard",
            "type": "Element",
            "namespace": "",
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    t: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    z_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "zOffset",
            "type": "Attribute",
        },
    )


@dataclass
class TRoadLanesLaneSection(OpenDriveElement):
    """A lane section splits a road into multiple parts whenever the number of
    lanes or their function changes.

    The distance between two succeeding lane sections shall not be zero.
    For easier navigation through an ASAM OpenDRIVE road description,
    the lanes within a lane section are grouped into left, center, and
    right lanes. Each lane section shall contain one &lt;center&gt;
    element and at least one &lt;right&gt; or &lt;left&gt; element.

    :ivar left:
    :ivar center:
    :ivar right:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar s: s-coordinate of start position
    :ivar single_side: Lane section element is valid for one side only
        (left, center, or right), depending on the child elements.
    """

    class Meta:
        name = "t_road_lanes_laneSection"

    left: Optional[TRoadLanesLaneSectionLeft] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    center: Optional[TRoadLanesLaneSectionCenter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    right: Optional[TRoadLanesLaneSectionRight] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    s: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    single_side: Optional[TBool] = field(
        default=None,
        metadata={
            "name": "singleSide",
            "type": "Attribute",
        },
    )


@dataclass
class TRoadSignals(OpenDriveElement):
    """Signals are traffic signs, traffic lights, and specific road markings for
    the control and regulation of road traffic.

    The &lt;signals&gt; element is the container for all signals along a
    road.
    """

    class Meta:
        name = "t_road_signals"

    signal: List[TRoadSignalsSignalRoad] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    signal_reference: List[TRoadSignalsSignalReference1] = field(
        default_factory=list,
        metadata={
            "name": "signalReference",
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoadLanes(OpenDriveElement):
    """Lanes are an essential part of all roads.

    Lanes are attached to the road reference line and are defined from
    inside to outside. Lanes contain a series of lane section elements
    that define the characteristics of the road cross sections with
    respect to the lanes along the road reference line.
    """

    class Meta:
        name = "t_road_lanes"

    lane_offset: List[TRoadLanesLaneOffset] = field(
        default_factory=list,
        metadata={
            "name": "laneOffset",
            "type": "Element",
            "namespace": "",
        },
    )
    lane_section: List[TRoadLanesLaneSection] = field(
        default_factory=list,
        metadata={
            "name": "laneSection",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TRoad(OpenDriveElement):
    """Roads are the core elements for any road network in ASAM OpenDRIVE.

    Each road runs along one road reference line. A road shall have at
    least the center lane. Vehicles may drive in both directions of the
    road reference line. The standard driving direction is defined by
    the value which is assigned to the @rule attribute (RHT=right-hand
    traffic, LHT=left-han traffic). ASAM OpenDRIVE roads may be roads in
    the real road network or artificial road network created for
    application use. Each road is described by one or more &lt;road&gt;
    elements. One &lt;road&gt; element may cover a long stretch of a
    road, shorter stretches between junctions, or even several roads. A
    new &lt;road&gt; element should only start if the properties of the
    road cannot be described within the previous &lt;road&gt; element or
    if a junction is required.d

    :ivar link:
    :ivar type_value:
    :ivar plan_view:
    :ivar elevation_profile:
    :ivar lateral_profile:
    :ivar lanes:
    :ivar objects:
    :ivar signals:
    :ivar surface:
    :ivar railroad:
    :ivar data_quality:
    :ivar include:
    :ivar user_data:
    :ivar id: Unique ID within the database. If it represents an integer
        number, it should comply to uint32_t and stay within the given
        range.
    :ivar junction: ID of the junction to which the road belongs, for
        example connecting roads, cross paths, and roads of a junction
        boundary. Use -1 for none.
    :ivar length: Total length of the reference line in the xy-plane.
        Change in length due to elevation is not considered
    :ivar name: Name of the road. May be chosen freely.
    :ivar rule: Basic rule for using the road; RHT=right-hand traffic,
        LHT=left-hand traffic. When this attribute is missing, RHT is
        assumed.
    """

    class Meta:
        name = "t_road"

    link: Optional[TRoadLink] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: List[TRoadType] = field(
        default_factory=list,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "",
        },
    )
    plan_view: Optional[TRoadPlanView] = field(
        default=None,
        metadata={
            "name": "planView",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    elevation_profile: Optional[TRoadElevationProfile] = field(
        default=None,
        metadata={
            "name": "elevationProfile",
            "type": "Element",
            "namespace": "",
        },
    )
    lateral_profile: Optional[TRoadLateralProfile] = field(
        default=None,
        metadata={
            "name": "lateralProfile",
            "type": "Element",
            "namespace": "",
        },
    )
    lanes: Optional[TRoadLanes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    objects: Optional[TRoadObjects] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    signals: Optional[TRoadSignals] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    surface: Optional[TRoadSurface] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    railroad: Optional[TRoadRailroad] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    junction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rule: Optional[ETrafficRule] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class OpenDrive:
    class Meta:
        name = "OpenDRIVE"

    header: Optional[THeader] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    road: List[TRoad] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    controller: List[TController] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    junction: List[
        Union[
            TJunction,
            TJunctionVirtual,
            TJunctionDirect,
            TJunctionCrossing,
            TJunctionCommon,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    junction_group: List[TJunctionGroup] = field(
        default_factory=list,
        metadata={
            "name": "junctionGroup",
            "type": "Element",
            "namespace": "",
        },
    )
    station: List[TStation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_quality: List[TDataQuality] = field(
        default_factory=list,
        metadata={
            "name": "dataQuality",
            "type": "Element",
            "namespace": "",
        },
    )
    include: List[TInclude] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_data: List[TUserData] = field(
        default_factory=list,
        metadata={
            "name": "userData",
            "type": "Element",
            "namespace": "",
        },
    )
    vms_group: List[TSignalGroupVmsGroup] = field(
        default_factory=list,
        metadata={
            "name": "vmsGroup",
            "type": "Element",
            "namespace": "",
        },
    )
