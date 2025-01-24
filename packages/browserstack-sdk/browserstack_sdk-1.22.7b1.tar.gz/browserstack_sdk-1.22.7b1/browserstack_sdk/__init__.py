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
import atexit
import os
import signal
import sys
import yaml
import requests
import logging
import threading
import socket
import datetime
import string
import random
import json
import collections.abc
import re
import multiprocessing
import traceback
import copy
import tempfile
from packaging import version
from uuid import uuid4
from browserstack.local import Local
from urllib.parse import urlparse
from dotenv import load_dotenv
from bstack_utils.constants import *
from bstack_utils.percy import *
from browserstack_sdk.bstack1111111l_opy_ import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack1l111l1lll_opy_ import bstack1l11l1l1l_opy_
import time
import requests
def bstack11ll11l1l1_opy_():
  global CONFIG
  headers = {
        bstack1l1_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫ৖"): bstack1l1_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩৗ"),
      }
  proxies = bstack1lll1l1lll_opy_(CONFIG, bstack111ll11ll_opy_)
  try:
    response = requests.get(bstack111ll11ll_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack11ll1l11l1_opy_ = response.json()[bstack1l1_opy_ (u"ࠧࡩࡷࡥࡷࠬ৘")]
      logger.debug(bstack1ll111111l_opy_.format(response.json()))
      return bstack11ll1l11l1_opy_
    else:
      logger.debug(bstack1l11lll11l_opy_.format(bstack1l1_opy_ (u"ࠣࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡎࡘࡕࡎࠡࡲࡤࡶࡸ࡫ࠠࡦࡴࡵࡳࡷࠦࠢ৙")))
  except Exception as e:
    logger.debug(bstack1l11lll11l_opy_.format(e))
def bstack1lll11l111_opy_(hub_url):
  global CONFIG
  url = bstack1l1_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦ৚")+  hub_url + bstack1l1_opy_ (u"ࠥ࠳ࡨ࡮ࡥࡤ࡭ࠥ৛")
  headers = {
        bstack1l1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪড়"): bstack1l1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨঢ়"),
      }
  proxies = bstack1lll1l1lll_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack1ll11l1111_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack11llll1ll1_opy_.format(hub_url, e))
def bstack1l1lll11l_opy_():
  try:
    global bstack11ll1ll111_opy_
    bstack11ll1l11l1_opy_ = bstack11ll11l1l1_opy_()
    bstack11l11l11l1_opy_ = []
    results = []
    for bstack11ll111l1l_opy_ in bstack11ll1l11l1_opy_:
      bstack11l11l11l1_opy_.append(bstack1l11111ll_opy_(target=bstack1lll11l111_opy_,args=(bstack11ll111l1l_opy_,)))
    for t in bstack11l11l11l1_opy_:
      t.start()
    for t in bstack11l11l11l1_opy_:
      results.append(t.join())
    bstack1l1ll11111_opy_ = {}
    for item in results:
      hub_url = item[bstack1l1_opy_ (u"࠭ࡨࡶࡤࡢࡹࡷࡲࠧ৞")]
      latency = item[bstack1l1_opy_ (u"ࠧ࡭ࡣࡷࡩࡳࡩࡹࠨয়")]
      bstack1l1ll11111_opy_[hub_url] = latency
    bstack1l1l1ll11_opy_ = min(bstack1l1ll11111_opy_, key= lambda x: bstack1l1ll11111_opy_[x])
    bstack11ll1ll111_opy_ = bstack1l1l1ll11_opy_
    logger.debug(bstack11lllll1ll_opy_.format(bstack1l1l1ll11_opy_))
  except Exception as e:
    logger.debug(bstack11111111l_opy_.format(e))
from bstack_utils.messages import *
from bstack_utils import bstack11ll11llll_opy_
from bstack_utils.config import Config
from bstack_utils.constants import bstack1llll1ll11_opy_
from bstack_utils.helper import bstack1l1lll1l11_opy_, bstack11lll11l1l_opy_, bstack1ll1l1l11l_opy_, bstack1l1111ll_opy_, bstack11l11lll1l_opy_, \
  Notset, bstack11llllll11_opy_, \
  bstack1llllll11l_opy_, bstack11llll111_opy_, bstack11l1l11l11_opy_, bstack111l1l1l1_opy_, bstack111lllll11_opy_, bstack111111ll1_opy_, \
  bstack1ll11llll1_opy_, \
  bstack11111ll1l_opy_, bstack1l1ll1111_opy_, bstack1l1l111111_opy_, bstack11lll1l1l_opy_, \
  bstack1l111l111_opy_, bstack1ll1111111_opy_, bstack1ll11l11l_opy_, bstack1lllll1l1_opy_
