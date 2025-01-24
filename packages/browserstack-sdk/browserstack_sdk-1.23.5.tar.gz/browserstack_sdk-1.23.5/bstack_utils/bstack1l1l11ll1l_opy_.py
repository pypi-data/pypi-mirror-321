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
from collections import deque
from bstack_utils.constants import *
class bstack11l11111_opy_:
    def __init__(self):
        self._1ll1l1l1l11_opy_ = deque()
        self._1ll1l1lll11_opy_ = {}
        self._1ll1l1ll1ll_opy_ = False
    def bstack1ll1l1l111l_opy_(self, test_name, bstack1ll1l1ll1l1_opy_):
        bstack1ll1l1lll1l_opy_ = self._1ll1l1lll11_opy_.get(test_name, {})
        return bstack1ll1l1lll1l_opy_.get(bstack1ll1l1ll1l1_opy_, 0)
    def bstack1ll1l1ll11l_opy_(self, test_name, bstack1ll1l1ll1l1_opy_):
        bstack1ll1l1l11l1_opy_ = self.bstack1ll1l1l111l_opy_(test_name, bstack1ll1l1ll1l1_opy_)
        self.bstack1ll1l1ll111_opy_(test_name, bstack1ll1l1ll1l1_opy_)
        return bstack1ll1l1l11l1_opy_
    def bstack1ll1l1ll111_opy_(self, test_name, bstack1ll1l1ll1l1_opy_):
        if test_name not in self._1ll1l1lll11_opy_:
            self._1ll1l1lll11_opy_[test_name] = {}
        bstack1ll1l1lll1l_opy_ = self._1ll1l1lll11_opy_[test_name]
        bstack1ll1l1l11l1_opy_ = bstack1ll1l1lll1l_opy_.get(bstack1ll1l1ll1l1_opy_, 0)
        bstack1ll1l1lll1l_opy_[bstack1ll1l1ll1l1_opy_] = bstack1ll1l1l11l1_opy_ + 1
    def bstack11llll1l11_opy_(self, bstack1ll1l1l1l1l_opy_, bstack1ll1l1l1ll1_opy_):
        bstack1ll1l1l1111_opy_ = self.bstack1ll1l1ll11l_opy_(bstack1ll1l1l1l1l_opy_, bstack1ll1l1l1ll1_opy_)
        event_name = bstack1lllll11111_opy_[bstack1ll1l1l1ll1_opy_]
        bstack1ll1l1l11ll_opy_ = bstack11111_opy_ (u"ࠧࢁࡽ࠮ࡽࢀ࠱ࢀࢃࠢᙸ").format(bstack1ll1l1l1l1l_opy_, event_name, bstack1ll1l1l1111_opy_)
        self._1ll1l1l1l11_opy_.append(bstack1ll1l1l11ll_opy_)
    def bstack111ll11l1_opy_(self):
        return len(self._1ll1l1l1l11_opy_) == 0
    def bstack11ll1l1ll_opy_(self):
        bstack1ll1l1l1lll_opy_ = self._1ll1l1l1l11_opy_.popleft()
        return bstack1ll1l1l1lll_opy_
    def capturing(self):
        return self._1ll1l1ll1ll_opy_
    def bstack1l1l1l1ll1_opy_(self):
        self._1ll1l1ll1ll_opy_ = True
    def bstack11lll1111l_opy_(self):
        self._1ll1l1ll1ll_opy_ = False