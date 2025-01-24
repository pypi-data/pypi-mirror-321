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
import threading
import logging
import bstack_utils.bstack111ll1111l_opy_ as bstack1l1lll1l1_opy_
from bstack_utils.helper import bstack1l11lll1ll_opy_
logger = logging.getLogger(__name__)
def bstack1111lllll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack11ll1l11l_opy_(context, *args):
    tags = getattr(args[0], bstack11111_opy_ (u"࠭ࡴࡢࡩࡶࠫᄤ"), [])
    bstack1lll1l11l_opy_ = bstack1l1lll1l1_opy_.bstack1l1lll11l_opy_(tags)
    threading.current_thread().isA11yTest = bstack1lll1l11l_opy_
    try:
      bstack1l11ll111l_opy_ = threading.current_thread().bstackSessionDriver if bstack1111lllll_opy_(bstack11111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ᄥ")) else context.browser
      if bstack1l11ll111l_opy_ and bstack1l11ll111l_opy_.session_id and bstack1lll1l11l_opy_ and bstack1l11lll1ll_opy_(
              threading.current_thread(), bstack11111_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧᄦ"), None):
          threading.current_thread().isA11yTest = bstack1l1lll1l1_opy_.bstack1l1lll1ll1_opy_(bstack1l11ll111l_opy_, bstack1lll1l11l_opy_)
    except Exception as e:
       logger.debug(bstack11111_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡦ࠷࠱ࡺࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩ࠿ࠦࡻࡾࠩᄧ").format(str(e)))
def bstack11l1l1ll1_opy_(bstack1l11ll111l_opy_):
    if bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧᄨ"), None) and bstack1l11lll1ll_opy_(
      threading.current_thread(), bstack11111_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᄩ"), None) and not bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠬࡧ࠱࠲ࡻࡢࡷࡹࡵࡰࠨᄪ"), False):
      threading.current_thread().a11y_stop = True
      bstack1l1lll1l1_opy_.bstack11ll11lll_opy_(bstack1l11ll111l_opy_, name=bstack11111_opy_ (u"ࠨࠢᄫ"), path=bstack11111_opy_ (u"ࠢࠣᄬ"))