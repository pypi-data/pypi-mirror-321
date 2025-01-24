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
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack11111111l1_opy_, bstack11l1llll_opy_, get_host_info, bstack1lll1l11lll_opy_, \
 bstack11l11l11l_opy_, bstack1l11lll1ll_opy_, bstack11l11ll11l_opy_, bstack1llll11lll1_opy_, bstack1l1l11lll_opy_
import bstack_utils.bstack111ll1111l_opy_ as bstack1l1lll1l1_opy_
from bstack_utils.bstack11l1lll111_opy_ import bstack1l1l11l1l1_opy_
from bstack_utils.percy import bstack1ll111l11l_opy_
from bstack_utils.config import Config
bstack1llllll1l1_opy_ = Config.bstack11lll111l_opy_()
logger = logging.getLogger(__name__)
percy = bstack1ll111l11l_opy_()
@bstack11l11ll11l_opy_(class_method=False)
def bstack1l1lllll1l1_opy_(bs_config, bstack11ll111l_opy_):
  try:
    data = {
        bstack11111_opy_ (u"ࠨࡨࡲࡶࡲࡧࡴࠨᡐ"): bstack11111_opy_ (u"ࠩ࡭ࡷࡴࡴࠧᡑ"),
        bstack11111_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡣࡳࡧ࡭ࡦࠩᡒ"): bs_config.get(bstack11111_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᡓ"), bstack11111_opy_ (u"ࠬ࠭ᡔ")),
        bstack11111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᡕ"): bs_config.get(bstack11111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᡖ"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack11111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᡗ"): bs_config.get(bstack11111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᡘ")),
        bstack11111_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨᡙ"): bs_config.get(bstack11111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡇࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧᡚ"), bstack11111_opy_ (u"ࠬ࠭ᡛ")),
        bstack11111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᡜ"): bstack1l1l11lll_opy_(),
        bstack11111_opy_ (u"ࠧࡵࡣࡪࡷࠬᡝ"): bstack1lll1l11lll_opy_(bs_config),
        bstack11111_opy_ (u"ࠨࡪࡲࡷࡹࡥࡩ࡯ࡨࡲࠫᡞ"): get_host_info(),
        bstack11111_opy_ (u"ࠩࡦ࡭ࡤ࡯࡮ࡧࡱࠪᡟ"): bstack11l1llll_opy_(),
        bstack11111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡࡵࡹࡳࡥࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᡠ"): os.environ.get(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡕ࡙ࡓࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪᡡ")),
        bstack11111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࡤࡺࡥࡴࡶࡶࡣࡷ࡫ࡲࡶࡰࠪᡢ"): os.environ.get(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࠫᡣ"), False),
        bstack11111_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࡠࡥࡲࡲࡹࡸ࡯࡭ࠩᡤ"): bstack11111111l1_opy_(),
        bstack11111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᡥ"): bstack1l1lll11lll_opy_(),
        bstack11111_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡪࡥࡵࡣ࡬ࡰࡸ࠭ᡦ"): bstack1l1lll1ll1l_opy_(bstack11ll111l_opy_),
        bstack11111_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࡣࡲࡧࡰࠨᡧ"): bstack11ll111ll_opy_(bs_config, bstack11ll111l_opy_.get(bstack11111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡶࡵࡨࡨࠬᡨ"), bstack11111_opy_ (u"ࠬ࠭ᡩ"))),
        bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᡪ"): bstack11l11l11l_opy_(bs_config),
    }
    return data
  except Exception as error:
    logger.error(bstack11111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡵࡧࡹ࡭ࡱࡤࡨࠥ࡬࡯ࡳࠢࡗࡩࡸࡺࡈࡶࡤ࠽ࠤࠥࢁࡽࠣᡫ").format(str(error)))
    return None
def bstack1l1lll1ll1l_opy_(framework):
  return {
    bstack11111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡒࡦࡳࡥࠨᡬ"): framework.get(bstack11111_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࠪᡭ"), bstack11111_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶࠪᡮ")),
    bstack11111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧᡯ"): framework.get(bstack11111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᡰ")),
    bstack11111_opy_ (u"࠭ࡳࡥ࡭࡙ࡩࡷࡹࡩࡰࡰࠪᡱ"): framework.get(bstack11111_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᡲ")),
    bstack11111_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪᡳ"): bstack11111_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩᡴ"),
    bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪᡵ"): framework.get(bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫᡶ"))
  }
