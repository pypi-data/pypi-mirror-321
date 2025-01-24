"""

serial_io 是 robotengine 控制硬件串口的节点。

"""

from .node import Node
import serial.tools.list_ports
import serial
from enum import Enum
import random
from robotengine.tools import hex2str, warning, error, info

class DeviceType(Enum):
    """ 设备类型枚举 """
    STM32F407 = 0
    """ STM32F407 设备类型 """
    ARDUINO_MEGA2560 = 1
    """ Arduino Mega2560 设备类型 """

class CheckSumType(Enum):
    """ 校验和类型枚举 """
    NONE = 0
    """ 无校验和 """
    SUM8 = 1
    """ SUM8 校验和 """
    SUM16 = 2
    """ SUM16 校验和 """
    XOR8 = 3
    """ XOR8 校验和 """
    XOR16 = 4
    """ XOR16 校验和 """
    CRC8 = 5
    """ CRC8 校验和 """
    CRC16 = 6
    """ CRC16 校验和 """

checksum_length_map = {
        CheckSumType.SUM8: 1,
        CheckSumType.SUM16: 2,
        CheckSumType.XOR8: 1,
        CheckSumType.XOR16: 2,
        CheckSumType.CRC8: 1,
        CheckSumType.CRC16: 2
    }
""" 校验和长度映射表 """

