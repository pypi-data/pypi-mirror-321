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
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack11111111_opy_ = {}
        bstack1llllllll_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩয"), bstack1l1_opy_ (u"ࠩࠪর"))
        if not bstack1llllllll_opy_:
            return bstack11111111_opy_
        try:
            bstack111111l1_opy_ = json.loads(bstack1llllllll_opy_)
            if bstack1l1_opy_ (u"ࠥࡳࡸࠨ঱") in bstack111111l1_opy_:
                bstack11111111_opy_[bstack1l1_opy_ (u"ࠦࡴࡹࠢল")] = bstack111111l1_opy_[bstack1l1_opy_ (u"ࠧࡵࡳࠣ঳")]
            if bstack1l1_opy_ (u"ࠨ࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠥ঴") in bstack111111l1_opy_ or bstack1l1_opy_ (u"ࠢࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠥ঵") in bstack111111l1_opy_:
                bstack11111111_opy_[bstack1l1_opy_ (u"ࠣࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠦশ")] = bstack111111l1_opy_.get(bstack1l1_opy_ (u"ࠤࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳࠨষ"), bstack111111l1_opy_.get(bstack1l1_opy_ (u"ࠥࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳࠨস")))
            if bstack1l1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࠧহ") in bstack111111l1_opy_ or bstack1l1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠥ঺") in bstack111111l1_opy_:
                bstack11111111_opy_[bstack1l1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦ঻")] = bstack111111l1_opy_.get(bstack1l1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲ়ࠣ"), bstack111111l1_opy_.get(bstack1l1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࠨঽ")))
            if bstack1l1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠦা") in bstack111111l1_opy_ or bstack1l1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠦি") in bstack111111l1_opy_:
                bstack11111111_opy_[bstack1l1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧী")] = bstack111111l1_opy_.get(bstack1l1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠢু"), bstack111111l1_opy_.get(bstack1l1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠢূ")))
            if bstack1l1_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࠢৃ") in bstack111111l1_opy_ or bstack1l1_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠧৄ") in bstack111111l1_opy_:
                bstack11111111_opy_[bstack1l1_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪࠨ৅")] = bstack111111l1_opy_.get(bstack1l1_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࠥ৆"), bstack111111l1_opy_.get(bstack1l1_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠣে")))
            if bstack1l1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࠢৈ") in bstack111111l1_opy_ or bstack1l1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧ৉") in bstack111111l1_opy_:
                bstack11111111_opy_[bstack1l1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨ৊")] = bstack111111l1_opy_.get(bstack1l1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠥো"), bstack111111l1_opy_.get(bstack1l1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣৌ")))
            if bstack1l1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡤࡼࡥࡳࡵ࡬ࡳࡳࠨ্") in bstack111111l1_opy_ or bstack1l1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨৎ") in bstack111111l1_opy_:
                bstack11111111_opy_[bstack1l1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢ৏")] = bstack111111l1_opy_.get(bstack1l1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠤ৐"), bstack111111l1_opy_.get(bstack1l1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤ৑")))
            if bstack1l1_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠥ৒") in bstack111111l1_opy_:
                bstack11111111_opy_[bstack1l1_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠦ৓")] = bstack111111l1_opy_[bstack1l1_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷࠧ৔")]
        except Exception as error:
            logger.error(bstack1l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡤࡷࡵࡶࡪࡴࡴࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡨࡦࡺࡡ࠻ࠢࠥ৕") +  str(error))
        return bstack11111111_opy_