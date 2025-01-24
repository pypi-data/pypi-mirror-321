import ctypes
from collections.abc import Callable
from typing import Self
from pyautd3.derive import datagram
from pyautd3.derive import gain
from pyautd3.derive.derive_datagram import datagram_with_segment
from pyautd3.driver.datagram.gain import Gain
from pyautd3.driver.firmware.fpga import Drive
from pyautd3.driver.firmware.fpga.emit_intensity import EmitIntensity
from pyautd3.driver.firmware.fpga.phase import Phase
from pyautd3.driver.geometry import Device
from pyautd3.driver.geometry import Geometry
from pyautd3.driver.geometry import Transducer
from pyautd3.native_methods.autd3_core import Drive as _Drive
from pyautd3.native_methods.autd3capi import NativeMethods as Base
from pyautd3.native_methods.autd3capi_driver import ConstPtr
from pyautd3.native_methods.autd3capi_driver import GainPtr
from pyautd3.native_methods.autd3capi_driver import GeometryPtr
from pyautd3.gain.cache import Cache
from pyautd3.utils import Duration
from pyautd3.driver.datagram.with_timeout import DatagramWithTimeout
from pyautd3.driver.datagram.with_parallel_threshold import DatagramWithParallelThreshold
from pyautd3.native_methods.autd3capi_driver import TransitionModeWrap
from pyautd3.native_methods.autd3_core import Segment
from pyautd3.driver.datagram.with_segment import DatagramWithSegment



class Custom(Gain):
    def __init__(self: Custom, f: Callable[[Device], Callable[[Transducer], Drive | EmitIntensity | Phase | tuple]]) -> None: ...
    def _gain_ptr(self: Custom, geometry: Geometry) -> GainPtr: ...
    def with_cache(self: Custom, ) -> Cache[Custom]: ...
    def with_timeout(self: Custom, timeout: Duration | None) -> DatagramWithTimeout[Custom]: ...
    def with_parallel_threshold(self: Custom, threshold: int | None) -> DatagramWithParallelThreshold[Custom]: ...
    def with_segment(self: Custom, segment: Segment, transition_mode: TransitionModeWrap | None) -> DatagramWithSegment[Custom]: ...
