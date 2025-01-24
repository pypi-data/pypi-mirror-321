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
import threading
from bstack_utils.helper import bstack1llll1lll1_opy_
from bstack_utils.constants import bstack1llll1llll1_opy_, EVENTS, STAGE
from bstack_utils.bstack11l1l11ll_opy_ import get_logger
logger = get_logger(__name__)
class bstack1l1l11l1l1_opy_:
    bstack1ll11ll111l_opy_ = None
    @classmethod
    def bstack1ll1l1ll1_opy_(cls):
        if cls.on():
            logger.info(
                bstack11111_opy_ (u"ࠧࡗ࡫ࡶ࡭ࡹࠦࡨࡵࡶࡳࡷ࠿࠵࠯ࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠦࡴࡰࠢࡹ࡭ࡪࡽࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡲࡲࡶࡹ࠲ࠠࡪࡰࡶ࡭࡬࡮ࡴࡴ࠮ࠣࡥࡳࡪࠠ࡮ࡣࡱࡽࠥࡳ࡯ࡳࡧࠣࡨࡪࡨࡵࡨࡩ࡬ࡲ࡬ࠦࡩ࡯ࡨࡲࡶࡲࡧࡴࡪࡱࡱࠤࡦࡲ࡬ࠡࡣࡷࠤࡴࡴࡥࠡࡲ࡯ࡥࡨ࡫ࠡ࡝ࡰࠪᢎ").format(os.environ[bstack11111_opy_ (u"ࠣࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠢᢏ")]))
    @classmethod
    def on(cls):
        if os.environ.get(bstack11111_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡊࡘࡖࠪᢐ"), None) is None or os.environ[bstack11111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡋ࡙ࡗࠫᢑ")] == bstack11111_opy_ (u"ࠦࡳࡻ࡬࡭ࠤᢒ"):
            return False
        return True
    @classmethod
    def bstack1l1lll1l11l_opy_(cls, bs_config, framework=bstack11111_opy_ (u"ࠧࠨᢓ")):
        bstack1l1lll111ll_opy_ = False
        for fw in bstack1llll1llll1_opy_:
            if fw in framework:
                bstack1l1lll111ll_opy_ = True
        return bstack1llll1lll1_opy_(bs_config.get(bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪᢔ"), bstack1l1lll111ll_opy_))
    @classmethod
    def bstack1l1ll1lll1l_opy_(cls, framework):
        return framework in bstack1llll1llll1_opy_
    @classmethod
    def bstack1l1llll1lll_opy_(cls, bs_config, framework):
        return cls.bstack1l1lll1l11l_opy_(bs_config, framework) is True and cls.bstack1l1ll1lll1l_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᢕ"), None)
    @staticmethod
    def bstack11l1ll1lll_opy_():
        if getattr(threading.current_thread(), bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬᢖ"), None):
            return {
                bstack11111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᢗ"): bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࠨᢘ"),
                bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᢙ"): getattr(threading.current_thread(), bstack11111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᢚ"), None)
            }
        if getattr(threading.current_thread(), bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᢛ"), None):
            return {
                bstack11111_opy_ (u"ࠧࡵࡻࡳࡩࠬᢜ"): bstack11111_opy_ (u"ࠨࡪࡲࡳࡰ࠭ᢝ"),
                bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᢞ"): getattr(threading.current_thread(), bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᢟ"), None)
            }
        return None
    @staticmethod
    def bstack1l1lll1111l_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l1l11l1l1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack111llll111_opy_(test, hook_name=None):
        bstack1l1ll1lllll_opy_ = test.parent
        if hook_name in [bstack11111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩᢠ"), bstack11111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸ࠭ᢡ"), bstack11111_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠬᢢ"), bstack11111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠩᢣ")]:
            bstack1l1ll1lllll_opy_ = test
        scope = []
        while bstack1l1ll1lllll_opy_ is not None:
            scope.append(bstack1l1ll1lllll_opy_.name)
            bstack1l1ll1lllll_opy_ = bstack1l1ll1lllll_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack1l1ll1llll1_opy_(hook_type):
        if hook_type == bstack11111_opy_ (u"ࠣࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍࠨᢤ"):
            return bstack11111_opy_ (u"ࠤࡖࡩࡹࡻࡰࠡࡪࡲࡳࡰࠨᢥ")
        elif hook_type == bstack11111_opy_ (u"ࠥࡅࡋ࡚ࡅࡓࡡࡈࡅࡈࡎࠢᢦ"):
            return bstack11111_opy_ (u"࡙ࠦ࡫ࡡࡳࡦࡲࡻࡳࠦࡨࡰࡱ࡮ࠦᢧ")
    @staticmethod
    def bstack1l1lll11111_opy_(bstack1l1l1llll1_opy_):
        try:
            if not bstack1l1l11l1l1_opy_.on():
                return bstack1l1l1llll1_opy_
            if os.environ.get(bstack11111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࠥᢨ"), None) == bstack11111_opy_ (u"ࠨࡴࡳࡷࡨᢩࠦ"):
                tests = os.environ.get(bstack11111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࡤ࡚ࡅࡔࡖࡖࠦᢪ"), None)
                if tests is None or tests == bstack11111_opy_ (u"ࠣࡰࡸࡰࡱࠨ᢫"):
                    return bstack1l1l1llll1_opy_
                bstack1l1l1llll1_opy_ = tests.split(bstack11111_opy_ (u"ࠩ࠯ࠫ᢬"))
                return bstack1l1l1llll1_opy_
        except Exception as exc:
            logger.debug(bstack1l1lll111l1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡵࡩࡷࡻ࡮ࠡࡪࡤࡲࡩࡲࡥࡳ࠼ࠣࡿࡸࡺࡲࠩࡧࡻࡧ࠮ࢃࠢ᢭"))
        return bstack1l1l1llll1_opy_