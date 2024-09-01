import enum
import sys
import os



class AddrMapLabelEnum(enum.Enum):
    ADDRMAP_LABEL_CS    = 0
    ADDRMAP_LABEL_BG    = 1
    ADDRMAP_LABEL_BA    = 2
    ADDRMAP_LABEL_COL   = 3
    ADDRMAP_LABEL_ROW   = 4
    ADDRMAP_LABEL_SPC   = 99 # Special Label

    _map_rename = {"COL": "C", "ROW": "R"}

    def __str__(self) -> str:
        name = self.name.replace("ADDRMAP_LABEL_", "") #self.value
        # translation_table = str.maketrans(self._map_rename)
        # return name.translate(translation_table, 1)
        return name

class AddrMapWrapCfg(object):
    pass


##
# For one Bit cfg
##
class AddrMapItemCfg(object):
    _idx_incr = 0
    item_label: AddrMapLabelEnum
    item_label_idx: int
    cfg_offset  = 0
    base_position = 0
    offset_position = 10

    def __init__(self, label:AddrMapLabelEnum, labelIdx: int) -> None:
        self.item_label = label
        self.item_label_idx = labelIdx
        self.base_position = self.GetBasePosition(label, labelIdx)
    
    def SetOffset(self, cfg_offset: int):
        self.cfg_offset = cfg_offset
    
    def GetBasePosition(self, label:AddrMapLabelEnum, labelIdx: int) -> int:
        labelBasePosition = 0

        if (label == AddrMapLabelEnum.ADDRMAP_LABEL_ROW):
            labelBasePosition = labelIdx + 5
        elif (label == AddrMapLabelEnum.ADDRMAP_LABEL_CS):
            labelBasePosition = labelIdx + 6
        elif (label == AddrMapLabelEnum.ADDRMAP_LABEL_BA):
            labelBasePosition = labelIdx + 2
        elif (label == AddrMapLabelEnum.ADDRMAP_LABEL_BG):
            labelBasePosition = labelIdx + 2
        elif (label == AddrMapLabelEnum.ADDRMAP_LABEL_COL):
            labelBasePosition = labelIdx + 0
        
        return labelBasePosition
    
    def GetPosition(self) -> int:
        pass

    pass

class AddrMapItem(object):
    item_label: AddrMapLabelEnum
    item_label_idx: int
    item_name: str
    full_position: int
    cfg: AddrMapItemCfg = None

    def __init__(self, label :AddrMapLabelEnum, labelIdx: int) -> None:
        self.item_label = label
        self.item_label_idx = labelIdx
        self.cfg = AddrMapItemCfg(label, labelIdx)
        self.full_position = 0

    def __str__(self):
        return ("%s_%0d" %(self.item_label, self.item_label_idx))


###
# WRAPPER for address
###

class AddrMapWrap(object):
    addr_map: list

    addr_map_settings = {
        AddrMapLabelEnum.ADDRMAP_LABEL_CS : [30],
        AddrMapLabelEnum.ADDRMAP_LABEL_BG : list(range(10+16+1+2,10+16+1+2+1)),
        AddrMapLabelEnum.ADDRMAP_LABEL_BA : list(range(10+16+1,10+16+1+2)),
        AddrMapLabelEnum.ADDRMAP_LABEL_ROW: list(range(10,10+16+1)),
        # AddrMapLabelEnum.ADDRMAP_LABEL_COL: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        AddrMapLabelEnum.ADDRMAP_LABEL_COL: list(range(0, 10)),
    }

    def CheckMapSettingsValid(self, map_settings: dict) -> bool:
        # combines all settings childs
        bit_map_list = []
        for key, value in map_settings.items():
            bit_map_list += value
        print(bit_map_list)

        # check the list valid: (repeated hollow)
        return True

    def __init__(self) -> None:
        self.addr_map = []

        print(self.addr_map_settings)

        self.CheckMapSettingsValid(self.addr_map_settings)

        c0_item = AddrMapItem(AddrMapLabelEnum.ADDRMAP_LABEL_COL, 0)
        c0_item.cfg.SetOffset(0)
        c1_item = AddrMapItem(AddrMapLabelEnum.ADDRMAP_LABEL_COL, 1)
        c1_item.cfg.SetOffset(1)
        c2_item = AddrMapItem(AddrMapLabelEnum.ADDRMAP_LABEL_COL, 2)
        c3_item = AddrMapItem(AddrMapLabelEnum.ADDRMAP_LABEL_COL, 3)
        c4_item = AddrMapItem(AddrMapLabelEnum.ADDRMAP_LABEL_COL, 4)
        c5_item = AddrMapItem(AddrMapLabelEnum.ADDRMAP_LABEL_COL, 5)
        c6_item = AddrMapItem(AddrMapLabelEnum.ADDRMAP_LABEL_COL, 6)
        c7_item = AddrMapItem(AddrMapLabelEnum.ADDRMAP_LABEL_COL, 7)
        c8_item = AddrMapItem(AddrMapLabelEnum.ADDRMAP_LABEL_COL, 8)
        c9_item = AddrMapItem(AddrMapLabelEnum.ADDRMAP_LABEL_COL, 9)
        cs0_item = AddrMapItem(AddrMapLabelEnum.ADDRMAP_LABEL_CS, 0)

        self.addr_map.append(c0_item)
        self.addr_map.append(cs0_item)


    def ParseAddr(self, addr: int):
        print("addr hex", hex(addr))
        print("addr binary", bin(addr))

        for item in self.addr_map:
            print(item, item.full_position, item.cfg.base_position)


class AddrMapSettingsEnum(enum.Enum):
    ADDRMAP_SETTINGS_ADDRMAP0    = 0
    ADDRMAP_SETTINGS_ADDRMAP1    = 1
    ADDRMAP_SETTINGS_ADDRMAP2    = 2
    ADDRMAP_SETTINGS_ADDRMAP3    = 3
    ADDRMAP_SETTINGS_ADDRMAP4    = 4
    ADDRMAP_SETTINGS_ADDRMAP5    = 5
    ADDRMAP_SETTINGS_ADDRMAP6    = 6
    ADDRMAP_SETTINGS_ADDRMAP7    = 7
    ADDRMAP_SETTINGS_ADDRMAP8    = 8
    ADDRMAP_SETTINGS_ADDRMAP9    = 9
    ADDRMAP_SETTINGS_ADDRMAP10   = 10
    ADDRMAP_SETTINGS_ADDRMAP11   = 11

    def __new__(cls, value):
        member = object.__new__(cls)
        member._value_ = value
        return member

    @staticmethod
    def SettingKeyStringToEnum(enumName: str) -> 'AddrMapSettingsEnum':
        for member in AddrMapSettingsEnum:
            if member.name == "ADDRMAP_SETTINGS_" + enumName:
                return member
        raise ValueError("Invalid enumName")

class AddrMapSettingsAdapter(object):

    @staticmethod
    def SelectValueSlice(value: str, start_pos: int, end_pos: int) -> str:
        length = end_pos - start_pos + 1
        res, coverted_value = StrConverter(value)
        if res == True:
            # 创建一个掩码，用于截取特定位
            mask = (1 << length) - 1
            # 右移并应用掩码
            extracted_bits = (coverted_value >> start_pos) & mask
            format_value = "%0x" % extracted_bits
            format_value_origin = "%0x" % coverted_value
            print(format_value_origin, format_value)
        pass


    def ConvertAddrMapSettingsItem(self, settingKey, settingValue):
        if (settingKey == AddrMapSettingsEnum.ADDRMAP_SETTINGS_ADDRMAP0):
            map_cfg_item = AddrMapItemCfg(AddrMapLabelEnum.ADDRMAP_LABEL_CS, 0)
            print("value", settingValue, AddrMapSettingsAdapter.SelectValueSlice(settingValue, 0, 3))
            pass

    def ConvertAddrMapSettings(self, settings):
        settingsMap = {
            "ADDRMAP0": "hFFFF_1818",
            "ADDRMAP1": "hFFFF_1a1a",
            "ADDRMAP2": "h0000_0000",
            "ADDRMAP3": "h0000_0000",
            "ADDRMAP4": "h0000_1F1F",
            "ADDRMAP5": "h040F_0404",
            "ADDRMAP6": "h0404_0404",
            "ADDRMAP7": "h0000_0F04",
            "ADDRMAP8": "h0000_3F19",
            "ADDRMAP9": "h0404_0404",
            "ADDRMAP10": "h0404_0404",
            "ADDRMAP11": "h001F_1F04"
        }

        for key, value in settingsMap.items(): 
            print(key, value, AddrMapSettingsEnum.SettingKeyStringToEnum(key))
            self.ConvertAddrMapSettingsItem(AddrMapSettingsEnum.SettingKeyStringToEnum(key), value)
    pass


if __name__ == "__main__":

    path_to_add = os.path.join(os.path.dirname(__file__), '../')
    sys.path.append(path_to_add)

    from utils.StrConverter import *

    print("hello world")

    ### SoC_ADDR -> HIF_ADDR
    addr_map_wrap = AddrMapWrap()
    addr_map_wrap.ParseAddr(int("0x8000_0000", 16))

    settings_adapter = AddrMapSettingsAdapter()
    settings_adapter.ConvertAddrMapSettings("")