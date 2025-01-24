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
import requests
import logging
import threading
from urllib.parse import urlparse
from bstack_utils.constants import bstack11111l1111_opy_ as bstack1111111l11_opy_, EVENTS
from bstack_utils.bstack1l11l1lll1_opy_ import bstack1l11l1lll1_opy_
from bstack_utils.helper import bstack1l1l11lll_opy_, bstack11l11l1ll1_opy_, bstack11l11l11l_opy_, bstack111111l11l_opy_, \
  bstack111111lll1_opy_, bstack11l1llll_opy_, get_host_info, bstack11111111l1_opy_, bstack11llll1l1l_opy_, bstack11l11ll11l_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack11l1l11ll_opy_ import get_logger
from bstack_utils.bstack1ll1ll1lll_opy_ import bstack1llllllllll_opy_
logger = get_logger(__name__)
bstack1ll1ll1lll_opy_ = bstack1llllllllll_opy_()
@bstack11l11ll11l_opy_(class_method=False)
def _11111l1lll_opy_(driver, bstack111ll11ll1_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack11111_opy_ (u"࠭࡯ࡴࡡࡱࡥࡲ࡫ࠧၙ"): caps.get(bstack11111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭ၚ"), None),
        bstack11111_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬၛ"): bstack111ll11ll1_opy_.get(bstack11111_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬၜ"), None),
        bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡳࡧ࡭ࡦࠩၝ"): caps.get(bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩၞ"), None),
        bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧၟ"): caps.get(bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧၠ"), None)
    }
  except Exception as error:
    logger.debug(bstack11111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡨࡪࡺࡡࡪ࡮ࡶࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡ࠼ࠣࠫၡ") + str(error))
  return response
def on():
    if os.environ.get(bstack11111_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ၢ"), None) is None or os.environ[bstack11111_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧၣ")] == bstack11111_opy_ (u"ࠥࡲࡺࡲ࡬ࠣၤ"):
        return False
    return True
