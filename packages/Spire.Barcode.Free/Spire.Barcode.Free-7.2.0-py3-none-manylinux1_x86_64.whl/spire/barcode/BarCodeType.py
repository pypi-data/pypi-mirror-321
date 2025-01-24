from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.barcode import *
from ctypes import *
import abc

class BarCodeType(Enum):
    """

    """
    Codabar = 1
    Code11 = 2
    Code25 = 3
    Interleaved25 = 4
    Code39 = 5
    Code39Extended = 6
    Code93 = 7
    Code93Extended = 8
    Code128 = 9
    EAN8 = 10
    EAN13 = 11
    EAN128 = 12
    EAN14 = 13
    QRCode = 24
    

