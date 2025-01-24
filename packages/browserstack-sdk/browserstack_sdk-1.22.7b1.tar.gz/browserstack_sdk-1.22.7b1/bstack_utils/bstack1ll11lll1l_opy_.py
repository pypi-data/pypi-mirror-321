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
import threading
import logging
import bstack_utils.accessibility as bstack111l1ll1_opy_
from bstack_utils.helper import bstack1l1111ll_opy_
logger = logging.getLogger(__name__)
def bstack1ll1l111l1_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack1l1ll1llll_opy_(context, *args):
    tags = getattr(args[0], bstack1l1_opy_ (u"ࠬࡺࡡࡨࡵࠪ᜵"), [])
    bstack11l111llll_opy_ = bstack111l1ll1_opy_.bstack11l1lll1l_opy_(tags)
    threading.current_thread().isA11yTest = bstack11l111llll_opy_
    try:
      bstack11l1llllll_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll1l111l1_opy_(bstack1l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬ᜶")) else context.browser
      if bstack11l1llllll_opy_ and bstack11l1llllll_opy_.session_id and bstack11l111llll_opy_ and bstack1l1111ll_opy_(
              threading.current_thread(), bstack1l1_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭᜷"), None):
          threading.current_thread().isA11yTest = bstack111l1ll1_opy_.bstack111l1l111_opy_(bstack11l1llllll_opy_, bstack11l111llll_opy_)
    except Exception as e:
       logger.debug(bstack1l1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡥ࠶࠷ࡹࠡ࡫ࡱࠤࡧ࡫ࡨࡢࡸࡨ࠾ࠥࢁࡽࠨ᜸").format(str(e)))
def bstack11lll1l111_opy_(bstack11l1llllll_opy_):
    if bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭᜹"), None) and bstack1l1111ll_opy_(
      threading.current_thread(), bstack1l1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ᜺"), None) and not bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠫࡦ࠷࠱ࡺࡡࡶࡸࡴࡶࠧ᜻"), False):
      threading.current_thread().a11y_stop = True
      bstack111l1ll1_opy_.bstack11l11l11_opy_(bstack11l1llllll_opy_, name=bstack1l1_opy_ (u"ࠧࠨ᜼"), path=bstack1l1_opy_ (u"ࠨࠢ᜽"))