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
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111111l11l_opy_, bstack111111lll1_opy_, bstack11llll1l1l_opy_, bstack11l11ll11l_opy_, bstack1llll11l1l1_opy_, bstack1lll11llll1_opy_, bstack1llll11lll1_opy_, bstack1l1l11lll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack1ll11ll111l_opy_ import bstack1ll11l1ll11_opy_
import bstack_utils.bstack1l1ll11l_opy_ as bstack1llll1ll1_opy_
from bstack_utils.bstack11l1lll111_opy_ import bstack1l1l11l1l1_opy_
import bstack_utils.bstack111ll1111l_opy_ as bstack1l1lll1l1_opy_
from bstack_utils.bstack1l11l1lll1_opy_ import bstack1l11l1lll1_opy_
from bstack_utils.bstack11l1l11ll1_opy_ import bstack11l11ll1l1_opy_
bstack1l1lllll11l_opy_ = bstack11111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡨࡵ࡬࡭ࡧࡦࡸࡴࡸ࠭ࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪ᝖")
logger = logging.getLogger(__name__)
class bstack1lll11llll_opy_:
    bstack1ll11ll111l_opy_ = None
    bs_config = None
    bstack11ll111l_opy_ = None
    @classmethod
    @bstack11l11ll11l_opy_(class_method=True)
    @measure(event_name=EVENTS.bstack1llll1l1l11_opy_, stage=STAGE.SINGLE)
    def launch(cls, bs_config, bstack11ll111l_opy_):
        cls.bs_config = bs_config
        cls.bstack11ll111l_opy_ = bstack11ll111l_opy_
        try:
            cls.bstack1ll11111lll_opy_()
            bstack11111l1l1l_opy_ = bstack111111l11l_opy_(bs_config)
            bstack1lllllll1ll_opy_ = bstack111111lll1_opy_(bs_config)
            data = bstack1llll1ll1_opy_.bstack1l1lllll1l1_opy_(bs_config, bstack11ll111l_opy_)
            config = {
                bstack11111_opy_ (u"ࠫࡦࡻࡴࡩࠩ᝗"): (bstack11111l1l1l_opy_, bstack1lllllll1ll_opy_),
                bstack11111_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭᝘"): cls.default_headers()
            }
            response = bstack11llll1l1l_opy_(bstack11111_opy_ (u"࠭ࡐࡐࡕࡗࠫ᝙"), cls.request_url(bstack11111_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠸࠯ࡣࡷ࡬ࡰࡩࡹࠧ᝚")), data, config)
            if response.status_code != 200:
                bstack1ll1111l11l_opy_ = response.json()
                if bstack1ll1111l11l_opy_[bstack11111_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩ᝛")] == False:
                    cls.bstack1l1llll11l1_opy_(bstack1ll1111l11l_opy_)
                    return
                cls.bstack1l1llll111l_opy_(bstack1ll1111l11l_opy_[bstack11111_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ᝜")])
                cls.bstack1ll11111ll1_opy_(bstack1ll1111l11l_opy_[bstack11111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ᝝")])
                return None
            bstack1ll11111111_opy_ = cls.bstack1ll1111l111_opy_(response)
            return bstack1ll11111111_opy_
        except Exception as error:
            logger.error(bstack11111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡤࡸ࡭ࡱࡪࠠࡧࡱࡵࠤ࡙࡫ࡳࡵࡊࡸࡦ࠿ࠦࡻࡾࠤ᝞").format(str(error)))
            return None
    @classmethod
    @bstack11l11ll11l_opy_(class_method=True)
    def stop(cls, bstack1l1llllll1l_opy_=None):
        if not bstack1l1l11l1l1_opy_.on() and not bstack1l1lll1l1_opy_.on():
            return
        if os.environ.get(bstack11111_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭᝟")) == bstack11111_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦᝠ") or os.environ.get(bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᝡ")) == bstack11111_opy_ (u"ࠣࡰࡸࡰࡱࠨᝢ"):
            logger.error(bstack11111_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡷࡳࡵࠦࡢࡶ࡫࡯ࡨࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡗࡩࡸࡺࡈࡶࡤ࠽ࠤࡒ࡯ࡳࡴ࡫ࡱ࡫ࠥࡧࡵࡵࡪࡨࡲࡹ࡯ࡣࡢࡶ࡬ࡳࡳࠦࡴࡰ࡭ࡨࡲࠬᝣ"))
            return {
                bstack11111_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᝤ"): bstack11111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᝥ"),
                bstack11111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᝦ"): bstack11111_opy_ (u"࠭ࡔࡰ࡭ࡨࡲ࠴ࡨࡵࡪ࡮ࡧࡍࡉࠦࡩࡴࠢࡸࡲࡩ࡫ࡦࡪࡰࡨࡨ࠱ࠦࡢࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠ࡮࡫ࡪ࡬ࡹࠦࡨࡢࡸࡨࠤ࡫ࡧࡩ࡭ࡧࡧࠫᝧ")
            }
        try:
            cls.bstack1ll11ll111l_opy_.shutdown()
            data = {
                bstack11111_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᝨ"): bstack1l1l11lll_opy_()
            }
            if not bstack1l1llllll1l_opy_ is None:
                data[bstack11111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡱࡪࡺࡡࡥࡣࡷࡥࠬᝩ")] = [{
                    bstack11111_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩᝪ"): bstack11111_opy_ (u"ࠪࡹࡸ࡫ࡲࡠ࡭࡬ࡰࡱ࡫ࡤࠨᝫ"),
                    bstack11111_opy_ (u"ࠫࡸ࡯ࡧ࡯ࡣ࡯ࠫᝬ"): bstack1l1llllll1l_opy_
                }]
            config = {
                bstack11111_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭᝭"): cls.default_headers()
            }
            bstack111l111lll_opy_ = bstack11111_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾ࠱ࡶࡸࡴࡶࠧᝮ").format(os.environ[bstack11111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠧᝯ")])
            bstack1ll111111ll_opy_ = cls.request_url(bstack111l111lll_opy_)
            response = bstack11llll1l1l_opy_(bstack11111_opy_ (u"ࠨࡒࡘࡘࠬᝰ"), bstack1ll111111ll_opy_, data, config)
            if not response.ok:
                raise Exception(bstack11111_opy_ (u"ࠤࡖࡸࡴࡶࠠࡳࡧࡴࡹࡪࡹࡴࠡࡰࡲࡸࠥࡵ࡫ࠣ᝱"))
        except Exception as error:
            logger.error(bstack11111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡴࡶࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣࡘࡪࡹࡴࡉࡷࡥ࠾࠿ࠦࠢᝲ") + str(error))
            return {
                bstack11111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᝳ"): bstack11111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ᝴"),
                bstack11111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ᝵"): str(error)
            }
    @classmethod
    @bstack11l11ll11l_opy_(class_method=True)
    def bstack1ll1111l111_opy_(cls, response):
        bstack1ll1111l11l_opy_ = response.json()
        bstack1ll11111111_opy_ = {}
        if bstack1ll1111l11l_opy_.get(bstack11111_opy_ (u"ࠧ࡫ࡹࡷࠫ᝶")) is None:
            os.environ[bstack11111_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ᝷")] = bstack11111_opy_ (u"ࠩࡱࡹࡱࡲࠧ᝸")
        else:
            os.environ[bstack11111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ᝹")] = bstack1ll1111l11l_opy_.get(bstack11111_opy_ (u"ࠫ࡯ࡽࡴࠨ᝺"), bstack11111_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ᝻"))
        os.environ[bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ᝼")] = bstack1ll1111l11l_opy_.get(bstack11111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ᝽"), bstack11111_opy_ (u"ࠨࡰࡸࡰࡱ࠭᝾"))
        if bstack1l1l11l1l1_opy_.bstack1l1llll1lll_opy_(cls.bs_config, cls.bstack11ll111l_opy_.get(bstack11111_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡻࡳࡦࡦࠪ᝿"), bstack11111_opy_ (u"ࠪࠫក"))) is True:
            bstack1l1llllllll_opy_, bstack1llll111l1_opy_, bstack1l1lllllll1_opy_ = cls.bstack1ll1111ll1l_opy_(bstack1ll1111l11l_opy_)
            if bstack1l1llllllll_opy_ != None and bstack1llll111l1_opy_ != None:
                bstack1ll11111111_opy_[bstack11111_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫខ")] = {
                    bstack11111_opy_ (u"ࠬࡰࡷࡵࡡࡷࡳࡰ࡫࡮ࠨគ"): bstack1l1llllllll_opy_,
                    bstack11111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨឃ"): bstack1llll111l1_opy_,
                    bstack11111_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫង"): bstack1l1lllllll1_opy_
                }
            else:
                bstack1ll11111111_opy_[bstack11111_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨច")] = {}
        else:
            bstack1ll11111111_opy_[bstack11111_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩឆ")] = {}
        if bstack1l1lll1l1_opy_.bstack11111l1l11_opy_(cls.bs_config) is True:
            bstack1l1llll11ll_opy_, bstack1llll111l1_opy_ = cls.bstack1l1llllll11_opy_(bstack1ll1111l11l_opy_)
            if bstack1l1llll11ll_opy_ != None and bstack1llll111l1_opy_ != None:
                bstack1ll11111111_opy_[bstack11111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪជ")] = {
                    bstack11111_opy_ (u"ࠫࡦࡻࡴࡩࡡࡷࡳࡰ࡫࡮ࠨឈ"): bstack1l1llll11ll_opy_,
                    bstack11111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧញ"): bstack1llll111l1_opy_,
                }
            else:
                bstack1ll11111111_opy_[bstack11111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ដ")] = {}
        else:
            bstack1ll11111111_opy_[bstack11111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧឋ")] = {}
        if bstack1ll11111111_opy_[bstack11111_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨឌ")].get(bstack11111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫឍ")) != None or bstack1ll11111111_opy_[bstack11111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪណ")].get(bstack11111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ត")) != None:
            cls.bstack1l1llll1l11_opy_(bstack1ll1111l11l_opy_.get(bstack11111_opy_ (u"ࠬࡰࡷࡵࠩថ")), bstack1ll1111l11l_opy_.get(bstack11111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨទ")))
        return bstack1ll11111111_opy_
    @classmethod
    def bstack1ll1111ll1l_opy_(cls, bstack1ll1111l11l_opy_):
        if bstack1ll1111l11l_opy_.get(bstack11111_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧធ")) == None:
            cls.bstack1l1llll111l_opy_()
            return [None, None, None]
        if bstack1ll1111l11l_opy_[bstack11111_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨន")][bstack11111_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪប")] != True:
            cls.bstack1l1llll111l_opy_(bstack1ll1111l11l_opy_[bstack11111_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪផ")])
            return [None, None, None]
        logger.debug(bstack11111_opy_ (u"࡙ࠫ࡫ࡳࡵࠢࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠢࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲࠡࠨព"))
        os.environ[bstack11111_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡅࡒࡑࡕࡒࡅࡕࡇࡇࠫភ")] = bstack11111_opy_ (u"࠭ࡴࡳࡷࡨࠫម")
        if bstack1ll1111l11l_opy_.get(bstack11111_opy_ (u"ࠧ࡫ࡹࡷࠫយ")):
            os.environ[bstack11111_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡐࡗࡕࠩរ")] = bstack1ll1111l11l_opy_[bstack11111_opy_ (u"ࠩ࡭ࡻࡹ࠭ល")]
            os.environ[bstack11111_opy_ (u"ࠪࡇࡗࡋࡄࡆࡐࡗࡍࡆࡒࡓࡠࡈࡒࡖࡤࡉࡒࡂࡕࡋࡣࡗࡋࡐࡐࡔࡗࡍࡓࡍࠧវ")] = json.dumps({
                bstack11111_opy_ (u"ࠫࡺࡹࡥࡳࡰࡤࡱࡪ࠭ឝ"): bstack111111l11l_opy_(cls.bs_config),
                bstack11111_opy_ (u"ࠬࡶࡡࡴࡵࡺࡳࡷࡪࠧឞ"): bstack111111lll1_opy_(cls.bs_config)
            })
        if bstack1ll1111l11l_opy_.get(bstack11111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨស")):
            os.environ[bstack11111_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭ហ")] = bstack1ll1111l11l_opy_[bstack11111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪឡ")]
        if bstack1ll1111l11l_opy_[bstack11111_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩអ")].get(bstack11111_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫឣ"), {}).get(bstack11111_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨឤ")):
            os.environ[bstack11111_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭ឥ")] = str(bstack1ll1111l11l_opy_[bstack11111_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ឦ")][bstack11111_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨឧ")][bstack11111_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬឨ")])
        return [bstack1ll1111l11l_opy_[bstack11111_opy_ (u"ࠩ࡭ࡻࡹ࠭ឩ")], bstack1ll1111l11l_opy_[bstack11111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬឪ")], os.environ[bstack11111_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡃࡏࡐࡔ࡝࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࡗࠬឫ")]]
    @classmethod
    def bstack1l1llllll11_opy_(cls, bstack1ll1111l11l_opy_):
        if bstack1ll1111l11l_opy_.get(bstack11111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬឬ")) == None:
            cls.bstack1ll11111ll1_opy_()
            return [None, None]
        if bstack1ll1111l11l_opy_[bstack11111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ឭ")][bstack11111_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨឮ")] != True:
            cls.bstack1ll11111ll1_opy_(bstack1ll1111l11l_opy_[bstack11111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨឯ")])
            return [None, None]
        if bstack1ll1111l11l_opy_[bstack11111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩឰ")].get(bstack11111_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫឱ")):
            logger.debug(bstack11111_opy_ (u"࡙ࠫ࡫ࡳࡵࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲࠡࠨឲ"))
            parsed = json.loads(os.getenv(bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ឳ"), bstack11111_opy_ (u"࠭ࡻࡾࠩ឴")))
            capabilities = bstack1llll1ll1_opy_.bstack1ll1111l1l1_opy_(bstack1ll1111l11l_opy_[bstack11111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ឵")][bstack11111_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩា")][bstack11111_opy_ (u"ࠩࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨិ")], bstack11111_opy_ (u"ࠪࡲࡦࡳࡥࠨី"), bstack11111_opy_ (u"ࠫࡻࡧ࡬ࡶࡧࠪឹ"))
            bstack1l1llll11ll_opy_ = capabilities[bstack11111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࡙ࡵ࡫ࡦࡰࠪឺ")]
            os.environ[bstack11111_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫុ")] = bstack1l1llll11ll_opy_
            parsed[bstack11111_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨូ")] = capabilities[bstack11111_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩួ")]
            os.environ[bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪើ")] = json.dumps(parsed)
            scripts = bstack1llll1ll1_opy_.bstack1ll1111l1l1_opy_(bstack1ll1111l11l_opy_[bstack11111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪឿ")][bstack11111_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬៀ")][bstack11111_opy_ (u"ࠬࡹࡣࡳ࡫ࡳࡸࡸ࠭េ")], bstack11111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫែ"), bstack11111_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࠨៃ"))
            bstack1l11l1lll1_opy_.bstack111111l1l1_opy_(scripts)
            commands = bstack1ll1111l11l_opy_[bstack11111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨោ")][bstack11111_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪៅ")][bstack11111_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷ࡙ࡵࡗࡳࡣࡳࠫំ")].get(bstack11111_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭ះ"))
            bstack1l11l1lll1_opy_.bstack1lllllllll1_opy_(commands)
            bstack1l11l1lll1_opy_.store()
        return [bstack1l1llll11ll_opy_, bstack1ll1111l11l_opy_[bstack11111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧៈ")]]
    @classmethod
    def bstack1l1llll111l_opy_(cls, response=None):
        os.environ[bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ៉")] = bstack11111_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬ៊")
        os.environ[bstack11111_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡈࡕࡍࡑࡎࡈࡘࡊࡊࠧ់")] = bstack11111_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ៌")
        os.environ[bstack11111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ៍")] = bstack11111_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ៎")
        os.environ[bstack11111_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭៏")] = bstack11111_opy_ (u"࠭࡮ࡶ࡮࡯ࠫ័")
        os.environ[bstack11111_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭៑")] = bstack11111_opy_ (u"ࠣࡰࡸࡰࡱࠨ្")
        os.environ[bstack11111_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪ៓")] = bstack11111_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ។")
        cls.bstack1l1llll11l1_opy_(response, bstack11111_opy_ (u"ࠦࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠦ៕"))
        return [None, None, None]
    @classmethod
    def bstack1ll11111ll1_opy_(cls, response=None):
        os.environ[bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ៖")] = bstack11111_opy_ (u"࠭࡮ࡶ࡮࡯ࠫៗ")
        os.environ[bstack11111_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ៘")] = bstack11111_opy_ (u"ࠨࡰࡸࡰࡱ࠭៙")
        os.environ[bstack11111_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ៚")] = bstack11111_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ៛")
        cls.bstack1l1llll11l1_opy_(response, bstack11111_opy_ (u"ࠦࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠦៜ"))
        return [None, None, None]
    @classmethod
    def bstack1l1llll1l11_opy_(cls, bstack1ll1111ll11_opy_, bstack1llll111l1_opy_):
        os.environ[bstack11111_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭៝")] = bstack1ll1111ll11_opy_
        os.environ[bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ៞")] = bstack1llll111l1_opy_
    @classmethod
    def bstack1l1llll11l1_opy_(cls, response=None, product=bstack11111_opy_ (u"ࠢࠣ៟")):
        if response == None:
            logger.error(product + bstack11111_opy_ (u"ࠣࠢࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡪࡦ࡯࡬ࡦࡦࠥ០"))
        for error in response[bstack11111_opy_ (u"ࠩࡨࡶࡷࡵࡲࡴࠩ១")]:
            bstack1lll111llll_opy_ = error[bstack11111_opy_ (u"ࠪ࡯ࡪࡿࠧ២")]
            error_message = error[bstack11111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ៣")]
            if error_message:
                if bstack1lll111llll_opy_ == bstack11111_opy_ (u"ࠧࡋࡒࡓࡑࡕࡣࡆࡉࡃࡆࡕࡖࡣࡉࡋࡎࡊࡇࡇࠦ៤"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack11111_opy_ (u"ࠨࡄࡢࡶࡤࠤࡺࡶ࡬ࡰࡣࡧࠤࡹࡵࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࠢ៥") + product + bstack11111_opy_ (u"ࠢࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡦࡸࡩࠥࡺ࡯ࠡࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠧ៦"))
    @classmethod
    def bstack1ll11111lll_opy_(cls):
        if cls.bstack1ll11ll111l_opy_ is not None:
            return
        cls.bstack1ll11ll111l_opy_ = bstack1ll11l1ll11_opy_(cls.bstack1ll11111l1l_opy_)
        cls.bstack1ll11ll111l_opy_.start()
    @classmethod
    def bstack11l11l11l1_opy_(cls):
        if cls.bstack1ll11ll111l_opy_ is None:
            return
        cls.bstack1ll11ll111l_opy_.shutdown()
    @classmethod
    @bstack11l11ll11l_opy_(class_method=True)
    def bstack1ll11111l1l_opy_(cls, bstack11l111l1ll_opy_, bstack1ll1111l1ll_opy_=bstack11111_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡤࡸࡨ࡮ࠧ៧")):
        config = {
            bstack11111_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪ៨"): cls.default_headers()
        }
        logger.debug(bstack11111_opy_ (u"ࠥࡴࡴࡹࡴࡠࡦࡤࡸࡦࡀࠠࡔࡧࡱࡨ࡮ࡴࡧࠡࡦࡤࡸࡦࠦࡴࡰࠢࡷࡩࡸࡺࡨࡶࡤࠣࡪࡴࡸࠠࡦࡸࡨࡲࡹࡹࠠࡼࡿࠥ៩").format(bstack11111_opy_ (u"ࠫ࠱ࠦࠧ៪").join([event[bstack11111_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ៫")] for event in bstack11l111l1ll_opy_])))
        response = bstack11llll1l1l_opy_(bstack11111_opy_ (u"࠭ࡐࡐࡕࡗࠫ៬"), cls.request_url(bstack1ll1111l1ll_opy_), bstack11l111l1ll_opy_, config)
        bstack1lllllll111_opy_ = response.json()
    @classmethod
    def bstack1l11l1l1l1_opy_(cls, bstack11l111l1ll_opy_, bstack1ll1111l1ll_opy_=bstack11111_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡣࡷࡧ࡭࠭៭")):
        logger.debug(bstack11111_opy_ (u"ࠣࡵࡨࡲࡩࡥࡤࡢࡶࡤ࠾ࠥࡇࡴࡵࡧࡰࡴࡹ࡯࡮ࡨࠢࡷࡳࠥࡧࡤࡥࠢࡧࡥࡹࡧࠠࡵࡱࠣࡦࡦࡺࡣࡩࠢࡺ࡭ࡹ࡮ࠠࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨ࠾ࠥࢁࡽࠣ៮").format(bstack11l111l1ll_opy_[bstack11111_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭៯")]))
        if not bstack1llll1ll1_opy_.bstack1l1lllll1ll_opy_(bstack11l111l1ll_opy_[bstack11111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ៰")]):
            logger.debug(bstack11111_opy_ (u"ࠦࡸ࡫࡮ࡥࡡࡧࡥࡹࡧ࠺ࠡࡐࡲࡸࠥࡧࡤࡥ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡻ࡮ࡺࡨࠡࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩ࠿ࠦࡻࡾࠤ៱").format(bstack11l111l1ll_opy_[bstack11111_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ៲")]))
            return
        bstack111l1ll1l_opy_ = bstack1llll1ll1_opy_.bstack1l1lllll111_opy_(bstack11l111l1ll_opy_[bstack11111_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ៳")], bstack11l111l1ll_opy_.get(bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩ៴")))
        if bstack111l1ll1l_opy_ != None:
            if bstack11l111l1ll_opy_.get(bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪ៵")) != None:
                bstack11l111l1ll_opy_[bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ៶")][bstack11111_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࡣࡲࡧࡰࠨ៷")] = bstack111l1ll1l_opy_
            else:
                bstack11l111l1ll_opy_[bstack11111_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࡤࡳࡡࡱࠩ៸")] = bstack111l1ll1l_opy_
        if bstack1ll1111l1ll_opy_ == bstack11111_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡡࡵࡥ࡫ࠫ៹"):
            cls.bstack1ll11111lll_opy_()
            logger.debug(bstack11111_opy_ (u"ࠨࡳࡦࡰࡧࡣࡩࡧࡴࡢ࠼ࠣࡅࡩࡪࡩ࡯ࡩࠣࡨࡦࡺࡡࠡࡶࡲࠤࡧࡧࡴࡤࡪࠣࡻ࡮ࡺࡨࠡࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩ࠿ࠦࡻࡾࠤ៺").format(bstack11l111l1ll_opy_[bstack11111_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ៻")]))
            cls.bstack1ll11ll111l_opy_.add(bstack11l111l1ll_opy_)
        elif bstack1ll1111l1ll_opy_ == bstack11111_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭៼"):
            cls.bstack1ll11111l1l_opy_([bstack11l111l1ll_opy_], bstack1ll1111l1ll_opy_)
    @classmethod
    @bstack11l11ll11l_opy_(class_method=True)
    def bstack11lll1l111_opy_(cls, bstack11l111l11l_opy_):
        bstack1l1llll1ll1_opy_ = []
        for log in bstack11l111l11l_opy_:
            bstack1ll11111l11_opy_ = {
                bstack11111_opy_ (u"ࠩ࡮࡭ࡳࡪࠧ៽"): bstack11111_opy_ (u"ࠪࡘࡊ࡙ࡔࡠࡎࡒࡋࠬ៾"),
                bstack11111_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ៿"): log[bstack11111_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ᠀")],
                bstack11111_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ᠁"): log[bstack11111_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ᠂")],
                bstack11111_opy_ (u"ࠨࡪࡷࡸࡵࡥࡲࡦࡵࡳࡳࡳࡹࡥࠨ᠃"): {},
                bstack11111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ᠄"): log[bstack11111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ᠅")],
            }
            if bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ᠆") in log:
                bstack1ll11111l11_opy_[bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ᠇")] = log[bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭᠈")]
            elif bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ᠉") in log:
                bstack1ll11111l11_opy_[bstack11111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ᠊")] = log[bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ᠋")]
            bstack1l1llll1ll1_opy_.append(bstack1ll11111l11_opy_)
        cls.bstack1l11l1l1l1_opy_({
            bstack11111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ᠌"): bstack11111_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨ᠍"),
            bstack11111_opy_ (u"ࠬࡲ࡯ࡨࡵࠪ᠎"): bstack1l1llll1ll1_opy_
        })
    @classmethod
    @bstack11l11ll11l_opy_(class_method=True)
    def bstack1l1lll1llll_opy_(cls, steps):
        bstack1ll1111111l_opy_ = []
        for step in steps:
            bstack1l1llll1l1l_opy_ = {
                bstack11111_opy_ (u"࠭࡫ࡪࡰࡧࠫ᠏"): bstack11111_opy_ (u"ࠧࡕࡇࡖࡘࡤ࡙ࡔࡆࡒࠪ᠐"),
                bstack11111_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ᠑"): step[bstack11111_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ᠒")],
                bstack11111_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭᠓"): step[bstack11111_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ᠔")],
                bstack11111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭᠕"): step[bstack11111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ᠖")],
                bstack11111_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩ᠗"): step[bstack11111_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪ᠘")]
            }
            if bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ᠙") in step:
                bstack1l1llll1l1l_opy_[bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ᠚")] = step[bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ᠛")]
            elif bstack11111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ᠜") in step:
                bstack1l1llll1l1l_opy_[bstack11111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭᠝")] = step[bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ᠞")]
            bstack1ll1111111l_opy_.append(bstack1l1llll1l1l_opy_)
        cls.bstack1l11l1l1l1_opy_({
            bstack11111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ᠟"): bstack11111_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭ᠠ"),
            bstack11111_opy_ (u"ࠪࡰࡴ࡭ࡳࠨᠡ"): bstack1ll1111111l_opy_
        })
    @classmethod
    @bstack11l11ll11l_opy_(class_method=True)
    def bstack11lll1l1ll_opy_(cls, screenshot):
        cls.bstack1l11l1l1l1_opy_({
            bstack11111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨᠢ"): bstack11111_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩᠣ"),
            bstack11111_opy_ (u"࠭࡬ࡰࡩࡶࠫᠤ"): [{
                bstack11111_opy_ (u"ࠧ࡬࡫ࡱࡨࠬᠥ"): bstack11111_opy_ (u"ࠨࡖࡈࡗ࡙ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࠪᠦ"),
                bstack11111_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬᠧ"): datetime.datetime.utcnow().isoformat() + bstack11111_opy_ (u"ࠪ࡞ࠬᠨ"),
                bstack11111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᠩ"): screenshot[bstack11111_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࠫᠪ")],
                bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᠫ"): screenshot[bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᠬ")]
            }]
        }, bstack1ll1111l1ll_opy_=bstack11111_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭ᠭ"))
    @classmethod
    @bstack11l11ll11l_opy_(class_method=True)
    def bstack1l1lll11_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1l11l1l1l1_opy_({
            bstack11111_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ᠮ"): bstack11111_opy_ (u"ࠪࡇࡇ࡚ࡓࡦࡵࡶ࡭ࡴࡴࡃࡳࡧࡤࡸࡪࡪࠧᠯ"),
            bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭ᠰ"): {
                bstack11111_opy_ (u"ࠧࡻࡵࡪࡦࠥᠱ"): cls.current_test_uuid(),
                bstack11111_opy_ (u"ࠨࡩ࡯ࡶࡨ࡫ࡷࡧࡴࡪࡱࡱࡷࠧᠲ"): cls.bstack11l1ll1ll1_opy_(driver)
            }
        })
    @classmethod
    def bstack11l1l1lll1_opy_(cls, event: str, bstack11l111l1ll_opy_: bstack11l11ll1l1_opy_):
        bstack111lll11ll_opy_ = {
            bstack11111_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫᠳ"): event,
            bstack11l111l1ll_opy_.bstack111llll11l_opy_(): bstack11l111l1ll_opy_.bstack111lll1ll1_opy_(event)
        }
        cls.bstack1l11l1l1l1_opy_(bstack111lll11ll_opy_)
        result = getattr(bstack11l111l1ll_opy_, bstack11111_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᠴ"), None)
        if event == bstack11111_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᠵ"):
            threading.current_thread().bstackTestMeta = {bstack11111_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᠶ"): bstack11111_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬᠷ")}
        elif event == bstack11111_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᠸ"):
            threading.current_thread().bstackTestMeta = {bstack11111_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ᠹ"): getattr(result, bstack11111_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᠺ"), bstack11111_opy_ (u"ࠨࠩᠻ"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack11111_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡊࡘࡖࠪᠼ"), None) is None or os.environ[bstack11111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡋ࡙ࡗࠫᠽ")] == bstack11111_opy_ (u"ࠦࡳࡻ࡬࡭ࠤᠾ")) and (os.environ.get(bstack11111_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪᠿ"), None) is None or os.environ[bstack11111_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫᡀ")] == bstack11111_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᡁ")):
            return False
        return True
    @staticmethod
    def bstack1ll111111l1_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1lll11llll_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack11111_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧᡂ"): bstack11111_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬᡃ"),
            bstack11111_opy_ (u"ࠪ࡜࠲ࡈࡓࡕࡃࡆࡏ࠲࡚ࡅࡔࡖࡒࡔࡘ࠭ᡄ"): bstack11111_opy_ (u"ࠫࡹࡸࡵࡦࠩᡅ")
        }
        if os.environ.get(bstack11111_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᡆ"), None):
            headers[bstack11111_opy_ (u"࠭ࡁࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ᡇ")] = bstack11111_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪᡈ").format(os.environ[bstack11111_opy_ (u"ࠣࡄࡖࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠤᡉ")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack11111_opy_ (u"ࠩࡾࢁ࠴ࢁࡽࠨᡊ").format(bstack1l1lllll11l_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᡋ"), None)
    @staticmethod
    def bstack11l1ll1ll1_opy_(driver):
        return {
            bstack1llll11l1l1_opy_(): bstack1lll11llll1_opy_(driver)
        }
    @staticmethod
    def bstack1l1llll1111_opy_(exception_info, report):
        return [{bstack11111_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧᡌ"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack111l1ll1ll_opy_(typename):
        if bstack11111_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣᡍ") in typename:
            return bstack11111_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢᡎ")
        return bstack11111_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣᡏ")