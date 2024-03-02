import enum

class AddrMapLabelEnum(enum.Enum):
    ADDRMAP_LABEL_CS    = 0
    ADDRMAP_LABEL_BG    = 1
    ADDRMAP_LABEL_BA    = 2
    ADDRMAP_LABEL_COL   = 3
    ADDRMAP_LABEL_ROW   = 4

    _map_rename = {"COL": "C", "ROW": "R"}

    def __str__(self) -> str:
        name = self.name.replace("ADDRMAP_LABEL_", "") #self.value
        # translation_table = str.maketrans(self._map_rename)
        # return name.translate(translation_table, 1)
        return name

class AddrMapWrapCfg(object):
    pass

class AddrMapItemCfg(object):
    offset_cfg  = 0

    base_position = 0
    offset_position = 10

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

    def __str__(self):
        return ("%s_%0d" %(self.item_label, self.item_label_idx))

class AddrMapWrap(object):
    addr_map: list

    def __init__(self) -> None:
        self.addr_map = []

        c0_item = AddrMapItem(AddrMapLabelEnum.ADDRMAP_LABEL_COL, 0)
        cs0_item = AddrMapItem(AddrMapLabelEnum.ADDRMAP_LABEL_CS, 1)

        self.addr_map.append(c0_item)
        self.addr_map.append(cs0_item)


    def ParseAddr(self, addr: int):
        print("addr", hex(addr))
        print("addr", bin(addr))

        for item in self.addr_map:
            print(item)

if __name__ == "__main__":
    print("hello world")

    addr_map_wrap = AddrMapWrap()
    addr_map_wrap.ParseAddr(int("0x8000_0000", 16))