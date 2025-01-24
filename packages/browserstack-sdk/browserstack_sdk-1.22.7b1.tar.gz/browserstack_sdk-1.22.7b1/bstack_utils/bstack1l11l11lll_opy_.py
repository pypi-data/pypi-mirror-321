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
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack1l1111l1l11_opy_, bstack111l1l1l1_opy_, get_host_info, bstack1l11ll1l11l_opy_, \
 bstack11l11lll1l_opy_, bstack1l1111ll_opy_, bstack1lll111l_opy_, bstack1l11l1l1111_opy_, bstack1l111ll1_opy_
import bstack_utils.accessibility as bstack111l1ll1_opy_
from bstack_utils.bstack1lll1l1l_opy_ import bstack1llll1l1_opy_
from bstack_utils.percy import bstack11ll1lll11_opy_
from bstack_utils.config import Config
bstack111l11ll_opy_ = Config.bstack11l111ll_opy_()
logger = logging.getLogger(__name__)
percy = bstack11ll1lll11_opy_()
@bstack1lll111l_opy_(class_method=False)
def bstack11ll111l1l1_opy_(bs_config, bstack1ll111l1ll_opy_):
  try:
    data = {
        bstack1l1_opy_ (u"ࠬ࡬࡯ࡳ࡯ࡤࡸࠬᰯ"): bstack1l1_opy_ (u"࠭ࡪࡴࡱࡱࠫᰰ"),
        bstack1l1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡠࡰࡤࡱࡪ࠭ᰱ"): bs_config.get(bstack1l1_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ᰲ"), bstack1l1_opy_ (u"ࠩࠪᰳ")),
        bstack1l1_opy_ (u"ࠪࡲࡦࡳࡥࠨᰴ"): bs_config.get(bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᰵ"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᰶ"): bs_config.get(bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ᰷")),
        bstack1l1_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ᰸"): bs_config.get(bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ᰹"), bstack1l1_opy_ (u"ࠩࠪ᰺")),
        bstack1l1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ᰻"): bstack1l111ll1_opy_(),
        bstack1l1_opy_ (u"ࠫࡹࡧࡧࡴࠩ᰼"): bstack1l11ll1l11l_opy_(bs_config),
        bstack1l1_opy_ (u"ࠬ࡮࡯ࡴࡶࡢ࡭ࡳ࡬࡯ࠨ᰽"): get_host_info(),
        bstack1l1_opy_ (u"࠭ࡣࡪࡡ࡬ࡲ࡫ࡵࠧ᰾"): bstack111l1l1l1_opy_(),
        bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡲࡶࡰࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ᰿"): os.environ.get(bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ᱀")),
        bstack1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࡠࡴࡨࡶࡺࡴࠧ᱁"): os.environ.get(bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠨ᱂"), False),
        bstack1l1_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࡤࡩ࡯࡯ࡶࡵࡳࡱ࠭᱃"): bstack1l1111l1l11_opy_(),
        bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ᱄"): bstack11l1lll1l1l_opy_(),
        bstack1l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡧࡩࡹࡧࡩ࡭ࡵࠪ᱅"): bstack11l1ll1llll_opy_(bstack1ll111l1ll_opy_),
        bstack1l1_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ᱆"): bstack11l1l11ll_opy_(bs_config, bstack1ll111l1ll_opy_.get(bstack1l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩ᱇"), bstack1l1_opy_ (u"ࠩࠪ᱈"))),
        bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ᱉"): bstack11l11lll1l_opy_(bs_config),
    }
    return data
  except Exception as error:
    logger.error(bstack1l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡲࡤࡽࡱࡵࡡࡥࠢࡩࡳࡷࠦࡔࡦࡵࡷࡌࡺࡨ࠺ࠡࠢࡾࢁࠧ᱊").format(str(error)))
    return None
def bstack11l1ll1llll_opy_(framework):
  return {
    bstack1l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡏࡣࡰࡩࠬ᱋"): framework.get(bstack1l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࠧ᱌"), bstack1l1_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺࠧᱍ")),
    bstack1l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫᱎ"): framework.get(bstack1l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᱏ")),
    bstack1l1_opy_ (u"ࠪࡷࡩࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ᱐"): framework.get(bstack1l1_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ᱑")),
    bstack1l1_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧ᱒"): bstack1l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭᱓"),
    bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ᱔"): framework.get(bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ᱕"))
  }
