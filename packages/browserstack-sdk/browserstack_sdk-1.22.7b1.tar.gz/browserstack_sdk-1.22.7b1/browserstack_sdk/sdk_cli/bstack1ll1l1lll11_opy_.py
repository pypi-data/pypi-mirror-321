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
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack11111l1l11_opy_ import bstack111111llll_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1111l11l1l_opy_,
    bstack1111ll1l11_opy_,
    bstack1111l11l11_opy_,
    bstack1lllll1ll1l_opy_,
    bstack1lll1ll111l_opy_,
)
import traceback
class bstack1ll1lll11l1_opy_(TestFramework):
    bstack1llll111lll_opy_ = bstack1l1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠣዻ")
    bstack1lllllll1l1_opy_ = bstack1l1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪࠢዼ")
    bstack1llll11llll_opy_ = bstack1l1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࠤዽ")
    bstack1lllll11111_opy_ = bstack1l1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟࡭ࡣࡶࡸࡤࡹࡴࡢࡴࡷࡩࡩࠨዾ")
    bstack1llllll1l1l_opy_ = bstack1l1_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠ࡮ࡤࡷࡹࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤࠣዿ")
    bstack1llll11ll11_opy_: bool
    bstack1lllll1l1l1_opy_ = [
        bstack1111l11l1l_opy_.BEFORE_ALL,
        bstack1111l11l1l_opy_.AFTER_ALL,
        bstack1111l11l1l_opy_.BEFORE_EACH,
        bstack1111l11l1l_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1lll1llllll_opy_: Dict[str, str],
        bstack1llll1l1l11_opy_: List[str]=[bstack1l1_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨጀ")],
    ):
        super().__init__(bstack1llll1l1l11_opy_, bstack1lll1llllll_opy_)
        self.bstack1llll11ll11_opy_ = any(bstack1l1_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢጁ") in item.lower() for item in bstack1llll1l1l11_opy_)
    def track_event(
        self,
        context: bstack1lllll1ll1l_opy_,
        test_framework_state: bstack1111l11l1l_opy_,
        test_hook_state: bstack1111l11l11_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1111l11l1l_opy_.NONE:
            self.logger.warning(bstack1l1_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡥࡥࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࠤࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂࠦࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥ࠾ࠤጂ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠤࠥጃ"))
            return
        if not self.bstack1llll11ll11_opy_:
            self.logger.warning(bstack1l1_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲࡸࡻࡰࡱࡱࡵࡸࡪࡪࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡀࠦጄ") + str(str(self.bstack1llll1l1l11_opy_)) + bstack1l1_opy_ (u"ࠦࠧጅ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1l1_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢጆ") + str(kwargs) + bstack1l1_opy_ (u"ࠨࠢጇ"))
            return
        instance = self.__1llll1l11ll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1l1_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡢࡴࡪࡷࡂࠨገ") + str(args) + bstack1l1_opy_ (u"ࠣࠤጉ"))
            return
        try:
            if not TestFramework.bstack111lll1l1l_opy_(instance, TestFramework.bstack1llll1ll11l_opy_) and test_hook_state == bstack1111l11l11_opy_.PRE:
                test = bstack1ll1lll11l1_opy_.__1lll1ll11ll_opy_(args[0])
                if test:
                    instance.data.update(test)
                    self.logger.debug(bstack1l1_opy_ (u"ࠤ࡯ࡳࡦࡪࡥࡥࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤጊ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠥࠦጋ"))
            if test_framework_state == bstack1111l11l1l_opy_.TEST:
                if test_hook_state == bstack1111l11l11_opy_.PRE and not TestFramework.bstack111lll1l1l_opy_(instance, TestFramework.bstack1111111111_opy_):
                    TestFramework.bstack111l1ll11l_opy_(instance, TestFramework.bstack1111111111_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1l1_opy_ (u"ࠦࡸ࡫ࡴࠡࡶࡨࡷࡹ࠳ࡳࡵࡣࡵࡸࠥ࡬࡯ࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤጌ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠧࠨግ"))
                elif test_hook_state == bstack1111l11l11_opy_.POST and not TestFramework.bstack111lll1l1l_opy_(instance, TestFramework.bstack1llll1lll1l_opy_):
                    TestFramework.bstack111l1ll11l_opy_(instance, TestFramework.bstack1llll1lll1l_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1l1_opy_ (u"ࠨࡳࡦࡶࠣࡸࡪࡹࡴ࠮ࡧࡱࡨࠥ࡬࡯ࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤጎ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠢࠣጏ"))
            elif test_framework_state == bstack1111l11l1l_opy_.LOG and test_hook_state == bstack1111l11l11_opy_.POST:
                bstack1ll1lll11l1_opy_.__1llll1l1l1l_opy_(instance, *args)
            elif test_framework_state == bstack1111l11l1l_opy_.LOG_REPORT and test_hook_state == bstack1111l11l11_opy_.POST:
                self.__1lllll1ll11_opy_(instance, *args)
            elif test_framework_state in bstack1ll1lll11l1_opy_.bstack1lllll1l1l1_opy_:
                self.__1llllll11ll_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1l1_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤጐ") + str(instance.ref()) + bstack1l1_opy_ (u"ࠤࠥ጑"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1llll1111ll_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
    def bstack1lllllllll1_opy_(self):
        return self.bstack1llll11ll11_opy_
    def __1llll1l111l_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1l1_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡳࡧࡶࡹࡱࡺࠢጒ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1llll1lll11_opy_(rep, [bstack1l1_opy_ (u"ࠦࡼ࡮ࡥ࡯ࠤጓ"), bstack1l1_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨጔ"), bstack1l1_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨጕ"), bstack1l1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ጖"), bstack1l1_opy_ (u"ࠣࡵ࡮࡭ࡵࡶࡥࡥࠤ጗"), bstack1l1_opy_ (u"ࠤ࡯ࡳࡳ࡭ࡲࡦࡲࡵࡸࡪࡾࡴࠣጘ")])
        return None
    def __1lllll1ll11_opy_(self, instance: bstack1111ll1l11_opy_, *args):
        result = self.__1llll1l111l_opy_(*args)
        if not result:
            return
        failure = None
        bstack111llll11l_opy_ = None
        if result.get(bstack1l1_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦጙ"), None) == bstack1l1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦጚ") and len(args) > 1 and getattr(args[1], bstack1l1_opy_ (u"ࠧ࡫ࡸࡤ࡫ࡱࡪࡴࠨጛ"), None) is not None:
            failure = [{bstack1l1_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩጜ"): [args[1].excinfo.exconly(), result.get(bstack1l1_opy_ (u"ࠢ࡭ࡱࡱ࡫ࡷ࡫ࡰࡳࡶࡨࡼࡹࠨጝ"), None)]}]
            bstack111llll11l_opy_ = bstack1l1_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤጞ") if bstack1l1_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧጟ") in getattr(args[1].excinfo, bstack1l1_opy_ (u"ࠥࡸࡾࡶࡥ࡯ࡣࡰࡩࠧጠ"), bstack1l1_opy_ (u"ࠦࠧጡ")) else bstack1l1_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨጢ")
        bstack1llll11lll1_opy_ = result.get(bstack1l1_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢጣ"), TestFramework.bstack1llll11l111_opy_)
        if bstack1llll11lll1_opy_ != TestFramework.bstack1llll11l111_opy_:
            TestFramework.bstack111l1ll11l_opy_(instance, TestFramework.bstack1lll1ll1l1l_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1llll111l11_opy_(instance, {
            TestFramework.bstack1111lll11l_opy_: failure,
            TestFramework.bstack1lll1ll11l1_opy_: bstack111llll11l_opy_,
            TestFramework.bstack1111l1l1ll_opy_: bstack1llll11lll1_opy_,
        })
    def __1llll1l11ll_opy_(
        self,
        context: bstack1lllll1ll1l_opy_,
        test_framework_state: bstack1111l11l1l_opy_,
        test_hook_state: bstack1111l11l11_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1111l11l1l_opy_.SETUP_FIXTURE:
            instance = self.__1llll11l1ll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1llll11l11l_opy_ bstack1llll1l1ll1_opy_ this to be bstack1l1_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢጤ")
            if test_framework_state == bstack1111l11l1l_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1lll1lll1l1_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1111l11l1l_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1l1_opy_ (u"ࠣࡰࡲࡨࡪࠨጥ"), None), bstack1l1_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤጦ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1l1_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥጧ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1llllllll1l_opy_(target) if target else None
        return instance
    def __1llllll11ll_opy_(
        self,
        instance: bstack1111ll1l11_opy_,
        test_framework_state: bstack1111l11l1l_opy_,
        test_hook_state: bstack1111l11l11_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1lllll1lll1_opy_ = TestFramework.bstack111l11ll11_opy_(instance, bstack1ll1lll11l1_opy_.bstack1lllllll1l1_opy_, {})
        if not key in bstack1lllll1lll1_opy_:
            bstack1lllll1lll1_opy_[key] = []
        bstack1lllll1llll_opy_ = TestFramework.bstack111l11ll11_opy_(instance, bstack1ll1lll11l1_opy_.bstack1llll11llll_opy_, {})
        if not key in bstack1lllll1llll_opy_:
            bstack1lllll1llll_opy_[key] = []
        bstack1lll1llll1l_opy_ = {
            bstack1ll1lll11l1_opy_.bstack1lllllll1l1_opy_: bstack1lllll1lll1_opy_,
            bstack1ll1lll11l1_opy_.bstack1llll11llll_opy_: bstack1lllll1llll_opy_,
        }
        if test_hook_state == bstack1111l11l11_opy_.PRE:
            hook = {
                bstack1l1_opy_ (u"ࠦࡰ࡫ࡹࠣጨ"): key,
                TestFramework.bstack1lllllll1ll_opy_: uuid4().__str__(),
                TestFramework.bstack1lll1llll11_opy_: TestFramework.bstack1llllll11l1_opy_,
                TestFramework.bstack11111111l1_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1llllll1ll1_opy_: [],
                TestFramework.bstack1lllll111l1_opy_: args[1] if len(args) > 1 else bstack1l1_opy_ (u"ࠬ࠭ጩ")
            }
            bstack1lllll1lll1_opy_[key].append(hook)
            bstack1lll1llll1l_opy_[bstack1ll1lll11l1_opy_.bstack1lllll11111_opy_] = key
        elif test_hook_state == bstack1111l11l11_opy_.POST:
            bstack1lll1lll111_opy_ = bstack1lllll1lll1_opy_.get(key, [])
            hook = bstack1lll1lll111_opy_.pop() if bstack1lll1lll111_opy_ else None
            if hook:
                result = self.__1llll1l111l_opy_(*args)
                if result:
                    bstack1lllll1l1ll_opy_ = result.get(bstack1l1_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢጪ"), TestFramework.bstack1llllll11l1_opy_)
                    if bstack1lllll1l1ll_opy_ != TestFramework.bstack1llllll11l1_opy_:
                        hook[TestFramework.bstack1lll1llll11_opy_] = bstack1lllll1l1ll_opy_
                hook[TestFramework.bstack1llll1llll1_opy_] = datetime.now(tz=timezone.utc)
                bstack1lllll1llll_opy_[key].append(hook)
                bstack1lll1llll1l_opy_[bstack1ll1lll11l1_opy_.bstack1llllll1l1l_opy_] = key
        TestFramework.bstack1llll111l11_opy_(instance, bstack1lll1llll1l_opy_)
        self.logger.debug(bstack1l1_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡨࡰࡱ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࡻ࡬ࡧࡼࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢ࡫ࡳࡴࡱࡳࡠࡵࡷࡥࡷࡺࡥࡥ࠿ࡾ࡬ࡴࡵ࡫ࡴࡡࡶࡸࡦࡸࡴࡦࡦࢀࠤ࡭ࡵ࡯࡬ࡵࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࡂࠨጫ") + str(bstack1lllll1llll_opy_) + bstack1l1_opy_ (u"ࠣࠤጬ"))
    def __1llll11l1ll_opy_(
        self,
        context: bstack1lllll1ll1l_opy_,
        test_framework_state: bstack1111l11l1l_opy_,
        test_hook_state: bstack1111l11l11_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1llll1lll11_opy_(args[0], [bstack1l1_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣጭ"), bstack1l1_opy_ (u"ࠥࡥࡷ࡭࡮ࡢ࡯ࡨࠦጮ"), bstack1l1_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࡶࠦጯ"), bstack1l1_opy_ (u"ࠧ࡯ࡤࡴࠤጰ"), bstack1l1_opy_ (u"ࠨࡵ࡯࡫ࡷࡸࡪࡹࡴࠣጱ"), bstack1l1_opy_ (u"ࠢࡣࡣࡶࡩ࡮ࡪࠢጲ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scope = request.scope if hasattr(request, bstack1l1_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢጳ")) else fixturedef.get(bstack1l1_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣጴ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1l1_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࠣጵ")) else None
        node = request.node if hasattr(request, bstack1l1_opy_ (u"ࠦࡳࡵࡤࡦࠤጶ")) else None
        target = request.node.nodeid if hasattr(node, bstack1l1_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧጷ")) else None
        baseid = fixturedef.get(bstack1l1_opy_ (u"ࠨࡢࡢࡵࡨ࡭ࡩࠨጸ"), None) or bstack1l1_opy_ (u"ࠢࠣጹ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1l1_opy_ (u"ࠣࡡࡳࡽ࡫ࡻ࡮ࡤ࡫ࡷࡩࡲࠨጺ")):
            target = bstack1ll1lll11l1_opy_.__1llll1l1111_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1l1_opy_ (u"ࠤ࡯ࡳࡨࡧࡴࡪࡱࡱࠦጻ")) else None
            if target and not TestFramework.bstack1llllllll1l_opy_(target):
                self.__1lll1lll1l1_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1l1_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡺࡡࡳࡩࡨࡸࡂࢁࡴࡢࡴࡪࡩࡹࢃࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡴ࡯ࡥࡧࡀࡿࡳࡵࡤࡦࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧጼ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠦࠧጽ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1l1_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫ࡤࡦࡨࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡩ࡫ࡦࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡷࡥࡷ࡭ࡥࡵ࠿ࠥጾ") + str(target) + bstack1l1_opy_ (u"ࠨࠢጿ"))
            return None
        instance = TestFramework.bstack1llllllll1l_opy_(target)
        if not instance:
            self.logger.warning(bstack1l1_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡢࡢࡵࡨ࡭ࡩࡃࡻࡣࡣࡶࡩ࡮ࡪࡽࠡࡶࡤࡶ࡬࡫ࡴ࠾ࠤፀ") + str(target) + bstack1l1_opy_ (u"ࠣࠤፁ"))
            return None
        bstack1llll111ll1_opy_ = TestFramework.bstack111l11ll11_opy_(instance, bstack1ll1lll11l1_opy_.bstack1llll111lll_opy_, {})
        if os.getenv(bstack1l1_opy_ (u"ࠤࡖࡈࡐࡥࡃࡍࡋࡢࡊࡑࡇࡇࡠࡈࡌ࡜࡙࡛ࡒࡆࡕࠥፂ"), bstack1l1_opy_ (u"ࠥ࠵ࠧፃ")) == bstack1l1_opy_ (u"ࠦ࠶ࠨፄ"):
            bstack1llllllllll_opy_ = bstack1l1_opy_ (u"ࠧࡀࠢፅ").join((scope, fixturename))
            bstack1llll1ll111_opy_ = datetime.now(tz=timezone.utc)
            bstack11111111ll_opy_ = {
                bstack1l1_opy_ (u"ࠨ࡫ࡦࡻࠥፆ"): bstack1llllllllll_opy_,
                bstack1l1_opy_ (u"ࠢࡵࡣࡪࡷࠧፇ"): bstack1ll1lll11l1_opy_.__1lll1lllll1_opy_(request.node),
                bstack1l1_opy_ (u"ࠣࡨ࡬ࡼࡹࡻࡲࡦࠤፈ"): fixturedef,
                bstack1l1_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣፉ"): scope,
                bstack1l1_opy_ (u"ࠥࡸࡾࡶࡥࠣፊ"): None,
            }
            try:
                if test_hook_state == bstack1111l11l11_opy_.POST and callable(getattr(args[-1], bstack1l1_opy_ (u"ࠦ࡬࡫ࡴࡠࡴࡨࡷࡺࡲࡴࠣፋ"), None)):
                    bstack11111111ll_opy_[bstack1l1_opy_ (u"ࠧࡺࡹࡱࡧࠥፌ")] = TestFramework.bstack1lllllll111_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1111l11l11_opy_.PRE:
                bstack11111111ll_opy_[bstack1l1_opy_ (u"ࠨࡵࡶ࡫ࡧࠦፍ")] = uuid4().__str__()
                bstack11111111ll_opy_[bstack1ll1lll11l1_opy_.bstack11111111l1_opy_] = bstack1llll1ll111_opy_
            elif test_hook_state == bstack1111l11l11_opy_.POST:
                bstack11111111ll_opy_[bstack1ll1lll11l1_opy_.bstack1llll1llll1_opy_] = bstack1llll1ll111_opy_
            if bstack1llllllllll_opy_ in bstack1llll111ll1_opy_:
                bstack1llll111ll1_opy_[bstack1llllllllll_opy_].update(bstack11111111ll_opy_)
                self.logger.debug(bstack1l1_opy_ (u"ࠢࡶࡲࡧࡥࡹ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࠽ࠣፎ") + str(bstack1llll111ll1_opy_[bstack1llllllllll_opy_]) + bstack1l1_opy_ (u"ࠣࠤፏ"))
            else:
                bstack1llll111ll1_opy_[bstack1llllllllll_opy_] = bstack11111111ll_opy_
                self.logger.debug(bstack1l1_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࠽ࡼࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡽࠡࡶࡵࡥࡨࡱࡥࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࡁࠧፐ") + str(len(bstack1llll111ll1_opy_)) + bstack1l1_opy_ (u"ࠥࠦፑ"))
        TestFramework.bstack111l1ll11l_opy_(instance, bstack1ll1lll11l1_opy_.bstack1llll111lll_opy_, bstack1llll111ll1_opy_)
        self.logger.debug(bstack1l1_opy_ (u"ࠦࡸࡧࡶࡦࡦࠣࡪ࡮ࡾࡴࡶࡴࡨࡷࡂࢁ࡬ࡦࡰࠫࡸࡷࡧࡣ࡬ࡧࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࡸ࠯ࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦፒ") + str(instance.ref()) + bstack1l1_opy_ (u"ࠧࠨፓ"))
        return instance
    def __1lll1lll1l1_opy_(
        self,
        context: bstack1lllll1ll1l_opy_,
        test_framework_state: bstack1111l11l1l_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack111111llll_opy_.create_context(target)
        ob = bstack1111ll1l11_opy_(ctx, self.bstack1llll1l1l11_opy_, self.bstack1lll1llllll_opy_, test_framework_state)
        TestFramework.bstack1llll111l11_opy_(ob, {
            TestFramework.bstack1llllll111l_opy_: context.test_framework_name,
            TestFramework.bstack1lll1l1llll_opy_: context.test_framework_version,
            TestFramework.bstack1lllll11lll_opy_: [],
            bstack1ll1lll11l1_opy_.bstack1llll111lll_opy_: {},
            bstack1ll1lll11l1_opy_.bstack1llll11llll_opy_: {},
            bstack1ll1lll11l1_opy_.bstack1lllllll1l1_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack111l1ll11l_opy_(ob, TestFramework.bstack1llllll1lll_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack111l1ll11l_opy_(ob, TestFramework.bstack111l111l11_opy_, context.platform_index)
        TestFramework.bstack1lllll11ll1_opy_[ctx.id] = ob
        self.logger.debug(bstack1l1_opy_ (u"ࠨࡳࡢࡸࡨࡨࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠠࡤࡶࡻ࠲࡮ࡪ࠽ࡼࡥࡷࡼ࠳࡯ࡤࡾࠢࡷࡥࡷ࡭ࡥࡵ࠿ࡾࡸࡦࡸࡧࡦࡶࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷࡂࠨፔ") + str(TestFramework.bstack1lllll11ll1_opy_.keys()) + bstack1l1_opy_ (u"ࠢࠣፕ"))
        return ob
    def bstack1llll1lllll_opy_(self, instance: bstack1111ll1l11_opy_, bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_]):
        bstack1lllllll11l_opy_ = (
            bstack1ll1lll11l1_opy_.bstack1lllll11111_opy_
            if bstack111ll111l1_opy_[1] == bstack1111l11l11_opy_.PRE
            else bstack1ll1lll11l1_opy_.bstack1llllll1l1l_opy_
        )
        hook = bstack1ll1lll11l1_opy_.bstack1llll1l1lll_opy_(instance, bstack1lllllll11l_opy_)
        entries = hook.get(TestFramework.bstack1llllll1ll1_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.bstack111l11ll11_opy_(instance, TestFramework.bstack1lllll11lll_opy_, []))
        return entries
    def bstack1llll11ll1l_opy_(self, instance: bstack1111ll1l11_opy_, bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_]):
        bstack1lllllll11l_opy_ = (
            bstack1ll1lll11l1_opy_.bstack1lllll11111_opy_
            if bstack111ll111l1_opy_[1] == bstack1111l11l11_opy_.PRE
            else bstack1ll1lll11l1_opy_.bstack1llllll1l1l_opy_
        )
        bstack1ll1lll11l1_opy_.bstack1llll1ll1l1_opy_(instance, bstack1lllllll11l_opy_)
        TestFramework.bstack111l11ll11_opy_(instance, TestFramework.bstack1lllll11lll_opy_, []).clear()
    @staticmethod
    def bstack1llll1l1lll_opy_(instance: bstack1111ll1l11_opy_, bstack1lllllll11l_opy_: str):
        bstack1lllll11l1l_opy_ = (
            bstack1ll1lll11l1_opy_.bstack1llll11llll_opy_
            if bstack1lllllll11l_opy_ == bstack1ll1lll11l1_opy_.bstack1llllll1l1l_opy_
            else bstack1ll1lll11l1_opy_.bstack1lllllll1l1_opy_
        )
        bstack1lll1lll11l_opy_ = TestFramework.bstack111l11ll11_opy_(instance, bstack1lllllll11l_opy_, None)
        bstack1llll1111l1_opy_ = TestFramework.bstack111l11ll11_opy_(instance, bstack1lllll11l1l_opy_, None) if bstack1lll1lll11l_opy_ else None
        return (
            bstack1llll1111l1_opy_[bstack1lll1lll11l_opy_][-1]
            if isinstance(bstack1llll1111l1_opy_, dict) and len(bstack1llll1111l1_opy_.get(bstack1lll1lll11l_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1llll1ll1l1_opy_(instance: bstack1111ll1l11_opy_, bstack1lllllll11l_opy_: str):
        hook = bstack1ll1lll11l1_opy_.bstack1llll1l1lll_opy_(instance, bstack1lllllll11l_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1llllll1ll1_opy_, []).clear()
    @staticmethod
    def __1llll1l1l1l_opy_(instance: bstack1111ll1l11_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1l1_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡤࡱࡵࡨࡸࠨፖ"), None)):
            return
        if os.getenv(bstack1l1_opy_ (u"ࠤࡖࡈࡐࡥࡃࡍࡋࡢࡊࡑࡇࡇࡠࡎࡒࡋࡘࠨፗ"), bstack1l1_opy_ (u"ࠥ࠵ࠧፘ")) != bstack1l1_opy_ (u"ࠦ࠶ࠨፙ"):
            bstack1ll1lll11l1_opy_.logger.warning(bstack1l1_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵ࡭ࡳ࡭ࠠࡤࡣࡳࡰࡴ࡭ࠢፚ"))
            return
        bstack1llllllll11_opy_ = {
            bstack1l1_opy_ (u"ࠨࡳࡦࡶࡸࡴࠧ፛"): (bstack1ll1lll11l1_opy_.bstack1lllll11111_opy_, bstack1ll1lll11l1_opy_.bstack1lllllll1l1_opy_),
            bstack1l1_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤ፜"): (bstack1ll1lll11l1_opy_.bstack1llllll1l1l_opy_, bstack1ll1lll11l1_opy_.bstack1llll11llll_opy_),
        }
        for when in (bstack1l1_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢ፝"), bstack1l1_opy_ (u"ࠤࡦࡥࡱࡲࠢ፞"), bstack1l1_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧ፟")):
            bstack1lll1ll1ll1_opy_ = args[1].get_records(when)
            if not bstack1lll1ll1ll1_opy_:
                continue
            records = [
                bstack1lll1ll111l_opy_(
                    kind=TestFramework.bstack1lllll1111l_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1l1_opy_ (u"ࠦࡱ࡫ࡶࡦ࡮ࡱࡥࡲ࡫ࠢ፠")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1l1_opy_ (u"ࠧࡩࡲࡦࡣࡷࡩࡩࠨ፡")) and r.created
                        else None
                    ),
                )
                for r in bstack1lll1ll1ll1_opy_
                if isinstance(getattr(r, bstack1l1_opy_ (u"ࠨ࡭ࡦࡵࡶࡥ࡬࡫ࠢ።"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1llll111111_opy_, bstack1lllll11l1l_opy_ = bstack1llllllll11_opy_.get(when, (None, None))
            bstack1lllll1l11l_opy_ = TestFramework.bstack111l11ll11_opy_(instance, bstack1llll111111_opy_, None) if bstack1llll111111_opy_ else None
            bstack1llll1111l1_opy_ = TestFramework.bstack111l11ll11_opy_(instance, bstack1lllll11l1l_opy_, None) if bstack1lllll1l11l_opy_ else None
            if isinstance(bstack1llll1111l1_opy_, dict) and len(bstack1llll1111l1_opy_.get(bstack1lllll1l11l_opy_, [])) > 0:
                hook = bstack1llll1111l1_opy_[bstack1lllll1l11l_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1llllll1ll1_opy_ in hook:
                    hook[TestFramework.bstack1llllll1ll1_opy_].extend(records)
                    continue
            logs = TestFramework.bstack111l11ll11_opy_(instance, TestFramework.bstack1lllll11lll_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1lll1ll11ll_opy_(test) -> Dict[str, Any]:
        test_id = bstack1ll1lll11l1_opy_.__1llll1l1111_opy_(test.location) if hasattr(test, bstack1l1_opy_ (u"ࠢ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠤ፣")) else getattr(test, bstack1l1_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣ፤"), None)
        test_name = test.name if hasattr(test, bstack1l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ፥")) else None
        bstack1lll1ll1111_opy_ = test.fspath.strpath if hasattr(test, bstack1l1_opy_ (u"ࠥࡪࡸࡶࡡࡵࡪࠥ፦")) and test.fspath else None
        if not test_id or not test_name or not bstack1lll1ll1111_opy_:
            return None
        code = None
        if hasattr(test, bstack1l1_opy_ (u"ࠦࡴࡨࡪࠣ፧")):
            try:
                import inspect
                code = inspect.getsource(test.obj)
            except:
                pass
        return {
            TestFramework.bstack1llll1ll1ll_opy_: uuid4().__str__(),
            TestFramework.bstack1llll1ll11l_opy_: test_id,
            TestFramework.bstack1lllll1l111_opy_: test_name,
            TestFramework.bstack1llllll1l11_opy_: getattr(test, bstack1l1_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧ፨"), None),
            TestFramework.bstack111111111l_opy_: bstack1lll1ll1111_opy_,
            TestFramework.bstack1lll1ll1l11_opy_: bstack1ll1lll11l1_opy_.__1lll1lllll1_opy_(test),
            TestFramework.bstack1lll1l1lll1_opy_: code,
            TestFramework.bstack1111l1l1ll_opy_: TestFramework.bstack1llll11l111_opy_,
            TestFramework.bstack1111l1l1l1_opy_: test_id
        }
    @staticmethod
    def __1lll1lllll1_opy_(test) -> List[str]:
        return (
            [getattr(f, bstack1l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ፩"), None) for f in test.own_markers if getattr(f, bstack1l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ፪"), None)]
            if isinstance(getattr(test, bstack1l1_opy_ (u"ࠣࡱࡺࡲࡤࡳࡡࡳ࡭ࡨࡶࡸࠨ፫"), None), list)
            else []
        )
    @staticmethod
    def __1llll1l1111_opy_(location):
        return bstack1l1_opy_ (u"ࠤ࠽࠾ࠧ፬").join(filter(lambda x: isinstance(x, str), location))