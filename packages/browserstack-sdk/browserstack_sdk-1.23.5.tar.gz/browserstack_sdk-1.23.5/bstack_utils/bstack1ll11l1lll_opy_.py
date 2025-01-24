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
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack1lll1l11ll1_opy_, bstack1ll1l1l1_opy_, bstack1l11lll1ll_opy_, bstack1llll111_opy_, \
    bstack1lll1l1llll_opy_
from bstack_utils.measure import measure
def bstack11ll1l1111_opy_(bstack1ll11l111l1_opy_):
    for driver in bstack1ll11l111l1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack111lll1ll_opy_, stage=STAGE.SINGLE)
def bstack1ll11l1111_opy_(driver, status, reason=bstack11111_opy_ (u"ࠧࠨᛣ")):
    bstack1llllll1l1_opy_ = Config.bstack11lll111l_opy_()
    if bstack1llllll1l1_opy_.bstack111ll1l1ll_opy_():
        return
    bstack111111111_opy_ = bstack1ll1l1llll_opy_(bstack11111_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫᛤ"), bstack11111_opy_ (u"ࠩࠪᛥ"), status, reason, bstack11111_opy_ (u"ࠪࠫᛦ"), bstack11111_opy_ (u"ࠫࠬᛧ"))
    driver.execute_script(bstack111111111_opy_)
@measure(event_name=EVENTS.bstack111lll1ll_opy_, stage=STAGE.SINGLE)
def bstack11llll11ll_opy_(page, status, reason=bstack11111_opy_ (u"ࠬ࠭ᛨ")):
    try:
        if page is None:
            return
        bstack1llllll1l1_opy_ = Config.bstack11lll111l_opy_()
        if bstack1llllll1l1_opy_.bstack111ll1l1ll_opy_():
            return
        bstack111111111_opy_ = bstack1ll1l1llll_opy_(bstack11111_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩᛩ"), bstack11111_opy_ (u"ࠧࠨᛪ"), status, reason, bstack11111_opy_ (u"ࠨࠩ᛫"), bstack11111_opy_ (u"ࠩࠪ᛬"))
        page.evaluate(bstack11111_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦ᛭"), bstack111111111_opy_)
    except Exception as e:
        print(bstack11111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡬࡯ࡳࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡻࡾࠤᛮ"), e)
def bstack1ll1l1llll_opy_(type, name, status, reason, bstack1l1ll1ll_opy_, bstack111ll1111_opy_):
    bstack1lll11l1_opy_ = {
        bstack11111_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬᛯ"): type,
        bstack11111_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᛰ"): {}
    }
    if type == bstack11111_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩᛱ"):
        bstack1lll11l1_opy_[bstack11111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᛲ")][bstack11111_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᛳ")] = bstack1l1ll1ll_opy_
        bstack1lll11l1_opy_[bstack11111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᛴ")][bstack11111_opy_ (u"ࠫࡩࡧࡴࡢࠩᛵ")] = json.dumps(str(bstack111ll1111_opy_))
    if type == bstack11111_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ᛶ"):
        bstack1lll11l1_opy_[bstack11111_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᛷ")][bstack11111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᛸ")] = name
    if type == bstack11111_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ᛹"):
        bstack1lll11l1_opy_[bstack11111_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ᛺")][bstack11111_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ᛻")] = status
        if status == bstack11111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ᛼") and str(reason) != bstack11111_opy_ (u"ࠧࠨ᛽"):
            bstack1lll11l1_opy_[bstack11111_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ᛾")][bstack11111_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧ᛿")] = json.dumps(str(reason))
    bstack111ll111_opy_ = bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭ᜀ").format(json.dumps(bstack1lll11l1_opy_))
    return bstack111ll111_opy_
def bstack1l1l1lllll_opy_(url, config, logger, bstack111lll1l_opy_=False):
    hostname = bstack1ll1l1l1_opy_(url)
    is_private = bstack1llll111_opy_(hostname)
    try:
        if is_private or bstack111lll1l_opy_:
            file_path = bstack1lll1l11ll1_opy_(bstack11111_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᜁ"), bstack11111_opy_ (u"ࠪ࠲ࡧࡹࡴࡢࡥ࡮࠱ࡨࡵ࡮ࡧ࡫ࡪ࠲࡯ࡹ࡯࡯ࠩᜂ"), logger)
            if os.environ.get(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡑࡓ࡙ࡥࡓࡆࡖࡢࡉࡗࡘࡏࡓࠩᜃ")) and eval(
                    os.environ.get(bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪᜄ"))):
                return
            if (bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪᜅ") in config and not config[bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫᜆ")]):
                os.environ[bstack11111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭ᜇ")] = str(True)
                bstack1ll11l1111l_opy_ = {bstack11111_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫᜈ"): hostname}
                bstack1lll1l1llll_opy_(bstack11111_opy_ (u"ࠪ࠲ࡧࡹࡴࡢࡥ࡮࠱ࡨࡵ࡮ࡧ࡫ࡪ࠲࡯ࡹ࡯࡯ࠩᜉ"), bstack11111_opy_ (u"ࠫࡳࡻࡤࡨࡧࡢࡰࡴࡩࡡ࡭ࠩᜊ"), bstack1ll11l1111l_opy_, logger)
    except Exception as e:
        pass
def bstack1lll1ll11l_opy_(caps, bstack1ll11l11l11_opy_):
    if bstack11111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᜋ") in caps:
        caps[bstack11111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᜌ")][bstack11111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࠭ᜍ")] = True
        if bstack1ll11l11l11_opy_:
            caps[bstack11111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᜎ")][bstack11111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᜏ")] = bstack1ll11l11l11_opy_
    else:
        caps[bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࠨᜐ")] = True
        if bstack1ll11l11l11_opy_:
            caps[bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᜑ")] = bstack1ll11l11l11_opy_
def bstack1ll1l111111_opy_(bstack111lll1l1l_opy_):
    bstack1ll11l111ll_opy_ = bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡖࡸࡦࡺࡵࡴࠩᜒ"), bstack11111_opy_ (u"࠭ࠧᜓ"))
    if bstack1ll11l111ll_opy_ == bstack11111_opy_ (u"ࠧࠨ᜔") or bstack1ll11l111ll_opy_ == bstack11111_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥ᜕ࠩ"):
        threading.current_thread().testStatus = bstack111lll1l1l_opy_
    else:
        if bstack111lll1l1l_opy_ == bstack11111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ᜖"):
            threading.current_thread().testStatus = bstack111lll1l1l_opy_