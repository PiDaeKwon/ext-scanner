#from bs4 import *

# from "https://www.garykessler.net/library/file_sigs.html"
signature_dic = [
    # document file
    {'ext': '.hwp', 'hex': 'D0 CF 11 E0 A1 B1 1A E1', 'byte': 8},
    {'ext': '.ico', 'hex': '00 00 01 00', 'byte': 4},
    {'ext': '.pdf', 'hex': '25 50 44 46', 'byte': 4},
    {'ext': '.docx', 'hex': '50 4B 03 04', 'byte': 4},
    {'ext': '.pptx', 'hex': '50 4B 03 04', 'byte': 4},
    {'ext': '.xlsx', 'hex': '50 4B 03 04', 'byte': 4},
    {'ext': '.fdf', 'hex': '25 50 44 46', 'byte': 4},
    {'ext': '.jar', 'hex': '4A 41 52 43 53 00', 'byte': 6},
    # microsoft system file
    {'ext': '.obj', 'hex': '4C 01', 'byte': 2},
    {'ext': '.exe', 'hex': '4D 5A', 'byte': 2},
    {'ext': '.dll', 'hex': '4D 5A', 'byte': 2},
    {'ext': '.sys', 'hex': '4D 5A', 'byte': 2},
    {'ext': '.qtx', 'hex': '4D 5A', 'byte': 2},
    {'ext': '.ocx', 'hex': '4D 5A', 'byte': 2},
    {'ext': '.olb', 'hex': '4D 5A', 'byte': 2},
    {'ext': '.scr', 'hex': '4D 5A', 'byte': 2},
    {'ext': '.vbx', 'hex': '4D 5A', 'byte': 2},
    {'ext': '.acm', 'hex': '4D 5A', 'byte': 2},
    {'ext': '.pif', 'hex': '4D 5A', 'byte': 2},
    {'ext': '.com', 'hex': '4D 5A', 'byte': 2},
    {'ext': '.drv', 'hex': '4D 5A', 'byte': 2},
    {'ext': '.vxd', 'hex': '4D 5A', 'byte': 2},
    {'ext': '.qts', 'hex': '4D 5A', 'byte': 2},
    # image file
    {'ext': '.img', 'hex': '50 49 43 54 00 08', 'byte': 6},
    {'ext': '.gif', 'hex': '47 49 46 38 39 61', 'byte': 6},
    {'ext': '.png', 'hex': '89 50 4E 47 0D 0A 1A 0A', 'byte': 8},
    {'ext': '.jpeg', 'hex': '', 'byte': 0},
    # video file
    {'ext': '.wav', 'hex': '52 49 46 46', 'byte': 4},
    # Acrchive file
    ]

def compare(file_extension):

    for item in signature_dic:
        if item["ext"] == file_extension:
            length = item["byte"]
            hex = item["hex"].replace(" ", "")
            if length != None:
                return length, hex
