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
import sys
import logging
import tarfile
import io
import os
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack1lllll11l11_opy_, bstack1llll1lll11_opy_
import tempfile
import json
bstack1ll1ll1l11l_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡦࡨࡦࡺ࡭࠮࡭ࡱࡪࠫᙋ"))
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack11111_opy_ (u"ࠪࡠࡳࠫࠨࡢࡵࡦࡸ࡮ࡳࡥࠪࡵࠣ࡟ࠪ࠮࡮ࡢ࡯ࡨ࠭ࡸࡣ࡛ࠦࠪ࡯ࡩࡻ࡫࡬࡯ࡣࡰࡩ࠮ࡹ࡝ࠡ࠯ࠣࠩ࠭ࡳࡥࡴࡵࡤ࡫ࡪ࠯ࡳࠨᙌ"),
      datefmt=bstack11111_opy_ (u"ࠫࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ᙍ"),
      stream=sys.stdout
    )
  return logger
def bstack1ll1ll11111_opy_():
  global bstack1ll1ll1l11l_opy_
  if os.path.exists(bstack1ll1ll1l11l_opy_):
    os.remove(bstack1ll1ll1l11l_opy_)
def bstack1l111ll11l_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def bstack1l11l11l11_opy_(config, log_level):
  bstack1ll1ll11l1l_opy_ = log_level
  if bstack11111_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧᙎ") in config and config[bstack11111_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨᙏ")] in bstack1lllll11l11_opy_:
    bstack1ll1ll11l1l_opy_ = bstack1lllll11l11_opy_[config[bstack11111_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩᙐ")]]
  if config.get(bstack11111_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡃࡸࡸࡴࡉࡡࡱࡶࡸࡶࡪࡒ࡯ࡨࡵࠪᙑ"), False):
    logging.getLogger().setLevel(bstack1ll1ll11l1l_opy_)
    return bstack1ll1ll11l1l_opy_
  global bstack1ll1ll1l11l_opy_
  bstack1l111ll11l_opy_()
  bstack1ll1ll1111l_opy_ = logging.Formatter(
    fmt=bstack11111_opy_ (u"ࠩ࡟ࡲࠪ࠮ࡡࡴࡥࡷ࡭ࡲ࡫ࠩࡴࠢ࡞ࠩ࠭ࡴࡡ࡮ࡧࠬࡷࡢࡡࠥࠩ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨ࠭ࡸࡣࠠ࠮ࠢࠨࠬࡲ࡫ࡳࡴࡣࡪࡩ࠮ࡹࠧᙒ"),
    datefmt=bstack11111_opy_ (u"ࠪࠩࡍࡀࠥࡎ࠼ࠨࡗࠬᙓ")
  )
  bstack1ll1ll1l111_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack1ll1ll1l11l_opy_)
  file_handler.setFormatter(bstack1ll1ll1111l_opy_)
  bstack1ll1ll1l111_opy_.setFormatter(bstack1ll1ll1111l_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack1ll1ll1l111_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack11111_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳ࠰ࡵࡩࡲࡵࡴࡦ࠰ࡵࡩࡲࡵࡴࡦࡡࡦࡳࡳࡴࡥࡤࡶ࡬ࡳࡳ࠭ᙔ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack1ll1ll1l111_opy_.setLevel(bstack1ll1ll11l1l_opy_)
  logging.getLogger().addHandler(bstack1ll1ll1l111_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack1ll1ll11l1l_opy_
def bstack1ll1ll11ll1_opy_(config):
  try:
    bstack1ll1ll11l11_opy_ = set(bstack1llll1lll11_opy_)
    bstack1ll1ll1l1l1_opy_ = bstack11111_opy_ (u"ࠬ࠭ᙕ")
    with open(bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩᙖ")) as bstack1ll1ll111ll_opy_:
      bstack1ll1l1llll1_opy_ = bstack1ll1ll111ll_opy_.read()
      bstack1ll1ll1l1l1_opy_ = re.sub(bstack11111_opy_ (u"ࡲࠨࡠࠫࡠࡸ࠱ࠩࡀࠥ࠱࠮ࠩࡢ࡮ࠨᙗ"), bstack11111_opy_ (u"ࠨࠩᙘ"), bstack1ll1l1llll1_opy_, flags=re.M)
      bstack1ll1ll1l1l1_opy_ = re.sub(
        bstack11111_opy_ (u"ࡴࠪࡢ࠭ࡢࡳࠬࠫࡂࠬࠬᙙ") + bstack11111_opy_ (u"ࠪࢀࠬᙚ").join(bstack1ll1ll11l11_opy_) + bstack11111_opy_ (u"ࠫ࠮࠴ࠪࠥࠩᙛ"),
        bstack11111_opy_ (u"ࡷ࠭࡜࠳࠼ࠣ࡟ࡗࡋࡄࡂࡅࡗࡉࡉࡣࠧᙜ"),
        bstack1ll1ll1l1l1_opy_, flags=re.M | re.I
      )
    def bstack1ll1l1lllll_opy_(dic):
      bstack1ll1ll111l1_opy_ = {}
      for key, value in dic.items():
        if key in bstack1ll1ll11l11_opy_:
          bstack1ll1ll111l1_opy_[key] = bstack11111_opy_ (u"࡛࠭ࡓࡇࡇࡅࡈ࡚ࡅࡅ࡟ࠪᙝ")
        else:
          if isinstance(value, dict):
            bstack1ll1ll111l1_opy_[key] = bstack1ll1l1lllll_opy_(value)
          else:
            bstack1ll1ll111l1_opy_[key] = value
      return bstack1ll1ll111l1_opy_
    bstack1ll1ll111l1_opy_ = bstack1ll1l1lllll_opy_(config)
    return {
      bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪᙞ"): bstack1ll1ll1l1l1_opy_,
      bstack11111_opy_ (u"ࠨࡨ࡬ࡲࡦࡲࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫᙟ"): json.dumps(bstack1ll1ll111l1_opy_)
    }
  except Exception as e:
    return {}
def bstack11lll1l111_opy_(config):
  global bstack1ll1ll1l11l_opy_
  try:
    if config.get(bstack11111_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫᙠ"), False):
      return
    uuid = os.getenv(bstack11111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᙡ"))
    if not uuid or uuid == bstack11111_opy_ (u"ࠫࡳࡻ࡬࡭ࠩᙢ"):
      return
    bstack1ll1ll11lll_opy_ = [bstack11111_opy_ (u"ࠬࡸࡥࡲࡷ࡬ࡶࡪࡳࡥ࡯ࡶࡶ࠲ࡹࡾࡴࠨᙣ"), bstack11111_opy_ (u"࠭ࡐࡪࡲࡩ࡭ࡱ࡫ࠧᙤ"), bstack11111_opy_ (u"ࠧࡱࡻࡳࡶࡴࡰࡥࡤࡶ࠱ࡸࡴࡳ࡬ࠨᙥ"), bstack1ll1ll1l11l_opy_]
    bstack1l111ll11l_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠮࡮ࡲ࡫ࡸ࠳ࠧᙦ") + uuid + bstack11111_opy_ (u"ࠩ࠱ࡸࡦࡸ࠮ࡨࡼࠪᙧ"))
    with tarfile.open(output_file, bstack11111_opy_ (u"ࠥࡻ࠿࡭ࡺࠣᙨ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack1ll1ll11lll_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack1ll1ll11ll1_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack1ll1ll1l1ll_opy_ = data.encode()
        tarinfo.size = len(bstack1ll1ll1l1ll_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack1ll1ll1l1ll_opy_))
    bstack1l11ll11l_opy_ = MultipartEncoder(
      fields= {
        bstack11111_opy_ (u"ࠫࡩࡧࡴࡢࠩᙩ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack11111_opy_ (u"ࠬࡸࡢࠨᙪ")), bstack11111_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳ࡽ࠳ࡧࡻ࡫ࡳࠫᙫ")),
        bstack11111_opy_ (u"ࠧࡤ࡮࡬ࡩࡳࡺࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩᙬ"): uuid
      }
    )
    response = requests.post(
      bstack11111_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࡸࡴࡱࡵࡡࡥ࠯ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡩ࡬ࡪࡧࡱࡸ࠲ࡲ࡯ࡨࡵ࠲ࡹࡵࡲ࡯ࡢࡦࠥ᙭"),
      data=bstack1l11ll11l_opy_,
      headers={bstack11111_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨ᙮"): bstack1l11ll11l_opy_.content_type},
      auth=(config[bstack11111_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᙯ")], config[bstack11111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᙰ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack11111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡺࡶ࡬ࡰࡣࡧࠤࡱࡵࡧࡴ࠼ࠣࠫᙱ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack11111_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡥ࡯ࡦ࡬ࡲ࡬ࠦ࡬ࡰࡩࡶ࠾ࠬᙲ") + str(e))
  finally:
    try:
      bstack1ll1ll11111_opy_()
    except:
      pass