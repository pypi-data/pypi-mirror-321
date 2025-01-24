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
import builtins
import logging
class bstack1l111l1l_opy_:
    def __init__(self, handler):
        self._1l1l1111ll1_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._1l1l1111l11_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack1l1_opy_ (u"ࠧࡪࡰࡩࡳࠬ᜾"), bstack1l1_opy_ (u"ࠨࡦࡨࡦࡺ࡭ࠧ᜿"), bstack1l1_opy_ (u"ࠩࡺࡥࡷࡴࡩ࡯ࡩࠪᝀ"), bstack1l1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᝁ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._1l1l1111l1l_opy_
        self._1l1l11111ll_opy_()
    def _1l1l1111l1l_opy_(self, *args, **kwargs):
        self._1l1l1111ll1_opy_(*args, **kwargs)
        message = bstack1l1_opy_ (u"ࠫࠥ࠭ᝂ").join(map(str, args)) + bstack1l1_opy_ (u"ࠬࡢ࡮ࠨᝃ")
        self._log_message(bstack1l1_opy_ (u"࠭ࡉࡏࡈࡒࠫᝄ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack1l1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ᝅ"): level, bstack1l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᝆ"): msg})
    def _1l1l11111ll_opy_(self):
        for level, bstack1l1l1111lll_opy_ in self._1l1l1111l11_opy_.items():
            setattr(logging, level, self._1l1l111l111_opy_(level, bstack1l1l1111lll_opy_))
    def _1l1l111l111_opy_(self, level, bstack1l1l1111lll_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack1l1l1111lll_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._1l1l1111ll1_opy_
        for level, bstack1l1l1111lll_opy_ in self._1l1l1111l11_opy_.items():
            setattr(logging, level, bstack1l1l1111lll_opy_)