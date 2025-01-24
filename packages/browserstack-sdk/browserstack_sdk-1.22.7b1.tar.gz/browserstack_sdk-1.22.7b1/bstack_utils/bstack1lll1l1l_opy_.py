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
import logging
import os
import threading
from bstack_utils.helper import bstack1ll11l11l_opy_
from bstack_utils.constants import bstack1l1l1l1l1ll_opy_
logger = logging.getLogger(__name__)
class bstack1llll1l1_opy_:
    bstack1l1l11ll1ll_opy_ = None
    @classmethod
    def bstack1ll11l111_opy_(cls):
        if cls.on() and os.getenv(bstack1l1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣᛟ")):
            logger.info(
                bstack1l1_opy_ (u"࡛ࠫ࡯ࡳࡪࡶࠣ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿࠣࡸࡴࠦࡶࡪࡧࡺࠤࡧࡻࡩ࡭ࡦࠣࡶࡪࡶ࡯ࡳࡶ࠯ࠤ࡮ࡴࡳࡪࡩ࡫ࡸࡸ࠲ࠠࡢࡰࡧࠤࡲࡧ࡮ࡺࠢࡰࡳࡷ࡫ࠠࡥࡧࡥࡹ࡬࡭ࡩ࡯ࡩࠣ࡭ࡳ࡬࡯ࡳ࡯ࡤࡸ࡮ࡵ࡮ࠡࡣ࡯ࡰࠥࡧࡴࠡࡱࡱࡩࠥࡶ࡬ࡢࡥࡨࠥࡡࡴࠧᛠ").format(os.getenv(bstack1l1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠥᛡ"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᛢ"), None) is None or os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᛣ")] == bstack1l1_opy_ (u"ࠣࡰࡸࡰࡱࠨᛤ"):
            return False
        return True
    @classmethod
    def bstack1l1l11l1ll1_opy_(cls, bs_config, framework=bstack1l1_opy_ (u"ࠤࠥᛥ")):
        if bstack1l1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪᛦ") in framework:
            return bstack1ll11l11l_opy_(bs_config.get(bstack1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᛧ")))
        bstack1l1l11ll1l1_opy_ = False
        for fw in bstack1l1l1l1l1ll_opy_:
            if fw in framework:
                bstack1l1l11ll1l1_opy_ = True
        return bstack1ll11l11l_opy_(bs_config.get(bstack1l1_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩᛨ"), bstack1l1l11ll1l1_opy_))
    @classmethod
    def bstack1l1l11ll11l_opy_(cls, framework):
        return framework in bstack1l1l1l1l1ll_opy_
    @classmethod
    def bstack1l1l11llll1_opy_(cls, bs_config, framework):
        return cls.bstack1l1l11l1ll1_opy_(bs_config, framework) is True and cls.bstack1l1l11ll11l_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack1l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᛩ"), None)
    @staticmethod
    def bstack11llll1l_opy_():
        if getattr(threading.current_thread(), bstack1l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᛪ"), None):
            return {
                bstack1l1_opy_ (u"ࠨࡶࡼࡴࡪ࠭᛫"): bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺࠧ᛬"),
                bstack1l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ᛭"): getattr(threading.current_thread(), bstack1l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᛮ"), None)
            }
        if getattr(threading.current_thread(), bstack1l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᛯ"), None):
            return {
                bstack1l1_opy_ (u"࠭ࡴࡺࡲࡨࠫᛰ"): bstack1l1_opy_ (u"ࠧࡩࡱࡲ࡯ࠬᛱ"),
                bstack1l1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᛲ"): getattr(threading.current_thread(), bstack1l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᛳ"), None)
            }
        return None
    @staticmethod
    def bstack1l1l11l1lll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1llll1l1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l1llll1_opy_(test, hook_name=None):
        bstack1l1l11lll11_opy_ = test.parent
        if hook_name in [bstack1l1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨᛴ"), bstack1l1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬᛵ"), bstack1l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫᛶ"), bstack1l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨᛷ")]:
            bstack1l1l11lll11_opy_ = test
        scope = []
        while bstack1l1l11lll11_opy_ is not None:
            scope.append(bstack1l1l11lll11_opy_.name)
            bstack1l1l11lll11_opy_ = bstack1l1l11lll11_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack1l1l11lll1l_opy_(hook_type):
        if hook_type == bstack1l1_opy_ (u"ࠢࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠧᛸ"):
            return bstack1l1_opy_ (u"ࠣࡕࡨࡸࡺࡶࠠࡩࡱࡲ࡯ࠧ᛹")
        elif hook_type == bstack1l1_opy_ (u"ࠤࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍࠨ᛺"):
            return bstack1l1_opy_ (u"ࠥࡘࡪࡧࡲࡥࡱࡺࡲࠥ࡮࡯ࡰ࡭ࠥ᛻")
    @staticmethod
    def bstack1l1l11ll111_opy_(bstack11111l1l_opy_):
        try:
            if not bstack1llll1l1_opy_.on():
                return bstack11111l1l_opy_
            if os.environ.get(bstack1l1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࠤ᛼"), None) == bstack1l1_opy_ (u"ࠧࡺࡲࡶࡧࠥ᛽"):
                tests = os.environ.get(bstack1l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࡣ࡙ࡋࡓࡕࡕࠥ᛾"), None)
                if tests is None or tests == bstack1l1_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ᛿"):
                    return bstack11111l1l_opy_
                bstack11111l1l_opy_ = tests.split(bstack1l1_opy_ (u"ࠨ࠮ࠪᜀ"))
                return bstack11111l1l_opy_
        except Exception as exc:
            print(bstack1l1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡴࡨࡶࡺࡴࠠࡩࡣࡱࡨࡱ࡫ࡲ࠻ࠢࠥᜁ"), str(exc))
        return bstack11111l1l_opy_