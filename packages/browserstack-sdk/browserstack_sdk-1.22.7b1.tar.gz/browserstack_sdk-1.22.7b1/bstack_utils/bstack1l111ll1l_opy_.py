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
class bstack11l111111l_opy_:
    def __init__(self, handler):
        self._1l1l1l111l1_opy_ = None
        self.handler = handler
        self._1l1l1l11111_opy_ = self.bstack1l1l1l1111l_opy_()
        self.patch()
    def patch(self):
        self._1l1l1l111l1_opy_ = self._1l1l1l11111_opy_.execute
        self._1l1l1l11111_opy_.execute = self.bstack1l1l11lllll_opy_()
    def bstack1l1l11lllll_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack1l1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࠣᛝ"), driver_command, None, this, args)
            response = self._1l1l1l111l1_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack1l1_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࠣᛞ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._1l1l1l11111_opy_.execute = self._1l1l1l111l1_opy_
    @staticmethod
    def bstack1l1l1l1111l_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver