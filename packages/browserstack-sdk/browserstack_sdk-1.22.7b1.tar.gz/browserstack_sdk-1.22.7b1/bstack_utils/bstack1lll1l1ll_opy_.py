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
import re
from bstack_utils.bstack1llll11l11_opy_ import bstack1l1ll11lll1_opy_
def bstack1l1l111lll1_opy_(fixture_name):
    if fixture_name.startswith(bstack1l1_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᜂ")):
        return bstack1l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᜃ")
    elif fixture_name.startswith(bstack1l1_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᜄ")):
        return bstack1l1_opy_ (u"࠭ࡳࡦࡶࡸࡴ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᜅ")
    elif fixture_name.startswith(bstack1l1_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᜆ")):
        return bstack1l1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᜇ")
    elif fixture_name.startswith(bstack1l1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᜈ")):
        return bstack1l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᜉ")
def bstack1l1l11l1l11_opy_(fixture_name):
    return bool(re.match(bstack1l1_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠࠪࡩࡹࡳࡩࡴࡪࡱࡱࢀࡲࡵࡤࡶ࡮ࡨ࠭ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥ࠮ࠫࠩᜊ"), fixture_name))
def bstack1l1l11l11l1_opy_(fixture_name):
    return bool(re.match(bstack1l1_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᜋ"), fixture_name))
def bstack1l1l111llll_opy_(fixture_name):
    return bool(re.match(bstack1l1_opy_ (u"࠭࡞ࡠࡺࡸࡲ࡮ࡺ࡟ࠩࡵࡨࡸࡺࡶࡼࡵࡧࡤࡶࡩࡵࡷ࡯ࠫࡢࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᜌ"), fixture_name))
def bstack1l1l11l1111_opy_(fixture_name):
    if fixture_name.startswith(bstack1l1_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᜍ")):
        return bstack1l1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᜎ"), bstack1l1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᜏ")
    elif fixture_name.startswith(bstack1l1_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᜐ")):
        return bstack1l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡱࡴࡪࡵ࡭ࡧࠪᜑ"), bstack1l1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩᜒ")
    elif fixture_name.startswith(bstack1l1_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᜓ")):
        return bstack1l1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡩࡹࡳࡩࡴࡪࡱࡱ᜔ࠫ"), bstack1l1_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌ᜕ࠬ")
    elif fixture_name.startswith(bstack1l1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬ᜖")):
        return bstack1l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬ᜗"), bstack1l1_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧ᜘")
    return None, None
def bstack1l1l111ll11_opy_(hook_name):
    if hook_name in [bstack1l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ᜙"), bstack1l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ᜚")]:
        return hook_name.capitalize()
    return hook_name
def bstack1l1l11l11ll_opy_(hook_name):
    if hook_name in [bstack1l1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨ᜛"), bstack1l1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧ᜜")]:
        return bstack1l1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧ᜝")
    elif hook_name in [bstack1l1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩ᜞"), bstack1l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩᜟ")]:
        return bstack1l1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩᜠ")
    elif hook_name in [bstack1l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪᜡ"), bstack1l1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩᜢ")]:
        return bstack1l1_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᜣ")
    elif hook_name in [bstack1l1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫᜤ"), bstack1l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫᜥ")]:
        return bstack1l1_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧᜦ")
    return hook_name
def bstack1l1l111l1l1_opy_(node, scenario):
    if hasattr(node, bstack1l1_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧᜧ")):
        parts = node.nodeid.rsplit(bstack1l1_opy_ (u"ࠨ࡛ࠣᜨ"))
        params = parts[-1]
        return bstack1l1_opy_ (u"ࠢࡼࡿࠣ࡟ࢀࢃࠢᜩ").format(scenario.name, params)
    return scenario.name
def bstack1l1l111l11l_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack1l1_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪᜪ")):
            examples = list(node.callspec.params[bstack1l1_opy_ (u"ࠩࡢࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡦࡺࡤࡱࡵࡲࡥࠨᜫ")].values())
        return examples
    except:
        return []
def bstack1l1l111l1ll_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack1l1l11l1l1l_opy_(report):
    try:
        status = bstack1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᜬ")
        if report.passed or (report.failed and hasattr(report, bstack1l1_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨᜭ"))):
            status = bstack1l1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᜮ")
        elif report.skipped:
            status = bstack1l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᜯ")
        bstack1l1ll11lll1_opy_(status)
    except:
        pass
def bstack111l11l1l_opy_(status):
    try:
        bstack1l1l11l111l_opy_ = bstack1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᜰ")
        if status == bstack1l1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᜱ"):
            bstack1l1l11l111l_opy_ = bstack1l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᜲ")
        elif status == bstack1l1_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᜳ"):
            bstack1l1l11l111l_opy_ = bstack1l1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨ᜴ࠬ")
        bstack1l1ll11lll1_opy_(bstack1l1l11l111l_opy_)
    except:
        pass
def bstack1l1l111ll1l_opy_(item=None, report=None, summary=None, extra=None):
    return