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
from browserstack_sdk.sdk_cli.bstack111l11l1l1_opy_ import (
    bstack111ll1ll11_opy_,
    bstack111ll11111_opy_,
    bstack111l1llll1_opy_,
    bstack1111llll11_opy_,
)
from browserstack_sdk.sdk_cli.bstack111l111l1l_opy_ import bstack111l111ll1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1111l11l1l_opy_, bstack1111l11l11_opy_, bstack1111ll1l11_opy_
from browserstack_sdk.sdk_cli.bstack1111ll11l1_opy_ import bstack1111lll1ll_opy_
from typing import Tuple, List, Any
class bstack1111ll1111_opy_(bstack1111lll1ll_opy_):
    bstack11111lllll_opy_ = bstack1l1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡤࡳ࡫ࡹࡩࡷࡹࠢ࿝")
    bstack1111l1llll_opy_ = bstack1l1_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣ࿞")
    bstack1111llll1l_opy_ = bstack1l1_opy_ (u"ࠥࡲࡴࡴ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧ࿟")
    bstack1111l1l11l_opy_ = bstack1l1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦ࿠")
    bstack1111llllll_opy_ = bstack1l1_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡣࡷ࡫ࡦࡴࠤ࿡")
    bstack1111l11111_opy_ = bstack1l1_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡨࡸࡥࡢࡶࡨࡨࠧ࿢")
    bstack11111lll11_opy_ = bstack1l1_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡴࡡ࡮ࡧࠥ࿣")
    bstack11111llll1_opy_ = bstack1l1_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡳࡵࡣࡷࡹࡸࠨ࿤")
    def __init__(self):
        super().__init__(bstack1111ll111l_opy_=self.bstack11111lllll_opy_, frameworks=[bstack111l111ll1_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack111l1ll111_opy_((bstack1111l11l1l_opy_.BEFORE_EACH, bstack1111l11l11_opy_.POST), self.bstack1111lll111_opy_)
        TestFramework.bstack111l1ll111_opy_((bstack1111l11l1l_opy_.TEST, bstack1111l11l11_opy_.PRE), self.bstack1111ll1l1l_opy_)
        TestFramework.bstack111l1ll111_opy_((bstack1111l11l1l_opy_.TEST, bstack1111l11l11_opy_.POST), self.bstack1111l111ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1111lll111_opy_(
        self,
        f: TestFramework,
        instance: bstack1111ll1l11_opy_,
        bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_],
        *args,
        **kwargs,
    ):
        bstack1111l1111l_opy_ = self.bstack1111l1ll11_opy_(instance.context)
        if not bstack1111l1111l_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡤࡳ࡫ࡹࡩࡷࡹ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧ࿥") + str(bstack111ll111l1_opy_) + bstack1l1_opy_ (u"ࠥࠦ࿦"))
        f.bstack111l1ll11l_opy_(instance, bstack1111ll1111_opy_.bstack1111l1llll_opy_, bstack1111l1111l_opy_)
        bstack11111ll1ll_opy_ = self.bstack1111l1ll11_opy_(instance.context, bstack1111l1ll1l_opy_=False)
        f.bstack111l1ll11l_opy_(instance, bstack1111ll1111_opy_.bstack1111llll1l_opy_, bstack11111ll1ll_opy_)
    def bstack1111ll1l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1111ll1l11_opy_,
        bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1111lll111_opy_(f, instance, bstack111ll111l1_opy_, *args, **kwargs)
        if not f.bstack111l11ll11_opy_(instance, bstack1111ll1111_opy_.bstack11111lll11_opy_, False):
            self.__1111ll1ll1_opy_(f,instance,bstack111ll111l1_opy_)
    def bstack1111l111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1111ll1l11_opy_,
        bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1111lll111_opy_(f, instance, bstack111ll111l1_opy_, *args, **kwargs)
        if not f.bstack111l11ll11_opy_(instance, bstack1111ll1111_opy_.bstack11111lll11_opy_, False):
            self.__1111ll1ll1_opy_(f, instance, bstack111ll111l1_opy_)
        if not f.bstack111l11ll11_opy_(instance, bstack1111ll1111_opy_.bstack11111llll1_opy_, False):
            self.__1111l1lll1_opy_(f, instance, bstack111ll111l1_opy_)
    def bstack1111lll1l1_opy_(
        self,
        f: bstack111l111ll1_opy_,
        driver: object,
        exec: Tuple[bstack111l1llll1_opy_, str],
        bstack111ll111l1_opy_: Tuple[bstack111ll1ll11_opy_, bstack111ll11111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1111lllll1_opy_(instance):
            return
        if f.bstack111l11ll11_opy_(instance, bstack1111ll1111_opy_.bstack11111llll1_opy_, False):
            return
        driver.execute_script(
            bstack1l1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠤ࿧").format(
                json.dumps(
                    {
                        bstack1l1_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧ࿨"): bstack1l1_opy_ (u"ࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤ࿩"),
                        bstack1l1_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࿪"): {bstack1l1_opy_ (u"ࠣࡵࡷࡥࡹࡻࡳࠣ࿫"): result},
                    }
                )
            )
        )
        f.bstack111l1ll11l_opy_(instance, bstack1111ll1111_opy_.bstack11111llll1_opy_, True)
    def bstack1111l1ll11_opy_(self, context: bstack1111llll11_opy_, bstack1111l1ll1l_opy_= True):
        if bstack1111l1ll1l_opy_:
            bstack1111l1111l_opy_ = self.bstack11111lll1l_opy_(context, reverse=True)
        else:
            bstack1111l1111l_opy_ = self.bstack1111l11ll1_opy_(context, reverse=True)
        return [f for f in bstack1111l1111l_opy_ if f[1].state != bstack111ll1ll11_opy_.QUIT]
    def __1111l1lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1111ll1l11_opy_,
        bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_],
    ):
        bstack1111l1111l_opy_ = f.bstack111l11ll11_opy_(instance, bstack1111ll1111_opy_.bstack1111l1llll_opy_, [])
        if not bstack1111l1111l_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡤࡳ࡫ࡹࡩࡷࡹ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧ࿬") + str(bstack111ll111l1_opy_) + bstack1l1_opy_ (u"ࠥࠦ࿭"))
            return
        driver = bstack1111l1111l_opy_[0][0]()
        status = f.bstack111l11ll11_opy_(instance, TestFramework.bstack1111l1l1ll_opy_, None)
        if not status:
            self.logger.debug(bstack1l1_opy_ (u"ࠦࡸ࡫ࡴࡠࡣࡦࡸ࡮ࡼࡥࡠࡦࡵ࡭ࡻ࡫ࡲࡴ࠼ࠣࡲࡴࠦࡳࡵࡣࡷࡹࡸࠦࡦࡰࡴࠣࡸࡪࡹࡴ࠭ࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨ࿮") + str(bstack111ll111l1_opy_) + bstack1l1_opy_ (u"ࠧࠨ࿯"))
            return
        bstack1111ll1lll_opy_ = {bstack1l1_opy_ (u"ࠨࡳࡵࡣࡷࡹࡸࠨ࿰"): status.lower()}
        bstack1111ll11ll_opy_ = f.bstack111l11ll11_opy_(instance, TestFramework.bstack1111lll11l_opy_, None)
        if status.lower() == bstack1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ࿱") and bstack1111ll11ll_opy_ is not None:
            bstack1111ll1lll_opy_[bstack1l1_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨ࿲")] = bstack1111ll11ll_opy_[0][bstack1l1_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬ࿳")][0] if isinstance(bstack1111ll11ll_opy_, list) else str(bstack1111ll11ll_opy_)
        driver.execute_script(
            bstack1l1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠣ࿴").format(
                json.dumps(
                    {
                        bstack1l1_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦ࿵"): bstack1l1_opy_ (u"ࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣ࿶"),
                        bstack1l1_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࿷"): bstack1111ll1lll_opy_,
                    }
                )
            )
        )
        f.bstack111l1ll11l_opy_(instance, bstack1111ll1111_opy_.bstack11111llll1_opy_, True)
    def __1111ll1ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1111ll1l11_opy_,
        bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_]
    ):
        test_name = f.bstack111l11ll11_opy_(instance, TestFramework.bstack1111l1l1l1_opy_, None)
        if not test_name:
            self.logger.debug(bstack1l1_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡰࡤࡱࡪࠨ࿸"))
            return
        bstack1111l1111l_opy_ = f.bstack111l11ll11_opy_(instance, bstack1111ll1111_opy_.bstack1111l1llll_opy_, [])
        if not bstack1111l1111l_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠣࡵࡨࡸࡤࡧࡣࡵ࡫ࡹࡩࡤࡪࡲࡪࡸࡨࡶࡸࡀࠠ࡯ࡱࠣࡷࡹࡧࡴࡶࡵࠣࡪࡴࡸࠠࡵࡧࡶࡸ࠱ࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࠥ࿹") + str(bstack111ll111l1_opy_) + bstack1l1_opy_ (u"ࠤࠥ࿺"))
            return
        for bstack1111l111l1_opy_, bstack1111l1l111_opy_ in bstack1111l1111l_opy_:
            if not bstack111l111ll1_opy_.bstack1111lllll1_opy_(bstack1111l1l111_opy_):
                continue
            driver = bstack1111l111l1_opy_()
            if not driver:
                continue
            driver.execute_script(
                bstack1l1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠣ࿻").format(
                    json.dumps(
                        {
                            bstack1l1_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦ࿼"): bstack1l1_opy_ (u"ࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨ࿽"),
                            bstack1l1_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࿾"): {bstack1l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ࿿"): test_name},
                        }
                    )
                )
            )
        f.bstack111l1ll11l_opy_(instance, bstack1111ll1111_opy_.bstack11111lll11_opy_, True)