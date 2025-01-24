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
import os
class RobotHandler():
    def __init__(self, args, logger, bstack111ll1l111_opy_, bstack111ll1l11l_opy_):
        self.args = args
        self.logger = logger
        self.bstack111ll1l111_opy_ = bstack111ll1l111_opy_
        self.bstack111ll1l11l_opy_ = bstack111ll1l11l_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack111llll111_opy_(bstack111l1lll1l_opy_):
        bstack111l1lll11_opy_ = []
        if bstack111l1lll1l_opy_:
            tokens = str(os.path.basename(bstack111l1lll1l_opy_)).split(bstack11111_opy_ (u"ࠦࡤࠨྚ"))
            camelcase_name = bstack11111_opy_ (u"ࠧࠦࠢྛ").join(t.title() for t in tokens)
            suite_name, bstack111l1llll1_opy_ = os.path.splitext(camelcase_name)
            bstack111l1lll11_opy_.append(suite_name)
        return bstack111l1lll11_opy_
    @staticmethod
    def bstack111l1ll1ll_opy_(typename):
        if bstack11111_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤྜ") in typename:
            return bstack11111_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣྜྷ")
        return bstack11111_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤྞ")