import asyncio
import serial_asyncio

from modbuspy import logger
from modbuspy.ADU.RTUADU import RTUADU
from modbuspy.Client import Client
from modbuspy.PDU.ClientPDU import (
    PDUReadCoils,
    PDUReadDiscreteInputs,
    PDUReadHoldingRegisters,
    PDUReadInputRegisters,
    PDUWriteMultipleCoils,
    PDUWriteMultipleRegisters,
    PDUWriteSingleCoil,
    PDUWriteSingleRegister,
)


class RTUClient(Client):
    def __init__(
        self,
        port: str,
        baudrate: int = 9600,
        bytesize: int = 8,
        parity: str = "N",
        stopbits: int = 1,
        timeout: float = 1.0,
    ) -> None:
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        self.timeout = timeout

    async def connect(self) -> None:
        """
        Establishes a connection to the Modbus server.
        """
        self._reader, self._writer = await serial_asyncio.open_serial_connection(
            url=self.port,
            baudrate=self.baudrate,
            bytesize=self.bytesize,
            parity=self.parity,
            stopbits=self.stopbits,
            timeout=self.timeout,
        )

    async def close(self) -> None:
        """
        Closes the connection to the Modbus server.
        """
        if self.writer:
            self.writer.close()
            await self.writer.wait_closed()
        if self.reader:
            self.reader.feed_eof()

    async def send_request(
        self,
        unit_id: int,
        pdu: (
            PDUReadCoils
            | PDUReadDiscreteInputs
            | PDUReadHoldingRegisters
            | PDUReadInputRegisters
            | PDUWriteMultipleCoils
            | PDUWriteMultipleRegisters
            | PDUWriteSingleCoil
            | PDUWriteSingleRegister
        ),
    ) -> None:
        serial_adu = RTUADU(unit_id, pdu.to_bytes())
        buffer = serial_adu.to_bytes()
        self.writer.write(buffer)
        logger.debug(f"Client sent request: {[int(b) for b in buffer]}")

    async def read_response(self) -> RTUADU:
        await asyncio.sleep(0.5)
        # Read bytes from the serial connection
        adu_bytes = await self.reader.read(512)
        logger.debug(f"Client received response: {[int(b) for b in adu_bytes]}")
            
        adu = RTUADU()
        adu.from_bytes(adu_bytes)
        return adu
