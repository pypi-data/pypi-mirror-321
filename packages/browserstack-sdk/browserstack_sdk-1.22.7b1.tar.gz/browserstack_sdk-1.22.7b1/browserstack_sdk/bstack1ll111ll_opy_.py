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
import os
class RobotHandler():
    def __init__(self, args, logger, bstack11l11ll1_opy_, bstack1111l11l_opy_):
        self.args = args
        self.logger = logger
        self.bstack11l11ll1_opy_ = bstack11l11ll1_opy_
        self.bstack1111l11l_opy_ = bstack1111l11l_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l1llll1_opy_(bstack111lll1lll_opy_):
        bstack111llll111_opy_ = []
        if bstack111lll1lll_opy_:
            tokens = str(os.path.basename(bstack111lll1lll_opy_)).split(bstack1l1_opy_ (u"ࠤࡢࠦྊ"))
            camelcase_name = bstack1l1_opy_ (u"ࠥࠤࠧྋ").join(t.title() for t in tokens)
            suite_name, bstack111lll1ll1_opy_ = os.path.splitext(camelcase_name)
            bstack111llll111_opy_.append(suite_name)
        return bstack111llll111_opy_
    @staticmethod
    def bstack111llll11l_opy_(typename):
        if bstack1l1_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࠢྌ") in typename:
            return bstack1l1_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨྍ")
        return bstack1l1_opy_ (u"ࠨࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠢྎ")