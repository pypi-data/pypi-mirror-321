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
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.helper import bstack1l1ll11llll_opy_, bstack11l1l11111_opy_, bstack1l1111ll_opy_, bstack1ll1l1lll1_opy_, \
    bstack1l1ll1l11l1_opy_
def bstack1l1ll1111l_opy_(bstack1l1ll1l1l11_opy_):
    for driver in bstack1l1ll1l1l11_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1l1lll1lll_opy_(driver, status, reason=bstack1l1_opy_ (u"ࠨࠩ፲")):
    bstack111l11ll_opy_ = Config.bstack11l111ll_opy_()
    if bstack111l11ll_opy_.bstack11111lll_opy_():
        return
    bstack1l11ll11ll_opy_ = bstack1l1ll1ll11_opy_(bstack1l1_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬ፳"), bstack1l1_opy_ (u"ࠪࠫ፴"), status, reason, bstack1l1_opy_ (u"ࠫࠬ፵"), bstack1l1_opy_ (u"ࠬ࠭፶"))
    driver.execute_script(bstack1l11ll11ll_opy_)
def bstack11ll1l11l_opy_(page, status, reason=bstack1l1_opy_ (u"࠭ࠧ፷")):
    try:
        if page is None:
            return
        bstack111l11ll_opy_ = Config.bstack11l111ll_opy_()
        if bstack111l11ll_opy_.bstack11111lll_opy_():
            return
        bstack1l11ll11ll_opy_ = bstack1l1ll1ll11_opy_(bstack1l1_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪ፸"), bstack1l1_opy_ (u"ࠨࠩ፹"), status, reason, bstack1l1_opy_ (u"ࠩࠪ፺"), bstack1l1_opy_ (u"ࠪࠫ፻"))
        page.evaluate(bstack1l1_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧ፼"), bstack1l11ll11ll_opy_)
    except Exception as e:
        print(bstack1l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࠦࡦࡰࡴࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡼࡿࠥ፽"), e)
def bstack1l1ll1ll11_opy_(type, name, status, reason, bstack1l11lll1ll_opy_, bstack1llll111l1_opy_):
    bstack11l1ll11l1_opy_ = {
        bstack1l1_opy_ (u"࠭ࡡࡤࡶ࡬ࡳࡳ࠭፾"): type,
        bstack1l1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ፿"): {}
    }
    if type == bstack1l1_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪᎀ"):
        bstack11l1ll11l1_opy_[bstack1l1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᎁ")][bstack1l1_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩᎂ")] = bstack1l11lll1ll_opy_
        bstack11l1ll11l1_opy_[bstack1l1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᎃ")][bstack1l1_opy_ (u"ࠬࡪࡡࡵࡣࠪᎄ")] = json.dumps(str(bstack1llll111l1_opy_))
    if type == bstack1l1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᎅ"):
        bstack11l1ll11l1_opy_[bstack1l1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᎆ")][bstack1l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᎇ")] = name
    if type == bstack1l1_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬᎈ"):
        bstack11l1ll11l1_opy_[bstack1l1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᎉ")][bstack1l1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᎊ")] = status
        if status == bstack1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᎋ") and str(reason) != bstack1l1_opy_ (u"ࠨࠢᎌ"):
            bstack11l1ll11l1_opy_[bstack1l1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᎍ")][bstack1l1_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨᎎ")] = json.dumps(str(reason))
    bstack11ll1ll1ll_opy_ = bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧᎏ").format(json.dumps(bstack11l1ll11l1_opy_))
    return bstack11ll1ll1ll_opy_
def bstack1l1l1l1l1l_opy_(url, config, logger, bstack11l11l1l1l_opy_=False):
    hostname = bstack11l1l11111_opy_(url)
    is_private = bstack1ll1l1lll1_opy_(hostname)
    try:
        if is_private or bstack11l11l1l1l_opy_:
            file_path = bstack1l1ll11llll_opy_(bstack1l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ᎐"), bstack1l1_opy_ (u"ࠫ࠳ࡨࡳࡵࡣࡦ࡯࠲ࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪ᎑"), logger)
            if os.environ.get(bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪ᎒")) and eval(
                    os.environ.get(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡓࡕࡔࡠࡕࡈࡘࡤࡋࡒࡓࡑࡕࠫ᎓"))):
                return
            if (bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ᎔") in config and not config[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ᎕")]):
                os.environ[bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧ᎖")] = str(True)
                bstack1l1ll1l11ll_opy_ = {bstack1l1_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬ᎗"): hostname}
                bstack1l1ll1l11l1_opy_(bstack1l1_opy_ (u"ࠫ࠳ࡨࡳࡵࡣࡦ࡯࠲ࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪ᎘"), bstack1l1_opy_ (u"ࠬࡴࡵࡥࡩࡨࡣࡱࡵࡣࡢ࡮ࠪ᎙"), bstack1l1ll1l11ll_opy_, logger)
    except Exception as e:
        pass
def bstack1l1l1l1lll_opy_(caps, bstack1l1ll1l1111_opy_):
    if bstack1l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ᎚") in caps:
        caps[bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ᎛")][bstack1l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࠧ᎜")] = True
        if bstack1l1ll1l1111_opy_:
            caps[bstack1l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ᎝")][bstack1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ᎞")] = bstack1l1ll1l1111_opy_
    else:
        caps[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࠩ᎟")] = True
        if bstack1l1ll1l1111_opy_:
            caps[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭Ꭰ")] = bstack1l1ll1l1111_opy_
def bstack1l1ll11lll1_opy_(bstack1l1l1lll_opy_):
    bstack1l1ll1l111l_opy_ = bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࡗࡹࡧࡴࡶࡵࠪᎡ"), bstack1l1_opy_ (u"ࠧࠨᎢ"))
    if bstack1l1ll1l111l_opy_ == bstack1l1_opy_ (u"ࠨࠩᎣ") or bstack1l1ll1l111l_opy_ == bstack1l1_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪᎤ"):
        threading.current_thread().testStatus = bstack1l1l1lll_opy_
    else:
        if bstack1l1l1lll_opy_ == bstack1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᎥ"):
            threading.current_thread().testStatus = bstack1l1l1lll_opy_