# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack11111l1_opy_ = 2048
bstack11l1lll_opy_ = 7
def bstack1l1_opy_ (bstack111l_opy_):
    global bstack11ll1_opy_
    bstack1111ll1_opy_ = ord (bstack111l_opy_ [-1])
    bstack11l11ll_opy_ = bstack111l_opy_ [:-1]
    bstack111lll_opy_ = bstack1111ll1_opy_ % len (bstack11l11ll_opy_)
    bstack1l111l_opy_ = bstack11l11ll_opy_ [:bstack111lll_opy_] + bstack11l11ll_opy_ [bstack111lll_opy_:]
    if bstack1llll11_opy_:
        bstack11l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l1_opy_ - (bstack11lllll_opy_ + bstack1111ll1_opy_) % bstack11l1lll_opy_) for bstack11lllll_opy_, char in enumerate (bstack1l111l_opy_)])
    else:
        bstack11l1_opy_ = str () .join ([chr (ord (char) - bstack11111l1_opy_ - (bstack11lllll_opy_ + bstack1111ll1_opy_) % bstack11l1lll_opy_) for bstack11lllll_opy_, char in enumerate (bstack1l111l_opy_)])
    return eval (bstack11l1_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack111l11111l_opy_ import bstack111l1111l1_opy_
class bstack111ll1l111_opy_(abc.ABC):
    bin_session_id: str
    bstack111l11111l_opy_: bstack111l1111l1_opy_
    def __init__(self):
        self.bstack111ll1l11l_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack111l11111l_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack111l111111_opy_(self):
        return (self.bstack111ll1l11l_opy_ != None and self.bin_session_id != None and self.bstack111l11111l_opy_ != None)
    def configure(self, bstack111ll1l11l_opy_, config, bin_session_id: str, bstack111l11111l_opy_: bstack111l1111l1_opy_):
        self.bstack111ll1l11l_opy_ = bstack111ll1l11l_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack111l11111l_opy_ = bstack111l11111l_opy_
        if self.bin_session_id:
            self.logger.debug(bstack1l1_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷ࡫ࡤࠡ࡯ࡲࡨࡺࡲࡥࠡࡽࡶࡩࡱ࡬࠮ࡠࡡࡦࡰࡦࡹࡳࡠࡡ࠱ࡣࡤࡴࡡ࡮ࡧࡢࡣࢂࡀࠠࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤ࠾ࠤ࿚") + str(self.bin_session_id) + bstack1l1_opy_ (u"ࠨࠢ࿛"))
    def bstack111l1lllll_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack1l1_opy_ (u"ࠢࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠡࡥࡤࡲࡳࡵࡴࠡࡤࡨࠤࡓࡵ࡮ࡦࠤ࿜"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False