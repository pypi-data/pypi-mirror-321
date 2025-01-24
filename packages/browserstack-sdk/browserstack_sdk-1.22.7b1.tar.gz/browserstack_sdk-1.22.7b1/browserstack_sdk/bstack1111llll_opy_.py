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
import multiprocessing
import os
import json
from time import sleep
import bstack_utils.accessibility as bstack111l1ll1_opy_
from browserstack_sdk.bstack111ll111_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack111l1l1l_opy_
class bstack11l11111_opy_:
    def __init__(self, args, logger, bstack11l11ll1_opy_, bstack1111l11l_opy_):
        self.args = args
        self.logger = logger
        self.bstack11l11ll1_opy_ = bstack11l11ll1_opy_
        self.bstack1111l11l_opy_ = bstack1111l11l_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack11111l1l_opy_ = []
        self.bstack11111l11_opy_ = None
        self.bstack111l11l1_opy_ = []
        self.bstack111llll1_opy_ = self.bstack11l1111l_opy_()
        self.bstack11l11l1l_opy_ = -1
    def bstack111ll1l1_opy_(self, bstack111lllll_opy_):
        self.parse_args()
        self.bstack111l1l11_opy_()
        self.bstack1111ll11_opy_(bstack111lllll_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack111ll1ll_opy_():
        import importlib
        if getattr(importlib, bstack1l1_opy_ (u"ࠫ࡫࡯࡮ࡥࡡ࡯ࡳࡦࡪࡥࡳࠩএ"), False):
            bstack111ll11l_opy_ = importlib.find_loader(bstack1l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧঐ"))
        else:
            bstack111ll11l_opy_ = importlib.util.find_spec(bstack1l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨ঑"))
    def bstack111lll1l_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack11l11l1l_opy_ = -1
        if self.bstack1111l11l_opy_ and bstack1l1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ঒") in self.bstack11l11ll1_opy_:
            self.bstack11l11l1l_opy_ = int(self.bstack11l11ll1_opy_[bstack1l1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨও")])
        try:
            bstack111l111l_opy_ = [bstack1l1_opy_ (u"ࠩ࠰࠱ࡩࡸࡩࡷࡧࡵࠫঔ"), bstack1l1_opy_ (u"ࠪ࠱࠲ࡶ࡬ࡶࡩ࡬ࡲࡸ࠭ক"), bstack1l1_opy_ (u"ࠫ࠲ࡶࠧখ")]
            if self.bstack11l11l1l_opy_ >= 0:
                bstack111l111l_opy_.extend([bstack1l1_opy_ (u"ࠬ࠳࠭࡯ࡷࡰࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭গ"), bstack1l1_opy_ (u"࠭࠭࡯ࠩঘ")])
            for arg in bstack111l111l_opy_:
                self.bstack111lll1l_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack111l1l11_opy_(self):
        bstack11111l11_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack11111l11_opy_ = bstack11111l11_opy_
        return bstack11111l11_opy_
    def bstack1111l1l1_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack111ll1ll_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack111l1l1l_opy_)
    def bstack1111ll11_opy_(self, bstack111lllll_opy_):
        bstack111l11ll_opy_ = Config.bstack11l111ll_opy_()
        if bstack111lllll_opy_:
            self.bstack11111l11_opy_.append(bstack1l1_opy_ (u"ࠧ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫঙ"))
            self.bstack11111l11_opy_.append(bstack1l1_opy_ (u"ࠨࡖࡵࡹࡪ࠭চ"))
        if bstack111l11ll_opy_.bstack11111lll_opy_():
            self.bstack11111l11_opy_.append(bstack1l1_opy_ (u"ࠩ࠰࠱ࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨছ"))
            self.bstack11111l11_opy_.append(bstack1l1_opy_ (u"ࠪࡘࡷࡻࡥࠨজ"))
        self.bstack11111l11_opy_.append(bstack1l1_opy_ (u"ࠫ࠲ࡶࠧঝ"))
        self.bstack11111l11_opy_.append(bstack1l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡴࡱࡻࡧࡪࡰࠪঞ"))
        self.bstack11111l11_opy_.append(bstack1l1_opy_ (u"࠭࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠨট"))
        self.bstack11111l11_opy_.append(bstack1l1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧঠ"))
        if self.bstack11l11l1l_opy_ > 1:
            self.bstack11111l11_opy_.append(bstack1l1_opy_ (u"ࠨ࠯ࡱࠫড"))
            self.bstack11111l11_opy_.append(str(self.bstack11l11l1l_opy_))
    def bstack111l1lll_opy_(self):
        bstack111l11l1_opy_ = []
        for spec in self.bstack11111l1l_opy_:
            bstack1111lll1_opy_ = [spec]
            bstack1111lll1_opy_ += self.bstack11111l11_opy_
            bstack111l11l1_opy_.append(bstack1111lll1_opy_)
        self.bstack111l11l1_opy_ = bstack111l11l1_opy_
        return bstack111l11l1_opy_
    def bstack11l1111l_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack111llll1_opy_ = True
            return True
        except Exception as e:
            self.bstack111llll1_opy_ = False
        return self.bstack111llll1_opy_
    def bstack111lll11_opy_(self, bstack11l111l1_opy_, bstack111ll1l1_opy_):
        bstack111ll1l1_opy_[bstack1l1_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩঢ")] = self.bstack11l11ll1_opy_
        multiprocessing.set_start_method(bstack1l1_opy_ (u"ࠪࡷࡵࡧࡷ࡯ࠩণ"))
        bstack1111ll1l_opy_ = []
        manager = multiprocessing.Manager()
        bstack11111ll1_opy_ = manager.list()
        if bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧত") in self.bstack11l11ll1_opy_:
            for index, platform in enumerate(self.bstack11l11ll1_opy_[bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨথ")]):
                bstack1111ll1l_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack11l111l1_opy_,
                                                            args=(self.bstack11111l11_opy_, bstack111ll1l1_opy_, bstack11111ll1_opy_)))
            bstack111111ll_opy_ = len(self.bstack11l11ll1_opy_[bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩদ")])
        else:
            bstack1111ll1l_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack11l111l1_opy_,
                                                        args=(self.bstack11111l11_opy_, bstack111ll1l1_opy_, bstack11111ll1_opy_)))
            bstack111111ll_opy_ = 1
        i = 0
        for t in bstack1111ll1l_opy_:
            os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧধ")] = str(i)
            if bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫন") in self.bstack11l11ll1_opy_:
                os.environ[bstack1l1_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪ঩")] = json.dumps(self.bstack11l11ll1_opy_[bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭প")][i % bstack111111ll_opy_])
            i += 1
            t.start()
        for t in bstack1111ll1l_opy_:
            t.join()
        return list(bstack11111ll1_opy_)
    @staticmethod
    def bstack111l1111_opy_(driver, bstack1111l1ll_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack1l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨফ"), None)
        if item and getattr(item, bstack1l1_opy_ (u"ࠬࡥࡡ࠲࠳ࡼࡣࡹ࡫ࡳࡵࡡࡦࡥࡸ࡫ࠧব"), None) and not getattr(item, bstack1l1_opy_ (u"࠭࡟ࡢ࠳࠴ࡽࡤࡹࡴࡰࡲࡢࡨࡴࡴࡥࠨভ"), False):
            logger.info(
                bstack1l1_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠥࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡹࡳࡪࡥࡳࡹࡤࡽ࠳ࠨম"))
            bstack1111l111_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack111l1ll1_opy_.bstack11l11l11_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)