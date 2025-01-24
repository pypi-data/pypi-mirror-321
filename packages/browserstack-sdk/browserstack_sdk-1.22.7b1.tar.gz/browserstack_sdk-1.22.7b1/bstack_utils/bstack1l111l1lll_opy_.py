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
from collections import deque
from bstack_utils.constants import *
class bstack1l11l1l1l_opy_:
    def __init__(self):
        self._1l11lll1ll1_opy_ = deque()
        self._1l11lll1lll_opy_ = {}
        self._1l11llllll1_opy_ = False
    def bstack1l11lllll11_opy_(self, test_name, bstack1l1l1111111_opy_):
        bstack1l1l11111l1_opy_ = self._1l11lll1lll_opy_.get(test_name, {})
        return bstack1l1l11111l1_opy_.get(bstack1l1l1111111_opy_, 0)
    def bstack1l1l111111l_opy_(self, test_name, bstack1l1l1111111_opy_):
        bstack1l11llll11l_opy_ = self.bstack1l11lllll11_opy_(test_name, bstack1l1l1111111_opy_)
        self.bstack1l11llll1ll_opy_(test_name, bstack1l1l1111111_opy_)
        return bstack1l11llll11l_opy_
    def bstack1l11llll1ll_opy_(self, test_name, bstack1l1l1111111_opy_):
        if test_name not in self._1l11lll1lll_opy_:
            self._1l11lll1lll_opy_[test_name] = {}
        bstack1l1l11111l1_opy_ = self._1l11lll1lll_opy_[test_name]
        bstack1l11llll11l_opy_ = bstack1l1l11111l1_opy_.get(bstack1l1l1111111_opy_, 0)
        bstack1l1l11111l1_opy_[bstack1l1l1111111_opy_] = bstack1l11llll11l_opy_ + 1
    def bstack1l11lll1l_opy_(self, bstack1l11llll1l1_opy_, bstack1l11lllll1l_opy_):
        bstack1l11llll111_opy_ = self.bstack1l1l111111l_opy_(bstack1l11llll1l1_opy_, bstack1l11lllll1l_opy_)
        event_name = bstack1l1l1l111ll_opy_[bstack1l11lllll1l_opy_]
        bstack1l1lll1ll1l_opy_ = bstack1l1_opy_ (u"ࠤࡾࢁ࠲ࢁࡽ࠮ࡽࢀࠦᝇ").format(bstack1l11llll1l1_opy_, event_name, bstack1l11llll111_opy_)
        self._1l11lll1ll1_opy_.append(bstack1l1lll1ll1l_opy_)
    def bstack11ll1l111l_opy_(self):
        return len(self._1l11lll1ll1_opy_) == 0
    def bstack1ll111l11_opy_(self):
        bstack1l11lllllll_opy_ = self._1l11lll1ll1_opy_.popleft()
        return bstack1l11lllllll_opy_
    def capturing(self):
        return self._1l11llllll1_opy_
    def bstack11llll11ll_opy_(self):
        self._1l11llllll1_opy_ = True
    def bstack1l11111l11_opy_(self):
        self._1l11llllll1_opy_ = False