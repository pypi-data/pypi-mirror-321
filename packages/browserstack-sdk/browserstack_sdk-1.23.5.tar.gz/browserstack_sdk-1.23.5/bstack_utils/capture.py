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
import builtins
import logging
class bstack11l1ll111l_opy_:
    def __init__(self, handler):
        self._1lllll1llll_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._1lllll1ll1l_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack11111_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭ᄭ"), bstack11111_opy_ (u"ࠩࡧࡩࡧࡻࡧࠨᄮ"), bstack11111_opy_ (u"ࠪࡻࡦࡸ࡮ࡪࡰࡪࠫᄯ"), bstack11111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᄰ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._1lllll1lll1_opy_
        self._1llllll1111_opy_()
    def _1lllll1lll1_opy_(self, *args, **kwargs):
        self._1lllll1llll_opy_(*args, **kwargs)
        message = bstack11111_opy_ (u"ࠬࠦࠧᄱ").join(map(str, args)) + bstack11111_opy_ (u"࠭࡜࡯ࠩᄲ")
        self._log_message(bstack11111_opy_ (u"ࠧࡊࡐࡉࡓࠬᄳ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack11111_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᄴ"): level, bstack11111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᄵ"): msg})
    def _1llllll1111_opy_(self):
        for level, bstack1lllll1ll11_opy_ in self._1lllll1ll1l_opy_.items():
            setattr(logging, level, self._1lllll1l1ll_opy_(level, bstack1lllll1ll11_opy_))
    def _1lllll1l1ll_opy_(self, level, bstack1lllll1ll11_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack1lllll1ll11_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._1lllll1llll_opy_
        for level, bstack1lllll1ll11_opy_ in self._1lllll1ll1l_opy_.items():
            setattr(logging, level, bstack1lllll1ll11_opy_)