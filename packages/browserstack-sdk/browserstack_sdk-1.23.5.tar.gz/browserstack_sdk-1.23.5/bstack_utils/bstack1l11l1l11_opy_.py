# coding: UTF-8
import sys
bstack11lllll_opy_ = sys.version_info [0] == 2
bstack1l1l1_opy_ = 2048
bstack11ll11_opy_ = 7
def bstack11111_opy_ (bstack11l1lll_opy_):
    global bstack11l1l11_opy_
    bstack1ll1ll_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lllll1l_opy_ = bstack11l1lll_opy_ [:-1]
    bstack1l11_opy_ = bstack1ll1ll_opy_ % len (bstack1lllll1l_opy_)
    bstack1lllll1_opy_ = bstack1lllll1l_opy_ [:bstack1l11_opy_] + bstack1lllll1l_opy_ [bstack1l11_opy_:]
    if bstack11lllll_opy_:
        bstack11lll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1_opy_ - (bstack11111l_opy_ + bstack1ll1ll_opy_) % bstack11ll11_opy_) for bstack11111l_opy_, char in enumerate (bstack1lllll1_opy_)])
    else:
        bstack11lll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1_opy_ - (bstack11111l_opy_ + bstack1ll1ll_opy_) % bstack11ll11_opy_) for bstack11111l_opy_, char in enumerate (bstack1lllll1_opy_)])
    return eval (bstack11lll1l_opy_)
class bstack1l1lll111_opy_:
    def __init__(self, handler):
        self._1ll11l11ll1_opy_ = None
        self.handler = handler
        self._1ll11l1l111_opy_ = self.bstack1ll11l11l1l_opy_()
        self.patch()
    def patch(self):
        self._1ll11l11ll1_opy_ = self._1ll11l1l111_opy_.execute
        self._1ll11l1l111_opy_.execute = self.bstack1ll11l11lll_opy_()
    def bstack1ll11l11lll_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11111_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࠧᛡ"), driver_command, None, this, args)
            response = self._1ll11l11ll1_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11111_opy_ (u"ࠨࡡࡧࡶࡨࡶࠧᛢ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._1ll11l1l111_opy_.execute = self._1ll11l11ll1_opy_
    @staticmethod
    def bstack1ll11l11l1l_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver