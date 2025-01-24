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
import multiprocessing
import os
import json
from time import sleep
import bstack_utils.bstack111ll1111l_opy_ as bstack1l1lll1l1_opy_
from browserstack_sdk.bstack1l1l1llll_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1ll1l111l_opy_
class bstack1l111ll11_opy_:
    def __init__(self, args, logger, bstack111ll1l111_opy_, bstack111ll1l11l_opy_):
        self.args = args
        self.logger = logger
        self.bstack111ll1l111_opy_ = bstack111ll1l111_opy_
        self.bstack111ll1l11l_opy_ = bstack111ll1l11l_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1l1l1llll1_opy_ = []
        self.bstack111lll1111_opy_ = None
        self.bstack1lll11l1l1_opy_ = []
        self.bstack111ll11l11_opy_ = self.bstack11l1l1l1_opy_()
        self.bstack1l1111l1_opy_ = -1
    def bstack1ll1l11ll1_opy_(self, bstack111l1lllll_opy_):
        self.parse_args()
        self.bstack111ll11111_opy_()
        self.bstack111ll1l1l1_opy_(bstack111l1lllll_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack111ll111ll_opy_():
        import importlib
        if getattr(importlib, bstack11111_opy_ (u"ࠧࡧ࡫ࡱࡨࡤࡲ࡯ࡢࡦࡨࡶེࠬ"), False):
            bstack111ll11l1l_opy_ = importlib.find_loader(bstack11111_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡵࡨࡰࡪࡴࡩࡶ࡯ཻࠪ"))
        else:
            bstack111ll11l1l_opy_ = importlib.util.find_spec(bstack11111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡶࡩࡱ࡫࡮ࡪࡷࡰོࠫ"))
    def bstack111ll11lll_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1l1111l1_opy_ = -1
        if self.bstack111ll1l11l_opy_ and bstack11111_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ཽࠪ") in self.bstack111ll1l111_opy_:
            self.bstack1l1111l1_opy_ = int(self.bstack111ll1l111_opy_[bstack11111_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫཾ")])
        try:
            bstack111ll1lll1_opy_ = [bstack11111_opy_ (u"ࠬ࠳࠭ࡥࡴ࡬ࡺࡪࡸࠧཿ"), bstack11111_opy_ (u"࠭࠭࠮ࡲ࡯ࡹ࡬࡯࡮ࡴྀࠩ"), bstack11111_opy_ (u"ࠧ࠮ࡲཱྀࠪ")]
            if self.bstack1l1111l1_opy_ >= 0:
                bstack111ll1lll1_opy_.extend([bstack11111_opy_ (u"ࠨ࠯࠰ࡲࡺࡳࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩྂ"), bstack11111_opy_ (u"ࠩ࠰ࡲࠬྃ")])
            for arg in bstack111ll1lll1_opy_:
                self.bstack111ll11lll_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack111ll11111_opy_(self):
        bstack111lll1111_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack111lll1111_opy_ = bstack111lll1111_opy_
        return bstack111lll1111_opy_
    def bstack11111l1l1_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack111ll111ll_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1ll1l111l_opy_)
    def bstack111ll1l1l1_opy_(self, bstack111l1lllll_opy_):
        bstack1llllll1l1_opy_ = Config.bstack11lll111l_opy_()
        if bstack111l1lllll_opy_:
            self.bstack111lll1111_opy_.append(bstack11111_opy_ (u"ࠪ࠱࠲ࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫྄ࠧ"))
            self.bstack111lll1111_opy_.append(bstack11111_opy_ (u"࡙ࠫࡸࡵࡦࠩ྅"))
        if bstack1llllll1l1_opy_.bstack111ll1l1ll_opy_():
            self.bstack111lll1111_opy_.append(bstack11111_opy_ (u"ࠬ࠳࠭ࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ྆"))
            self.bstack111lll1111_opy_.append(bstack11111_opy_ (u"࠭ࡔࡳࡷࡨࠫ྇"))
        self.bstack111lll1111_opy_.append(bstack11111_opy_ (u"ࠧ࠮ࡲࠪྈ"))
        self.bstack111lll1111_opy_.append(bstack11111_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡰ࡭ࡷࡪ࡭ࡳ࠭ྉ"))
        self.bstack111lll1111_opy_.append(bstack11111_opy_ (u"ࠩ࠰࠱ࡩࡸࡩࡷࡧࡵࠫྊ"))
        self.bstack111lll1111_opy_.append(bstack11111_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪྋ"))
        if self.bstack1l1111l1_opy_ > 1:
            self.bstack111lll1111_opy_.append(bstack11111_opy_ (u"ࠫ࠲ࡴࠧྌ"))
            self.bstack111lll1111_opy_.append(str(self.bstack1l1111l1_opy_))
    def bstack111ll1ll11_opy_(self):
        bstack1lll11l1l1_opy_ = []
        for spec in self.bstack1l1l1llll1_opy_:
            bstack1ll11ll11l_opy_ = [spec]
            bstack1ll11ll11l_opy_ += self.bstack111lll1111_opy_
            bstack1lll11l1l1_opy_.append(bstack1ll11ll11l_opy_)
        self.bstack1lll11l1l1_opy_ = bstack1lll11l1l1_opy_
        return bstack1lll11l1l1_opy_
    def bstack11l1l1l1_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack111ll11l11_opy_ = True
            return True
        except Exception as e:
            self.bstack111ll11l11_opy_ = False
        return self.bstack111ll11l11_opy_
    def bstack1lll1llll1_opy_(self, bstack111ll1llll_opy_, bstack1ll1l11ll1_opy_):
        bstack1ll1l11ll1_opy_[bstack11111_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬྍ")] = self.bstack111ll1l111_opy_
        multiprocessing.set_start_method(bstack11111_opy_ (u"࠭ࡳࡱࡣࡺࡲࠬྎ"))
        bstack11ll111lll_opy_ = []
        manager = multiprocessing.Manager()
        bstack1lllllll1_opy_ = manager.list()
        if bstack11111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪྏ") in self.bstack111ll1l111_opy_:
            for index, platform in enumerate(self.bstack111ll1l111_opy_[bstack11111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫྐ")]):
                bstack11ll111lll_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack111ll1llll_opy_,
                                                            args=(self.bstack111lll1111_opy_, bstack1ll1l11ll1_opy_, bstack1lllllll1_opy_)))
            bstack111ll111l1_opy_ = len(self.bstack111ll1l111_opy_[bstack11111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬྑ")])
        else:
            bstack11ll111lll_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack111ll1llll_opy_,
                                                        args=(self.bstack111lll1111_opy_, bstack1ll1l11ll1_opy_, bstack1lllllll1_opy_)))
            bstack111ll111l1_opy_ = 1
        i = 0
        for t in bstack11ll111lll_opy_:
            os.environ[bstack11111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪྒ")] = str(i)
            if bstack11111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧྒྷ") in self.bstack111ll1l111_opy_:
                os.environ[bstack11111_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭ྔ")] = json.dumps(self.bstack111ll1l111_opy_[bstack11111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩྕ")][i % bstack111ll111l1_opy_])
            i += 1
            t.start()
        for t in bstack11ll111lll_opy_:
            t.join()
        return list(bstack1lllllll1_opy_)
    @staticmethod
    def bstack11111ll1_opy_(driver, bstack111ll11ll1_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫྖ"), None)
        if item and getattr(item, bstack11111_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤࡩࡡࡴࡧࠪྗ"), None) and not getattr(item, bstack11111_opy_ (u"ࠩࡢࡥ࠶࠷ࡹࡠࡵࡷࡳࡵࡥࡤࡰࡰࡨࠫ྘"), False):
            logger.info(
                bstack11111_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠤ࡭ࡧࡳࠡࡧࡱࡨࡪࡪ࠮ࠡࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡶࡼࡧࡹ࠯ࠤྙ"))
            bstack111ll1ll1l_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1l1lll1l1_opy_.bstack11ll11lll_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)