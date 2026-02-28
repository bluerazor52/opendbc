""" AUTO-FORMATTED USING opendbc/car/debug/format_fingerprints.py, EDIT STRUCTURE THERE."""
from opendbc.car.structs import CarParams
from opendbc.car.subaru.values import CAR

Ecu = CarParams.Ecu

FW_VERSIONS = {
  CAR.SUBARU_IMPREZA_2020: {
    (Ecu.abs, 0x7b0, None): [
      b'\xa2 \x193\x00',
      b'\xa2 \x194\x00',
      b'\xa2  `\x00',
      b'\xa2 !3\x00',
      b'\xa2 !6\x00',
      b'\xa2 !`\x00',
      b'\xa2 !i\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'\n\xc0\x04\x00',
      b'\n\xc0\x04\x01',
      b'\x9a\xc0\x00\x00',
      b'\x9a\xc0\x04\x00',
      b'\x9a\xc0\n\x01',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00eb\x1f@ "',
      b'\x00\x00eq\x00\x00\x00\x00',
      b'\x00\x00eq\x1f@ "',
      b'\x00\x00e\x8f\x00\x00\x00\x00',
      b'\x00\x00e\x8f\x1f@ )',
      b'\x00\x00e\x92\x00\x00\x00\x00',
      b'\x00\x00e\xa4\x00\x00\x00\x00',
      b'\x00\x00e\xa4\x1f@ (',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xca!`0\x07',
      b'\xca!`p\x07',
      b'\xca!`t\x07',
      b'\xca!a0\x07',
      b'\xca!ap\x07',
      b'\xca!f@\x07',
      b'\xca!fp\x07',
      b'\xcaacp\x07',
      b'\xcc!`p\x07',
      b'\xcc!fp\x07',
      b'\xcc"f0\x07',
      b'\xe6!`@\x07',
      b'\xe6!fp\x07',
      b'\xe6"f0\x07',
      b'\xe6"fp\x07',
      b'\xf3"f@\x07',
      b'\xf3"fp\x07',
      b'\xf3"fr\x07',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xe6\x15\x042\x00',
      b'\xe6\xf5\x04\x00\x00',
      b'\xe6\xf5$\x00\x00',
      b'\xe6\xf5D0\x00',
      b'\xe7\xf5\x04\x00\x00',
      b'\xe7\xf5D0\x00',
      b'\xe7\xf6B0\x00',
      b'\xe9\xf5"\x00\x00',
      b'\xe9\xf5B0\x00',
      b'\xe9\xf6B0\x00',
      b'\xe9\xf6F0\x00',
    ],
  },
}
