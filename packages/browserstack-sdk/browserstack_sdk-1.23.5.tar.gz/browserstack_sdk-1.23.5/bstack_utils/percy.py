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
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack1111l1lll_opy_, bstack11llll1l1l_opy_
from bstack_utils.measure import measure
class bstack1ll111l11l_opy_:
  working_dir = os.getcwd()
  bstack11l1ll11l_opy_ = False
  config = {}
  binary_path = bstack11111_opy_ (u"ࠪࠫ࿦")
  bstack1111l1l1l1_opy_ = bstack11111_opy_ (u"ࠫࠬ࿧")
  bstack1ll111l1l_opy_ = False
  bstack1111llll1l_opy_ = None
  bstack11111ll1ll_opy_ = {}
  bstack111l111ll1_opy_ = 300
  bstack1111ll1l1l_opy_ = False
  logger = None
  bstack1111l1l11l_opy_ = False
  bstack11l11l11_opy_ = False
  bstack1llll1l11l_opy_ = None
  bstack111l1111l1_opy_ = bstack11111_opy_ (u"ࠬ࠭࿨")
  bstack1111lllll1_opy_ = {
    bstack11111_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭࿩") : 1,
    bstack11111_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࠨ࿪") : 2,
    bstack11111_opy_ (u"ࠨࡧࡧ࡫ࡪ࠭࿫") : 3,
    bstack11111_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࠩ࿬") : 4
  }
  def __init__(self) -> None: pass
  def bstack111l1l111l_opy_(self):
    bstack1111llllll_opy_ = bstack11111_opy_ (u"ࠪࠫ࿭")
    bstack111l1l1l11_opy_ = sys.platform
    bstack111l1l1111_opy_ = bstack11111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ࿮")
    if re.match(bstack11111_opy_ (u"ࠧࡪࡡࡳࡹ࡬ࡲࢁࡳࡡࡤࠢࡲࡷࠧ࿯"), bstack111l1l1l11_opy_) != None:
      bstack1111llllll_opy_ = bstack111l11111l_opy_ + bstack11111_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳࡯ࡴࡺ࠱ࡾ࡮ࡶࠢ࿰")
      self.bstack111l1111l1_opy_ = bstack11111_opy_ (u"ࠧ࡮ࡣࡦࠫ࿱")
    elif re.match(bstack11111_opy_ (u"ࠣ࡯ࡶࡻ࡮ࡴࡼ࡮ࡵࡼࡷࢁࡳࡩ࡯ࡩࡺࢀࡨࡿࡧࡸ࡫ࡱࢀࡧࡩࡣࡸ࡫ࡱࢀࡼ࡯࡮ࡤࡧࡿࡩࡲࡩࡼࡸ࡫ࡱ࠷࠷ࠨ࿲"), bstack111l1l1l11_opy_) != None:
      bstack1111llllll_opy_ = bstack111l11111l_opy_ + bstack11111_opy_ (u"ࠤ࠲ࡴࡪࡸࡣࡺ࠯ࡺ࡭ࡳ࠴ࡺࡪࡲࠥ࿳")
      bstack111l1l1111_opy_ = bstack11111_opy_ (u"ࠥࡴࡪࡸࡣࡺ࠰ࡨࡼࡪࠨ࿴")
      self.bstack111l1111l1_opy_ = bstack11111_opy_ (u"ࠫࡼ࡯࡮ࠨ࿵")
    else:
      bstack1111llllll_opy_ = bstack111l11111l_opy_ + bstack11111_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡲࡩ࡯ࡷࡻ࠲ࡿ࡯ࡰࠣ࿶")
      self.bstack111l1111l1_opy_ = bstack11111_opy_ (u"࠭࡬ࡪࡰࡸࡼࠬ࿷")
    return bstack1111llllll_opy_, bstack111l1l1111_opy_
  def bstack111l1111ll_opy_(self):
    try:
      bstack1111ll111l_opy_ = [os.path.join(expanduser(bstack11111_opy_ (u"ࠢࡿࠤ࿸")), bstack11111_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ࿹")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1111ll111l_opy_:
        if(self.bstack1111l111l1_opy_(path)):
          return path
      raise bstack11111_opy_ (u"ࠤࡘࡲࡦࡲࡢࡦࠢࡷࡳࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠨ࿺")
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡦࡪࡰࡧࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠠࡱࡣࡷ࡬ࠥ࡬࡯ࡳࠢࡳࡩࡷࡩࡹࠡࡦࡲࡻࡳࡲ࡯ࡢࡦ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠ࠮ࠢࡾࢁࠧ࿻").format(e))
  def bstack1111l111l1_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  @measure(event_name=EVENTS.bstack1111lll1ll_opy_, stage=STAGE.SINGLE)
  def bstack11111lll1l_opy_(self, bstack1111llllll_opy_, bstack111l1l1111_opy_):
    try:
      bstack1111l1llll_opy_ = self.bstack111l1111ll_opy_()
      bstack1111ll11ll_opy_ = os.path.join(bstack1111l1llll_opy_, bstack11111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻ࠱ࡾ࡮ࡶࠧ࿼"))
      bstack1111ll1ll1_opy_ = os.path.join(bstack1111l1llll_opy_, bstack111l1l1111_opy_)
      if os.path.exists(bstack1111ll1ll1_opy_):
        self.logger.info(bstack11111_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡻࡾ࠮ࠣࡷࡰ࡯ࡰࡱ࡫ࡱ࡫ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠢ࿽").format(bstack1111ll1ll1_opy_))
        return bstack1111ll1ll1_opy_
      if os.path.exists(bstack1111ll11ll_opy_):
        self.logger.info(bstack11111_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࢀࡩࡱࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࢀࢃࠬࠡࡷࡱࡾ࡮ࡶࡰࡪࡰࡪࠦ࿾").format(bstack1111ll11ll_opy_))
        return self.bstack111l11l11l_opy_(bstack1111ll11ll_opy_, bstack111l1l1111_opy_)
      self.logger.info(bstack11111_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡸ࡯࡮ࠢࡾࢁࠧ࿿").format(bstack1111llllll_opy_))
      response = bstack11llll1l1l_opy_(bstack11111_opy_ (u"ࠨࡉࡈࡘࠬက"), bstack1111llllll_opy_, {}, {})
      if response.status_code == 200:
        with open(bstack1111ll11ll_opy_, bstack11111_opy_ (u"ࠩࡺࡦࠬခ")) as file:
          file.write(response.content)
        self.logger.info(bstack11111_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡡ࡯ࡦࠣࡷࡦࡼࡥࡥࠢࡤࡸࠥࢁࡽࠣဂ").format(bstack1111ll11ll_opy_))
        return self.bstack111l11l11l_opy_(bstack1111ll11ll_opy_, bstack111l1l1111_opy_)
      else:
        raise(bstack11111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡷ࡬ࡪࠦࡦࡪ࡮ࡨ࠲࡙ࠥࡴࡢࡶࡸࡷࠥࡩ࡯ࡥࡧ࠽ࠤࢀࢃࠢဃ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺ࠼ࠣࡿࢂࠨင").format(e))
  def bstack1111l1ll11_opy_(self, bstack1111llllll_opy_, bstack111l1l1111_opy_):
    try:
      retry = 2
      bstack1111ll1ll1_opy_ = None
      bstack111l11ll1l_opy_ = False
      while retry > 0:
        bstack1111ll1ll1_opy_ = self.bstack11111lll1l_opy_(bstack1111llllll_opy_, bstack111l1l1111_opy_)
        bstack111l11ll1l_opy_ = self.bstack1111ll1111_opy_(bstack1111llllll_opy_, bstack111l1l1111_opy_, bstack1111ll1ll1_opy_)
        if bstack111l11ll1l_opy_:
          break
        retry -= 1
      return bstack1111ll1ll1_opy_, bstack111l11ll1l_opy_
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡹࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡶࡡࡵࡪࠥစ").format(e))
    return bstack1111ll1ll1_opy_, False
  def bstack1111ll1111_opy_(self, bstack1111llllll_opy_, bstack111l1l1111_opy_, bstack1111ll1ll1_opy_, bstack111l11llll_opy_ = 0):
    if bstack111l11llll_opy_ > 1:
      return False
    if bstack1111ll1ll1_opy_ == None or os.path.exists(bstack1111ll1ll1_opy_) == False:
      self.logger.warn(bstack11111_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡰࡢࡶ࡫ࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠬࠡࡴࡨࡸࡷࡿࡩ࡯ࡩࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠧဆ"))
      return False
    bstack11111lllll_opy_ = bstack11111_opy_ (u"ࠣࡠ࠱࠮ࡅࡶࡥࡳࡥࡼࡠ࠴ࡩ࡬ࡪࠢ࡟ࡨ࠳ࡢࡤࠬ࠰࡟ࡨ࠰ࠨဇ")
    command = bstack11111_opy_ (u"ࠩࡾࢁࠥ࠳࠭ࡷࡧࡵࡷ࡮ࡵ࡮ࠨဈ").format(bstack1111ll1ll1_opy_)
    bstack1111lll111_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack11111lllll_opy_, bstack1111lll111_opy_) != None:
      return True
    else:
      self.logger.error(bstack11111_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡹࡩࡷࡹࡩࡰࡰࠣࡧ࡭࡫ࡣ࡬ࠢࡩࡥ࡮ࡲࡥࡥࠤဉ"))
      return False
  def bstack111l11l11l_opy_(self, bstack1111ll11ll_opy_, bstack111l1l1111_opy_):
    try:
      working_dir = os.path.dirname(bstack1111ll11ll_opy_)
      shutil.unpack_archive(bstack1111ll11ll_opy_, working_dir)
      bstack1111ll1ll1_opy_ = os.path.join(working_dir, bstack111l1l1111_opy_)
      os.chmod(bstack1111ll1ll1_opy_, 0o755)
      return bstack1111ll1ll1_opy_
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡶࡰࡽ࡭ࡵࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠧည"))
  def bstack1111lll11l_opy_(self):
    try:
      bstack11111lll11_opy_ = self.config.get(bstack11111_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫဋ"))
      bstack1111lll11l_opy_ = bstack11111lll11_opy_ or (bstack11111lll11_opy_ is None and self.bstack11l1ll11l_opy_)
      if not bstack1111lll11l_opy_ or self.config.get(bstack11111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩဌ"), None) not in bstack1111l11l1l_opy_:
        return False
      self.bstack1ll111l1l_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡪࡺࡥࡤࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤဍ").format(e))
  def bstack1111l11111_opy_(self):
    try:
      bstack1111l11111_opy_ = self.bstack1111l1ll1l_opy_
      return bstack1111l11111_opy_
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡥࡷࠤࡵ࡫ࡲࡤࡻࠣࡧࡦࡶࡴࡶࡴࡨࠤࡲࡵࡤࡦ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤဎ").format(e))
  def init(self, bstack11l1ll11l_opy_, config, logger):
    self.bstack11l1ll11l_opy_ = bstack11l1ll11l_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1111lll11l_opy_():
      return
    self.bstack11111ll1ll_opy_ = config.get(bstack11111_opy_ (u"ࠩࡳࡩࡷࡩࡹࡐࡲࡷ࡭ࡴࡴࡳࠨဏ"), {})
    self.bstack1111l1ll1l_opy_ = config.get(bstack11111_opy_ (u"ࠪࡴࡪࡸࡣࡺࡅࡤࡴࡹࡻࡲࡦࡏࡲࡨࡪ࠭တ"))
    try:
      bstack1111llllll_opy_, bstack111l1l1111_opy_ = self.bstack111l1l111l_opy_()
      bstack1111ll1ll1_opy_, bstack111l11ll1l_opy_ = self.bstack1111l1ll11_opy_(bstack1111llllll_opy_, bstack111l1l1111_opy_)
      if bstack111l11ll1l_opy_:
        self.binary_path = bstack1111ll1ll1_opy_
        thread = Thread(target=self.bstack11111llll1_opy_)
        thread.start()
      else:
        self.bstack1111l1l11l_opy_ = True
        self.logger.error(bstack11111_opy_ (u"ࠦࡎࡴࡶࡢ࡮࡬ࡨࠥࡶࡥࡳࡥࡼࠤࡵࡧࡴࡩࠢࡩࡳࡺࡴࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡓࡩࡷࡩࡹࠣထ").format(bstack1111ll1ll1_opy_))
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨဒ").format(e))
  def bstack1111l11ll1_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack11111_opy_ (u"࠭࡬ࡰࡩࠪဓ"), bstack11111_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠴࡬ࡰࡩࠪန"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack11111_opy_ (u"ࠣࡒࡸࡷ࡭࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡ࡮ࡲ࡫ࡸࠦࡡࡵࠢࡾࢁࠧပ").format(logfile))
      self.bstack1111l1l1l1_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡥࡵࠢࡳࡩࡷࡩࡹࠡ࡮ࡲ࡫ࠥࡶࡡࡵࡪ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥဖ").format(e))
  @measure(event_name=EVENTS.bstack111l1l1l1l_opy_, stage=STAGE.SINGLE)
  def bstack11111llll1_opy_(self):
    bstack1111l1lll1_opy_ = self.bstack111l11ll11_opy_()
    if bstack1111l1lll1_opy_ == None:
      self.bstack1111l1l11l_opy_ = True
      self.logger.error(bstack11111_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡷࡳࡰ࡫࡮ࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧ࠰ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾࠨဗ"))
      return False
    command_args = [bstack11111_opy_ (u"ࠦࡦࡶࡰ࠻ࡧࡻࡩࡨࡀࡳࡵࡣࡵࡸࠧဘ") if self.bstack11l1ll11l_opy_ else bstack11111_opy_ (u"ࠬ࡫ࡸࡦࡥ࠽ࡷࡹࡧࡲࡵࠩမ")]
    bstack111l1l11l1_opy_ = self.bstack111l111l11_opy_()
    if bstack111l1l11l1_opy_ != None:
      command_args.append(bstack11111_opy_ (u"ࠨ࠭ࡤࠢࡾࢁࠧယ").format(bstack111l1l11l1_opy_))
    env = os.environ.copy()
    env[bstack11111_opy_ (u"ࠢࡑࡇࡕࡇ࡞ࡥࡔࡐࡍࡈࡒࠧရ")] = bstack1111l1lll1_opy_
    env[bstack11111_opy_ (u"ࠣࡖࡋࡣࡇ࡛ࡉࡍࡆࡢ࡙࡚ࡏࡄࠣလ")] = os.environ.get(bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧဝ"), bstack11111_opy_ (u"ࠪࠫသ"))
    bstack1111l1l1ll_opy_ = [self.binary_path]
    self.bstack1111l11ll1_opy_()
    self.bstack1111llll1l_opy_ = self.bstack1111ll1lll_opy_(bstack1111l1l1ll_opy_ + command_args, env)
    self.logger.debug(bstack11111_opy_ (u"ࠦࡘࡺࡡࡳࡶ࡬ࡲ࡬ࠦࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠧဟ"))
    bstack111l11llll_opy_ = 0
    while self.bstack1111llll1l_opy_.poll() == None:
      bstack111l11l1l1_opy_ = self.bstack1111ll11l1_opy_()
      if bstack111l11l1l1_opy_:
        self.logger.debug(bstack11111_opy_ (u"ࠧࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡸࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬ࠣဠ"))
        self.bstack1111ll1l1l_opy_ = True
        return True
      bstack111l11llll_opy_ += 1
      self.logger.debug(bstack11111_opy_ (u"ࠨࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡘࡥࡵࡴࡼࠤ࠲ࠦࡻࡾࠤအ").format(bstack111l11llll_opy_))
      time.sleep(2)
    self.logger.error(bstack11111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡣࡩࡸࡪࡸࠠࡼࡿࠣࡥࡹࡺࡥ࡮ࡲࡷࡷࠧဢ").format(bstack111l11llll_opy_))
    self.bstack1111l1l11l_opy_ = True
    return False
  def bstack1111ll11l1_opy_(self, bstack111l11llll_opy_ = 0):
    if bstack111l11llll_opy_ > 10:
      return False
    try:
      bstack111l111111_opy_ = os.environ.get(bstack11111_opy_ (u"ࠨࡒࡈࡖࡈ࡟࡟ࡔࡇࡕ࡚ࡊࡘ࡟ࡂࡆࡇࡖࡊ࡙ࡓࠨဣ"), bstack11111_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱࡯ࡳࡨࡧ࡬ࡩࡱࡶࡸ࠿࠻࠳࠴࠺ࠪဤ"))
      bstack1111l111ll_opy_ = bstack111l111111_opy_ + bstack111l11l1ll_opy_
      response = requests.get(bstack1111l111ll_opy_)
      data = response.json()
      self.bstack1llll1l11l_opy_ = data.get(bstack11111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࠩဥ"), {}).get(bstack11111_opy_ (u"ࠫ࡮ࡪࠧဦ"), None)
      return True
    except:
      self.logger.debug(bstack11111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡴࡩࡣࡶࡴࡵࡩࡩࠦࡷࡩ࡫࡯ࡩࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡲࡴࡩࠢࡦ࡬ࡪࡩ࡫ࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࠥဧ"))
      return False
  def bstack111l11ll11_opy_(self):
    bstack1111lll1l1_opy_ = bstack11111_opy_ (u"࠭ࡡࡱࡲࠪဨ") if self.bstack11l1ll11l_opy_ else bstack11111_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩဩ")
    bstack1111l1l111_opy_ = bstack11111_opy_ (u"ࠣࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧࠦဪ") if self.config.get(bstack11111_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨါ")) is None else True
    bstack111l111lll_opy_ = bstack11111_opy_ (u"ࠥࡥࡵ࡯࠯ࡢࡲࡳࡣࡵ࡫ࡲࡤࡻ࠲࡫ࡪࡺ࡟ࡱࡴࡲ࡮ࡪࡩࡴࡠࡶࡲ࡯ࡪࡴ࠿࡯ࡣࡰࡩࡂࢁࡽࠧࡶࡼࡴࡪࡃࡻࡾࠨࡳࡩࡷࡩࡹ࠾ࡽࢀࠦာ").format(self.config[bstack11111_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩိ")], bstack1111lll1l1_opy_, bstack1111l1l111_opy_)
    if self.bstack1111l1ll1l_opy_:
      bstack111l111lll_opy_ += bstack11111_opy_ (u"ࠧࠬࡰࡦࡴࡦࡽࡤࡩࡡࡱࡶࡸࡶࡪࡥ࡭ࡰࡦࡨࡁࢀࢃࠢီ").format(self.bstack1111l1ll1l_opy_)
    uri = bstack1111l1lll_opy_(bstack111l111lll_opy_)
    try:
      response = bstack11llll1l1l_opy_(bstack11111_opy_ (u"࠭ࡇࡆࡖࠪု"), uri, {}, {bstack11111_opy_ (u"ࠧࡢࡷࡷ࡬ࠬူ"): (self.config[bstack11111_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪေ")], self.config[bstack11111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬဲ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1ll111l1l_opy_ = data.get(bstack11111_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫဳ"))
        self.bstack1111l1ll1l_opy_ = data.get(bstack11111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡢࡧࡦࡶࡴࡶࡴࡨࡣࡲࡵࡤࡦࠩဴ"))
        os.environ[bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࠪဵ")] = str(self.bstack1ll111l1l_opy_)
        os.environ[bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࡣࡈࡇࡐࡕࡗࡕࡉࡤࡓࡏࡅࡇࠪံ")] = str(self.bstack1111l1ll1l_opy_)
        if bstack1111l1l111_opy_ == bstack11111_opy_ (u"ࠢࡶࡰࡧࡩ࡫࡯࡮ࡦࡦ့ࠥ") and str(self.bstack1ll111l1l_opy_).lower() == bstack11111_opy_ (u"ࠣࡶࡵࡹࡪࠨး"):
          self.bstack11l11l11_opy_ = True
        if bstack11111_opy_ (u"ࠤࡷࡳࡰ࡫࡮္ࠣ") in data:
          return data[bstack11111_opy_ (u"ࠥࡸࡴࡱࡥ࡯ࠤ်")]
        else:
          raise bstack11111_opy_ (u"࡙ࠫࡵ࡫ࡦࡰࠣࡒࡴࡺࠠࡇࡱࡸࡲࡩࠦ࠭ࠡࡽࢀࠫျ").format(data)
      else:
        raise bstack11111_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡱࡧࡵࡧࡾࠦࡴࡰ࡭ࡨࡲ࠱ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡵࡷࡥࡹࡻࡳࠡ࠯ࠣࡿࢂ࠲ࠠࡓࡧࡶࡴࡴࡴࡳࡦࠢࡅࡳࡩࡿࠠ࠮ࠢࡾࢁࠧြ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡱࡧࡵࡧࡾࠦࡰࡳࡱ࡭ࡩࡨࡺࠢွ").format(e))
  def bstack111l111l11_opy_(self):
    bstack111l1l11ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠢࡱࡧࡵࡧࡾࡉ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠥှ"))
    try:
      if bstack11111_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩဿ") not in self.bstack11111ll1ll_opy_:
        self.bstack11111ll1ll_opy_[bstack11111_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪ၀")] = 2
      with open(bstack111l1l11ll_opy_, bstack11111_opy_ (u"ࠪࡻࠬ၁")) as fp:
        json.dump(self.bstack11111ll1ll_opy_, fp)
      return bstack111l1l11ll_opy_
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡤࡴࡨࡥࡹ࡫ࠠࡱࡧࡵࡧࡾࠦࡣࡰࡰࡩ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦ၂").format(e))
  def bstack1111ll1lll_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack111l1111l1_opy_ == bstack11111_opy_ (u"ࠬࡽࡩ࡯ࠩ၃"):
        bstack111l11l111_opy_ = [bstack11111_opy_ (u"࠭ࡣ࡮ࡦ࠱ࡩࡽ࡫ࠧ၄"), bstack11111_opy_ (u"ࠧ࠰ࡥࠪ၅")]
        cmd = bstack111l11l111_opy_ + cmd
      cmd = bstack11111_opy_ (u"ࠨࠢࠪ၆").join(cmd)
      self.logger.debug(bstack11111_opy_ (u"ࠤࡕࡹࡳࡴࡩ࡯ࡩࠣࡿࢂࠨ၇").format(cmd))
      with open(self.bstack1111l1l1l1_opy_, bstack11111_opy_ (u"ࠥࡥࠧ၈")) as bstack1111l11lll_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1111l11lll_opy_, text=True, stderr=bstack1111l11lll_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1111l1l11l_opy_ = True
      self.logger.error(bstack11111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽࠥࡽࡩࡵࡪࠣࡧࡲࡪࠠ࠮ࠢࡾࢁ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࡿࢂࠨ၉").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1111ll1l1l_opy_:
        self.logger.info(bstack11111_opy_ (u"࡙ࠧࡴࡰࡲࡳ࡭ࡳ࡭ࠠࡑࡧࡵࡧࡾࠨ၊"))
        cmd = [self.binary_path, bstack11111_opy_ (u"ࠨࡥࡹࡧࡦ࠾ࡸࡺ࡯ࡱࠤ။")]
        self.bstack1111ll1lll_opy_(cmd)
        self.bstack1111ll1l1l_opy_ = False
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡵࡰࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡺ࡭ࡹ࡮ࠠࡤࡱࡰࡱࡦࡴࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠢ၌").format(cmd, e))
  def bstack1lllll11l1_opy_(self):
    if not self.bstack1ll111l1l_opy_:
      return
    try:
      bstack1111llll11_opy_ = 0
      while not self.bstack1111ll1l1l_opy_ and bstack1111llll11_opy_ < self.bstack111l111ll1_opy_:
        if self.bstack1111l1l11l_opy_:
          self.logger.info(bstack11111_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡴࡧࡷࡹࡵࠦࡦࡢ࡫࡯ࡩࡩࠨ၍"))
          return
        time.sleep(1)
        bstack1111llll11_opy_ += 1
      os.environ[bstack11111_opy_ (u"ࠩࡓࡉࡗࡉ࡙ࡠࡄࡈࡗ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࠨ၎")] = str(self.bstack1111l11l11_opy_())
      self.logger.info(bstack11111_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡶࡩࡹࡻࡰࠡࡥࡲࡱࡵࡲࡥࡵࡧࡧࠦ၏"))
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡧࡷࡹࡵࠦࡰࡦࡴࡦࡽ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧၐ").format(e))
  def bstack1111l11l11_opy_(self):
    if self.bstack11l1ll11l_opy_:
      return
    try:
      bstack111l111l1l_opy_ = [platform[bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪၑ")].lower() for platform in self.config.get(bstack11111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩၒ"), [])]
      bstack1111l1111l_opy_ = sys.maxsize
      bstack111l11lll1_opy_ = bstack11111_opy_ (u"ࠧࠨၓ")
      for browser in bstack111l111l1l_opy_:
        if browser in self.bstack1111lllll1_opy_:
          bstack1111ll1l11_opy_ = self.bstack1111lllll1_opy_[browser]
        if bstack1111ll1l11_opy_ < bstack1111l1111l_opy_:
          bstack1111l1111l_opy_ = bstack1111ll1l11_opy_
          bstack111l11lll1_opy_ = browser
      return bstack111l11lll1_opy_
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡥࡩࡸࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤၔ").format(e))
  @classmethod
  def bstack1111llll_opy_(self):
    return os.getenv(bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟ࠧၕ"), bstack11111_opy_ (u"ࠪࡊࡦࡲࡳࡦࠩၖ")).lower()
  @classmethod
  def bstack111l1111l_opy_(self):
    return os.getenv(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࡡࡆࡅࡕ࡚ࡕࡓࡇࡢࡑࡔࡊࡅࠨၗ"), bstack11111_opy_ (u"ࠬ࠭ၘ"))