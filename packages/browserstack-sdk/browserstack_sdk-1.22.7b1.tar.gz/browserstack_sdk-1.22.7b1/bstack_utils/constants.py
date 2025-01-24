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
bstack1lllllllll_opy_ = {
	bstack1l1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ᏷"): bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩࡷ࠭ᏸ"),
  bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᏹ"): bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡯ࡪࡿࠧᏺ"),
  bstack1l1_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨᏻ"): bstack1l1_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪᏼ"),
  bstack1l1_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧᏽ"): bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡵࡨࡣࡼ࠹ࡣࠨ᏾"),
  bstack1l1_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧ᏿"): bstack1l1_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࠫ᐀"),
  bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᐁ"): bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࠫᐂ"),
  bstack1l1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᐃ"): bstack1l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᐄ"),
  bstack1l1_opy_ (u"ࠨࡦࡨࡦࡺ࡭ࠧᐅ"): bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡦࡨࡦࡺ࡭ࠧᐆ"),
  bstack1l1_opy_ (u"ࠪࡧࡴࡴࡳࡰ࡮ࡨࡐࡴ࡭ࡳࠨᐇ"): bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡴࡳࡰ࡮ࡨࠫᐈ"),
  bstack1l1_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰࡒ࡯ࡨࡵࠪᐉ"): bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡴࡥࡵࡹࡲࡶࡰࡒ࡯ࡨࡵࠪᐊ"),
  bstack1l1_opy_ (u"ࠧࡢࡲࡳ࡭ࡺࡳࡌࡰࡩࡶࠫᐋ"): bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡲࡳ࡭ࡺࡳࡌࡰࡩࡶࠫᐌ"),
  bstack1l1_opy_ (u"ࠩࡹ࡭ࡩ࡫࡯ࠨᐍ"): bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡹ࡭ࡩ࡫࡯ࠨᐎ"),
  bstack1l1_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡒ࡯ࡨࡵࠪᐏ"): bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡒ࡯ࡨࡵࠪᐐ"),
  bstack1l1_opy_ (u"࠭ࡴࡦ࡮ࡨࡱࡪࡺࡲࡺࡎࡲ࡫ࡸ࠭ᐑ"): bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡦ࡮ࡨࡱࡪࡺࡲࡺࡎࡲ࡫ࡸ࠭ᐒ"),
  bstack1l1_opy_ (u"ࠨࡩࡨࡳࡑࡵࡣࡢࡶ࡬ࡳࡳ࠭ᐓ"): bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡩࡨࡳࡑࡵࡣࡢࡶ࡬ࡳࡳ࠭ᐔ"),
  bstack1l1_opy_ (u"ࠪࡸ࡮ࡳࡥࡻࡱࡱࡩࠬᐕ"): bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸ࡮ࡳࡥࡻࡱࡱࡩࠬᐖ"),
  bstack1l1_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡖࡦࡴࡶ࡭ࡴࡴࠧᐗ"): bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᐘ"),
  bstack1l1_opy_ (u"ࠧ࡮ࡣࡶ࡯ࡈࡵ࡭࡮ࡣࡱࡨࡸ࠭ᐙ"): bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡮ࡣࡶ࡯ࡈࡵ࡭࡮ࡣࡱࡨࡸ࠭ᐚ"),
  bstack1l1_opy_ (u"ࠩ࡬ࡨࡱ࡫ࡔࡪ࡯ࡨࡳࡺࡺࠧᐛ"): bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡬ࡨࡱ࡫ࡔࡪ࡯ࡨࡳࡺࡺࠧᐜ"),
  bstack1l1_opy_ (u"ࠫࡲࡧࡳ࡬ࡄࡤࡷ࡮ࡩࡁࡶࡶ࡫ࠫᐝ"): bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡲࡧࡳ࡬ࡄࡤࡷ࡮ࡩࡁࡶࡶ࡫ࠫᐞ"),
  bstack1l1_opy_ (u"࠭ࡳࡦࡰࡧࡏࡪࡿࡳࠨᐟ"): bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡳࡦࡰࡧࡏࡪࡿࡳࠨᐠ"),
  bstack1l1_opy_ (u"ࠨࡣࡸࡸࡴ࡝ࡡࡪࡶࠪᐡ"): bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡸࡸࡴ࡝ࡡࡪࡶࠪᐢ"),
  bstack1l1_opy_ (u"ࠪ࡬ࡴࡹࡴࡴࠩᐣ"): bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡬ࡴࡹࡴࡴࠩᐤ"),
  bstack1l1_opy_ (u"ࠬࡨࡦࡤࡣࡦ࡬ࡪ࠭ᐥ"): bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡦࡤࡣࡦ࡬ࡪ࠭ᐦ"),
  bstack1l1_opy_ (u"ࠧࡸࡵࡏࡳࡨࡧ࡬ࡔࡷࡳࡴࡴࡸࡴࠨᐧ"): bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡸࡵࡏࡳࡨࡧ࡬ࡔࡷࡳࡴࡴࡸࡴࠨᐨ"),
  bstack1l1_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡆࡳࡷࡹࡒࡦࡵࡷࡶ࡮ࡩࡴࡪࡱࡱࡷࠬᐩ"): bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡧ࡭ࡸࡧࡢ࡭ࡧࡆࡳࡷࡹࡒࡦࡵࡷࡶ࡮ࡩࡴࡪࡱࡱࡷࠬᐪ"),
  bstack1l1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨᐫ"): bstack1l1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬᐬ"),
  bstack1l1_opy_ (u"࠭ࡲࡦࡣ࡯ࡑࡴࡨࡩ࡭ࡧࠪᐭ"): bstack1l1_opy_ (u"ࠧࡳࡧࡤࡰࡤࡳ࡯ࡣ࡫࡯ࡩࠬᐮ"),
  bstack1l1_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᐯ"): bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡳࡴ࡮ࡻ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᐰ"),
  bstack1l1_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡑࡩࡹࡽ࡯ࡳ࡭ࠪᐱ"): bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡺࡹࡴࡰ࡯ࡑࡩࡹࡽ࡯ࡳ࡭ࠪᐲ"),
  bstack1l1_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰࡖࡲࡰࡨ࡬ࡰࡪ࠭ᐳ"): bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡴࡥࡵࡹࡲࡶࡰࡖࡲࡰࡨ࡬ࡰࡪ࠭ᐴ"),
  bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡉ࡯ࡵࡨࡧࡺࡸࡥࡄࡧࡵࡸࡸ࠭ᐵ"): bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡔࡵ࡯ࡇࡪࡸࡴࡴࠩᐶ"),
  bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫᐷ"): bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫᐸ"),
  bstack1l1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫᐹ"): bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡸࡵࡵࡳࡥࡨࠫᐺ"),
  bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᐻ"): bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᐼ"),
  bstack1l1_opy_ (u"ࠨࡪࡲࡷࡹࡔࡡ࡮ࡧࠪᐽ"): bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡪࡲࡷࡹࡔࡡ࡮ࡧࠪᐾ"),
  bstack1l1_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡖ࡭ࡲ࠭ᐿ"): bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡩࡳࡧࡢ࡭ࡧࡖ࡭ࡲ࠭ᑀ"),
  bstack1l1_opy_ (u"ࠬࡹࡩ࡮ࡑࡳࡸ࡮ࡵ࡮ࡴࠩᑁ"): bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡹࡩ࡮ࡑࡳࡸ࡮ࡵ࡮ࡴࠩᑂ"),
  bstack1l1_opy_ (u"ࠧࡶࡲ࡯ࡳࡦࡪࡍࡦࡦ࡬ࡥࠬᑃ"): bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡲ࡯ࡳࡦࡪࡍࡦࡦ࡬ࡥࠬᑄ"),
  bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᑅ"): bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᑆ"),
  bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᑇ"): bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᑈ")
}
bstack1l1l1ll111l_opy_ = [
  bstack1l1_opy_ (u"࠭࡯ࡴࠩᑉ"),
  bstack1l1_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪᑊ"),
  bstack1l1_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪᑋ"),
  bstack1l1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᑌ"),
  bstack1l1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧᑍ"),
  bstack1l1_opy_ (u"ࠫࡷ࡫ࡡ࡭ࡏࡲࡦ࡮ࡲࡥࠨᑎ"),
  bstack1l1_opy_ (u"ࠬࡧࡰࡱ࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᑏ"),
]
bstack1lll1l1l11_opy_ = {
  bstack1l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨᑐ"): [bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨᑑ"), bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡤࡔࡁࡎࡇࠪᑒ")],
  bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬᑓ"): bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭ᑔ"),
  bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᑕ"): bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡒࡆࡓࡅࠨᑖ"),
  bstack1l1_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᑗ"): bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡏࡃࡐࡉࠬᑘ"),
  bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᑙ"): bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫᑚ"),
  bstack1l1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᑛ"): bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡆࡘࡁࡍࡎࡈࡐࡘࡥࡐࡆࡔࡢࡔࡑࡇࡔࡇࡑࡕࡑࠬᑜ"),
  bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩᑝ"): bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࠫᑞ"),
  bstack1l1_opy_ (u"ࠧࡳࡧࡵࡹࡳ࡚ࡥࡴࡶࡶࠫᑟ"): bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࡥࡔࡆࡕࡗࡗࠬᑠ"),
  bstack1l1_opy_ (u"ࠩࡤࡴࡵ࠭ᑡ"): [bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡔࡕࡥࡉࡅࠩᑢ"), bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅࡕࡖࠧᑣ")],
  bstack1l1_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧᑤ"): bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡙ࡄࡌࡡࡏࡓࡌࡒࡅࡗࡇࡏࠫᑥ"),
  bstack1l1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᑦ"): bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫᑧ"),
  bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᑨ"): bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡐࡄࡖࡉࡗ࡜ࡁࡃࡋࡏࡍ࡙࡟ࠧᑩ"),
  bstack1l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨᑪ"): bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙࡛ࡒࡃࡑࡖࡇࡆࡒࡅࠨᑫ")
}
bstack11l111l1l_opy_ = {
  bstack1l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨᑬ"): [bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡵࡴࡧࡵࡣࡳࡧ࡭ࡦࠩᑭ"), bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡵࡨࡶࡓࡧ࡭ࡦࠩᑮ")],
  bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬᑯ"): [bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴࡡ࡮ࡩࡾ࠭ᑰ"), bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᑱ")],
  bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨᑲ"): bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨᑳ"),
  bstack1l1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᑴ"): bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᑵ"),
  bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᑶ"): bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᑷ"),
  bstack1l1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫᑸ"): [bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡵࡶࡰࠨᑹ"), bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬᑺ")],
  bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫᑻ"): bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱ࠭ᑼ"),
  bstack1l1_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡕࡧࡶࡸࡸ࠭ᑽ"): bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡵࡩࡷࡻ࡮ࡕࡧࡶࡸࡸ࠭ᑾ"),
  bstack1l1_opy_ (u"ࠫࡦࡶࡰࠨᑿ"): bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡶࡰࠨᒀ"),
  bstack1l1_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨᒁ"): bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨᒂ"),
  bstack1l1_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᒃ"): bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᒄ")
}
bstack11ll11111_opy_ = {
  bstack1l1_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᒅ"): bstack1l1_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᒆ"),
  bstack1l1_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡖࡦࡴࡶ࡭ࡴࡴࠧᒇ"): [bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᒈ"), bstack1l1_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠪᒉ")],
  bstack1l1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ᒊ"): bstack1l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᒋ"),
  bstack1l1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧᒌ"): bstack1l1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫᒍ"),
  bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪᒎ"): [bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧᒏ"), bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡰࡤࡱࡪ࠭ᒐ")],
  bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᒑ"): bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫᒒ"),
  bstack1l1_opy_ (u"ࠪࡶࡪࡧ࡬ࡎࡱࡥ࡭ࡱ࡫ࠧᒓ"): bstack1l1_opy_ (u"ࠫࡷ࡫ࡡ࡭ࡡࡰࡳࡧ࡯࡬ࡦࠩᒔ"),
  bstack1l1_opy_ (u"ࠬࡧࡰࡱ࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᒕ"): [bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡰࡱ࡫ࡸࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᒖ"), bstack1l1_opy_ (u"ࠧࡢࡲࡳ࡭ࡺࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᒗ")],
  bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡊࡰࡶࡩࡨࡻࡲࡦࡅࡨࡶࡹࡹࠧᒘ"): [bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡕࡶࡰࡈ࡫ࡲࡵࡵࠪᒙ"), bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡖࡷࡱࡉࡥࡳࡶࠪᒚ")]
}
bstack111ll1111_opy_ = [
  bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡍࡳࡹࡥࡤࡷࡵࡩࡈ࡫ࡲࡵࡵࠪᒛ"),
  bstack1l1_opy_ (u"ࠬࡶࡡࡨࡧࡏࡳࡦࡪࡓࡵࡴࡤࡸࡪ࡭ࡹࠨᒜ"),
  bstack1l1_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬᒝ"),
  bstack1l1_opy_ (u"ࠧࡴࡧࡷ࡛࡮ࡴࡤࡰࡹࡕࡩࡨࡺࠧᒞ"),
  bstack1l1_opy_ (u"ࠨࡶ࡬ࡱࡪࡵࡵࡵࡵࠪᒟ"),
  bstack1l1_opy_ (u"ࠩࡶࡸࡷ࡯ࡣࡵࡈ࡬ࡰࡪࡏ࡮ࡵࡧࡵࡥࡨࡺࡡࡣ࡫࡯࡭ࡹࡿࠧᒠ"),
  bstack1l1_opy_ (u"ࠪࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡖࡲࡰ࡯ࡳࡸࡇ࡫ࡨࡢࡸ࡬ࡳࡷ࠭ᒡ"),
  bstack1l1_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᒢ"),
  bstack1l1_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡩ࡭ࡷ࡫ࡦࡰࡺࡒࡴࡹ࡯࡯࡯ࡵࠪᒣ"),
  bstack1l1_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᒤ"),
  bstack1l1_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᒥ"),
  bstack1l1_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᒦ"),
]
bstack1l1l11ll1_opy_ = [
  bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᒧ"),
  bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧᒨ"),
  bstack1l1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪᒩ"),
  bstack1l1_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬᒪ"),
  bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩᒫ"),
  bstack1l1_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩᒬ"),
  bstack1l1_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᒭ"),
  bstack1l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ᒮ"),
  bstack1l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ᒯ"),
  bstack1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠩᒰ"),
  bstack1l1_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩᒱ"),
  bstack1l1_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠨᒲ"),
  bstack1l1_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡔࡢࡩࠪᒳ"),
  bstack1l1_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᒴ"),
  bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᒵ"),
  bstack1l1_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡖࡨࡷࡹࡹࠧᒶ"),
  bstack1l1_opy_ (u"ࠫࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࠳ࠪᒷ"),
  bstack1l1_opy_ (u"ࠬࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࠵ࠫᒸ"),
  bstack1l1_opy_ (u"࠭ࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢ࠷ࠬᒹ"),
  bstack1l1_opy_ (u"ࠧࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣ࠹࠭ᒺ"),
  bstack1l1_opy_ (u"ࠨࡅࡘࡗ࡙ࡕࡍࡠࡖࡄࡋࡤ࠻ࠧᒻ"),
  bstack1l1_opy_ (u"ࠩࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࠶ࠨᒼ"),
  bstack1l1_opy_ (u"ࠪࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࠸ࠩᒽ"),
  bstack1l1_opy_ (u"ࠫࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࠺ࠪᒾ"),
  bstack1l1_opy_ (u"ࠬࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࠼ࠫᒿ"),
  bstack1l1_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬᓀ"),
  bstack1l1_opy_ (u"ࠧࡱࡧࡵࡧࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᓁ"),
  bstack1l1_opy_ (u"ࠨࡲࡨࡶࡨࡿࡃࡢࡲࡷࡹࡷ࡫ࡍࡰࡦࡨࠫᓂ"),
  bstack1l1_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫᓃ"),
  bstack1l1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧᓄ"),
  bstack1l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᓅ")
]
bstack1l1l1ll11l1_opy_ = [
  bstack1l1_opy_ (u"ࠬࡻࡰ࡭ࡱࡤࡨࡒ࡫ࡤࡪࡣࠪᓆ"),
  bstack1l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨᓇ"),
  bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪᓈ"),
  bstack1l1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ᓉ"),
  bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺࡐࡳ࡫ࡲࡶ࡮ࡺࡹࠨᓊ"),
  bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ᓋ"),
  bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡗࡥ࡬࠭ᓌ"),
  bstack1l1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᓍ"),
  bstack1l1_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᓎ"),
  bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᓏ"),
  bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᓐ"),
  bstack1l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࠨᓑ"),
  bstack1l1_opy_ (u"ࠪࡳࡸ࠭ᓒ"),
  bstack1l1_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧᓓ"),
  bstack1l1_opy_ (u"ࠬ࡮࡯ࡴࡶࡶࠫᓔ"),
  bstack1l1_opy_ (u"࠭ࡡࡶࡶࡲ࡛ࡦ࡯ࡴࠨᓕ"),
  bstack1l1_opy_ (u"ࠧࡳࡧࡪ࡭ࡴࡴࠧᓖ"),
  bstack1l1_opy_ (u"ࠨࡶ࡬ࡱࡪࢀ࡯࡯ࡧࠪᓗ"),
  bstack1l1_opy_ (u"ࠩࡰࡥࡨ࡮ࡩ࡯ࡧࠪᓘ"),
  bstack1l1_opy_ (u"ࠪࡶࡪࡹ࡯࡭ࡷࡷ࡭ࡴࡴࠧᓙ"),
  bstack1l1_opy_ (u"ࠫ࡮ࡪ࡬ࡦࡖ࡬ࡱࡪࡵࡵࡵࠩᓚ"),
  bstack1l1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡔࡸࡩࡦࡰࡷࡥࡹ࡯࡯࡯ࠩᓛ"),
  bstack1l1_opy_ (u"࠭ࡶࡪࡦࡨࡳࠬᓜ"),
  bstack1l1_opy_ (u"ࠧ࡯ࡱࡓࡥ࡬࡫ࡌࡰࡣࡧࡘ࡮ࡳࡥࡰࡷࡷࠫᓝ"),
  bstack1l1_opy_ (u"ࠨࡤࡩࡧࡦࡩࡨࡦࠩᓞ"),
  bstack1l1_opy_ (u"ࠩࡧࡩࡧࡻࡧࠨᓟ"),
  bstack1l1_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡖࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧᓠ"),
  bstack1l1_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡗࡪࡴࡤࡌࡧࡼࡷࠬᓡ"),
  bstack1l1_opy_ (u"ࠬࡸࡥࡢ࡮ࡐࡳࡧ࡯࡬ࡦࠩᓢ"),
  bstack1l1_opy_ (u"࠭࡮ࡰࡒ࡬ࡴࡪࡲࡩ࡯ࡧࠪᓣ"),
  bstack1l1_opy_ (u"ࠧࡤࡪࡨࡧࡰ࡛ࡒࡍࠩᓤ"),
  bstack1l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᓥ"),
  bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡅࡲࡳࡰ࡯ࡥࡴࠩᓦ"),
  bstack1l1_opy_ (u"ࠪࡧࡦࡶࡴࡶࡴࡨࡇࡷࡧࡳࡩࠩᓧ"),
  bstack1l1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨᓨ"),
  bstack1l1_opy_ (u"ࠬࡧࡰࡱ࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᓩ"),
  bstack1l1_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰ࡙ࡩࡷࡹࡩࡰࡰࠪᓪ"),
  bstack1l1_opy_ (u"ࠧ࡯ࡱࡅࡰࡦࡴ࡫ࡑࡱ࡯ࡰ࡮ࡴࡧࠨᓫ"),
  bstack1l1_opy_ (u"ࠨ࡯ࡤࡷࡰ࡙ࡥ࡯ࡦࡎࡩࡾࡹࠧᓬ"),
  bstack1l1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡎࡲ࡫ࡸ࠭ᓭ"),
  bstack1l1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡌࡨࠬᓮ"),
  bstack1l1_opy_ (u"ࠫࡩ࡫ࡤࡪࡥࡤࡸࡪࡪࡄࡦࡸ࡬ࡧࡪ࠭ᓯ"),
  bstack1l1_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡕࡧࡲࡢ࡯ࡶࠫᓰ"),
  bstack1l1_opy_ (u"࠭ࡰࡩࡱࡱࡩࡓࡻ࡭ࡣࡧࡵࠫᓱ"),
  bstack1l1_opy_ (u"ࠧ࡯ࡧࡷࡻࡴࡸ࡫ࡍࡱࡪࡷࠬᓲ"),
  bstack1l1_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸࡕࡰࡵ࡫ࡲࡲࡸ࠭ᓳ"),
  bstack1l1_opy_ (u"ࠩࡦࡳࡳࡹ࡯࡭ࡧࡏࡳ࡬ࡹࠧᓴ"),
  bstack1l1_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪᓵ"),
  bstack1l1_opy_ (u"ࠫࡦࡶࡰࡪࡷࡰࡐࡴ࡭ࡳࠨᓶ"),
  bstack1l1_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡇ࡯࡯࡮ࡧࡷࡶ࡮ࡩࠧᓷ"),
  bstack1l1_opy_ (u"࠭ࡶࡪࡦࡨࡳ࡛࠸ࠧᓸ"),
  bstack1l1_opy_ (u"ࠧ࡮࡫ࡧࡗࡪࡹࡳࡪࡱࡱࡍࡳࡹࡴࡢ࡮࡯ࡅࡵࡶࡳࠨᓹ"),
  bstack1l1_opy_ (u"ࠨࡧࡶࡴࡷ࡫ࡳࡴࡱࡖࡩࡷࡼࡥࡳࠩᓺ"),
  bstack1l1_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࡐࡴ࡭ࡳࠨᓻ"),
  bstack1l1_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࡈࡪࡰࠨᓼ"),
  bstack1l1_opy_ (u"ࠫࡹ࡫࡬ࡦ࡯ࡨࡸࡷࡿࡌࡰࡩࡶࠫᓽ"),
  bstack1l1_opy_ (u"ࠬࡹࡹ࡯ࡥࡗ࡭ࡲ࡫ࡗࡪࡶ࡫ࡒ࡙ࡖࠧᓾ"),
  bstack1l1_opy_ (u"࠭ࡧࡦࡱࡏࡳࡨࡧࡴࡪࡱࡱࠫᓿ"),
  bstack1l1_opy_ (u"ࠧࡨࡲࡶࡐࡴࡩࡡࡵ࡫ࡲࡲࠬᔀ"),
  bstack1l1_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡒࡵࡳ࡫࡯࡬ࡦࠩᔁ"),
  bstack1l1_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡐࡨࡸࡼࡵࡲ࡬ࠩᔂ"),
  bstack1l1_opy_ (u"ࠪࡪࡴࡸࡣࡦࡅ࡫ࡥࡳ࡭ࡥࡋࡣࡵࠫᔃ"),
  bstack1l1_opy_ (u"ࠫࡽࡳࡳࡋࡣࡵࠫᔄ"),
  bstack1l1_opy_ (u"ࠬࡾ࡭ࡹࡌࡤࡶࠬᔅ"),
  bstack1l1_opy_ (u"࠭࡭ࡢࡵ࡮ࡇࡴࡳ࡭ࡢࡰࡧࡷࠬᔆ"),
  bstack1l1_opy_ (u"ࠧ࡮ࡣࡶ࡯ࡇࡧࡳࡪࡥࡄࡹࡹ࡮ࠧᔇ"),
  bstack1l1_opy_ (u"ࠨࡹࡶࡐࡴࡩࡡ࡭ࡕࡸࡴࡵࡵࡲࡵࠩᔈ"),
  bstack1l1_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡆࡳࡷࡹࡒࡦࡵࡷࡶ࡮ࡩࡴࡪࡱࡱࡷࠬᔉ"),
  bstack1l1_opy_ (u"ࠪࡥࡵࡶࡖࡦࡴࡶ࡭ࡴࡴࠧᔊ"),
  bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡍࡳࡹࡥࡤࡷࡵࡩࡈ࡫ࡲࡵࡵࠪᔋ"),
  bstack1l1_opy_ (u"ࠬࡸࡥࡴ࡫ࡪࡲࡆࡶࡰࠨᔌ"),
  bstack1l1_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁ࡯࡫ࡰࡥࡹ࡯࡯࡯ࡵࠪᔍ"),
  bstack1l1_opy_ (u"ࠧࡤࡣࡱࡥࡷࡿࠧᔎ"),
  bstack1l1_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࠩᔏ"),
  bstack1l1_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩᔐ"),
  bstack1l1_opy_ (u"ࠪ࡭ࡪ࠭ᔑ"),
  bstack1l1_opy_ (u"ࠫࡪࡪࡧࡦࠩᔒ"),
  bstack1l1_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬᔓ"),
  bstack1l1_opy_ (u"࠭ࡱࡶࡧࡸࡩࠬᔔ"),
  bstack1l1_opy_ (u"ࠧࡪࡰࡷࡩࡷࡴࡡ࡭ࠩᔕ"),
  bstack1l1_opy_ (u"ࠨࡣࡳࡴࡘࡺ࡯ࡳࡧࡆࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠩᔖ"),
  bstack1l1_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡅࡤࡱࡪࡸࡡࡊ࡯ࡤ࡫ࡪࡏ࡮࡫ࡧࡦࡸ࡮ࡵ࡮ࠨᔗ"),
  bstack1l1_opy_ (u"ࠪࡲࡪࡺࡷࡰࡴ࡮ࡐࡴ࡭ࡳࡆࡺࡦࡰࡺࡪࡥࡉࡱࡶࡸࡸ࠭ᔘ"),
  bstack1l1_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡑࡵࡧࡴࡋࡱࡧࡱࡻࡤࡦࡊࡲࡷࡹࡹࠧᔙ"),
  bstack1l1_opy_ (u"ࠬࡻࡰࡥࡣࡷࡩࡆࡶࡰࡔࡧࡷࡸ࡮ࡴࡧࡴࠩᔚ"),
  bstack1l1_opy_ (u"࠭ࡲࡦࡵࡨࡶࡻ࡫ࡄࡦࡸ࡬ࡧࡪ࠭ᔛ"),
  bstack1l1_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧᔜ"),
  bstack1l1_opy_ (u"ࠨࡵࡨࡲࡩࡑࡥࡺࡵࠪᔝ"),
  bstack1l1_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡒࡤࡷࡸࡩ࡯ࡥࡧࠪᔞ"),
  bstack1l1_opy_ (u"ࠪࡹࡵࡪࡡࡵࡧࡌࡳࡸࡊࡥࡷ࡫ࡦࡩࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭ᔟ"),
  bstack1l1_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡅࡺࡪࡩࡰࡋࡱ࡮ࡪࡩࡴࡪࡱࡱࠫᔠ"),
  bstack1l1_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡆࡶࡰ࡭ࡧࡓࡥࡾ࠭ᔡ"),
  bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧᔢ"),
  bstack1l1_opy_ (u"ࠧࡸࡦ࡬ࡳࡘ࡫ࡲࡷ࡫ࡦࡩࠬᔣ"),
  bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᔤ"),
  bstack1l1_opy_ (u"ࠩࡳࡶࡪࡼࡥ࡯ࡶࡆࡶࡴࡹࡳࡔ࡫ࡷࡩ࡙ࡸࡡࡤ࡭࡬ࡲ࡬࠭ᔥ"),
  bstack1l1_opy_ (u"ࠪ࡬࡮࡭ࡨࡄࡱࡱࡸࡷࡧࡳࡵࠩᔦ"),
  bstack1l1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡔࡷ࡫ࡦࡦࡴࡨࡲࡨ࡫ࡳࠨᔧ"),
  bstack1l1_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡘ࡯࡭ࠨᔨ"),
  bstack1l1_opy_ (u"࠭ࡳࡪ࡯ࡒࡴࡹ࡯࡯࡯ࡵࠪᔩ"),
  bstack1l1_opy_ (u"ࠧࡳࡧࡰࡳࡻ࡫ࡉࡐࡕࡄࡴࡵ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹࡌࡰࡥࡤࡰ࡮ࢀࡡࡵ࡫ࡲࡲࠬᔪ"),
  bstack1l1_opy_ (u"ࠨࡪࡲࡷࡹࡔࡡ࡮ࡧࠪᔫ"),
  bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᔬ"),
  bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࠬᔭ"),
  bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪᔮ"),
  bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧᔯ"),
  bstack1l1_opy_ (u"࠭ࡰࡢࡩࡨࡐࡴࡧࡤࡔࡶࡵࡥࡹ࡫ࡧࡺࠩᔰ"),
  bstack1l1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭ᔱ"),
  bstack1l1_opy_ (u"ࠨࡶ࡬ࡱࡪࡵࡵࡵࡵࠪᔲ"),
  bstack1l1_opy_ (u"ࠩࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡕࡸ࡯࡮ࡲࡷࡆࡪ࡮ࡡࡷ࡫ࡲࡶࠬᔳ")
]
bstack1l1llll11_opy_ = {
  bstack1l1_opy_ (u"ࠪࡺࠬᔴ"): bstack1l1_opy_ (u"ࠫࡻ࠭ᔵ"),
  bstack1l1_opy_ (u"ࠬ࡬ࠧᔶ"): bstack1l1_opy_ (u"࠭ࡦࠨᔷ"),
  bstack1l1_opy_ (u"ࠧࡧࡱࡵࡧࡪ࠭ᔸ"): bstack1l1_opy_ (u"ࠨࡨࡲࡶࡨ࡫ࠧᔹ"),
  bstack1l1_opy_ (u"ࠩࡲࡲࡱࡿࡡࡶࡶࡲࡱࡦࡺࡥࠨᔺ"): bstack1l1_opy_ (u"ࠪࡳࡳࡲࡹࡂࡷࡷࡳࡲࡧࡴࡦࠩᔻ"),
  bstack1l1_opy_ (u"ࠫ࡫ࡵࡲࡤࡧ࡯ࡳࡨࡧ࡬ࠨᔼ"): bstack1l1_opy_ (u"ࠬ࡬࡯ࡳࡥࡨࡰࡴࡩࡡ࡭ࠩᔽ"),
  bstack1l1_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡭ࡵࡳࡵࠩᔾ"): bstack1l1_opy_ (u"ࠧࡱࡴࡲࡼࡾࡎ࡯ࡴࡶࠪᔿ"),
  bstack1l1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡰࡰࡴࡷࠫᕀ"): bstack1l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡱࡵࡸࠬᕁ"),
  bstack1l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡷࡶࡩࡷ࠭ᕂ"): bstack1l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡘࡷࡪࡸࠧᕃ"),
  bstack1l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡴࡦࡹࡳࠨᕄ"): bstack1l1_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡧࡳࡴࠩᕅ"),
  bstack1l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡶࡲࡰࡺࡼ࡬ࡴࡹࡴࠨᕆ"): bstack1l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡐࡳࡱࡻࡽࡍࡵࡳࡵࠩᕇ"),
  bstack1l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡱࡴࡲࡼࡾࡶ࡯ࡳࡶࠪᕈ"): bstack1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡒࡵࡳࡽࡿࡐࡰࡴࡷࠫᕉ"),
  bstack1l1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡳࡶࡴࡾࡹࡶࡵࡨࡶࠬᕊ"): bstack1l1_opy_ (u"ࠬ࠳࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡘࡷࡪࡸࠧᕋ"),
  bstack1l1_opy_ (u"࠭࠭࡭ࡱࡦࡥࡱࡶࡲࡰࡺࡼࡹࡸ࡫ࡲࠨᕌ"): bstack1l1_opy_ (u"ࠧ࠮࡮ࡲࡧࡦࡲࡐࡳࡱࡻࡽ࡚ࡹࡥࡳࠩᕍ"),
  bstack1l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡰࡳࡱࡻࡽࡵࡧࡳࡴࠩᕎ"): bstack1l1_opy_ (u"ࠩ࠰ࡰࡴࡩࡡ࡭ࡒࡵࡳࡽࡿࡐࡢࡵࡶࠫᕏ"),
  bstack1l1_opy_ (u"ࠪ࠱ࡱࡵࡣࡢ࡮ࡳࡶࡴࡾࡹࡱࡣࡶࡷࠬᕐ"): bstack1l1_opy_ (u"ࠫ࠲ࡲ࡯ࡤࡣ࡯ࡔࡷࡵࡸࡺࡒࡤࡷࡸ࠭ᕑ"),
  bstack1l1_opy_ (u"ࠬࡨࡩ࡯ࡣࡵࡽࡵࡧࡴࡩࠩᕒ"): bstack1l1_opy_ (u"࠭ࡢࡪࡰࡤࡶࡾࡶࡡࡵࡪࠪᕓ"),
  bstack1l1_opy_ (u"ࠧࡱࡣࡦࡪ࡮ࡲࡥࠨᕔ"): bstack1l1_opy_ (u"ࠨ࠯ࡳࡥࡨ࠳ࡦࡪ࡮ࡨࠫᕕ"),
  bstack1l1_opy_ (u"ࠩࡳࡥࡨ࠳ࡦࡪ࡮ࡨࠫᕖ"): bstack1l1_opy_ (u"ࠪ࠱ࡵࡧࡣ࠮ࡨ࡬ࡰࡪ࠭ᕗ"),
  bstack1l1_opy_ (u"ࠫ࠲ࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧᕘ"): bstack1l1_opy_ (u"ࠬ࠳ࡰࡢࡥ࠰ࡪ࡮ࡲࡥࠨᕙ"),
  bstack1l1_opy_ (u"࠭࡬ࡰࡩࡩ࡭ࡱ࡫ࠧᕚ"): bstack1l1_opy_ (u"ࠧ࡭ࡱࡪࡪ࡮ࡲࡥࠨᕛ"),
  bstack1l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᕜ"): bstack1l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᕝ"),
  bstack1l1_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯࠰ࡶࡪࡶࡥࡢࡶࡨࡶࠬᕞ"): bstack1l1_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡖࡪࡶࡥࡢࡶࡨࡶࠬᕟ")
}
bstack1l1l1ll11ll_opy_ = bstack1l1_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡧࡪࡶ࡫ࡹࡧ࠴ࡣࡰ࡯࠲ࡴࡪࡸࡣࡺ࠱ࡦࡰ࡮࠵ࡲࡦ࡮ࡨࡥࡸ࡫ࡳ࠰࡮ࡤࡸࡪࡹࡴ࠰ࡦࡲࡻࡳࡲ࡯ࡢࡦࠥᕠ")
bstack1l1l1l11l11_opy_ = bstack1l1_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠵ࡨࡦࡣ࡯ࡸ࡭ࡩࡨࡦࡥ࡮ࠦᕡ")
bstack11l11l1ll1_opy_ = bstack1l1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡪࡸࡦ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡹࡧ࠳࡭ࡻࡢࠨᕢ")
bstack11l1111l1l_opy_ = bstack1l1_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰ࡪࡸࡦ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠫᕣ")
bstack111ll11ll_opy_ = bstack1l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲࡬ࡺࡨ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡲࡪࡾࡴࡠࡪࡸࡦࡸ࠭ᕤ")
bstack1l1l1l1l11l_opy_ = {
  bstack1l1_opy_ (u"ࠪࡧࡷ࡯ࡴࡪࡥࡤࡰࠬᕥ"): 50,
  bstack1l1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᕦ"): 40,
  bstack1l1_opy_ (u"ࠬࡽࡡࡳࡰ࡬ࡲ࡬࠭ᕧ"): 30,
  bstack1l1_opy_ (u"࠭ࡩ࡯ࡨࡲࠫᕨ"): 20,
  bstack1l1_opy_ (u"ࠧࡥࡧࡥࡹ࡬࠭ᕩ"): 10
}
bstack11ll11ll11_opy_ = bstack1l1l1l1l11l_opy_[bstack1l1_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭ᕪ")]
bstack11l11111ll_opy_ = bstack1l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠯ࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࠨᕫ")
bstack11l1ll1lll_opy_ = bstack1l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯ࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࠨᕬ")
bstack1ll1l1l111_opy_ = bstack1l1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨ࠱ࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࠪᕭ")
bstack11ll1ll1l1_opy_ = bstack1l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࠫᕮ")
bstack111l1l1l_opy_ = bstack1l1_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡱࡻࡷࡩࡸࡺࠠࡢࡰࡧࠤࡵࡿࡴࡦࡵࡷ࠱ࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠦࡰࡢࡥ࡮ࡥ࡬࡫ࡳ࠯ࠢࡣࡴ࡮ࡶࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴࠡࡲࡼࡸࡪࡹࡴ࠮ࡵࡨࡰࡪࡴࡩࡶ࡯ࡣࠫᕯ")
bstack1l1l1l1l111_opy_ = [bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨᕰ"), bstack1l1_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨᕱ")]
bstack1l1l1l1llll_opy_ = [bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬᕲ"), bstack1l1_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬᕳ")]
bstack1l1111lll1_opy_ = re.compile(bstack1l1_opy_ (u"ࠫࡣࡡ࡜࡝ࡹ࠰ࡡ࠰ࡀ࠮ࠫࠦࠪᕴ"))
bstack111l11lll_opy_ = [
  bstack1l1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡐࡤࡱࡪ࠭ᕵ"),
  bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᕶ"),
  bstack1l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫᕷ"),
  bstack1l1_opy_ (u"ࠨࡰࡨࡻࡈࡵ࡭࡮ࡣࡱࡨ࡙࡯࡭ࡦࡱࡸࡸࠬᕸ"),
  bstack1l1_opy_ (u"ࠩࡤࡴࡵ࠭ᕹ"),
  bstack1l1_opy_ (u"ࠪࡹࡩ࡯ࡤࠨᕺ"),
  bstack1l1_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪ࠭ᕻ"),
  bstack1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡩࠬᕼ"),
  bstack1l1_opy_ (u"࠭࡯ࡳ࡫ࡨࡲࡹࡧࡴࡪࡱࡱࠫᕽ"),
  bstack1l1_opy_ (u"ࠧࡢࡷࡷࡳ࡜࡫ࡢࡷ࡫ࡨࡻࠬᕾ"),
  bstack1l1_opy_ (u"ࠨࡰࡲࡖࡪࡹࡥࡵࠩᕿ"), bstack1l1_opy_ (u"ࠩࡩࡹࡱࡲࡒࡦࡵࡨࡸࠬᖀ"),
  bstack1l1_opy_ (u"ࠪࡧࡱ࡫ࡡࡳࡕࡼࡷࡹ࡫࡭ࡇ࡫࡯ࡩࡸ࠭ᖁ"),
  bstack1l1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡗ࡭ࡲ࡯࡮ࡨࡵࠪᖂ"),
  bstack1l1_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡕ࡫ࡲࡧࡱࡵࡱࡦࡴࡣࡦࡎࡲ࡫࡬࡯࡮ࡨࠩᖃ"),
  bstack1l1_opy_ (u"࠭࡯ࡵࡪࡨࡶࡆࡶࡰࡴࠩᖄ"),
  bstack1l1_opy_ (u"ࠧࡱࡴ࡬ࡲࡹࡖࡡࡨࡧࡖࡳࡺࡸࡣࡦࡑࡱࡊ࡮ࡴࡤࡇࡣ࡬ࡰࡺࡸࡥࠨᖅ"),
  bstack1l1_opy_ (u"ࠨࡣࡳࡴࡆࡩࡴࡪࡸ࡬ࡸࡾ࠭ᖆ"), bstack1l1_opy_ (u"ࠩࡤࡴࡵࡖࡡࡤ࡭ࡤ࡫ࡪ࠭ᖇ"), bstack1l1_opy_ (u"ࠪࡥࡵࡶࡗࡢ࡫ࡷࡅࡨࡺࡩࡷ࡫ࡷࡽࠬᖈ"), bstack1l1_opy_ (u"ࠫࡦࡶࡰࡘࡣ࡬ࡸࡕࡧࡣ࡬ࡣࡪࡩࠬᖉ"), bstack1l1_opy_ (u"ࠬࡧࡰࡱ࡙ࡤ࡭ࡹࡊࡵࡳࡣࡷ࡭ࡴࡴࠧᖊ"),
  bstack1l1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡘࡥࡢࡦࡼࡘ࡮ࡳࡥࡰࡷࡷࠫᖋ"),
  bstack1l1_opy_ (u"ࠧࡢ࡮࡯ࡳࡼ࡚ࡥࡴࡶࡓࡥࡨࡱࡡࡨࡧࡶࠫᖌ"),
  bstack1l1_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࡅࡲࡺࡪࡸࡡࡨࡧࠪᖍ"), bstack1l1_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡆࡳࡻ࡫ࡲࡢࡩࡨࡉࡳࡪࡉ࡯ࡶࡨࡲࡹ࠭ᖎ"),
  bstack1l1_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࡈࡪࡼࡩࡤࡧࡕࡩࡦࡪࡹࡕ࡫ࡰࡩࡴࡻࡴࠨᖏ"),
  bstack1l1_opy_ (u"ࠫࡦࡪࡢࡑࡱࡵࡸࠬᖐ"),
  bstack1l1_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩࡊࡥࡷ࡫ࡦࡩࡘࡵࡣ࡬ࡧࡷࠫᖑ"),
  bstack1l1_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࡉ࡯ࡵࡷࡥࡱࡲࡔࡪ࡯ࡨࡳࡺࡺࠧᖒ"),
  bstack1l1_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࡊࡰࡶࡸࡦࡲ࡬ࡑࡣࡷ࡬ࠬᖓ"),
  bstack1l1_opy_ (u"ࠨࡣࡹࡨࠬᖔ"), bstack1l1_opy_ (u"ࠩࡤࡺࡩࡒࡡࡶࡰࡦ࡬࡙࡯࡭ࡦࡱࡸࡸࠬᖕ"), bstack1l1_opy_ (u"ࠪࡥࡻࡪࡒࡦࡣࡧࡽ࡙࡯࡭ࡦࡱࡸࡸࠬᖖ"), bstack1l1_opy_ (u"ࠫࡦࡼࡤࡂࡴࡪࡷࠬᖗ"),
  bstack1l1_opy_ (u"ࠬࡻࡳࡦࡍࡨࡽࡸࡺ࡯ࡳࡧࠪᖘ"), bstack1l1_opy_ (u"࠭࡫ࡦࡻࡶࡸࡴࡸࡥࡑࡣࡷ࡬ࠬᖙ"), bstack1l1_opy_ (u"ࠧ࡬ࡧࡼࡷࡹࡵࡲࡦࡒࡤࡷࡸࡽ࡯ࡳࡦࠪᖚ"),
  bstack1l1_opy_ (u"ࠨ࡭ࡨࡽࡆࡲࡩࡢࡵࠪᖛ"), bstack1l1_opy_ (u"ࠩ࡮ࡩࡾࡖࡡࡴࡵࡺࡳࡷࡪࠧᖜ"),
  bstack1l1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡇࡻࡩࡨࡻࡴࡢࡤ࡯ࡩࠬᖝ"), bstack1l1_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡨࡷ࡯ࡶࡦࡴࡄࡶ࡬ࡹࠧᖞ"), bstack1l1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡩࡸࡩࡷࡧࡵࡉࡽ࡫ࡣࡶࡶࡤࡦࡱ࡫ࡄࡪࡴࠪᖟ"), bstack1l1_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡪࡲࡪࡸࡨࡶࡈ࡮ࡲࡰ࡯ࡨࡑࡦࡶࡰࡪࡰࡪࡊ࡮ࡲࡥࠨᖠ"), bstack1l1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷ࡛ࡳࡦࡕࡼࡷࡹ࡫࡭ࡆࡺࡨࡧࡺࡺࡡࡣ࡮ࡨࠫᖡ"),
  bstack1l1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡥࡴ࡬ࡺࡪࡸࡐࡰࡴࡷࠫᖢ"), bstack1l1_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡦࡵ࡭ࡻ࡫ࡲࡑࡱࡵࡸࡸ࠭ᖣ"),
  bstack1l1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡆ࡬ࡷࡦࡨ࡬ࡦࡄࡸ࡭ࡱࡪࡃࡩࡧࡦ࡯ࠬᖤ"),
  bstack1l1_opy_ (u"ࠫࡦࡻࡴࡰ࡙ࡨࡦࡻ࡯ࡥࡸࡖ࡬ࡱࡪࡵࡵࡵࠩᖥ"),
  bstack1l1_opy_ (u"ࠬ࡯࡮ࡵࡧࡱࡸࡆࡩࡴࡪࡱࡱࠫᖦ"), bstack1l1_opy_ (u"࠭ࡩ࡯ࡶࡨࡲࡹࡉࡡࡵࡧࡪࡳࡷࡿࠧᖧ"), bstack1l1_opy_ (u"ࠧࡪࡰࡷࡩࡳࡺࡆ࡭ࡣࡪࡷࠬᖨ"), bstack1l1_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡢ࡮ࡌࡲࡹ࡫࡮ࡵࡃࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᖩ"),
  bstack1l1_opy_ (u"ࠩࡧࡳࡳࡺࡓࡵࡱࡳࡅࡵࡶࡏ࡯ࡔࡨࡷࡪࡺࠧᖪ"),
  bstack1l1_opy_ (u"ࠪࡹࡳ࡯ࡣࡰࡦࡨࡏࡪࡿࡢࡰࡣࡵࡨࠬᖫ"), bstack1l1_opy_ (u"ࠫࡷ࡫ࡳࡦࡶࡎࡩࡾࡨ࡯ࡢࡴࡧࠫᖬ"),
  bstack1l1_opy_ (u"ࠬࡴ࡯ࡔ࡫ࡪࡲࠬᖭ"),
  bstack1l1_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪ࡛࡮ࡪ࡯ࡳࡳࡷࡺࡡ࡯ࡶ࡙࡭ࡪࡽࡳࠨᖮ"),
  bstack1l1_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡰࡧࡶࡴ࡯ࡤࡘࡣࡷࡧ࡭࡫ࡲࡴࠩᖯ"),
  bstack1l1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᖰ"),
  bstack1l1_opy_ (u"ࠩࡵࡩࡨࡸࡥࡢࡶࡨࡇ࡭ࡸ࡯࡮ࡧࡇࡶ࡮ࡼࡥࡳࡕࡨࡷࡸ࡯࡯࡯ࡵࠪᖱ"),
  bstack1l1_opy_ (u"ࠪࡲࡦࡺࡩࡷࡧ࡚ࡩࡧ࡙ࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠩᖲ"),
  bstack1l1_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࡘࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡑࡣࡷ࡬ࠬᖳ"),
  bstack1l1_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰ࡙ࡰࡦࡧࡧࠫᖴ"),
  bstack1l1_opy_ (u"࠭ࡧࡱࡵࡈࡲࡦࡨ࡬ࡦࡦࠪᖵ"),
  bstack1l1_opy_ (u"ࠧࡪࡵࡋࡩࡦࡪ࡬ࡦࡵࡶࠫᖶ"),
  bstack1l1_opy_ (u"ࠨࡣࡧࡦࡊࡾࡥࡤࡖ࡬ࡱࡪࡵࡵࡵࠩᖷ"),
  bstack1l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡦࡕࡦࡶ࡮ࡶࡴࠨᖸ"),
  bstack1l1_opy_ (u"ࠪࡷࡰ࡯ࡰࡅࡧࡹ࡭ࡨ࡫ࡉ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡣࡷ࡭ࡴࡴࠧᖹ"),
  bstack1l1_opy_ (u"ࠫࡦࡻࡴࡰࡉࡵࡥࡳࡺࡐࡦࡴࡰ࡭ࡸࡹࡩࡰࡰࡶࠫᖺ"),
  bstack1l1_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩࡔࡡࡵࡷࡵࡥࡱࡕࡲࡪࡧࡱࡸࡦࡺࡩࡰࡰࠪᖻ"),
  bstack1l1_opy_ (u"࠭ࡳࡺࡵࡷࡩࡲࡖ࡯ࡳࡶࠪᖼ"),
  bstack1l1_opy_ (u"ࠧࡳࡧࡰࡳࡹ࡫ࡁࡥࡤࡋࡳࡸࡺࠧᖽ"),
  bstack1l1_opy_ (u"ࠨࡵ࡮࡭ࡵ࡛࡮࡭ࡱࡦ࡯ࠬᖾ"), bstack1l1_opy_ (u"ࠩࡸࡲࡱࡵࡣ࡬ࡖࡼࡴࡪ࠭ᖿ"), bstack1l1_opy_ (u"ࠪࡹࡳࡲ࡯ࡤ࡭ࡎࡩࡾ࠭ᗀ"),
  bstack1l1_opy_ (u"ࠫࡦࡻࡴࡰࡎࡤࡹࡳࡩࡨࠨᗁ"),
  bstack1l1_opy_ (u"ࠬࡹ࡫ࡪࡲࡏࡳ࡬ࡩࡡࡵࡅࡤࡴࡹࡻࡲࡦࠩᗂ"),
  bstack1l1_opy_ (u"࠭ࡵ࡯࡫ࡱࡷࡹࡧ࡬࡭ࡑࡷ࡬ࡪࡸࡐࡢࡥ࡮ࡥ࡬࡫ࡳࠨᗃ"),
  bstack1l1_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡘ࡫ࡱࡨࡴࡽࡁ࡯࡫ࡰࡥࡹ࡯࡯࡯ࠩᗄ"),
  bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡔࡰࡱ࡯ࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬᗅ"),
  bstack1l1_opy_ (u"ࠩࡨࡲ࡫ࡵࡲࡤࡧࡄࡴࡵࡏ࡮ࡴࡶࡤࡰࡱ࠭ᗆ"),
  bstack1l1_opy_ (u"ࠪࡩࡳࡹࡵࡳࡧ࡚ࡩࡧࡼࡩࡦࡹࡶࡌࡦࡼࡥࡑࡣࡪࡩࡸ࠭ᗇ"), bstack1l1_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࡉ࡫ࡶࡵࡱࡲࡰࡸࡖ࡯ࡳࡶࠪᗈ"), bstack1l1_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩ࡜࡫ࡢࡷ࡫ࡨࡻࡉ࡫ࡴࡢ࡫࡯ࡷࡈࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࠨᗉ"),
  bstack1l1_opy_ (u"࠭ࡲࡦ࡯ࡲࡸࡪࡇࡰࡱࡵࡆࡥࡨ࡮ࡥࡍ࡫ࡰ࡭ࡹ࠭ᗊ"),
  bstack1l1_opy_ (u"ࠧࡤࡣ࡯ࡩࡳࡪࡡࡳࡈࡲࡶࡲࡧࡴࠨᗋ"),
  bstack1l1_opy_ (u"ࠨࡤࡸࡲࡩࡲࡥࡊࡦࠪᗌ"),
  bstack1l1_opy_ (u"ࠩ࡯ࡥࡺࡴࡣࡩࡖ࡬ࡱࡪࡵࡵࡵࠩᗍ"),
  bstack1l1_opy_ (u"ࠪࡰࡴࡩࡡࡵ࡫ࡲࡲࡘ࡫ࡲࡷ࡫ࡦࡩࡸࡋ࡮ࡢࡤ࡯ࡩࡩ࠭ᗎ"), bstack1l1_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࡙ࡥࡳࡸ࡬ࡧࡪࡹࡁࡶࡶ࡫ࡳࡷ࡯ࡺࡦࡦࠪᗏ"),
  bstack1l1_opy_ (u"ࠬࡧࡵࡵࡱࡄࡧࡨ࡫ࡰࡵࡃ࡯ࡩࡷࡺࡳࠨᗐ"), bstack1l1_opy_ (u"࠭ࡡࡶࡶࡲࡈ࡮ࡹ࡭ࡪࡵࡶࡅࡱ࡫ࡲࡵࡵࠪᗑ"),
  bstack1l1_opy_ (u"ࠧ࡯ࡣࡷ࡭ࡻ࡫ࡉ࡯ࡵࡷࡶࡺࡳࡥ࡯ࡶࡶࡐ࡮ࡨࠧᗒ"),
  bstack1l1_opy_ (u"ࠨࡰࡤࡸ࡮ࡼࡥࡘࡧࡥࡘࡦࡶࠧᗓ"),
  bstack1l1_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࡋࡱ࡭ࡹ࡯ࡡ࡭ࡗࡵࡰࠬᗔ"), bstack1l1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࡄࡰࡱࡵࡷࡑࡱࡳࡹࡵࡹࠧᗕ"), bstack1l1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࡍ࡬ࡴ࡯ࡳࡧࡉࡶࡦࡻࡤࡘࡣࡵࡲ࡮ࡴࡧࠨᗖ"), bstack1l1_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࡔࡶࡥ࡯ࡎ࡬ࡲࡰࡹࡉ࡯ࡄࡤࡧࡰ࡭ࡲࡰࡷࡱࡨࠬᗗ"),
  bstack1l1_opy_ (u"࠭࡫ࡦࡧࡳࡏࡪࡿࡃࡩࡣ࡬ࡲࡸ࠭ᗘ"),
  bstack1l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࡯ࡺࡢࡤ࡯ࡩࡘࡺࡲࡪࡰࡪࡷࡉ࡯ࡲࠨᗙ"),
  bstack1l1_opy_ (u"ࠨࡲࡵࡳࡨ࡫ࡳࡴࡃࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᗚ"),
  bstack1l1_opy_ (u"ࠩ࡬ࡲࡹ࡫ࡲࡌࡧࡼࡈࡪࡲࡡࡺࠩᗛ"),
  bstack1l1_opy_ (u"ࠪࡷ࡭ࡵࡷࡊࡑࡖࡐࡴ࡭ࠧᗜ"),
  bstack1l1_opy_ (u"ࠫࡸ࡫࡮ࡥࡍࡨࡽࡘࡺࡲࡢࡶࡨ࡫ࡾ࠭ᗝ"),
  bstack1l1_opy_ (u"ࠬࡽࡥࡣ࡭࡬ࡸࡗ࡫ࡳࡱࡱࡱࡷࡪ࡚ࡩ࡮ࡧࡲࡹࡹ࠭ᗞ"), bstack1l1_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶ࡚ࡥ࡮ࡺࡔࡪ࡯ࡨࡳࡺࡺࠧᗟ"),
  bstack1l1_opy_ (u"ࠧࡳࡧࡰࡳࡹ࡫ࡄࡦࡤࡸ࡫ࡕࡸ࡯ࡹࡻࠪᗠ"),
  bstack1l1_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡂࡵࡼࡲࡨࡋࡸࡦࡥࡸࡸࡪࡌࡲࡰ࡯ࡋࡸࡹࡶࡳࠨᗡ"),
  bstack1l1_opy_ (u"ࠩࡶ࡯࡮ࡶࡌࡰࡩࡆࡥࡵࡺࡵࡳࡧࠪᗢ"),
  bstack1l1_opy_ (u"ࠪࡻࡪࡨ࡫ࡪࡶࡇࡩࡧࡻࡧࡑࡴࡲࡼࡾࡖ࡯ࡳࡶࠪᗣ"),
  bstack1l1_opy_ (u"ࠫ࡫ࡻ࡬࡭ࡅࡲࡲࡹ࡫ࡸࡵࡎ࡬ࡷࡹ࠭ᗤ"),
  bstack1l1_opy_ (u"ࠬࡽࡡࡪࡶࡉࡳࡷࡇࡰࡱࡕࡦࡶ࡮ࡶࡴࠨᗥ"),
  bstack1l1_opy_ (u"࠭ࡷࡦࡤࡹ࡭ࡪࡽࡃࡰࡰࡱࡩࡨࡺࡒࡦࡶࡵ࡭ࡪࡹࠧᗦ"),
  bstack1l1_opy_ (u"ࠧࡢࡲࡳࡒࡦࡳࡥࠨᗧ"),
  bstack1l1_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡔࡕࡏࡇࡪࡸࡴࠨᗨ"),
  bstack1l1_opy_ (u"ࠩࡷࡥࡵ࡝ࡩࡵࡪࡖ࡬ࡴࡸࡴࡑࡴࡨࡷࡸࡊࡵࡳࡣࡷ࡭ࡴࡴࠧᗩ"),
  bstack1l1_opy_ (u"ࠪࡷࡨࡧ࡬ࡦࡈࡤࡧࡹࡵࡲࠨᗪ"),
  bstack1l1_opy_ (u"ࠫࡼࡪࡡࡍࡱࡦࡥࡱࡖ࡯ࡳࡶࠪᗫ"),
  bstack1l1_opy_ (u"ࠬࡹࡨࡰࡹ࡛ࡧࡴࡪࡥࡍࡱࡪࠫᗬ"),
  bstack1l1_opy_ (u"࠭ࡩࡰࡵࡌࡲࡸࡺࡡ࡭࡮ࡓࡥࡺࡹࡥࠨᗭ"),
  bstack1l1_opy_ (u"ࠧࡹࡥࡲࡨࡪࡉ࡯࡯ࡨ࡬࡫ࡋ࡯࡬ࡦࠩᗮ"),
  bstack1l1_opy_ (u"ࠨ࡭ࡨࡽࡨ࡮ࡡࡪࡰࡓࡥࡸࡹࡷࡰࡴࡧࠫᗯ"),
  bstack1l1_opy_ (u"ࠩࡸࡷࡪࡖࡲࡦࡤࡸ࡭ࡱࡺࡗࡅࡃࠪᗰ"),
  bstack1l1_opy_ (u"ࠪࡴࡷ࡫ࡶࡦࡰࡷ࡛ࡉࡇࡁࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠫᗱ"),
  bstack1l1_opy_ (u"ࠫࡼ࡫ࡢࡅࡴ࡬ࡺࡪࡸࡁࡨࡧࡱࡸ࡚ࡸ࡬ࠨᗲ"),
  bstack1l1_opy_ (u"ࠬࡱࡥࡺࡥ࡫ࡥ࡮ࡴࡐࡢࡶ࡫ࠫᗳ"),
  bstack1l1_opy_ (u"࠭ࡵࡴࡧࡑࡩࡼ࡝ࡄࡂࠩᗴ"),
  bstack1l1_opy_ (u"ࠧࡸࡦࡤࡐࡦࡻ࡮ࡤࡪࡗ࡭ࡲ࡫࡯ࡶࡶࠪᗵ"), bstack1l1_opy_ (u"ࠨࡹࡧࡥࡈࡵ࡮࡯ࡧࡦࡸ࡮ࡵ࡮ࡕ࡫ࡰࡩࡴࡻࡴࠨᗶ"),
  bstack1l1_opy_ (u"ࠩࡻࡧࡴࡪࡥࡐࡴࡪࡍࡩ࠭ᗷ"), bstack1l1_opy_ (u"ࠪࡼࡨࡵࡤࡦࡕ࡬࡫ࡳ࡯࡮ࡨࡋࡧࠫᗸ"),
  bstack1l1_opy_ (u"ࠫࡺࡶࡤࡢࡶࡨࡨ࡜ࡊࡁࡃࡷࡱࡨࡱ࡫ࡉࡥࠩᗹ"),
  bstack1l1_opy_ (u"ࠬࡸࡥࡴࡧࡷࡓࡳ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡴࡷࡓࡳࡲࡹࠨᗺ"),
  bstack1l1_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡔࡪ࡯ࡨࡳࡺࡺࡳࠨᗻ"),
  bstack1l1_opy_ (u"ࠧࡸࡦࡤࡗࡹࡧࡲࡵࡷࡳࡖࡪࡺࡲࡪࡧࡶࠫᗼ"), bstack1l1_opy_ (u"ࠨࡹࡧࡥࡘࡺࡡࡳࡶࡸࡴࡗ࡫ࡴࡳࡻࡌࡲࡹ࡫ࡲࡷࡣ࡯ࠫᗽ"),
  bstack1l1_opy_ (u"ࠩࡦࡳࡳࡴࡥࡤࡶࡋࡥࡷࡪࡷࡢࡴࡨࡏࡪࡿࡢࡰࡣࡵࡨࠬᗾ"),
  bstack1l1_opy_ (u"ࠪࡱࡦࡾࡔࡺࡲ࡬ࡲ࡬ࡌࡲࡦࡳࡸࡩࡳࡩࡹࠨᗿ"),
  bstack1l1_opy_ (u"ࠫࡸ࡯࡭ࡱ࡮ࡨࡍࡸ࡜ࡩࡴ࡫ࡥࡰࡪࡉࡨࡦࡥ࡮ࠫᘀ"),
  bstack1l1_opy_ (u"ࠬࡻࡳࡦࡅࡤࡶࡹ࡮ࡡࡨࡧࡖࡷࡱ࠭ᘁ"),
  bstack1l1_opy_ (u"࠭ࡳࡩࡱࡸࡰࡩ࡛ࡳࡦࡕ࡬ࡲ࡬ࡲࡥࡵࡱࡱࡘࡪࡹࡴࡎࡣࡱࡥ࡬࡫ࡲࠨᘂ"),
  bstack1l1_opy_ (u"ࠧࡴࡶࡤࡶࡹࡏࡗࡅࡒࠪᘃ"),
  bstack1l1_opy_ (u"ࠨࡣ࡯ࡰࡴࡽࡔࡰࡷࡦ࡬ࡎࡪࡅ࡯ࡴࡲࡰࡱ࠭ᘄ"),
  bstack1l1_opy_ (u"ࠩ࡬࡫ࡳࡵࡲࡦࡊ࡬ࡨࡩ࡫࡮ࡂࡲ࡬ࡔࡴࡲࡩࡤࡻࡈࡶࡷࡵࡲࠨᘅ"),
  bstack1l1_opy_ (u"ࠪࡱࡴࡩ࡫ࡍࡱࡦࡥࡹ࡯࡯࡯ࡃࡳࡴࠬᘆ"),
  bstack1l1_opy_ (u"ࠫࡱࡵࡧࡤࡣࡷࡊࡴࡸ࡭ࡢࡶࠪᘇ"), bstack1l1_opy_ (u"ࠬࡲ࡯ࡨࡥࡤࡸࡋ࡯࡬ࡵࡧࡵࡗࡵ࡫ࡣࡴࠩᘈ"),
  bstack1l1_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡉ࡫࡬ࡢࡻࡄࡨࡧ࠭ᘉ"),
  bstack1l1_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡊࡦࡏࡳࡨࡧࡴࡰࡴࡄࡹࡹࡵࡣࡰ࡯ࡳࡰࡪࡺࡩࡰࡰࠪᘊ")
]
bstack11l1l1l1l_opy_ = bstack1l1_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡴ࡮࠳ࡣ࡭ࡱࡸࡨ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫࠯ࡶࡲ࡯ࡳࡦࡪࠧᘋ")
bstack1ll111lll1_opy_ = [bstack1l1_opy_ (u"ࠩ࠱ࡥࡵࡱࠧᘌ"), bstack1l1_opy_ (u"ࠪ࠲ࡦࡧࡢࠨᘍ"), bstack1l1_opy_ (u"ࠫ࠳࡯ࡰࡢࠩᘎ")]
bstack11l1ll11l_opy_ = [bstack1l1_opy_ (u"ࠬ࡯ࡤࠨᘏ"), bstack1l1_opy_ (u"࠭ࡰࡢࡶ࡫ࠫᘐ"), bstack1l1_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪᘑ"), bstack1l1_opy_ (u"ࠨࡵ࡫ࡥࡷ࡫ࡡࡣ࡮ࡨࡣ࡮ࡪࠧᘒ")]
bstack1llll1l1ll_opy_ = {
  bstack1l1_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᘓ"): bstack1l1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᘔ"),
  bstack1l1_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࡔࡶࡴࡪࡱࡱࡷࠬᘕ"): bstack1l1_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡩ࡭ࡷ࡫ࡦࡰࡺࡒࡴࡹ࡯࡯࡯ࡵࠪᘖ"),
  bstack1l1_opy_ (u"࠭ࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫᘗ"): bstack1l1_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᘘ"),
  bstack1l1_opy_ (u"ࠨ࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫᘙ"): bstack1l1_opy_ (u"ࠩࡶࡩ࠿࡯ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᘚ"),
  bstack1l1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࡒࡴࡹ࡯࡯࡯ࡵࠪᘛ"): bstack1l1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬᘜ")
}
bstack1l11l1lll1_opy_ = [
  bstack1l1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᘝ"),
  bstack1l1_opy_ (u"࠭࡭ࡰࡼ࠽ࡪ࡮ࡸࡥࡧࡱࡻࡓࡵࡺࡩࡰࡰࡶࠫᘞ"),
  bstack1l1_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᘟ"),
  bstack1l1_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᘠ"),
  bstack1l1_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪᘡ"),
]
bstack11ll11ll1_opy_ = bstack1l1l11ll1_opy_ + bstack1l1l1ll11l1_opy_ + bstack111l11lll_opy_
bstack111ll1ll1_opy_ = [
  bstack1l1_opy_ (u"ࠪࡢࡱࡵࡣࡢ࡮࡫ࡳࡸࡺࠤࠨᘢ"),
  bstack1l1_opy_ (u"ࠫࡣࡨࡳ࠮࡮ࡲࡧࡦࡲ࠮ࡤࡱࡰࠨࠬᘣ"),
  bstack1l1_opy_ (u"ࠬࡤ࠱࠳࠹࠱ࠫᘤ"),
  bstack1l1_opy_ (u"࠭࡞࠲࠲࠱ࠫᘥ"),
  bstack1l1_opy_ (u"ࠧ࡟࠳࠺࠶࠳࠷࡛࠷࠯࠼ࡡ࠳࠭ᘦ"),
  bstack1l1_opy_ (u"ࠨࡠ࠴࠻࠷࠴࠲࡜࠲࠰࠽ࡢ࠴ࠧᘧ"),
  bstack1l1_opy_ (u"ࠩࡡ࠵࠼࠸࠮࠴࡝࠳࠱࠶ࡣ࠮ࠨᘨ"),
  bstack1l1_opy_ (u"ࠪࡢ࠶࠿࠲࠯࠳࠹࠼࠳࠭ᘩ")
]
bstack1l1l1l1ll11_opy_ = bstack1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬᘪ")
bstack1lll11ll1l_opy_ = bstack1l1_opy_ (u"ࠬࡹࡤ࡬࠱ࡹ࠵࠴࡫ࡶࡦࡰࡷࠫᘫ")
bstack1l1l1l1l11_opy_ = [ bstack1l1_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨᘬ") ]
bstack111ll1l1l_opy_ = [ bstack1l1_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᘭ") ]
bstack1l11ll1l1_opy_ = [bstack1l1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬᘮ")]
bstack1l111l11l1_opy_ = [ bstack1l1_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩᘯ") ]
bstack1l11l11ll1_opy_ = bstack1l1_opy_ (u"ࠪࡗࡉࡑࡓࡦࡶࡸࡴࠬᘰ")
bstack1l1lll11l1_opy_ = bstack1l1_opy_ (u"ࠫࡘࡊࡋࡕࡧࡶࡸࡆࡺࡴࡦ࡯ࡳࡸࡪࡪࠧᘱ")
bstack11ll1111l_opy_ = bstack1l1_opy_ (u"࡙ࠬࡄࡌࡖࡨࡷࡹ࡙ࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠩᘲ")
bstack1ll11l111l_opy_ = bstack1l1_opy_ (u"࠭࠴࠯࠲࠱࠴ࠬᘳ")
bstack1l1l11ll11_opy_ = [
  bstack1l1_opy_ (u"ࠧࡆࡔࡕࡣࡋࡇࡉࡍࡇࡇࠫᘴ"),
  bstack1l1_opy_ (u"ࠨࡇࡕࡖࡤ࡚ࡉࡎࡇࡇࡣࡔ࡛ࡔࠨᘵ"),
  bstack1l1_opy_ (u"ࠩࡈࡖࡗࡥࡂࡍࡑࡆࡏࡊࡊ࡟ࡃ࡛ࡢࡇࡑࡏࡅࡏࡖࠪᘶ"),
  bstack1l1_opy_ (u"ࠪࡉࡗࡘ࡟ࡏࡇࡗ࡛ࡔࡘࡋࡠࡅࡋࡅࡓࡍࡅࡅࠩᘷ"),
  bstack1l1_opy_ (u"ࠫࡊࡘࡒࡠࡕࡒࡇࡐࡋࡔࡠࡐࡒࡘࡤࡉࡏࡏࡐࡈࡇ࡙ࡋࡄࠨᘸ"),
  bstack1l1_opy_ (u"ࠬࡋࡒࡓࡡࡆࡓࡓࡔࡅࡄࡖࡌࡓࡓࡥࡃࡍࡑࡖࡉࡉ࠭ᘹ"),
  bstack1l1_opy_ (u"࠭ࡅࡓࡔࡢࡇࡔࡔࡎࡆࡅࡗࡍࡔࡔ࡟ࡓࡇࡖࡉ࡙࠭ᘺ"),
  bstack1l1_opy_ (u"ࠧࡆࡔࡕࡣࡈࡕࡎࡏࡇࡆࡘࡎࡕࡎࡠࡔࡈࡊ࡚࡙ࡅࡅࠩᘻ"),
  bstack1l1_opy_ (u"ࠨࡇࡕࡖࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡄࡆࡔࡘࡔࡆࡆࠪᘼ"),
  bstack1l1_opy_ (u"ࠩࡈࡖࡗࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡊࡆࡏࡌࡆࡆࠪᘽ"),
  bstack1l1_opy_ (u"ࠪࡉࡗࡘ࡟ࡏࡃࡐࡉࡤࡔࡏࡕࡡࡕࡉࡘࡕࡌࡗࡇࡇࠫᘾ"),
  bstack1l1_opy_ (u"ࠫࡊࡘࡒࡠࡃࡇࡈࡗࡋࡓࡔࡡࡌࡒ࡛ࡇࡌࡊࡆࠪᘿ"),
  bstack1l1_opy_ (u"ࠬࡋࡒࡓࡡࡄࡈࡉࡘࡅࡔࡕࡢ࡙ࡓࡘࡅࡂࡅࡋࡅࡇࡒࡅࠨᙀ"),
  bstack1l1_opy_ (u"࠭ࡅࡓࡔࡢࡘ࡚ࡔࡎࡆࡎࡢࡇࡔࡔࡎࡆࡅࡗࡍࡔࡔ࡟ࡇࡃࡌࡐࡊࡊࠧᙁ"),
  bstack1l1_opy_ (u"ࠧࡆࡔࡕࡣࡈࡕࡎࡏࡇࡆࡘࡎࡕࡎࡠࡖࡌࡑࡊࡊ࡟ࡐࡗࡗࠫᙂ"),
  bstack1l1_opy_ (u"ࠨࡇࡕࡖࡤ࡙ࡏࡄࡍࡖࡣࡈࡕࡎࡏࡇࡆࡘࡎࡕࡎࡠࡈࡄࡍࡑࡋࡄࠨᙃ"),
  bstack1l1_opy_ (u"ࠩࡈࡖࡗࡥࡓࡐࡅࡎࡗࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡋࡓࡘ࡚࡟ࡖࡐࡕࡉࡆࡉࡈࡂࡄࡏࡉࠬᙄ"),
  bstack1l1_opy_ (u"ࠪࡉࡗࡘ࡟ࡑࡔࡒ࡜࡞ࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡊࡆࡏࡌࡆࡆࠪᙅ"),
  bstack1l1_opy_ (u"ࠫࡊࡘࡒࡠࡐࡄࡑࡊࡥࡎࡐࡖࡢࡖࡊ࡙ࡏࡍࡘࡈࡈࠬᙆ"),
  bstack1l1_opy_ (u"ࠬࡋࡒࡓࡡࡑࡅࡒࡋ࡟ࡓࡇࡖࡓࡑ࡛ࡔࡊࡑࡑࡣࡋࡇࡉࡍࡇࡇࠫᙇ"),
  bstack1l1_opy_ (u"࠭ࡅࡓࡔࡢࡑࡆࡔࡄࡂࡖࡒࡖ࡞ࡥࡐࡓࡑ࡛࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤࡌࡁࡊࡎࡈࡈࠬᙈ"),
]
bstack11lll1lll_opy_ = bstack1l1_opy_ (u"ࠧ࠯࠱ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠮ࡣࡵࡸ࡮࡬ࡡࡤࡶࡶ࠳ࠬᙉ")
bstack1111l1ll1_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠨࢀࠪᙊ")), bstack1l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᙋ"), bstack1l1_opy_ (u"ࠪ࠲ࡧࡹࡴࡢࡥ࡮࠱ࡨࡵ࡮ࡧ࡫ࡪ࠲࡯ࡹ࡯࡯ࠩᙌ"))
bstack1l1l1l1l1l1_opy_ = bstack1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡣࡳ࡭ࠬᙍ")
bstack1l1l1l1l1ll_opy_ = [ bstack1l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᙎ"), bstack1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬᙏ"), bstack1l1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ᙐ"), bstack1l1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨᙑ")]
bstack111ll111l_opy_ = [ bstack1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᙒ"), bstack1l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩᙓ"), bstack1l1_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪᙔ"), bstack1l1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬᙕ") ]
bstack1llll1ll_opy_ = {
  bstack1l1_opy_ (u"࠭ࡐࡂࡕࡖࠫᙖ"): bstack1l1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᙗ"),
  bstack1l1_opy_ (u"ࠨࡈࡄࡍࡑ࠭ᙘ"): bstack1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᙙ"),
  bstack1l1_opy_ (u"ࠪࡗࡐࡏࡐࠨᙚ"): bstack1l1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬᙛ")
}
bstack1lll111l1_opy_ = [
  bstack1l1_opy_ (u"ࠧ࡭ࡥࡵࠤᙜ"),
  bstack1l1_opy_ (u"ࠨࡧࡰࡄࡤࡧࡰࠨᙝ"),
  bstack1l1_opy_ (u"ࠢࡨࡱࡉࡳࡷࡽࡡࡳࡦࠥᙞ"),
  bstack1l1_opy_ (u"ࠣࡴࡨࡪࡷ࡫ࡳࡩࠤᙟ"),
  bstack1l1_opy_ (u"ࠤࡦࡰ࡮ࡩ࡫ࡆ࡮ࡨࡱࡪࡴࡴࠣᙠ"),
  bstack1l1_opy_ (u"ࠥࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠢᙡ"),
  bstack1l1_opy_ (u"ࠦࡸࡻࡢ࡮࡫ࡷࡉࡱ࡫࡭ࡦࡰࡷࠦᙢ"),
  bstack1l1_opy_ (u"ࠧࡹࡥ࡯ࡦࡎࡩࡾࡹࡔࡰࡇ࡯ࡩࡲ࡫࡮ࡵࠤᙣ"),
  bstack1l1_opy_ (u"ࠨࡳࡦࡰࡧࡏࡪࡿࡳࡕࡱࡄࡧࡹ࡯ࡶࡦࡇ࡯ࡩࡲ࡫࡮ࡵࠤᙤ"),
  bstack1l1_opy_ (u"ࠢࡤ࡮ࡨࡥࡷࡋ࡬ࡦ࡯ࡨࡲࡹࠨᙥ"),
  bstack1l1_opy_ (u"ࠣࡣࡦࡸ࡮ࡵ࡮ࡴࠤᙦ"),
  bstack1l1_opy_ (u"ࠤࡨࡼࡪࡩࡵࡵࡧࡖࡧࡷ࡯ࡰࡵࠤᙧ"),
  bstack1l1_opy_ (u"ࠥࡩࡽ࡫ࡣࡶࡶࡨࡅࡸࡿ࡮ࡤࡕࡦࡶ࡮ࡶࡴࠣᙨ"),
  bstack1l1_opy_ (u"ࠦࡨࡲ࡯ࡴࡧࠥᙩ"),
  bstack1l1_opy_ (u"ࠧࡷࡵࡪࡶࠥᙪ"),
  bstack1l1_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳࡔࡰࡷࡦ࡬ࡆࡩࡴࡪࡱࡱࠦᙫ"),
  bstack1l1_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡎࡷ࡯ࡸ࡮࡚࡯ࡶࡥ࡫ࠦᙬ"),
  bstack1l1_opy_ (u"ࠣࡵ࡫ࡥࡰ࡫ࠢ᙭"),
  bstack1l1_opy_ (u"ࠤࡦࡰࡴࡹࡥࡂࡲࡳࠦ᙮")
]
bstack1l1l1l11lll_opy_ = [
  bstack1l1_opy_ (u"ࠥࡧࡱ࡯ࡣ࡬ࠤᙯ"),
  bstack1l1_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣᙰ"),
  bstack1l1_opy_ (u"ࠧࡧࡵࡵࡱࠥᙱ"),
  bstack1l1_opy_ (u"ࠨ࡭ࡢࡰࡸࡥࡱࠨᙲ"),
  bstack1l1_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤᙳ")
]
bstack1l1ll111ll_opy_ = {
  bstack1l1_opy_ (u"ࠣࡥ࡯࡭ࡨࡱࠢᙴ"): [bstack1l1_opy_ (u"ࠤࡦࡰ࡮ࡩ࡫ࡆ࡮ࡨࡱࡪࡴࡴࠣᙵ")],
  bstack1l1_opy_ (u"ࠥࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠢᙶ"): [bstack1l1_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣᙷ")],
  bstack1l1_opy_ (u"ࠧࡧࡵࡵࡱࠥᙸ"): [bstack1l1_opy_ (u"ࠨࡳࡦࡰࡧࡏࡪࡿࡳࡕࡱࡈࡰࡪࡳࡥ࡯ࡶࠥᙹ"), bstack1l1_opy_ (u"ࠢࡴࡧࡱࡨࡐ࡫ࡹࡴࡖࡲࡅࡨࡺࡩࡷࡧࡈࡰࡪࡳࡥ࡯ࡶࠥᙺ"), bstack1l1_opy_ (u"ࠣࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠧᙻ"), bstack1l1_opy_ (u"ࠤࡦࡰ࡮ࡩ࡫ࡆ࡮ࡨࡱࡪࡴࡴࠣᙼ")],
  bstack1l1_opy_ (u"ࠥࡱࡦࡴࡵࡢ࡮ࠥᙽ"): [bstack1l1_opy_ (u"ࠦࡲࡧ࡮ࡶࡣ࡯ࠦᙾ")],
  bstack1l1_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢᙿ"): [bstack1l1_opy_ (u"ࠨࡴࡦࡵࡷࡧࡦࡹࡥࠣ ")],
}
bstack1l1l1l111ll_opy_ = {
  bstack1l1_opy_ (u"ࠢࡤ࡮࡬ࡧࡰࡋ࡬ࡦ࡯ࡨࡲࡹࠨᚁ"): bstack1l1_opy_ (u"ࠣࡥ࡯࡭ࡨࡱࠢᚂ"),
  bstack1l1_opy_ (u"ࠤࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠨᚃ"): bstack1l1_opy_ (u"ࠥࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠢᚄ"),
  bstack1l1_opy_ (u"ࠦࡸ࡫࡮ࡥࡍࡨࡽࡸ࡚࡯ࡆ࡮ࡨࡱࡪࡴࡴࠣᚅ"): bstack1l1_opy_ (u"ࠧࡹࡥ࡯ࡦࡎࡩࡾࡹࠢᚆ"),
  bstack1l1_opy_ (u"ࠨࡳࡦࡰࡧࡏࡪࡿࡳࡕࡱࡄࡧࡹ࡯ࡶࡦࡇ࡯ࡩࡲ࡫࡮ࡵࠤᚇ"): bstack1l1_opy_ (u"ࠢࡴࡧࡱࡨࡐ࡫ࡹࡴࠤᚈ"),
  bstack1l1_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥᚉ"): bstack1l1_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦᚊ")
}
bstack1l1l11ll_opy_ = {
  bstack1l1_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡅࡑࡒࠧᚋ"): bstack1l1_opy_ (u"ࠫࡘࡻࡩࡵࡧࠣࡗࡪࡺࡵࡱࠩᚌ"),
  bstack1l1_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨᚍ"): bstack1l1_opy_ (u"࠭ࡓࡶ࡫ࡷࡩ࡚ࠥࡥࡢࡴࡧࡳࡼࡴࠧᚎ"),
  bstack1l1_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬᚏ"): bstack1l1_opy_ (u"ࠨࡖࡨࡷࡹࠦࡓࡦࡶࡸࡴࠬᚐ"),
  bstack1l1_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭ᚑ"): bstack1l1_opy_ (u"ࠪࡘࡪࡹࡴࠡࡖࡨࡥࡷࡪ࡯ࡸࡰࠪᚒ")
}
bstack1l1l1l1ll1l_opy_ = 65536
bstack1l1l1l11l1l_opy_ = bstack1l1_opy_ (u"ࠫ࠳࠴࠮࡜ࡖࡕ࡙ࡓࡉࡁࡕࡇࡇࡡࠬᚓ")
bstack1l1l1ll1111_opy_ = [
      bstack1l1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᚔ"), bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩᚕ"), bstack1l1_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᚖ"), bstack1l1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬᚗ"), bstack1l1_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠫᚘ"),
      bstack1l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭ᚙ"), bstack1l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧᚚ"), bstack1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡔࡷࡵࡸࡺࡗࡶࡩࡷ࠭᚛"), bstack1l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡓࡥࡸࡹࠧ᚜"),
      bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡵࡴࡧࡵࡒࡦࡳࡥࠨ᚝"), bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ᚞"), bstack1l1_opy_ (u"ࠩࡤࡹࡹ࡮ࡔࡰ࡭ࡨࡲࠬ᚟")
    ]
