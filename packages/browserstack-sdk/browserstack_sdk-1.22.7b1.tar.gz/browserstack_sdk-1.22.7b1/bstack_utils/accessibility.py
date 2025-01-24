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
import requests
import logging
import threading
from urllib.parse import urlparse
from bstack_utils.constants import bstack1l1l1l1l1l1_opy_ as bstack11ll11l11ll_opy_
from bstack_utils.bstack11ll111lll_opy_ import bstack11ll111lll_opy_
from bstack_utils.helper import bstack1l111ll1_opy_, bstack1ll1l11l_opy_, bstack11l11lll1l_opy_, bstack1l1111ll111_opy_, bstack1l111lll1l1_opy_, bstack111l1l1l1_opy_, get_host_info, bstack1l1111l1l11_opy_, bstack11lll11l1l_opy_, bstack1lll111l_opy_
from browserstack_sdk._version import __version__
logger = logging.getLogger(__name__)
@bstack1lll111l_opy_(class_method=False)
def _11ll1l111l1_opy_(driver, bstack1111l1ll_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack1l1_opy_ (u"ࠧࡰࡵࡢࡲࡦࡳࡥࠨ᪔"): caps.get(bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧ᪕"), None),
        bstack1l1_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭᪖"): bstack1111l1ll_opy_.get(bstack1l1_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭᪗"), None),
        bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡴࡡ࡮ࡧࠪ᪘"): caps.get(bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ᪙"), None),
        bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ᪚"): caps.get(bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ᪛"), None)
    }
  except Exception as error:
    logger.debug(bstack1l1_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡩ࡫ࡴࡢ࡫࡯ࡷࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳࠢ࠽ࠤࠬ᪜") + str(error))
  return response
def on():
    if os.environ.get(bstack1l1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ᪝"), None) is None or os.environ[bstack1l1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ᪞")] == bstack1l1_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ᪟"):
        return False
    return True
