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
class bstack1llllll111l_opy_(object):
  bstack11111l111_opy_ = os.path.join(os.path.expanduser(bstack11111_opy_ (u"࠭ࡾࠨᄏ")), bstack11111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᄐ"))
  bstack1llllll11ll_opy_ = os.path.join(bstack11111l111_opy_, bstack11111_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵ࠱࡮ࡸࡵ࡮ࠨᄑ"))
  bstack1llllll11l1_opy_ = None
  perform_scan = None
  bstack111l11ll1_opy_ = None
  bstack1ll11llll_opy_ = None
  bstack1llllll1lll_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11111_opy_ (u"ࠩ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠫᄒ")):
      cls.instance = super(bstack1llllll111l_opy_, cls).__new__(cls)
      cls.instance.bstack1llllll1ll1_opy_()
    return cls.instance
  def bstack1llllll1ll1_opy_(self):
    try:
      with open(self.bstack1llllll11ll_opy_, bstack11111_opy_ (u"ࠪࡶࠬᄓ")) as bstack1lllll1l1_opy_:
        bstack1llllll1l1l_opy_ = bstack1lllll1l1_opy_.read()
        data = json.loads(bstack1llllll1l1l_opy_)
        if bstack11111_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭ᄔ") in data:
          self.bstack1lllllllll1_opy_(data[bstack11111_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧᄕ")])
        if bstack11111_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹࠧᄖ") in data:
          self.bstack111111l1l1_opy_(data[bstack11111_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨᄗ")])
    except:
      pass
  def bstack111111l1l1_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts[bstack11111_opy_ (u"ࠨࡵࡦࡥࡳ࠭ᄘ")]
      self.bstack111l11ll1_opy_ = scripts[bstack11111_opy_ (u"ࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࠭ᄙ")]
      self.bstack1ll11llll_opy_ = scripts[bstack11111_opy_ (u"ࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠧᄚ")]
      self.bstack1llllll1lll_opy_ = scripts[bstack11111_opy_ (u"ࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩᄛ")]
  def bstack1lllllllll1_opy_(self, bstack1llllll11l1_opy_):
    if bstack1llllll11l1_opy_ != None and len(bstack1llllll11l1_opy_) != 0:
      self.bstack1llllll11l1_opy_ = bstack1llllll11l1_opy_
  def store(self):
    try:
      with open(self.bstack1llllll11ll_opy_, bstack11111_opy_ (u"ࠬࡽࠧᄜ")) as file:
        json.dump({
          bstack11111_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࡳࠣᄝ"): self.bstack1llllll11l1_opy_,
          bstack11111_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࡳࠣᄞ"): {
            bstack11111_opy_ (u"ࠣࡵࡦࡥࡳࠨᄟ"): self.perform_scan,
            bstack11111_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸࠨᄠ"): self.bstack111l11ll1_opy_,
            bstack11111_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠢᄡ"): self.bstack1ll11llll_opy_,
            bstack11111_opy_ (u"ࠦࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠤᄢ"): self.bstack1llllll1lll_opy_
          }
        }, file)
    except:
      pass
  def bstack11111llll_opy_(self, bstack1llllll1l11_opy_):
    try:
      return any(command.get(bstack11111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᄣ")) == bstack1llllll1l11_opy_ for command in self.bstack1llllll11l1_opy_)
    except:
      return False
bstack1l11l1lll1_opy_ = bstack1llllll111l_opy_()