def bstack11111l1l11_opy_(config):
  return config.get(bstack11111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫၥ"), False) or any([p.get(bstack11111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬၦ"), False) == True for p in config.get(bstack11111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩၧ"), [])])
def bstack11ll11llll_opy_(config, bstack111l11111_opy_):
  try:
    if not bstack11l11l11l_opy_(config):
      return False
    bstack11111ll11l_opy_ = config.get(bstack11111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧၨ"), False)
    if int(bstack111l11111_opy_) < len(config.get(bstack11111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫၩ"), [])) and config[bstack11111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬၪ")][bstack111l11111_opy_]:
      bstack1lllllll1l1_opy_ = config[bstack11111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ၫ")][bstack111l11111_opy_].get(bstack11111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫၬ"), None)
    else:
      bstack1lllllll1l1_opy_ = config.get(bstack11111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬၭ"), None)
    if bstack1lllllll1l1_opy_ != None:
      bstack11111ll11l_opy_ = bstack1lllllll1l1_opy_
    bstack1111111l1l_opy_ = os.getenv(bstack11111_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫၮ")) is not None and len(os.getenv(bstack11111_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬၯ"))) > 0 and os.getenv(bstack11111_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ၰ")) != bstack11111_opy_ (u"ࠩࡱࡹࡱࡲࠧၱ")
    return bstack11111ll11l_opy_ and bstack1111111l1l_opy_
  except Exception as error:
    logger.debug(bstack11111_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡹࡩࡷ࡯ࡦࡺ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡩࡸࡹࡩࡰࡰࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸࠠ࠻ࠢࠪၲ") + str(error))
  return False
def bstack1l1lll11l_opy_(test_tags):
  bstack1111111111_opy_ = os.getenv(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬၳ"))
  if bstack1111111111_opy_ is None:
    return True
  bstack1111111111_opy_ = json.loads(bstack1111111111_opy_)
  try:
    include_tags = bstack1111111111_opy_[bstack11111_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪၴ")] if bstack11111_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫၵ") in bstack1111111111_opy_ and isinstance(bstack1111111111_opy_[bstack11111_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬၶ")], list) else []
    exclude_tags = bstack1111111111_opy_[bstack11111_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ၷ")] if bstack11111_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧၸ") in bstack1111111111_opy_ and isinstance(bstack1111111111_opy_[bstack11111_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨၹ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack11111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡹࡥࡱ࡯ࡤࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡣࡱࡲ࡮ࡴࡧ࠯ࠢࡈࡶࡷࡵࡲࠡ࠼ࠣࠦၺ") + str(error))
  return False
def bstack11111l111l_opy_(config, bstack1111111lll_opy_, bstack111111111l_opy_, bstack111111ll11_opy_):
  bstack11111l1l1l_opy_ = bstack111111l11l_opy_(config)
  bstack1lllllll1ll_opy_ = bstack111111lll1_opy_(config)
  if bstack11111l1l1l_opy_ is None or bstack1lllllll1ll_opy_ is None:
    logger.error(bstack11111_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡳࡷࡱࠤ࡫ࡵࡲࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠾ࠥࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡡࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷ࡭ࡴࡴࠠࡵࡱ࡮ࡩࡳ࠭ၻ"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧၼ"), bstack11111_opy_ (u"ࠧࡼࡿࠪၽ")))
    data = {
        bstack11111_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ၾ"): config[bstack11111_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧၿ")],
        bstack11111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ႀ"): config.get(bstack11111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧႁ"), os.path.basename(os.getcwd())),
        bstack11111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡘ࡮ࡳࡥࠨႂ"): bstack1l1l11lll_opy_(),
        bstack11111_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫႃ"): config.get(bstack11111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪႄ"), bstack11111_opy_ (u"ࠨࠩႅ")),
        bstack11111_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩႆ"): {
            bstack11111_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡔࡡ࡮ࡧࠪႇ"): bstack1111111lll_opy_,
            bstack11111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧႈ"): bstack111111111l_opy_,
            bstack11111_opy_ (u"ࠬࡹࡤ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩႉ"): __version__,
            bstack11111_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨႊ"): bstack11111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧႋ"),
            bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨႌ"): bstack11111_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰႍࠫ"),
            bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪႎ"): bstack111111ll11_opy_
        },
        bstack11111_opy_ (u"ࠫࡸ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭ႏ"): settings,
        bstack11111_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࡉ࡯࡯ࡶࡵࡳࡱ࠭႐"): bstack11111111l1_opy_(),
        bstack11111_opy_ (u"࠭ࡣࡪࡋࡱࡪࡴ࠭႑"): bstack11l1llll_opy_(),
        bstack11111_opy_ (u"ࠧࡩࡱࡶࡸࡎࡴࡦࡰࠩ႒"): get_host_info(),
        bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪ႓"): bstack11l11l11l_opy_(config)
    }
    headers = {
        bstack11111_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨ႔"): bstack11111_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭႕"),
    }
    config = {
        bstack11111_opy_ (u"ࠫࡦࡻࡴࡩࠩ႖"): (bstack11111l1l1l_opy_, bstack1lllllll1ll_opy_),
        bstack11111_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭႗"): headers
    }
    response = bstack11llll1l1l_opy_(bstack11111_opy_ (u"࠭ࡐࡐࡕࡗࠫ႘"), bstack1111111l11_opy_ + bstack11111_opy_ (u"ࠧ࠰ࡸ࠵࠳ࡹ࡫ࡳࡵࡡࡵࡹࡳࡹࠧ႙"), data, config)
    bstack1lllllll111_opy_ = response.json()
    if bstack1lllllll111_opy_[bstack11111_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩႚ")]:
      parsed = json.loads(os.getenv(bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪႛ"), bstack11111_opy_ (u"ࠪࡿࢂ࠭ႜ")))
      parsed[bstack11111_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬႝ")] = bstack1lllllll111_opy_[bstack11111_opy_ (u"ࠬࡪࡡࡵࡣࠪ႞")][bstack11111_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ႟")]
      os.environ[bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨႠ")] = json.dumps(parsed)
      bstack1l11l1lll1_opy_.bstack111111l1l1_opy_(bstack1lllllll111_opy_[bstack11111_opy_ (u"ࠨࡦࡤࡸࡦ࠭Ⴁ")][bstack11111_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪႢ")])
      bstack1l11l1lll1_opy_.bstack1lllllllll1_opy_(bstack1lllllll111_opy_[bstack11111_opy_ (u"ࠪࡨࡦࡺࡡࠨႣ")][bstack11111_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭Ⴄ")])
      bstack1l11l1lll1_opy_.store()
      return bstack1lllllll111_opy_[bstack11111_opy_ (u"ࠬࡪࡡࡵࡣࠪႥ")][bstack11111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࡚࡯࡬ࡧࡱࠫႦ")], bstack1lllllll111_opy_[bstack11111_opy_ (u"ࠧࡥࡣࡷࡥࠬႧ")][bstack11111_opy_ (u"ࠨ࡫ࡧࠫႨ")]
    else:
      logger.error(bstack11111_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡷࡻ࡮࡯࡫ࡱ࡫ࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠻ࠢࠪႩ") + bstack1lllllll111_opy_[bstack11111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫႪ")])
      if bstack1lllllll111_opy_[bstack11111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬႫ")] == bstack11111_opy_ (u"ࠬࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦࡰࡢࡵࡶࡩࡩ࠴ࠧႬ"):
        for bstack1llllllll1l_opy_ in bstack1lllllll111_opy_[bstack11111_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭Ⴍ")]:
          logger.error(bstack1llllllll1l_opy_[bstack11111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨႮ")])
      return None, None
  except Exception as error:
    logger.error(bstack11111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡶࡺࡴࠠࡧࡱࡵࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࠤႯ") +  str(error))
    return None, None
def bstack111111ll1l_opy_():
  if os.getenv(bstack11111_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧႰ")) is None:
    return {
        bstack11111_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪႱ"): bstack11111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪႲ"),
        bstack11111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭Ⴓ"): bstack11111_opy_ (u"࠭ࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡩࡣࡧࠤ࡫ࡧࡩ࡭ࡧࡧ࠲ࠬႴ")
    }
  data = {bstack11111_opy_ (u"ࠧࡦࡰࡧࡘ࡮ࡳࡥࠨႵ"): bstack1l1l11lll_opy_()}
  headers = {
      bstack11111_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨႶ"): bstack11111_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࠪႷ") + os.getenv(bstack11111_opy_ (u"ࠥࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠣႸ")),
      bstack11111_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪႹ"): bstack11111_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨႺ")
  }
  response = bstack11llll1l1l_opy_(bstack11111_opy_ (u"࠭ࡐࡖࡖࠪႻ"), bstack1111111l11_opy_ + bstack11111_opy_ (u"ࠧ࠰ࡶࡨࡷࡹࡥࡲࡶࡰࡶ࠳ࡸࡺ࡯ࡱࠩႼ"), data, { bstack11111_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩႽ"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack11111_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࡚ࠥࡥࡴࡶࠣࡖࡺࡴࠠ࡮ࡣࡵ࡯ࡪࡪࠠࡢࡵࠣࡧࡴࡳࡰ࡭ࡧࡷࡩࡩࠦࡡࡵࠢࠥႾ") + bstack11l11l1ll1_opy_().isoformat() + bstack11111_opy_ (u"ࠪ࡞ࠬႿ"))
      return {bstack11111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫჀ"): bstack11111_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭Ⴡ"), bstack11111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧჂ"): bstack11111_opy_ (u"ࠧࠨჃ")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack11111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡨࡵ࡭ࡱ࡮ࡨࡸ࡮ࡵ࡮ࠡࡱࡩࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡕࡧࡶࡸࠥࡘࡵ࡯࠼ࠣࠦჄ") + str(error))
    return {
        bstack11111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩჅ"): bstack11111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ჆"),
        bstack11111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬჇ"): str(error)
    }
def bstack1l1l1l111l_opy_(caps, options, desired_capabilities={}):
  try:
    bstack1111111ll1_opy_ = caps.get(bstack11111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭჈"), {}).get(bstack11111_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪ჉"), caps.get(bstack11111_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ჊"), bstack11111_opy_ (u"ࠨࠩ჋")))
    if bstack1111111ll1_opy_:
      logger.warn(bstack11111_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡇࡩࡸࡱࡴࡰࡲࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨ჌"))
      return False
    if options:
      bstack1llllllll11_opy_ = options.to_capabilities()
    elif desired_capabilities:
      bstack1llllllll11_opy_ = desired_capabilities
    else:
      bstack1llllllll11_opy_ = {}
    browser = caps.get(bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨჍ"), bstack11111_opy_ (u"ࠫࠬ჎")).lower() or bstack1llllllll11_opy_.get(bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ჏"), bstack11111_opy_ (u"࠭ࠧა")).lower()
    if browser != bstack11111_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧბ"):
      logger.warn(bstack11111_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦგ"))
      return False
    browser_version = caps.get(bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪდ")) or caps.get(bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬე")) or bstack1llllllll11_opy_.get(bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬვ")) or bstack1llllllll11_opy_.get(bstack11111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ზ"), {}).get(bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧთ")) or bstack1llllllll11_opy_.get(bstack11111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨი"), {}).get(bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪკ"))
    if browser_version and browser_version != bstack11111_opy_ (u"ࠩ࡯ࡥࡹ࡫ࡳࡵࠩლ") and int(browser_version.split(bstack11111_opy_ (u"ࠪ࠲ࠬმ"))[0]) <= 98:
      logger.warn(bstack11111_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡧࡳࡧࡤࡸࡪࡸࠠࡵࡪࡤࡲࠥ࠿࠸࠯ࠤნ"))
      return False
    if not options:
      bstack11111ll1l1_opy_ = caps.get(bstack11111_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪო")) or bstack1llllllll11_opy_.get(bstack11111_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫპ"), {})
      if bstack11111_opy_ (u"ࠧ࠮࠯࡫ࡩࡦࡪ࡬ࡦࡵࡶࠫჟ") in bstack11111ll1l1_opy_.get(bstack11111_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭რ"), []):
        logger.warn(bstack11111_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡳࡵࡴࠡࡴࡸࡲࠥࡵ࡮ࠡ࡮ࡨ࡫ࡦࡩࡹࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠢࡖࡻ࡮ࡺࡣࡩࠢࡷࡳࠥࡴࡥࡸࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦࠢࡲࡶࠥࡧࡶࡰ࡫ࡧࠤࡺࡹࡩ࡯ࡩࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠦს"))
        return False
    return True
  except Exception as error:
    logger.debug(bstack11111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡹࡥࡱ࡯ࡤࡢࡶࡨࠤࡦ࠷࠱ࡺࠢࡶࡹࡵࡶ࡯ࡳࡶࠣ࠾ࠧტ") + str(error))
    return False
def set_capabilities(caps, config):
  try:
    bstack1lllllll11l_opy_ = config.get(bstack11111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫუ"), {})
    bstack1lllllll11l_opy_[bstack11111_opy_ (u"ࠬࡧࡵࡵࡪࡗࡳࡰ࡫࡮ࠨფ")] = os.getenv(bstack11111_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫქ"))
    bstack111111l1ll_opy_ = json.loads(os.getenv(bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨღ"), bstack11111_opy_ (u"ࠨࡽࢀࠫყ"))).get(bstack11111_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪშ"))
    caps[bstack11111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪჩ")] = True
    if bstack11111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬც") in caps:
      caps[bstack11111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ძ")][bstack11111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭წ")] = bstack1lllllll11l_opy_
      caps[bstack11111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨჭ")][bstack11111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨხ")][bstack11111_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪჯ")] = bstack111111l1ll_opy_
    else:
      caps[bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩჰ")] = bstack1lllllll11l_opy_
      caps[bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪჱ")][bstack11111_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ჲ")] = bstack111111l1ll_opy_
  except Exception as error:
    logger.debug(bstack11111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷ࠳ࠦࡅࡳࡴࡲࡶ࠿ࠦࠢჳ") +  str(error))
def bstack1l1lll1ll1_opy_(driver, bstack11111ll111_opy_):
  try:
    setattr(driver, bstack11111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧჴ"), True)
    session = driver.session_id
    if session:
      bstack11111l11l1_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack11111l11l1_opy_ = False
      bstack11111l11l1_opy_ = url.scheme in [bstack11111_opy_ (u"ࠣࡪࡷࡸࡵࠨჵ"), bstack11111_opy_ (u"ࠤ࡫ࡸࡹࡶࡳࠣჶ")]
      if bstack11111l11l1_opy_:
        if bstack11111ll111_opy_:
          logger.info(bstack11111_opy_ (u"ࠥࡗࡪࡺࡵࡱࠢࡩࡳࡷࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡩࡣࡶࠤࡸࡺࡡࡳࡶࡨࡨ࠳ࠦࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡨࡥࡨ࡫ࡱࠤࡲࡵ࡭ࡦࡰࡷࡥࡷ࡯࡬ࡺ࠰ࠥჷ"))
      return bstack11111ll111_opy_
  except Exception as e:
    logger.error(bstack11111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢჸ") + str(e))
    return False
def bstack11ll11lll_opy_(driver, name, path):
  try:
    bstack11111l1ll1_opy_ = {
        bstack11111_opy_ (u"ࠬࡺࡨࡕࡧࡶࡸࡗࡻ࡮ࡖࡷ࡬ࡨࠬჹ"): threading.current_thread().current_test_uuid,
        bstack11111_opy_ (u"࠭ࡴࡩࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫჺ"): os.environ.get(bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ჻"), bstack11111_opy_ (u"ࠨࠩჼ")),
        bstack11111_opy_ (u"ࠩࡷ࡬ࡏࡽࡴࡕࡱ࡮ࡩࡳ࠭ჽ"): os.environ.get(bstack11111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫჾ"), bstack11111_opy_ (u"ࠫࠬჿ"))
    }
    bstack111111l111_opy_ = bstack1ll1ll1lll_opy_.bstack11111l11ll_opy_(EVENTS.bstack1ll1111l11_opy_.value)
    bstack1ll1ll1lll_opy_.mark(bstack111111l111_opy_ + bstack11111_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᄀ"))
    logger.debug(bstack11111_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡤࡺ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩᄁ"))
    try:
      logger.debug(driver.execute_async_script(bstack1l11l1lll1_opy_.perform_scan, {bstack11111_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪࠢᄂ"): name}))
      bstack1ll1ll1lll_opy_.end(bstack111111l111_opy_, bstack111111l111_opy_ + bstack11111_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᄃ"), bstack111111l111_opy_ + bstack11111_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᄄ"), True, None)
    except Exception as error:
      bstack1ll1ll1lll_opy_.end(bstack111111l111_opy_, bstack111111l111_opy_ + bstack11111_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᄅ"), bstack111111l111_opy_ + bstack11111_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᄆ"), False, str(error))
    bstack111111l111_opy_ = bstack1ll1ll1lll_opy_.bstack11111l11ll_opy_(EVENTS.bstack11111111ll_opy_.value)
    bstack1ll1ll1lll_opy_.mark(bstack111111l111_opy_ + bstack11111_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᄇ"))
    try:
      logger.debug(driver.execute_async_script(bstack1l11l1lll1_opy_.bstack1llllll1lll_opy_, bstack11111l1ll1_opy_))
      bstack1ll1ll1lll_opy_.end(bstack111111l111_opy_, bstack111111l111_opy_ + bstack11111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᄈ"), bstack111111l111_opy_ + bstack11111_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᄉ"),True, None)
    except Exception as error:
      bstack1ll1ll1lll_opy_.end(bstack111111l111_opy_, bstack111111l111_opy_ + bstack11111_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᄊ"), bstack111111l111_opy_ + bstack11111_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᄋ"),False, str(error))
    logger.info(bstack11111_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠨᄌ"))
  except Exception as bstack111111llll_opy_:
    logger.error(bstack11111_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡩ࡯ࡶ࡮ࡧࠤࡳࡵࡴࠡࡤࡨࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨᄍ") + str(path) + bstack11111_opy_ (u"ࠧࠦࡅࡳࡴࡲࡶࠥࡀࠢᄎ") + str(bstack111111llll_opy_))