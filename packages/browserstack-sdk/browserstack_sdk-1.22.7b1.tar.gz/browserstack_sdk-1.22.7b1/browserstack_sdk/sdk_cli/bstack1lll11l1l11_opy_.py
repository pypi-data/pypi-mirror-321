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
from datetime import datetime
import os
from browserstack_sdk.sdk_cli.bstack111l11l1l1_opy_ import (
    bstack111ll1ll11_opy_,
    bstack111ll11111_opy_,
    bstack11111ll111_opy_,
    bstack111l1llll1_opy_,
)
from browserstack_sdk.sdk_cli.bstack111l111l1l_opy_ import bstack111l111ll1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1111l11l1l_opy_, bstack1111l11l11_opy_, bstack1111ll1l11_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack111l1ll1ll_opy_ import bstack111ll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1111l11lll_opy_ import bstack1111ll1111_opy_
import grpc
import traceback
class bstack1ll1l1l111l_opy_(bstack111ll1l111_opy_):
    bstack1lll11lll11_opy_ = False
    bstack1ll111l1l11_opy_ = bstack1l1_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱ࠳ࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲࠣᇳ")
    bstack1ll1111llll_opy_ = bstack1l1_opy_ (u"ࠦࡷ࡫࡭ࡰࡶࡨ࠲ࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸࠢᇴ")
    bstack1ll1111l11l_opy_ = bstack1l1_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤ࡯࡮ࡪࡶࠥᇵ")
    bstack1ll1111l111_opy_ = bstack1l1_opy_ (u"ࠨࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡩࡴࡡࡶࡧࡦࡴ࡮ࡪࡰࡪࠦᇶ")
    bstack1ll1111ll11_opy_ = bstack1l1_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࡟ࡩࡣࡶࡣࡺࡸ࡬ࠣᇷ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        if not self.is_enabled():
            return
        bstack111l111ll1_opy_.bstack111l1ll111_opy_((bstack111ll1ll11_opy_.bstack111ll1l1l1_opy_, bstack111ll11111_opy_.PRE), self.bstack1ll11111l1l_opy_)
        TestFramework.bstack111l1ll111_opy_((bstack1111l11l1l_opy_.TEST, bstack1111l11l11_opy_.PRE), self.bstack1111ll1l1l_opy_)
        TestFramework.bstack111l1ll111_opy_((bstack1111l11l1l_opy_.TEST, bstack1111l11l11_opy_.POST), self.bstack1111l111ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1111ll1l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1111ll1l11_opy_,
        bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1ll111ll111_opy_(instance, args)
        test_framework = f.bstack111l11ll11_opy_(instance, TestFramework.bstack1llllll111l_opy_)
        if bstack1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬᇸ") in instance.bstack1llll1l1l11_opy_:
            platform_index = f.bstack111l11ll11_opy_(instance, TestFramework.bstack111l111l11_opy_)
            self.accessibility = self.bstack11l1lll1l_opy_(tags) and self.bstack1ll1111ll_opy_(self.config[bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬᇹ")][platform_index])
        else:
            bstack1111l1111l_opy_ = f.bstack111l11ll11_opy_(instance, bstack1111ll1111_opy_.bstack1111l1llll_opy_, [])
            if not bstack1111l1111l_opy_:
                self.logger.debug(bstack1l1_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᇺ") + str(kwargs) + bstack1l1_opy_ (u"ࠦࠧᇻ"))
                return
            if len(bstack1111l1111l_opy_) > 1:
                self.logger.debug(bstack1l1_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠࡼ࡮ࡨࡲ࠭ࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᇼ") + str(kwargs) + bstack1l1_opy_ (u"ࠨࠢᇽ"))
            bstack1111l111l1_opy_, bstack1ll111ll1ll_opy_ = bstack1111l1111l_opy_[0]
            driver = bstack1111l111l1_opy_()
            if not driver:
                self.logger.debug(bstack1l1_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᇾ") + str(kwargs) + bstack1l1_opy_ (u"ࠣࠤᇿ"))
                return
            capabilities = f.bstack111l11ll11_opy_(bstack1ll111ll1ll_opy_, bstack111l111ll1_opy_.bstack1ll111l1lll_opy_)
            if not capabilities:
                self.logger.debug(bstack1l1_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡦࡰࡷࡱࡨࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤሀ") + str(kwargs) + bstack1l1_opy_ (u"ࠥࠦሁ"))
                return
            self.accessibility = self.bstack11l1lll1l_opy_(tags) and self.bstack1ll1111ll_opy_(capabilities[bstack1l1_opy_ (u"ࠫࡦࡲࡷࡢࡻࡶࡑࡦࡺࡣࡩࠩሂ")])
        self.logger.debug(bstack1l1_opy_ (u"ࠧࡹࡨࡰࡷ࡯ࡨࠥࡸࡵ࡯ࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡹࡥࡱࡻࡥ࠾ࠤሃ") + str(self.accessibility) + bstack1l1_opy_ (u"ࠨࠢሄ"))
    def bstack1ll11111l1l_opy_(
        self,
        f: bstack111l111ll1_opy_,
        driver: object,
        exec: Tuple[bstack111l1llll1_opy_, str],
        bstack111ll111l1_opy_: Tuple[bstack111ll1ll11_opy_, bstack111ll11111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        bstack11l1l1ll11_opy_ = datetime.now()
        self.bstack1ll111lll11_opy_(f, exec, *args, **kwargs)
        instance, method_name = exec
        instance.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠢࡢ࠳࠴ࡽ࠿࡯࡮ࡪࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡧࡴࡴࡦࡪࡩࠥህ"), datetime.now() - bstack11l1l1ll11_opy_)
        if (
            not f.bstack1ll11l1l1l1_opy_(method_name)
            or f.bstack1ll111l1ll1_opy_(method_name, *args)
            or f.bstack1ll111ll11l_opy_(method_name, *args)
        ):
            return
        if not f.bstack111l11ll11_opy_(instance, bstack1ll1l1l111l_opy_.bstack1ll1111l11l_opy_, False):
            if not bstack1ll1l1l111l_opy_.bstack1lll11lll11_opy_:
                self.logger.warning(bstack1l1_opy_ (u"ࠣ࡝ࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࡀࠦሆ") + str(f.platform_index) + bstack1l1_opy_ (u"ࠤࡠࠤࡦ࠷࠱ࡺࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠡࡪࡤࡺࡪࠦ࡮ࡰࡶࠣࡦࡪ࡫࡮ࠡࡵࡨࡸࠥ࡬࡯ࡳࠢࡷ࡬࡮ࡹࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣሇ"))
                bstack1ll1l1l111l_opy_.bstack1lll11lll11_opy_ = True
            return
        bstack1ll1111l1ll_opy_ = self.scripts.get(f.framework_name, {})
        if not bstack1ll1111l1ll_opy_:
            platform_index = f.bstack111l11ll11_opy_(instance, bstack111l111ll1_opy_.bstack111l111l11_opy_, 0)
            self.logger.debug(bstack1l1_opy_ (u"ࠥࡲࡴࠦࡡ࠲࠳ࡼࠤࡸࡩࡲࡪࡲࡷࡷࠥ࡬࡯ࡳࠢࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࡀࡿࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࢂࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣለ") + str(f.framework_name) + bstack1l1_opy_ (u"ࠦࠧሉ"))
            return
        bstack1lll11lllll_opy_ = f.bstack1lll1l11l1l_opy_(*args)
        if not bstack1lll11lllll_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠧࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡣࡰ࡯ࡰࡥࡳࡪ࡟࡯ࡣࡰࡩࠥ࡬࡯ࡳࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࡃࠢሊ") + str(method_name) + bstack1l1_opy_ (u"ࠨࠢላ"))
            return
        bstack1ll11111ll1_opy_ = f.bstack111l11ll11_opy_(instance, bstack1ll1l1l111l_opy_.bstack1ll1111ll11_opy_, False)
        if bstack1lll11lllll_opy_ == bstack1l1_opy_ (u"ࠢࡨࡧࡷࠦሌ") and not bstack1ll11111ll1_opy_:
            f.bstack111l1ll11l_opy_(instance, bstack1ll1l1l111l_opy_.bstack1ll1111ll11_opy_, True)
        if not bstack1ll11111ll1_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠣࡰࡲࠤ࡚ࡘࡌࠡ࡮ࡲࡥࡩ࡫ࡤࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪ࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠࡤࡱࡰࡱࡦࡴࡤࡠࡰࡤࡱࡪࡃࠢል") + str(bstack1lll11lllll_opy_) + bstack1l1_opy_ (u"ࠤࠥሎ"))
            return
        scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(bstack1lll11lllll_opy_, [])
        if not scripts_to_run:
            self.logger.debug(bstack1l1_opy_ (u"ࠥࡲࡴࠦࡡ࠲࠳ࡼࠤࡸࡩࡲࡪࡲࡷࡷࠥ࡬࡯ࡳࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡࡥࡲࡱࡲࡧ࡮ࡥࡡࡱࡥࡲ࡫࠽ࠣሏ") + str(bstack1lll11lllll_opy_) + bstack1l1_opy_ (u"ࠦࠧሐ"))
            return
        self.logger.info(bstack1l1_opy_ (u"ࠧࡸࡵ࡯ࡰ࡬ࡲ࡬ࠦࡻ࡭ࡧࡱࠬࡸࡩࡲࡪࡲࡷࡷࡤࡺ࡯ࡠࡴࡸࡲ࠮ࢃࠠࡴࡥࡵ࡭ࡵࡺࡳࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪ࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠࡤࡱࡰࡱࡦࡴࡤࡠࡰࡤࡱࡪࡃࠢሑ") + str(bstack1lll11lllll_opy_) + bstack1l1_opy_ (u"ࠨࠢሒ"))
        scripts = [(s, bstack1ll1111l1ll_opy_[s]) for s in scripts_to_run if s in bstack1ll1111l1ll_opy_]
        for bstack1ll111l111l_opy_, bstack1ll111l1l1l_opy_ in scripts:
            try:
                bstack11l1l1ll11_opy_ = datetime.now()
                if bstack1ll111l111l_opy_ == bstack1l1_opy_ (u"ࠢࡴࡥࡤࡲࠧሓ"):
                    result = self.perform_scan(driver, method=bstack1lll11lllll_opy_, framework_name=f.framework_name)
                instance.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠣࡣ࠴࠵ࡾࡀࠢሔ") + bstack1ll111l111l_opy_, datetime.now() - bstack11l1l1ll11_opy_)
                if isinstance(result, dict) and not result.get(bstack1l1_opy_ (u"ࠤࡶࡹࡨࡩࡥࡴࡵࠥሕ"), True):
                    self.logger.warning(bstack1l1_opy_ (u"ࠥࡷࡰ࡯ࡰࠡࡧࡻࡩࡨࡻࡴࡪࡰࡪࠤࡷ࡫࡭ࡢ࡫ࡱ࡭ࡳ࡭ࠠࡴࡥࡵ࡭ࡵࡺࡳ࠻ࠢࠥሖ") + str(result) + bstack1l1_opy_ (u"ࠦࠧሗ"))
                    break
            except Exception as e:
                self.logger.error(bstack1l1_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠤࡪࡾࡥࡤࡷࡷ࡭ࡳ࡭ࠠࡴࡥࡵ࡭ࡵࡺ࠽ࡼࡵࡦࡶ࡮ࡶࡴࡠࡰࡤࡱࡪࢃࠠࡦࡴࡵࡳࡷࡃࠢመ") + str(e) + bstack1l1_opy_ (u"ࠨࠢሙ"))
    def bstack1111l111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1111ll1l11_opy_,
        bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_],
        *args,
        **kwargs,
    ):
        if not self.accessibility:
            self.logger.debug(bstack1l1_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡣ࠴࠵ࡾࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠦሚ"))
            return
        bstack1111l1111l_opy_ = f.bstack111l11ll11_opy_(instance, bstack1111ll1111_opy_.bstack1111l1llll_opy_, [])
        if not bstack1111l1111l_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥማ") + str(kwargs) + bstack1l1_opy_ (u"ࠤࠥሜ"))
            return
        if len(bstack1111l1111l_opy_) > 1:
            self.logger.debug(bstack1l1_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧም") + str(kwargs) + bstack1l1_opy_ (u"ࠦࠧሞ"))
        bstack1111l111l1_opy_, bstack1ll111ll1ll_opy_ = bstack1111l1111l_opy_[0]
        driver = bstack1111l111l1_opy_()
        if not driver:
            self.logger.debug(bstack1l1_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨሟ") + str(kwargs) + bstack1l1_opy_ (u"ࠨࠢሠ"))
            return
        test_name = f.bstack111l11ll11_opy_(instance, TestFramework.bstack1lllll1l111_opy_)
        if not test_name:
            self.logger.debug(bstack1l1_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡷࡩࡸࡺࠠ࡯ࡣࡰࡩࠧሡ"))
            return
        test_uuid = f.bstack111l11ll11_opy_(instance, TestFramework.bstack1llll1ll1ll_opy_)
        if not test_uuid:
            self.logger.debug(bstack1l1_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡷࡸ࡭ࡩࠨሢ"))
            return
        return self.bstack11l11l11_opy_(driver, test_name, bstack1ll111ll1ll_opy_.framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        if not self.accessibility:
            self.logger.debug(bstack1l1_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮࠻ࠢࡤ࠵࠶ࡿࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࠥሣ"))
            return
        bstack11l1l1ll11_opy_ = datetime.now()
        bstack1ll111l1l1l_opy_ = self.scripts.get(framework_name, {}).get(bstack1l1_opy_ (u"ࠥࡷࡨࡧ࡮ࠣሤ"), None)
        if not bstack1ll111l1l1l_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠦࡵ࡫ࡲࡧࡱࡵࡱࡤࡹࡣࡢࡰ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࠭ࡳࡤࡣࡱࠫࠥࡹࡣࡳ࡫ࡳࡸࠥ࡬࡯ࡳࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࠦሥ") + str(framework_name) + bstack1l1_opy_ (u"ࠧࠦࠢሦ"))
            return
        instance = bstack11111ll111_opy_.bstack1llllllll1l_opy_(driver)
        if instance:
            if not bstack11111ll111_opy_.bstack111l11ll11_opy_(instance, bstack1ll1l1l111l_opy_.bstack1ll1111l111_opy_, False):
                bstack11111ll111_opy_.bstack111l1ll11l_opy_(instance, bstack1ll1l1l111l_opy_.bstack1ll1111l111_opy_, True)
            else:
                self.logger.info(bstack1l1_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲ࠿ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡪࡰࠣࡴࡷࡵࡧࡳࡧࡶࡷࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࡰࡩࡹ࡮࡯ࡥ࠿ࠥሧ") + str(method) + bstack1l1_opy_ (u"ࠢࠣረ"))
                return
        self.logger.info(bstack1l1_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡳࡥࡵࡪࡲࡨࡂࠨሩ") + str(method) + bstack1l1_opy_ (u"ࠤࠥሪ"))
        result = driver.execute_async_script(bstack1ll111l1l1l_opy_, {bstack1l1_opy_ (u"ࠥࡱࡪࡺࡨࡰࡦࠥራ"): method if method else bstack1l1_opy_ (u"ࠦࠧሬ")})
        if instance:
            bstack11111ll111_opy_.bstack111l1ll11l_opy_(instance, bstack1ll1l1l111l_opy_.bstack1ll1111l111_opy_, False)
            instance.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠧࡧ࠱࠲ࡻ࠽ࡴࡪࡸࡦࡰࡴࡰࡣࡸࡩࡡ࡯ࠤር"), datetime.now() - bstack11l1l1ll11_opy_)
        return result
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1l1_opy_ (u"ࠨࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡶࡪࡹࡵ࡭ࡶࡶ࠾ࠥࡧ࠱࠲ࡻࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠣሮ"))
            return
        bstack1ll111l1l1l_opy_ = self.scripts.get(framework_name, {}).get(bstack1l1_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠦሯ"), None)
        if not bstack1ll111l1l1l_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠣ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠧࠡࡵࡦࡶ࡮ࡶࡴࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢሰ") + str(framework_name) + bstack1l1_opy_ (u"ࠤࠥሱ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack11l1l1ll11_opy_ = datetime.now()
        result = driver.execute_async_script(bstack1ll111l1l1l_opy_)
        instance = bstack11111ll111_opy_.bstack1llllllll1l_opy_(driver)
        if instance:
            instance.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠥࡥ࠶࠷ࡹ࠻ࡩࡨࡸࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡸࡥࡴࡷ࡯ࡸࡸࠨሲ"), datetime.now() - bstack11l1l1ll11_opy_)
        return result
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1l1_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࡴࡡࡶࡹࡲࡳࡡࡳࡻ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠢሳ"))
            return
        bstack1ll111l1l1l_opy_ = self.scripts.get(framework_name, {}).get(bstack1l1_opy_ (u"ࠧ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࡕࡸࡱࡲࡧࡲࡺࠤሴ"), None)
        if not bstack1ll111l1l1l_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠨ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠬࠦࡳࡤࡴ࡬ࡴࡹࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࠧስ") + str(framework_name) + bstack1l1_opy_ (u"ࠢࠣሶ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack11l1l1ll11_opy_ = datetime.now()
        result = driver.execute_async_script(bstack1ll111l1l1l_opy_)
        instance = bstack11111ll111_opy_.bstack1llllllll1l_opy_(driver)
        if instance:
            instance.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠣࡣ࠴࠵ࡾࡀࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡶࡪࡹࡵ࡭ࡶࡶࡣࡸࡻ࡭࡮ࡣࡵࡽࠧሷ"), datetime.now() - bstack11l1l1ll11_opy_)
        return result
    def bstack1ll111l11ll_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack111l1lllll_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack111ll1l11l_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack1l1_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦሸ") + str(r) + bstack1l1_opy_ (u"ࠥࠦሹ"))
            else:
                self.bstack1ll111l11l1_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤሺ") + str(e) + bstack1l1_opy_ (u"ࠧࠨሻ"))
            traceback.print_exc()
            raise e
    def bstack1ll111l11l1_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack1l1_opy_ (u"ࠨ࡬ࡰࡣࡧࡣࡨࡵ࡮ࡧ࡫ࡪ࠾ࠥࡧ࠱࠲ࡻࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩࠨሼ"))
            return False
        if result.accessibility.options:
            options = result.accessibility.options
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1ll1111lll1_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1ll111l1l11_opy_ and command.module == self.bstack1ll1111llll_opy_:
                        if command.method and not command.method in bstack1ll1111lll1_opy_:
                            bstack1ll1111lll1_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1ll1111lll1_opy_[command.method]:
                            bstack1ll1111lll1_opy_[command.method][command.name] = list()
                        bstack1ll1111lll1_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1ll1111lll1_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1ll111lll11_opy_(
        self,
        f: bstack111l111ll1_opy_,
        exec: Tuple[bstack111l1llll1_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if bstack11111ll111_opy_.bstack111lll1l1l_opy_(instance, bstack1ll1l1l111l_opy_.bstack1ll1111l11l_opy_):
            return
        if not f.bstack1111lllll1_opy_(instance):
            if not bstack1ll1l1l111l_opy_.bstack1lll11lll11_opy_:
                self.logger.warning(bstack1l1_opy_ (u"ࠢࡢ࠳࠴ࡽࠥ࡬࡬ࡰࡹࠣࡨ࡮ࡹࡡࡣ࡮ࡨࡨࠥ࡬࡯ࡳࠢࡱࡳࡳ࠳ࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥ࡯࡮ࡧࡴࡤࠦሽ"))
                bstack1ll1l1l111l_opy_.bstack1lll11lll11_opy_ = True
            return
        if f.bstack111l1lll11_opy_(method_name, *args):
            bstack1ll111lll1l_opy_ = False
            desired_capabilities = f.bstack1ll111111ll_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1ll1111ll1l_opy_(instance)
                platform_index = f.bstack111l11ll11_opy_(instance, bstack111l111ll1_opy_.bstack111l111l11_opy_, 0)
                bstack1ll11111lll_opy_ = datetime.now()
                r = self.bstack1ll111l11ll_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠣࡩࡵࡴࡨࡀࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡣࡰࡰࡩ࡭࡬ࠨሾ"), datetime.now() - bstack1ll11111lll_opy_)
                bstack1ll111lll1l_opy_ = r.success
            else:
                self.logger.error(bstack1l1_opy_ (u"ࠤࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡨࡪࡹࡩࡳࡧࡧࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࡀࠦሿ") + str(desired_capabilities) + bstack1l1_opy_ (u"ࠥࠦቀ"))
            f.bstack111l1ll11l_opy_(instance, bstack1ll1l1l111l_opy_.bstack1ll1111l11l_opy_, bstack1ll111lll1l_opy_)
    def bstack11l1lll1l_opy_(self, test_tags):
        bstack1ll111l11ll_opy_ = self.config.get(bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫቁ"))
        if not bstack1ll111l11ll_opy_:
            return True
        try:
            include_tags = bstack1ll111l11ll_opy_[bstack1l1_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪቂ")] if bstack1l1_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫቃ") in bstack1ll111l11ll_opy_ and isinstance(bstack1ll111l11ll_opy_[bstack1l1_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬቄ")], list) else []
            exclude_tags = bstack1ll111l11ll_opy_[bstack1l1_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ቅ")] if bstack1l1_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧቆ") in bstack1ll111l11ll_opy_ and isinstance(bstack1ll111l11ll_opy_[bstack1l1_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨቇ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack1l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡹࡥࡱ࡯ࡤࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡣࡱࡲ࡮ࡴࡧ࠯ࠢࡈࡶࡷࡵࡲࠡ࠼ࠣࠦቈ") + str(error))
        return False
    def bstack1ll1111ll_opy_(self, caps):
        try:
            bstack1ll111l1111_opy_ = caps.get(bstack1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭቉"), {}).get(bstack1l1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪቊ"), caps.get(bstack1l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧቋ"), bstack1l1_opy_ (u"ࠨࠩቌ")))
            if bstack1ll111l1111_opy_:
                self.logger.warning(bstack1l1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡇࡩࡸࡱࡴࡰࡲࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨቍ"))
                return False
            browser = caps.get(bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ቎"), bstack1l1_opy_ (u"ࠫࠬ቏")).lower()
            if browser != bstack1l1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬቐ"):
                self.logger.warning(bstack1l1_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࡳ࠯ࠤቑ"))
                return False
            browser_version = caps.get(bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨቒ"))
            if browser_version and browser_version != bstack1l1_opy_ (u"ࠨ࡮ࡤࡸࡪࡹࡴࠨቓ") and int(browser_version.split(bstack1l1_opy_ (u"ࠩ࠱ࠫቔ"))[0]) <= 98:
                self.logger.warning(bstack1l1_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥ࡭ࡲࡦࡣࡷࡩࡷࠦࡴࡩࡣࡱࠤ࠾࠾࠮ࠣቕ"))
                return False
            bstack1ll11111l11_opy_ = caps.get(bstack1l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬቖ"), {}).get(bstack1l1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ቗"))
            if bstack1ll11111l11_opy_ and bstack1l1_opy_ (u"࠭࠭࠮ࡪࡨࡥࡩࡲࡥࡴࡵࠪቘ") in bstack1ll11111l11_opy_.get(bstack1l1_opy_ (u"ࠧࡢࡴࡪࡷࠬ቙"), []):
                self.logger.warning(bstack1l1_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡲࡴࡺࠠࡳࡷࡱࠤࡴࡴࠠ࡭ࡧࡪࡥࡨࡿࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠡࡕࡺ࡭ࡹࡩࡨࠡࡶࡲࠤࡳ࡫ࡷࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥࠡࡱࡵࠤࡦࡼ࡯ࡪࡦࠣࡹࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠥቚ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack1l1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡸࡤࡰ࡮ࡪࡡࡵࡧࠣࡥ࠶࠷ࡹࠡࡵࡸࡴࡵࡵࡲࡵࠢ࠽ࠦቛ") + str(error))
            return False
    def bstack11l11l11_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        try:
            bstack1ll1111l1l1_opy_ = {
                bstack1l1_opy_ (u"ࠪࡸ࡭࡚ࡥࡴࡶࡕࡹࡳ࡛ࡵࡪࡦࠪቜ"): test_uuid,
                bstack1l1_opy_ (u"ࠫࡹ࡮ࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩቝ"): os.environ.get(bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ቞"), bstack1l1_opy_ (u"࠭ࠧ቟")),
                bstack1l1_opy_ (u"ࠧࡵࡪࡍࡻࡹ࡚࡯࡬ࡧࡱࠫበ"): os.environ.get(bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬቡ"), bstack1l1_opy_ (u"ࠩࠪቢ"))
            }
            self.logger.debug(bstack1l1_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥࡹࡡࡷ࡫ࡱ࡫ࠥࡸࡥࡴࡷ࡯ࡸࡸ࠭ባ") + str(bstack1ll1111l1l1_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            bstack1ll111l1l1l_opy_ = self.scripts.get(framework_name, {}).get(bstack1l1_opy_ (u"ࠦࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠤቤ"), None)
            if not bstack1ll111l1l1l_opy_:
                self.logger.debug(bstack1l1_opy_ (u"ࠧࡶࡥࡳࡨࡲࡶࡲࡥࡳࡤࡣࡱ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࠧࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷࠬࠦࡳࡤࡴ࡬ࡴࡹࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࠧብ") + str(framework_name) + bstack1l1_opy_ (u"ࠨࠠࠣቦ"))
                return
            self.logger.debug(driver.execute_async_script(bstack1ll111l1l1l_opy_, bstack1ll1111l1l1_opy_))
            self.logger.info(bstack1l1_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠥቧ"))
        except Exception as bstack1ll111ll1l1_opy_:
            self.logger.error(bstack1l1_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡦࡳࡺࡲࡤࠡࡰࡲࡸࠥࡨࡥࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥ࠻ࠢࠥቨ") + bstack1l1_opy_ (u"ࠤࡶࡸࡷ࠮ࡰࡢࡶ࡫࠭ࠧቩ") + bstack1l1_opy_ (u"ࠥࠤࡊࡸࡲࡰࡴࠣ࠾ࠧቪ") + str(bstack1ll111ll1l1_opy_))
    def _1ll111ll111_opy_(self, instance: bstack1111ll1l11_opy_, args: Tuple) -> list:
        bstack1l1_opy_ (u"ࠦࠧࠨࡅࡹࡶࡵࡥࡨࡺࠠࡵࡣࡪࡷࠥࡨࡡࡴࡧࡧࠤࡴࡴࠠࡵࡪࡨࠤࡹ࡫ࡳࡵࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯࠳ࠨࠢࠣቫ")
        if bstack1l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩቬ") in instance.bstack1llll1l1l11_opy_:
            return args[2].tags if hasattr(args[2], bstack1l1_opy_ (u"࠭ࡴࡢࡩࡶࠫቭ")) else []
        if hasattr(args[0], bstack1l1_opy_ (u"ࠧࡰࡹࡱࡣࡲࡧࡲ࡬ࡧࡵࡷࠬቮ")):
            return [marker.name for marker in args[0].own_markers]
        return []