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
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack11111lll1_opy_ = {}
        bstack11l1lllll1_opy_ = os.environ.get(bstack11111_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃฺࠪ"), bstack11111_opy_ (u"ࠪࠫ฻"))
        if not bstack11l1lllll1_opy_:
            return bstack11111lll1_opy_
        try:
            bstack11l1llllll_opy_ = json.loads(bstack11l1lllll1_opy_)
            if bstack11111_opy_ (u"ࠦࡴࡹࠢ฼") in bstack11l1llllll_opy_:
                bstack11111lll1_opy_[bstack11111_opy_ (u"ࠧࡵࡳࠣ฽")] = bstack11l1llllll_opy_[bstack11111_opy_ (u"ࠨ࡯ࡴࠤ฾")]
            if bstack11111_opy_ (u"ࠢࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠦ฿") in bstack11l1llllll_opy_ or bstack11111_opy_ (u"ࠣࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠦเ") in bstack11l1llllll_opy_:
                bstack11111lll1_opy_[bstack11111_opy_ (u"ࠤࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠧแ")] = bstack11l1llllll_opy_.get(bstack11111_opy_ (u"ࠥࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠢโ"), bstack11l1llllll_opy_.get(bstack11111_opy_ (u"ࠦࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠢใ")))
            if bstack11111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࠨไ") in bstack11l1llllll_opy_ or bstack11111_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦๅ") in bstack11l1llllll_opy_:
                bstack11111lll1_opy_[bstack11111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠧๆ")] = bstack11l1llllll_opy_.get(bstack11111_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࠤ็"), bstack11l1llllll_opy_.get(bstack11111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫่ࠢ")))
            if bstack11111_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲ้ࠧ") in bstack11l1llllll_opy_ or bstack11111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲ๊ࠧ") in bstack11l1llllll_opy_:
                bstack11111lll1_opy_[bstack11111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨ๋")] = bstack11l1llllll_opy_.get(bstack11111_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣ์"), bstack11l1llllll_opy_.get(bstack11111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠣํ")))
            if bstack11111_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࠣ๎") in bstack11l1llllll_opy_ or bstack11111_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪࠨ๏") in bstack11l1llllll_opy_:
                bstack11111lll1_opy_[bstack11111_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠢ๐")] = bstack11l1llllll_opy_.get(bstack11111_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࠦ๑"), bstack11l1llllll_opy_.get(bstack11111_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠤ๒")))
            if bstack11111_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠣ๓") in bstack11l1llllll_opy_ or bstack11111_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨ๔") in bstack11l1llllll_opy_:
                bstack11111lll1_opy_[bstack11111_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢ๕")] = bstack11l1llllll_opy_.get(bstack11111_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦ๖"), bstack11l1llllll_opy_.get(bstack11111_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤ๗")))
            if bstack11111_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ๘") in bstack11l1llllll_opy_ or bstack11111_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢ๙") in bstack11l1llllll_opy_:
                bstack11111lll1_opy_[bstack11111_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣ๚")] = bstack11l1llllll_opy_.get(bstack11111_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠥ๛"), bstack11l1llllll_opy_.get(bstack11111_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥ๜")))
            if bstack11111_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠦ๝") in bstack11l1llllll_opy_:
                bstack11111lll1_opy_[bstack11111_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷࠧ๞")] = bstack11l1llllll_opy_[bstack11111_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸࠨ๟")]
        except Exception as error:
            logger.error(bstack11111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡥࡸࡶࡷ࡫࡮ࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡩࡧࡴࡢ࠼ࠣࠦ๠") +  str(error))
        return bstack11111lll1_opy_