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
import logging
import os
import datetime
import threading
from bstack_utils.helper import bstack1l1111ll111_opy_, bstack1l111lll1l1_opy_, bstack11lll11l1l_opy_, bstack1lll111l_opy_, bstack1l1111l11l1_opy_, bstack1l1111l11ll_opy_, bstack1l11l1l1111_opy_, bstack1l111ll1_opy_
from bstack_utils.bstack1l1l11ll1ll_opy_ import bstack1l11lll1l11_opy_
import bstack_utils.bstack1l11l11lll_opy_ as bstack11l1111111_opy_
from bstack_utils.bstack1lll1l1l_opy_ import bstack1llll1l1_opy_
import bstack_utils.accessibility as bstack111l1ll1_opy_
from bstack_utils.bstack11ll111lll_opy_ import bstack11ll111lll_opy_
from bstack_utils.bstack1l1ll1ll_opy_ import bstack1llll111_opy_
bstack11l1llllll1_opy_ = bstack1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡩ࡯࡭࡮ࡨࡧࡹࡵࡲ࠮ࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫᭀ")
logger = logging.getLogger(__name__)
class bstack1l1ll1l1_opy_:
    bstack1l1l11ll1ll_opy_ = None
    bs_config = None
    bstack1ll111l1ll_opy_ = None
    @classmethod
    @bstack1lll111l_opy_(class_method=True)
    def launch(cls, bs_config, bstack1ll111l1ll_opy_):
        cls.bs_config = bs_config
        cls.bstack1ll111l1ll_opy_ = bstack1ll111l1ll_opy_
        try:
            cls.bstack11l1lllllll_opy_()
            bstack11ll1l11111_opy_ = bstack1l1111ll111_opy_(bs_config)
            bstack11ll11l1ll1_opy_ = bstack1l111lll1l1_opy_(bs_config)
            data = bstack11l1111111_opy_.bstack11ll111l1l1_opy_(bs_config, bstack1ll111l1ll_opy_)
            config = {
                bstack1l1_opy_ (u"ࠬࡧࡵࡵࡪࠪᭁ"): (bstack11ll1l11111_opy_, bstack11ll11l1ll1_opy_),
                bstack1l1_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧᭂ"): cls.default_headers()
            }
            response = bstack11lll11l1l_opy_(bstack1l1_opy_ (u"ࠧࡑࡑࡖࡘࠬᭃ"), cls.request_url(bstack1l1_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠲࠰ࡤࡸ࡭ࡱࡪࡳࠨ᭄")), data, config)
            if response.status_code != 200:
                bstack1ll1ll1111l_opy_ = response.json()
                if bstack1ll1ll1111l_opy_[bstack1l1_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪᭅ")] == False:
                    cls.bstack11ll1111lll_opy_(bstack1ll1ll1111l_opy_)
                    return
                cls.bstack11ll11l11l1_opy_(bstack1ll1ll1111l_opy_[bstack1l1_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪᭆ")])
                cls.bstack11ll111l111_opy_(bstack1ll1ll1111l_opy_[bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᭇ")])
                return None
            bstack11ll11l1111_opy_ = cls.bstack11ll111llll_opy_(response)
            return bstack11ll11l1111_opy_
        except Exception as error:
            logger.error(bstack1l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡥࡹ࡮ࡲࡤࠡࡨࡲࡶ࡚ࠥࡥࡴࡶࡋࡹࡧࡀࠠࡼࡿࠥᭈ").format(str(error)))
            return None
    @classmethod
    @bstack1lll111l_opy_(class_method=True)
    def stop(cls, bstack11ll11111ll_opy_=None):
        if not bstack1llll1l1_opy_.on() and not bstack111l1ll1_opy_.on():
            return
        if os.environ.get(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᭉ")) == bstack1l1_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᭊ") or os.environ.get(bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᭋ")) == bstack1l1_opy_ (u"ࠤࡱࡹࡱࡲࠢᭌ"):
            logger.error(bstack1l1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡴࡶࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡡࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷ࡭ࡴࡴࠠࡵࡱ࡮ࡩࡳ࠭᭍"))
            return {
                bstack1l1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ᭎"): bstack1l1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ᭏"),
                bstack1l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ᭐"): bstack1l1_opy_ (u"ࠧࡕࡱ࡮ࡩࡳ࠵ࡢࡶ࡫࡯ࡨࡎࡊࠠࡪࡵࠣࡹࡳࡪࡥࡧ࡫ࡱࡩࡩ࠲ࠠࡣࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡ࡯࡬࡫࡭ࡺࠠࡩࡣࡹࡩࠥ࡬ࡡࡪ࡮ࡨࡨࠬ᭑")
            }
        try:
            cls.bstack1l1l11ll1ll_opy_.shutdown()
            data = {
                bstack1l1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭᭒"): bstack1l111ll1_opy_()
            }
            if not bstack11ll11111ll_opy_ is None:
                data[bstack1l1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡲ࡫ࡴࡢࡦࡤࡸࡦ࠭᭓")] = [{
                    bstack1l1_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪ᭔"): bstack1l1_opy_ (u"ࠫࡺࡹࡥࡳࡡ࡮࡭ࡱࡲࡥࡥࠩ᭕"),
                    bstack1l1_opy_ (u"ࠬࡹࡩࡨࡰࡤࡰࠬ᭖"): bstack11ll11111ll_opy_
                }]
            config = {
                bstack1l1_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ᭗"): cls.default_headers()
            }
            bstack1l111lllll1_opy_ = bstack1l1_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡷࡹࡵࡰࠨ᭘").format(os.environ[bstack1l1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨ᭙")])
            bstack11l1llll1l1_opy_ = cls.request_url(bstack1l111lllll1_opy_)
            response = bstack11lll11l1l_opy_(bstack1l1_opy_ (u"ࠩࡓ࡙࡙࠭᭚"), bstack11l1llll1l1_opy_, data, config)
            if not response.ok:
                raise Exception(bstack1l1_opy_ (u"ࠥࡗࡹࡵࡰࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡱࡳࡹࠦ࡯࡬ࠤ᭛"))
        except Exception as error:
            logger.error(bstack1l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡵࡰࠡࡤࡸ࡭ࡱࡪࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤ࡙࡫ࡳࡵࡊࡸࡦ࠿ࡀࠠࠣ᭜") + str(error))
            return {
                bstack1l1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ᭝"): bstack1l1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ᭞"),
                bstack1l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ᭟"): str(error)
            }
    @classmethod
    @bstack1lll111l_opy_(class_method=True)
    def bstack11ll111llll_opy_(cls, response):
        bstack1ll1ll1111l_opy_ = response.json() if not isinstance(response, dict) else response
        bstack11ll11l1111_opy_ = {}
        if bstack1ll1ll1111l_opy_.get(bstack1l1_opy_ (u"ࠨ࡬ࡺࡸࠬ᭠")) is None:
            os.environ[bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭᭡")] = bstack1l1_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ᭢")
        else:
            os.environ[bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ᭣")] = bstack1ll1ll1111l_opy_.get(bstack1l1_opy_ (u"ࠬࡰࡷࡵࠩ᭤"), bstack1l1_opy_ (u"࠭࡮ࡶ࡮࡯ࠫ᭥"))
        os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ᭦")] = bstack1ll1ll1111l_opy_.get(bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ᭧"), bstack1l1_opy_ (u"ࠩࡱࡹࡱࡲࠧ᭨"))
        if bstack1llll1l1_opy_.bstack1l1l11llll1_opy_(cls.bs_config, cls.bstack1ll111l1ll_opy_.get(bstack1l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡵࡴࡧࡧࠫ᭩"), bstack1l1_opy_ (u"ࠫࠬ᭪"))) is True:
            bstack11l1llll11l_opy_, build_hashed_id, bstack11l1lllll11_opy_ = cls.bstack11ll111lll1_opy_(bstack1ll1ll1111l_opy_)
            if bstack11l1llll11l_opy_ != None and build_hashed_id != None:
                bstack11ll11l1111_opy_[bstack1l1_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ᭫")] = {
                    bstack1l1_opy_ (u"࠭ࡪࡸࡶࡢࡸࡴࡱࡥ࡯᭬ࠩ"): bstack11l1llll11l_opy_,
                    bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ᭭"): build_hashed_id,
                    bstack1l1_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬ᭮"): bstack11l1lllll11_opy_
                }
            else:
                bstack11ll11l1111_opy_[bstack1l1_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ᭯")] = {}
        else:
            bstack11ll11l1111_opy_[bstack1l1_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ᭰")] = {}
        if bstack111l1ll1_opy_.bstack11ll1l1111l_opy_(cls.bs_config) is True:
            bstack11ll111111l_opy_, build_hashed_id = cls.bstack11ll11l111l_opy_(bstack1ll1ll1111l_opy_)
            if bstack11ll111111l_opy_ != None and build_hashed_id != None:
                bstack11ll11l1111_opy_[bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ᭱")] = {
                    bstack1l1_opy_ (u"ࠬࡧࡵࡵࡪࡢࡸࡴࡱࡥ࡯ࠩ᭲"): bstack11ll111111l_opy_,
                    bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ᭳"): build_hashed_id,
                }
            else:
                bstack11ll11l1111_opy_[bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ᭴")] = {}
        else:
            bstack11ll11l1111_opy_[bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ᭵")] = {}
        if bstack11ll11l1111_opy_[bstack1l1_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ᭶")].get(bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ᭷")) != None or bstack11ll11l1111_opy_[bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ᭸")].get(bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ᭹")) != None:
            cls.bstack11ll111ll11_opy_(bstack1ll1ll1111l_opy_.get(bstack1l1_opy_ (u"࠭ࡪࡸࡶࠪ᭺")), bstack1ll1ll1111l_opy_.get(bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ᭻")))
        return bstack11ll11l1111_opy_
    @classmethod
    def bstack11ll111lll1_opy_(cls, bstack1ll1ll1111l_opy_):
        if bstack1ll1ll1111l_opy_.get(bstack1l1_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ᭼")) == None:
            cls.bstack11ll11l11l1_opy_()
            return [None, None, None]
        if bstack1ll1ll1111l_opy_[bstack1l1_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ᭽")][bstack1l1_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ᭾")] != True:
            cls.bstack11ll11l11l1_opy_(bstack1ll1ll1111l_opy_[bstack1l1_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ᭿")])
            return [None, None, None]
        logger.debug(bstack1l1_opy_ (u"࡚ࠬࡥࡴࡶࠣࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠣࡆࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤࡘࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬ࠢࠩᮀ"))
        os.environ[bstack1l1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡆࡓࡒࡖࡌࡆࡖࡈࡈࠬᮁ")] = bstack1l1_opy_ (u"ࠧࡵࡴࡸࡩࠬᮂ")
        if bstack1ll1ll1111l_opy_.get(bstack1l1_opy_ (u"ࠨ࡬ࡺࡸࠬᮃ")):
            os.environ[bstack1l1_opy_ (u"ࠩࡆࡖࡊࡊࡅࡏࡖࡌࡅࡑ࡙࡟ࡇࡑࡕࡣࡈࡘࡁࡔࡊࡢࡖࡊࡖࡏࡓࡖࡌࡒࡌ࠭ᮄ")] = json.dumps({
                bstack1l1_opy_ (u"ࠪࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬᮅ"): bstack1l1111ll111_opy_(cls.bs_config),
                bstack1l1_opy_ (u"ࠫࡵࡧࡳࡴࡹࡲࡶࡩ࠭ᮆ"): bstack1l111lll1l1_opy_(cls.bs_config)
            })
        if bstack1ll1ll1111l_opy_.get(bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧᮇ")):
            os.environ[bstack1l1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬᮈ")] = bstack1ll1ll1111l_opy_[bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩᮉ")]
        if bstack1ll1ll1111l_opy_[bstack1l1_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᮊ")].get(bstack1l1_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪᮋ"), {}).get(bstack1l1_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧᮌ")):
            os.environ[bstack1l1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡃࡏࡐࡔ࡝࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࡗࠬᮍ")] = str(bstack1ll1ll1111l_opy_[bstack1l1_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬᮎ")][bstack1l1_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧᮏ")][bstack1l1_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫᮐ")])
        else:
            os.environ[bstack1l1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡇࡌࡍࡑ࡚ࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࡔࠩᮑ")] = bstack1l1_opy_ (u"ࠤࡱࡹࡱࡲࠢᮒ")
        return [bstack1ll1ll1111l_opy_[bstack1l1_opy_ (u"ࠪ࡮ࡼࡺࠧᮓ")], bstack1ll1ll1111l_opy_[bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ᮔ")], os.environ[bstack1l1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭ᮕ")]]
    @classmethod
    def bstack11ll11l111l_opy_(cls, bstack1ll1ll1111l_opy_):
        if bstack1ll1ll1111l_opy_.get(bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᮖ")) == None:
            cls.bstack11ll111l111_opy_()
            return [None, None]
        if bstack1ll1ll1111l_opy_[bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᮗ")][bstack1l1_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩᮘ")] != True:
            cls.bstack11ll111l111_opy_(bstack1ll1ll1111l_opy_[bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᮙ")])
            return [None, None]
        if bstack1ll1ll1111l_opy_[bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᮚ")].get(bstack1l1_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬᮛ")):
            logger.debug(bstack1l1_opy_ (u"࡚ࠬࡥࡴࡶࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡆࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤࡘࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬ࠢࠩᮜ"))
            parsed = json.loads(os.getenv(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧᮝ"), bstack1l1_opy_ (u"ࠧࡼࡿࠪᮞ")))
            capabilities = bstack11l1111111_opy_.bstack11l1lllll1l_opy_(bstack1ll1ll1111l_opy_[bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᮟ")][bstack1l1_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪᮠ")][bstack1l1_opy_ (u"ࠪࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩᮡ")], bstack1l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᮢ"), bstack1l1_opy_ (u"ࠬࡼࡡ࡭ࡷࡨࠫᮣ"))
            bstack11ll111111l_opy_ = capabilities[bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࡚࡯࡬ࡧࡱࠫᮤ")]
            os.environ[bstack1l1_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬᮥ")] = bstack11ll111111l_opy_
            parsed[bstack1l1_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᮦ")] = capabilities[bstack1l1_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᮧ")]
            os.environ[bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫᮨ")] = json.dumps(parsed)
            scripts = bstack11l1111111_opy_.bstack11l1lllll1l_opy_(bstack1ll1ll1111l_opy_[bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᮩ")][bstack1l1_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ᮪࠭")][bstack1l1_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹ᮫ࠧ")], bstack1l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᮬ"), bstack1l1_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࠩᮭ"))
            bstack11ll111lll_opy_.bstack11ll1l1l111_opy_(scripts)
            commands = bstack1ll1ll1111l_opy_[bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᮮ")][bstack1l1_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫᮯ")][bstack1l1_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࡚࡯ࡘࡴࡤࡴࠬ᮰")].get(bstack1l1_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧ᮱"))
            bstack11ll111lll_opy_.bstack11ll1l1l1l1_opy_(commands)
            bstack11ll111lll_opy_.store()
        return [bstack11ll111111l_opy_, bstack1ll1ll1111l_opy_[bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ᮲")]]
    @classmethod
    def bstack11ll11l11l1_opy_(cls, response=None):
        os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ᮳")] = bstack1l1_opy_ (u"ࠨࡰࡸࡰࡱ࠭᮴")
        os.environ[bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭᮵")] = bstack1l1_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ᮶")
        os.environ[bstack1l1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡄࡑࡐࡔࡑࡋࡔࡆࡆࠪ᮷")] = bstack1l1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ᮸")
        os.environ[bstack1l1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬ᮹")] = bstack1l1_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᮺ")
        os.environ[bstack1l1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡇࡌࡍࡑ࡚ࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࡔࠩᮻ")] = bstack1l1_opy_ (u"ࠤࡱࡹࡱࡲࠢᮼ")
        cls.bstack11ll1111lll_opy_(response, bstack1l1_opy_ (u"ࠥࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠥᮽ"))
        return [None, None, None]
    @classmethod
    def bstack11ll111l111_opy_(cls, response=None):
        os.environ[bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᮾ")] = bstack1l1_opy_ (u"ࠬࡴࡵ࡭࡮ࠪᮿ")
        os.environ[bstack1l1_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫᯀ")] = bstack1l1_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬᯁ")
        os.environ[bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᯂ")] = bstack1l1_opy_ (u"ࠩࡱࡹࡱࡲࠧᯃ")
        cls.bstack11ll1111lll_opy_(response, bstack1l1_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠥᯄ"))
        return [None, None, None]
    @classmethod
    def bstack11ll111ll11_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᯅ")] = jwt
        os.environ[bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᯆ")] = build_hashed_id
    @classmethod
    def bstack11ll1111lll_opy_(cls, response=None, product=bstack1l1_opy_ (u"ࠨࠢᯇ")):
        if response == None:
            logger.error(product + bstack1l1_opy_ (u"ࠢࠡࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡩࡥ࡮ࡲࡥࡥࠤᯈ"))
        for error in response[bstack1l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࡳࠨᯉ")]:
            bstack1l11l11l1l1_opy_ = error[bstack1l1_opy_ (u"ࠩ࡮ࡩࡾ࠭ᯊ")]
            error_message = error[bstack1l1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᯋ")]
            if error_message:
                if bstack1l11l11l1l1_opy_ == bstack1l1_opy_ (u"ࠦࡊࡘࡒࡐࡔࡢࡅࡈࡉࡅࡔࡕࡢࡈࡊࡔࡉࡆࡆࠥᯌ"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack1l1_opy_ (u"ࠧࡊࡡࡵࡣࠣࡹࡵࡲ࡯ࡢࡦࠣࡸࡴࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࠨᯍ") + product + bstack1l1_opy_ (u"ࠨࠠࡧࡣ࡬ࡰࡪࡪࠠࡥࡷࡨࠤࡹࡵࠠࡴࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠦᯎ"))
    @classmethod
    def bstack11l1lllllll_opy_(cls):
        if cls.bstack1l1l11ll1ll_opy_ is not None:
            return
        cls.bstack1l1l11ll1ll_opy_ = bstack1l11lll1l11_opy_(cls.post_data)
        cls.bstack1l1l11ll1ll_opy_.start()
    @classmethod
    def bstack1l1l1ll1_opy_(cls):
        if cls.bstack1l1l11ll1ll_opy_ is None:
            return
        cls.bstack1l1l11ll1ll_opy_.shutdown()
    @classmethod
    @bstack1lll111l_opy_(class_method=True)
    def post_data(cls, bstack1l1l1l1l_opy_, event_url=bstack1l1_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡣࡷࡧ࡭࠭ᯏ")):
        config = {
            bstack1l1_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩᯐ"): cls.default_headers()
        }
        response = bstack11lll11l1l_opy_(bstack1l1_opy_ (u"ࠩࡓࡓࡘ࡚ࠧᯑ"), cls.request_url(event_url), bstack1l1l1l1l_opy_, config)
        bstack11ll1l111ll_opy_ = response.json()
    @classmethod
    def bstack1ll1l111_opy_(cls, bstack1l1l1l1l_opy_, event_url=bstack1l1_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡦࡺࡣࡩࠩᯒ")):
        if not bstack11l1111111_opy_.bstack11ll1111111_opy_(bstack1l1l1l1l_opy_[bstack1l1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨᯓ")]):
            return
        bstack1l11lll11_opy_ = bstack11l1111111_opy_.bstack11ll1111ll1_opy_(bstack1l1l1l1l_opy_[bstack1l1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩᯔ")], bstack1l1l1l1l_opy_.get(bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨᯕ")))
        if bstack1l11lll11_opy_ != None:
            if bstack1l1l1l1l_opy_.get(bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩᯖ")) != None:
                bstack1l1l1l1l_opy_[bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪᯗ")][bstack1l1_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࡢࡱࡦࡶࠧᯘ")] = bstack1l11lll11_opy_
            else:
                bstack1l1l1l1l_opy_[bstack1l1_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࡣࡲࡧࡰࠨᯙ")] = bstack1l11lll11_opy_
        if event_url == bstack1l1_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪᯚ"):
            cls.bstack11l1lllllll_opy_()
            cls.bstack1l1l11ll1ll_opy_.add(bstack1l1l1l1l_opy_)
        elif event_url == bstack1l1_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᯛ"):
            cls.post_data([bstack1l1l1l1l_opy_], event_url)
    @classmethod
    @bstack1lll111l_opy_(class_method=True)
    def bstack1lll1111_opy_(cls, logs):
        bstack11l1llll1ll_opy_ = []
        for log in logs:
            bstack11ll1111l1l_opy_ = {
                bstack1l1_opy_ (u"࠭࡫ࡪࡰࡧࠫᯜ"): bstack1l1_opy_ (u"ࠧࡕࡇࡖࡘࡤࡒࡏࡈࠩᯝ"),
                bstack1l1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᯞ"): log[bstack1l1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᯟ")],
                bstack1l1_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ᯠ"): log[bstack1l1_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧᯡ")],
                bstack1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡢࡶࡪࡹࡰࡰࡰࡶࡩࠬᯢ"): {},
                bstack1l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᯣ"): log[bstack1l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᯤ")],
            }
            if bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᯥ") in log:
                bstack11ll1111l1l_opy_[bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥ᯦ࠩ")] = log[bstack1l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᯧ")]
            elif bstack1l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᯨ") in log:
                bstack11ll1111l1l_opy_[bstack1l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᯩ")] = log[bstack1l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᯪ")]
            bstack11l1llll1ll_opy_.append(bstack11ll1111l1l_opy_)
        cls.bstack1ll1l111_opy_({
            bstack1l1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫᯫ"): bstack1l1_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬᯬ"),
            bstack1l1_opy_ (u"ࠩ࡯ࡳ࡬ࡹࠧᯭ"): bstack11l1llll1ll_opy_
        })
    @classmethod
    @bstack1lll111l_opy_(class_method=True)
    def bstack11ll11111l1_opy_(cls, steps):
        bstack11ll1111l11_opy_ = []
        for step in steps:
            bstack11ll111ll1l_opy_ = {
                bstack1l1_opy_ (u"ࠪ࡯࡮ࡴࡤࠨᯮ"): bstack1l1_opy_ (u"࡙ࠫࡋࡓࡕࡡࡖࡘࡊࡖࠧᯯ"),
                bstack1l1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫᯰ"): step[bstack1l1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᯱ")],
                bstack1l1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲ᯲ࠪ"): step[bstack1l1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳ᯳ࠫ")],
                bstack1l1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ᯴"): step[bstack1l1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ᯵")],
                bstack1l1_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭᯶"): step[bstack1l1_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧ᯷")]
            }
            if bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭᯸") in step:
                bstack11ll111ll1l_opy_[bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ᯹")] = step[bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ᯺")]
            elif bstack1l1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ᯻") in step:
                bstack11ll111ll1l_opy_[bstack1l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ᯼")] = step[bstack1l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ᯽")]
            bstack11ll1111l11_opy_.append(bstack11ll111ll1l_opy_)
        cls.bstack1ll1l111_opy_({
            bstack1l1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ᯾"): bstack1l1_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ᯿"),
            bstack1l1_opy_ (u"ࠧ࡭ࡱࡪࡷࠬᰀ"): bstack11ll1111l11_opy_
        })
    @classmethod
    @bstack1lll111l_opy_(class_method=True)
    def bstack1l1ll1l11_opy_(cls, screenshot):
        cls.bstack1ll1l111_opy_({
            bstack1l1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬᰁ"): bstack1l1_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭ᰂ"),
            bstack1l1_opy_ (u"ࠪࡰࡴ࡭ࡳࠨᰃ"): [{
                bstack1l1_opy_ (u"ࠫࡰ࡯࡮ࡥࠩᰄ"): bstack1l1_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࠧᰅ"),
                bstack1l1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩᰆ"): datetime.datetime.utcnow().isoformat() + bstack1l1_opy_ (u"࡛ࠧࠩᰇ"),
                bstack1l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᰈ"): screenshot[bstack1l1_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨᰉ")],
                bstack1l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᰊ"): screenshot[bstack1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᰋ")]
            }]
        }, event_url=bstack1l1_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᰌ"))
    @classmethod
    @bstack1lll111l_opy_(class_method=True)
    def bstack1ll1l111l_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1ll1l111_opy_({
            bstack1l1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᰍ"): bstack1l1_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫᰎ"),
            bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪᰏ"): {
                bstack1l1_opy_ (u"ࠤࡸࡹ࡮ࡪࠢᰐ"): cls.current_test_uuid(),
                bstack1l1_opy_ (u"ࠥ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠤᰑ"): cls.bstack1llll11l_opy_(driver)
            }
        })
    @classmethod
    def bstack1l11ll11_opy_(cls, event: str, bstack1l1l1l1l_opy_: bstack1llll111_opy_):
        bstack1l1111l1_opy_ = {
            bstack1l1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨᰒ"): event,
            bstack1l1l1l1l_opy_.bstack1lll1ll1_opy_(): bstack1l1l1l1l_opy_.bstack1l11llll_opy_(event)
        }
        cls.bstack1ll1l111_opy_(bstack1l1111l1_opy_)
        result = getattr(bstack1l1l1l1l_opy_, bstack1l1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᰓ"), None)
        if event == bstack1l1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᰔ"):
            threading.current_thread().bstackTestMeta = {bstack1l1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᰕ"): bstack1l1_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩᰖ")}
        elif event == bstack1l1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᰗ"):
            threading.current_thread().bstackTestMeta = {bstack1l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᰘ"): getattr(result, bstack1l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᰙ"), bstack1l1_opy_ (u"ࠬ࠭ᰚ"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᰛ"), None) is None or os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᰜ")] == bstack1l1_opy_ (u"ࠣࡰࡸࡰࡱࠨᰝ")) and (os.environ.get(bstack1l1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧᰞ"), None) is None or os.environ[bstack1l1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨᰟ")] == bstack1l1_opy_ (u"ࠦࡳࡻ࡬࡭ࠤᰠ")):
            return False
        return True
    @staticmethod
    def bstack11ll111l1ll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l1ll1l1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack1l1_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫᰡ"): bstack1l1_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩᰢ"),
            bstack1l1_opy_ (u"࡙ࠧ࠯ࡅࡗ࡙ࡇࡃࡌ࠯ࡗࡉࡘ࡚ࡏࡑࡕࠪᰣ"): bstack1l1_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᰤ")
        }
        if os.environ.get(bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᰥ"), None):
            headers[bstack1l1_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪᰦ")] = bstack1l1_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧᰧ").format(os.environ[bstack1l1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠤᰨ")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack1l1_opy_ (u"࠭ࡻࡾ࠱ࡾࢁࠬᰩ").format(bstack11l1llllll1_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack1l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᰪ"), None)
    @staticmethod
    def bstack1llll11l_opy_(driver):
        return {
            bstack1l1111l11l1_opy_(): bstack1l1111l11ll_opy_(driver)
        }
    @staticmethod
    def bstack11ll111l11l_opy_(exception_info, report):
        return [{bstack1l1_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᰫ"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack111llll11l_opy_(typename):
        if bstack1l1_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧᰬ") in typename:
            return bstack1l1_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦᰭ")
        return bstack1l1_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧᰮ")