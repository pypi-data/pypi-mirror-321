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
class bstack11ll1l11lll_opy_(object):
  bstack1l1l111l11_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠧࡿ᩿ࠩ")), bstack1l1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ᪀"))
  bstack11ll1l11ll1_opy_ = os.path.join(bstack1l1l111l11_opy_, bstack1l1_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶ࠲࡯ࡹ࡯࡯ࠩ᪁"))
  commands_to_wrap = None
  perform_scan = None
  bstack111l1lll1_opy_ = None
  bstack1llll1l1l1_opy_ = None
  bstack11ll1l11l1l_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack1l1_opy_ (u"ࠪ࡭ࡳࡹࡴࡢࡰࡦࡩࠬ᪂")):
      cls.instance = super(bstack11ll1l11lll_opy_, cls).__new__(cls)
      cls.instance.bstack11ll1l1l1ll_opy_()
    return cls.instance
  def bstack11ll1l1l1ll_opy_(self):
    try:
      with open(self.bstack11ll1l11ll1_opy_, bstack1l1_opy_ (u"ࠫࡷ࠭᪃")) as bstack11l111ll1l_opy_:
        bstack11ll1l1l11l_opy_ = bstack11l111ll1l_opy_.read()
        data = json.loads(bstack11ll1l1l11l_opy_)
        if bstack1l1_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧ᪄") in data:
          self.bstack11ll1l1l1l1_opy_(data[bstack1l1_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨ᪅")])
        if bstack1l1_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨ᪆") in data:
          self.bstack11ll1l1l111_opy_(data[bstack1l1_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩ᪇")])
    except:
      pass
  def bstack11ll1l1l111_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts[bstack1l1_opy_ (u"ࠩࡶࡧࡦࡴࠧ᪈")]
      self.bstack111l1lll1_opy_ = scripts[bstack1l1_opy_ (u"ࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠧ᪉")]
      self.bstack1llll1l1l1_opy_ = scripts[bstack1l1_opy_ (u"ࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠨ᪊")]
      self.bstack11ll1l11l1l_opy_ = scripts[bstack1l1_opy_ (u"ࠬࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠪ᪋")]
  def bstack11ll1l1l1l1_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack11ll1l11ll1_opy_, bstack1l1_opy_ (u"࠭ࡷࠨ᪌")) as file:
        json.dump({
          bstack1l1_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࠤ᪍"): self.commands_to_wrap,
          bstack1l1_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࡴࠤ᪎"): {
            bstack1l1_opy_ (u"ࠤࡶࡧࡦࡴࠢ᪏"): self.perform_scan,
            bstack1l1_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠢ᪐"): self.bstack111l1lll1_opy_,
            bstack1l1_opy_ (u"ࠦ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠣ᪑"): self.bstack1llll1l1l1_opy_,
            bstack1l1_opy_ (u"ࠧࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠥ᪒"): self.bstack11ll1l11l1l_opy_
          }
        }, file)
    except:
      pass
  def bstack1lll11l1l1_opy_(self, bstack1lll11lllll_opy_):
    try:
      return any(command.get(bstack1l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ᪓")) == bstack1lll11lllll_opy_ for command in self.commands_to_wrap)
    except:
      return False
bstack11ll111lll_opy_ = bstack11ll1l11lll_opy_()