class SerialIO(Node):
    """ 串口节点 """
    def __init__(self, name="SerialIO", device_type=DeviceType.STM32F407, checksum_type=CheckSumType.NONE, header=[], baudrate=115200, timeout=1.0, warn=True):
        """ 
        初始化串口节点。

            :param name: 节点名称。
            :param device_type: 设备类型。
            :param checksum_type: 校验和类型。
            :param header: 数据头。
            :param baudrate: 波特率。
            :param timeout: 超时时间。
        """
        super().__init__(name)
        self._device_type = device_type
        self._checksum_type = checksum_type
        self._header = header
        self._header_flag = 0
        self._device = None
        self._serial: serial.Serial = None
        self._baudrate = baudrate
        self._timeout = timeout

        self._warn = warn
        self._receive_data = bytes()

        self._initialize()
        if self._device is None and self._warn:
            warning(f"节点 {self.name} 初始化时未检测到 {self._device_type} 设备，将在内部更新中继续尝试")

    def _update(self, delta) -> None:
        if self._device is None:
            self._initialize()
            return
        
    def _initialize(self):
        self._device = self._find_device()
        if self._device:
            try:
                info(f"节点 {self.name} 初始化时检测到 {self._device_type} 设备，串口为 {self._device}，波特率为 {self._baudrate}")
                self._serial = serial.Serial(self._device, self._baudrate, timeout=self._timeout)
                # 清空串口缓冲区
                self._serial.reset_input_buffer()
                self._serial.reset_output_buffer()
            except serial.SerialException as e:
                error(f"节点 {self.name} 尝试打开串口 {self._device} 失败，错误信息为 {e}")
                self._device = None
                self._serial = None

    def _find_device(self):
        if self._device_type == DeviceType.STM32F407:
            target_vid = 0x1A86
            target_pid = 0x7523
        elif self._device_type == DeviceType.ARDUINO_MEGA2560:
            target_vid = 0x2341
            target_pid = 0x0043

        ports = serial.tools.list_ports.comports()
        for port in ports:
            if port.vid == target_vid and port.pid == target_pid:
                return port.device
        return None
    
    def _get_check_sum(self, data: bytes) -> bytes:
        if self._checksum_type == CheckSumType.SUM8:
            check_sum = sum(data) & 0xFF
            return bytes([check_sum])
        elif self._checksum_type == CheckSumType.SUM16:
            check_sum = sum(data) & 0xFFFF
            return check_sum.to_bytes(2, byteorder='big')
        elif self._checksum_type == CheckSumType.XOR8:
            check_sum = 0
            for byte in data:
                check_sum ^= byte
            return bytes([check_sum])
        elif self._checksum_type == CheckSumType.XOR16:
            check_sum = 0
            for byte in data:
                check_sum ^= byte
            return check_sum.to_bytes(2, byteorder='big')
        elif self._checksum_type == CheckSumType.CRC8:
            crc = 0x00
            polynomial = 0x07
            for byte in data:
                crc ^= byte
                for _ in range(8):
                    if crc & 0x80:
                        crc = (crc << 1) ^ polynomial
                    else:
                        crc <<= 1
                    crc &= 0xFF
            return bytes([crc])
        elif self._checksum_type == CheckSumType.CRC16:
            crc = 0xFFFF
            polynomial = 0x8005
            for byte in data:
                crc ^= byte
                for _ in range(8):
                    if crc & 0x0001:
                        crc = (crc >> 1) ^ polynomial
                    else:
                        crc >>= 1  # 否则仅右移
            return crc.to_bytes(2, byteorder='big')
        else:
            raise ValueError("无效的校验和类型")
            
    def _add_header(self, data: bytes) -> bytes:
        return bytes(self._header) + data
    
    def random_bytes(self, length: int) -> bytes:
        """ 生成随机字节 """
        return bytes([random.randint(0, 255) for _ in range(length)])
    
    def fixed_bytes(self, byte: int, length: int) -> bytes:
        """ 生成固定字节 """
        return bytes([byte for _ in range(length)])
    
    def transmit(self, data: bytes) -> bytes:
        """ 发送串口数据 """
        if self._serial is None:
            if self._warn:
                warning(f"节点 {self.name} 串口未初始化，无法发送数据")
            return
        if self._checksum_type !=CheckSumType.NONE:
            data += self._get_check_sum(data)
        if self._header:
            data = self._add_header(data)
        self._serial.write(data)
        return data
    
    def receive(self, length: int) -> bytes:
        """ 
        接收串口数据 
        
            :param len: 接收数据的长度
        """
        if self._serial is None:
            if self._warn:
                warning(f"节点 {self.name} 串口未初始化，无法接收数据")
            return
        
        in_waiting = self._serial.in_waiting
        if in_waiting == 0:
            return None
        
        if self._header and self._header_flag < len(self._header):
            target_data = self._header[self._header_flag]
            data = self._serial.read(1)
            if ord(data) == target_data:
                self._header_flag += 1
                self._receive_data += data
            else:
                self._header_flag = 0
                self._receive_data = bytes()
            return None
        
        pending_length = length - len(self._receive_data)
        self._receive_data += self._serial.read(min(in_waiting, pending_length))
        if len(self._receive_data) >= length:
            data = self._receive_data[:length]
            self._receive_data = self._receive_data[length:]
            self._header_flag = 0
            return data
        else:
            return None
        
            
    # def receive(self, length: int) -> bytes:
    #     """ 
    #     接收串口数据 
        
    #         :param len: 接收数据的长度
    #     """
    #     if self._serial is None:
    #         if self._warn:
    #             warning(f"节点 {self.name} 串口未初始化，无法接收数据")
    #         return
        
    #     in_waiting = self._serial.in_waiting
    #     pending_length = length - len(self._receive_data)
    #     if in_waiting >= 0:
    #         self._receive_data += self._serial.read(min(in_waiting, pending_length))
    #         if len(self._receive_data) >= length:
    #             data = self._receive_data[:length]
    #             self._receive_data = self._receive_data[length:]
    #             return data
    #         else:
    #             return None
    #     else:
    #         return None
        
    def check_sum(self, data: bytes) -> bool:
        """ 校验串口数据 """
        if self._checksum_type == CheckSumType.NONE:
            return True
        checksum_length = checksum_length_map.get(self._checksum_type)
        if checksum_length is None:
            raise ValueError("无效的校验和类型，无法进行校验")

        data_to_check = data[len(self._header):-checksum_length]
        expected_checksum = data[-checksum_length:]
        calculated_checksum = self._get_check_sum(data_to_check)

        return calculated_checksum == expected_checksum

    def __del__(self):
        if self._serial:
            self._serial.close()