def bstack11l1l11ll_opy_(bs_config, framework):
  bstack1l111ll1ll_opy_ = False
  bstack1l111lll11_opy_ = False
  bstack11l1lll111l_opy_ = False
  if bstack1l1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭᱖") in bs_config:
    bstack11l1lll111l_opy_ = True
  elif bstack1l1_opy_ (u"ࠪࡥࡵࡶࠧ᱗") in bs_config:
    bstack1l111ll1ll_opy_ = True
  else:
    bstack1l111lll11_opy_ = True
  bstack1l11lll11_opy_ = {
    bstack1l1_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ᱘"): bstack1llll1l1_opy_.bstack1l1l11l1ll1_opy_(bs_config, framework),
    bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ᱙"): bstack111l1ll1_opy_.bstack11ll1l1111l_opy_(bs_config),
    bstack1l1_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬᱚ"): bs_config.get(bstack1l1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ᱛ"), False),
    bstack1l1_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪᱜ"): bstack1l111lll11_opy_,
    bstack1l1_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨᱝ"): bstack1l111ll1ll_opy_,
    bstack1l1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧᱞ"): bstack11l1lll111l_opy_
  }
  return bstack1l11lll11_opy_
@bstack1lll111l_opy_(class_method=False)
def bstack11l1lll1l1l_opy_():
  try:
    bstack11l1lll1ll1_opy_ = json.loads(os.getenv(bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬᱟ"), bstack1l1_opy_ (u"ࠬࢁࡽࠨᱠ")))
    return {
        bstack1l1_opy_ (u"࠭ࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠨᱡ"): bstack11l1lll1ll1_opy_
    }
  except Exception as error:
    logger.error(bstack1l1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤ࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡵࡨࡸࡹ࡯࡮ࡨࡵࠣࡪࡴࡸࠠࡕࡧࡶࡸࡍࡻࡢ࠻ࠢࠣࡿࢂࠨᱢ").format(str(error)))
    return {}
def bstack11l1lllll1l_opy_(array, bstack11l1lll1l11_opy_, bstack11l1lll11l1_opy_):
  result = {}
  for o in array:
    key = o[bstack11l1lll1l11_opy_]
    result[key] = o[bstack11l1lll11l1_opy_]
  return result
def bstack11ll1111111_opy_(bstack1l1l11lll_opy_=bstack1l1_opy_ (u"ࠨࠩᱣ")):
  bstack11l1lll11ll_opy_ = bstack111l1ll1_opy_.on()
  bstack11l1lll1lll_opy_ = bstack1llll1l1_opy_.on()
  bstack11l1lll1111_opy_ = percy.bstack1l11lll111_opy_()
  if bstack11l1lll1111_opy_ and not bstack11l1lll1lll_opy_ and not bstack11l1lll11ll_opy_:
    return bstack1l1l11lll_opy_ not in [bstack1l1_opy_ (u"ࠩࡆࡆ࡙࡙ࡥࡴࡵ࡬ࡳࡳࡉࡲࡦࡣࡷࡩࡩ࠭ᱤ"), bstack1l1_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧᱥ")]
  elif bstack11l1lll11ll_opy_ and not bstack11l1lll1lll_opy_:
    return bstack1l1l11lll_opy_ not in [bstack1l1_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᱦ"), bstack1l1_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᱧ"), bstack1l1_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪᱨ")]
  return bstack11l1lll11ll_opy_ or bstack11l1lll1lll_opy_ or bstack11l1lll1111_opy_
@bstack1lll111l_opy_(class_method=False)
def bstack11ll1111ll1_opy_(bstack1l1l11lll_opy_, test=None):
  bstack11l1llll111_opy_ = bstack111l1ll1_opy_.on()
  if not bstack11l1llll111_opy_ or bstack1l1l11lll_opy_ not in [bstack1l1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᱩ")] or test == None:
    return None
  return {
    bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᱪ"): bstack11l1llll111_opy_ and bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᱫ"), None) == True and bstack111l1ll1_opy_.bstack11l1lll1l_opy_(test[bstack1l1_opy_ (u"ࠪࡸࡦ࡭ࡳࠨᱬ")])
  }