bstack1l1l1l1lll1_opy_= {
  bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᚠ"): bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨᚡ"),
  bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩᚢ"): bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪᚣ"),
  bstack1l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ᚤ"): bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬᚥ"),
  bstack1l1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩᚦ"): bstack1l1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᚧ"),
  bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᚨ"): bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᚩ"),
  bstack1l1_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨᚪ"): bstack1l1_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩᚫ"),
  bstack1l1_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᚬ"): bstack1l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᚭ"),
  bstack1l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧᚮ"): bstack1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨᚯ"),
  bstack1l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨᚰ"): bstack1l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩᚱ"),
  bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬᚲ"): bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸ࠭ᚳ"),
  bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᚴ"): bstack1l1_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᚵ"),
  bstack1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᚶ"): bstack1l1_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᚷ"),
  bstack1l1_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠨᚸ"): bstack1l1_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠩᚹ"),
  bstack1l1_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᚺ"): bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᚻ"),
  bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᚼ"): bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᚽ"),
  bstack1l1_opy_ (u"ࠬࡸࡥࡳࡷࡱࡘࡪࡹࡴࡴࠩᚾ"): bstack1l1_opy_ (u"࠭ࡲࡦࡴࡸࡲ࡙࡫ࡳࡵࡵࠪᚿ"),
  bstack1l1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ᛀ"): bstack1l1_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧᛁ"),
  bstack1l1_opy_ (u"ࠩࡳࡩࡷࡩࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᛂ"): bstack1l1_opy_ (u"ࠪࡴࡪࡸࡣࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᛃ"),
  bstack1l1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡆࡥࡵࡺࡵࡳࡧࡐࡳࡩ࡫ࠧᛄ"): bstack1l1_opy_ (u"ࠬࡶࡥࡳࡥࡼࡇࡦࡶࡴࡶࡴࡨࡑࡴࡪࡥࠨᛅ"),
  bstack1l1_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨᛆ"): bstack1l1_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩᛇ"),
  bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᛈ"): bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᛉ"),
  bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᛊ"): bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᛋ"),
  bstack1l1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩᛌ"): bstack1l1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪᛍ"),
  bstack1l1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶࠫᛎ"): bstack1l1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࡔࡶࡴࡪࡱࡱࡷࠬᛏ"),
  bstack1l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡔࡧࡷࡸ࡮ࡴࡧࡴࠩᛐ"): bstack1l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡕࡨࡸࡹ࡯࡮ࡨࡵࠪᛑ")
}
bstack1l1l1l11ll1_opy_ = [bstack1l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᛒ"), bstack1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫᛓ")]
bstack1llll1ll11_opy_ = (bstack1l1_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨᛔ"),)
bstack1l1l1ll1l11_opy_ = bstack1l1_opy_ (u"ࠧࡴࡦ࡮࠳ࡻ࠷࠯ࡶࡲࡧࡥࡹ࡫࡟ࡤ࡮࡬ࠫᛕ")
bstack11l1l1111_opy_ = bstack1l1_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡴ࡮࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡤࡹࡹࡵ࡭ࡢࡶࡨ࠱ࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥ࠰ࡸ࠴࠳࡬ࡸࡩࡥࡵ࠲ࠦᛖ")
bstack1l1111l111_opy_ = bstack1l1_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲࡫ࡷ࡯ࡤ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡩࡧࡳࡩࡤࡲࡥࡷࡪ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࠣᛗ")
bstack111111l1l_opy_ = bstack1l1_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡶࡩ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠳ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧ࠲ࡺ࠶࠵ࡢࡶ࡫࡯ࡨࡸ࠴ࡪࡴࡱࡱࠦᛘ")
bstack1llll11l1l_opy_ = {
  bstack1l1_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗࠫᛙ"): bstack1l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᛚ"),
  bstack1l1_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙࠳ࡂࡅࡆࠪᛛ"): bstack1l1_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺ࠭ࡤࡷࡦࡹࡲࡨࡥࡳࠩᛜ")
}