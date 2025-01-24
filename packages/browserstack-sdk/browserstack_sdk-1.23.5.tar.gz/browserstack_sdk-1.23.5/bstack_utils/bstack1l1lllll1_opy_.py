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
from browserstack_sdk.bstack1l1llll111_opy_ import bstack1l111ll11_opy_
from browserstack_sdk.bstack11l1l1111l_opy_ import RobotHandler
def bstack1ll11l1ll_opy_(framework):
    if framework.lower() == bstack11111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ᑂ"):
        return bstack1l111ll11_opy_.version()
    elif framework.lower() == bstack11111_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ᑃ"):
        return RobotHandler.version()
    elif framework.lower() == bstack11111_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨᑄ"):
        import behave
        return behave.__version__
    else:
        return bstack11111_opy_ (u"ࠩࡸࡲࡰࡴ࡯ࡸࡰࠪᑅ")