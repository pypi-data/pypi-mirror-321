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
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack1l1l1l1l11l_opy_, bstack1l1l1ll1111_opy_
import tempfile
import json
bstack11llllll111_opy_ = os.getenv(bstack1l1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡉࡢࡊࡎࡒࡅࠣᦟ"), None) or os.path.join(tempfile.gettempdir(), bstack1l1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡥࡧࡥࡹ࡬࠴࡬ࡰࡩࠥᦠ"))
bstack11lllll1l1l_opy_ = os.path.join(bstack1l1_opy_ (u"ࠤ࡯ࡳ࡬ࠨᦡ"), bstack1l1_opy_ (u"ࠪࡷࡩࡱ࠭ࡤ࡮࡬࠱ࡩ࡫ࡢࡶࡩ࠱ࡰࡴ࡭ࠧᦢ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack1l1_opy_ (u"ࠫࠪ࠮ࡡࡴࡥࡷ࡭ࡲ࡫ࠩࡴࠢ࡞ࠩ࠭ࡴࡡ࡮ࡧࠬࡷࡢࡡࠥࠩ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨ࠭ࡸࡣࠠ࠮ࠢࠨࠬࡲ࡫ࡳࡴࡣࡪࡩ࠮ࡹࠧᦣ"),
      datefmt=bstack1l1_opy_ (u"࡙ࠬࠫ࠮ࠧࡰ࠱ࠪࡪࡔࠦࡊ࠽ࠩࡒࡀࠥࡔ࡜ࠪᦤ"),
      stream=sys.stdout
    )
  return logger
def bstack1lll111ll1l_opy_():
  bstack11llllll1l1_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤࡊࡅࡃࡗࡊࠦᦥ"), bstack1l1_opy_ (u"ࠢࡧࡣ࡯ࡷࡪࠨᦦ"))
  return logging.DEBUG if bstack11llllll1l1_opy_.lower() == bstack1l1_opy_ (u"ࠣࡶࡵࡹࡪࠨᦧ") else logging.INFO
def bstack1llll11ll1l_opy_():
  global bstack11llllll111_opy_
  if os.path.exists(bstack11llllll111_opy_):
    os.remove(bstack11llllll111_opy_)
  if os.path.exists(bstack11lllll1l1l_opy_):
    os.remove(bstack11lllll1l1l_opy_)
def bstack1l111l1ll_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def bstack1ll111l1l1_opy_(config, log_level):
  bstack11lllll1lll_opy_ = log_level
  if bstack1l1_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫᦨ") in config and config[bstack1l1_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬᦩ")] in bstack1l1l1l1l11l_opy_:
    bstack11lllll1lll_opy_ = bstack1l1l1l1l11l_opy_[config[bstack1l1_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭ᦪ")]]
  if config.get(bstack1l1_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡇࡵࡵࡱࡆࡥࡵࡺࡵࡳࡧࡏࡳ࡬ࡹࠧᦫ"), False):
    logging.getLogger().setLevel(bstack11lllll1lll_opy_)
    return bstack11lllll1lll_opy_
  global bstack11llllll111_opy_
  bstack1l111l1ll_opy_()
  bstack11lllllllll_opy_ = logging.Formatter(
    fmt=bstack1l1_opy_ (u"࠭ࠥࠩࡣࡶࡧࡹ࡯࡭ࡦࠫࡶࠤࡠࠫࠨ࡯ࡣࡰࡩ࠮ࡹ࡝࡜ࠧࠫࡰࡪࡼࡥ࡭ࡰࡤࡱࡪ࠯ࡳ࡞ࠢ࠰ࠤࠪ࠮࡭ࡦࡵࡶࡥ࡬࡫ࠩࡴࠩ᦬"),
    datefmt=bstack1l1_opy_ (u"࡛ࠧࠦ࠰ࠩࡲ࠳ࠥࡥࡖࠨࡌ࠿ࠫࡍ࠻ࠧࡖ࡞ࠬ᦭"),
  )
  bstack1l11111111l_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11llllll111_opy_)
  file_handler.setFormatter(bstack11lllllllll_opy_)
  bstack1l11111111l_opy_.setFormatter(bstack11lllllllll_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack1l11111111l_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack1l1_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࠱ࡻࡪࡨࡤࡳ࡫ࡹࡩࡷ࠴ࡲࡦ࡯ࡲࡸࡪ࠴ࡲࡦ࡯ࡲࡸࡪࡥࡣࡰࡰࡱࡩࡨࡺࡩࡰࡰࠪ᦮"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack1l11111111l_opy_.setLevel(bstack11lllll1lll_opy_)
  logging.getLogger().addHandler(bstack1l11111111l_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11lllll1lll_opy_
def bstack11lllllll11_opy_(config):
  try:
    bstack1l111111111_opy_ = set(bstack1l1l1ll1111_opy_)
    bstack1l1111111l1_opy_ = bstack1l1_opy_ (u"ࠩࠪ᦯")
    with open(bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭ᦰ")) as bstack11llllllll1_opy_:
      bstack11lllllll1l_opy_ = bstack11llllllll1_opy_.read()
      bstack1l1111111l1_opy_ = re.sub(bstack1l1_opy_ (u"ࡶࠬࡤࠨ࡝ࡵ࠮࠭ࡄࠩ࠮ࠫࠦ࡟ࡲࠬᦱ"), bstack1l1_opy_ (u"ࠬ࠭ᦲ"), bstack11lllllll1l_opy_, flags=re.M)
      bstack1l1111111l1_opy_ = re.sub(
        bstack1l1_opy_ (u"ࡸࠧ࡟ࠪ࡟ࡷ࠰࠯࠿ࠩࠩᦳ") + bstack1l1_opy_ (u"ࠧࡽࠩᦴ").join(bstack1l111111111_opy_) + bstack1l1_opy_ (u"ࠨࠫ࠱࠮ࠩ࠭ᦵ"),
        bstack1l1_opy_ (u"ࡴࠪࡠ࠷ࡀࠠ࡜ࡔࡈࡈࡆࡉࡔࡆࡆࡠࠫᦶ"),
        bstack1l1111111l1_opy_, flags=re.M | re.I
      )
    def bstack11lllll1ll1_opy_(dic):
      bstack11llllll1ll_opy_ = {}
      for key, value in dic.items():
        if key in bstack1l111111111_opy_:
          bstack11llllll1ll_opy_[key] = bstack1l1_opy_ (u"ࠪ࡟ࡗࡋࡄࡂࡅࡗࡉࡉࡣࠧᦷ")
        else:
          if isinstance(value, dict):
            bstack11llllll1ll_opy_[key] = bstack11lllll1ll1_opy_(value)
          else:
            bstack11llllll1ll_opy_[key] = value
      return bstack11llllll1ll_opy_
    bstack11llllll1ll_opy_ = bstack11lllll1ll1_opy_(config)
    return {
      bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲࠧᦸ"): bstack1l1111111l1_opy_,
      bstack1l1_opy_ (u"ࠬ࡬ࡩ࡯ࡣ࡯ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨᦹ"): json.dumps(bstack11llllll1ll_opy_)
    }
  except Exception as e:
    return {}
def bstack1lll1111_opy_(config):
  global bstack11llllll111_opy_
  try:
    if config.get(bstack1l1_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨᦺ"), False):
      return
    uuid = os.getenv(bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᦻ"))
    if not uuid or uuid == bstack1l1_opy_ (u"ࠨࡰࡸࡰࡱ࠭ᦼ"):
      return
    bstack11lllll1l11_opy_ = [bstack1l1_opy_ (u"ࠩࡵࡩࡶࡻࡩࡳࡧࡰࡩࡳࡺࡳ࠯ࡶࡻࡸࠬᦽ"), bstack1l1_opy_ (u"ࠪࡔ࡮ࡶࡦࡪ࡮ࡨࠫᦾ"), bstack1l1_opy_ (u"ࠫࡵࡿࡰࡳࡱ࡭ࡩࡨࡺ࠮ࡵࡱࡰࡰࠬᦿ"), bstack11llllll111_opy_, bstack11lllll1l1l_opy_]
    bstack1l111l1ll_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠲ࡲ࡯ࡨࡵ࠰ࠫᧀ") + uuid + bstack1l1_opy_ (u"࠭࠮ࡵࡣࡵ࠲࡬ࢀࠧᧁ"))
    with tarfile.open(output_file, bstack1l1_opy_ (u"ࠢࡸ࠼ࡪࡾࠧᧂ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11lllll1l11_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11lllllll11_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11llllll11l_opy_ = data.encode()
        tarinfo.size = len(bstack11llllll11l_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11llllll11l_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack1l1_opy_ (u"ࠨࡦࡤࡸࡦ࠭ᧃ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack1l1_opy_ (u"ࠩࡵࡦࠬᧄ")), bstack1l1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰ࡺ࠰࡫ࡿ࡯ࡰࠨᧅ")),
        bstack1l1_opy_ (u"ࠫࡨࡲࡩࡦࡰࡷࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᧆ"): uuid
      }
    )
    response = requests.post(
      bstack1l1_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡵࡱ࡮ࡲࡥࡩ࠳࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡦࡰ࡮࡫࡮ࡵ࠯࡯ࡳ࡬ࡹ࠯ࡶࡲ࡯ࡳࡦࡪࠢᧇ"),
      data=multipart_data,
      headers={bstack1l1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬᧈ"): multipart_data.content_type},
      auth=(config[bstack1l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩᧉ")], config[bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ᧊")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack1l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡷࡳࡰࡴࡧࡤࠡ࡮ࡲ࡫ࡸࡀࠠࠨ᧋") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack1l1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡳࡪࡩ࡯ࡩࠣࡰࡴ࡭ࡳ࠻ࠩ᧌") + str(e))
  finally:
    try:
      bstack1llll11ll1l_opy_()
    except:
      pass