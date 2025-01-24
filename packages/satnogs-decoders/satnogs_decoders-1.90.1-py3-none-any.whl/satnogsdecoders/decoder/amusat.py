# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Amusat(KaitaiStruct):
    """:field flag1: amusat.flag1
    :field ax25_header: amusat.ax25_header
    :field dest_address: amusat.ax25_header.dest_address
    :field dest_ssid: amusat.ax25_header.dest_ssid
    :field src_address: amusat.ax25_header.src_address
    :field src_ssid: amusat.ax25_header.src_ssid
    :field control_id: amusat.ax25_header.control_id
    :field pid: amusat.ax25_header.pid
    :field information_field: amusat.information_field
    :field packet_type: amusat.information_field.packet_type
    :field telemetry_data_1: amusat.information_field.telemetry_data_1
    :field sensor1: amusat.information_field.telemetry_data_1.sensor1
    :field sensor2: amusat.information_field.telemetry_data_1.sensor2
    :field sensor3: amusat.information_field.telemetry_data_1.sensor3
    :field sensor4: amusat.information_field.telemetry_data_1.sensor4
    :field battery_voltage: amusat.information_field.telemetry_data_1.battery_voltage
    :field battery_temperature: amusat.information_field.telemetry_data_1.battery_temperature
    :field battery_soc: amusat.information_field.telemetry_data_1.battery_soc
    :field battery_current: amusat.information_field.telemetry_data_1.battery_current
    :field temp_in: amusat.information_field.telemetry_data_1.temp_in
    :field temp_out: amusat.information_field.telemetry_data_1.temp_out
    :field temp_3: amusat.information_field.telemetry_data_1.temp_3
    :field pl_temp: amusat.information_field.telemetry_data_1.pl_temp
    :field rtc: amusat.information_field.telemetry_data_1.rtc
    :field temp_out_l: amusat.information_field.telemetry_data_1.temp_out_l
    :field temp_out_h: amusat.information_field.telemetry_data_1.temp_out_h
    :field acceleration_x: amusat.information_field.telemetry_data_1.acceleration_x
    :field acceleration_y: amusat.information_field.telemetry_data_1.acceleration_y
    :field acceleration_z: amusat.information_field.telemetry_data_1.acceleration_z
    :field magnetic_field_x: amusat.information_field.telemetry_data_1.magnetic_field_x
    :field magnetic_field_y: amusat.information_field.telemetry_data_1.magnetic_field_y
    :field magnetic_field_z: amusat.information_field.telemetry_data_1.magnetic_field_z
    :field angular_rate_x: amusat.information_field.telemetry_data_1.angular_rate_x
    :field angular_rate_y: amusat.information_field.telemetry_data_1.angular_rate_y
    :field angular_rate_z: amusat.information_field.telemetry_data_1.angular_rate_z
    :field velocity: amusat.information_field.telemetry_data_1.velocity
    :field latitude: amusat.information_field.telemetry_data_1.latitude
    :field longitude: amusat.information_field.telemetry_data_1.longitude
    :field gps_time: amusat.information_field.telemetry_data_1.gps_time
    :field solar_deployment_status: amusat.information_field.telemetry_data_1.solar_deployment_status
    :field eps_health_status: amusat.information_field.telemetry_data_1.eps_health_status
    :field adcs_health_status: amusat.information_field.telemetry_data_1.adcs_health_status
    :field payload_health_status: amusat.information_field.telemetry_data_1.payload_health_status
    :field com_health_status: amusat.information_field.telemetry_data_1.com_health_status
    :field battery1_health_status: amusat.information_field.telemetry_data_1.battery1_health_status
    :field battery2_health_status: amusat.information_field.telemetry_data_1.battery2_health_status
    :field image_data_0: amusat.information_field.image_data_0
    :field image_number: amusat.information_field.image_data_0.image_number
    :field total_image_packets: amusat.information_field.image_data_0.total_image_packets
    :field image_packet_number: amusat.information_field.image_data_0.image_packet_number
    :field payload_array_size: amusat.information_field.image_data_0.payload_array_size
    :field payload_data: amusat.information_field.image_data_0.payload_data
    :field fcs: amusat.fcs
    :field flag2: amusat.flag2
    
    .. seealso::
       Source - https://smallsatgasteam.github.io/GASPACS-Comms-Info/
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.flag1 = self._io.read_u1()
        self.ax25_header = Amusat.Ax25HeaderStruct(self._io, self, self._root)
        self.information_field = Amusat.InformationFieldStruct(self._io, self, self._root)
        self.fcs = self._io.read_u2be()
        self.flag2 = self._io.read_u1()

    class Ax25HeaderStruct(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.dest_address = (self._io.read_bytes(7)).decode(u"ASCII")
            self.dest_ssid = self._io.read_u1()
            self.src_address = (self._io.read_bytes(7)).decode(u"ASCII")
            self.src_ssid = self._io.read_u1()
            self.control_id = self._io.read_u1()
            self.pid = self._io.read_u1()


    class InformationFieldStruct(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.packet_type = self._io.read_u1()
            if self.packet_type == 1:
                self.telemetry_data_1 = Amusat.TelemetryDataStruct1(self._io, self, self._root)

            if self.packet_type == 0:
                self.image_data_0 = Amusat.ImageDataStruct0(self._io, self, self._root)



    class TelemetryDataStruct1(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sensor1 = self._io.read_f4be()
            self.sensor2 = self._io.read_f4be()
            self.sensor3 = self._io.read_f4be()
            self.sensor4 = self._io.read_f4be()
            self.battery_voltage = self._io.read_f4be()
            self.battery_temperature = self._io.read_f4be()
            self.battery_soc = self._io.read_f4be()
            self.battery_current = self._io.read_f4be()
            self.temp_in = self._io.read_u1()
            self.temp_out = self._io.read_u1()
            self.temp_3 = self._io.read_u1()
            self.pl_temp = self._io.read_u1()
            self.rtc = self._io.read_u8be()
            self.temp_out_l = self._io.read_u1()
            self.temp_out_h = self._io.read_u1()
            self.acceleration_x = self._io.read_f4be()
            self.acceleration_y = self._io.read_f4be()
            self.acceleration_z = self._io.read_f4be()
            self.magnetic_field_x = self._io.read_f4be()
            self.magnetic_field_y = self._io.read_f4be()
            self.magnetic_field_z = self._io.read_f4be()
            self.angular_rate_x = self._io.read_f4be()
            self.angular_rate_y = self._io.read_f4be()
            self.angular_rate_z = self._io.read_f4be()
            self.velocity = self._io.read_f4be()
            self.latitude = self._io.read_f4be()
            self.longitude = self._io.read_f4be()
            self.gps_time = self._io.read_u8be()
            self.solar_deployment_status = self._io.read_bits_int_be(1) != 0
            self.eps_health_status = self._io.read_bits_int_be(1) != 0
            self.adcs_health_status = self._io.read_bits_int_be(1) != 0
            self.payload_health_status = self._io.read_bits_int_be(1) != 0
            self.com_health_status = self._io.read_bits_int_be(1) != 0
            self.battery1_health_status = self._io.read_bits_int_be(1) != 0
            self.battery2_health_status = self._io.read_bits_int_be(1) != 0


    class ImageDataStruct0(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.image_number = self._io.read_u1()
            self.total_image_packets = self._io.read_u1()
            self.image_packet_number = self._io.read_u1()
            self.payload_array_size = self._io.read_u1()
            self.payload_data = self._io.read_bits_int_be(251)



