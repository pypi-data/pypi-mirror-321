# (c) Meta Platforms, Inc. and affiliates.
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

import dataclasses as dc
import logging
import os
import typing as ty

from pci_lmt.constants import EXPRESS_SPEED

logger: logging.Logger = logging.getLogger(__name__)


@dc.dataclass
class CapabilityInfo:  # pylint: disable=too-few-public-methods
    # FIXME: should this error msg really be part of capability info or is it just a mechanism
    # to report errors while detecting pci caps? likely the second, so should be removed.
    # This would also make all of these optionals unnecessary, since objects can be fully constructed
    # as opposed to being in an union state of either 1. err_msg is valid and none others or 2. err_msg
    # is invalid and all others are valid. It is basically impossible to write correct code to handle this
    err_msg: ty.Optional[str]
    id: ty.Optional[int]
    version: ty.Optional[int]
    offset: ty.Optional[int]
    offset_next: int


@dc.dataclass
class LinkStatusInfo:  # pylint: disable=too-few-public-methods
    err_msg: ty.Optional[str]
    speed: ty.Optional[int]
    speed_gts: ty.Optional[str]
    width: ty.Optional[int]


class PciDevice:
    """
    Model a PCI express device and operations.
    """

    PCI_EXPRESS_CAP_ID = 0x10
    PCI_LMT_EXT_CAP_ID = 0x27
    LINK_STATUS_REG_OFFSET = 0x12
    CAPABILITIES_POINTER = 0x34
    EXTENDED_CAPABILITIES_POINTER = 0x100

    # Helper maps.
    width_str = {8: "b", 16: "w", 32: "l"}
    speed_gts = EXPRESS_SPEED

    def __init__(self, bdf: str) -> None:
        """
        Initialize the PCI library with the given Bus:Device:Function info.
        Args: bdf: Bus:Device:Function info
        """
        self.bdf = bdf
        self.cap_dict: ty.Dict[ty.Any, CapabilityInfo] = {}
        self.ext_cap_dict: ty.Dict[ty.Any, CapabilityInfo] = {}

    def read(self, address, width=32) -> int:
        """Helper to read PCI config space register at the given address."""
        if address < 0 or address >= 0xFFF:
            print(f"BDF:{self.bdf} Invalid address {hex(address)}")
            return -1

        if width not in self.width_str:
            print(f"BDF:{self.bdf} Invalid width {width}")
            return -1
        width_str = self.width_str[width]

        data: int = -1
        try:
            data = int(
                "0x" + os.popen(f"setpci -s {self.bdf} {hex(address)}.{width_str}").readlines()[0].split("\n")[0],
                16,
            )
        except BaseException as e:  # pylint: disable=broad-exception-caught # FIXME
            print(f"BDF:{self.bdf} Could not read PCI reg at address {hex(address)}. Exception:{e}")
            return -1

        logger.debug("BDF:%s Data read from address 0x%x : 0x%x", self.bdf, address, data)
        return data

    def write(self, address, data, width=32) -> int:
        """Helper to write PCI config space register at the given address."""
        if address < 0 or address >= 0xFFF:
            print(f"BDF:{self.bdf} Invalid address {hex(address)}")
            return -1

        if width not in self.width_str:
            print(f"BDF:{self.bdf} Invalid width {width}")
            return -1
        width_str = self.width_str[width]

        try:
            os.popen(f"setpci -s {self.bdf} {hex(address)}.{width_str}={hex(data)}")
        except BaseException as e:  # pylint: disable=broad-exception-caught # FIXME
            print(f"BDF:{self.bdf} Could not write PCI reg at address {hex(address)}. Exception:{e}")
            return -1

        logger.debug("BDF:%s Data written to address 0x%x : 0x%x", self.bdf, address, data)
        return 0

    def create_dict_capabilities(self):
        """Creates a dictionary mapping capability IDs to capability info."""

        def decode_capability(address) -> CapabilityInfo:
            """Decodes the capability info at the given address."""
            data = self.read(address=address, width=32)
            if data in (-1, 0xFFFFFFFF):
                cap_info = CapabilityInfo(
                    err_msg=f"ERROR: BDF {self.bdf} decode_capability address {hex(address)}",
                    id=None,
                    version=None,
                    offset=None,
                    offset_next=0,
                )
            else:
                cap_info = CapabilityInfo(
                    err_msg=None,
                    id=(data >> 0) & 0xFF,  # 7:0 Capability ID
                    version=(data >> 16) & 0x7,  # 18:16 Capability Version
                    offset=address,
                    offset_next=(data >> 8) & 0xFC,  # 15:8 Next Capability Offset
                    # The bottom two bits are Reserved and must be set to 00b.
                    # Software must mask these bits off before using this register as a
                    # pointer in Configuration Space to the first entry of a linked list of new capabilities.
                )

            logger.debug(cap_info)
            return cap_info

        # Return if the dictionary is already populated.
        if len(self.cap_dict) != 0:
            return

        offset_next = self.read(address=self.CAPABILITIES_POINTER, width=32)
        while offset_next not in (0, -1):
            cap_info = decode_capability(address=offset_next)
            self.cap_dict[cap_info.id] = cap_info
            offset_next = cap_info.offset_next

    def create_dict_extended_capabilities(self):
        """Creates a dictionary mapping extended capability IDs to capability info."""

        def decode_extended_capability(address) -> CapabilityInfo:
            """Decodes the extended capability info at the given address."""
            data = self.read(address=address, width=32)
            if data == -1:
                cap_info = CapabilityInfo(
                    err_msg=f"ERROR: BDF:{self.bdf} decode_extended_capability address {hex(address)}",
                    id=None,
                    version=None,
                    offset=None,
                    offset_next=0,
                )
            else:
                cap_info = CapabilityInfo(
                    err_msg=None,
                    id=(data >> 0) & 0xFFFF,  # 15:0 Capability ID
                    version=(data >> 16) & 0xF,  # 19:16 Capability Version
                    offset=address,
                    offset_next=(data >> 20) & 0xFFF,  # 31:20 Next Capability Offset
                )

            logger.debug(cap_info)
            return cap_info

        # Return if the dictionary is already populated.
        if len(self.ext_cap_dict) != 0:
            return

        offset_next = self.EXTENDED_CAPABILITIES_POINTER
        while offset_next not in (0, -1):
            cap_info = decode_extended_capability(address=offset_next)
            self.ext_cap_dict[cap_info.id] = cap_info
            offset_next = cap_info.offset_next

    def get_link_status(self) -> LinkStatusInfo:
        """Returns the link status of the PCI device."""
        # FIXME: this is likely not the place to populate an instance field; this detection should be
        # part of __init__ and get an object correct by construction
        self.create_dict_capabilities()

        if self.PCI_EXPRESS_CAP_ID not in self.cap_dict:
            err_msg = f"BDF:{self.bdf} PCI Express capability not found"
            logger.warning(err_msg)
            return LinkStatusInfo(
                err_msg=err_msg,
                speed=None,
                speed_gts=None,
                width=None,
            )

        # FIXME: need to cast to int because at this point the `offset` field is optional, so
        # it may have a None in it, which cannot be used with addition
        offset = ty.cast(int, self.cap_dict[self.PCI_EXPRESS_CAP_ID].offset) + self.LINK_STATUS_REG_OFFSET
        data = self.read(address=offset, width=16)
        if data == -1:
            err_msg = f"BDF:{self.bdf} Couldn't read Link status"
            logger.warning(err_msg)
            return LinkStatusInfo(
                err_msg=err_msg,
                speed=None,
                speed_gts=None,
                width=None,
            )

        # Current Link Speed – This field indicates the negotiated Link speed of the given PCI Express Link.
        # The encoded value specifies a bit location in the Supported Link Speeds Vector (in the Link Capabilities
        # 2 register) that corresponds to the current Link speed.
        # Defined encodings are:
        # 0001b Supported Link Speeds Vector field bit 0
        # 0010b Supported Link Speeds Vector field bit 1
        # 0011b Supported Link Speeds Vector field bit 2
        # 0100b Supported Link Speeds Vector field bit 3
        # 0101b Supported Link Speeds Vector field bit 4
        # 0110b Supported Link Speeds Vector field bit 5
        # 0111b Supported Link Speeds Vector field bit 6
        # All other encodings are Reserved.
        # The value in this field is undefined when the Link is not up.
        speed = (data >> 0) & 0xF  # 3:0
        speed_gts = self.speed_gts.get(speed, "Unknown")

        # Negotiated Link Width – This field indicates the negotiated width of the given PCI Express Link.
        # Defined encodings are: 00 0001b x1
        # 00 0010b x2
        # 00 0100b x4
        # 00 1000b x8 00 1100b x12 01 0000b x16 10 0000b x32
        # All other encodings are Reserved. The value in this field is undefined when the Link is not up.
        width = (data >> 4) & 0x3F  # 9:4
        logger.debug("BDF:%s Link speed %d '%s' and width %d", self.bdf, speed, speed_gts, width)
        return LinkStatusInfo(err_msg=None, speed=speed, speed_gts=speed_gts, width=width)

    def get_lmt_cap_info(self) -> CapabilityInfo:
        """Returns the Lane Margining Capability info."""
        # FIXME: this is likely not the place to populate an instance field; this detection should be
        # part of __init__ and get an object correct by construction
        self.create_dict_extended_capabilities()

        if self.PCI_LMT_EXT_CAP_ID not in self.ext_cap_dict:
            err_msg = f"BDF:{self.bdf} PCI LMT capability not found"
            logger.warning(err_msg)
            return CapabilityInfo(
                err_msg=err_msg,
                id=None,
                version=None,
                offset=None,
                offset_next=0,
            )

        return self.ext_cap_dict[self.PCI_LMT_EXT_CAP_ID]
