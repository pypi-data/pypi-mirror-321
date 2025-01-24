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
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack111l1ll1ll_opy_ import bstack111ll1l111_opy_
from browserstack_sdk.sdk_cli.bstack111l11l1l1_opy_ import (
    bstack111ll1ll11_opy_,
    bstack111ll11111_opy_,
    bstack111l1llll1_opy_,
)
from bstack_utils.helper import  bstack1l1111ll_opy_
from browserstack_sdk.sdk_cli.bstack111l111l1l_opy_ import bstack111l111ll1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1111l11l1l_opy_, bstack1111ll1l11_opy_, bstack1111l11l11_opy_, bstack1lll1ll111l_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack1l111l1lll_opy_ import bstack1l11l1l1l_opy_
from browserstack_sdk.sdk_cli.bstack1111l11lll_opy_ import bstack1111ll1111_opy_
from bstack_utils.percy import bstack11ll1lll11_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1lll111111l_opy_(bstack111ll1l111_opy_):
    def __init__(self, bstack1l1lll1l111_opy_: Dict[str, str]):
        super().__init__()
        self.bstack1l1lll1l111_opy_ = bstack1l1lll1l111_opy_
        self.percy = bstack11ll1lll11_opy_()
        self.bstack1l1l11llll_opy_ = bstack1l11l1l1l_opy_()
        self.bstack1l1lll1llll_opy_()
        bstack111l111ll1_opy_.bstack111l1ll111_opy_((bstack111ll1ll11_opy_.bstack111ll1l1l1_opy_, bstack111ll11111_opy_.PRE), self.bstack1l1lll1lll1_opy_)
        TestFramework.bstack111l1ll111_opy_((bstack1111l11l1l_opy_.TEST, bstack1111l11l11_opy_.POST), self.bstack1111l111ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1ll11l11ll1_opy_(self, instance: bstack111l1llll1_opy_, driver: object):
        bstack1ll11ll1111_opy_ = TestFramework.bstack1ll1l111l1l_opy_(instance.context)
        for t in bstack1ll11ll1111_opy_:
            bstack1111l1111l_opy_ = TestFramework.bstack111l11ll11_opy_(t, bstack1111ll1111_opy_.bstack1111l1llll_opy_, [])
            if any(instance is d[1] for d in bstack1111l1111l_opy_) or instance == driver:
                return t
    def bstack1l1lll1lll1_opy_(
        self,
        f: bstack111l111ll1_opy_,
        driver: object,
        exec: Tuple[bstack111l1llll1_opy_, str],
        bstack111ll111l1_opy_: Tuple[bstack111ll1ll11_opy_, bstack111ll11111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack111l111ll1_opy_.bstack1ll11l1l1l1_opy_(method_name):
                return
            platform_index = f.bstack111l11ll11_opy_(instance, bstack111l111ll1_opy_.bstack111l111l11_opy_, 0)
            bstack1ll11llll11_opy_ = self.bstack1ll11l11ll1_opy_(instance, driver)
            bstack1l1lll1ll1l_opy_ = TestFramework.bstack111l11ll11_opy_(bstack1ll11llll11_opy_, TestFramework.bstack1llllll1l11_opy_, None)
            if not bstack1l1lll1ll1l_opy_:
                self.logger.debug(bstack1l1_opy_ (u"ࠧࡵ࡮ࡠࡲࡵࡩࡤ࡫ࡸࡦࡥࡸࡸࡪࡀࠠࡳࡧࡷࡹࡷࡴࡩ࡯ࡩࠣࡥࡸࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡪࡵࠣࡲࡴࡺࠠࡺࡧࡷࠤࡸࡺࡡࡳࡶࡨࡨࠧኲ"))
                return
            driver_command = f.bstack1lll1l11l1l_opy_(*args)
            for command in bstack1lll111l1_opy_:
                if command == driver_command:
                    self.bstack1lll1l11ll_opy_(driver, platform_index)
            bstack1ll1111ll1_opy_ = self.percy.bstack1lll11l11_opy_()
            if driver_command in bstack1l1ll111ll_opy_[bstack1ll1111ll1_opy_]:
                self.bstack1l1l11llll_opy_.bstack1l11lll1l_opy_(bstack1l1lll1ll1l_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack1l1_opy_ (u"ࠨ࡯࡯ࡡࡳࡶࡪࡥࡥࡹࡧࡦࡹࡹ࡫࠺ࠡࡧࡵࡶࡴࡸࠢኳ"), e)
    def bstack1111l111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1111ll1l11_opy_,
        bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_],
        *args,
        **kwargs,
    ):
        bstack1111l1111l_opy_ = f.bstack111l11ll11_opy_(instance, bstack1111ll1111_opy_.bstack1111l1llll_opy_, [])
        if not bstack1111l1111l_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤኴ") + str(kwargs) + bstack1l1_opy_ (u"ࠣࠤኵ"))
            return
        if len(bstack1111l1111l_opy_) > 1:
            self.logger.debug(bstack1l1_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦ኶") + str(kwargs) + bstack1l1_opy_ (u"ࠥࠦ኷"))
        bstack1111l111l1_opy_, bstack1ll111ll1ll_opy_ = bstack1111l1111l_opy_[0]
        driver = bstack1111l111l1_opy_()
        if not driver:
            self.logger.debug(bstack1l1_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧኸ") + str(kwargs) + bstack1l1_opy_ (u"ࠧࠨኹ"))
            return
        bstack1l1lll1l1l1_opy_ = {
            TestFramework.bstack1lllll1l111_opy_: bstack1l1_opy_ (u"ࠨࡴࡦࡵࡷࠤࡳࡧ࡭ࡦࠤኺ"),
            TestFramework.bstack1llll1ll1ll_opy_: bstack1l1_opy_ (u"ࠢࡵࡧࡶࡸࠥࡻࡵࡪࡦࠥኻ"),
            TestFramework.bstack1llllll1l11_opy_: bstack1l1_opy_ (u"ࠣࡶࡨࡷࡹࠦࡲࡦࡴࡸࡲࠥࡴࡡ࡮ࡧࠥኼ")
        }
        bstack1l1lll1l1ll_opy_ = { key: f.bstack111l11ll11_opy_(instance, key) for key in bstack1l1lll1l1l1_opy_ }
        bstack1l1lll1ll11_opy_ = [key for key, value in bstack1l1lll1l1ll_opy_.items() if not value]
        if bstack1l1lll1ll11_opy_:
            for key in bstack1l1lll1ll11_opy_:
                self.logger.debug(bstack1l1_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࠧኽ") + str(key) + bstack1l1_opy_ (u"ࠥࠦኾ"))
            return
        platform_index = f.bstack111l11ll11_opy_(instance, bstack111l111ll1_opy_.bstack111l111l11_opy_, 0)
        if self.bstack1l1lll1l111_opy_.percy_capture_mode == bstack1l1_opy_ (u"ࠦࡹ࡫ࡳࡵࡥࡤࡷࡪࠨ኿"):
            bstack111l111l1_opy_ = bstack1l1lll1l1ll_opy_.get(TestFramework.bstack1llllll1l11_opy_) + bstack1l1_opy_ (u"ࠧ࠳ࡴࡦࡵࡷࡧࡦࡹࡥࠣዀ")
            PercySDK.screenshot(
                driver,
                bstack111l111l1_opy_,
                bstack1ll11ll1l1_opy_=bstack1l1lll1l1ll_opy_[TestFramework.bstack1lllll1l111_opy_],
                bstack1llll1111l_opy_=bstack1l1lll1l1ll_opy_[TestFramework.bstack1llll1ll1ll_opy_],
                bstack1l1l11l1l_opy_=platform_index
            )
    def bstack1lll1l11ll_opy_(self, driver, platform_index):
        if self.bstack1l1l11llll_opy_.bstack11ll1l111l_opy_() is True or self.bstack1l1l11llll_opy_.capturing() is True:
            return
        self.bstack1l1l11llll_opy_.bstack11llll11ll_opy_()
        while not self.bstack1l1l11llll_opy_.bstack11ll1l111l_opy_():
            bstack1l1lll1ll1l_opy_ = self.bstack1l1l11llll_opy_.bstack1ll111l11_opy_()
            self.bstack11l1111l11_opy_(driver, bstack1l1lll1ll1l_opy_, platform_index)
        self.bstack1l1l11llll_opy_.bstack1l11111l11_opy_()
    def bstack11l1111l11_opy_(self, driver, bstack11ll11l11l_opy_, platform_index, test=None):
        if test != None:
            bstack1ll11ll1l1_opy_ = getattr(test, bstack1l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ዁"), None)
            bstack1llll1111l_opy_ = getattr(test, bstack1l1_opy_ (u"ࠧࡶࡷ࡬ࡨࠬዂ"), None)
            PercySDK.screenshot(driver, bstack11ll11l11l_opy_, bstack1ll11ll1l1_opy_=bstack1ll11ll1l1_opy_, bstack1llll1111l_opy_=bstack1llll1111l_opy_, bstack1l1l11l1l_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack11ll11l11l_opy_)
    def bstack1l1lll1llll_opy_(self):
        os.environ[bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞࠭ዃ")] = str(self.bstack1l1lll1l111_opy_.success)
        os.environ[bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟࡟ࡄࡃࡓࡘ࡚ࡘࡅࡠࡏࡒࡈࡊ࠭ዄ")] = str(self.bstack1l1lll1l111_opy_.percy_capture_mode)
        self.percy.bstack1l1lll1l11l_opy_(self.bstack1l1lll1l111_opy_.is_percy_auto_enabled)
        self.percy.bstack1l1lll11lll_opy_(self.bstack1l1lll1l111_opy_.percy_build_id)