def bstack11ll111ll_opy_(bs_config, framework):
  bstack1111l11l1_opy_ = False
  bstack1l11l11ll1_opy_ = False
  bstack1l1lll1l1l1_opy_ = False
  if bstack11111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩᡷ") in bs_config:
    bstack1l1lll1l1l1_opy_ = True
  elif bstack11111_opy_ (u"࠭ࡡࡱࡲࠪᡸ") in bs_config:
    bstack1111l11l1_opy_ = True
  else:
    bstack1l11l11ll1_opy_ = True
  bstack111l1ll1l_opy_ = {
    bstack11111_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ᡹"): bstack1l1l11l1l1_opy_.bstack1l1lll1l11l_opy_(bs_config, framework),
    bstack11111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ᡺"): bstack1l1lll1l1_opy_.bstack11111l1l11_opy_(bs_config),
    bstack11111_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ᡻"): bs_config.get(bstack11111_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩ᡼"), False),
    bstack11111_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭᡽"): bstack1l11l11ll1_opy_,
    bstack11111_opy_ (u"ࠬࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ᡾"): bstack1111l11l1_opy_,
    bstack11111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪ᡿"): bstack1l1lll1l1l1_opy_
  }
  return bstack111l1ll1l_opy_
@bstack11l11ll11l_opy_(class_method=False)
def bstack1l1lll11lll_opy_():
  try:
    bstack1l1lll11ll1_opy_ = json.loads(os.getenv(bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨᢀ"), bstack11111_opy_ (u"ࠨࡽࢀࠫᢁ")))
    return {
        bstack11111_opy_ (u"ࠩࡶࡩࡹࡺࡩ࡯ࡩࡶࠫᢂ"): bstack1l1lll11ll1_opy_
    }
  except Exception as error:
    logger.error(bstack11111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡨࡧࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡸ࡫ࡴࡵ࡫ࡱ࡫ࡸࠦࡦࡰࡴࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࠦࡻࡾࠤᢃ").format(str(error)))
    return {}
def bstack1ll1111l1l1_opy_(array, bstack1l1lll1l1ll_opy_, bstack1l1lll1l111_opy_):
  result = {}
  for o in array:
    key = o[bstack1l1lll1l1ll_opy_]
    result[key] = o[bstack1l1lll1l111_opy_]
  return result
def bstack1l1lllll1ll_opy_(bstack1ll1llll11_opy_=bstack11111_opy_ (u"ࠫࠬᢄ")):
  bstack1l1lll1lll1_opy_ = bstack1l1lll1l1_opy_.on()
  bstack1l1lll11l11_opy_ = bstack1l1l11l1l1_opy_.on()
  bstack1l1lll1ll11_opy_ = percy.bstack1111llll_opy_()
  if bstack1l1lll1ll11_opy_ and not bstack1l1lll11l11_opy_ and not bstack1l1lll1lll1_opy_:
    return bstack1ll1llll11_opy_ not in [bstack11111_opy_ (u"ࠬࡉࡂࡕࡕࡨࡷࡸ࡯࡯࡯ࡅࡵࡩࡦࡺࡥࡥࠩᢅ"), bstack11111_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪᢆ")]
  elif bstack1l1lll1lll1_opy_ and not bstack1l1lll11l11_opy_:
    return bstack1ll1llll11_opy_ not in [bstack11111_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨᢇ"), bstack11111_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᢈ"), bstack11111_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭ᢉ")]
  return bstack1l1lll1lll1_opy_ or bstack1l1lll11l11_opy_ or bstack1l1lll1ll11_opy_
@bstack11l11ll11l_opy_(class_method=False)
def bstack1l1lllll111_opy_(bstack1ll1llll11_opy_, test=None):
  bstack1l1lll11l1l_opy_ = bstack1l1lll1l1_opy_.on()
  if not bstack1l1lll11l1l_opy_ or bstack1ll1llll11_opy_ not in [bstack11111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᢊ")] or test == None:
    return None
  return {
    bstack11111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᢋ"): bstack1l1lll11l1l_opy_ and bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫᢌ"), None) == True and bstack1l1lll1l1_opy_.bstack1l1lll11l_opy_(test[bstack11111_opy_ (u"࠭ࡴࡢࡩࡶࠫᢍ")])
  }