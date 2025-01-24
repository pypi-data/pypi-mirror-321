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
import re
from bstack_utils.bstack1ll11l1lll_opy_ import bstack1ll1l111111_opy_
def bstack1ll11ll1ll1_opy_(fixture_name):
    if fixture_name.startswith(bstack11111_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᚮ")):
        return bstack11111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᚯ")
    elif fixture_name.startswith(bstack11111_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᚰ")):
        return bstack11111_opy_ (u"࠭ࡳࡦࡶࡸࡴ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᚱ")
    elif fixture_name.startswith(bstack11111_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᚲ")):
        return bstack11111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᚳ")
    elif fixture_name.startswith(bstack11111_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᚴ")):
        return bstack11111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᚵ")
def bstack1ll11llll11_opy_(fixture_name):
    return bool(re.match(bstack11111_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠࠪࡩࡹࡳࡩࡴࡪࡱࡱࢀࡲࡵࡤࡶ࡮ࡨ࠭ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥ࠮ࠫࠩᚶ"), fixture_name))
def bstack1ll11llllll_opy_(fixture_name):
    return bool(re.match(bstack11111_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᚷ"), fixture_name))
def bstack1ll11lll1l1_opy_(fixture_name):
    return bool(re.match(bstack11111_opy_ (u"࠭࡞ࡠࡺࡸࡲ࡮ࡺ࡟ࠩࡵࡨࡸࡺࡶࡼࡵࡧࡤࡶࡩࡵࡷ࡯ࠫࡢࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᚸ"), fixture_name))
def bstack1ll1l1111l1_opy_(fixture_name):
    if fixture_name.startswith(bstack11111_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᚹ")):
        return bstack11111_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᚺ"), bstack11111_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᚻ")
    elif fixture_name.startswith(bstack11111_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᚼ")):
        return bstack11111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡱࡴࡪࡵ࡭ࡧࠪᚽ"), bstack11111_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩᚾ")
    elif fixture_name.startswith(bstack11111_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᚿ")):
        return bstack11111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᛀ"), bstack11111_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᛁ")
    elif fixture_name.startswith(bstack11111_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᛂ")):
        return bstack11111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᛃ"), bstack11111_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧᛄ")
    return None, None
def bstack1ll1l11111l_opy_(hook_name):
    if hook_name in [bstack11111_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫᛅ"), bstack11111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨᛆ")]:
        return hook_name.capitalize()
    return hook_name
def bstack1ll11llll1l_opy_(hook_name):
    if hook_name in [bstack11111_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᛇ"), bstack11111_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧᛈ")]:
        return bstack11111_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᛉ")
    elif hook_name in [bstack11111_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩᛊ"), bstack11111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩᛋ")]:
        return bstack11111_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩᛌ")
    elif hook_name in [bstack11111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪᛍ"), bstack11111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩᛎ")]:
        return bstack11111_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᛏ")
    elif hook_name in [bstack11111_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫᛐ"), bstack11111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫᛑ")]:
        return bstack11111_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧᛒ")
    return hook_name
def bstack1ll11lllll1_opy_(node, scenario):
    if hasattr(node, bstack11111_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧᛓ")):
        parts = node.nodeid.rsplit(bstack11111_opy_ (u"ࠨ࡛ࠣᛔ"))
        params = parts[-1]
        return bstack11111_opy_ (u"ࠢࡼࡿࠣ࡟ࢀࢃࠢᛕ").format(scenario.name, params)
    return scenario.name
def bstack1ll11ll1lll_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack11111_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪᛖ")):
            examples = list(node.callspec.params[bstack11111_opy_ (u"ࠩࡢࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡦࡺࡤࡱࡵࡲࡥࠨᛗ")].values())
        return examples
    except:
        return []
def bstack1ll11lll111_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack1ll11lll1ll_opy_(report):
    try:
        status = bstack11111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᛘ")
        if report.passed or (report.failed and hasattr(report, bstack11111_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨᛙ"))):
            status = bstack11111_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᛚ")
        elif report.skipped:
            status = bstack11111_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᛛ")
        bstack1ll1l111111_opy_(status)
    except:
        pass
def bstack1llll1ll11_opy_(status):
    try:
        bstack1ll11ll1l1l_opy_ = bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᛜ")
        if status == bstack11111_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᛝ"):
            bstack1ll11ll1l1l_opy_ = bstack11111_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᛞ")
        elif status == bstack11111_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᛟ"):
            bstack1ll11ll1l1l_opy_ = bstack11111_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬᛠ")
        bstack1ll1l111111_opy_(bstack1ll11ll1l1l_opy_)
    except:
        pass
def bstack1ll11lll11l_opy_(item=None, report=None, summary=None, extra=None):
    return