from bstack_utils.bstack11l11lll11_opy_ import bstack1l1llll1ll_opy_
from bstack_utils.bstack1l111ll1l_opy_ import bstack11l111111l_opy_
from bstack_utils.bstack1llll11l11_opy_ import bstack1l1lll1lll_opy_, bstack11ll1l11l_opy_
from bstack_utils.bstack1l11l1l1_opy_ import bstack1l1ll1l1_opy_
from bstack_utils.bstack1lll1l1l_opy_ import bstack1llll1l1_opy_
from bstack_utils.bstack11ll111lll_opy_ import bstack11ll111lll_opy_
from bstack_utils.proxy import bstack1ll1111l1l_opy_, bstack1lll1l1lll_opy_, bstack1l1ll11lll_opy_, bstack11l11l11ll_opy_
import bstack_utils.accessibility as bstack111l1ll1_opy_
from browserstack_sdk.bstack1111llll_opy_ import *
from browserstack_sdk.bstack111ll111_opy_ import *
from bstack_utils.bstack1lll1l1ll_opy_ import bstack111l11l1l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l11l_opy_ import bstack1llll1l11l_opy_, Events, bstack1l11l111ll_opy_, bstack11ll1111ll_opy_
from browserstack_sdk.bstack11l1l11l_opy_ import *
import requests
from bstack_utils.constants import *
def bstack1l11l1l11_opy_():
    global bstack11ll1ll111_opy_
    try:
        bstack1l1lll1111_opy_ = bstack11ll111ll1_opy_()
        bstack1llll1ll1l_opy_(bstack1l1lll1111_opy_)
        hub_url = bstack1l1lll1111_opy_.get(bstack1l1_opy_ (u"ࠣࡷࡵࡰࠧৠ"), bstack1l1_opy_ (u"ࠤࠥৡ"))
        if hub_url.endswith(bstack1l1_opy_ (u"ࠪ࠳ࡼࡪ࠯ࡩࡷࡥࠫৢ")):
            hub_url = hub_url.rsplit(bstack1l1_opy_ (u"ࠫ࠴ࡽࡤ࠰ࡪࡸࡦࠬৣ"), 1)[0]
        if hub_url.startswith(bstack1l1_opy_ (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴࠭৤")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack1l1_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࠨ৥")):
            hub_url = hub_url[8:]
        bstack11ll1ll111_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack11ll111ll1_opy_():
    global CONFIG
    bstack1ll1l111ll_opy_ = CONFIG.get(bstack1l1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶࠫ০"), {}).get(bstack1l1_opy_ (u"ࠨࡩࡵ࡭ࡩࡔࡡ࡮ࡧࠪ১"), bstack1l1_opy_ (u"ࠩࡑࡓࡤࡍࡒࡊࡆࡢࡒࡆࡓࡅࡠࡒࡄࡗࡘࡋࡄࠨ২"))
    if not isinstance(bstack1ll1l111ll_opy_, str):
        raise ValueError(bstack1l1_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡊࡶ࡮ࡪࠠ࡯ࡣࡰࡩࠥࡳࡵࡴࡶࠣࡦࡪࠦࡡࠡࡸࡤࡰ࡮ࡪࠠࡴࡶࡵ࡭ࡳ࡭ࠢ৩"))
    try:
        bstack1l1lll1111_opy_ = bstack11lll11l1_opy_(bstack1ll1l111ll_opy_)
        return bstack1l1lll1111_opy_
    except Exception as e:
        logger.error(bstack1l1_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡧࡳ࡫ࡧࠤࡩ࡫ࡴࡢ࡫࡯ࡷࠥࡀࠠࡼࡿࠥ৪").format(str(e)))
        return {}
def bstack11lll11l1_opy_(bstack1ll1l111ll_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack1l1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ৫")] or not CONFIG[bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ৬")]:
            raise ValueError(bstack1l1_opy_ (u"ࠢࡎ࡫ࡶࡷ࡮ࡴࡧࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡶࡵࡨࡶࡳࡧ࡭ࡦࠢࡲࡶࠥࡧࡣࡤࡧࡶࡷࠥࡱࡥࡺࠤ৭"))
        url = bstack11l1l1111_opy_ + bstack1ll1l111ll_opy_
        auth = (CONFIG[bstack1l1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ৮")], CONFIG[bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ৯")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack111llll1l_opy_ = json.loads(response.text)
            return bstack111llll1l_opy_
    except ValueError as ve:
        logger.error(bstack1l1_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫࡫ࡴࡤࡪ࡬ࡲ࡬ࠦࡧࡳ࡫ࡧࠤࡩ࡫ࡴࡢ࡫࡯ࡷࠥࡀࠠࡼࡿࠥৰ").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack1l1_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡨࡴ࡬ࡨࠥࡪࡥࡵࡣ࡬ࡰࡸࠦ࠺ࠡࡽࢀࠦৱ").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack1llll1ll1l_opy_(bstack1ll1l11ll_opy_):
    global CONFIG
    if bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ৲") not in CONFIG or str(CONFIG[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ৳")]).lower() == bstack1l1_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭৴"):
        CONFIG[bstack1l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࠧ৵")] = False
    elif bstack1l1_opy_ (u"ࠩ࡬ࡷ࡙ࡸࡩࡢ࡮ࡊࡶ࡮ࡪࠧ৶") in bstack1ll1l11ll_opy_:
        bstack1l1lll1l1l_opy_ = CONFIG.get(bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ৷"), {})
        logger.debug(bstack1l1_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡉࡽ࡯ࡳࡵ࡫ࡱ࡫ࠥࡲ࡯ࡤࡣ࡯ࠤࡴࡶࡴࡪࡱࡱࡷ࠿ࠦࠥࡴࠤ৸"), bstack1l1lll1l1l_opy_)
        bstack11llllll1l_opy_ = bstack1ll1l11ll_opy_.get(bstack1l1_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱࡗ࡫ࡰࡦࡣࡷࡩࡷࡹࠢ৹"), [])
        bstack1l111lll1l_opy_ = bstack1l1_opy_ (u"ࠨࠬࠣ৺").join(bstack11llllll1l_opy_)
        logger.debug(bstack1l1_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡃࡶࡵࡷࡳࡲࠦࡲࡦࡲࡨࡥࡹ࡫ࡲࠡࡵࡷࡶ࡮ࡴࡧ࠻ࠢࠨࡷࠧ৻"), bstack1l111lll1l_opy_)
        bstack111l1ll11_opy_ = {
            bstack1l1_opy_ (u"ࠣ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠥৼ"): bstack1l1_opy_ (u"ࠤࡤࡸࡸ࠳ࡲࡦࡲࡨࡥࡹ࡫ࡲࠣ৽"),
            bstack1l1_opy_ (u"ࠥࡪࡴࡸࡣࡦࡎࡲࡧࡦࡲࠢ৾"): bstack1l1_opy_ (u"ࠦࡹࡸࡵࡦࠤ৿"),
            bstack1l1_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱ࠲ࡸࡥࡱࡧࡤࡸࡪࡸࠢ਀"): bstack1l111lll1l_opy_
        }
        bstack1l1lll1l1l_opy_.update(bstack111l1ll11_opy_)
        logger.debug(bstack1l1_opy_ (u"ࠨࡁࡕࡕࠣ࠾࡛ࠥࡰࡥࡣࡷࡩࡩࠦ࡬ࡰࡥࡤࡰࠥࡵࡰࡵ࡫ࡲࡲࡸࡀࠠࠦࡵࠥਁ"), bstack1l1lll1l1l_opy_)
        CONFIG[bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫਂ")] = bstack1l1lll1l1l_opy_
        logger.debug(bstack1l1_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡇ࡫ࡱࡥࡱࠦࡃࡐࡐࡉࡍࡌࡀࠠࠦࡵࠥਃ"), CONFIG)
def bstack11ll1ll1l_opy_():
    bstack1l1lll1111_opy_ = bstack11ll111ll1_opy_()
    if not bstack1l1lll1111_opy_[bstack1l1_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࡛ࡲ࡭ࠩ਄")]:
      raise ValueError(bstack1l1_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࡕࡳ࡮ࠣ࡭ࡸࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡧࡴࡲࡱࠥ࡭ࡲࡪࡦࠣࡨࡪࡺࡡࡪ࡮ࡶ࠲ࠧਅ"))
    return bstack1l1lll1111_opy_[bstack1l1_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡖࡴ࡯ࠫਆ")] + bstack1l1_opy_ (u"ࠬࡅࡣࡢࡲࡶࡁࠬਇ")
def bstack1111ll111_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack1l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨਈ")], CONFIG[bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪਉ")])
        url = bstack111111l1l_opy_
        logger.debug(bstack1l1_opy_ (u"ࠣࡃࡷࡸࡪࡳࡰࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡣࡷ࡬ࡰࡩࡹࠠࡧࡴࡲࡱࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤ࡙ࡻࡲࡣࡱࡖࡧࡦࡲࡥࠡࡃࡓࡍࠧਊ"))
        try:
            response = requests.get(url, auth=auth, headers={bstack1l1_opy_ (u"ࠤࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠣ਋"): bstack1l1_opy_ (u"ࠥࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳࠨ਌")})
            if response.status_code == 200:
                bstack11llll111l_opy_ = json.loads(response.text)
                bstack1lll1l11l1_opy_ = bstack11llll111l_opy_.get(bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡶࠫ਍"), [])
                if bstack1lll1l11l1_opy_:
                    bstack11ll1l1lll_opy_ = bstack1lll1l11l1_opy_[0]
                    build_hashed_id = bstack11ll1l1lll_opy_.get(bstack1l1_opy_ (u"ࠬ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ਎"))
                    bstack1l11l1l1ll_opy_ = bstack1l1111l111_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack1l11l1l1ll_opy_])
                    logger.info(bstack11lllllll_opy_.format(bstack1l11l1l1ll_opy_))
                    bstack11ll1l1l11_opy_ = CONFIG[bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩਏ")]
                    if bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩਐ") in CONFIG:
                      bstack11ll1l1l11_opy_ += bstack1l1_opy_ (u"ࠨࠢࠪ਑") + CONFIG[bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ਒")]
                    if bstack11ll1l1l11_opy_ != bstack11ll1l1lll_opy_.get(bstack1l1_opy_ (u"ࠪࡲࡦࡳࡥࠨਓ")):
                      logger.debug(bstack11ll1l1ll_opy_.format(bstack11ll1l1lll_opy_.get(bstack1l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩਔ")), bstack11ll1l1l11_opy_))
                    return result
                else:
                    logger.debug(bstack1l1_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡓࡵࠠࡣࡷ࡬ࡰࡩࡹࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡷ࡬ࡪࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠯ࠤਕ"))
            else:
                logger.debug(bstack1l1_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡣࡷ࡬ࡰࡩࡹ࠮ࠣਖ"))
        except Exception as e:
            logger.error(bstack1l1_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡥࡹ࡮ࡲࡤࡴࠢ࠽ࠤࢀࢃࠢਗ").format(str(e)))
    else:
        logger.debug(bstack1l1_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡄࡑࡑࡊࡎࡍࠠࡪࡵࠣࡲࡴࡺࠠࡴࡧࡷ࠲࡛ࠥ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡣࡷ࡬ࡰࡩࡹ࠮ࠣਘ"))
    return [None, None]
import bstack_utils.bstack1l11l11lll_opy_ as bstack11l1111111_opy_
import bstack_utils.bstack1ll11lll1l_opy_ as bstack1l1111l11l_opy_
from browserstack_sdk.sdk_cli.cli import cli
cli.bstack1lll111lll_opy_()
bstack1l1l1l1111_opy_ = bstack1l1_opy_ (u"ࠩࠣࠤ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵࡜࡯ࠢࠣ࡭࡫࠮ࡰࡢࡩࡨࠤࡂࡃ࠽ࠡࡸࡲ࡭ࡩࠦ࠰ࠪࠢࡾࡠࡳࠦࠠࠡࡶࡵࡽࢀࡢ࡮ࠡࡥࡲࡲࡸࡺࠠࡧࡵࠣࡁࠥࡸࡥࡲࡷ࡬ࡶࡪ࠮࡜ࠨࡨࡶࡠࠬ࠯࠻࡝ࡰࠣࠤࠥࠦࠠࡧࡵ࠱ࡥࡵࡶࡥ࡯ࡦࡉ࡭ࡱ࡫ࡓࡺࡰࡦࠬࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩ࠮ࠣࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡵࡥࡩ࡯ࡦࡨࡼ࠮ࠦࠫࠡࠤ࠽ࠦࠥ࠱ࠠࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡌࡖࡓࡓ࠴ࡰࡢࡴࡶࡩ࠭࠮ࡡࡸࡣ࡬ࡸࠥࡴࡥࡸࡒࡤ࡫ࡪ࠸࠮ࡦࡸࡤࡰࡺࡧࡴࡦࠪࠥࠬ࠮ࠦ࠽࠿ࠢࡾࢁࠧ࠲ࠠ࡝ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡪࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡥࡵࡣ࡬ࡰࡸࠨࡽ࡝ࠩࠬ࠭࠮ࡡࠢࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠥࡡ࠮ࠦࠫࠡࠤ࠯ࡠࡡࡴࠢࠪ࡞ࡱࠤࠥࠦࠠࡾࡥࡤࡸࡨ࡮ࠨࡦࡺࠬࡿࡡࡴࠠࠡࠢࠣࢁࡡࡴࠠࠡࡿ࡟ࡲࠥࠦ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰ࠩਙ")
bstack11l1lllll_opy_ = bstack1l1_opy_ (u"ࠪࡠࡳ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯࡝ࡰࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡲࡤࡸ࡭ࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠵ࡠࡠࡳࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡨࡧࡰࡴࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠶ࡣ࡜࡯ࡥࡲࡲࡸࡺࠠࡱࡡ࡬ࡲࡩ࡫ࡸࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠶ࡢࡢ࡮ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮ࡴ࡮࡬ࡧࡪ࠮࠰࠭ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠷࠮ࡢ࡮ࡤࡱࡱࡷࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮ࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ࠯࠻࡝ࡰ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰࡯ࡥࡺࡴࡣࡩࠢࡀࠤࡦࡹࡹ࡯ࡥࠣࠬࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶ࠭ࠥࡃ࠾ࠡࡽ࡟ࡲࡱ࡫ࡴࠡࡥࡤࡴࡸࡁ࡜࡯ࡶࡵࡽࠥࢁ࡜࡯ࡥࡤࡴࡸࠦ࠽ࠡࡌࡖࡓࡓ࠴ࡰࡢࡴࡶࡩ࠭ࡨࡳࡵࡣࡦ࡯ࡤࡩࡡࡱࡵࠬࡠࡳࠦࠠࡾࠢࡦࡥࡹࡩࡨࠩࡧࡻ࠭ࠥࢁ࡜࡯ࠢࠣࠤࠥࢃ࡜࡯ࠢࠣࡶࡪࡺࡵࡳࡰࠣࡥࡼࡧࡩࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰ࡦࡳࡳࡴࡥࡤࡶࠫࡿࡡࡴࠠࠡࠢࠣࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺ࠺ࠡࡢࡺࡷࡸࡀ࠯࠰ࡥࡧࡴ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࡄࡩࡡࡱࡵࡀࠨࢀ࡫࡮ࡤࡱࡧࡩ࡚ࡘࡉࡄࡱࡰࡴࡴࡴࡥ࡯ࡶࠫࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡨࡧࡰࡴࠫࠬࢁࡥ࠲࡜࡯ࠢࠣࠤࠥ࠴࠮࠯࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳ࡝ࡰࠣࠤࢂ࠯࡜࡯ࡿ࡟ࡲ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵࡜࡯ࠩਚ")
from ._version import __version__
bstack1lll11llll_opy_ = None
CONFIG = {}
bstack1l1lll1l1_opy_ = {}
bstack11l1ll1l1l_opy_ = {}
bstack1ll1l1111_opy_ = None
bstack1111l11l1_opy_ = None
bstack1l1lll111l_opy_ = None
bstack1llll11111_opy_ = -1
bstack1ll1lllll1_opy_ = 0
bstack1l1l11l1l1_opy_ = bstack11ll11ll11_opy_
bstack1l111llll1_opy_ = 1
bstack1ll11llll_opy_ = False
bstack1l11ll111l_opy_ = False
bstack11lll1l1ll_opy_ = bstack1l1_opy_ (u"ࠫࠬਛ")
bstack1ll1ll11l_opy_ = bstack1l1_opy_ (u"ࠬ࠭ਜ")
bstack1ll1lll11_opy_ = False
bstack1ll11ll1ll_opy_ = True
bstack1ll11ll1l_opy_ = bstack1l1_opy_ (u"࠭ࠧਝ")
bstack1l1ll1ll1l_opy_ = []
bstack11ll1ll111_opy_ = bstack1l1_opy_ (u"ࠧࠨਞ")
bstack1lll11111_opy_ = False
bstack11lll1l1l1_opy_ = None
bstack11ll11l111_opy_ = None
bstack111ll1lll_opy_ = None
bstack1ll11l1l1l_opy_ = -1
bstack111llll1ll_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠨࢀࠪਟ")), bstack1l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩਠ"), bstack1l1_opy_ (u"ࠪ࠲ࡷࡵࡢࡰࡶ࠰ࡶࡪࡶ࡯ࡳࡶ࠰࡬ࡪࡲࡰࡦࡴ࠱࡮ࡸࡵ࡮ࠨਡ"))
bstack1l1llll1l1_opy_ = 0
bstack1lll11ll1_opy_ = 0
bstack1lllllll1l_opy_ = []
bstack1ll111llll_opy_ = []
bstack1l1l1ll11l_opy_ = []
bstack11l11l11l_opy_ = []
bstack111ll1l11_opy_ = bstack1l1_opy_ (u"ࠫࠬਢ")
bstack1l1l1111l1_opy_ = bstack1l1_opy_ (u"ࠬ࠭ਣ")
bstack1ll11l11l1_opy_ = False
bstack1l1lllll1_opy_ = False
bstack1ll111111_opy_ = {}
bstack1l111111ll_opy_ = None
bstack1lll1ll1ll_opy_ = None
bstack1l11l1111l_opy_ = None
bstack11ll11l11_opy_ = None
bstack11ll1l1l1l_opy_ = None
bstack1lll1l11l_opy_ = None
bstack11lllllll1_opy_ = None
bstack1l1l11lll1_opy_ = None
bstack1l1lllllll_opy_ = None
bstack1l1l1l11ll_opy_ = None
bstack1ll1l11l11_opy_ = None
bstack11ll1l111_opy_ = None
bstack1l111111l_opy_ = None
bstack1ll111l11l_opy_ = None
bstack1111l11ll_opy_ = None
bstack1lll1ll111_opy_ = None
bstack11lll11l11_opy_ = None
bstack11llll1lll_opy_ = None
bstack1ll1l1llll_opy_ = None
bstack11l11l1lll_opy_ = None
bstack1l11l1111_opy_ = None
bstack1l1l1111ll_opy_ = None
bstack1l1111lll_opy_ = False
bstack1lll1ll11_opy_ = bstack1l1_opy_ (u"ࠨࠢਤ")
logger = bstack11ll11llll_opy_.get_logger(__name__, bstack1l1l11l1l1_opy_)
bstack111l11ll_opy_ = Config.bstack11l111ll_opy_()
percy = bstack11ll1lll11_opy_()
bstack1l1l11llll_opy_ = bstack1l11l1l1l_opy_()
bstack1lllll111l_opy_ = bstack11l1l11l_opy_()
def bstack1111l1111_opy_():
  global CONFIG
  global bstack1ll11l11l1_opy_
  global bstack111l11ll_opy_
  bstack11lll1lll1_opy_ = bstack1lll1l1111_opy_(CONFIG)
  if bstack11l11lll1l_opy_(CONFIG):
    if (bstack1l1_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩਥ") in bstack11lll1lll1_opy_ and str(bstack11lll1lll1_opy_[bstack1l1_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪਦ")]).lower() == bstack1l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧਧ")):
      bstack1ll11l11l1_opy_ = True
    bstack111l11ll_opy_.bstack1l11ll1l11_opy_(bstack11lll1lll1_opy_.get(bstack1l1_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧਨ"), False))
  else:
    bstack1ll11l11l1_opy_ = True
    bstack111l11ll_opy_.bstack1l11ll1l11_opy_(True)
def bstack1ll111ll1_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1lll1lll11_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack11l111ll1_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack1l1_opy_ (u"ࠦ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡨࡵ࡮ࡧ࡫ࡪࡪ࡮ࡲࡥࠣ਩") == args[i].lower() or bstack1l1_opy_ (u"ࠧ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰࡰࡩ࡭࡬ࠨਪ") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1ll11ll1l_opy_
      bstack1ll11ll1l_opy_ += bstack1l1_opy_ (u"࠭࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡃࡰࡰࡩ࡭࡬ࡌࡩ࡭ࡧࠣࠫਫ") + path
      return path
  return None
bstack11l1l111l1_opy_ = re.compile(bstack1l1_opy_ (u"ࡲࠣ࠰࠭ࡃࡡࠪࡻࠩ࠰࠭ࡃ࠮ࢃ࠮ࠫࡁࠥਬ"))
def bstack1ll1ll11ll_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack11l1l111l1_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack1l1_opy_ (u"ࠣࠦࡾࠦਭ") + group + bstack1l1_opy_ (u"ࠤࢀࠦਮ"), os.environ.get(group))
  return value
def bstack11lll11ll_opy_():
  bstack11l1l11ll1_opy_ = bstack11l111ll1_opy_()
  if bstack11l1l11ll1_opy_ and os.path.exists(os.path.abspath(bstack11l1l11ll1_opy_)):
    fileName = bstack11l1l11ll1_opy_
  if bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋࠧਯ") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨਰ")])) and not bstack1l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡑࡥࡲ࡫ࠧ਱") in locals():
    fileName = os.environ[bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࡤࡌࡉࡍࡇࠪਲ")]
  if bstack1l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡓࡧ࡭ࡦࠩਲ਼") in locals():
    bstack111111l_opy_ = os.path.abspath(fileName)
  else:
    bstack111111l_opy_ = bstack1l1_opy_ (u"ࠨࠩ਴")
  bstack111l111ll_opy_ = os.getcwd()
  bstack1l1llllll1_opy_ = bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬਵ")
  bstack11l1l11l1l_opy_ = bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡥࡲࡲࠧਸ਼")
  while (not os.path.exists(bstack111111l_opy_)) and bstack111l111ll_opy_ != bstack1l1_opy_ (u"ࠦࠧ਷"):
    bstack111111l_opy_ = os.path.join(bstack111l111ll_opy_, bstack1l1llllll1_opy_)
    if not os.path.exists(bstack111111l_opy_):
      bstack111111l_opy_ = os.path.join(bstack111l111ll_opy_, bstack11l1l11l1l_opy_)
    if bstack111l111ll_opy_ != os.path.dirname(bstack111l111ll_opy_):
      bstack111l111ll_opy_ = os.path.dirname(bstack111l111ll_opy_)
    else:
      bstack111l111ll_opy_ = bstack1l1_opy_ (u"ࠧࠨਸ")
  return bstack111111l_opy_ if os.path.exists(bstack111111l_opy_) else None
def bstack11ll11lll_opy_():
  bstack111111l_opy_ = bstack11lll11ll_opy_()
  if not os.path.exists(bstack111111l_opy_):
    bstack1l11ll1111_opy_(
      bstack11l111l11l_opy_.format(os.getcwd()))
  try:
    with open(bstack111111l_opy_, bstack1l1_opy_ (u"࠭ࡲࠨਹ")) as stream:
      yaml.add_implicit_resolver(bstack1l1_opy_ (u"ࠢࠢࡲࡤࡸ࡭࡫ࡸࠣ਺"), bstack11l1l111l1_opy_)
      yaml.add_constructor(bstack1l1_opy_ (u"ࠣࠣࡳࡥࡹ࡮ࡥࡹࠤ਻"), bstack1ll1ll11ll_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      return config
  except:
    with open(bstack111111l_opy_, bstack1l1_opy_ (u"ࠩࡵ਼ࠫ")) as stream:
      try:
        config = yaml.safe_load(stream)
        return config
      except yaml.YAMLError as exc:
        bstack1l11ll1111_opy_(bstack11l1llll1_opy_.format(str(exc)))
def bstack11lll11111_opy_(config):
  bstack1ll1llll1l_opy_ = bstack1ll1l11111_opy_(config)
  for option in list(bstack1ll1llll1l_opy_):
    if option.lower() in bstack1l1llll11_opy_ and option != bstack1l1llll11_opy_[option.lower()]:
      bstack1ll1llll1l_opy_[bstack1l1llll11_opy_[option.lower()]] = bstack1ll1llll1l_opy_[option]
      del bstack1ll1llll1l_opy_[option]
  return config
def bstack1ll1111l11_opy_():
  global bstack11l1ll1l1l_opy_
  for key, bstack1ll1l1l11_opy_ in bstack1lll1l1l11_opy_.items():
    if isinstance(bstack1ll1l1l11_opy_, list):
      for var in bstack1ll1l1l11_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack11l1ll1l1l_opy_[key] = os.environ[var]
          break
    elif bstack1ll1l1l11_opy_ in os.environ and os.environ[bstack1ll1l1l11_opy_] and str(os.environ[bstack1ll1l1l11_opy_]).strip():
      bstack11l1ll1l1l_opy_[key] = os.environ[bstack1ll1l1l11_opy_]
  if bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ਽") in os.environ:
    bstack11l1ll1l1l_opy_[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨਾ")] = {}
    bstack11l1ll1l1l_opy_[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩਿ")][bstack1l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨੀ")] = os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩੁ")]
def bstack11l1l11lll_opy_():
  global bstack1l1lll1l1_opy_
  global bstack1ll11ll1l_opy_
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) and bstack1l1_opy_ (u"ࠨ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫੂ").lower() == val.lower():
      bstack1l1lll1l1_opy_[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭੃")] = {}
      bstack1l1lll1l1_opy_[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ੄")][bstack1l1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭੅")] = sys.argv[idx + 1]
      del sys.argv[idx:idx + 2]
      break
  for key, bstack11lll1111l_opy_ in bstack11l111l1l_opy_.items():
    if isinstance(bstack11lll1111l_opy_, list):
      for idx, val in enumerate(sys.argv):
        for var in bstack11lll1111l_opy_:
          if idx < len(sys.argv) and bstack1l1_opy_ (u"ࠬ࠳࠭ࠨ੆") + var.lower() == val.lower() and not key in bstack1l1lll1l1_opy_:
            bstack1l1lll1l1_opy_[key] = sys.argv[idx + 1]
            bstack1ll11ll1l_opy_ += bstack1l1_opy_ (u"࠭ࠠ࠮࠯ࠪੇ") + var + bstack1l1_opy_ (u"ࠧࠡࠩੈ") + sys.argv[idx + 1]
            del sys.argv[idx:idx + 2]
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx < len(sys.argv) and bstack1l1_opy_ (u"ࠨ࠯࠰ࠫ੉") + bstack11lll1111l_opy_.lower() == val.lower() and not key in bstack1l1lll1l1_opy_:
          bstack1l1lll1l1_opy_[key] = sys.argv[idx + 1]
          bstack1ll11ll1l_opy_ += bstack1l1_opy_ (u"ࠩࠣ࠱࠲࠭੊") + bstack11lll1111l_opy_ + bstack1l1_opy_ (u"ࠪࠤࠬੋ") + sys.argv[idx + 1]
          del sys.argv[idx:idx + 2]
def bstack1l1l1111l_opy_(config):
  bstack1111l111l_opy_ = config.keys()
  for bstack1ll11ll11_opy_, bstack1ll11lllll_opy_ in bstack1lllllllll_opy_.items():
    if bstack1ll11lllll_opy_ in bstack1111l111l_opy_:
      config[bstack1ll11ll11_opy_] = config[bstack1ll11lllll_opy_]
      del config[bstack1ll11lllll_opy_]
  for bstack1ll11ll11_opy_, bstack1ll11lllll_opy_ in bstack11ll11111_opy_.items():
    if isinstance(bstack1ll11lllll_opy_, list):
      for bstack11ll11l1ll_opy_ in bstack1ll11lllll_opy_:
        if bstack11ll11l1ll_opy_ in bstack1111l111l_opy_:
          config[bstack1ll11ll11_opy_] = config[bstack11ll11l1ll_opy_]
          del config[bstack11ll11l1ll_opy_]
          break
    elif bstack1ll11lllll_opy_ in bstack1111l111l_opy_:
      config[bstack1ll11ll11_opy_] = config[bstack1ll11lllll_opy_]
      del config[bstack1ll11lllll_opy_]
  for bstack11ll11l1ll_opy_ in list(config):
    for bstack11l11llll_opy_ in bstack11ll11ll1_opy_:
      if bstack11ll11l1ll_opy_.lower() == bstack11l11llll_opy_.lower() and bstack11ll11l1ll_opy_ != bstack11l11llll_opy_:
        config[bstack11l11llll_opy_] = config[bstack11ll11l1ll_opy_]
        del config[bstack11ll11l1ll_opy_]
  bstack1ll1ll1ll1_opy_ = [{}]
  if not config.get(bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧੌ")):
    config[bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ੍")] = [{}]
  bstack1ll1ll1ll1_opy_ = config[bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ੎")]
  for platform in bstack1ll1ll1ll1_opy_:
    for bstack11ll11l1ll_opy_ in list(platform):
      for bstack11l11llll_opy_ in bstack11ll11ll1_opy_:
        if bstack11ll11l1ll_opy_.lower() == bstack11l11llll_opy_.lower() and bstack11ll11l1ll_opy_ != bstack11l11llll_opy_:
          platform[bstack11l11llll_opy_] = platform[bstack11ll11l1ll_opy_]
          del platform[bstack11ll11l1ll_opy_]
  for bstack1ll11ll11_opy_, bstack1ll11lllll_opy_ in bstack11ll11111_opy_.items():
    for platform in bstack1ll1ll1ll1_opy_:
      if isinstance(bstack1ll11lllll_opy_, list):
        for bstack11ll11l1ll_opy_ in bstack1ll11lllll_opy_:
          if bstack11ll11l1ll_opy_ in platform:
            platform[bstack1ll11ll11_opy_] = platform[bstack11ll11l1ll_opy_]
            del platform[bstack11ll11l1ll_opy_]
            break
      elif bstack1ll11lllll_opy_ in platform:
        platform[bstack1ll11ll11_opy_] = platform[bstack1ll11lllll_opy_]
        del platform[bstack1ll11lllll_opy_]
  for bstack111l1l11l_opy_ in bstack1llll1l1ll_opy_:
    if bstack111l1l11l_opy_ in config:
      if not bstack1llll1l1ll_opy_[bstack111l1l11l_opy_] in config:
        config[bstack1llll1l1ll_opy_[bstack111l1l11l_opy_]] = {}
      config[bstack1llll1l1ll_opy_[bstack111l1l11l_opy_]].update(config[bstack111l1l11l_opy_])
      del config[bstack111l1l11l_opy_]
  for platform in bstack1ll1ll1ll1_opy_:
    for bstack111l1l11l_opy_ in bstack1llll1l1ll_opy_:
      if bstack111l1l11l_opy_ in list(platform):
        if not bstack1llll1l1ll_opy_[bstack111l1l11l_opy_] in platform:
          platform[bstack1llll1l1ll_opy_[bstack111l1l11l_opy_]] = {}
        platform[bstack1llll1l1ll_opy_[bstack111l1l11l_opy_]].update(platform[bstack111l1l11l_opy_])
        del platform[bstack111l1l11l_opy_]
  config = bstack11lll11111_opy_(config)
  return config
def bstack11llll1l1l_opy_(config):
  global bstack1ll1ll11l_opy_
  bstack1l11l111l1_opy_ = False
  if bstack1l1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ੏") in config and str(config[bstack1l1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ੐")]).lower() != bstack1l1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨੑ"):
    if bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ੒") not in config or str(config[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ੓")]).lower() == bstack1l1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ੔"):
      config[bstack1l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬ੕")] = False
    else:
      bstack1l1lll1111_opy_ = bstack11ll111ll1_opy_()
      if bstack1l1_opy_ (u"ࠧࡪࡵࡗࡶ࡮ࡧ࡬ࡈࡴ࡬ࡨࠬ੖") in bstack1l1lll1111_opy_:
        if not bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ੗") in config:
          config[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭੘")] = {}
        config[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧਖ਼")][bstack1l1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ਗ਼")] = bstack1l1_opy_ (u"ࠬࡧࡴࡴ࠯ࡵࡩࡵ࡫ࡡࡵࡧࡵࠫਜ਼")
        bstack1l11l111l1_opy_ = True
        bstack1ll1ll11l_opy_ = config[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪੜ")].get(bstack1l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ੝"))
  if bstack11l11lll1l_opy_(config) and bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬਫ਼") in config and str(config[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭੟")]).lower() != bstack1l1_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ੠") and not bstack1l11l111l1_opy_:
    if not bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ੡") in config:
      config[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ੢")] = {}
    if not config[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ੣")].get(bstack1l1_opy_ (u"ࠧࡴ࡭࡬ࡴࡇ࡯࡮ࡢࡴࡼࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡸࡧࡴࡪࡱࡱࠫ੤")) and not bstack1l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ੥") in config[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭੦")]:
      bstack1l111ll1_opy_ = datetime.datetime.now()
      bstack1ll1l11l1l_opy_ = bstack1l111ll1_opy_.strftime(bstack1l1_opy_ (u"ࠪࠩࡩࡥࠥࡣࡡࠨࡌࠪࡓࠧ੧"))
      hostname = socket.gethostname()
      bstack1l1l1lll11_opy_ = bstack1l1_opy_ (u"ࠫࠬ੨").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack1l1_opy_ (u"ࠬࢁࡽࡠࡽࢀࡣࢀࢃࠧ੩").format(bstack1ll1l11l1l_opy_, hostname, bstack1l1l1lll11_opy_)
      config[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ੪")][bstack1l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ੫")] = identifier
    bstack1ll1ll11l_opy_ = config[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ੬")].get(bstack1l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ੭"))
  return config
def bstack1lll1111l_opy_():
  bstack11l1l1l11_opy_ =  bstack111l1l1l1_opy_()[bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠩ੮")]
  return bstack11l1l1l11_opy_ if bstack11l1l1l11_opy_ else -1
def bstack1lll1lll1l_opy_(bstack11l1l1l11_opy_):
  global CONFIG
  if not bstack1l1_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭੯") in CONFIG[bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧੰ")]:
    return
  CONFIG[bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨੱ")] = CONFIG[bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩੲ")].replace(
    bstack1l1_opy_ (u"ࠨࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪੳ"),
    str(bstack11l1l1l11_opy_)
  )
def bstack1l1l1l1ll_opy_():
  global CONFIG
  if not bstack1l1_opy_ (u"ࠩࠧࡿࡉࡇࡔࡆࡡࡗࡍࡒࡋࡽࠨੴ") in CONFIG[bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬੵ")]:
    return
  bstack1l111ll1_opy_ = datetime.datetime.now()
  bstack1ll1l11l1l_opy_ = bstack1l111ll1_opy_.strftime(bstack1l1_opy_ (u"ࠫࠪࡪ࠭ࠦࡤ࠰ࠩࡍࡀࠥࡎࠩ੶"))
  CONFIG[bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ੷")] = CONFIG[bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ੸")].replace(
    bstack1l1_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭੹"),
    bstack1ll1l11l1l_opy_
  )
def bstack1l1l1lll1_opy_():
  global CONFIG
  if bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ੺") in CONFIG and not bool(CONFIG[bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ੻")]):
    del CONFIG[bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ੼")]
    return
  if not bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭੽") in CONFIG:
    CONFIG[bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ੾")] = bstack1l1_opy_ (u"࠭ࠣࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩ੿")
  if bstack1l1_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭઀") in CONFIG[bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪઁ")]:
    bstack1l1l1l1ll_opy_()
    os.environ[bstack1l1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭ં")] = CONFIG[bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬઃ")]
  if not bstack1l1_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭઄") in CONFIG[bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧઅ")]:
    return
  bstack11l1l1l11_opy_ = bstack1l1_opy_ (u"࠭ࠧઆ")
  bstack1llll11ll_opy_ = bstack1lll1111l_opy_()
  if bstack1llll11ll_opy_ != -1:
    bstack11l1l1l11_opy_ = bstack1l1_opy_ (u"ࠧࡄࡋࠣࠫઇ") + str(bstack1llll11ll_opy_)
  if bstack11l1l1l11_opy_ == bstack1l1_opy_ (u"ࠨࠩઈ"):
    bstack1l1l1ll111_opy_ = bstack11111ll11_opy_(CONFIG[bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬઉ")])
    if bstack1l1l1ll111_opy_ != -1:
      bstack11l1l1l11_opy_ = str(bstack1l1l1ll111_opy_)
  if bstack11l1l1l11_opy_:
    bstack1lll1lll1l_opy_(bstack11l1l1l11_opy_)
    os.environ[bstack1l1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧઊ")] = CONFIG[bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ઋ")]
def bstack111lllll1_opy_(bstack1lll111l11_opy_, bstack1lll11l11l_opy_, path):
  json_data = {
    bstack1l1_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩઌ"): bstack1lll11l11l_opy_
  }
  if os.path.exists(path):
    bstack1ll11ll11l_opy_ = json.load(open(path, bstack1l1_opy_ (u"࠭ࡲࡣࠩઍ")))
  else:
    bstack1ll11ll11l_opy_ = {}
  bstack1ll11ll11l_opy_[bstack1lll111l11_opy_] = json_data
  with open(path, bstack1l1_opy_ (u"ࠢࡸ࠭ࠥ઎")) as outfile:
    json.dump(bstack1ll11ll11l_opy_, outfile)
def bstack11111ll11_opy_(bstack1lll111l11_opy_):
  bstack1lll111l11_opy_ = str(bstack1lll111l11_opy_)
  bstack1l1l111l11_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠨࢀࠪએ")), bstack1l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩઐ"))
  try:
    if not os.path.exists(bstack1l1l111l11_opy_):
      os.makedirs(bstack1l1l111l11_opy_)
    file_path = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠪࢂࠬઑ")), bstack1l1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ઒"), bstack1l1_opy_ (u"ࠬ࠴ࡢࡶ࡫࡯ࡨ࠲ࡴࡡ࡮ࡧ࠰ࡧࡦࡩࡨࡦ࠰࡭ࡷࡴࡴࠧઓ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack1l1_opy_ (u"࠭ࡷࠨઔ")):
        pass
      with open(file_path, bstack1l1_opy_ (u"ࠢࡸ࠭ࠥક")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack1l1_opy_ (u"ࠨࡴࠪખ")) as bstack11l111ll1l_opy_:
      bstack1lll1l1ll1_opy_ = json.load(bstack11l111ll1l_opy_)
    if bstack1lll111l11_opy_ in bstack1lll1l1ll1_opy_:
      bstack1ll1lllll_opy_ = bstack1lll1l1ll1_opy_[bstack1lll111l11_opy_][bstack1l1_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ગ")]
      bstack111111l11_opy_ = int(bstack1ll1lllll_opy_) + 1
      bstack111lllll1_opy_(bstack1lll111l11_opy_, bstack111111l11_opy_, file_path)
      return bstack111111l11_opy_
    else:
      bstack111lllll1_opy_(bstack1lll111l11_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1lll11l1ll_opy_.format(str(e)))
    return -1
def bstack1l111l11l_opy_(config):
  if not config[bstack1l1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬઘ")] or not config[bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧઙ")]:
    return True
  else:
    return False
def bstack11ll11ll1l_opy_(config, index=0):
  global bstack1ll1lll11_opy_
  bstack1l1111ll1l_opy_ = {}
  caps = bstack1l1l11ll1_opy_ + bstack111ll1111_opy_
  if config.get(bstack1l1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩચ"), False):
    bstack1l1111ll1l_opy_[bstack1l1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪછ")] = True
    bstack1l1111ll1l_opy_[bstack1l1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶࠫજ")] = config.get(bstack1l1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࡔࡶࡴࡪࡱࡱࡷࠬઝ"), {})
  if bstack1ll1lll11_opy_:
    caps += bstack111l11lll_opy_
  for key in config:
    if key in caps + [bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬઞ")]:
      continue
    bstack1l1111ll1l_opy_[key] = config[key]
  if bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ટ") in config:
    for bstack1l1l11111l_opy_ in config[bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧઠ")][index]:
      if bstack1l1l11111l_opy_ in caps:
        continue
      bstack1l1111ll1l_opy_[bstack1l1l11111l_opy_] = config[bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨડ")][index][bstack1l1l11111l_opy_]
  bstack1l1111ll1l_opy_[bstack1l1_opy_ (u"࠭ࡨࡰࡵࡷࡒࡦࡳࡥࠨઢ")] = socket.gethostname()
  if bstack1l1_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨણ") in bstack1l1111ll1l_opy_:
    del (bstack1l1111ll1l_opy_[bstack1l1_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩત")])
  return bstack1l1111ll1l_opy_
def bstack11l11ll1l_opy_(config):
  global bstack1ll1lll11_opy_
  bstack1lllll111_opy_ = {}
  caps = bstack111ll1111_opy_
  if bstack1ll1lll11_opy_:
    caps += bstack111l11lll_opy_
  for key in caps:
    if key in config:
      bstack1lllll111_opy_[key] = config[key]
  return bstack1lllll111_opy_
def bstack11lll111ll_opy_(bstack1l1111ll1l_opy_, bstack1lllll111_opy_):
  bstack11l1ll1l11_opy_ = {}
  for key in bstack1l1111ll1l_opy_.keys():
    if key in bstack1lllllllll_opy_:
      bstack11l1ll1l11_opy_[bstack1lllllllll_opy_[key]] = bstack1l1111ll1l_opy_[key]
    else:
      bstack11l1ll1l11_opy_[key] = bstack1l1111ll1l_opy_[key]
  for key in bstack1lllll111_opy_:
    if key in bstack1lllllllll_opy_:
      bstack11l1ll1l11_opy_[bstack1lllllllll_opy_[key]] = bstack1lllll111_opy_[key]
    else:
      bstack11l1ll1l11_opy_[key] = bstack1lllll111_opy_[key]
  return bstack11l1ll1l11_opy_
def bstack11lll1ll1l_opy_(config, index=0):
  global bstack1ll1lll11_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack11l11ll1l1_opy_ = bstack1l1lll1l11_opy_(bstack1l1111lll1_opy_, config, logger)
  bstack1lllll111_opy_ = bstack11l11ll1l_opy_(config)
  bstack1lll111ll_opy_ = bstack111ll1111_opy_
  bstack1lll111ll_opy_ += bstack1l11l1lll1_opy_
  bstack1lllll111_opy_ = update(bstack1lllll111_opy_, bstack11l11ll1l1_opy_)
  if bstack1ll1lll11_opy_:
    bstack1lll111ll_opy_ += bstack111l11lll_opy_
  if bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬથ") in config:
    if bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨદ") in config[bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧધ")][index]:
      caps[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪન")] = config[bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ઩")][index][bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬપ")]
    if bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩફ") in config[bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬબ")][index]:
      caps[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫભ")] = str(config[bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧમ")][index][bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ય")])
    bstack11l11lllll_opy_ = bstack1l1lll1l11_opy_(bstack1l1111lll1_opy_, config[bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩર")][index], logger)
    bstack1lll111ll_opy_ += list(bstack11l11lllll_opy_.keys())
    for bstack11llllll1_opy_ in bstack1lll111ll_opy_:
      if bstack11llllll1_opy_ in config[bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ઱")][index]:
        if bstack11llllll1_opy_ == bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪલ"):
          try:
            bstack11l11lllll_opy_[bstack11llllll1_opy_] = str(config[bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬળ")][index][bstack11llllll1_opy_] * 1.0)
          except:
            bstack11l11lllll_opy_[bstack11llllll1_opy_] = str(config[bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭઴")][index][bstack11llllll1_opy_])
        else:
          bstack11l11lllll_opy_[bstack11llllll1_opy_] = config[bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧવ")][index][bstack11llllll1_opy_]
        del (config[bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨશ")][index][bstack11llllll1_opy_])
    bstack1lllll111_opy_ = update(bstack1lllll111_opy_, bstack11l11lllll_opy_)
  bstack1l1111ll1l_opy_ = bstack11ll11ll1l_opy_(config, index)
  for bstack11ll11l1ll_opy_ in bstack111ll1111_opy_ + list(bstack11l11ll1l1_opy_.keys()):
    if bstack11ll11l1ll_opy_ in bstack1l1111ll1l_opy_:
      bstack1lllll111_opy_[bstack11ll11l1ll_opy_] = bstack1l1111ll1l_opy_[bstack11ll11l1ll_opy_]
      del (bstack1l1111ll1l_opy_[bstack11ll11l1ll_opy_])
  if bstack11llllll11_opy_(config):
    bstack1l1111ll1l_opy_[bstack1l1_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ષ")] = True
    caps.update(bstack1lllll111_opy_)
    caps[bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨસ")] = bstack1l1111ll1l_opy_
  else:
    bstack1l1111ll1l_opy_[bstack1l1_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨહ")] = False
    caps.update(bstack11lll111ll_opy_(bstack1l1111ll1l_opy_, bstack1lllll111_opy_))
    if bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ઺") in caps:
      caps[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫ઻")] = caps[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦ઼ࠩ")]
      del (caps[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪઽ")])
    if bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧા") in caps:
      caps[bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩિ")] = caps[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩી")]
      del (caps[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪુ")])
  return caps
def bstack1ll1ll11l1_opy_():
  global bstack11ll1ll111_opy_
  global CONFIG
  if bstack1lll1lll11_opy_() <= version.parse(bstack1l1_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪૂ")):
    if bstack11ll1ll111_opy_ != bstack1l1_opy_ (u"ࠫࠬૃ"):
      return bstack1l1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨૄ") + bstack11ll1ll111_opy_ + bstack1l1_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥૅ")
    return bstack11l1111l1l_opy_
  if bstack11ll1ll111_opy_ != bstack1l1_opy_ (u"ࠧࠨ૆"):
    return bstack1l1_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥે") + bstack11ll1ll111_opy_ + bstack1l1_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥૈ")
  return bstack11l11l1ll1_opy_
def bstack11l1ll1111_opy_(options):
  return hasattr(options, bstack1l1_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫૉ"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack11l1ll111l_opy_(options, bstack1l111ll11l_opy_):
  for bstack11ll1111l1_opy_ in bstack1l111ll11l_opy_:
    if bstack11ll1111l1_opy_ in [bstack1l1_opy_ (u"ࠫࡦࡸࡧࡴࠩ૊"), bstack1l1_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩો")]:
      continue
    if bstack11ll1111l1_opy_ in options._experimental_options:
      options._experimental_options[bstack11ll1111l1_opy_] = update(options._experimental_options[bstack11ll1111l1_opy_],
                                                         bstack1l111ll11l_opy_[bstack11ll1111l1_opy_])
    else:
      options.add_experimental_option(bstack11ll1111l1_opy_, bstack1l111ll11l_opy_[bstack11ll1111l1_opy_])
  if bstack1l1_opy_ (u"࠭ࡡࡳࡩࡶࠫૌ") in bstack1l111ll11l_opy_:
    for arg in bstack1l111ll11l_opy_[bstack1l1_opy_ (u"ࠧࡢࡴࡪࡷ્ࠬ")]:
      options.add_argument(arg)
    del (bstack1l111ll11l_opy_[bstack1l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭૎")])
  if bstack1l1_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭૏") in bstack1l111ll11l_opy_:
    for ext in bstack1l111ll11l_opy_[bstack1l1_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧૐ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack1l111ll11l_opy_[bstack1l1_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ૑")])
def bstack11lll1l11l_opy_(options, bstack1l1ll1lll_opy_):
  if bstack1l1_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ૒") in bstack1l1ll1lll_opy_:
    for bstack1l11l1l1l1_opy_ in bstack1l1ll1lll_opy_[bstack1l1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ૓")]:
      if bstack1l11l1l1l1_opy_ in options._preferences:
        options._preferences[bstack1l11l1l1l1_opy_] = update(options._preferences[bstack1l11l1l1l1_opy_], bstack1l1ll1lll_opy_[bstack1l1_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭૔")][bstack1l11l1l1l1_opy_])
      else:
        options.set_preference(bstack1l11l1l1l1_opy_, bstack1l1ll1lll_opy_[bstack1l1_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ૕")][bstack1l11l1l1l1_opy_])
  if bstack1l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ૖") in bstack1l1ll1lll_opy_:
    for arg in bstack1l1ll1lll_opy_[bstack1l1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ૗")]:
      options.add_argument(arg)
def bstack111l1ll1l_opy_(options, bstack11ll111ll_opy_):
  if bstack1l1_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࠬ૘") in bstack11ll111ll_opy_:
    options.use_webview(bool(bstack11ll111ll_opy_[bstack1l1_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼ࠭૙")]))
  bstack11l1ll111l_opy_(options, bstack11ll111ll_opy_)
def bstack11llll11l1_opy_(options, bstack111lllll1l_opy_):
  for bstack1ll1llll1_opy_ in bstack111lllll1l_opy_:
    if bstack1ll1llll1_opy_ in [bstack1l1_opy_ (u"࠭ࡴࡦࡥ࡫ࡲࡴࡲ࡯ࡨࡻࡓࡶࡪࡼࡩࡦࡹࠪ૚"), bstack1l1_opy_ (u"ࠧࡢࡴࡪࡷࠬ૛")]:
      continue
    options.set_capability(bstack1ll1llll1_opy_, bstack111lllll1l_opy_[bstack1ll1llll1_opy_])
  if bstack1l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭૜") in bstack111lllll1l_opy_:
    for arg in bstack111lllll1l_opy_[bstack1l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ૝")]:
      options.add_argument(arg)
  if bstack1l1_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧ૞") in bstack111lllll1l_opy_:
    options.bstack11l11l1ll_opy_(bool(bstack111lllll1l_opy_[bstack1l1_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨ૟")]))
def bstack1l1l111l1l_opy_(options, bstack1l11ll1ll1_opy_):
  for bstack11lllll111_opy_ in bstack1l11ll1ll1_opy_:
    if bstack11lllll111_opy_ in [bstack1l1_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩૠ"), bstack1l1_opy_ (u"࠭ࡡࡳࡩࡶࠫૡ")]:
      continue
    options._options[bstack11lllll111_opy_] = bstack1l11ll1ll1_opy_[bstack11lllll111_opy_]
  if bstack1l1_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫૢ") in bstack1l11ll1ll1_opy_:
    for bstack1l1ll11ll_opy_ in bstack1l11ll1ll1_opy_[bstack1l1_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬૣ")]:
      options.bstack1l111l11ll_opy_(
        bstack1l1ll11ll_opy_, bstack1l11ll1ll1_opy_[bstack1l1_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭૤")][bstack1l1ll11ll_opy_])
  if bstack1l1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ૥") in bstack1l11ll1ll1_opy_:
    for arg in bstack1l11ll1ll1_opy_[bstack1l1_opy_ (u"ࠫࡦࡸࡧࡴࠩ૦")]:
      options.add_argument(arg)
def bstack1l1l1l1ll1_opy_(options, caps):
  if not hasattr(options, bstack1l1_opy_ (u"ࠬࡑࡅ࡚ࠩ૧")):
    return
  if options.KEY == bstack1l1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ૨") and options.KEY in caps:
    bstack11l1ll111l_opy_(options, caps[bstack1l1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ૩")])
  elif options.KEY == bstack1l1_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭૪") and options.KEY in caps:
    bstack11lll1l11l_opy_(options, caps[bstack1l1_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧ૫")])
  elif options.KEY == bstack1l1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫ૬") and options.KEY in caps:
    bstack11llll11l1_opy_(options, caps[bstack1l1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬ૭")])
  elif options.KEY == bstack1l1_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭૮") and options.KEY in caps:
    bstack111l1ll1l_opy_(options, caps[bstack1l1_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ૯")])
  elif options.KEY == bstack1l1_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭૰") and options.KEY in caps:
    bstack1l1l111l1l_opy_(options, caps[bstack1l1_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ૱")])
def bstack1ll1ll111_opy_(caps):
  global bstack1ll1lll11_opy_
  if isinstance(os.environ.get(bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ૲")), str):
    bstack1ll1lll11_opy_ = eval(os.getenv(bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ૳")))
  if bstack1ll1lll11_opy_:
    if bstack1ll111ll1_opy_() < version.parse(bstack1l1_opy_ (u"ࠫ࠷࠴࠳࠯࠲ࠪ૴")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack1l1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ૵")
    if bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ૶") in caps:
      browser = caps[bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ૷")]
    elif bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩ૸") in caps:
      browser = caps[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪૹ")]
    browser = str(browser).lower()
    if browser == bstack1l1_opy_ (u"ࠪ࡭ࡵ࡮࡯࡯ࡧࠪૺ") or browser == bstack1l1_opy_ (u"ࠫ࡮ࡶࡡࡥࠩૻ"):
      browser = bstack1l1_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬૼ")
    if browser == bstack1l1_opy_ (u"࠭ࡳࡢ࡯ࡶࡹࡳ࡭ࠧ૽"):
      browser = bstack1l1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ૾")
    if browser not in [bstack1l1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ૿"), bstack1l1_opy_ (u"ࠩࡨࡨ࡬࡫ࠧ଀"), bstack1l1_opy_ (u"ࠪ࡭ࡪ࠭ଁ"), bstack1l1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫଂ"), bstack1l1_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭ଃ")]:
      return None
    try:
      package = bstack1l1_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵ࠲ࢀࢃ࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨ଄").format(browser)
      name = bstack1l1_opy_ (u"ࠧࡐࡲࡷ࡭ࡴࡴࡳࠨଅ")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack11l1ll1111_opy_(options):
        return None
      for bstack11ll11l1ll_opy_ in caps.keys():
        options.set_capability(bstack11ll11l1ll_opy_, caps[bstack11ll11l1ll_opy_])
      bstack1l1l1l1ll1_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1l11lllll_opy_(options, bstack1llll1l111_opy_):
  if not bstack11l1ll1111_opy_(options):
    return
  for bstack11ll11l1ll_opy_ in bstack1llll1l111_opy_.keys():
    if bstack11ll11l1ll_opy_ in bstack1l11l1lll1_opy_:
      continue
    if bstack11ll11l1ll_opy_ in options._caps and type(options._caps[bstack11ll11l1ll_opy_]) in [dict, list]:
      options._caps[bstack11ll11l1ll_opy_] = update(options._caps[bstack11ll11l1ll_opy_], bstack1llll1l111_opy_[bstack11ll11l1ll_opy_])
    else:
      options.set_capability(bstack11ll11l1ll_opy_, bstack1llll1l111_opy_[bstack11ll11l1ll_opy_])
  bstack1l1l1l1ll1_opy_(options, bstack1llll1l111_opy_)
  if bstack1l1_opy_ (u"ࠨ࡯ࡲࡾ࠿ࡪࡥࡣࡷࡪ࡫ࡪࡸࡁࡥࡦࡵࡩࡸࡹࠧଆ") in options._caps:
    if options._caps[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧଇ")] and options._caps[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨଈ")].lower() != bstack1l1_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬଉ"):
      del options._caps[bstack1l1_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡧࡩࡧࡻࡧࡨࡧࡵࡅࡩࡪࡲࡦࡵࡶࠫଊ")]
def bstack11l1l1111l_opy_(proxy_config):
  if bstack1l1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪଋ") in proxy_config:
    proxy_config[bstack1l1_opy_ (u"ࠧࡴࡵ࡯ࡔࡷࡵࡸࡺࠩଌ")] = proxy_config[bstack1l1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ଍")]
    del (proxy_config[bstack1l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭଎")])
  if bstack1l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭ଏ") in proxy_config and proxy_config[bstack1l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧଐ")].lower() != bstack1l1_opy_ (u"ࠬࡪࡩࡳࡧࡦࡸࠬ଑"):
    proxy_config[bstack1l1_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡙ࡿࡰࡦࠩ଒")] = bstack1l1_opy_ (u"ࠧ࡮ࡣࡱࡹࡦࡲࠧଓ")
  if bstack1l1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡁࡶࡶࡲࡧࡴࡴࡦࡪࡩࡘࡶࡱ࠭ଔ") in proxy_config:
    proxy_config[bstack1l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬକ")] = bstack1l1_opy_ (u"ࠪࡴࡦࡩࠧଖ")
  return proxy_config
def bstack1l11l11l1l_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack1l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪଗ") in config:
    return proxy
  config[bstack1l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫଘ")] = bstack11l1l1111l_opy_(config[bstack1l1_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬଙ")])
  if proxy == None:
    proxy = Proxy(config[bstack1l1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭ଚ")])
  return proxy
def bstack11l11llll1_opy_(self):
  global CONFIG
  global bstack11ll1l111_opy_
  try:
    proxy = bstack1l1ll11lll_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack1l1_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭ଛ")):
        proxies = bstack1ll1111l1l_opy_(proxy, bstack1ll1ll11l1_opy_())
        if len(proxies) > 0:
          protocol, bstack1l1l111lll_opy_ = proxies.popitem()
          if bstack1l1_opy_ (u"ࠤ࠽࠳࠴ࠨଜ") in bstack1l1l111lll_opy_:
            return bstack1l1l111lll_opy_
          else:
            return bstack1l1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦଝ") + bstack1l1l111lll_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack1l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡱࡴࡲࡼࡾࠦࡵࡳ࡮ࠣ࠾ࠥࢁࡽࠣଞ").format(str(e)))
  return bstack11ll1l111_opy_(self)
def bstack1l1l11l11l_opy_():
  global CONFIG
  return bstack11l11l11ll_opy_(CONFIG) and bstack111111ll1_opy_() and bstack1lll1lll11_opy_() >= version.parse(bstack1ll11l111l_opy_)
def bstack111llll11_opy_():
  global CONFIG
  return (bstack1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨଟ") in CONFIG or bstack1l1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪଠ") in CONFIG) and bstack1ll11llll1_opy_()
def bstack1ll1l11111_opy_(config):
  bstack1ll1llll1l_opy_ = {}
  if bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫଡ") in config:
    bstack1ll1llll1l_opy_ = config[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬଢ")]
  if bstack1l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨଣ") in config:
    bstack1ll1llll1l_opy_ = config[bstack1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩତ")]
  proxy = bstack1l1ll11lll_opy_(config)
  if proxy:
    if proxy.endswith(bstack1l1_opy_ (u"ࠫ࠳ࡶࡡࡤࠩଥ")) and os.path.isfile(proxy):
      bstack1ll1llll1l_opy_[bstack1l1_opy_ (u"ࠬ࠳ࡰࡢࡥ࠰ࡪ࡮ࡲࡥࠨଦ")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack1l1_opy_ (u"࠭࠮ࡱࡣࡦࠫଧ")):
        proxies = bstack1lll1l1lll_opy_(config, bstack1ll1ll11l1_opy_())
        if len(proxies) > 0:
          protocol, bstack1l1l111lll_opy_ = proxies.popitem()
          if bstack1l1_opy_ (u"ࠢ࠻࠱࠲ࠦନ") in bstack1l1l111lll_opy_:
            parsed_url = urlparse(bstack1l1l111lll_opy_)
          else:
            parsed_url = urlparse(protocol + bstack1l1_opy_ (u"ࠣ࠼࠲࠳ࠧ଩") + bstack1l1l111lll_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1ll1llll1l_opy_[bstack1l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡉࡱࡶࡸࠬପ")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1ll1llll1l_opy_[bstack1l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡲࡶࡹ࠭ଫ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1ll1llll1l_opy_[bstack1l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡘࡷࡪࡸࠧବ")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1ll1llll1l_opy_[bstack1l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡦࡹࡳࠨଭ")] = str(parsed_url.password)
  return bstack1ll1llll1l_opy_
def bstack1lll1l1111_opy_(config):
  if bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠫମ") in config:
    return config[bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬଯ")]
  return {}
def bstack1l1l1l1lll_opy_(caps):
  global bstack1ll1ll11l_opy_
  if bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩର") in caps:
    caps[bstack1l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ଱")][bstack1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩଲ")] = True
    if bstack1ll1ll11l_opy_:
      caps[bstack1l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬଳ")][bstack1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ଴")] = bstack1ll1ll11l_opy_
  else:
    caps[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࠫଵ")] = True
    if bstack1ll1ll11l_opy_:
      caps[bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨଶ")] = bstack1ll1ll11l_opy_
def bstack11ll1l1111_opy_():
  global CONFIG
  if not bstack11l11lll1l_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬଷ") in CONFIG and bstack1ll11l11l_opy_(CONFIG[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ସ")]):
    if (
      bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧହ") in CONFIG
      and bstack1ll11l11l_opy_(CONFIG[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ଺")].get(bstack1l1_opy_ (u"ࠬࡹ࡫ࡪࡲࡅ࡭ࡳࡧࡲࡺࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡥࡹ࡯࡯࡯ࠩ଻")))
    ):
      logger.debug(bstack1l1_opy_ (u"ࠨࡌࡰࡥࡤࡰࠥࡨࡩ࡯ࡣࡵࡽࠥࡴ࡯ࡵࠢࡶࡸࡦࡸࡴࡦࡦࠣࡥࡸࠦࡳ࡬࡫ࡳࡆ࡮ࡴࡡࡳࡻࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡦࡺࡩࡰࡰࠣ࡭ࡸࠦࡥ࡯ࡣࡥࡰࡪࡪ଼ࠢ"))
      return
    bstack1ll1llll1l_opy_ = bstack1ll1l11111_opy_(CONFIG)
    bstack11l1l111l_opy_(CONFIG[bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪଽ")], bstack1ll1llll1l_opy_)
def bstack11l1l111l_opy_(key, bstack1ll1llll1l_opy_):
  global bstack1lll11llll_opy_
  logger.info(bstack1l11ll1l1l_opy_)
  try:
    bstack1lll11llll_opy_ = Local()
    bstack11l1111ll_opy_ = {bstack1l1_opy_ (u"ࠨ࡭ࡨࡽࠬା"): key}
    bstack11l1111ll_opy_.update(bstack1ll1llll1l_opy_)
    logger.debug(bstack11lllll11l_opy_.format(str(bstack11l1111ll_opy_)))
    bstack1lll11llll_opy_.start(**bstack11l1111ll_opy_)
    if bstack1lll11llll_opy_.isRunning():
      logger.info(bstack1l11l1l111_opy_)
  except Exception as e:
    bstack1l11ll1111_opy_(bstack11l11ll11l_opy_.format(str(e)))
def bstack1l11lllll1_opy_():
  global bstack1lll11llll_opy_
  if bstack1lll11llll_opy_.isRunning():
    logger.info(bstack1l11lll1l1_opy_)
    bstack1lll11llll_opy_.stop()
  bstack1lll11llll_opy_ = None
def bstack1lll111ll1_opy_(bstack11l1ll1ll1_opy_=[]):
  global CONFIG
  bstack1lllllll11_opy_ = []
  bstack1l11ll11l_opy_ = [bstack1l1_opy_ (u"ࠩࡲࡷࠬି"), bstack1l1_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ୀ"), bstack1l1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨୁ"), bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧୂ"), bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫୃ"), bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨୄ")]
  try:
    for err in bstack11l1ll1ll1_opy_:
      bstack1llll1l11_opy_ = {}
      for k in bstack1l11ll11l_opy_:
        val = CONFIG[bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ୅")][int(err[bstack1l1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ୆")])].get(k)
        if val:
          bstack1llll1l11_opy_[k] = val
      if(err[bstack1l1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩେ")] != bstack1l1_opy_ (u"ࠫࠬୈ")):
        bstack1llll1l11_opy_[bstack1l1_opy_ (u"ࠬࡺࡥࡴࡶࡶࠫ୉")] = {
          err[bstack1l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ୊")]: err[bstack1l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ୋ")]
        }
        bstack1lllllll11_opy_.append(bstack1llll1l11_opy_)
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪࡴࡸ࡭ࡢࡶࡷ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴ࠻ࠢࠪୌ") + str(e))
  finally:
    return bstack1lllllll11_opy_
def bstack1lll111111_opy_(file_name):
  bstack1llllll1ll_opy_ = []
  try:
    bstack1ll11l1lll_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1ll11l1lll_opy_):
      with open(bstack1ll11l1lll_opy_) as f:
        bstack1l11l1ll11_opy_ = json.load(f)
        bstack1llllll1ll_opy_ = bstack1l11l1ll11_opy_
      os.remove(bstack1ll11l1lll_opy_)
    return bstack1llllll1ll_opy_
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫࡯࡮ࡥ࡫ࡱ࡫ࠥ࡫ࡲࡳࡱࡵࠤࡱ࡯ࡳࡵ࠼୍ࠣࠫ") + str(e))
    return bstack1llllll1ll_opy_
def bstack1l1ll1111l_opy_():
  global bstack1lll1ll11_opy_
  global bstack1l1ll1ll1l_opy_
  global bstack1lllllll1l_opy_
  global bstack1ll111llll_opy_
  global bstack1l1l1ll11l_opy_
  global bstack1l1l1111l1_opy_
  global CONFIG
  bstack1lll1llll_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫ୎"))
  if bstack1lll1llll_opy_ in [bstack1l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ୏"), bstack1l1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ୐")]:
    bstack1l1111111l_opy_()
  percy.shutdown()
  if bstack1lll1ll11_opy_:
    logger.warning(bstack11lll1111_opy_.format(str(bstack1lll1ll11_opy_)))
  else:
    try:
      bstack1ll11ll11l_opy_ = bstack1llllll11l_opy_(bstack1l1_opy_ (u"࠭࠮ࡣࡵࡷࡥࡨࡱ࠭ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬ୑"), logger)
      if bstack1ll11ll11l_opy_.get(bstack1l1_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬ୒")) and bstack1ll11ll11l_opy_.get(bstack1l1_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭୓")).get(bstack1l1_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫ୔")):
        logger.warning(bstack11lll1111_opy_.format(str(bstack1ll11ll11l_opy_[bstack1l1_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨ୕")][bstack1l1_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ࠭ୖ")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack1llll1l11l_opy_.invoke(Events.bstack1ll111l1l_opy_)
  logger.info(bstack11l111l111_opy_)
  global bstack1lll11llll_opy_
  if bstack1lll11llll_opy_:
    bstack1l11lllll1_opy_()
  try:
    for driver in bstack1l1ll1ll1l_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1l1l1l1l1_opy_)
  if bstack1l1l1111l1_opy_ == bstack1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫୗ"):
    bstack1l1l1ll11l_opy_ = bstack1lll111111_opy_(bstack1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧ୘"))
  if bstack1l1l1111l1_opy_ == bstack1l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ୙") and len(bstack1ll111llll_opy_) == 0:
    bstack1ll111llll_opy_ = bstack1lll111111_opy_(bstack1l1_opy_ (u"ࠨࡲࡺࡣࡵࡿࡴࡦࡵࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭୚"))
    if len(bstack1ll111llll_opy_) == 0:
      bstack1ll111llll_opy_ = bstack1lll111111_opy_(bstack1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡳࡴࡵࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨ୛"))
  bstack1111111l1_opy_ = bstack1l1_opy_ (u"ࠪࠫଡ଼")
  if len(bstack1lllllll1l_opy_) > 0:
    bstack1111111l1_opy_ = bstack1lll111ll1_opy_(bstack1lllllll1l_opy_)
  elif len(bstack1ll111llll_opy_) > 0:
    bstack1111111l1_opy_ = bstack1lll111ll1_opy_(bstack1ll111llll_opy_)
  elif len(bstack1l1l1ll11l_opy_) > 0:
    bstack1111111l1_opy_ = bstack1lll111ll1_opy_(bstack1l1l1ll11l_opy_)
  elif len(bstack11l11l11l_opy_) > 0:
    bstack1111111l1_opy_ = bstack1lll111ll1_opy_(bstack11l11l11l_opy_)
  if bool(bstack1111111l1_opy_):
    bstack1111lll11_opy_(bstack1111111l1_opy_)
  else:
    bstack1111lll11_opy_()
  bstack11llll111_opy_(bstack1111l1ll1_opy_, logger)
  bstack11ll11llll_opy_.bstack1lll1111_opy_(CONFIG)
  if len(bstack1l1l1ll11l_opy_) > 0:
    sys.exit(len(bstack1l1l1ll11l_opy_))
def bstack1ll111lll_opy_(bstack1l1llll11l_opy_, frame):
  global bstack111l11ll_opy_
  logger.error(bstack1l11111l1_opy_)
  bstack111l11ll_opy_.set_property(bstack1l1_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡓࡵࠧଢ଼"), bstack1l1llll11l_opy_)
  if hasattr(signal, bstack1l1_opy_ (u"࡙ࠬࡩࡨࡰࡤࡰࡸ࠭୞")):
    bstack111l11ll_opy_.set_property(bstack1l1_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭ୟ"), signal.Signals(bstack1l1llll11l_opy_).name)
  else:
    bstack111l11ll_opy_.set_property(bstack1l1_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧୠ"), bstack1l1_opy_ (u"ࠨࡕࡌࡋ࡚ࡔࡋࡏࡑ࡚ࡒࠬୡ"))
  if cli.is_running():
    bstack1llll1l11l_opy_.invoke(Events.bstack1ll111l1l_opy_)
  bstack1lll1llll_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪୢ"))
  if bstack1lll1llll_opy_ == bstack1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪୣ") and not cli.is_enabled(CONFIG):
    bstack1l1ll1l1_opy_.stop(bstack111l11ll_opy_.get_property(bstack1l1_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡘ࡯ࡧ࡯ࡣ࡯ࠫ୤")))
  bstack1l1ll1111l_opy_()
  sys.exit(1)
def bstack1l11ll1111_opy_(err):
  logger.critical(bstack11llll1ll_opy_.format(str(err)))
  bstack1111lll11_opy_(bstack11llll1ll_opy_.format(str(err)), True)
  atexit.unregister(bstack1l1ll1111l_opy_)
  bstack1l1111111l_opy_()
  sys.exit(1)
def bstack1l1l1lll1l_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1111lll11_opy_(message, True)
  atexit.unregister(bstack1l1ll1111l_opy_)
  bstack1l1111111l_opy_()
  sys.exit(1)
def bstack1llll11l1_opy_():
  global CONFIG
  global bstack1l1lll1l1_opy_
  global bstack11l1ll1l1l_opy_
  global bstack1ll11ll1ll_opy_
  CONFIG = bstack11ll11lll_opy_()
  load_dotenv(CONFIG.get(bstack1l1_opy_ (u"ࠬ࡫࡮ࡷࡈ࡬ࡰࡪ࠭୥")))
  bstack1ll1111l11_opy_()
  bstack11l1l11lll_opy_()
  CONFIG = bstack1l1l1111l_opy_(CONFIG)
  update(CONFIG, bstack11l1ll1l1l_opy_)
  update(CONFIG, bstack1l1lll1l1_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack11llll1l1l_opy_(CONFIG)
  bstack1ll11ll1ll_opy_ = bstack11l11lll1l_opy_(CONFIG)
  os.environ[bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩ୦")] = bstack1ll11ll1ll_opy_.__str__()
  bstack111l11ll_opy_.set_property(bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨ୧"), bstack1ll11ll1ll_opy_)
  if (bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ୨") in CONFIG and bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ୩") in bstack1l1lll1l1_opy_) or (
          bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭୪") in CONFIG and bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ୫") not in bstack11l1ll1l1l_opy_):
    if os.getenv(bstack1l1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩ୬")):
      CONFIG[bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ୭")] = os.getenv(bstack1l1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫ୮"))
    else:
      if not CONFIG.get(bstack1l1_opy_ (u"ࠣࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠦ୯"), bstack1l1_opy_ (u"ࠤࠥ୰")) in bstack1llll1ll11_opy_:
        bstack1l1l1lll1_opy_()
  elif (bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ୱ") not in CONFIG and bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭୲") in CONFIG) or (
          bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ୳") in bstack11l1ll1l1l_opy_ and bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ୴") not in bstack1l1lll1l1_opy_):
    del (CONFIG[bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ୵")])
  if bstack1l111l11l_opy_(CONFIG):
    bstack1l11ll1111_opy_(bstack1ll1lll1ll_opy_)
  bstack1l111ll111_opy_()
  bstack1l11l11l11_opy_()
  if bstack1ll1lll11_opy_ and not CONFIG.get(bstack1l1_opy_ (u"ࠣࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠦ୶"), bstack1l1_opy_ (u"ࠤࠥ୷")) in bstack1llll1ll11_opy_:
    CONFIG[bstack1l1_opy_ (u"ࠪࡥࡵࡶࠧ୸")] = bstack11ll11l1l_opy_(CONFIG)
    logger.info(bstack1l1111l1ll_opy_.format(CONFIG[bstack1l1_opy_ (u"ࠫࡦࡶࡰࠨ୹")]))
  if not bstack1ll11ll1ll_opy_:
    CONFIG[bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ୺")] = [{}]
def bstack1l1lllll1l_opy_(config, bstack1l1111ll1_opy_):
  global CONFIG
  global bstack1ll1lll11_opy_
  CONFIG = config
  bstack1ll1lll11_opy_ = bstack1l1111ll1_opy_
def bstack1l11l11l11_opy_():
  global CONFIG
  global bstack1ll1lll11_opy_
  if bstack1l1_opy_ (u"࠭ࡡࡱࡲࠪ୻") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1l1l1lll1l_opy_(e, bstack11ll1llll_opy_)
    bstack1ll1lll11_opy_ = True
    bstack111l11ll_opy_.set_property(bstack1l1_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭୼"), True)
def bstack11ll11l1l_opy_(config):
  bstack11l11ll11_opy_ = bstack1l1_opy_ (u"ࠨࠩ୽")
  app = config[bstack1l1_opy_ (u"ࠩࡤࡴࡵ࠭୾")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1ll111lll1_opy_:
      if os.path.exists(app):
        bstack11l11ll11_opy_ = bstack1l11l11111_opy_(config, app)
      elif bstack1l1l11111_opy_(app):
        bstack11l11ll11_opy_ = app
      else:
        bstack1l11ll1111_opy_(bstack1111l1l1l_opy_.format(app))
    else:
      if bstack1l1l11111_opy_(app):
        bstack11l11ll11_opy_ = app
      elif os.path.exists(app):
        bstack11l11ll11_opy_ = bstack1l11l11111_opy_(app)
      else:
        bstack1l11ll1111_opy_(bstack11ll111l11_opy_)
  else:
    if len(app) > 2:
      bstack1l11ll1111_opy_(bstack111llll1l1_opy_)
    elif len(app) == 2:
      if bstack1l1_opy_ (u"ࠪࡴࡦࡺࡨࠨ୿") in app and bstack1l1_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡣ࡮ࡪࠧ஀") in app:
        if os.path.exists(app[bstack1l1_opy_ (u"ࠬࡶࡡࡵࡪࠪ஁")]):
          bstack11l11ll11_opy_ = bstack1l11l11111_opy_(config, app[bstack1l1_opy_ (u"࠭ࡰࡢࡶ࡫ࠫஂ")], app[bstack1l1_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪஃ")])
        else:
          bstack1l11ll1111_opy_(bstack1111l1l1l_opy_.format(app))
      else:
        bstack1l11ll1111_opy_(bstack111llll1l1_opy_)
    else:
      for key in app:
        if key in bstack11l1ll11l_opy_:
          if key == bstack1l1_opy_ (u"ࠨࡲࡤࡸ࡭࠭஄"):
            if os.path.exists(app[key]):
              bstack11l11ll11_opy_ = bstack1l11l11111_opy_(config, app[key])
            else:
              bstack1l11ll1111_opy_(bstack1111l1l1l_opy_.format(app))
          else:
            bstack11l11ll11_opy_ = app[key]
        else:
          bstack1l11ll1111_opy_(bstack1lllllll1_opy_)
  return bstack11l11ll11_opy_
def bstack1l1l11111_opy_(bstack11l11ll11_opy_):
  import re
  bstack11lll11ll1_opy_ = re.compile(bstack1l1_opy_ (u"ࡴࠥࡢࡠࡧ࠭ࡻࡃ࠰࡞࠵࠳࠹࡝ࡡ࠱ࡠ࠲ࡣࠪࠥࠤஅ"))
  bstack1ll1lll11l_opy_ = re.compile(bstack1l1_opy_ (u"ࡵࠦࡣࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫ࠱࡞ࡥ࠲ࢀࡁ࠮࡜࠳࠱࠾ࡢ࡟࠯࡞࠰ࡡ࠯ࠪࠢஆ"))
  if bstack1l1_opy_ (u"ࠫࡧࡹ࠺࠰࠱ࠪஇ") in bstack11l11ll11_opy_ or re.fullmatch(bstack11lll11ll1_opy_, bstack11l11ll11_opy_) or re.fullmatch(bstack1ll1lll11l_opy_, bstack11l11ll11_opy_):
    return True
  else:
    return False
def bstack1l11l11111_opy_(config, path, bstack1l1lll11ll_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack1l1_opy_ (u"ࠬࡸࡢࠨஈ")).read()).hexdigest()
  bstack1llll1lll_opy_ = bstack1ll1ll111l_opy_(md5_hash)
  bstack11l11ll11_opy_ = None
  if bstack1llll1lll_opy_:
    logger.info(bstack1l1l1l111l_opy_.format(bstack1llll1lll_opy_, md5_hash))
    return bstack1llll1lll_opy_
  bstack11l1l1ll11_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࠫஉ"): (os.path.basename(path), open(os.path.abspath(path), bstack1l1_opy_ (u"ࠧࡳࡤࠪஊ")), bstack1l1_opy_ (u"ࠨࡶࡨࡼࡹ࠵ࡰ࡭ࡣ࡬ࡲࠬ஋")),
      bstack1l1_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠬ஌"): bstack1l1lll11ll_opy_
    }
  )
  response = requests.post(bstack11l1l1l1l_opy_, data=multipart_data,
                           headers={bstack1l1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ஍"): multipart_data.content_type},
                           auth=(config[bstack1l1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭எ")], config[bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨஏ")]))
  try:
    res = json.loads(response.text)
    bstack11l11ll11_opy_ = res[bstack1l1_opy_ (u"࠭ࡡࡱࡲࡢࡹࡷࡲࠧஐ")]
    logger.info(bstack1ll111l111_opy_.format(bstack11l11ll11_opy_))
    bstack1111l1lll_opy_(md5_hash, bstack11l11ll11_opy_)
    cli.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠢࡩࡶࡷࡴ࠿ࡻࡰ࡭ࡱࡤࡨࡤࡧࡰࡱࠤ஑"), datetime.datetime.now() - bstack11l1l1ll11_opy_)
  except ValueError as err:
    bstack1l11ll1111_opy_(bstack111l1llll_opy_.format(str(err)))
  return bstack11l11ll11_opy_
def bstack1l111ll111_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1l111llll1_opy_
  bstack11111111_opy_ = 1
  bstack11ll1llll1_opy_ = 1
  if bstack1l1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨஒ") in CONFIG:
    bstack11ll1llll1_opy_ = CONFIG[bstack1l1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩஓ")]
  else:
    bstack11ll1llll1_opy_ = bstack1lllll1111_opy_(framework_name, args) or 1
  if bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ஔ") in CONFIG:
    bstack11111111_opy_ = len(CONFIG[bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧக")])
  bstack1l111llll1_opy_ = int(bstack11ll1llll1_opy_) * int(bstack11111111_opy_)
def bstack1lllll1111_opy_(framework_name, args):
  if framework_name == bstack11l1ll1lll_opy_ and args and bstack1l1_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪ஖") in args:
      bstack11lllll1l_opy_ = args.index(bstack1l1_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫ஗"))
      return int(args[bstack11lllll1l_opy_ + 1]) or 1
  return 1
def bstack1ll1ll111l_opy_(md5_hash):
  bstack1l111l1l1l_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠧࡿࠩ஘")), bstack1l1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨங"), bstack1l1_opy_ (u"ࠩࡤࡴࡵ࡛ࡰ࡭ࡱࡤࡨࡒࡊ࠵ࡉࡣࡶ࡬࠳ࡰࡳࡰࡰࠪச"))
  if os.path.exists(bstack1l111l1l1l_opy_):
    bstack1l1l1llll1_opy_ = json.load(open(bstack1l111l1l1l_opy_, bstack1l1_opy_ (u"ࠪࡶࡧ࠭஛")))
    if md5_hash in bstack1l1l1llll1_opy_:
      bstack1ll111ll1l_opy_ = bstack1l1l1llll1_opy_[md5_hash]
      bstack11l11l111l_opy_ = datetime.datetime.now()
      bstack1l111ll11_opy_ = datetime.datetime.strptime(bstack1ll111ll1l_opy_[bstack1l1_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧஜ")], bstack1l1_opy_ (u"ࠬࠫࡤ࠰ࠧࡰ࠳ࠪ࡟ࠠࠦࡊ࠽ࠩࡒࡀࠥࡔࠩ஝"))
      if (bstack11l11l111l_opy_ - bstack1l111ll11_opy_).days > 30:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack1ll111ll1l_opy_[bstack1l1_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫஞ")]):
        return None
      return bstack1ll111ll1l_opy_[bstack1l1_opy_ (u"ࠧࡪࡦࠪட")]
  else:
    return None
def bstack1111l1lll_opy_(md5_hash, bstack11l11ll11_opy_):
  bstack1l1l111l11_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠨࢀࠪ஠")), bstack1l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ஡"))
  if not os.path.exists(bstack1l1l111l11_opy_):
    os.makedirs(bstack1l1l111l11_opy_)
  bstack1l111l1l1l_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠪࢂࠬ஢")), bstack1l1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫண"), bstack1l1_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭த"))
  bstack11111l1l1_opy_ = {
    bstack1l1_opy_ (u"࠭ࡩࡥࠩ஥"): bstack11l11ll11_opy_,
    bstack1l1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ஦"): datetime.datetime.strftime(datetime.datetime.now(), bstack1l1_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬ஧")),
    bstack1l1_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧந"): str(__version__)
  }
  if os.path.exists(bstack1l111l1l1l_opy_):
    bstack1l1l1llll1_opy_ = json.load(open(bstack1l111l1l1l_opy_, bstack1l1_opy_ (u"ࠪࡶࡧ࠭ன")))
  else:
    bstack1l1l1llll1_opy_ = {}
  bstack1l1l1llll1_opy_[md5_hash] = bstack11111l1l1_opy_
  with open(bstack1l111l1l1l_opy_, bstack1l1_opy_ (u"ࠦࡼ࠱ࠢப")) as outfile:
    json.dump(bstack1l1l1llll1_opy_, outfile)
def bstack1lll1111l1_opy_(self):
  return
def bstack1ll11l1l11_opy_(self):
  return
def bstack1111llll1_opy_(self):
  global bstack1l111111l_opy_
  bstack1l111111l_opy_(self)
def bstack1llllllll1_opy_():
  global bstack111ll1lll_opy_
  bstack111ll1lll_opy_ = True
def bstack1l1l11ll1l_opy_(self):
  global bstack11lll1l1ll_opy_
  global bstack1ll1l1111_opy_
  global bstack1lll1ll1ll_opy_
  try:
    if bstack1l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ஫") in bstack11lll1l1ll_opy_ and self.session_id != None and bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࡗࡹࡧࡴࡶࡵࠪ஬"), bstack1l1_opy_ (u"ࠧࠨ஭")) != bstack1l1_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩம"):
      bstack1lll1l1l1l_opy_ = bstack1l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩய") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪர")
      if bstack1lll1l1l1l_opy_ == bstack1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫற"):
        bstack1l111l111_opy_(logger)
      if self != None:
        bstack1l1lll1lll_opy_(self, bstack1lll1l1l1l_opy_, bstack1l1_opy_ (u"ࠬ࠲ࠠࠨல").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack1l1_opy_ (u"࠭ࠧள")
    if bstack1l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧழ") in bstack11lll1l1ll_opy_ and getattr(threading.current_thread(), bstack1l1_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧவ"), None):
      bstack11l11111_opy_.bstack111l1111_opy_(self, bstack1ll111111_opy_, logger, wait=True)
    if bstack1l1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩஶ") in bstack11lll1l1ll_opy_:
      if not threading.currentThread().behave_test_status:
        bstack1l1lll1lll_opy_(self, bstack1l1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥஷ"))
      bstack1l1111l11l_opy_.bstack11lll1l111_opy_(self)
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࠧஸ") + str(e))
  bstack1lll1ll1ll_opy_(self)
  self.session_id = None
def bstack1l11llll1l_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack1l11llll1_opy_
    global bstack11lll1l1ll_opy_
    command_executor = kwargs.get(bstack1l1_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠨஹ"), bstack1l1_opy_ (u"࠭ࠧ஺"))
    bstack11ll111111_opy_ = False
    if type(command_executor) == str and bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪ஻") in command_executor:
      bstack11ll111111_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫ஼") in str(getattr(command_executor, bstack1l1_opy_ (u"ࠩࡢࡹࡷࡲࠧ஽"), bstack1l1_opy_ (u"ࠪࠫா"))):
      bstack11ll111111_opy_ = True
    else:
      return bstack1l111111ll_opy_(self, *args, **kwargs)
    if bstack11ll111111_opy_:
      bstack1l11lll11_opy_ = bstack11l1111111_opy_.bstack11l1l11ll_opy_(CONFIG, bstack11lll1l1ll_opy_)
      if kwargs.get(bstack1l1_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬி")):
        kwargs[bstack1l1_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭ீ")] = bstack1l11llll1_opy_(kwargs[bstack1l1_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧு")], bstack11lll1l1ll_opy_, bstack1l11lll11_opy_)
      elif kwargs.get(bstack1l1_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧூ")):
        kwargs[bstack1l1_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ௃")] = bstack1l11llll1_opy_(kwargs[bstack1l1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ௄")], bstack11lll1l1ll_opy_, bstack1l11lll11_opy_)
  except Exception as e:
    logger.error(bstack1l1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬ࡪࡴࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡘࡊࡋࠡࡥࡤࡴࡸࡀࠠࡼࡿࠥ௅").format(str(e)))
  return bstack1l111111ll_opy_(self, *args, **kwargs)
def bstack11l1l1lll_opy_(self, command_executor=bstack1l1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳࠶࠸࠷࠯࠲࠱࠴࠳࠷࠺࠵࠶࠷࠸ࠧெ"), *args, **kwargs):
  bstack111111111_opy_ = bstack1l11llll1l_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1llll1l1_opy_.on():
    return bstack111111111_opy_
  try:
    logger.debug(bstack1l1_opy_ (u"ࠬࡉ࡯࡮࡯ࡤࡲࡩࠦࡅࡹࡧࡦࡹࡹࡵࡲࠡࡹ࡫ࡩࡳࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢ࡬ࡷࠥ࡬ࡡ࡭ࡵࡨࠤ࠲ࠦࡻࡾࠩே").format(str(command_executor)))
    logger.debug(bstack1l1_opy_ (u"࠭ࡈࡶࡤ࡙ࠣࡗࡒࠠࡪࡵࠣ࠱ࠥࢁࡽࠨை").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪ௉") in command_executor._url:
      bstack111l11ll_opy_.set_property(bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩொ"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬோ") in command_executor):
    bstack111l11ll_opy_.set_property(bstack1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫௌ"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack11lllll11_opy_ = getattr(threading.current_thread(), bstack1l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡘࡪࡹࡴࡎࡧࡷࡥ்ࠬ"), None)
  if bstack1l1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ௎") in bstack11lll1l1ll_opy_ or bstack1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ௏") in bstack11lll1l1ll_opy_:
    bstack1l1ll1l1_opy_.bstack1ll1l111l_opy_(self)
  if bstack1l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧௐ") in bstack11lll1l1ll_opy_ and bstack11lllll11_opy_ and bstack11lllll11_opy_.get(bstack1l1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ௑"), bstack1l1_opy_ (u"ࠩࠪ௒")) == bstack1l1_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫ௓"):
    bstack1l1ll1l1_opy_.bstack1ll1l111l_opy_(self)
  return bstack111111111_opy_
def bstack1ll1l11l1_opy_(args):
  return bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠬ௔") in str(args)
def bstack1l11l1l11l_opy_(self, driver_command, *args, **kwargs):
  global bstack11l11l1lll_opy_
  global bstack1l1111lll_opy_
  bstack11l11ll111_opy_ = bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ௕"), None) and bstack1l1111ll_opy_(
          threading.current_thread(), bstack1l1_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ௖"), None)
  bstack1l111l111l_opy_ = getattr(self, bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧௗ"), None) != None and getattr(self, bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨ௘"), None) == True
  if not bstack1l1111lll_opy_ and bstack1ll11ll1ll_opy_ and bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ௙") in CONFIG and CONFIG[bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ௚")] == True and bstack11ll111lll_opy_.bstack1lll11l1l1_opy_(driver_command) and (bstack1l111l111l_opy_ or bstack11l11ll111_opy_) and not bstack1ll1l11l1_opy_(args):
    try:
      bstack1l1111lll_opy_ = True
      logger.debug(bstack1l1_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡦࡰࡴࠣࡿࢂ࠭௛").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack1l1_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡨࡶ࡫ࡵࡲ࡮ࠢࡶࡧࡦࡴࠠࡼࡿࠪ௜").format(str(err)))
    bstack1l1111lll_opy_ = False
  response = bstack11l11l1lll_opy_(self, driver_command, *args, **kwargs)
  if (bstack1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ௝") in str(bstack11lll1l1ll_opy_).lower() or bstack1l1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ௞") in str(bstack11lll1l1ll_opy_).lower()) and bstack1llll1l1_opy_.on():
    try:
      if driver_command == bstack1l1_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬ௟"):
        bstack1l1ll1l1_opy_.bstack1l1ll1l11_opy_({
            bstack1l1_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨ௠"): response[bstack1l1_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩ௡")],
            bstack1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ௢"): bstack1l1ll1l1_opy_.current_test_uuid() if bstack1l1ll1l1_opy_.current_test_uuid() else bstack1llll1l1_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
def bstack1ll111ll11_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack1ll1l1111_opy_
  global bstack1llll11111_opy_
  global bstack1l1lll111l_opy_
  global bstack1ll11llll_opy_
  global bstack1l11ll111l_opy_
  global bstack11lll1l1ll_opy_
  global bstack1l111111ll_opy_
  global bstack1l1ll1ll1l_opy_
  global bstack1ll11l1l1l_opy_
  global bstack1ll111111_opy_
  CONFIG[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ௣")] = str(bstack11lll1l1ll_opy_) + str(__version__)
  bstack1ll11lll11_opy_ = os.environ[bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ௤")]
  bstack1l11lll11_opy_ = bstack11l1111111_opy_.bstack11l1l11ll_opy_(CONFIG, bstack11lll1l1ll_opy_)
  CONFIG[bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪ௥")] = bstack1ll11lll11_opy_
  CONFIG[bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪ௦")] = bstack1l11lll11_opy_
  command_executor = bstack1ll1ll11l1_opy_()
  logger.debug(bstack1lll1ll1l_opy_.format(command_executor))
  proxy = bstack1l11l11l1l_opy_(CONFIG, proxy)
  bstack11l111l1ll_opy_ = 0 if bstack1llll11111_opy_ < 0 else bstack1llll11111_opy_
  try:
    if bstack1ll11llll_opy_ is True:
      bstack11l111l1ll_opy_ = int(multiprocessing.current_process().name)
    elif bstack1l11ll111l_opy_ is True:
      bstack11l111l1ll_opy_ = int(threading.current_thread().name)
  except:
    bstack11l111l1ll_opy_ = 0
  bstack1llll1l111_opy_ = bstack11lll1ll1l_opy_(CONFIG, bstack11l111l1ll_opy_)
  logger.debug(bstack11lll1ll11_opy_.format(str(bstack1llll1l111_opy_)))
  if bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭௧") in CONFIG and bstack1ll11l11l_opy_(CONFIG[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ௨")]):
    bstack1l1l1l1lll_opy_(bstack1llll1l111_opy_)
  if bstack111l1ll1_opy_.bstack1llll1llll_opy_(CONFIG, bstack11l111l1ll_opy_) and bstack111l1ll1_opy_.bstack1ll1111ll_opy_(bstack1llll1l111_opy_, options, desired_capabilities):
    threading.current_thread().a11yPlatform = True
    if not cli.accessibility.is_enabled():
      bstack111l1ll1_opy_.set_capabilities(bstack1llll1l111_opy_, CONFIG)
  if desired_capabilities:
    bstack11l111l11_opy_ = bstack1l1l1111l_opy_(desired_capabilities)
    bstack11l111l11_opy_[bstack1l1_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫ௩")] = bstack11llllll11_opy_(CONFIG)
    bstack1ll11l11ll_opy_ = bstack11lll1ll1l_opy_(bstack11l111l11_opy_)
    if bstack1ll11l11ll_opy_:
      bstack1llll1l111_opy_ = update(bstack1ll11l11ll_opy_, bstack1llll1l111_opy_)
    desired_capabilities = None
  if options:
    bstack1l11lllll_opy_(options, bstack1llll1l111_opy_)
  if not options:
    options = bstack1ll1ll111_opy_(bstack1llll1l111_opy_)
  bstack1ll111111_opy_ = CONFIG.get(bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ௪"))[bstack11l111l1ll_opy_]
  if proxy and bstack1lll1lll11_opy_() >= version.parse(bstack1l1_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭௫")):
    options.proxy(proxy)
  if options and bstack1lll1lll11_opy_() >= version.parse(bstack1l1_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭௬")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1lll1lll11_opy_() < version.parse(bstack1l1_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧ௭")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1llll1l111_opy_)
  logger.info(bstack1ll11lll1_opy_)
  if bstack1lll1lll11_opy_() >= version.parse(bstack1l1_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩ௮")):
    bstack1l111111ll_opy_(self, command_executor=command_executor,
              options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
  elif bstack1lll1lll11_opy_() >= version.parse(bstack1l1_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩ௯")):
    bstack1l111111ll_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities, options=options,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1lll1lll11_opy_() >= version.parse(bstack1l1_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫ௰")):
    bstack1l111111ll_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  else:
    bstack1l111111ll_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive)
  try:
    bstack1l11ll111_opy_ = bstack1l1_opy_ (u"ࠬ࠭௱")
    if bstack1lll1lll11_opy_() >= version.parse(bstack1l1_opy_ (u"࠭࠴࠯࠲࠱࠴ࡧ࠷ࠧ௲")):
      bstack1l11ll111_opy_ = self.caps.get(bstack1l1_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢ௳"))
    else:
      bstack1l11ll111_opy_ = self.capabilities.get(bstack1l1_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣ௴"))
    if bstack1l11ll111_opy_:
      bstack1l1l111111_opy_(bstack1l11ll111_opy_)
      if bstack1lll1lll11_opy_() <= version.parse(bstack1l1_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩ௵")):
        self.command_executor._url = bstack1l1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦ௶") + bstack11ll1ll111_opy_ + bstack1l1_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣ௷")
      else:
        self.command_executor._url = bstack1l1_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢ௸") + bstack1l11ll111_opy_ + bstack1l1_opy_ (u"ࠨ࠯ࡸࡦ࠲࡬ࡺࡨࠢ௹")
      logger.debug(bstack1ll1l1lll_opy_.format(bstack1l11ll111_opy_))
    else:
      logger.debug(bstack1llll111l_opy_.format(bstack1l1_opy_ (u"ࠢࡐࡲࡷ࡭ࡲࡧ࡬ࠡࡊࡸࡦࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤࠣ௺")))
  except Exception as e:
    logger.debug(bstack1llll111l_opy_.format(e))
  if bstack1l1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ௻") in bstack11lll1l1ll_opy_:
    bstack11lll1llll_opy_(bstack1llll11111_opy_, bstack1ll11l1l1l_opy_)
  bstack1ll1l1111_opy_ = self.session_id
  if bstack1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ௼") in bstack11lll1l1ll_opy_ or bstack1l1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ௽") in bstack11lll1l1ll_opy_ or bstack1l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ௾") in bstack11lll1l1ll_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack11lllll11_opy_ = getattr(threading.current_thread(), bstack1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࡙࡫ࡳࡵࡏࡨࡸࡦ࠭௿"), None)
  if bstack1l1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ఀ") in bstack11lll1l1ll_opy_ or bstack1l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ఁ") in bstack11lll1l1ll_opy_:
    bstack1l1ll1l1_opy_.bstack1ll1l111l_opy_(self)
  if bstack1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨం") in bstack11lll1l1ll_opy_ and bstack11lllll11_opy_ and bstack11lllll11_opy_.get(bstack1l1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩః"), bstack1l1_opy_ (u"ࠪࠫఄ")) == bstack1l1_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬఅ"):
    bstack1l1ll1l1_opy_.bstack1ll1l111l_opy_(self)
  bstack1l1ll1ll1l_opy_.append(self)
  if bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨఆ") in CONFIG and bstack1l1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫఇ") in CONFIG[bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪఈ")][bstack11l111l1ll_opy_]:
    bstack1l1lll111l_opy_ = CONFIG[bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫఉ")][bstack11l111l1ll_opy_][bstack1l1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧఊ")]
  logger.debug(bstack1l1llll111_opy_.format(bstack1ll1l1111_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack11ll1ll1l_opy_
    def bstack1ll1ll1111_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1lll11111_opy_
      if(bstack1l1_opy_ (u"ࠥ࡭ࡳࡪࡥࡹ࠰࡭ࡷࠧఋ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠫࢃ࠭ఌ")), bstack1l1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ఍"), bstack1l1_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨఎ")), bstack1l1_opy_ (u"ࠧࡸࠩఏ")) as fp:
          fp.write(bstack1l1_opy_ (u"ࠣࠤఐ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack1l1_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦ఑")))):
          with open(args[1], bstack1l1_opy_ (u"ࠪࡶࠬఒ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack1l1_opy_ (u"ࠫࡦࡹࡹ࡯ࡥࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࡥ࡮ࡦࡹࡓࡥ࡬࡫ࠨࡤࡱࡱࡸࡪࡾࡴ࠭ࠢࡳࡥ࡬࡫ࠠ࠾ࠢࡹࡳ࡮ࡪࠠ࠱ࠫࠪఓ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1l1l1l1111_opy_)
            if bstack1l1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩఔ") in CONFIG and str(CONFIG[bstack1l1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪక")]).lower() != bstack1l1_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ఖ"):
                bstack1ll1ll1l1_opy_ = bstack11ll1ll1l_opy_()
                bstack11l1lllll_opy_ = bstack1l1_opy_ (u"ࠨࠩࠪࠎ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵ࠊࡤࡱࡱࡷࡹࠦࡢࡴࡶࡤࡧࡰࡥࡰࡢࡶ࡫ࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳࡞࠽ࠍࡧࡴࡴࡳࡵࠢࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠴ࡡࡀࠐࡣࡰࡰࡶࡸࠥࡶ࡟ࡪࡰࡧࡩࡽࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠴ࡠ࠿ࠏࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡹ࡬ࡪࡥࡨࠬ࠵࠲ࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠵ࠬ࠿ࠏࡩ࡯࡯ࡵࡷࠤ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬ࠢࡀࠤࡷ࡫ࡱࡶ࡫ࡵࡩ࠭ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ࠭ࡀࠐࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴࡬ࡢࡷࡱࡧ࡭ࠦ࠽ࠡࡣࡶࡽࡳࡩࠠࠩ࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳࠪࠢࡀࡂࠥࢁࡻࠋࠢࠣࡰࡪࡺࠠࡤࡣࡳࡷࡀࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࡴࡳࡻࠣࡿࢀࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࡦࡥࡵࡹࠠ࠾ࠢࡍࡗࡔࡔ࠮ࡱࡣࡵࡷࡪ࠮ࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶ࠭ࡀࠐࠠࠡࡿࢀࠤࡨࡧࡴࡤࡪࠣࠬࡪࡾࠩࠡࡽࡾࠎࠥࠦࠠࠡࡥࡲࡲࡸࡵ࡬ࡦ࠰ࡨࡶࡷࡵࡲࠩࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ࠽ࠦ࠱ࠦࡥࡹࠫ࠾ࠎࠥࠦࡽࡾࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࡶࡪࡺࡵࡳࡰࠣࡥࡼࡧࡩࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰ࡦࡳࡳࡴࡥࡤࡶࠫࡿࢀࠐࠠࠡࠢࠣࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺ࠺ࠡࠩࡾࡧࡩࡶࡕࡳ࡮ࢀࠫࠥ࠱ࠠࡦࡰࡦࡳࡩ࡫ࡕࡓࡋࡆࡳࡲࡶ࡯࡯ࡧࡱࡸ࠭ࡐࡓࡐࡐ࠱ࡷࡹࡸࡩ࡯ࡩ࡬ࡪࡾ࠮ࡣࡢࡲࡶ࠭࠮࠲ࠊࠡࠢࠣࠤ࠳࠴࠮࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹࠊࠡࠢࢀࢁ࠮ࡁࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠎࢂࢃ࠻ࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠎ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵ࠊࠨࠩࠪగ").format(bstack1ll1ll1l1_opy_=bstack1ll1ll1l1_opy_)
            lines.insert(1, bstack11l1lllll_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack1l1_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦఘ")), bstack1l1_opy_ (u"ࠪࡻࠬఙ")) as bstack1l1l1ll1l_opy_:
              bstack1l1l1ll1l_opy_.writelines(lines)
        CONFIG[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭చ")] = str(bstack11lll1l1ll_opy_) + str(__version__)
        bstack1ll11lll11_opy_ = os.environ[bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪఛ")]
        bstack1l11lll11_opy_ = bstack11l1111111_opy_.bstack11l1l11ll_opy_(CONFIG, bstack11lll1l1ll_opy_)
        CONFIG[bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩజ")] = bstack1ll11lll11_opy_
        CONFIG[bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩఝ")] = bstack1l11lll11_opy_
        bstack11l111l1ll_opy_ = 0 if bstack1llll11111_opy_ < 0 else bstack1llll11111_opy_
        try:
          if bstack1ll11llll_opy_ is True:
            bstack11l111l1ll_opy_ = int(multiprocessing.current_process().name)
          elif bstack1l11ll111l_opy_ is True:
            bstack11l111l1ll_opy_ = int(threading.current_thread().name)
        except:
          bstack11l111l1ll_opy_ = 0
        CONFIG[bstack1l1_opy_ (u"ࠣࡷࡶࡩ࡜࠹ࡃࠣఞ")] = False
        CONFIG[bstack1l1_opy_ (u"ࠤ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣట")] = True
        bstack1llll1l111_opy_ = bstack11lll1ll1l_opy_(CONFIG, bstack11l111l1ll_opy_)
        logger.debug(bstack11lll1ll11_opy_.format(str(bstack1llll1l111_opy_)))
        if CONFIG.get(bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧఠ")):
          bstack1l1l1l1lll_opy_(bstack1llll1l111_opy_)
        if bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧడ") in CONFIG and bstack1l1_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪఢ") in CONFIG[bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩణ")][bstack11l111l1ll_opy_]:
          bstack1l1lll111l_opy_ = CONFIG[bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪత")][bstack11l111l1ll_opy_][bstack1l1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭థ")]
        args.append(os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠩࢁࠫద")), bstack1l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪధ"), bstack1l1_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭న")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1llll1l111_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack1l1_opy_ (u"ࠧ࡯࡮ࡥࡧࡻࡣࡧࡹࡴࡢࡥ࡮࠲࡯ࡹࠢ఩"))
      bstack1lll11111_opy_ = True
      return bstack1111l11ll_opy_(self, args, bufsize=bufsize, executable=executable,
                    stdin=stdin, stdout=stdout, stderr=stderr,
                    preexec_fn=preexec_fn, close_fds=close_fds,
                    shell=shell, cwd=cwd, env=env, universal_newlines=universal_newlines,
                    startupinfo=startupinfo, creationflags=creationflags,
                    restore_signals=restore_signals, start_new_session=start_new_session,
                    pass_fds=pass_fds, user=user, group=group, extra_groups=extra_groups,
                    encoding=encoding, errors=errors, text=text, umask=umask, pipesize=pipesize)
  except Exception as e:
    pass
  import playwright._impl._api_structures
  import playwright._impl._helper
  def bstack1l1lll1ll_opy_(self,
        executablePath = None,
        channel = None,
        args = None,
        ignoreDefaultArgs = None,
        handleSIGINT = None,
        handleSIGTERM = None,
        handleSIGHUP = None,
        timeout = None,
        env = None,
        headless = None,
        devtools = None,
        proxy = None,
        downloadsPath = None,
        slowMo = None,
        tracesDir = None,
        chromiumSandbox = None,
        firefoxUserPrefs = None
        ):
    global CONFIG
    global bstack1llll11111_opy_
    global bstack1l1lll111l_opy_
    global bstack1ll11llll_opy_
    global bstack1l11ll111l_opy_
    global bstack11lll1l1ll_opy_
    CONFIG[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨప")] = str(bstack11lll1l1ll_opy_) + str(__version__)
    bstack1ll11lll11_opy_ = os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬఫ")]
    bstack1l11lll11_opy_ = bstack11l1111111_opy_.bstack11l1l11ll_opy_(CONFIG, bstack11lll1l1ll_opy_)
    CONFIG[bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫబ")] = bstack1ll11lll11_opy_
    CONFIG[bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫభ")] = bstack1l11lll11_opy_
    bstack11l111l1ll_opy_ = 0 if bstack1llll11111_opy_ < 0 else bstack1llll11111_opy_
    try:
      if bstack1ll11llll_opy_ is True:
        bstack11l111l1ll_opy_ = int(multiprocessing.current_process().name)
      elif bstack1l11ll111l_opy_ is True:
        bstack11l111l1ll_opy_ = int(threading.current_thread().name)
    except:
      bstack11l111l1ll_opy_ = 0
    CONFIG[bstack1l1_opy_ (u"ࠥ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤమ")] = True
    bstack1llll1l111_opy_ = bstack11lll1ll1l_opy_(CONFIG, bstack11l111l1ll_opy_)
    logger.debug(bstack11lll1ll11_opy_.format(str(bstack1llll1l111_opy_)))
    if CONFIG.get(bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨయ")):
      bstack1l1l1l1lll_opy_(bstack1llll1l111_opy_)
    if bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨర") in CONFIG and bstack1l1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫఱ") in CONFIG[bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪల")][bstack11l111l1ll_opy_]:
      bstack1l1lll111l_opy_ = CONFIG[bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫళ")][bstack11l111l1ll_opy_][bstack1l1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧఴ")]
    import urllib
    import json
    if bstack1l1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧవ") in CONFIG and str(CONFIG[bstack1l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨశ")]).lower() != bstack1l1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫష"):
        bstack1lll11lll1_opy_ = bstack11ll1ll1l_opy_()
        bstack1ll1ll1l1_opy_ = bstack1lll11lll1_opy_ + urllib.parse.quote(json.dumps(bstack1llll1l111_opy_))
    else:
        bstack1ll1ll1l1_opy_ = bstack1l1_opy_ (u"࠭ࡷࡴࡵ࠽࠳࠴ࡩࡤࡱ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡁࡦࡥࡵࡹ࠽ࠨస") + urllib.parse.quote(json.dumps(bstack1llll1l111_opy_))
    browser = self.connect(bstack1ll1ll1l1_opy_)
    return browser
except Exception as e:
    pass
def bstack11l1lll1l1_opy_():
    global bstack1lll11111_opy_
    global bstack11lll1l1ll_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1l11llll11_opy_
        global bstack111l11ll_opy_
        if not bstack1ll11ll1ll_opy_:
          global bstack1l1l1111ll_opy_
          if not bstack1l1l1111ll_opy_:
            from bstack_utils.helper import bstack1l1l111ll_opy_, bstack11l1111ll1_opy_, bstack1llllll1l1_opy_
            bstack1l1l1111ll_opy_ = bstack1l1l111ll_opy_()
            bstack11l1111ll1_opy_(bstack11lll1l1ll_opy_)
            bstack1l11lll11_opy_ = bstack11l1111111_opy_.bstack11l1l11ll_opy_(CONFIG, bstack11lll1l1ll_opy_)
            bstack111l11ll_opy_.set_property(bstack1l1_opy_ (u"ࠢࡑࡎࡄ࡝࡜ࡘࡉࡈࡊࡗࡣࡕࡘࡏࡅࡗࡆࡘࡤࡓࡁࡑࠤహ"), bstack1l11lll11_opy_)
          BrowserType.connect = bstack1l11llll11_opy_
          return
        BrowserType.launch = bstack1l1lll1ll_opy_
        bstack1lll11111_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1ll1ll1111_opy_
      bstack1lll11111_opy_ = True
    except Exception as e:
      pass
def bstack11l1l1l111_opy_(context, bstack1llll1lll1_opy_):
  try:
    context.page.evaluate(bstack1l1_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ఺"), bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿࠭఻")+ json.dumps(bstack1llll1lll1_opy_) + bstack1l1_opy_ (u"ࠥࢁࢂࠨ఼"))
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡻࡾࠤఽ"), e)
def bstack11l11l1l11_opy_(context, message, level):
  try:
    context.page.evaluate(bstack1l1_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨా"), bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫి") + json.dumps(message) + bstack1l1_opy_ (u"ࠧ࠭ࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠪీ") + json.dumps(level) + bstack1l1_opy_ (u"ࠨࡿࢀࠫు"))
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡧ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠢࡾࢁࠧూ"), e)
def bstack1lll1lll1_opy_(self, url):
  global bstack1ll111l11l_opy_
  try:
    bstack1l1l1l1l1l_opy_(url)
  except Exception as err:
    logger.debug(bstack1l11ll1ll_opy_.format(str(err)))
  try:
    bstack1ll111l11l_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack1l1l11ll11_opy_):
        bstack1l1l1l1l1l_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1l11ll1ll_opy_.format(str(err)))
    raise e
def bstack111l1111l_opy_(self):
  global bstack11ll11l111_opy_
  bstack11ll11l111_opy_ = self
  return
def bstack1l1ll111l1_opy_(self):
  global bstack11lll1l1l1_opy_
  bstack11lll1l1l1_opy_ = self
  return
def bstack11ll11111l_opy_(test_name, bstack11ll1ll11_opy_):
  global CONFIG
  if percy.bstack1l11lll111_opy_() == bstack1l1_opy_ (u"ࠥࡸࡷࡻࡥࠣృ"):
    bstack111llllll_opy_ = os.path.relpath(bstack11ll1ll11_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack111llllll_opy_)
    bstack1l1ll1l1ll_opy_ = suite_name + bstack1l1_opy_ (u"ࠦ࠲ࠨౄ") + test_name
    threading.current_thread().percySessionName = bstack1l1ll1l1ll_opy_
def bstack1l1ll11l11_opy_(self, test, *args, **kwargs):
  global bstack1l11l1111l_opy_
  test_name = None
  bstack11ll1ll11_opy_ = None
  if test:
    test_name = str(test.name)
    bstack11ll1ll11_opy_ = str(test.source)
  bstack11ll11111l_opy_(test_name, bstack11ll1ll11_opy_)
  bstack1l11l1111l_opy_(self, test, *args, **kwargs)
def bstack1111l1l11_opy_(driver, bstack1l1ll1l1ll_opy_):
  if not bstack1ll11l11l1_opy_ and bstack1l1ll1l1ll_opy_:
      bstack11l1ll11l1_opy_ = {
          bstack1l1_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬ౅"): bstack1l1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧె"),
          bstack1l1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪే"): {
              bstack1l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ై"): bstack1l1ll1l1ll_opy_
          }
      }
      bstack11ll1ll1ll_opy_ = bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧ౉").format(json.dumps(bstack11l1ll11l1_opy_))
      driver.execute_script(bstack11ll1ll1ll_opy_)
  if bstack1111l11l1_opy_:
      bstack1ll1ll1l11_opy_ = {
          bstack1l1_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪొ"): bstack1l1_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ో"),
          bstack1l1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨౌ"): {
              bstack1l1_opy_ (u"࠭ࡤࡢࡶࡤ్ࠫ"): bstack1l1ll1l1ll_opy_ + bstack1l1_opy_ (u"ࠧࠡࡲࡤࡷࡸ࡫ࡤࠢࠩ౎"),
              bstack1l1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ౏"): bstack1l1_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧ౐")
          }
      }
      if bstack1111l11l1_opy_.status == bstack1l1_opy_ (u"ࠪࡔࡆ࡙ࡓࠨ౑"):
          bstack11l11lll1_opy_ = bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩ౒").format(json.dumps(bstack1ll1ll1l11_opy_))
          driver.execute_script(bstack11l11lll1_opy_)
          bstack1l1lll1lll_opy_(driver, bstack1l1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ౓"))
      elif bstack1111l11l1_opy_.status == bstack1l1_opy_ (u"࠭ࡆࡂࡋࡏࠫ౔"):
          reason = bstack1l1_opy_ (u"ౕࠢࠣ")
          bstack1ll1ll1lll_opy_ = bstack1l1ll1l1ll_opy_ + bstack1l1_opy_ (u"ࠨࠢࡩࡥ࡮ࡲࡥࡥౖࠩ")
          if bstack1111l11l1_opy_.message:
              reason = str(bstack1111l11l1_opy_.message)
              bstack1ll1ll1lll_opy_ = bstack1ll1ll1lll_opy_ + bstack1l1_opy_ (u"ࠩࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸ࠺ࠡࠩ౗") + reason
          bstack1ll1ll1l11_opy_[bstack1l1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ౘ")] = {
              bstack1l1_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪౙ"): bstack1l1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫౚ"),
              bstack1l1_opy_ (u"࠭ࡤࡢࡶࡤࠫ౛"): bstack1ll1ll1lll_opy_
          }
          bstack11l11lll1_opy_ = bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬ౜").format(json.dumps(bstack1ll1ll1l11_opy_))
          driver.execute_script(bstack11l11lll1_opy_)
          bstack1l1lll1lll_opy_(driver, bstack1l1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨౝ"), reason)
          bstack1ll1111111_opy_(reason, str(bstack1111l11l1_opy_), str(bstack1llll11111_opy_), logger)
def bstack11l1l1ll1_opy_(driver, test):
  if percy.bstack1l11lll111_opy_() == bstack1l1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ౞") and percy.bstack1lll11l11_opy_() == bstack1l1_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧ౟"):
      bstack111l111l1_opy_ = bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧౠ"), None)
      bstack11l1111l11_opy_(driver, bstack111l111l1_opy_, test)
  if bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩౡ"), None) and bstack1l1111ll_opy_(
          threading.current_thread(), bstack1l1_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬౢ"), None):
      logger.info(bstack1l1_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠥࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡹࡳࡪࡥࡳࡹࡤࡽ࠳ࠦࠢౣ"))
      bstack111l1ll1_opy_.bstack11l11l11_opy_(driver, name=test.name, path=test.source)
def bstack111l11ll1_opy_(test, bstack1l1ll1l1ll_opy_):
    try:
      bstack11l1l1ll11_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack1l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭౤")] = bstack1l1ll1l1ll_opy_
      if bstack1111l11l1_opy_:
        if bstack1111l11l1_opy_.status == bstack1l1_opy_ (u"ࠩࡓࡅࡘ࡙ࠧ౥"):
          data[bstack1l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ౦")] = bstack1l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ౧")
        elif bstack1111l11l1_opy_.status == bstack1l1_opy_ (u"ࠬࡌࡁࡊࡎࠪ౨"):
          data[bstack1l1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭౩")] = bstack1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ౪")
          if bstack1111l11l1_opy_.message:
            data[bstack1l1_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨ౫")] = str(bstack1111l11l1_opy_.message)
      user = CONFIG[bstack1l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ౬")]
      key = CONFIG[bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭౭")]
      url = bstack1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࢁࡽ࠻ࡽࢀࡄࡦࡶࡩ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡳࡦࡵࡶ࡭ࡴࡴࡳ࠰ࡽࢀ࠲࡯ࡹ࡯࡯ࠩ౮").format(user, key, bstack1ll1l1111_opy_)
      headers = {
        bstack1l1_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫ౯"): bstack1l1_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ౰"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
        cli.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠢࡩࡶࡷࡴ࠿ࡻࡰࡥࡣࡷࡩࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡸࡺࡡࡵࡷࡶࠦ౱"), datetime.datetime.now() - bstack11l1l1ll11_opy_)
    except Exception as e:
      logger.error(bstack1l111l1l11_opy_.format(str(e)))
def bstack11l1l11l1_opy_(test, bstack1l1ll1l1ll_opy_):
  global CONFIG
  global bstack11lll1l1l1_opy_
  global bstack11ll11l111_opy_
  global bstack1ll1l1111_opy_
  global bstack1111l11l1_opy_
  global bstack1l1lll111l_opy_
  global bstack11ll11l11_opy_
  global bstack11ll1l1l1l_opy_
  global bstack1lll1l11l_opy_
  global bstack1l11l1111_opy_
  global bstack1l1ll1ll1l_opy_
  global bstack1ll111111_opy_
  try:
    if not bstack1ll1l1111_opy_:
      with open(os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠨࢀࠪ౲")), bstack1l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ౳"), bstack1l1_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬ౴"))) as f:
        bstack11lll1l11_opy_ = json.loads(bstack1l1_opy_ (u"ࠦࢀࠨ౵") + f.read().strip() + bstack1l1_opy_ (u"ࠬࠨࡸࠣ࠼ࠣࠦࡾࠨࠧ౶") + bstack1l1_opy_ (u"ࠨࡽࠣ౷"))
        bstack1ll1l1111_opy_ = bstack11lll1l11_opy_[str(threading.get_ident())]
  except:
    pass
  if bstack1l1ll1ll1l_opy_:
    for driver in bstack1l1ll1ll1l_opy_:
      if bstack1ll1l1111_opy_ == driver.session_id:
        if test:
          bstack11l1l1ll1_opy_(driver, test)
        bstack1111l1l11_opy_(driver, bstack1l1ll1l1ll_opy_)
  elif bstack1ll1l1111_opy_:
    bstack111l11ll1_opy_(test, bstack1l1ll1l1ll_opy_)
  if bstack11lll1l1l1_opy_:
    bstack11ll1l1l1l_opy_(bstack11lll1l1l1_opy_)
  if bstack11ll11l111_opy_:
    bstack1lll1l11l_opy_(bstack11ll11l111_opy_)
  if bstack111ll1lll_opy_:
    bstack1l11l1111_opy_()
def bstack1ll1llllll_opy_(self, test, *args, **kwargs):
  bstack1l1ll1l1ll_opy_ = None
  if test:
    bstack1l1ll1l1ll_opy_ = str(test.name)
  bstack11l1l11l1_opy_(test, bstack1l1ll1l1ll_opy_)
  bstack11ll11l11_opy_(self, test, *args, **kwargs)
def bstack11l1ll111_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack11lllllll1_opy_
  global CONFIG
  global bstack1l1ll1ll1l_opy_
  global bstack1ll1l1111_opy_
  bstack11l1llllll_opy_ = None
  try:
    if bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭౸"), None):
      try:
        if not bstack1ll1l1111_opy_:
          with open(os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠨࢀࠪ౹")), bstack1l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ౺"), bstack1l1_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬ౻"))) as f:
            bstack11lll1l11_opy_ = json.loads(bstack1l1_opy_ (u"ࠦࢀࠨ౼") + f.read().strip() + bstack1l1_opy_ (u"ࠬࠨࡸࠣ࠼ࠣࠦࡾࠨࠧ౽") + bstack1l1_opy_ (u"ࠨࡽࠣ౾"))
            bstack1ll1l1111_opy_ = bstack11lll1l11_opy_[str(threading.get_ident())]
      except:
        pass
      if bstack1l1ll1ll1l_opy_:
        for driver in bstack1l1ll1ll1l_opy_:
          if bstack1ll1l1111_opy_ == driver.session_id:
            bstack11l1llllll_opy_ = driver
    bstack11l111llll_opy_ = bstack111l1ll1_opy_.bstack11l1lll1l_opy_(test.tags)
    if bstack11l1llllll_opy_:
      threading.current_thread().isA11yTest = bstack111l1ll1_opy_.bstack111l1l111_opy_(bstack11l1llllll_opy_, bstack11l111llll_opy_)
    else:
      threading.current_thread().isA11yTest = bstack11l111llll_opy_
  except:
    pass
  bstack11lllllll1_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1111l11l1_opy_
  bstack1111l11l1_opy_ = self._test
def bstack11l1llll1l_opy_():
  global bstack111llll1ll_opy_
  try:
    if os.path.exists(bstack111llll1ll_opy_):
      os.remove(bstack111llll1ll_opy_)
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡧࡩࡱ࡫ࡴࡪࡰࡪࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪ౿") + str(e))
def bstack1lll111l1l_opy_():
  global bstack111llll1ll_opy_
  bstack1ll11ll11l_opy_ = {}
  try:
    if not os.path.isfile(bstack111llll1ll_opy_):
      with open(bstack111llll1ll_opy_, bstack1l1_opy_ (u"ࠨࡹࠪಀ")):
        pass
      with open(bstack111llll1ll_opy_, bstack1l1_opy_ (u"ࠤࡺ࠯ࠧಁ")) as outfile:
        json.dump({}, outfile)
    if os.path.exists(bstack111llll1ll_opy_):
      bstack1ll11ll11l_opy_ = json.load(open(bstack111llll1ll_opy_, bstack1l1_opy_ (u"ࠪࡶࡧ࠭ಂ")))
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡲࡦࡣࡧ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ಃ") + str(e))
  finally:
    return bstack1ll11ll11l_opy_
def bstack11lll1llll_opy_(platform_index, item_index):
  global bstack111llll1ll_opy_
  try:
    bstack1ll11ll11l_opy_ = bstack1lll111l1l_opy_()
    bstack1ll11ll11l_opy_[item_index] = platform_index
    with open(bstack111llll1ll_opy_, bstack1l1_opy_ (u"ࠧࡽࠫࠣ಄")) as outfile:
      json.dump(bstack1ll11ll11l_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡹࡵ࡭ࡹ࡯࡮ࡨࠢࡷࡳࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫಅ") + str(e))
def bstack1llll11ll1_opy_(bstack1l1l111l1_opy_):
  global CONFIG
  bstack11111l111_opy_ = bstack1l1_opy_ (u"ࠧࠨಆ")
  if not bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಇ") in CONFIG:
    logger.info(bstack1l1_opy_ (u"ࠩࡑࡳࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠡࡲࡤࡷࡸ࡫ࡤࠡࡷࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡬࡫࡮ࡦࡴࡤࡸࡪࠦࡲࡦࡲࡲࡶࡹࠦࡦࡰࡴࠣࡖࡴࡨ࡯ࡵࠢࡵࡹࡳ࠭ಈ"))
  try:
    platform = CONFIG[bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಉ")][bstack1l1l111l1_opy_]
    if bstack1l1_opy_ (u"ࠫࡴࡹࠧಊ") in platform:
      bstack11111l111_opy_ += str(platform[bstack1l1_opy_ (u"ࠬࡵࡳࠨಋ")]) + bstack1l1_opy_ (u"࠭ࠬࠡࠩಌ")
    if bstack1l1_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪ಍") in platform:
      bstack11111l111_opy_ += str(platform[bstack1l1_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫಎ")]) + bstack1l1_opy_ (u"ࠩ࠯ࠤࠬಏ")
    if bstack1l1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧಐ") in platform:
      bstack11111l111_opy_ += str(platform[bstack1l1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨ಑")]) + bstack1l1_opy_ (u"ࠬ࠲ࠠࠨಒ")
    if bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨಓ") in platform:
      bstack11111l111_opy_ += str(platform[bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩಔ")]) + bstack1l1_opy_ (u"ࠨ࠮ࠣࠫಕ")
    if bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧಖ") in platform:
      bstack11111l111_opy_ += str(platform[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨಗ")]) + bstack1l1_opy_ (u"ࠫ࠱ࠦࠧಘ")
    if bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ಙ") in platform:
      bstack11111l111_opy_ += str(platform[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧಚ")]) + bstack1l1_opy_ (u"ࠧ࠭ࠢࠪಛ")
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠨࡕࡲࡱࡪࠦࡥࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡱ࡫ࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡴࡶࡵ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡷ࡫ࡰࡰࡴࡷࠤ࡬࡫࡮ࡦࡴࡤࡸ࡮ࡵ࡮ࠨಜ") + str(e))
  finally:
    if bstack11111l111_opy_[len(bstack11111l111_opy_) - 2:] == bstack1l1_opy_ (u"ࠩ࠯ࠤࠬಝ"):
      bstack11111l111_opy_ = bstack11111l111_opy_[:-2]
    return bstack11111l111_opy_
def bstack11l1lll11_opy_(path, bstack11111l111_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1l1111ll11_opy_ = ET.parse(path)
    bstack1l11l1ll1l_opy_ = bstack1l1111ll11_opy_.getroot()
    bstack11l111lll1_opy_ = None
    for suite in bstack1l11l1ll1l_opy_.iter(bstack1l1_opy_ (u"ࠪࡷࡺ࡯ࡴࡦࠩಞ")):
      if bstack1l1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫಟ") in suite.attrib:
        suite.attrib[bstack1l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪಠ")] += bstack1l1_opy_ (u"࠭ࠠࠨಡ") + bstack11111l111_opy_
        bstack11l111lll1_opy_ = suite
    bstack1lll1l111_opy_ = None
    for robot in bstack1l11l1ll1l_opy_.iter(bstack1l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ಢ")):
      bstack1lll1l111_opy_ = robot
    bstack11l11111l1_opy_ = len(bstack1lll1l111_opy_.findall(bstack1l1_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧಣ")))
    if bstack11l11111l1_opy_ == 1:
      bstack1lll1l111_opy_.remove(bstack1lll1l111_opy_.findall(bstack1l1_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨತ"))[0])
      bstack1l111lll1_opy_ = ET.Element(bstack1l1_opy_ (u"ࠪࡷࡺ࡯ࡴࡦࠩಥ"), attrib={bstack1l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩದ"): bstack1l1_opy_ (u"࡙ࠬࡵࡪࡶࡨࡷࠬಧ"), bstack1l1_opy_ (u"࠭ࡩࡥࠩನ"): bstack1l1_opy_ (u"ࠧࡴ࠲ࠪ಩")})
      bstack1lll1l111_opy_.insert(1, bstack1l111lll1_opy_)
      bstack1l1lll111_opy_ = None
      for suite in bstack1lll1l111_opy_.iter(bstack1l1_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧಪ")):
        bstack1l1lll111_opy_ = suite
      bstack1l1lll111_opy_.append(bstack11l111lll1_opy_)
      bstack1l111lllll_opy_ = None
      for status in bstack11l111lll1_opy_.iter(bstack1l1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩಫ")):
        bstack1l111lllll_opy_ = status
      bstack1l1lll111_opy_.append(bstack1l111lllll_opy_)
    bstack1l1111ll11_opy_.write(path)
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡳࡵ࡬ࡲ࡬ࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡯࡮ࡨࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠨಬ") + str(e))
def bstack1ll1111lll_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack11llll1lll_opy_
  global CONFIG
  if bstack1l1_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡴࡦࡺࡨࠣಭ") in options:
    del options[bstack1l1_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࡵࡧࡴࡩࠤಮ")]
  json_data = bstack1lll111l1l_opy_()
  for bstack1ll11111l_opy_ in json_data.keys():
    path = os.path.join(os.getcwd(), bstack1l1_opy_ (u"࠭ࡰࡢࡤࡲࡸࡤࡸࡥࡴࡷ࡯ࡸࡸ࠭ಯ"), str(bstack1ll11111l_opy_), bstack1l1_opy_ (u"ࠧࡰࡷࡷࡴࡺࡺ࠮ࡹ࡯࡯ࠫರ"))
    bstack11l1lll11_opy_(path, bstack1llll11ll1_opy_(json_data[bstack1ll11111l_opy_]))
  bstack11l1llll1l_opy_()
  return bstack11llll1lll_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1111lllll_opy_(self, ff_profile_dir):
  global bstack1l1l11lll1_opy_
  if not ff_profile_dir:
    return None
  return bstack1l1l11lll1_opy_(self, ff_profile_dir)
def bstack1l1ll1l11l_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1ll1ll11l_opy_
  bstack1lllll11ll_opy_ = []
  if bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಱ") in CONFIG:
    bstack1lllll11ll_opy_ = CONFIG[bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಲ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack1l1_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࠦಳ")],
      pabot_args[bstack1l1_opy_ (u"ࠦࡻ࡫ࡲࡣࡱࡶࡩࠧ಴")],
      argfile,
      pabot_args.get(bstack1l1_opy_ (u"ࠧ࡮ࡩࡷࡧࠥವ")),
      pabot_args[bstack1l1_opy_ (u"ࠨࡰࡳࡱࡦࡩࡸࡹࡥࡴࠤಶ")],
      platform[0],
      bstack1ll1ll11l_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack1l1_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡨ࡬ࡰࡪࡹࠢಷ")] or [(bstack1l1_opy_ (u"ࠣࠤಸ"), None)]
    for platform in enumerate(bstack1lllll11ll_opy_)
  ]
def bstack1l1ll1l1l1_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1l11l11ll_opy_=bstack1l1_opy_ (u"ࠩࠪಹ")):
  global bstack1l1l1l11ll_opy_
  self.platform_index = platform_index
  self.bstack1ll1lll1l_opy_ = bstack1l11l11ll_opy_
  bstack1l1l1l11ll_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1lll1llll1_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1ll1l11l11_opy_
  global bstack1ll11ll1l_opy_
  bstack1ll1l1111l_opy_ = copy.deepcopy(item)
  if not bstack1l1_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬ಺") in item.options:
    bstack1ll1l1111l_opy_.options[bstack1l1_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭಻")] = []
  bstack1ll11ll111_opy_ = bstack1ll1l1111l_opy_.options[bstack1l1_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫಼ࠧ")].copy()
  for v in bstack1ll1l1111l_opy_.options[bstack1l1_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨಽ")]:
    if bstack1l1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝࠭ಾ") in v:
      bstack1ll11ll111_opy_.remove(v)
    if bstack1l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡄࡎࡌࡅࡗࡍࡓࠨಿ") in v:
      bstack1ll11ll111_opy_.remove(v)
    if bstack1l1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ೀ") in v:
      bstack1ll11ll111_opy_.remove(v)
  bstack1ll11ll111_opy_.insert(0, bstack1l1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡓࡐࡆ࡚ࡆࡐࡔࡐࡍࡓࡊࡅ࡙࠼ࡾࢁࠬು").format(bstack1ll1l1111l_opy_.platform_index))
  bstack1ll11ll111_opy_.insert(0, bstack1l1_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡈࡊࡌࡌࡐࡅࡄࡐࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒ࠻ࡽࢀࠫೂ").format(bstack1ll1l1111l_opy_.bstack1ll1lll1l_opy_))
  bstack1ll1l1111l_opy_.options[bstack1l1_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧೃ")] = bstack1ll11ll111_opy_
  if bstack1ll11ll1l_opy_:
    bstack1ll1l1111l_opy_.options[bstack1l1_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨೄ")].insert(0, bstack1l1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡃࡍࡋࡄࡖࡌ࡙࠺ࡼࡿࠪ೅").format(bstack1ll11ll1l_opy_))
  return bstack1ll1l11l11_opy_(caller_id, datasources, is_last, bstack1ll1l1111l_opy_, outs_dir)
def bstack111ll11l1_opy_(command, item_index):
  if bstack111l11ll_opy_.get_property(bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩೆ")):
    os.environ[bstack1l1_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪೇ")] = json.dumps(CONFIG[bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ೈ")][item_index % bstack1ll1lllll1_opy_])
  global bstack1ll11ll1l_opy_
  if bstack1ll11ll1l_opy_:
    command[0] = command[0].replace(bstack1l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ೉"), bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠱ࡸࡪ࡫ࠡࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠢ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠡࠩೊ") + str(
      item_index) + bstack1l1_opy_ (u"࠭ࠠࠨೋ") + bstack1ll11ll1l_opy_, 1)
  else:
    command[0] = command[0].replace(bstack1l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ೌ"),
                                    bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡴࡦ࡮ࠤࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠥ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠤ್ࠬ") + str(item_index), 1)
def bstack1l1ll11l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1l1lllllll_opy_
  bstack111ll11l1_opy_(command, item_index)
  return bstack1l1lllllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack1ll1l1ll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1l1lllllll_opy_
  bstack111ll11l1_opy_(command, item_index)
  return bstack1l1lllllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
def bstack11l111l1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1l1lllllll_opy_
  bstack111ll11l1_opy_(command, item_index)
  return bstack1l1lllllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack11ll1lllll_opy_(self, runner, quiet=False, capture=True):
  global bstack1l11ll11l1_opy_
  bstack1llll1l1l_opy_ = bstack1l11ll11l1_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack1l1_opy_ (u"ࠩࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࡤࡧࡲࡳࠩ೎")):
      runner.exception_arr = []
    if not hasattr(runner, bstack1l1_opy_ (u"ࠪࡩࡽࡩ࡟ࡵࡴࡤࡧࡪࡨࡡࡤ࡭ࡢࡥࡷࡸࠧ೏")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1llll1l1l_opy_
def bstack1ll1l1ll1l_opy_(runner, hook_name, context, element, bstack11l1l1l1ll_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack1lllll111l_opy_.bstack11ll11ll_opy_(hook_name, element)
    bstack11l1l1l1ll_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack1lllll111l_opy_.bstack11l1ll1l_opy_(element)
      if hook_name not in [bstack1l1_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠨ೐"), bstack1l1_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡦࡲ࡬ࠨ೑")] and args and hasattr(args[0], bstack1l1_opy_ (u"࠭ࡥࡳࡴࡲࡶࡤࡳࡥࡴࡵࡤ࡫ࡪ࠭೒")):
        args[0].error_message = bstack1l1_opy_ (u"ࠧࠨ೓")
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡭ࡧ࡮ࡥ࡮ࡨࠤ࡭ࡵ࡯࡬ࡵࠣ࡭ࡳࠦࡢࡦࡪࡤࡺࡪࡀࠠࡼࡿࠪ೔").format(str(e)))
def bstack1l111ll1l1_opy_(runner, name, context, bstack11l1l1l1ll_opy_, *args):
    if runner.hooks.get(bstack1l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨೕ")).__name__ != bstack1l1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲ࡟ࡥࡧࡩࡥࡺࡲࡴࡠࡪࡲࡳࡰࠨೖ"):
      bstack1ll1l1ll1l_opy_(runner, name, context, runner, bstack11l1l1l1ll_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack1ll1l111l1_opy_(bstack1l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ೗")) else context.browser
      runner.driver_initialised = bstack1l1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤ೘")
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡤࡳ࡫ࡹࡩࡷࠦࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡴࡧࠣࡥࡹࡺࡲࡪࡤࡸࡸࡪࡀࠠࡼࡿࠪ೙").format(str(e)))
def bstack1l1l111ll1_opy_(runner, name, context, bstack11l1l1l1ll_opy_, *args):
    bstack1ll1l1ll1l_opy_(runner, name, context, context.feature, bstack11l1l1l1ll_opy_, *args)
    try:
      if not bstack1ll11l11l1_opy_:
        bstack11l1llllll_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll1l111l1_opy_(bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭೚")) else context.browser
        if is_driver_active(bstack11l1llllll_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack1l1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤ೛")
          bstack1llll1lll1_opy_ = str(runner.feature.name)
          bstack11l1l1l111_opy_(context, bstack1llll1lll1_opy_)
          bstack11l1llllll_opy_.execute_script(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧ೜") + json.dumps(bstack1llll1lll1_opy_) + bstack1l1_opy_ (u"ࠪࢁࢂ࠭ೝ"))
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡦࡦࡣࡷࡹࡷ࡫࠺ࠡࡽࢀࠫೞ").format(str(e)))
def bstack111lll111_opy_(runner, name, context, bstack11l1l1l1ll_opy_, *args):
    if hasattr(context, bstack1l1_opy_ (u"ࠬࡹࡣࡦࡰࡤࡶ࡮ࡵࠧ೟")):
        bstack1lllll111l_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack1l1_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨೠ")) else context.feature
    bstack1ll1l1ll1l_opy_(runner, name, context, target, bstack11l1l1l1ll_opy_, *args)
def bstack11l1ll1ll_opy_(runner, name, context, bstack11l1l1l1ll_opy_, *args):
    if len(context.scenario.tags) == 0: bstack1lllll111l_opy_.start_test(context)
    bstack1ll1l1ll1l_opy_(runner, name, context, context.scenario, bstack11l1l1l1ll_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack1l1111l11l_opy_.bstack1l1ll1llll_opy_(context, *args)
    try:
      bstack11l1llllll_opy_ = bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ೡ"), context.browser)
      if is_driver_active(bstack11l1llllll_opy_):
        bstack1l1ll1l1_opy_.bstack1ll1l111l_opy_(bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧೢ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack1l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠦೣ")
        if (not bstack1ll11l11l1_opy_):
          scenario_name = args[0].name
          feature_name = bstack1llll1lll1_opy_ = str(runner.feature.name)
          bstack1llll1lll1_opy_ = feature_name + bstack1l1_opy_ (u"ࠪࠤ࠲ࠦࠧ೤") + scenario_name
          if runner.driver_initialised == bstack1l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨ೥"):
            bstack11l1l1l111_opy_(context, bstack1llll1lll1_opy_)
            bstack11l1llllll_opy_.execute_script(bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪ೦") + json.dumps(bstack1llll1lll1_opy_) + bstack1l1_opy_ (u"࠭ࡽࡾࠩ೧"))
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡩ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡧࡪࡴࡡࡳ࡫ࡲ࠾ࠥࢁࡽࠨ೨").format(str(e)))
def bstack11lll1ll1_opy_(runner, name, context, bstack11l1l1l1ll_opy_, *args):
    bstack1ll1l1ll1l_opy_(runner, name, context, args[0], bstack11l1l1l1ll_opy_, *args)
    try:
      bstack11l1llllll_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll1l111l1_opy_(bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ೩")) else context.browser
      if is_driver_active(bstack11l1llllll_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack1l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢ೪")
        bstack1lllll111l_opy_.bstack11ll11l1_opy_(args[0])
        if runner.driver_initialised == bstack1l1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣ೫"):
          feature_name = bstack1llll1lll1_opy_ = str(runner.feature.name)
          bstack1llll1lll1_opy_ = feature_name + bstack1l1_opy_ (u"ࠫࠥ࠳ࠠࠨ೬") + context.scenario.name
          bstack11l1llllll_opy_.execute_script(bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪ೭") + json.dumps(bstack1llll1lll1_opy_) + bstack1l1_opy_ (u"࠭ࡽࡾࠩ೮"))
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡩ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡸࡪࡶ࠺ࠡࡽࢀࠫ೯").format(str(e)))
def bstack1l1ll11l1l_opy_(runner, name, context, bstack11l1l1l1ll_opy_, *args):
  bstack1lllll111l_opy_.bstack11l1l1l1_opy_(args[0])
  try:
    bstack11l1111l1_opy_ = args[0].status.name
    bstack11l1llllll_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ೰") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack11l1llllll_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack1l1_opy_ (u"ࠩ࡬ࡲࡸࡺࡥࡱࠩೱ")
        feature_name = bstack1llll1lll1_opy_ = str(runner.feature.name)
        bstack1llll1lll1_opy_ = feature_name + bstack1l1_opy_ (u"ࠪࠤ࠲ࠦࠧೲ") + context.scenario.name
        bstack11l1llllll_opy_.execute_script(bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩೳ") + json.dumps(bstack1llll1lll1_opy_) + bstack1l1_opy_ (u"ࠬࢃࡽࠨ೴"))
    if str(bstack11l1111l1_opy_).lower() == bstack1l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭೵"):
      bstack11lll11lll_opy_ = bstack1l1_opy_ (u"ࠧࠨ೶")
      bstack11l11l1l1_opy_ = bstack1l1_opy_ (u"ࠨࠩ೷")
      bstack11ll1l1l1_opy_ = bstack1l1_opy_ (u"ࠩࠪ೸")
      try:
        import traceback
        bstack11lll11lll_opy_ = runner.exception.__class__.__name__
        bstack11l11lll_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11l11l1l1_opy_ = bstack1l1_opy_ (u"ࠪࠤࠬ೹").join(bstack11l11lll_opy_)
        bstack11ll1l1l1_opy_ = bstack11l11lll_opy_[-1]
      except Exception as e:
        logger.debug(bstack1ll1l11ll1_opy_.format(str(e)))
      bstack11lll11lll_opy_ += bstack11ll1l1l1_opy_
      bstack11l11l1l11_opy_(context, json.dumps(str(args[0].name) + bstack1l1_opy_ (u"ࠦࠥ࠳ࠠࡇࡣ࡬ࡰࡪࡪࠡ࡝ࡰࠥ೺") + str(bstack11l11l1l1_opy_)),
                          bstack1l1_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦ೻"))
      if runner.driver_initialised == bstack1l1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦ೼"):
        bstack11ll1l11l_opy_(getattr(context, bstack1l1_opy_ (u"ࠧࡱࡣࡪࡩࠬ೽"), None), bstack1l1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ೾"), bstack11lll11lll_opy_)
        bstack11l1llllll_opy_.execute_script(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧ೿") + json.dumps(str(args[0].name) + bstack1l1_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤഀ") + str(bstack11l11l1l1_opy_)) + bstack1l1_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣࡿࢀࠫഁ"))
      if runner.driver_initialised == bstack1l1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥം"):
        bstack1l1lll1lll_opy_(bstack11l1llllll_opy_, bstack1l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ഃ"), bstack1l1_opy_ (u"ࠢࡔࡥࡨࡲࡦࡸࡩࡰࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡ࡞ࡱࠦഄ") + str(bstack11lll11lll_opy_))
    else:
      bstack11l11l1l11_opy_(context, bstack1l1_opy_ (u"ࠣࡒࡤࡷࡸ࡫ࡤࠢࠤഅ"), bstack1l1_opy_ (u"ࠤ࡬ࡲ࡫ࡵࠢആ"))
      if runner.driver_initialised == bstack1l1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣഇ"):
        bstack11ll1l11l_opy_(getattr(context, bstack1l1_opy_ (u"ࠫࡵࡧࡧࡦࠩഈ"), None), bstack1l1_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧഉ"))
      bstack11l1llllll_opy_.execute_script(bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫഊ") + json.dumps(str(args[0].name) + bstack1l1_opy_ (u"ࠢࠡ࠯ࠣࡔࡦࡹࡳࡦࡦࠤࠦഋ")) + bstack1l1_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡩ࡯ࡨࡲࠦࢂࢃࠧഌ"))
      if runner.driver_initialised == bstack1l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢ഍"):
        bstack1l1lll1lll_opy_(bstack11l1llllll_opy_, bstack1l1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥഎ"))
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠ࡮ࡣࡵ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࠦࡩ࡯ࠢࡤࡪࡹ࡫ࡲࠡࡵࡷࡩࡵࡀࠠࡼࡿࠪഏ").format(str(e)))
  bstack1ll1l1ll1l_opy_(runner, name, context, args[0], bstack11l1l1l1ll_opy_, *args)
def bstack11lll111l1_opy_(runner, name, context, bstack11l1l1l1ll_opy_, *args):
  bstack1lllll111l_opy_.end_test(args[0])
  try:
    bstack1l11l111l_opy_ = args[0].status.name
    bstack11l1llllll_opy_ = bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫഐ"), context.browser)
    bstack1l1111l11l_opy_.bstack11lll1l111_opy_(bstack11l1llllll_opy_)
    if str(bstack1l11l111l_opy_).lower() == bstack1l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭഑"):
      bstack11lll11lll_opy_ = bstack1l1_opy_ (u"ࠧࠨഒ")
      bstack11l11l1l1_opy_ = bstack1l1_opy_ (u"ࠨࠩഓ")
      bstack11ll1l1l1_opy_ = bstack1l1_opy_ (u"ࠩࠪഔ")
      try:
        import traceback
        bstack11lll11lll_opy_ = runner.exception.__class__.__name__
        bstack11l11lll_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11l11l1l1_opy_ = bstack1l1_opy_ (u"ࠪࠤࠬക").join(bstack11l11lll_opy_)
        bstack11ll1l1l1_opy_ = bstack11l11lll_opy_[-1]
      except Exception as e:
        logger.debug(bstack1ll1l11ll1_opy_.format(str(e)))
      bstack11lll11lll_opy_ += bstack11ll1l1l1_opy_
      bstack11l11l1l11_opy_(context, json.dumps(str(args[0].name) + bstack1l1_opy_ (u"ࠦࠥ࠳ࠠࡇࡣ࡬ࡰࡪࡪࠡ࡝ࡰࠥഖ") + str(bstack11l11l1l1_opy_)),
                          bstack1l1_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦഗ"))
      if runner.driver_initialised == bstack1l1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣഘ") or runner.driver_initialised == bstack1l1_opy_ (u"ࠧࡪࡰࡶࡸࡪࡶࠧങ"):
        bstack11ll1l11l_opy_(getattr(context, bstack1l1_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭ച"), None), bstack1l1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤഛ"), bstack11lll11lll_opy_)
        bstack11l1llllll_opy_.execute_script(bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨജ") + json.dumps(str(args[0].name) + bstack1l1_opy_ (u"ࠦࠥ࠳ࠠࡇࡣ࡬ࡰࡪࡪࠡ࡝ࡰࠥഝ") + str(bstack11l11l1l1_opy_)) + bstack1l1_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥࡩࡷࡸ࡯ࡳࠤࢀࢁࠬഞ"))
      if runner.driver_initialised == bstack1l1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣട") or runner.driver_initialised == bstack1l1_opy_ (u"ࠧࡪࡰࡶࡸࡪࡶࠧഠ"):
        bstack1l1lll1lll_opy_(bstack11l1llllll_opy_, bstack1l1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨഡ"), bstack1l1_opy_ (u"ࠤࡖࡧࡪࡴࡡࡳ࡫ࡲࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࡠࡳࠨഢ") + str(bstack11lll11lll_opy_))
    else:
      bstack11l11l1l11_opy_(context, bstack1l1_opy_ (u"ࠥࡔࡦࡹࡳࡦࡦࠤࠦണ"), bstack1l1_opy_ (u"ࠦ࡮ࡴࡦࡰࠤത"))
      if runner.driver_initialised == bstack1l1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢഥ") or runner.driver_initialised == bstack1l1_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭ദ"):
        bstack11ll1l11l_opy_(getattr(context, bstack1l1_opy_ (u"ࠧࡱࡣࡪࡩࠬധ"), None), bstack1l1_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣന"))
      bstack11l1llllll_opy_.execute_script(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧഩ") + json.dumps(str(args[0].name) + bstack1l1_opy_ (u"ࠥࠤ࠲ࠦࡐࡢࡵࡶࡩࡩࠧࠢപ")) + bstack1l1_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤ࡬ࡲ࡫ࡵࠢࡾࡿࠪഫ"))
      if runner.driver_initialised == bstack1l1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢബ") or runner.driver_initialised == bstack1l1_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭ഭ"):
        bstack1l1lll1lll_opy_(bstack11l1llllll_opy_, bstack1l1_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢമ"))
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪയ").format(str(e)))
  bstack1ll1l1ll1l_opy_(runner, name, context, context.scenario, bstack11l1l1l1ll_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack1l1ll1l111_opy_(runner, name, context, bstack11l1l1l1ll_opy_, *args):
    target = context.scenario if hasattr(context, bstack1l1_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫര")) else context.feature
    bstack1ll1l1ll1l_opy_(runner, name, context, target, bstack11l1l1l1ll_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack1l111111l1_opy_(runner, name, context, bstack11l1l1l1ll_opy_, *args):
    try:
      bstack11l1llllll_opy_ = bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩറ"), context.browser)
      if context.failed is True:
        bstack1l1111l1l1_opy_ = []
        bstack1l11l1llll_opy_ = []
        bstack1lll1l1l1_opy_ = []
        bstack1l1l1l11l_opy_ = bstack1l1_opy_ (u"ࠫࠬല")
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack1l1111l1l1_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11l11lll_opy_ = traceback.format_tb(exc_tb)
            bstack11ll1lll1_opy_ = bstack1l1_opy_ (u"ࠬࠦࠧള").join(bstack11l11lll_opy_)
            bstack1l11l1llll_opy_.append(bstack11ll1lll1_opy_)
            bstack1lll1l1l1_opy_.append(bstack11l11lll_opy_[-1])
        except Exception as e:
          logger.debug(bstack1ll1l11ll1_opy_.format(str(e)))
        bstack11lll11lll_opy_ = bstack1l1_opy_ (u"࠭ࠧഴ")
        for i in range(len(bstack1l1111l1l1_opy_)):
          bstack11lll11lll_opy_ += bstack1l1111l1l1_opy_[i] + bstack1lll1l1l1_opy_[i] + bstack1l1_opy_ (u"ࠧ࡝ࡰࠪവ")
        bstack1l1l1l11l_opy_ = bstack1l1_opy_ (u"ࠨࠢࠪശ").join(bstack1l11l1llll_opy_)
        if runner.driver_initialised in [bstack1l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥഷ"), bstack1l1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠢസ")]:
          bstack11l11l1l11_opy_(context, bstack1l1l1l11l_opy_, bstack1l1_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥഹ"))
          bstack11ll1l11l_opy_(getattr(context, bstack1l1_opy_ (u"ࠬࡶࡡࡨࡧࠪഺ"), None), bstack1l1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ഻"), bstack11lll11lll_opy_)
          bstack11l1llllll_opy_.execute_script(bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾഼ࠬ") + json.dumps(bstack1l1l1l11l_opy_) + bstack1l1_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧࢃࡽࠨഽ"))
          bstack1l1lll1lll_opy_(bstack11l1llllll_opy_, bstack1l1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤാ"), bstack1l1_opy_ (u"ࠥࡗࡴࡳࡥࠡࡵࡦࡩࡳࡧࡲࡪࡱࡶࠤ࡫ࡧࡩ࡭ࡧࡧ࠾ࠥࡢ࡮ࠣി") + str(bstack11lll11lll_opy_))
          bstack11lllll1l1_opy_ = bstack11lll1l1l_opy_(bstack1l1l1l11l_opy_, runner.feature.name, logger)
          if (bstack11lllll1l1_opy_ != None):
            bstack11l11l11l_opy_.append(bstack11lllll1l1_opy_)
      else:
        if runner.driver_initialised in [bstack1l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠧീ"), bstack1l1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤു")]:
          bstack11l11l1l11_opy_(context, bstack1l1_opy_ (u"ࠨࡆࡦࡣࡷࡹࡷ࡫࠺ࠡࠤൂ") + str(runner.feature.name) + bstack1l1_opy_ (u"ࠢࠡࡲࡤࡷࡸ࡫ࡤࠢࠤൃ"), bstack1l1_opy_ (u"ࠣ࡫ࡱࡪࡴࠨൄ"))
          bstack11ll1l11l_opy_(getattr(context, bstack1l1_opy_ (u"ࠩࡳࡥ࡬࡫ࠧ൅"), None), bstack1l1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥെ"))
          bstack11l1llllll_opy_.execute_script(bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩേ") + json.dumps(bstack1l1_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࡀࠠࠣൈ") + str(runner.feature.name) + bstack1l1_opy_ (u"ࠨࠠࡱࡣࡶࡷࡪࡪࠡࠣ൉")) + bstack1l1_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭ൊ"))
          bstack1l1lll1lll_opy_(bstack11l1llllll_opy_, bstack1l1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨോ"))
          bstack11lllll1l1_opy_ = bstack11lll1l1l_opy_(bstack1l1l1l11l_opy_, runner.feature.name, logger)
          if (bstack11lllll1l1_opy_ != None):
            bstack11l11l11l_opy_.append(bstack11lllll1l1_opy_)
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡮ࡴࠠࡢࡨࡷࡩࡷࠦࡦࡦࡣࡷࡹࡷ࡫࠺ࠡࡽࢀࠫൌ").format(str(e)))
    bstack1ll1l1ll1l_opy_(runner, name, context, context.feature, bstack11l1l1l1ll_opy_, *args)
def bstack1ll1l11lll_opy_(runner, name, context, bstack11l1l1l1ll_opy_, *args):
    bstack1ll1l1ll1l_opy_(runner, name, context, runner, bstack11l1l1l1ll_opy_, *args)
def bstack1l1l11l1ll_opy_(self, name, context, *args):
  if bstack1ll11ll1ll_opy_:
    platform_index = int(threading.current_thread()._name) % bstack1ll1lllll1_opy_
    bstack1l1llll1l_opy_ = CONFIG[bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ്࠭")][platform_index]
    os.environ[bstack1l1_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬൎ")] = json.dumps(bstack1l1llll1l_opy_)
  global bstack11l1l1l1ll_opy_
  if not hasattr(self, bstack1l1_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡳࡦࡦࠪ൏")):
    self.driver_initialised = None
  bstack11l111lll_opy_ = {
      bstack1l1_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠪ൐"): bstack1l111ll1l1_opy_,
      bstack1l1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠨ൑"): bstack1l1l111ll1_opy_,
      bstack1l1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡶࡤ࡫ࠬ൒"): bstack111lll111_opy_,
      bstack1l1_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫ൓"): bstack11l1ll1ll_opy_,
      bstack1l1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠨൔ"): bstack11lll1ll1_opy_,
      bstack1l1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡹ࡫ࡰࠨൕ"): bstack1l1ll11l1l_opy_,
      bstack1l1_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ൖ"): bstack11lll111l1_opy_,
      bstack1l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡺࡡࡨࠩൗ"): bstack1l1ll1l111_opy_,
      bstack1l1_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡦࡦࡣࡷࡹࡷ࡫ࠧ൘"): bstack1l111111l1_opy_,
      bstack1l1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫ൙"): bstack1ll1l11lll_opy_
  }
  handler = bstack11l111lll_opy_.get(name, bstack11l1l1l1ll_opy_)
  handler(self, name, context, bstack11l1l1l1ll_opy_, *args)
  if name in [bstack1l1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠩ൚"), bstack1l1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫ൛"), bstack1l1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠧ൜")]:
    try:
      bstack11l1llllll_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll1l111l1_opy_(bstack1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫ൝")) else context.browser
      bstack11l1l1llll_opy_ = (
        (name == bstack1l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠩ൞") and self.driver_initialised == bstack1l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦൟ")) or
        (name == bstack1l1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨൠ") and self.driver_initialised == bstack1l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥൡ")) or
        (name == bstack1l1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫൢ") and self.driver_initialised in [bstack1l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨൣ"), bstack1l1_opy_ (u"ࠧ࡯࡮ࡴࡶࡨࡴࠧ൤")]) or
        (name == bstack1l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡹࡴࡦࡲࠪ൥") and self.driver_initialised == bstack1l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧ൦"))
      )
      if bstack11l1l1llll_opy_:
        self.driver_initialised = None
        bstack11l1llllll_opy_.quit()
    except Exception:
      pass
def bstack11l11ll1ll_opy_(config, startdir):
  return bstack1l1_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾ࠴ࢂࠨ൧").format(bstack1l1_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣ൨"))
notset = Notset()
def bstack11l1llll11_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1lll1ll111_opy_
  if str(name).lower() == bstack1l1_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࠪ൩"):
    return bstack1l1_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥ൪")
  else:
    return bstack1lll1ll111_opy_(self, name, default, skip)
def bstack1llll11lll_opy_(item, when):
  global bstack11lll11l11_opy_
  try:
    bstack11lll11l11_opy_(item, when)
  except Exception as e:
    pass
def bstack111lll11l_opy_():
  return
def bstack1l1ll1ll11_opy_(type, name, status, reason, bstack1l11lll1ll_opy_, bstack1llll111l1_opy_):
  bstack11l1ll11l1_opy_ = {
    bstack1l1_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬ൫"): type,
    bstack1l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ൬"): {}
  }
  if type == bstack1l1_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩ൭"):
    bstack11l1ll11l1_opy_[bstack1l1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ൮")][bstack1l1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ൯")] = bstack1l11lll1ll_opy_
    bstack11l1ll11l1_opy_[bstack1l1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭൰")][bstack1l1_opy_ (u"ࠫࡩࡧࡴࡢࠩ൱")] = json.dumps(str(bstack1llll111l1_opy_))
  if type == bstack1l1_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭൲"):
    bstack11l1ll11l1_opy_[bstack1l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ൳")][bstack1l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ൴")] = name
  if type == bstack1l1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ൵"):
    bstack11l1ll11l1_opy_[bstack1l1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ൶")][bstack1l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ൷")] = status
    if status == bstack1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ൸"):
      bstack11l1ll11l1_opy_[bstack1l1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ൹")][bstack1l1_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ൺ")] = json.dumps(str(reason))
  bstack11ll1ll1ll_opy_ = bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬൻ").format(json.dumps(bstack11l1ll11l1_opy_))
  return bstack11ll1ll1ll_opy_
def bstack1l1l11l11_opy_(driver_command, response):
    if driver_command == bstack1l1_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬർ"):
        bstack1l1ll1l1_opy_.bstack1l1ll1l11_opy_({
            bstack1l1_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨൽ"): response[bstack1l1_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩൾ")],
            bstack1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫൿ"): bstack1l1ll1l1_opy_.current_test_uuid()
        })
def bstack11l1l1lll1_opy_(item, call, rep):
  global bstack1ll1l1llll_opy_
  global bstack1l1ll1ll1l_opy_
  global bstack1ll11l11l1_opy_
  name = bstack1l1_opy_ (u"ࠬ࠭඀")
  try:
    if rep.when == bstack1l1_opy_ (u"࠭ࡣࡢ࡮࡯ࠫඁ"):
      bstack1ll1l1111_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack1ll11l11l1_opy_:
          name = str(rep.nodeid)
          bstack1l11ll11ll_opy_ = bstack1l1ll1ll11_opy_(bstack1l1_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨං"), name, bstack1l1_opy_ (u"ࠨࠩඃ"), bstack1l1_opy_ (u"ࠩࠪ඄"), bstack1l1_opy_ (u"ࠪࠫඅ"), bstack1l1_opy_ (u"ࠫࠬආ"))
          threading.current_thread().bstack1l1ll1l1l_opy_ = name
          for driver in bstack1l1ll1ll1l_opy_:
            if bstack1ll1l1111_opy_ == driver.session_id:
              driver.execute_script(bstack1l11ll11ll_opy_)
      except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬඇ").format(str(e)))
      try:
        bstack111l11l1l_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack1l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧඈ"):
          status = bstack1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧඉ") if rep.outcome.lower() == bstack1l1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨඊ") else bstack1l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩඋ")
          reason = bstack1l1_opy_ (u"ࠪࠫඌ")
          if status == bstack1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫඍ"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack1l1_opy_ (u"ࠬ࡯࡮ࡧࡱࠪඎ") if status == bstack1l1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ඏ") else bstack1l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ඐ")
          data = name + bstack1l1_opy_ (u"ࠨࠢࡳࡥࡸࡹࡥࡥࠣࠪඑ") if status == bstack1l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩඒ") else name + bstack1l1_opy_ (u"ࠪࠤ࡫ࡧࡩ࡭ࡧࡧࠥࠥ࠭ඓ") + reason
          bstack1l1lllll11_opy_ = bstack1l1ll1ll11_opy_(bstack1l1_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ඔ"), bstack1l1_opy_ (u"ࠬ࠭ඕ"), bstack1l1_opy_ (u"࠭ࠧඖ"), bstack1l1_opy_ (u"ࠧࠨ඗"), level, data)
          for driver in bstack1l1ll1ll1l_opy_:
            if bstack1ll1l1111_opy_ == driver.session_id:
              driver.execute_script(bstack1l1lllll11_opy_)
      except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡩ࡯࡯ࡶࡨࡼࡹࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬ඘").format(str(e)))
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡴࡢࡶࡨࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿࢂ࠭඙").format(str(e)))
  bstack1ll1l1llll_opy_(item, call, rep)
def bstack11l1111l11_opy_(driver, bstack11ll11l11l_opy_, test=None):
  global bstack1llll11111_opy_
  if test != None:
    bstack1ll11ll1l1_opy_ = getattr(test, bstack1l1_opy_ (u"ࠪࡲࡦࡳࡥࠨක"), None)
    bstack1llll1111l_opy_ = getattr(test, bstack1l1_opy_ (u"ࠫࡺࡻࡩࡥࠩඛ"), None)
    PercySDK.screenshot(driver, bstack11ll11l11l_opy_, bstack1ll11ll1l1_opy_=bstack1ll11ll1l1_opy_, bstack1llll1111l_opy_=bstack1llll1111l_opy_, bstack1l1l11l1l_opy_=bstack1llll11111_opy_)
  else:
    PercySDK.screenshot(driver, bstack11ll11l11l_opy_)
def bstack1lll1l11ll_opy_(driver):
  if bstack1l1l11llll_opy_.bstack11ll1l111l_opy_() is True or bstack1l1l11llll_opy_.capturing() is True:
    return
  bstack1l1l11llll_opy_.bstack11llll11ll_opy_()
  while not bstack1l1l11llll_opy_.bstack11ll1l111l_opy_():
    bstack1l1ll11ll1_opy_ = bstack1l1l11llll_opy_.bstack1ll111l11_opy_()
    bstack11l1111l11_opy_(driver, bstack1l1ll11ll1_opy_)
  bstack1l1l11llll_opy_.bstack1l11111l11_opy_()
def bstack1lllll11l1_opy_(sequence, driver_command, response = None, bstack1ll1l1ll11_opy_ = None, args = None):
    try:
      if sequence != bstack1l1_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬග"):
        return
      if percy.bstack1l11lll111_opy_() == bstack1l1_opy_ (u"ࠨࡦࡢ࡮ࡶࡩࠧඝ"):
        return
      bstack1l1ll11ll1_opy_ = bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪඞ"), None)
      for command in bstack1lll111l1_opy_:
        if command == driver_command:
          for driver in bstack1l1ll1ll1l_opy_:
            bstack1lll1l11ll_opy_(driver)
      bstack1ll1111ll1_opy_ = percy.bstack1lll11l11_opy_()
      if driver_command in bstack1l1ll111ll_opy_[bstack1ll1111ll1_opy_]:
        bstack1l1l11llll_opy_.bstack1l11lll1l_opy_(bstack1l1ll11ll1_opy_, driver_command)
    except Exception as e:
      pass
def bstack11ll1l1ll1_opy_(framework_name):
  if bstack111l11ll_opy_.get_property(bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬඟ")):
      return
  bstack111l11ll_opy_.set_property(bstack1l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡰࡳࡩࡥࡣࡢ࡮࡯ࡩࡩ࠭ච"), True)
  global bstack11lll1l1ll_opy_
  global bstack1lll11111_opy_
  global bstack1l1lllll1_opy_
  bstack11lll1l1ll_opy_ = framework_name
  logger.info(bstack1l1l11l111_opy_.format(bstack11lll1l1ll_opy_.split(bstack1l1_opy_ (u"ࠪ࠱ࠬඡ"))[0]))
  bstack1111l1111_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1ll11ll1ll_opy_:
      Service.start = bstack1lll1111l1_opy_
      Service.stop = bstack1ll11l1l11_opy_
      webdriver.Remote.get = bstack1lll1lll1_opy_
      WebDriver.close = bstack1111llll1_opy_
      WebDriver.quit = bstack1l1l11ll1l_opy_
      webdriver.Remote.__init__ = bstack1ll111ll11_opy_
      WebDriver.getAccessibilityResults = getAccessibilityResults
      WebDriver.get_accessibility_results = getAccessibilityResults
      WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
      WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
      WebDriver.performScan = perform_scan
      WebDriver.perform_scan = perform_scan
    if not bstack1ll11ll1ll_opy_:
        webdriver.Remote.__init__ = bstack11l1l1lll_opy_
    WebDriver.execute = bstack1l11l1l11l_opy_
    bstack1lll11111_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1ll11ll1ll_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1llllllll1_opy_
  except Exception as e:
    pass
  bstack11l1lll1l1_opy_()
  if not bstack1lll11111_opy_:
    bstack1l1l1lll1l_opy_(bstack1l1_opy_ (u"ࠦࡕࡧࡣ࡬ࡣࡪࡩࡸࠦ࡮ࡰࡶࠣ࡭ࡳࡹࡴࡢ࡮࡯ࡩࡩࠨජ"), bstack1lll1111ll_opy_)
  if bstack1l1l11l11l_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      RemoteConnection._11l1l111ll_opy_ = bstack11l11llll1_opy_
    except Exception as e:
      logger.error(bstack11111lll1_opy_.format(str(e)))
  if bstack111llll11_opy_():
    bstack11111ll1l_opy_(CONFIG, logger)
  if (bstack1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫඣ") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack1l11lll111_opy_() == bstack1l1_opy_ (u"ࠨࡴࡳࡷࡨࠦඤ"):
          bstack11l111111l_opy_(bstack1lllll11l1_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1111lllll_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1l1ll111l1_opy_
      except Exception as e:
        logger.warn(bstack1111ll1ll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack111l1111l_opy_
      except Exception as e:
        logger.debug(bstack11llll1l1_opy_ + str(e))
    except Exception as e:
      bstack1l1l1lll1l_opy_(e, bstack1111ll1ll_opy_)
    Output.start_test = bstack1l1ll11l11_opy_
    Output.end_test = bstack1ll1llllll_opy_
    TestStatus.__init__ = bstack11l1ll111_opy_
    QueueItem.__init__ = bstack1l1ll1l1l1_opy_
    pabot._create_items = bstack1l1ll1l11l_opy_
    try:
      from pabot import __version__ as bstack1ll1ll1ll_opy_
      if version.parse(bstack1ll1ll1ll_opy_) >= version.parse(bstack1l1_opy_ (u"ࠧ࠳࠰࠴࠹࠳࠶ࠧඥ")):
        pabot._run = bstack11l111l1l1_opy_
      elif version.parse(bstack1ll1ll1ll_opy_) >= version.parse(bstack1l1_opy_ (u"ࠨ࠴࠱࠵࠸࠴࠰ࠨඦ")):
        pabot._run = bstack1ll1l1ll1_opy_
      else:
        pabot._run = bstack1l1ll11l1_opy_
    except Exception as e:
      pabot._run = bstack1l1ll11l1_opy_
    pabot._create_command_for_execution = bstack1lll1llll1_opy_
    pabot._report_results = bstack1ll1111lll_opy_
  if bstack1l1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩට") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l1l1lll1l_opy_(e, bstack1lll11lll_opy_)
    Runner.run_hook = bstack1l1l11l1ll_opy_
    Step.run = bstack11ll1lllll_opy_
  if bstack1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪඨ") in str(framework_name).lower():
    if not bstack1ll11ll1ll_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack11l11ll1ll_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack111lll11l_opy_
      Config.getoption = bstack11l1llll11_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack11l1l1lll1_opy_
    except Exception as e:
      pass
def bstack1llll1111_opy_():
  global CONFIG
  if bstack1l1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫඩ") in CONFIG and int(CONFIG[bstack1l1_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬඪ")]) > 1:
    logger.warn(bstack1lll1lllll_opy_)
def bstack11l1lll11l_opy_(arg, bstack111ll1l1_opy_, bstack1llllll1ll_opy_=None):
  global CONFIG
  global bstack11ll1ll111_opy_
  global bstack1ll1lll11_opy_
  global bstack1ll11ll1ll_opy_
  global bstack111l11ll_opy_
  bstack1lll1llll_opy_ = bstack1l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ණ")
  if bstack111ll1l1_opy_ and isinstance(bstack111ll1l1_opy_, str):
    bstack111ll1l1_opy_ = eval(bstack111ll1l1_opy_)
  CONFIG = bstack111ll1l1_opy_[bstack1l1_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧඬ")]
  bstack11ll1ll111_opy_ = bstack111ll1l1_opy_[bstack1l1_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩත")]
  bstack1ll1lll11_opy_ = bstack111ll1l1_opy_[bstack1l1_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫථ")]
  bstack1ll11ll1ll_opy_ = bstack111ll1l1_opy_[bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ද")]
  bstack111l11ll_opy_.set_property(bstack1l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬධ"), bstack1ll11ll1ll_opy_)
  os.environ[bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧන")] = bstack1lll1llll_opy_
  os.environ[bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࠬ඲")] = json.dumps(CONFIG)
  os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡈࡖࡄࡢ࡙ࡗࡒࠧඳ")] = bstack11ll1ll111_opy_
  os.environ[bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩප")] = str(bstack1ll1lll11_opy_)
  os.environ[bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡏ࡙ࡌࡏࡎࠨඵ")] = str(True)
  if bstack11l1l11l11_opy_(arg, [bstack1l1_opy_ (u"ࠪ࠱ࡳ࠭බ"), bstack1l1_opy_ (u"ࠫ࠲࠳࡮ࡶ࡯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬභ")]) != -1:
    os.environ[bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡇࡒࡂࡎࡏࡉࡑ࠭ම")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1l1l1l11l1_opy_)
    return
  bstack1llllll111_opy_()
  global bstack1l111llll1_opy_
  global bstack1llll11111_opy_
  global bstack1ll1ll11l_opy_
  global bstack1ll11ll1l_opy_
  global bstack1ll111llll_opy_
  global bstack1l1lllll1_opy_
  global bstack1ll11llll_opy_
  arg.append(bstack1l1_opy_ (u"ࠨ࠭ࡘࠤඹ"))
  arg.append(bstack1l1_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡫࠺ࡎࡱࡧࡹࡱ࡫ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡ࡫ࡰࡴࡴࡸࡴࡦࡦ࠽ࡴࡾࡺࡥࡴࡶ࠱ࡔࡾࡺࡥࡴࡶ࡚ࡥࡷࡴࡩ࡯ࡩࠥය"))
  arg.append(bstack1l1_opy_ (u"ࠣ࠯࡚ࠦර"))
  arg.append(bstack1l1_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡦ࠼ࡗ࡬ࡪࠦࡨࡰࡱ࡮࡭ࡲࡶ࡬ࠣ඼"))
  global bstack1l111111ll_opy_
  global bstack1lll1ll1ll_opy_
  global bstack11l11l1lll_opy_
  global bstack11lllllll1_opy_
  global bstack1l1l11lll1_opy_
  global bstack1l1l1l11ll_opy_
  global bstack1ll1l11l11_opy_
  global bstack1l111111l_opy_
  global bstack1ll111l11l_opy_
  global bstack11ll1l111_opy_
  global bstack1lll1ll111_opy_
  global bstack11lll11l11_opy_
  global bstack1ll1l1llll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1l111111ll_opy_ = webdriver.Remote.__init__
    bstack1lll1ll1ll_opy_ = WebDriver.quit
    bstack1l111111l_opy_ = WebDriver.close
    bstack1ll111l11l_opy_ = WebDriver.get
    bstack11l11l1lll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack11l11l11ll_opy_(CONFIG) and bstack111111ll1_opy_():
    if bstack1lll1lll11_opy_() < version.parse(bstack1ll11l111l_opy_):
      logger.error(bstack1l1111l11_opy_.format(bstack1lll1lll11_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack11ll1l111_opy_ = RemoteConnection._11l1l111ll_opy_
      except Exception as e:
        logger.error(bstack11111lll1_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack1lll1ll111_opy_ = Config.getoption
    from _pytest import runner
    bstack11lll11l11_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack111l1l1l_opy_)
  try:
    from pytest_bdd import reporting
    bstack1ll1l1llll_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡲࠤࡷࡻ࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࡶࠫල"))
  bstack1ll1ll11l_opy_ = CONFIG.get(bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ඾"), {}).get(bstack1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ඿"))
  bstack1ll11llll_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack1ll1ll1l1l_opy_():
      bstack1llll1l11l_opy_.invoke(Events.CONNECT, bstack11ll1111ll_opy_())
    platform_index = int(os.environ.get(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ව"), bstack1l1_opy_ (u"ࠧ࠱ࠩශ")))
  else:
    bstack11ll1l1ll1_opy_(bstack11ll1ll1l1_opy_)
  os.environ[bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩෂ")] = CONFIG[bstack1l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫස")]
  os.environ[bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭හ")] = CONFIG[bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧළ")]
  os.environ[bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨෆ")] = bstack1ll11ll1ll_opy_.__str__()
  from _pytest.config import main as bstack1l1l1llll_opy_
  bstack11ll1l11ll_opy_ = []
  try:
    bstack1l1ll111l_opy_ = bstack1l1l1llll_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack11l111ll11_opy_()
    if bstack1l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶࠪ෇") in multiprocessing.current_process().__dict__.keys():
      for bstack11111l11l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11ll1l11ll_opy_.append(bstack11111l11l_opy_)
    try:
      bstack1111lll1l_opy_ = (bstack11ll1l11ll_opy_, int(bstack1l1ll111l_opy_))
      bstack1llllll1ll_opy_.append(bstack1111lll1l_opy_)
    except:
      bstack1llllll1ll_opy_.append((bstack11ll1l11ll_opy_, bstack1l1ll111l_opy_))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack11ll1l11ll_opy_.append({bstack1l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ෈"): bstack1l1_opy_ (u"ࠨࡒࡵࡳࡨ࡫ࡳࡴࠢࠪ෉") + os.environ.get(bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ්࡙ࠩ")), bstack1l1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ෋"): traceback.format_exc(), bstack1l1_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ෌"): int(os.environ.get(bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ෍")))})
    bstack1llllll1ll_opy_.append((bstack11ll1l11ll_opy_, 1))
def bstack1ll11111l1_opy_(arg):
  global bstack1lll11ll1_opy_
  bstack11ll1l1ll1_opy_(bstack1ll1l1l111_opy_)
  os.environ[bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ෎")] = str(bstack1ll1lll11_opy_)
  from behave.__main__ import main as bstack1lll11l1l_opy_
  status_code = bstack1lll11l1l_opy_(arg)
  if status_code != 0:
    bstack1lll11ll1_opy_ = status_code
def bstack11l1l1ll1l_opy_():
  logger.info(bstack1lllll1l11_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack1l1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ා"), help=bstack1l1_opy_ (u"ࠨࡉࡨࡲࡪࡸࡡࡵࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡦࡳࡳ࡬ࡩࡨࠩැ"))
  parser.add_argument(bstack1l1_opy_ (u"ࠩ࠰ࡹࠬෑ"), bstack1l1_opy_ (u"ࠪ࠱࠲ࡻࡳࡦࡴࡱࡥࡲ࡫ࠧි"), help=bstack1l1_opy_ (u"ࠫ࡞ࡵࡵࡳࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡷࡶࡩࡷࡴࡡ࡮ࡧࠪී"))
  parser.add_argument(bstack1l1_opy_ (u"ࠬ࠳࡫ࠨු"), bstack1l1_opy_ (u"࠭࠭࠮࡭ࡨࡽࠬ෕"), help=bstack1l1_opy_ (u"࡚ࠧࡱࡸࡶࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡦࡩࡣࡦࡵࡶࠤࡰ࡫ࡹࠨූ"))
  parser.add_argument(bstack1l1_opy_ (u"ࠨ࠯ࡩࠫ෗"), bstack1l1_opy_ (u"ࠩ࠰࠱࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧෘ"), help=bstack1l1_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡶࡨࡷࡹࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩෙ"))
  bstack1lll11ll11_opy_ = parser.parse_args()
  try:
    bstack1ll1l1l1l1_opy_ = bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡫ࡪࡴࡥࡳ࡫ࡦ࠲ࡾࡳ࡬࠯ࡵࡤࡱࡵࡲࡥࠨේ")
    if bstack1lll11ll11_opy_.framework and bstack1lll11ll11_opy_.framework not in (bstack1l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬෛ"), bstack1l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠹ࠧො")):
      bstack1ll1l1l1l1_opy_ = bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠰ࡼࡱࡱ࠴ࡳࡢ࡯ࡳࡰࡪ࠭ෝ")
    bstack11l1l1l11l_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1ll1l1l1l1_opy_)
    bstack111l11111_opy_ = open(bstack11l1l1l11l_opy_, bstack1l1_opy_ (u"ࠨࡴࠪෞ"))
    bstack1ll1l1l1l_opy_ = bstack111l11111_opy_.read()
    bstack111l11111_opy_.close()
    if bstack1lll11ll11_opy_.username:
      bstack1ll1l1l1l_opy_ = bstack1ll1l1l1l_opy_.replace(bstack1l1_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩෟ"), bstack1lll11ll11_opy_.username)
    if bstack1lll11ll11_opy_.key:
      bstack1ll1l1l1l_opy_ = bstack1ll1l1l1l_opy_.replace(bstack1l1_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬ෠"), bstack1lll11ll11_opy_.key)
    if bstack1lll11ll11_opy_.framework:
      bstack1ll1l1l1l_opy_ = bstack1ll1l1l1l_opy_.replace(bstack1l1_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬ෡"), bstack1lll11ll11_opy_.framework)
    file_name = bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠨ෢")
    file_path = os.path.abspath(file_name)
    bstack1l11l1lll_opy_ = open(file_path, bstack1l1_opy_ (u"࠭ࡷࠨ෣"))
    bstack1l11l1lll_opy_.write(bstack1ll1l1l1l_opy_)
    bstack1l11l1lll_opy_.close()
    logger.info(bstack1llll1ll1_opy_)
    try:
      os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩ෤")] = bstack1lll11ll11_opy_.framework if bstack1lll11ll11_opy_.framework != None else bstack1l1_opy_ (u"ࠣࠤ෥")
      config = yaml.safe_load(bstack1ll1l1l1l_opy_)
      config[bstack1l1_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ෦")] = bstack1l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠰ࡷࡪࡺࡵࡱࠩ෧")
      bstack1l1ll1ll1_opy_(bstack1l11l11ll1_opy_, config)
    except Exception as e:
      logger.debug(bstack1l1111l1l_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1l1l1lllll_opy_.format(str(e)))
def bstack1l1ll1ll1_opy_(bstack1l1l11lll_opy_, config, bstack1l1l1ll1l1_opy_={}):
  global bstack1ll11ll1ll_opy_
  global bstack1l1l1111l1_opy_
  global bstack111l11ll_opy_
  if not config:
    return
  bstack1ll11l1l1_opy_ = bstack1l111l11l1_opy_ if not bstack1ll11ll1ll_opy_ else (
    bstack111ll1l1l_opy_ if bstack1l1_opy_ (u"ࠫࡦࡶࡰࠨ෨") in config else (
        bstack1l11ll1l1_opy_ if config.get(bstack1l1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ෩")) else bstack1l1l1l1l11_opy_
    )
)
  bstack1l111ll1ll_opy_ = False
  bstack1l111lll11_opy_ = False
  if bstack1ll11ll1ll_opy_ is True:
      if bstack1l1_opy_ (u"࠭ࡡࡱࡲࠪ෪") in config:
          bstack1l111ll1ll_opy_ = True
      else:
          bstack1l111lll11_opy_ = True
  bstack1l11lll11_opy_ = bstack11l1111111_opy_.bstack11l1l11ll_opy_(config, bstack1l1l1111l1_opy_)
  data = {
    bstack1l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ෫"): config[bstack1l1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ෬")],
    bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ෭"): config[bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭෮")],
    bstack1l1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ෯"): bstack1l1l11lll_opy_,
    bstack1l1_opy_ (u"ࠬࡪࡥࡵࡧࡦࡸࡪࡪࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ෰"): os.environ.get(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ෱"), bstack1l1l1111l1_opy_),
    bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩෲ"): bstack111ll1l11_opy_,
    bstack1l1_opy_ (u"ࠨࡱࡳࡸ࡮ࡳࡡ࡭ࡡ࡫ࡹࡧࡥࡵࡳ࡮ࠪෳ"): bstack1l1ll1111_opy_(),
    bstack1l1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ෴"): {
      bstack1l1_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ෵"): str(config[bstack1l1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ෶")]) if bstack1l1_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ෷") in config else bstack1l1_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢ෸"),
      bstack1l1_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࡘࡨࡶࡸ࡯࡯࡯ࠩ෹"): sys.version,
      bstack1l1_opy_ (u"ࠨࡴࡨࡪࡪࡸࡲࡦࡴࠪ෺"): bstack11l1lll111_opy_(os.getenv(bstack1l1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠦ෻"), bstack1l1_opy_ (u"ࠥࠦ෼"))),
      bstack1l1_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪ࠭෽"): bstack1l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ෾"),
      bstack1l1_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧ෿"): bstack1ll11l1l1_opy_,
      bstack1l1_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ฀"): bstack1l11lll11_opy_,
      bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࡡࡸࡹ࡮ࡪࠧก"): os.environ[bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧข")],
      bstack1l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ฃ"): bstack1l1llll1ll_opy_(os.environ.get(bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ค"), bstack1l1l1111l1_opy_)),
      bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨฅ"): config[bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩฆ")] if config[bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪง")] else bstack1l1_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࠤจ"),
      bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫฉ"): str(config[bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬช")]) if bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ซ") in config else bstack1l1_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨฌ"),
      bstack1l1_opy_ (u"࠭࡯ࡴࠩญ"): sys.platform,
      bstack1l1_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩฎ"): socket.gethostname(),
      bstack1l1_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠪฏ"): bstack111l11ll_opy_.get_property(bstack1l1_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫฐ"))
    }
  }
  if not bstack111l11ll_opy_.get_property(bstack1l1_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡗ࡮࡭࡮ࡢ࡮ࠪฑ")) is None:
    data[bstack1l1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧฒ")][bstack1l1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࡍࡦࡶࡤࡨࡦࡺࡡࠨณ")] = {
      bstack1l1_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ด"): bstack1l1_opy_ (u"ࠧࡶࡵࡨࡶࡤࡱࡩ࡭࡮ࡨࡨࠬต"),
      bstack1l1_opy_ (u"ࠨࡵ࡬࡫ࡳࡧ࡬ࠨถ"): bstack111l11ll_opy_.get_property(bstack1l1_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡖ࡭࡬ࡴࡡ࡭ࠩท")),
      bstack1l1_opy_ (u"ࠪࡷ࡮࡭࡮ࡢ࡮ࡑࡹࡲࡨࡥࡳࠩธ"): bstack111l11ll_opy_.get_property(bstack1l1_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡓࡵࠧน"))
    }
  if bstack1l1l11lll_opy_ == bstack11ll1111l_opy_:
    data[bstack1l1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨบ")][bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡈࡵ࡮ࡧ࡫ࡪࠫป")] = bstack1lllll1l1_opy_(config)
    data[bstack1l1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪผ")][bstack1l1_opy_ (u"ࠨ࡫ࡶࡔࡪࡸࡣࡺࡃࡸࡸࡴࡋ࡮ࡢࡤ࡯ࡩࡩ࠭ฝ")] = percy.bstack11ll11lll1_opy_
    data[bstack1l1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬพ")][bstack1l1_opy_ (u"ࠪࡴࡪࡸࡣࡺࡄࡸ࡭ࡱࡪࡉࡥࠩฟ")] = percy.percy_build_id
  update(data[bstack1l1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧภ")], bstack1l1l1ll1l1_opy_)
  try:
    response = bstack11lll11l1l_opy_(bstack1l1_opy_ (u"ࠬࡖࡏࡔࡖࠪม"), bstack1ll1l1l11l_opy_(bstack1lll11ll1l_opy_), data, {
      bstack1l1_opy_ (u"࠭ࡡࡶࡶ࡫ࠫย"): (config[bstack1l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩร")], config[bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫฤ")])
    })
    if response:
      logger.debug(bstack1lllll1l1l_opy_.format(bstack1l1l11lll_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack1l111l1l1_opy_.format(str(e)))
def bstack11l1lll111_opy_(framework):
  return bstack1l1_opy_ (u"ࠤࡾࢁ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࡿࢂࠨล").format(str(framework), __version__) if framework else bstack1l1_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࡽࢀࠦฦ").format(
    __version__)
def bstack1llllll111_opy_():
  global CONFIG
  global bstack1l1l11l1l1_opy_
  if bool(CONFIG):
    return
  try:
    bstack1llll11l1_opy_()
    logger.debug(bstack1l1llllll_opy_.format(str(CONFIG)))
    bstack1l1l11l1l1_opy_ = bstack11ll11llll_opy_.bstack1ll111l1l1_opy_(CONFIG, bstack1l1l11l1l1_opy_)
    bstack1111l1111_opy_()
  except Exception as e:
    logger.error(bstack1l1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࡹࡵ࠲ࠠࡦࡴࡵࡳࡷࡀࠠࠣว") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1l1l1l111_opy_
  atexit.register(bstack1l1ll1111l_opy_)
  signal.signal(signal.SIGINT, bstack1ll111lll_opy_)
  signal.signal(signal.SIGTERM, bstack1ll111lll_opy_)
def bstack1l1l1l111_opy_(exctype, value, traceback):
  global bstack1l1ll1ll1l_opy_
  try:
    for driver in bstack1l1ll1ll1l_opy_:
      bstack1l1lll1lll_opy_(driver, bstack1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬศ"), bstack1l1_opy_ (u"ࠨࡓࡦࡵࡶ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤษ") + str(value))
  except Exception:
    pass
  logger.info(bstack1ll11111ll_opy_)
  bstack1111lll11_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1111lll11_opy_(message=bstack1l1_opy_ (u"ࠧࠨส"), bstack11111l1ll_opy_ = False):
  global CONFIG
  bstack11l1l1l1l1_opy_ = bstack1l1_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡆࡺࡦࡩࡵࡺࡩࡰࡰࠪห") if bstack11111l1ll_opy_ else bstack1l1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨฬ")
  try:
    if message:
      bstack1l1l1ll1l1_opy_ = {
        bstack11l1l1l1l1_opy_ : str(message)
      }
      bstack1l1ll1ll1_opy_(bstack11ll1111l_opy_, CONFIG, bstack1l1l1ll1l1_opy_)
    else:
      bstack1l1ll1ll1_opy_(bstack11ll1111l_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack11ll1lll1l_opy_.format(str(e)))
def bstack11lll111l_opy_(bstack1llllll11_opy_, size):
  bstack11l1111lll_opy_ = []
  while len(bstack1llllll11_opy_) > size:
    bstack1l111l1111_opy_ = bstack1llllll11_opy_[:size]
    bstack11l1111lll_opy_.append(bstack1l111l1111_opy_)
    bstack1llllll11_opy_ = bstack1llllll11_opy_[size:]
  bstack11l1111lll_opy_.append(bstack1llllll11_opy_)
  return bstack11l1111lll_opy_
def bstack1l11llllll_opy_(args):
  if bstack1l1_opy_ (u"ࠪ࠱ࡲ࠭อ") in args and bstack1l1_opy_ (u"ࠫࡵࡪࡢࠨฮ") in args:
    return True
  return False
def run_on_browserstack(bstack1l11l1ll1_opy_=None, bstack1llllll1ll_opy_=None, bstack1ll1llll11_opy_=False):
  global CONFIG
  global bstack11ll1ll111_opy_
  global bstack1ll1lll11_opy_
  global bstack1l1l1111l1_opy_
  global bstack111l11ll_opy_
  bstack1lll1llll_opy_ = bstack1l1_opy_ (u"ࠬ࠭ฯ")
  bstack11llll111_opy_(bstack1111l1ll1_opy_, logger)
  if bstack1l11l1ll1_opy_ and isinstance(bstack1l11l1ll1_opy_, str):
    bstack1l11l1ll1_opy_ = eval(bstack1l11l1ll1_opy_)
  if bstack1l11l1ll1_opy_:
    CONFIG = bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭ะ")]
    bstack11ll1ll111_opy_ = bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨั")]
    bstack1ll1lll11_opy_ = bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪา")]
    bstack111l11ll_opy_.set_property(bstack1l1_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫำ"), bstack1ll1lll11_opy_)
    bstack1lll1llll_opy_ = bstack1l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪิ")
  bstack111l11ll_opy_.set_property(bstack1l1_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭ี"), uuid4().__str__())
  logger.debug(bstack1l1_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪ࠽ࠨึ") + bstack111l11ll_opy_.get_property(bstack1l1_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨื")))
  if not bstack1ll1llll11_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1l1l1l11l1_opy_)
      return
    if sys.argv[1] == bstack1l1_opy_ (u"ࠧ࠮࠯ࡹࡩࡷࡹࡩࡰࡰุࠪ") or sys.argv[1] == bstack1l1_opy_ (u"ࠨ࠯ࡹูࠫ"):
      logger.info(bstack1l1_opy_ (u"ࠩࡅࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡒࡼࡸ࡭ࡵ࡮ࠡࡕࡇࡏࠥࡼࡻࡾฺࠩ").format(__version__))
      return
    if sys.argv[1] == bstack1l1_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩ฻"):
      bstack11l1l1ll1l_opy_()
      return
  args = sys.argv
  bstack1llllll111_opy_()
  global bstack1l111llll1_opy_
  global bstack1ll1lllll1_opy_
  global bstack1ll11llll_opy_
  global bstack1l11ll111l_opy_
  global bstack1llll11111_opy_
  global bstack1ll1ll11l_opy_
  global bstack1ll11ll1l_opy_
  global bstack1lllllll1l_opy_
  global bstack1ll111llll_opy_
  global bstack1l1lllll1_opy_
  global bstack1l1llll1l1_opy_
  bstack1ll1lllll1_opy_ = len(CONFIG.get(bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ฼"), []))
  if not bstack1lll1llll_opy_:
    if args[1] == bstack1l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ฽") or args[1] == bstack1l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠹ࠧ฾"):
      bstack1lll1llll_opy_ = bstack1l1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ฿")
      args = args[2:]
    elif args[1] == bstack1l1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧเ"):
      bstack1lll1llll_opy_ = bstack1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨแ")
      args = args[2:]
    elif args[1] == bstack1l1_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩโ"):
      bstack1lll1llll_opy_ = bstack1l1_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪใ")
      args = args[2:]
    elif args[1] == bstack1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭ไ"):
      bstack1lll1llll_opy_ = bstack1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧๅ")
      args = args[2:]
    elif args[1] == bstack1l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧๆ"):
      bstack1lll1llll_opy_ = bstack1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ็")
      args = args[2:]
    elif args[1] == bstack1l1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦ่ࠩ"):
      bstack1lll1llll_opy_ = bstack1l1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧ้ࠪ")
      args = args[2:]
    else:
      if not bstack1l1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ๊ࠧ") in CONFIG or str(CONFIG[bstack1l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ๋")]).lower() in [bstack1l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭์"), bstack1l1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠳ࠨํ")]:
        bstack1lll1llll_opy_ = bstack1l1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ๎")
        args = args[1:]
      elif str(CONFIG[bstack1l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ๏")]).lower() == bstack1l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ๐"):
        bstack1lll1llll_opy_ = bstack1l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ๑")
        args = args[1:]
      elif str(CONFIG[bstack1l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ๒")]).lower() == bstack1l1_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ๓"):
        bstack1lll1llll_opy_ = bstack1l1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭๔")
        args = args[1:]
      elif str(CONFIG[bstack1l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ๕")]).lower() == bstack1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ๖"):
        bstack1lll1llll_opy_ = bstack1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ๗")
        args = args[1:]
      elif str(CONFIG[bstack1l1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ๘")]).lower() == bstack1l1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ๙"):
        bstack1lll1llll_opy_ = bstack1l1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭๚")
        args = args[1:]
      else:
        os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩ๛")] = bstack1lll1llll_opy_
        bstack1l11ll1111_opy_(bstack111111lll_opy_)
  os.environ[bstack1l1_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩ๜")] = bstack1lll1llll_opy_
  bstack1l1l1111l1_opy_ = bstack1lll1llll_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack1lll1ll11l_opy_ = bstack1llll11l1l_opy_[bstack1l1_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕ࠯ࡅࡈࡉ࠭๝")] if bstack1lll1llll_opy_ == bstack1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ๞") and bstack111lllll11_opy_() else bstack1lll1llll_opy_
      bstack1llll1l11l_opy_.invoke(Events.bstack1ll1lll1l1_opy_, bstack1l11l111ll_opy_(
        sdk_version=__version__,
        path_config=bstack11lll11ll_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack1lll1ll11l_opy_,
        frameworks=[bstack1lll1ll11l_opy_],
        framework_versions={
          bstack1lll1ll11l_opy_: bstack1l1llll1ll_opy_(bstack1l1_opy_ (u"ࠫࡗࡵࡢࡰࡶࠪ๟") if bstack1lll1llll_opy_ in [bstack1l1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ๠"), bstack1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ๡"), bstack1l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨ๢")] else bstack1lll1llll_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack1l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠥ๣"), None):
        CONFIG[bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠦ๤")] = cli.config.get(bstack1l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠧ๥"), None)
    except Exception as e:
      bstack1llll1l11l_opy_.invoke(Events.bstack1l111llll_opy_, e.__traceback__, 1)
    if bstack1ll1lll11_opy_:
      CONFIG[bstack1l1_opy_ (u"ࠦࡦࡶࡰࠣ๦")] = cli.config[bstack1l1_opy_ (u"ࠧࡧࡰࡱࠤ๧")]
      logger.info(bstack1l1111l1ll_opy_.format(CONFIG[bstack1l1_opy_ (u"࠭ࡡࡱࡲࠪ๨")]))
  else:
    bstack1llll1l11l_opy_.clear()
  global bstack1111l11ll_opy_
  global bstack1l1l1111ll_opy_
  if bstack1l11l1ll1_opy_:
    try:
      bstack11l1l1ll11_opy_ = datetime.datetime.now()
      os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩ๩")] = bstack1lll1llll_opy_
      bstack1l1ll1ll1_opy_(bstack1l1lll11l1_opy_, CONFIG)
      cli.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠣࡪࡷࡸࡵࡀࡳࡥ࡭ࡢࡸࡪࡹࡴࡠࡣࡷࡸࡪࡳࡰࡵࡧࡧࠦ๪"), datetime.datetime.now() - bstack11l1l1ll11_opy_)
    except Exception as e:
      logger.debug(bstack11l111111_opy_.format(str(e)))
  global bstack1l111111ll_opy_
  global bstack1lll1ll1ll_opy_
  global bstack1l11l1111l_opy_
  global bstack11ll11l11_opy_
  global bstack1lll1l11l_opy_
  global bstack11ll1l1l1l_opy_
  global bstack11lllllll1_opy_
  global bstack1l1l11lll1_opy_
  global bstack1l1lllllll_opy_
  global bstack1l1l1l11ll_opy_
  global bstack1ll1l11l11_opy_
  global bstack1l111111l_opy_
  global bstack11l1l1l1ll_opy_
  global bstack1l11ll11l1_opy_
  global bstack1ll111l11l_opy_
  global bstack11ll1l111_opy_
  global bstack1lll1ll111_opy_
  global bstack11lll11l11_opy_
  global bstack11llll1lll_opy_
  global bstack1ll1l1llll_opy_
  global bstack11l11l1lll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1l111111ll_opy_ = webdriver.Remote.__init__
    bstack1lll1ll1ll_opy_ = WebDriver.quit
    bstack1l111111l_opy_ = WebDriver.close
    bstack1ll111l11l_opy_ = WebDriver.get
    bstack11l11l1lll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1111l11ll_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack1l1l111ll_opy_
    bstack1l1l1111ll_opy_ = bstack1l1l111ll_opy_()
  except Exception as e:
    pass
  try:
    global bstack1l11l1111_opy_
    from QWeb.keywords import browser
    bstack1l11l1111_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack11l11l11ll_opy_(CONFIG) and bstack111111ll1_opy_():
    if bstack1lll1lll11_opy_() < version.parse(bstack1ll11l111l_opy_):
      logger.error(bstack1l1111l11_opy_.format(bstack1lll1lll11_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack11ll1l111_opy_ = RemoteConnection._11l1l111ll_opy_
      except Exception as e:
        logger.error(bstack11111lll1_opy_.format(str(e)))
  if not CONFIG.get(bstack1l1_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫ๫"), False) and not bstack1l11l1ll1_opy_:
    logger.info(bstack1ll11l1ll_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack1l1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ๬") in CONFIG and str(CONFIG[bstack1l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ๭")]).lower() != bstack1l1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ๮"):
      bstack1l11l1l11_opy_()
    elif bstack1lll1llll_opy_ != bstack1l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭๯") or (bstack1lll1llll_opy_ == bstack1l1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ๰") and not bstack1l11l1ll1_opy_):
      bstack1l1lll11l_opy_()
  if (bstack1lll1llll_opy_ in [bstack1l1_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ๱"), bstack1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ๲"), bstack1l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫ๳")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1111lllll_opy_
        bstack11ll1l1l1l_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1111ll1ll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1lll1l11l_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack11llll1l1_opy_ + str(e))
    except Exception as e:
      bstack1l1l1lll1l_opy_(e, bstack1111ll1ll_opy_)
    if bstack1lll1llll_opy_ != bstack1l1_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬ๴"):
      bstack11l1llll1l_opy_()
    bstack1l11l1111l_opy_ = Output.start_test
    bstack11ll11l11_opy_ = Output.end_test
    bstack11lllllll1_opy_ = TestStatus.__init__
    bstack1l1lllllll_opy_ = pabot._run
    bstack1l1l1l11ll_opy_ = QueueItem.__init__
    bstack1ll1l11l11_opy_ = pabot._create_command_for_execution
    bstack11llll1lll_opy_ = pabot._report_results
  if bstack1lll1llll_opy_ == bstack1l1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ๵"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l1l1lll1l_opy_(e, bstack1lll11lll_opy_)
    bstack11l1l1l1ll_opy_ = Runner.run_hook
    bstack1l11ll11l1_opy_ = Step.run
  if bstack1lll1llll_opy_ == bstack1l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭๶"):
    try:
      from _pytest.config import Config
      bstack1lll1ll111_opy_ = Config.getoption
      from _pytest import runner
      bstack11lll11l11_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack111l1l1l_opy_)
    try:
      from pytest_bdd import reporting
      bstack1ll1l1llll_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺ࡯ࠡࡴࡸࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࡳࠨ๷"))
  try:
    framework_name = bstack1l1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ๸") if bstack1lll1llll_opy_ in [bstack1l1_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ๹"), bstack1l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ๺"), bstack1l1_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬ๻")] else bstack1111ll11l_opy_(bstack1lll1llll_opy_)
    bstack1ll111l1ll_opy_ = {
      bstack1l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪ࠭๼"): bstack1l1_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠳ࡣࡶࡥࡸࡱࡧ࡫ࡲࠨ๽") if bstack1lll1llll_opy_ == bstack1l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ๾") and bstack111lllll11_opy_() else framework_name,
      bstack1l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ๿"): bstack1l1llll1ll_opy_(framework_name),
      bstack1l1_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ຀"): __version__,
      bstack1l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡵࡴࡧࡧࠫກ"): bstack1lll1llll_opy_
    }
    if bstack1lll1llll_opy_ in bstack111ll111l_opy_:
      if bstack1ll11ll1ll_opy_ and bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫຂ") in CONFIG and CONFIG[bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ຃")] == True:
        if bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ຄ") in CONFIG:
          os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ຅")] = os.getenv(bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩຆ"), json.dumps(CONFIG[bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩງ")]))
          CONFIG[bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪຈ")].pop(bstack1l1_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩຉ"), None)
          CONFIG[bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬຊ")].pop(bstack1l1_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ຋"), None)
        bstack1ll111l1ll_opy_[bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧຌ")] = {
          bstack1l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ຍ"): bstack1l1_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫຎ"),
          bstack1l1_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫຏ"): str(bstack1lll1lll11_opy_())
        }
    if bstack1lll1llll_opy_ not in [bstack1l1_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬຐ")] and not cli.is_running():
      bstack1l1lll1ll1_opy_ = bstack1l1ll1l1_opy_.launch(CONFIG, bstack1ll111l1ll_opy_)
  except Exception as e:
    logger.debug(bstack11l11l111_opy_.format(bstack1l1_opy_ (u"࡚ࠬࡥࡴࡶࡋࡹࡧ࠭ຑ"), str(e)))
  if bstack1lll1llll_opy_ == bstack1l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ຒ"):
    bstack1ll11llll_opy_ = True
    if bstack1l11l1ll1_opy_ and bstack1ll1llll11_opy_:
      bstack1ll1ll11l_opy_ = CONFIG.get(bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫຓ"), {}).get(bstack1l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪດ"))
      bstack11ll1l1ll1_opy_(bstack11l11111ll_opy_)
    elif bstack1l11l1ll1_opy_:
      bstack1ll1ll11l_opy_ = CONFIG.get(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ຕ"), {}).get(bstack1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬຖ"))
      global bstack1l1ll1ll1l_opy_
      try:
        if bstack1l11llllll_opy_(bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧທ")]) and multiprocessing.current_process().name == bstack1l1_opy_ (u"ࠬ࠶ࠧຘ"):
          bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩນ")].remove(bstack1l1_opy_ (u"ࠧ࠮࡯ࠪບ"))
          bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫປ")].remove(bstack1l1_opy_ (u"ࠩࡳࡨࡧ࠭ຜ"))
          bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ຝ")] = bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧພ")][0]
          with open(bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨຟ")], bstack1l1_opy_ (u"࠭ࡲࠨຠ")) as f:
            file_content = f.read()
          bstack1llllll1l_opy_ = bstack1l1_opy_ (u"ࠢࠣࠤࡩࡶࡴࡳࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡳࡥ࡭ࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡁࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡧࠫࡿࢂ࠯࠻ࠡࡨࡵࡳࡲࠦࡰࡥࡤࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡔࡩࡨ࠻ࠡࡱࡪࡣࡩࡨࠠ࠾ࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡪࡥࡧࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯࠭ࡹࡥ࡭ࡨ࠯ࠤࡦࡸࡧ࠭ࠢࡷࡩࡲࡶ࡯ࡳࡣࡵࡽࠥࡃࠠ࠱ࠫ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡷࡶࡾࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡢࡴࡪࠤࡂࠦࡳࡵࡴࠫ࡭ࡳࡺࠨࡢࡴࡪ࠭࠰࠷࠰ࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡦࡺࡦࡩࡵࡺࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡥࡸࠦࡥ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡳࡥࡸࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡵࡧࡠࡦࡥࠬࡸ࡫࡬ࡧ࠮ࡤࡶ࡬࠲ࡴࡦ࡯ࡳࡳࡷࡧࡲࡺࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡐࡥࡤ࠱ࡨࡴࡥࡢࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫ࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡓࡨࡧ࠮ࠩ࠯ࡵࡨࡸࡤࡺࡲࡢࡥࡨࠬ࠮ࡢ࡮ࠣࠤࠥມ").format(str(bstack1l11l1ll1_opy_))
          bstack11l1ll1l1_opy_ = bstack1llllll1l_opy_ + file_content
          bstack11l1lllll1_opy_ = bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫຢ")] + bstack1l1_opy_ (u"ࠩࡢࡦࡸࡺࡡࡤ࡭ࡢࡸࡪࡳࡰ࠯ࡲࡼࠫຣ")
          with open(bstack11l1lllll1_opy_, bstack1l1_opy_ (u"ࠪࡻࠬ຤")):
            pass
          with open(bstack11l1lllll1_opy_, bstack1l1_opy_ (u"ࠦࡼ࠱ࠢລ")) as f:
            f.write(bstack11l1ll1l1_opy_)
          import subprocess
          process_data = subprocess.run([bstack1l1_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࠧ຦"), bstack11l1lllll1_opy_])
          if os.path.exists(bstack11l1lllll1_opy_):
            os.unlink(bstack11l1lllll1_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack1l11llllll_opy_(bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩວ")]):
            bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪຨ")].remove(bstack1l1_opy_ (u"ࠨ࠯ࡰࠫຩ"))
            bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬສ")].remove(bstack1l1_opy_ (u"ࠪࡴࡩࡨࠧຫ"))
            bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧຬ")] = bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨອ")][0]
          bstack11ll1l1ll1_opy_(bstack11l11111ll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩຮ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack1l1_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠࠩຯ")] = bstack1l1_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪະ")
          mod_globals[bstack1l1_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫັ")] = os.path.abspath(bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭າ")])
          exec(open(bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧຳ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack1l1_opy_ (u"ࠬࡉࡡࡶࡩ࡫ࡸࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠬິ").format(str(e)))
          for driver in bstack1l1ll1ll1l_opy_:
            bstack1llllll1ll_opy_.append({
              bstack1l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫີ"): bstack1l11l1ll1_opy_[bstack1l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪຶ")],
              bstack1l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧື"): str(e),
              bstack1l1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨຸ"): multiprocessing.current_process().name
            })
            bstack1l1lll1lll_opy_(driver, bstack1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦູࠪ"), bstack1l1_opy_ (u"ࠦࡘ࡫ࡳࡴ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴ຺ࠢ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1l1ll1ll1l_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack1ll1lll11_opy_, CONFIG, logger)
      bstack11ll1l1111_opy_()
      bstack1llll1111_opy_()
      bstack111ll1l1_opy_ = {
        bstack1l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨົ"): args[0],
        bstack1l1_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭ຼ"): CONFIG,
        bstack1l1_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨຽ"): bstack11ll1ll111_opy_,
        bstack1l1_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ຾"): bstack1ll1lll11_opy_
      }
      percy.bstack11l11111l_opy_()
      if bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ຿") in CONFIG:
        bstack1111ll1l_opy_ = []
        manager = multiprocessing.Manager()
        bstack11111ll1_opy_ = manager.list()
        if bstack1l11llllll_opy_(args):
          for index, platform in enumerate(CONFIG[bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ເ")]):
            if index == 0:
              bstack111ll1l1_opy_[bstack1l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧແ")] = args
            bstack1111ll1l_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack111ll1l1_opy_, bstack11111ll1_opy_)))
        else:
          for index, platform in enumerate(CONFIG[bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨໂ")]):
            bstack1111ll1l_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack111ll1l1_opy_, bstack11111ll1_opy_)))
        for t in bstack1111ll1l_opy_:
          t.start()
        for t in bstack1111ll1l_opy_:
          t.join()
        bstack1lllllll1l_opy_ = list(bstack11111ll1_opy_)
      else:
        if bstack1l11llllll_opy_(args):
          bstack111ll1l1_opy_[bstack1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩໃ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack111ll1l1_opy_,))
          test.start()
          test.join()
        else:
          bstack11ll1l1ll1_opy_(bstack11l11111ll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack1l1_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠࠩໄ")] = bstack1l1_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪ໅")
          mod_globals[bstack1l1_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫໆ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1lll1llll_opy_ == bstack1l1_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ໇") or bstack1lll1llll_opy_ == bstack1l1_opy_ (u"ࠫࡷࡵࡢࡰࡶ່ࠪ"):
    percy.init(bstack1ll1lll11_opy_, CONFIG, logger)
    percy.bstack11l11111l_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1l1l1lll1l_opy_(e, bstack1111ll1ll_opy_)
    bstack11ll1l1111_opy_()
    bstack11ll1l1ll1_opy_(bstack11l1ll1lll_opy_)
    if bstack1ll11ll1ll_opy_:
      bstack1l111ll111_opy_(bstack11l1ll1lll_opy_, args)
      if bstack1l1_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵ້ࠪ") in args:
        i = args.index(bstack1l1_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶ໊ࠫ"))
        args.pop(i)
        args.pop(i)
      if bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵ໋ࠪ") not in CONFIG:
        CONFIG[bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ໌")] = [{}]
        bstack1ll1lllll1_opy_ = 1
      if bstack1l111llll1_opy_ == 0:
        bstack1l111llll1_opy_ = 1
      args.insert(0, str(bstack1l111llll1_opy_))
      args.insert(0, str(bstack1l1_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧໍ")))
    if bstack1l1ll1l1_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack111llllll1_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack1ll1l1l1ll_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack1l1_opy_ (u"ࠥࡖࡔࡈࡏࡕࡡࡒࡔ࡙ࡏࡏࡏࡕࠥ໎"),
        ).parse_args(bstack111llllll1_opy_)
        bstack1l11ll1lll_opy_ = args.index(bstack111llllll1_opy_[0]) if len(bstack111llllll1_opy_) > 0 else len(args)
        args.insert(bstack1l11ll1lll_opy_, str(bstack1l1_opy_ (u"ࠫ࠲࠳࡬ࡪࡵࡷࡩࡳ࡫ࡲࠨ໏")))
        args.insert(bstack1l11ll1lll_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡸ࡯ࡣࡱࡷࡣࡱ࡯ࡳࡵࡧࡱࡩࡷ࠴ࡰࡺࠩ໐"))))
        if bstack1ll11l11l_opy_(os.environ.get(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࠫ໑"))) and str(os.environ.get(bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࡤ࡚ࡅࡔࡖࡖࠫ໒"), bstack1l1_opy_ (u"ࠨࡰࡸࡰࡱ࠭໓"))) != bstack1l1_opy_ (u"ࠩࡱࡹࡱࡲࠧ໔"):
          for bstack1lll1ll1l1_opy_ in bstack1ll1l1l1ll_opy_:
            args.remove(bstack1lll1ll1l1_opy_)
          bstack1l1111llll_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠧ໕")).split(bstack1l1_opy_ (u"ࠫ࠱࠭໖"))
          for bstack1ll11l1ll1_opy_ in bstack1l1111llll_opy_:
            args.append(bstack1ll11l1ll1_opy_)
      except Exception as e:
        logger.error(bstack1l1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡥࡹࡺࡡࡤࡪ࡬ࡲ࡬ࠦ࡬ࡪࡵࡷࡩࡳ࡫ࡲࠡࡨࡲࡶࠥࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࠦࡅࡳࡴࡲࡶࠥ࠳ࠠࠣ໗").format(e))
    pabot.main(args)
  elif bstack1lll1llll_opy_ == bstack1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧ໘"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1l1l1lll1l_opy_(e, bstack1111ll1ll_opy_)
    for a in args:
      if bstack1l1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝࠭໙") in a:
        bstack1llll11111_opy_ = int(a.split(bstack1l1_opy_ (u"ࠨ࠼ࠪ໚"))[1])
      if bstack1l1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭໛") in a:
        bstack1ll1ll11l_opy_ = str(a.split(bstack1l1_opy_ (u"ࠪ࠾ࠬໜ"))[1])
      if bstack1l1_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖࠫໝ") in a:
        bstack1ll11ll1l_opy_ = str(a.split(bstack1l1_opy_ (u"ࠬࡀࠧໞ"))[1])
    bstack11llll11l_opy_ = None
    if bstack1l1_opy_ (u"࠭࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠬໟ") in args:
      i = args.index(bstack1l1_opy_ (u"ࠧ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽ࠭໠"))
      args.pop(i)
      bstack11llll11l_opy_ = args.pop(i)
    if bstack11llll11l_opy_ is not None:
      global bstack1ll11l1l1l_opy_
      bstack1ll11l1l1l_opy_ = bstack11llll11l_opy_
    bstack11ll1l1ll1_opy_(bstack11l1ll1lll_opy_)
    run_cli(args)
    if bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸࠬ໡") in multiprocessing.current_process().__dict__.keys():
      for bstack11111l11l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1llllll1ll_opy_.append(bstack11111l11l_opy_)
  elif bstack1lll1llll_opy_ == bstack1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ໢"):
    bstack1l11l11l1_opy_ = bstack11l11111_opy_(args, logger, CONFIG, bstack1ll11ll1ll_opy_)
    bstack1l11l11l1_opy_.bstack1111l1l1_opy_()
    bstack11ll1l1111_opy_()
    bstack1l11ll111l_opy_ = True
    bstack1l1lllll1_opy_ = bstack1l11l11l1_opy_.bstack11l1111l_opy_()
    bstack1l11l11l1_opy_.bstack111ll1l1_opy_(bstack1ll11l11l1_opy_)
    bstack1l111l1ll1_opy_ = bstack1l11l11l1_opy_.bstack111lll11_opy_(bstack11l1lll11l_opy_, {
      bstack1l1_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫ໣"): bstack11ll1ll111_opy_,
      bstack1l1_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭໤"): bstack1ll1lll11_opy_,
      bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ໥"): bstack1ll11ll1ll_opy_
    })
    try:
      bstack11ll1l11ll_opy_, bstack11l1lll1ll_opy_ = map(list, zip(*bstack1l111l1ll1_opy_))
      bstack1ll111llll_opy_ = bstack11ll1l11ll_opy_[0]
      for status_code in bstack11l1lll1ll_opy_:
        if status_code != 0:
          bstack1l1llll1l1_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡥࡻ࡫ࠠࡦࡴࡵࡳࡷࡹࠠࡢࡰࡧࠤࡸࡺࡡࡵࡷࡶࠤࡨࡵࡤࡦ࠰ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦ࠺ࠡࡽࢀࠦ໦").format(str(e)))
  elif bstack1lll1llll_opy_ == bstack1l1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ໧"):
    try:
      from behave.__main__ import main as bstack1lll11l1l_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1l1l1lll1l_opy_(e, bstack1lll11lll_opy_)
    bstack11ll1l1111_opy_()
    bstack1l11ll111l_opy_ = True
    bstack11l11l1l_opy_ = 1
    if bstack1l1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ໨") in CONFIG:
      bstack11l11l1l_opy_ = CONFIG[bstack1l1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ໩")]
    if bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭໪") in CONFIG:
      bstack11l11l1111_opy_ = int(bstack11l11l1l_opy_) * int(len(CONFIG[bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ໫")]))
    else:
      bstack11l11l1111_opy_ = int(bstack11l11l1l_opy_)
    config = Configuration(args)
    bstack1ll1lll111_opy_ = config.paths
    if len(bstack1ll1lll111_opy_) == 0:
      import glob
      pattern = bstack1l1_opy_ (u"ࠬ࠰ࠪ࠰ࠬ࠱ࡪࡪࡧࡴࡶࡴࡨࠫ໬")
      bstack111lll1l1_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack111lll1l1_opy_)
      config = Configuration(args)
      bstack1ll1lll111_opy_ = config.paths
    bstack11111l1l_opy_ = [os.path.normpath(item) for item in bstack1ll1lll111_opy_]
    bstack1l11111111_opy_ = [os.path.normpath(item) for item in args]
    bstack1ll1111l1_opy_ = [item for item in bstack1l11111111_opy_ if item not in bstack11111l1l_opy_]
    import platform as pf
    if pf.system().lower() == bstack1l1_opy_ (u"࠭ࡷࡪࡰࡧࡳࡼࡹࠧ໭"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack11111l1l_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1llll111ll_opy_)))
                    for bstack1llll111ll_opy_ in bstack11111l1l_opy_]
    bstack111l11l1_opy_ = []
    for spec in bstack11111l1l_opy_:
      bstack1111lll1_opy_ = []
      bstack1111lll1_opy_ += bstack1ll1111l1_opy_
      bstack1111lll1_opy_.append(spec)
      bstack111l11l1_opy_.append(bstack1111lll1_opy_)
    execution_items = []
    for bstack1111lll1_opy_ in bstack111l11l1_opy_:
      if bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ໮") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ໯")]):
          item = {}
          item[bstack1l1_opy_ (u"ࠩࡤࡶ࡬࠭໰")] = bstack1l1_opy_ (u"ࠪࠤࠬ໱").join(bstack1111lll1_opy_)
          item[bstack1l1_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ໲")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack1l1_opy_ (u"ࠬࡧࡲࡨࠩ໳")] = bstack1l1_opy_ (u"࠭ࠠࠨ໴").join(bstack1111lll1_opy_)
        item[bstack1l1_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭໵")] = 0
        execution_items.append(item)
    bstack1lll11111l_opy_ = bstack11lll111l_opy_(execution_items, bstack11l11l1111_opy_)
    for execution_item in bstack1lll11111l_opy_:
      bstack1111ll1l_opy_ = []
      for item in execution_item:
        bstack1111ll1l_opy_.append(bstack1l11111ll_opy_(name=str(item[bstack1l1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ໶")]),
                                             target=bstack1ll11111l1_opy_,
                                             args=(item[bstack1l1_opy_ (u"ࠩࡤࡶ࡬࠭໷")],)))
      for t in bstack1111ll1l_opy_:
        t.start()
      for t in bstack1111ll1l_opy_:
        t.join()
  else:
    bstack1l11ll1111_opy_(bstack111111lll_opy_)
  if not bstack1l11l1ll1_opy_:
    bstack1l1111111l_opy_()
  bstack11ll11llll_opy_.bstack1l111l1ll_opy_()
def browserstack_initialize(bstack1l1111111_opy_=None):
  run_on_browserstack(bstack1l1111111_opy_, None, True)
def bstack1l1111111l_opy_():
  global CONFIG
  global bstack1l1l1111l1_opy_
  global bstack1l1llll1l1_opy_
  global bstack1lll11ll1_opy_
  global bstack111l11ll_opy_
  if cli.is_running():
    bstack1llll1l11l_opy_.invoke(Events.bstack1ll111l1l_opy_)
  if bstack1l1l1111l1_opy_ == bstack1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ໸"):
    if not cli.is_enabled(CONFIG):
      bstack1l1ll1l1_opy_.stop()
  else:
    bstack1l1ll1l1_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1llll1l1_opy_.bstack1ll11l111_opy_()
  if bstack1l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ໹") in CONFIG and str(CONFIG[bstack1l1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ໺")]).lower() != bstack1l1_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬ໻"):
    bstack1lllll1ll_opy_, bstack1l11l1l1ll_opy_ = bstack1111ll111_opy_()
  else:
    bstack1lllll1ll_opy_, bstack1l11l1l1ll_opy_ = get_build_link()
  bstack1l11111l1l_opy_(bstack1lllll1ll_opy_)
  if bstack1lllll1ll_opy_ is not None and bstack1lll1111l_opy_() != -1:
    sessions = bstack1lllll1lll_opy_(bstack1lllll1ll_opy_)
    bstack1111ll1l1_opy_(sessions, bstack1l11l1l1ll_opy_)
  if bstack1l1l1111l1_opy_ == bstack1l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ໼") and bstack1l1llll1l1_opy_ != 0:
    sys.exit(bstack1l1llll1l1_opy_)
  if bstack1l1l1111l1_opy_ == bstack1l1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ໽") and bstack1lll11ll1_opy_ != 0:
    sys.exit(bstack1lll11ll1_opy_)
def bstack1l11111l1l_opy_(new_id):
    global bstack111ll1l11_opy_
    bstack111ll1l11_opy_ = new_id
def bstack1111ll11l_opy_(bstack1l11111lll_opy_):
  if bstack1l11111lll_opy_:
    return bstack1l11111lll_opy_.capitalize()
  else:
    return bstack1l1_opy_ (u"ࠩࠪ໾")
def bstack111l11l11_opy_(bstack111lllllll_opy_):
  if bstack1l1_opy_ (u"ࠪࡲࡦࡳࡥࠨ໿") in bstack111lllllll_opy_ and bstack111lllllll_opy_[bstack1l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩༀ")] != bstack1l1_opy_ (u"ࠬ࠭༁"):
    return bstack111lllllll_opy_[bstack1l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ༂")]
  else:
    bstack1l1ll1l1ll_opy_ = bstack1l1_opy_ (u"ࠢࠣ༃")
    if bstack1l1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ༄") in bstack111lllllll_opy_ and bstack111lllllll_opy_[bstack1l1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩ༅")] != None:
      bstack1l1ll1l1ll_opy_ += bstack111lllllll_opy_[bstack1l1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪ༆")] + bstack1l1_opy_ (u"ࠦ࠱ࠦࠢ༇")
      if bstack111lllllll_opy_[bstack1l1_opy_ (u"ࠬࡵࡳࠨ༈")] == bstack1l1_opy_ (u"ࠨࡩࡰࡵࠥ༉"):
        bstack1l1ll1l1ll_opy_ += bstack1l1_opy_ (u"ࠢࡪࡑࡖࠤࠧ༊")
      bstack1l1ll1l1ll_opy_ += (bstack111lllllll_opy_[bstack1l1_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ་")] or bstack1l1_opy_ (u"ࠩࠪ༌"))
      return bstack1l1ll1l1ll_opy_
    else:
      bstack1l1ll1l1ll_opy_ += bstack1111ll11l_opy_(bstack111lllllll_opy_[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫ།")]) + bstack1l1_opy_ (u"ࠦࠥࠨ༎") + (
              bstack111lllllll_opy_[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ༏")] or bstack1l1_opy_ (u"࠭ࠧ༐")) + bstack1l1_opy_ (u"ࠢ࠭ࠢࠥ༑")
      if bstack111lllllll_opy_[bstack1l1_opy_ (u"ࠨࡱࡶࠫ༒")] == bstack1l1_opy_ (u"ࠤ࡚࡭ࡳࡪ࡯ࡸࡵࠥ༓"):
        bstack1l1ll1l1ll_opy_ += bstack1l1_opy_ (u"࡛ࠥ࡮ࡴࠠࠣ༔")
      bstack1l1ll1l1ll_opy_ += bstack111lllllll_opy_[bstack1l1_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ༕")] or bstack1l1_opy_ (u"ࠬ࠭༖")
      return bstack1l1ll1l1ll_opy_
def bstack11llll1111_opy_(bstack11111llll_opy_):
  if bstack11111llll_opy_ == bstack1l1_opy_ (u"ࠨࡤࡰࡰࡨࠦ༗"):
    return bstack1l1_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡪࡶࡪ࡫࡮࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡪࡶࡪ࡫࡮ࠣࡀࡆࡳࡲࡶ࡬ࡦࡶࡨࡨࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀ༘ࠪ")
  elif bstack11111llll_opy_ == bstack1l1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤ༙ࠣ"):
    return bstack1l1_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡷ࡫ࡤ࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡵࡩࡩࠨ࠾ࡇࡣ࡬ࡰࡪࡪ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬ༚")
  elif bstack11111llll_opy_ == bstack1l1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥ༛"):
    return bstack1l1_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡧࡳࡧࡨࡲࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡧࡳࡧࡨࡲࠧࡄࡐࡢࡵࡶࡩࡩࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫ༜")
  elif bstack11111llll_opy_ == bstack1l1_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦ༝"):
    return bstack1l1_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡴࡨࡨࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡲࡦࡦࠥࡂࡊࡸࡲࡰࡴ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ༞")
  elif bstack11111llll_opy_ == bstack1l1_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࠣ༟"):
    return bstack1l1_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࠧࡪ࡫ࡡ࠴࠴࠹࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࠩࡥࡦࡣ࠶࠶࠻ࠨ࠾ࡕ࡫ࡰࡩࡴࡻࡴ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭༠")
  elif bstack11111llll_opy_ == bstack1l1_opy_ (u"ࠤࡵࡹࡳࡴࡩ࡯ࡩࠥ༡"):
    return bstack1l1_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡨ࡬ࡢࡥ࡮࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࡨ࡬ࡢࡥ࡮ࠦࡃࡘࡵ࡯ࡰ࡬ࡲ࡬ࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫ༢")
  else:
    return bstack1l1_opy_ (u"ࠫࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡣ࡮ࡤࡧࡰࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡣ࡮ࡤࡧࡰࠨ࠾ࠨ༣") + bstack1111ll11l_opy_(
      bstack11111llll_opy_) + bstack1l1_opy_ (u"ࠬࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫ༤")
def bstack1l1l1ll1ll_opy_(session):
  return bstack1l1_opy_ (u"࠭࠼ࡵࡴࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡶࡴࡽࠢ࠿࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠣࡷࡪࡹࡳࡪࡱࡱ࠱ࡳࡧ࡭ࡦࠤࡁࡀࡦࠦࡨࡳࡧࡩࡁࠧࢁࡽࠣࠢࡷࡥࡷ࡭ࡥࡵ࠿ࠥࡣࡧࡲࡡ࡯࡭ࠥࡂࢀࢃ࠼࠰ࡣࡁࡀ࠴ࡺࡤ࠿ࡽࢀࡿࢂࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽࠱ࡷࡶࡃ࠭༥").format(
    session[bstack1l1_opy_ (u"ࠧࡱࡷࡥࡰ࡮ࡩ࡟ࡶࡴ࡯ࠫ༦")], bstack111l11l11_opy_(session), bstack11llll1111_opy_(session[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡴࡶࡤࡸࡺࡹࠧ༧")]),
    bstack11llll1111_opy_(session[bstack1l1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ༨")]),
    bstack1111ll11l_opy_(session[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫ༩")] or session[bstack1l1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫ༪")] or bstack1l1_opy_ (u"ࠬ࠭༫")) + bstack1l1_opy_ (u"ࠨࠠࠣ༬") + (session[bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ༭")] or bstack1l1_opy_ (u"ࠨࠩ༮")),
    session[bstack1l1_opy_ (u"ࠩࡲࡷࠬ༯")] + bstack1l1_opy_ (u"ࠥࠤࠧ༰") + session[bstack1l1_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ༱")], session[bstack1l1_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧ༲")] or bstack1l1_opy_ (u"࠭ࠧ༳"),
    session[bstack1l1_opy_ (u"ࠧࡤࡴࡨࡥࡹ࡫ࡤࡠࡣࡷࠫ༴")] if session[bstack1l1_opy_ (u"ࠨࡥࡵࡩࡦࡺࡥࡥࡡࡤࡸ༵ࠬ")] else bstack1l1_opy_ (u"ࠩࠪ༶"))
def bstack1111ll1l1_opy_(sessions, bstack1l11l1l1ll_opy_):
  try:
    bstack11ll111l1_opy_ = bstack1l1_opy_ (u"༷ࠥࠦ")
    if not os.path.exists(bstack11lll1lll_opy_):
      os.mkdir(bstack11lll1lll_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l1_opy_ (u"ࠫࡦࡹࡳࡦࡶࡶ࠳ࡷ࡫ࡰࡰࡴࡷ࠲࡭ࡺ࡭࡭ࠩ༸")), bstack1l1_opy_ (u"ࠬࡸ༹ࠧ")) as f:
      bstack11ll111l1_opy_ = f.read()
    bstack11ll111l1_opy_ = bstack11ll111l1_opy_.replace(bstack1l1_opy_ (u"࠭ࡻࠦࡔࡈࡗ࡚ࡒࡔࡔࡡࡆࡓ࡚ࡔࡔࠦࡿࠪ༺"), str(len(sessions)))
    bstack11ll111l1_opy_ = bstack11ll111l1_opy_.replace(bstack1l1_opy_ (u"ࠧࡼࠧࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠪࢃࠧ༻"), bstack1l11l1l1ll_opy_)
    bstack11ll111l1_opy_ = bstack11ll111l1_opy_.replace(bstack1l1_opy_ (u"ࠨࡽࠨࡆ࡚ࡏࡌࡅࡡࡑࡅࡒࡋࠥࡾࠩ༼"),
                                              sessions[0].get(bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡰࡤࡱࡪ࠭༽")) if sessions[0] else bstack1l1_opy_ (u"ࠪࠫ༾"))
    with open(os.path.join(bstack11lll1lll_opy_, bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡶࡪࡶ࡯ࡳࡶ࠱࡬ࡹࡳ࡬ࠨ༿")), bstack1l1_opy_ (u"ࠬࡽࠧཀ")) as stream:
      stream.write(bstack11ll111l1_opy_.split(bstack1l1_opy_ (u"࠭ࡻࠦࡕࡈࡗࡘࡏࡏࡏࡕࡢࡈࡆ࡚ࡁࠦࡿࠪཁ"))[0])
      for session in sessions:
        stream.write(bstack1l1l1ll1ll_opy_(session))
      stream.write(bstack11ll111l1_opy_.split(bstack1l1_opy_ (u"ࠧࡼࠧࡖࡉࡘ࡙ࡉࡐࡐࡖࡣࡉࡇࡔࡂࠧࢀࠫག"))[1])
    logger.info(bstack1l1_opy_ (u"ࠨࡉࡨࡲࡪࡸࡡࡵࡧࡧࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡦࡺ࡯࡬ࡥࠢࡤࡶࡹ࡯ࡦࡢࡥࡷࡷࠥࡧࡴࠡࡽࢀࠫགྷ").format(bstack11lll1lll_opy_));
  except Exception as e:
    logger.debug(bstack111l1l1ll_opy_.format(str(e)))
def bstack1lllll1lll_opy_(bstack1lllll1ll_opy_):
  global CONFIG
  try:
    bstack11l1l1ll11_opy_ = datetime.datetime.now()
    host = bstack1l1_opy_ (u"ࠩࡤࡴ࡮࠳ࡣ࡭ࡱࡸࡨࠬང") if bstack1l1_opy_ (u"ࠪࡥࡵࡶࠧཅ") in CONFIG else bstack1l1_opy_ (u"ࠫࡦࡶࡩࠨཆ")
    user = CONFIG[bstack1l1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧཇ")]
    key = CONFIG[bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ཈")]
    bstack1lll1l111l_opy_ = bstack1l1_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ཉ") if bstack1l1_opy_ (u"ࠨࡣࡳࡴࠬཊ") in CONFIG else (bstack1l1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ཋ") if CONFIG.get(bstack1l1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧཌ")) else bstack1l1_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ཌྷ"))
    url = bstack1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡻࡾ࠼ࡾࢁࡅࢁࡽ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࢀࢃ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡷࡪࡹࡳࡪࡱࡱࡷ࠳ࡰࡳࡰࡰࠪཎ").format(user, key, host, bstack1lll1l111l_opy_,
                                                                                bstack1lllll1ll_opy_)
    headers = {
      bstack1l1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡵࡻࡳࡩࠬཏ"): bstack1l1_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪཐ"),
    }
    proxies = bstack1lll1l1lll_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.json():
      cli.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠣࡪࡷࡸࡵࡀࡧࡦࡶࡢࡷࡪࡹࡳࡪࡱࡱࡷࡤࡲࡩࡴࡶࠥད"), datetime.datetime.now() - bstack11l1l1ll11_opy_)
      return list(map(lambda session: session[bstack1l1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠧདྷ")], response.json()))
  except Exception as e:
    logger.debug(bstack1lllll1ll1_opy_.format(str(e)))
def get_build_link():
  global CONFIG
  global bstack111ll1l11_opy_
  try:
    if bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ན") in CONFIG:
      bstack11l1l1ll11_opy_ = datetime.datetime.now()
      host = bstack1l1_opy_ (u"ࠫࡦࡶࡩ࠮ࡥ࡯ࡳࡺࡪࠧཔ") if bstack1l1_opy_ (u"ࠬࡧࡰࡱࠩཕ") in CONFIG else bstack1l1_opy_ (u"࠭ࡡࡱ࡫ࠪབ")
      user = CONFIG[bstack1l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩབྷ")]
      key = CONFIG[bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫམ")]
      bstack1lll1l111l_opy_ = bstack1l1_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨཙ") if bstack1l1_opy_ (u"ࠪࡥࡵࡶࠧཚ") in CONFIG else bstack1l1_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ཛ")
      url = bstack1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡻࡾ࠼ࡾࢁࡅࢁࡽ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࢀࢃ࠯ࡣࡷ࡬ࡰࡩࡹ࠮࡫ࡵࡲࡲࠬཛྷ").format(user, key, host, bstack1lll1l111l_opy_)
      headers = {
        bstack1l1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡵࡻࡳࡩࠬཝ"): bstack1l1_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪཞ"),
      }
      if bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪཟ") in CONFIG:
        params = {bstack1l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧའ"): CONFIG[bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ཡ")], bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧར"): CONFIG[bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧལ")]}
      else:
        params = {bstack1l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫཤ"): CONFIG[bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪཥ")]}
      proxies = bstack1lll1l1lll_opy_(CONFIG, url)
      response = requests.get(url, params=params, headers=headers, proxies=proxies)
      if response.json():
        bstack111lll1ll_opy_ = response.json()[0][bstack1l1_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡨࡵࡪ࡮ࡧࠫས")]
        if bstack111lll1ll_opy_:
          bstack1l11l1l1ll_opy_ = bstack111lll1ll_opy_[bstack1l1_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤࡡࡸࡶࡱ࠭ཧ")].split(bstack1l1_opy_ (u"ࠪࡴࡺࡨ࡬ࡪࡥ࠰ࡦࡺ࡯࡬ࡥࠩཨ"))[0] + bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡶ࠳ࠬཀྵ") + bstack111lll1ll_opy_[
            bstack1l1_opy_ (u"ࠬ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨཪ")]
          logger.info(bstack11lllllll_opy_.format(bstack1l11l1l1ll_opy_))
          bstack111ll1l11_opy_ = bstack111lll1ll_opy_[bstack1l1_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩཫ")]
          bstack11ll1l1l11_opy_ = CONFIG[bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪཬ")]
          if bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ཭") in CONFIG:
            bstack11ll1l1l11_opy_ += bstack1l1_opy_ (u"ࠩࠣࠫ཮") + CONFIG[bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ཯")]
          if bstack11ll1l1l11_opy_ != bstack111lll1ll_opy_[bstack1l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ཰")]:
            logger.debug(bstack11ll1l1ll_opy_.format(bstack111lll1ll_opy_[bstack1l1_opy_ (u"ࠬࡴࡡ࡮ࡧཱࠪ")], bstack11ll1l1l11_opy_))
          cli.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠨࡨࡵࡶࡳ࠾࡬࡫ࡴࡠࡤࡸ࡭ࡱࡪ࡟࡭࡫ࡱ࡯ིࠧ"), datetime.datetime.now() - bstack11l1l1ll11_opy_)
          return [bstack111lll1ll_opy_[bstack1l1_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦཱིࠪ")], bstack1l11l1l1ll_opy_]
    else:
      logger.warn(bstack1111111ll_opy_)
  except Exception as e:
    logger.debug(bstack1l1ll1lll1_opy_.format(str(e)))
  return [None, None]
def bstack1l1l1l1l1l_opy_(url, bstack11l11l1l1l_opy_=False):
  global CONFIG
  global bstack1lll1ll11_opy_
  if not bstack1lll1ll11_opy_:
    hostname = bstack11l1l11111_opy_(url)
    is_private = bstack1ll1l1lll1_opy_(hostname)
    if (bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰུࠬ") in CONFIG and not bstack1ll11l11l_opy_(CONFIG[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱཱུ࠭")])) and (is_private or bstack11l11l1l1l_opy_):
      bstack1lll1ll11_opy_ = hostname
def bstack11l1l11111_opy_(url):
  return urlparse(url).hostname
def bstack1ll1l1lll1_opy_(hostname):
  for bstack1l11111ll1_opy_ in bstack111ll1ll1_opy_:
    regex = re.compile(bstack1l11111ll1_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1ll1l111l1_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1llll11111_opy_
  bstack1lllll11l_opy_ = not (bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧྲྀ"), None) and bstack1l1111ll_opy_(
          threading.current_thread(), bstack1l1_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪཷ"), None))
  bstack11ll1ll11l_opy_ = getattr(driver, bstack1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬླྀ"), None) != True
  if not bstack111l1ll1_opy_.bstack1llll1llll_opy_(CONFIG, bstack1llll11111_opy_) or (bstack11ll1ll11l_opy_ and bstack1lllll11l_opy_):
    logger.warning(bstack1l1_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳ࠯ࠤཹ"))
    return {}
  try:
    logger.debug(bstack1l1_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶེࠫ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack11ll111lll_opy_.bstack111l1lll1_opy_)
    return results
  except Exception:
    logger.error(bstack1l1_opy_ (u"ࠣࡐࡲࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡽࡥࡳࡧࠣࡪࡴࡻ࡮ࡥ࠰ཻࠥ"))
    return {}
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1llll11111_opy_
  bstack1lllll11l_opy_ = not (bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹོ࠭"), None) and bstack1l1111ll_opy_(
          threading.current_thread(), bstack1l1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ཽࠩ"), None))
  bstack11ll1ll11l_opy_ = getattr(driver, bstack1l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫཾ"), None) != True
  if not bstack111l1ll1_opy_.bstack1llll1llll_opy_(CONFIG, bstack1llll11111_opy_) or (bstack11ll1ll11l_opy_ and bstack1lllll11l_opy_):
    logger.warning(bstack1l1_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡴࡷࡰࡱࡦࡸࡹ࠯ࠤཿ"))
    return {}
  try:
    logger.debug(bstack1l1_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡷࡺࡳ࡭ࡢࡴࡼྀࠫ"))
    logger.debug(perform_scan(driver))
    bstack11llllllll_opy_ = driver.execute_async_script(bstack11ll111lll_opy_.bstack1llll1l1l1_opy_)
    return bstack11llllllll_opy_
  except Exception:
    logger.error(bstack1l1_opy_ (u"ࠢࡏࡱࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡺࡳ࡭ࡢࡴࡼࠤࡼࡧࡳࠡࡨࡲࡹࡳࡪ࠮ཱྀࠣ"))
    return {}
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack1llll11111_opy_
  bstack1lllll11l_opy_ = not (bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬྂ"), None) and bstack1l1111ll_opy_(
          threading.current_thread(), bstack1l1_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨྃ"), None))
  bstack11ll1ll11l_opy_ = getattr(driver, bstack1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰ྄ࠪ"), None) != True
  if not bstack111l1ll1_opy_.bstack1llll1llll_opy_(CONFIG, bstack1llll11111_opy_) or (bstack11ll1ll11l_opy_ and bstack1lllll11l_opy_):
    logger.warning(bstack1l1_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡺࡴࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡥࡤࡲ࠳ࠨ྅"))
    return {}
  try:
    bstack11llll1l11_opy_ = driver.execute_async_script(bstack11ll111lll_opy_.perform_scan, {bstack1l1_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࠬ྆"): kwargs.get(bstack1l1_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷࡥࡣࡰ࡯ࡰࡥࡳࡪࠧ྇"), None) or bstack1l1_opy_ (u"ࠧࠨྈ")})
    return bstack11llll1l11_opy_
  except Exception:
    logger.error(bstack1l1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡷࡻ࡮ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡦࡥࡳ࠴ࠢྉ"))
    return {}