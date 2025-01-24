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
from browserstack_sdk.bstack1111llll_opy_ import bstack11l11111_opy_
from browserstack_sdk.bstack1ll111ll_opy_ import RobotHandler
def bstack1l1llll1ll_opy_(framework):
    if framework.lower() == bstack1l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᱭ"):
        return bstack11l11111_opy_.version()
    elif framework.lower() == bstack1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫᱮ"):
        return RobotHandler.version()
    elif framework.lower() == bstack1l1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ᱯ"):
        import behave
        return behave.__version__
    else:
        return bstack1l1_opy_ (u"ࠧࡶࡰ࡮ࡲࡴࡽ࡮ࠨᱰ")