import struct
import io
from typing import Optional
from modbuspy import logger
from modbuspy.ADU import MODBUS_EXCEPTION_MESSAGES


class RTUADU:
    def __init__(
        self, unit_id: Optional[int] = None, pdu: Optional[bytes] = None
    ) -> None:
        """Initializes a SerialADU instance.

        Args:
            address (int): The address of the device.
            pdu (bytes): The Protocol Data Unit (PDU).
        """
        self._unit_id = unit_id
        self._pdu = pdu

    @property
    def unit_id(self) -> int:
        if self._unit_id is None:
            raise ValueError("unit_id is not set")
        return self._unit_id

    @unit_id.setter
    def unit_id(self, value: int) -> None:
        self._unit_id = value

    @property
    def pdu(self) -> bytes:
        if self._pdu is None:
            raise ValueError("pdu is not set")
        return self._pdu

    @pdu.setter
    def pdu(self, value: bytes) -> None:
        self._pdu = value

    @property
    def crc(self) -> bytes:
        data = struct.pack("B", self.unit_id) + self.pdu
        crc = 0xFFFF
        for pos in data:
            crc ^= pos
            for _ in range(8):
                if (crc & 1) != 0:
                    crc = (crc >> 1) ^ 0xA001
                else:
                    crc >>= 1
        return struct.pack("<H", crc)


    def is_error(self) -> tuple[bool, str]:
        if self.pdu[0] >= 0x80:
            exception_code = self.pdu[1]
            err = MODBUS_EXCEPTION_MESSAGES.get(
                exception_code, "Unknown exception code"
            )
            return True, err
        return False, ""

    def to_bytes(self) -> bytes:
        """Converts the SerialADU instance to bytes.

        Returns:
            bytes: The byte representation of the SerialADU instance.
        """
        try:
            buffer = io.BytesIO()
            buffer.write(struct.pack("B", self.unit_id))
            buffer.write(self.pdu)
            buffer.write(self.crc)
            return buffer.getvalue()
        except Exception as e:
            raise ValueError(f"failed to convert SerialADU to bytes: {e}")

    def from_bytes(self, data: bytes) -> None:
        """Initializes the SerialADU instance from bytes.

        Args:
            data (bytes): The byte data to initialize the instance from.

        Raises:
            ValueError: If the data is too short or the CRC check fails.
        """
        try:
            buffer = io.BytesIO(data)
            self.unit_id = struct.unpack("B", buffer.read(1))[0]
            self.pdu = buffer.read(len(data) - 3)
            crc = buffer.read(2)
            if crc != self.crc:
                raise ValueError(
                    f"CRC mismatch: expected {[int(b) for b in self.crc]}, got {[int(b) for b in crc]}"
                )
        except Exception as e:
            raise ValueError(f"failed to parse SerialADU: {e}")
