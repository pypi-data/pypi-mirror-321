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
from bstack_utils.helper import bstack1ll1l1l11l_opy_, bstack11lll11l1l_opy_
class bstack11ll1lll11_opy_:
  working_dir = os.getcwd()
  bstack1l1111ll1_opy_ = False
  config = {}
  binary_path = bstack1l1_opy_ (u"ࠫࠬᨌ")
  bstack11lll1l1lll_opy_ = bstack1l1_opy_ (u"ࠬ࠭ᨍ")
  bstack1l1l11llll_opy_ = False
  bstack11ll1ll1ll1_opy_ = None
  bstack11lll1111l1_opy_ = {}
  bstack11ll1ll11l1_opy_ = 300
  bstack11lll1l11ll_opy_ = False
  logger = None
  bstack11ll1lllll1_opy_ = False
  bstack11ll11lll1_opy_ = False
  percy_build_id = None
  bstack11lll1l1l11_opy_ = bstack1l1_opy_ (u"࠭ࠧᨎ")
  bstack11lll11111l_opy_ = {
    bstack1l1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧᨏ") : 1,
    bstack1l1_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࠩᨐ") : 2,
    bstack1l1_opy_ (u"ࠩࡨࡨ࡬࡫ࠧᨑ") : 3,
    bstack1l1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪᨒ") : 4
  }
  def __init__(self) -> None: pass
  def bstack11ll1lll1l1_opy_(self):
    bstack11lll1ll1l1_opy_ = bstack1l1_opy_ (u"ࠫࠬᨓ")
    bstack11lll111111_opy_ = sys.platform
    bstack11lll1lll11_opy_ = bstack1l1_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫᨔ")
    if re.match(bstack1l1_opy_ (u"ࠨࡤࡢࡴࡺ࡭ࡳࢂ࡭ࡢࡥࠣࡳࡸࠨᨕ"), bstack11lll111111_opy_) != None:
      bstack11lll1ll1l1_opy_ = bstack1l1l1ll11ll_opy_ + bstack1l1_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠭ࡰࡵࡻ࠲ࡿ࡯ࡰࠣᨖ")
      self.bstack11lll1l1l11_opy_ = bstack1l1_opy_ (u"ࠨ࡯ࡤࡧࠬᨗ")
    elif re.match(bstack1l1_opy_ (u"ࠤࡰࡷࡼ࡯࡮ࡽ࡯ࡶࡽࡸࢂ࡭ࡪࡰࡪࡻࢁࡩࡹࡨࡹ࡬ࡲࢁࡨࡣࡤࡹ࡬ࡲࢁࡽࡩ࡯ࡥࡨࢀࡪࡳࡣࡽࡹ࡬ࡲ࠸࠸ᨘࠢ"), bstack11lll111111_opy_) != None:
      bstack11lll1ll1l1_opy_ = bstack1l1l1ll11ll_opy_ + bstack1l1_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡻ࡮ࡴ࠮ࡻ࡫ࡳࠦᨙ")
      bstack11lll1lll11_opy_ = bstack1l1_opy_ (u"ࠦࡵ࡫ࡲࡤࡻ࠱ࡩࡽ࡫ࠢᨚ")
      self.bstack11lll1l1l11_opy_ = bstack1l1_opy_ (u"ࠬࡽࡩ࡯ࠩᨛ")
    else:
      bstack11lll1ll1l1_opy_ = bstack1l1l1ll11ll_opy_ + bstack1l1_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳࡬ࡪࡰࡸࡼ࠳ࢀࡩࡱࠤ᨜")
      self.bstack11lll1l1l11_opy_ = bstack1l1_opy_ (u"ࠧ࡭࡫ࡱࡹࡽ࠭᨝")
    return bstack11lll1ll1l1_opy_, bstack11lll1lll11_opy_
  def bstack11lll1llll1_opy_(self):
    try:
      bstack11llll1111l_opy_ = [os.path.join(expanduser(bstack1l1_opy_ (u"ࠣࢀࠥ᨞")), bstack1l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ᨟")), self.working_dir, tempfile.gettempdir()]
      for path in bstack11llll1111l_opy_:
        if(self.bstack11lll11l1l1_opy_(path)):
          return path
      raise bstack1l1_opy_ (u"࡙ࠥࡳࡧ࡬ࡣࡧࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠢᨠ")
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡲࡤࡸ࡭ࠦࡦࡰࡴࠣࡴࡪࡸࡣࡺࠢࡧࡳࡼࡴ࡬ࡰࡣࡧ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࠯ࠣࡿࢂࠨᨡ").format(e))
  def bstack11lll11l1l1_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack11lll1l1ll1_opy_(self, bstack11lll1ll1l1_opy_, bstack11lll1lll11_opy_):
    try:
      bstack11lll11lll1_opy_ = self.bstack11lll1llll1_opy_()
      bstack11ll1llll11_opy_ = os.path.join(bstack11lll11lll1_opy_, bstack1l1_opy_ (u"ࠬࡶࡥࡳࡥࡼ࠲ࡿ࡯ࡰࠨᨢ"))
      bstack11ll1lll111_opy_ = os.path.join(bstack11lll11lll1_opy_, bstack11lll1lll11_opy_)
      if os.path.exists(bstack11ll1lll111_opy_):
        self.logger.info(bstack1l1_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡼࡿ࠯ࠤࡸࡱࡩࡱࡲ࡬ࡲ࡬ࠦࡤࡰࡹࡱࡰࡴࡧࡤࠣᨣ").format(bstack11ll1lll111_opy_))
        return bstack11ll1lll111_opy_
      if os.path.exists(bstack11ll1llll11_opy_):
        self.logger.info(bstack1l1_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡺࡪࡲࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࢁࡽ࠭ࠢࡸࡲࡿ࡯ࡰࡱ࡫ࡱ࡫ࠧᨤ").format(bstack11ll1llll11_opy_))
        return self.bstack11lll111l11_opy_(bstack11ll1llll11_opy_, bstack11lll1lll11_opy_)
      self.logger.info(bstack1l1_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥ࡬ࡲࡰ࡯ࠣࡿࢂࠨᨥ").format(bstack11lll1ll1l1_opy_))
      response = bstack11lll11l1l_opy_(bstack1l1_opy_ (u"ࠩࡊࡉ࡙࠭ᨦ"), bstack11lll1ll1l1_opy_, {}, {})
      if response.status_code == 200:
        with open(bstack11ll1llll11_opy_, bstack1l1_opy_ (u"ࠪࡻࡧ࠭ᨧ")) as file:
          file.write(response.content)
        self.logger.info(bstack1l1_opy_ (u"ࠦࡉࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡢࡰࡧࠤࡸࡧࡶࡦࡦࠣࡥࡹࠦࡻࡾࠤᨨ").format(bstack11ll1llll11_opy_))
        return self.bstack11lll111l11_opy_(bstack11ll1llll11_opy_, bstack11lll1lll11_opy_)
      else:
        raise(bstack1l1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠣࡸ࡭࡫ࠠࡧ࡫࡯ࡩ࠳ࠦࡓࡵࡣࡷࡹࡸࠦࡣࡰࡦࡨ࠾ࠥࢁࡽࠣᨩ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻ࠽ࠤࢀࢃࠢᨪ").format(e))
  def bstack11lll11l1ll_opy_(self, bstack11lll1ll1l1_opy_, bstack11lll1lll11_opy_):
    try:
      retry = 2
      bstack11ll1lll111_opy_ = None
      bstack11lll11ll1l_opy_ = False
      while retry > 0:
        bstack11ll1lll111_opy_ = self.bstack11lll1l1ll1_opy_(bstack11lll1ll1l1_opy_, bstack11lll1lll11_opy_)
        bstack11lll11ll1l_opy_ = self.bstack11lll111l1l_opy_(bstack11lll1ll1l1_opy_, bstack11lll1lll11_opy_, bstack11ll1lll111_opy_)
        if bstack11lll11ll1l_opy_:
          break
        retry -= 1
      return bstack11ll1lll111_opy_, bstack11lll11ll1l_opy_
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣ࡫ࡪࡺࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡰࡢࡶ࡫ࠦᨫ").format(e))
    return bstack11ll1lll111_opy_, False
  def bstack11lll111l1l_opy_(self, bstack11lll1ll1l1_opy_, bstack11lll1lll11_opy_, bstack11ll1lll111_opy_, bstack11lll1ll11l_opy_ = 0):
    if bstack11lll1ll11l_opy_ > 1:
      return False
    if bstack11ll1lll111_opy_ == None or os.path.exists(bstack11ll1lll111_opy_) == False:
      self.logger.warn(bstack1l1_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡱࡣࡷ࡬ࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤ࠭ࠢࡵࡩࡹࡸࡹࡪࡰࡪࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠨᨬ"))
      return False
    bstack11lll1ll111_opy_ = bstack1l1_opy_ (u"ࠤࡡ࠲࠯ࡆࡰࡦࡴࡦࡽࡡ࠵ࡣ࡭࡫ࠣࡠࡩ࠴࡜ࡥ࠭࠱ࡠࡩ࠱ࠢᨭ")
    command = bstack1l1_opy_ (u"ࠪࡿࢂࠦ࠭࠮ࡸࡨࡶࡸ࡯࡯࡯ࠩᨮ").format(bstack11ll1lll111_opy_)
    bstack11lll1ll1ll_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack11lll1ll111_opy_, bstack11lll1ll1ll_opy_) != None:
      return True
    else:
      self.logger.error(bstack1l1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡺࡪࡸࡳࡪࡱࡱࠤࡨ࡮ࡥࡤ࡭ࠣࡪࡦ࡯࡬ࡦࡦࠥᨯ"))
      return False
  def bstack11lll111l11_opy_(self, bstack11ll1llll11_opy_, bstack11lll1lll11_opy_):
    try:
      working_dir = os.path.dirname(bstack11ll1llll11_opy_)
      shutil.unpack_archive(bstack11ll1llll11_opy_, working_dir)
      bstack11ll1lll111_opy_ = os.path.join(working_dir, bstack11lll1lll11_opy_)
      os.chmod(bstack11ll1lll111_opy_, 0o755)
      return bstack11ll1lll111_opy_
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡷࡱࡾ࡮ࡶࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠨᨰ"))
  def bstack11ll1ll1l11_opy_(self):
    try:
      bstack11ll1llllll_opy_ = self.config.get(bstack1l1_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬᨱ"))
      bstack11ll1ll1l11_opy_ = bstack11ll1llllll_opy_ or (bstack11ll1llllll_opy_ is None and self.bstack1l1111ll1_opy_)
      if not bstack11ll1ll1l11_opy_ or self.config.get(bstack1l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪᨲ"), None) not in bstack1l1l1l11ll1_opy_:
        return False
      self.bstack1l1l11llll_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡥࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᨳ").format(e))
  def bstack11ll1l1llll_opy_(self):
    try:
      bstack11ll1l1llll_opy_ = self.percy_capture_mode
      return bstack11ll1l1llll_opy_
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡦࡸࠥࡶࡥࡳࡥࡼࠤࡨࡧࡰࡵࡷࡵࡩࠥࡳ࡯ࡥࡧ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᨴ").format(e))
  def init(self, bstack1l1111ll1_opy_, config, logger):
    self.bstack1l1111ll1_opy_ = bstack1l1111ll1_opy_
    self.config = config
    self.logger = logger
    if not self.bstack11ll1ll1l11_opy_():
      return
    self.bstack11lll1111l1_opy_ = config.get(bstack1l1_opy_ (u"ࠪࡴࡪࡸࡣࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᨵ"), {})
    self.percy_capture_mode = config.get(bstack1l1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡆࡥࡵࡺࡵࡳࡧࡐࡳࡩ࡫ࠧᨶ"))
    try:
      bstack11lll1ll1l1_opy_, bstack11lll1lll11_opy_ = self.bstack11ll1lll1l1_opy_()
      bstack11ll1lll111_opy_, bstack11lll11ll1l_opy_ = self.bstack11lll11l1ll_opy_(bstack11lll1ll1l1_opy_, bstack11lll1lll11_opy_)
      if bstack11lll11ll1l_opy_:
        self.binary_path = bstack11ll1lll111_opy_
        thread = Thread(target=self.bstack11lll1l1l1l_opy_)
        thread.start()
      else:
        self.bstack11ll1lllll1_opy_ = True
        self.logger.error(bstack1l1_opy_ (u"ࠧࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡰࡦࡴࡦࡽࠥࡶࡡࡵࡪࠣࡪࡴࡻ࡮ࡥࠢ࠰ࠤࢀࢃࠬࠡࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡔࡪࡸࡣࡺࠤᨷ").format(bstack11ll1lll111_opy_))
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᨸ").format(e))
  def bstack11ll1lll1ll_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack1l1_opy_ (u"ࠧ࡭ࡱࡪࠫᨹ"), bstack1l1_opy_ (u"ࠨࡲࡨࡶࡨࡿ࠮࡭ࡱࡪࠫᨺ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack1l1_opy_ (u"ࠤࡓࡹࡸ࡮ࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢ࡯ࡳ࡬ࡹࠠࡢࡶࠣࡿࢂࠨᨻ").format(logfile))
      self.bstack11lll1l1lll_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡦࡶࠣࡴࡪࡸࡣࡺࠢ࡯ࡳ࡬ࠦࡰࡢࡶ࡫࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᨼ").format(e))
  def bstack11lll1l1l1l_opy_(self):
    bstack11ll1llll1l_opy_ = self.bstack11lll1l1111_opy_()
    if bstack11ll1llll1l_opy_ == None:
      self.bstack11ll1lllll1_opy_ = True
      self.logger.error(bstack1l1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡸࡴࡱࡥ࡯ࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨ࠱ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠢᨽ"))
      return False
    command_args = [bstack1l1_opy_ (u"ࠧࡧࡰࡱ࠼ࡨࡼࡪࡩ࠺ࡴࡶࡤࡶࡹࠨᨾ") if self.bstack1l1111ll1_opy_ else bstack1l1_opy_ (u"࠭ࡥࡹࡧࡦ࠾ࡸࡺࡡࡳࡶࠪᨿ")]
    bstack11lll11l11l_opy_ = self.bstack11lll11llll_opy_()
    if bstack11lll11l11l_opy_ != None:
      command_args.append(bstack1l1_opy_ (u"ࠢ࠮ࡥࠣࡿࢂࠨᩀ").format(bstack11lll11l11l_opy_))
    env = os.environ.copy()
    env[bstack1l1_opy_ (u"ࠣࡒࡈࡖࡈ࡟࡟ࡕࡑࡎࡉࡓࠨᩁ")] = bstack11ll1llll1l_opy_
    env[bstack1l1_opy_ (u"ࠤࡗࡌࡤࡈࡕࡊࡎࡇࡣ࡚࡛ࡉࡅࠤᩂ")] = os.environ.get(bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᩃ"), bstack1l1_opy_ (u"ࠫࠬᩄ"))
    bstack11lll11l111_opy_ = [self.binary_path]
    self.bstack11ll1lll1ll_opy_()
    self.bstack11ll1ll1ll1_opy_ = self.bstack11lll1111ll_opy_(bstack11lll11l111_opy_ + command_args, env)
    self.logger.debug(bstack1l1_opy_ (u"࡙ࠧࡴࡢࡴࡷ࡭ࡳ࡭ࠠࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠨᩅ"))
    bstack11lll1ll11l_opy_ = 0
    while self.bstack11ll1ll1ll1_opy_.poll() == None:
      bstack11ll1ll11ll_opy_ = self.bstack11lll1lll1l_opy_()
      if bstack11ll1ll11ll_opy_:
        self.logger.debug(bstack1l1_opy_ (u"ࠨࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡹࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠤᩆ"))
        self.bstack11lll1l11ll_opy_ = True
        return True
      bstack11lll1ll11l_opy_ += 1
      self.logger.debug(bstack1l1_opy_ (u"ࠢࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡒࡦࡶࡵࡽࠥ࠳ࠠࡼࡿࠥᩇ").format(bstack11lll1ll11l_opy_))
      time.sleep(2)
    self.logger.error(bstack1l1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠢࡉࡥ࡮ࡲࡥࡥࠢࡤࡪࡹ࡫ࡲࠡࡽࢀࠤࡦࡺࡴࡦ࡯ࡳࡸࡸࠨᩈ").format(bstack11lll1ll11l_opy_))
    self.bstack11ll1lllll1_opy_ = True
    return False
  def bstack11lll1lll1l_opy_(self, bstack11lll1ll11l_opy_ = 0):
    if bstack11lll1ll11l_opy_ > 10:
      return False
    try:
      bstack11llll11111_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠩࡓࡉࡗࡉ࡙ࡠࡕࡈࡖ࡛ࡋࡒࡠࡃࡇࡈࡗࡋࡓࡔࠩᩉ"), bstack1l1_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࡰࡴࡩࡡ࡭ࡪࡲࡷࡹࡀ࠵࠴࠵࠻ࠫᩊ"))
      bstack11lll1l111l_opy_ = bstack11llll11111_opy_ + bstack1l1l1l11l11_opy_
      response = requests.get(bstack11lll1l111l_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࠪᩋ"), {}).get(bstack1l1_opy_ (u"ࠬ࡯ࡤࠨᩌ"), None)
      return True
    except:
      self.logger.debug(bstack1l1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡵࡣࡤࡷࡵࡶࡪࡪࠠࡸࡪ࡬ࡰࡪࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣ࡬ࡪࡧ࡬ࡵࡪࠣࡧ࡭࡫ࡣ࡬ࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠦᩍ"))
      return False
  def bstack11lll1l1111_opy_(self):
    bstack11ll1ll1l1l_opy_ = bstack1l1_opy_ (u"ࠧࡢࡲࡳࠫᩎ") if self.bstack1l1111ll1_opy_ else bstack1l1_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪᩏ")
    bstack11lll11ll11_opy_ = bstack1l1_opy_ (u"ࠤࡸࡲࡩ࡫ࡦࡪࡰࡨࡨࠧᩐ") if self.config.get(bstack1l1_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩᩑ")) is None else True
    bstack1l111lllll1_opy_ = bstack1l1_opy_ (u"ࠦࡦࡶࡩ࠰ࡣࡳࡴࡤࡶࡥࡳࡥࡼ࠳࡬࡫ࡴࡠࡲࡵࡳ࡯࡫ࡣࡵࡡࡷࡳࡰ࡫࡮ࡀࡰࡤࡱࡪࡃࡻࡾࠨࡷࡽࡵ࡫࠽ࡼࡿࠩࡴࡪࡸࡣࡺ࠿ࡾࢁࠧᩒ").format(self.config[bstack1l1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᩓ")], bstack11ll1ll1l1l_opy_, bstack11lll11ll11_opy_)
    if self.percy_capture_mode:
      bstack1l111lllll1_opy_ += bstack1l1_opy_ (u"ࠨࠦࡱࡧࡵࡧࡾࡥࡣࡢࡲࡷࡹࡷ࡫࡟࡮ࡱࡧࡩࡂࢁࡽࠣᩔ").format(self.percy_capture_mode)
    uri = bstack1ll1l1l11l_opy_(bstack1l111lllll1_opy_)
    try:
      response = bstack11lll11l1l_opy_(bstack1l1_opy_ (u"ࠧࡈࡇࡗࠫᩕ"), uri, {}, {bstack1l1_opy_ (u"ࠨࡣࡸࡸ࡭࠭ᩖ"): (self.config[bstack1l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᩗ")], self.config[bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᩘ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1l1l11llll_opy_ = data.get(bstack1l1_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬᩙ"))
        self.percy_capture_mode = data.get(bstack1l1_opy_ (u"ࠬࡶࡥࡳࡥࡼࡣࡨࡧࡰࡵࡷࡵࡩࡤࡳ࡯ࡥࡧࠪᩚ"))
        os.environ[bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࠫᩛ")] = str(self.bstack1l1l11llll_opy_)
        os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࡤࡉࡁࡑࡖࡘࡖࡊࡥࡍࡐࡆࡈࠫᩜ")] = str(self.percy_capture_mode)
        if bstack11lll11ll11_opy_ == bstack1l1_opy_ (u"ࠣࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧࠦᩝ") and str(self.bstack1l1l11llll_opy_).lower() == bstack1l1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᩞ"):
          self.bstack11ll11lll1_opy_ = True
        if bstack1l1_opy_ (u"ࠥࡸࡴࡱࡥ࡯ࠤ᩟") in data:
          return data[bstack1l1_opy_ (u"ࠦࡹࡵ࡫ࡦࡰ᩠ࠥ")]
        else:
          raise bstack1l1_opy_ (u"࡚ࠬ࡯࡬ࡧࡱࠤࡓࡵࡴࠡࡈࡲࡹࡳࡪࠠ࠮ࠢࡾࢁࠬᩡ").format(data)
      else:
        raise bstack1l1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡩࡩࡹࡩࡨࠡࡲࡨࡶࡨࡿࠠࡵࡱ࡮ࡩࡳ࠲ࠠࡓࡧࡶࡴࡴࡴࡳࡦࠢࡶࡸࡦࡺࡵࡴࠢ࠰ࠤࢀࢃࠬࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡆࡴࡪࡹࠡ࠯ࠣࡿࢂࠨᩢ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡲࡨࡶࡨࡿࠠࡱࡴࡲ࡮ࡪࡩࡴࠣᩣ").format(e))
  def bstack11lll11llll_opy_(self):
    bstack11lll1lllll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1_opy_ (u"ࠣࡲࡨࡶࡨࡿࡃࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠦᩤ"))
    try:
      if bstack1l1_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪᩥ") not in self.bstack11lll1111l1_opy_:
        self.bstack11lll1111l1_opy_[bstack1l1_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫᩦ")] = 2
      with open(bstack11lll1lllll_opy_, bstack1l1_opy_ (u"ࠫࡼ࠭ᩧ")) as fp:
        json.dump(self.bstack11lll1111l1_opy_, fp)
      return bstack11lll1lllll_opy_
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡥࡵࡩࡦࡺࡥࠡࡲࡨࡶࡨࡿࠠࡤࡱࡱࡪ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᩨ").format(e))
  def bstack11lll1111ll_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack11lll1l1l11_opy_ == bstack1l1_opy_ (u"࠭ࡷࡪࡰࠪᩩ"):
        bstack11ll1l1lll1_opy_ = [bstack1l1_opy_ (u"ࠧࡤ࡯ࡧ࠲ࡪࡾࡥࠨᩪ"), bstack1l1_opy_ (u"ࠨ࠱ࡦࠫᩫ")]
        cmd = bstack11ll1l1lll1_opy_ + cmd
      cmd = bstack1l1_opy_ (u"ࠩࠣࠫᩬ").join(cmd)
      self.logger.debug(bstack1l1_opy_ (u"ࠥࡖࡺࡴ࡮ࡪࡰࡪࠤࢀࢃࠢᩭ").format(cmd))
      with open(self.bstack11lll1l1lll_opy_, bstack1l1_opy_ (u"ࠦࡦࠨᩮ")) as bstack11ll1ll1111_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack11ll1ll1111_opy_, text=True, stderr=bstack11ll1ll1111_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack11ll1lllll1_opy_ = True
      self.logger.error(bstack1l1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾࠦࡷࡪࡶ࡫ࠤࡨࡳࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠢᩯ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack11lll1l11ll_opy_:
        self.logger.info(bstack1l1_opy_ (u"ࠨࡓࡵࡱࡳࡴ࡮ࡴࡧࠡࡒࡨࡶࡨࡿࠢᩰ"))
        cmd = [self.binary_path, bstack1l1_opy_ (u"ࠢࡦࡺࡨࡧ࠿ࡹࡴࡰࡲࠥᩱ")]
        self.bstack11lll1111ll_opy_(cmd)
        self.bstack11lll1l11ll_opy_ = False
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺ࡯ࡱࠢࡶࡩࡸࡹࡩࡰࡰࠣࡻ࡮ࡺࡨࠡࡥࡲࡱࡲࡧ࡮ࡥࠢ࠰ࠤࢀࢃࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠣᩲ").format(cmd, e))
  def bstack11l11111l_opy_(self):
    if not self.bstack1l1l11llll_opy_:
      return
    try:
      bstack11lll1l11l1_opy_ = 0
      while not self.bstack11lll1l11ll_opy_ and bstack11lll1l11l1_opy_ < self.bstack11ll1ll11l1_opy_:
        if self.bstack11ll1lllll1_opy_:
          self.logger.info(bstack1l1_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡵࡨࡸࡺࡶࠠࡧࡣ࡬ࡰࡪࡪࠢᩳ"))
          return
        time.sleep(1)
        bstack11lll1l11l1_opy_ += 1
      os.environ[bstack1l1_opy_ (u"ࠪࡔࡊࡘࡃ࡚ࡡࡅࡉࡘ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࠩᩴ")] = str(self.bstack11ll1ll1lll_opy_())
      self.logger.info(bstack1l1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡷࡪࡺࡵࡱࠢࡦࡳࡲࡶ࡬ࡦࡶࡨࡨࠧ᩵"))
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠠࡱࡧࡵࡧࡾ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨ᩶").format(e))
  def bstack11ll1ll1lll_opy_(self):
    if self.bstack1l1111ll1_opy_:
      return
    try:
      bstack11ll1l1ll11_opy_ = [platform[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ᩷")].lower() for platform in self.config.get(bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ᩸"), [])]
      bstack11lll111lll_opy_ = sys.maxsize
      bstack11ll1lll11l_opy_ = bstack1l1_opy_ (u"ࠨࠩ᩹")
      for browser in bstack11ll1l1ll11_opy_:
        if browser in self.bstack11lll11111l_opy_:
          bstack11ll1ll111l_opy_ = self.bstack11lll11111l_opy_[browser]
        if bstack11ll1ll111l_opy_ < bstack11lll111lll_opy_:
          bstack11lll111lll_opy_ = bstack11ll1ll111l_opy_
          bstack11ll1lll11l_opy_ = browser
      return bstack11ll1lll11l_opy_
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡦࡪࡹࡴࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥ᩺").format(e))
  @classmethod
  def bstack1l11lll111_opy_(self):
    return os.getenv(bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࠨ᩻"), bstack1l1_opy_ (u"ࠫࡋࡧ࡬ࡴࡧࠪ᩼")).lower()
  @classmethod
  def bstack1lll11l11_opy_(self):
    return os.getenv(bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࡢࡇࡆࡖࡔࡖࡔࡈࡣࡒࡕࡄࡆࠩ᩽"), bstack1l1_opy_ (u"࠭ࠧ᩾"))
  @classmethod
  def bstack1l1lll1l11l_opy_(cls, value):
    cls.bstack11ll11lll1_opy_ = value
  @classmethod
  def bstack11lll111ll1_opy_(cls):
    return cls.bstack11ll11lll1_opy_
  @classmethod
  def bstack1l1lll11lll_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack11ll1l1ll1l_opy_(cls):
    return cls.percy_build_id