def bstack11ll1l1111l_opy_(config):
  return config.get(bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ᪠"), False) or any([p.get(bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭᪡"), False) == True for p in config.get(bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ᪢"), [])])
def bstack1llll1llll_opy_(config, bstack11l111l1ll_opy_):
  try:
    if not bstack11l11lll1l_opy_(config):
      return False
    bstack11ll11llll1_opy_ = config.get(bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ᪣"), False)
    if int(bstack11l111l1ll_opy_) < len(config.get(bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ᪤"), [])) and config[bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭᪥")][bstack11l111l1ll_opy_]:
      bstack11ll11ll1l1_opy_ = config[bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ᪦")][bstack11l111l1ll_opy_].get(bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᪧ"), None)
    else:
      bstack11ll11ll1l1_opy_ = config.get(bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭᪨"), None)
    if bstack11ll11ll1l1_opy_ != None:
      bstack11ll11llll1_opy_ = bstack11ll11ll1l1_opy_
    bstack11ll11lllll_opy_ = os.getenv(bstack1l1_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ᪩")) is not None and len(os.getenv(bstack1l1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭᪪"))) > 0 and os.getenv(bstack1l1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ᪫")) != bstack1l1_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ᪬")
    return bstack11ll11llll1_opy_ and bstack11ll11lllll_opy_
  except Exception as error:
    logger.debug(bstack1l1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡪࡸࡩࡧࡻ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡪࡹࡳࡪࡱࡱࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡ࠼ࠣࠫ᪭") + str(error))
  return False
def bstack11l1lll1l_opy_(test_tags):
  bstack1ll111l11ll_opy_ = os.getenv(bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭᪮"))
  if bstack1ll111l11ll_opy_ is None:
    return True
  bstack1ll111l11ll_opy_ = json.loads(bstack1ll111l11ll_opy_)
  try:
    include_tags = bstack1ll111l11ll_opy_[bstack1l1_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ᪯")] if bstack1l1_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ᪰") in bstack1ll111l11ll_opy_ and isinstance(bstack1ll111l11ll_opy_[bstack1l1_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭᪱")], list) else []
    exclude_tags = bstack1ll111l11ll_opy_[bstack1l1_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ᪲")] if bstack1l1_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ᪳") in bstack1ll111l11ll_opy_ and isinstance(bstack1ll111l11ll_opy_[bstack1l1_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ᪴")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack1l1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡺࡦࡲࡩࡥࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡪࡴࡸࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡥࡤࡲࡳ࡯࡮ࡨ࠰ࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠤ᪵ࠧ") + str(error))
  return False
def bstack11ll11l1l11_opy_(config, frameworkName, bstack11ll11ll1ll_opy_, bstack11ll11ll111_opy_):
  bstack11ll1l11111_opy_ = bstack1l1111ll111_opy_(config)
  bstack11ll11l1ll1_opy_ = bstack1l111lll1l1_opy_(config)
  if bstack11ll1l11111_opy_ is None or bstack11ll11l1ll1_opy_ is None:
    logger.error(bstack1l1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡴࡸࡲࠥ࡬࡯ࡳࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࠿ࠦࡍࡪࡵࡶ࡭ࡳ࡭ࠠࡢࡷࡷ࡬ࡪࡴࡴࡪࡥࡤࡸ࡮ࡵ࡮ࠡࡶࡲ࡯ࡪࡴ᪶ࠧ"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ᪷"), bstack1l1_opy_ (u"ࠨࡽࢀ᪸ࠫ")))
    data = {
        bstack1l1_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫᪹ࠧ"): config[bstack1l1_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨ᪺")],
        bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ᪻"): config.get(bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ᪼"), os.path.basename(os.getcwd())),
        bstack1l1_opy_ (u"࠭ࡳࡵࡣࡵࡸ࡙࡯࡭ࡦ᪽ࠩ"): bstack1l111ll1_opy_(),
        bstack1l1_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ᪾"): config.get(bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱᪿࠫ"), bstack1l1_opy_ (u"ᫀࠩࠪ")),
        bstack1l1_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ᫁"): {
            bstack1l1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡎࡢ࡯ࡨࠫ᫂"): frameworkName,
            bstack1l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ᫃"): bstack11ll11ll1ll_opy_,
            bstack1l1_opy_ (u"࠭ࡳࡥ࡭࡙ࡩࡷࡹࡩࡰࡰ᫄ࠪ"): __version__,
            bstack1l1_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࠩ᫅"): bstack1l1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ᫆"),
            bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ᫇"): bstack1l1_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࠬ᫈"),
            bstack1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫ᫉"): bstack11ll11ll111_opy_
        },
        bstack1l1_opy_ (u"ࠬࡹࡥࡵࡶ࡬ࡲ࡬ࡹ᫊ࠧ"): settings,
        bstack1l1_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࡃࡰࡰࡷࡶࡴࡲࠧ᫋"): bstack1l1111l1l11_opy_(),
        bstack1l1_opy_ (u"ࠧࡤ࡫ࡌࡲ࡫ࡵࠧᫌ"): bstack111l1l1l1_opy_(),
        bstack1l1_opy_ (u"ࠨࡪࡲࡷࡹࡏ࡮ࡧࡱࠪᫍ"): get_host_info(),
        bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᫎ"): bstack11l11lll1l_opy_(config)
    }
    headers = {
        bstack1l1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ᫏"): bstack1l1_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ᫐"),
    }
    config = {
        bstack1l1_opy_ (u"ࠬࡧࡵࡵࡪࠪ᫑"): (bstack11ll1l11111_opy_, bstack11ll11l1ll1_opy_),
        bstack1l1_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ᫒"): headers
    }
    response = bstack11lll11l1l_opy_(bstack1l1_opy_ (u"ࠧࡑࡑࡖࡘࠬ᫓"), bstack11ll11l11ll_opy_ + bstack1l1_opy_ (u"ࠨ࠱ࡹ࠶࠴ࡺࡥࡴࡶࡢࡶࡺࡴࡳࠨ᫔"), data, config)
    bstack11ll1l111ll_opy_ = response.json()
    if bstack11ll1l111ll_opy_[bstack1l1_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ᫕")]:
      parsed = json.loads(os.getenv(bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ᫖"), bstack1l1_opy_ (u"ࠫࢀࢃࠧ᫗")))
      parsed[bstack1l1_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭᫘")] = bstack11ll1l111ll_opy_[bstack1l1_opy_ (u"࠭ࡤࡢࡶࡤࠫ᫙")][bstack1l1_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ᫚")]
      os.environ[bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ᫛")] = json.dumps(parsed)
      bstack11ll111lll_opy_.bstack11ll1l1l111_opy_(bstack11ll1l111ll_opy_[bstack1l1_opy_ (u"ࠩࡧࡥࡹࡧࠧ᫜")][bstack1l1_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫ᫝")])
      bstack11ll111lll_opy_.bstack11ll1l1l1l1_opy_(bstack11ll1l111ll_opy_[bstack1l1_opy_ (u"ࠫࡩࡧࡴࡢࠩ᫞")][bstack1l1_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧ᫟")])
      bstack11ll111lll_opy_.store()
      return bstack11ll1l111ll_opy_[bstack1l1_opy_ (u"࠭ࡤࡢࡶࡤࠫ᫠")][bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡔࡰ࡭ࡨࡲࠬ᫡")], bstack11ll1l111ll_opy_[bstack1l1_opy_ (u"ࠨࡦࡤࡸࡦ࠭᫢")][bstack1l1_opy_ (u"ࠩ࡬ࡨࠬ᫣")]
    else:
      logger.error(bstack1l1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡸࡵ࡯ࡰ࡬ࡲ࡬ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠼ࠣࠫ᫤") + bstack11ll1l111ll_opy_[bstack1l1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ᫥")])
      if bstack11ll1l111ll_opy_[bstack1l1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭᫦")] == bstack1l1_opy_ (u"࠭ࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠࡱࡣࡶࡷࡪࡪ࠮ࠨ᫧"):
        for bstack11ll11l1l1l_opy_ in bstack11ll1l111ll_opy_[bstack1l1_opy_ (u"ࠧࡦࡴࡵࡳࡷࡹࠧ᫨")]:
          logger.error(bstack11ll11l1l1l_opy_[bstack1l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ᫩")])
      return None, None
  except Exception as error:
    logger.error(bstack1l1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡷࡻ࡮ࠡࡨࡲࡶࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠻ࠢࠥ᫪") +  str(error))
    return None, None
def bstack11ll11lll11_opy_():
  if os.getenv(bstack1l1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ᫫")) is None:
    return {
        bstack1l1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ᫬"): bstack1l1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ᫭"),
        bstack1l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ᫮"): bstack1l1_opy_ (u"ࠧࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡪࡤࡨࠥ࡬ࡡࡪ࡮ࡨࡨ࠳࠭᫯")
    }
  data = {bstack1l1_opy_ (u"ࠨࡧࡱࡨ࡙࡯࡭ࡦࠩ᫰"): bstack1l111ll1_opy_()}
  headers = {
      bstack1l1_opy_ (u"ࠩࡄࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩ᫱"): bstack1l1_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࠫ᫲") + os.getenv(bstack1l1_opy_ (u"ࠦࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠤ᫳")),
      bstack1l1_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ᫴"): bstack1l1_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ᫵")
  }
  response = bstack11lll11l1l_opy_(bstack1l1_opy_ (u"ࠧࡑࡗࡗࠫ᫶"), bstack11ll11l11ll_opy_ + bstack1l1_opy_ (u"ࠨ࠱ࡷࡩࡸࡺ࡟ࡳࡷࡱࡷ࠴ࡹࡴࡰࡲࠪ᫷"), data, { bstack1l1_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪ᫸"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack1l1_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡔࡦࡵࡷࠤࡗࡻ࡮ࠡ࡯ࡤࡶࡰ࡫ࡤࠡࡣࡶࠤࡨࡵ࡭ࡱ࡮ࡨࡸࡪࡪࠠࡢࡶࠣࠦ᫹") + bstack1ll1l11l_opy_().isoformat() + bstack1l1_opy_ (u"ࠫ࡟࠭᫺"))
      return {bstack1l1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ᫻"): bstack1l1_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧ᫼"), bstack1l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ᫽"): bstack1l1_opy_ (u"ࠨࠩ᫾")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack1l1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡯࡯࡯ࠢࡲࡪࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡖࡨࡷࡹࠦࡒࡶࡰ࠽ࠤࠧ᫿") + str(error))
    return {
        bstack1l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᬀ"): bstack1l1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᬁ"),
        bstack1l1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᬂ"): str(error)
    }
def bstack1ll1111ll_opy_(caps, options, desired_capabilities={}):
  try:
    bstack1ll111l1111_opy_ = caps.get(bstack1l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᬃ"), {}).get(bstack1l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫᬄ"), caps.get(bstack1l1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨᬅ"), bstack1l1_opy_ (u"ࠩࠪᬆ")))
    if bstack1ll111l1111_opy_:
      logger.warn(bstack1l1_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡈࡪࡹ࡫ࡵࡱࡳࠤࡧࡸ࡯ࡸࡵࡨࡶࡸ࠴ࠢᬇ"))
      return False
    if options:
      bstack11ll11lll1l_opy_ = options.to_capabilities()
    elif desired_capabilities:
      bstack11ll11lll1l_opy_ = desired_capabilities
    else:
      bstack11ll11lll1l_opy_ = {}
    browser = caps.get(bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩᬈ"), bstack1l1_opy_ (u"ࠬ࠭ᬉ")).lower() or bstack11ll11lll1l_opy_.get(bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫᬊ"), bstack1l1_opy_ (u"ࠧࠨᬋ")).lower()
    if browser != bstack1l1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨᬌ"):
      logger.warning(bstack1l1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡆ࡬ࡷࡵ࡭ࡦࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧᬍ"))
      return False
    browser_version = caps.get(bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᬎ")) or caps.get(bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᬏ")) or bstack11ll11lll1l_opy_.get(bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᬐ")) or bstack11ll11lll1l_opy_.get(bstack1l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᬑ"), {}).get(bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᬒ")) or bstack11ll11lll1l_opy_.get(bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᬓ"), {}).get(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫᬔ"))
    if browser_version and browser_version != bstack1l1_opy_ (u"ࠪࡰࡦࡺࡥࡴࡶࠪᬕ") and int(browser_version.split(bstack1l1_opy_ (u"ࠫ࠳࠭ᬖ"))[0]) <= 98:
      logger.warning(bstack1l1_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡨࡴࡨࡥࡹ࡫ࡲࠡࡶ࡫ࡥࡳࠦ࠹࠹࠰ࠥᬗ"))
      return False
    if not options:
      bstack1ll11111l11_opy_ = caps.get(bstack1l1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫᬘ")) or bstack11ll11lll1l_opy_.get(bstack1l1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬᬙ"), {})
      if bstack1l1_opy_ (u"ࠨ࠯࠰࡬ࡪࡧࡤ࡭ࡧࡶࡷࠬᬚ") in bstack1ll11111l11_opy_.get(bstack1l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧᬛ"), []):
        logger.warn(bstack1l1_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡵࡹࡳࠦ࡯࡯ࠢ࡯ࡩ࡬ࡧࡣࡺࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠣࡗࡼ࡯ࡴࡤࡪࠣࡸࡴࠦ࡮ࡦࡹࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧࠣࡳࡷࠦࡡࡷࡱ࡬ࡨࠥࡻࡳࡪࡰࡪࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲ࠧᬜ"))
        return False
    return True
  except Exception as error:
    logger.debug(bstack1l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡦࡲࡩࡥࡣࡷࡩࠥࡧ࠱࠲ࡻࠣࡷࡺࡶࡰࡰࡴࡷࠤ࠿ࠨᬝ") + str(error))
    return False
def set_capabilities(caps, config):
  try:
    bstack1lll11111ll_opy_ = config.get(bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬᬞ"), {})
    bstack1lll11111ll_opy_[bstack1l1_opy_ (u"࠭ࡡࡶࡶ࡫ࡘࡴࡱࡥ࡯ࠩᬟ")] = os.getenv(bstack1l1_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬᬠ"))
    bstack11ll11l1lll_opy_ = json.loads(os.getenv(bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩᬡ"), bstack1l1_opy_ (u"ࠩࡾࢁࠬᬢ"))).get(bstack1l1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᬣ"))
    caps[bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᬤ")] = True
    if bstack1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᬥ") in caps:
      caps[bstack1l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᬦ")][bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᬧ")] = bstack1lll11111ll_opy_
      caps[bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᬨ")][bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᬩ")][bstack1l1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᬪ")] = bstack11ll11l1lll_opy_
    else:
      caps[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᬫ")] = bstack1lll11111ll_opy_
      caps[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᬬ")][bstack1l1_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᬭ")] = bstack11ll11l1lll_opy_
  except Exception as error:
    logger.debug(bstack1l1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠴ࠠࡆࡴࡵࡳࡷࡀࠠࠣᬮ") +  str(error))
def bstack111l1l111_opy_(driver, bstack11ll11ll11l_opy_):
  try:
    setattr(driver, bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨᬯ"), True)
    session = driver.session_id
    if session:
      bstack11ll1l11l11_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack11ll1l11l11_opy_ = False
      bstack11ll1l11l11_opy_ = url.scheme in [bstack1l1_opy_ (u"ࠤ࡫ࡸࡹࡶࠢᬰ"), bstack1l1_opy_ (u"ࠥ࡬ࡹࡺࡰࡴࠤᬱ")]
      if bstack11ll1l11l11_opy_:
        if bstack11ll11ll11l_opy_:
          logger.info(bstack1l1_opy_ (u"ࠦࡘ࡫ࡴࡶࡲࠣࡪࡴࡸࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡࡪࡤࡷࠥࡹࡴࡢࡴࡷࡩࡩ࠴ࠠࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡢࡦࡩ࡬ࡲࠥࡳ࡯࡮ࡧࡱࡸࡦࡸࡩ࡭ࡻ࠱ࠦᬲ"))
      return bstack11ll11ll11l_opy_
  except Exception as e:
    logger.error(bstack1l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸࡺࡡࡳࡶ࡬ࡲ࡬ࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡨࡧ࡮ࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࡀࠠࠣᬳ") + str(e))
    return False
def bstack11l11l11_opy_(driver, name, path):
  try:
    bstack1ll1111l1l1_opy_ = {
        bstack1l1_opy_ (u"࠭ࡴࡩࡖࡨࡷࡹࡘࡵ࡯ࡗࡸ࡭ࡩ᬴࠭"): threading.current_thread().current_test_uuid,
        bstack1l1_opy_ (u"ࠧࡵࡪࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᬵ"): os.environ.get(bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᬶ"), bstack1l1_opy_ (u"ࠩࠪᬷ")),
        bstack1l1_opy_ (u"ࠪࡸ࡭ࡐࡷࡵࡖࡲ࡯ࡪࡴࠧᬸ"): os.environ.get(bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᬹ"), bstack1l1_opy_ (u"ࠬ࠭ᬺ"))
    }
    logger.debug(bstack1l1_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡤࡺ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩᬻ"))
    logger.debug(driver.execute_async_script(bstack11ll111lll_opy_.perform_scan, {bstack1l1_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪࠢᬼ"): name}))
    logger.debug(driver.execute_async_script(bstack11ll111lll_opy_.bstack11ll1l11l1l_opy_, bstack1ll1111l1l1_opy_))
    logger.info(bstack1l1_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠦᬽ"))
  except Exception as bstack1ll111ll1l1_opy_:
    logger.error(bstack1l1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡧࡴࡻ࡬ࡥࠢࡱࡳࡹࠦࡢࡦࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦ࠼ࠣࠦᬾ") + str(path) + bstack1l1_opy_ (u"ࠥࠤࡊࡸࡲࡰࡴࠣ࠾ࠧᬿ") + str(bstack1ll111ll1l1_opy_))