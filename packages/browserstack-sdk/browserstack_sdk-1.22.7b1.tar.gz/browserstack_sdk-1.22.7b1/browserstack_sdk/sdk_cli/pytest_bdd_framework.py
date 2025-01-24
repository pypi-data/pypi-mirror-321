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
from pyexpat import features
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
class PytestBDDFramework(TestFramework):
    bstack1llll111lll_opy_ = bstack1l1_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨအ")
    bstack1lllllll1l1_opy_ = bstack1l1_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࠧဢ")
    bstack1llll11llll_opy_ = bstack1l1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢဣ")
    bstack1lllll11111_opy_ = bstack1l1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡲࡡࡴࡶࡢࡷࡹࡧࡲࡵࡧࡧࠦဤ")
    bstack1llllll1l1l_opy_ = bstack1l1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥ࡬ࡢࡵࡷࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨဥ")
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
        bstack1llll1l1l11_opy_: List[str]=[bstack1l1_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣဦ")],
    ):
        super().__init__(bstack1llll1l1l11_opy_, bstack1lll1llllll_opy_)
        self.bstack1llll11ll11_opy_ = any(bstack1l1_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤဧ") in item.lower() for item in bstack1llll1l1l11_opy_)
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
            self.logger.warning(bstack1l1_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡪࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀࠤࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࠢဨ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠢࠣဩ"))
            return
        if not self.bstack1llll11ll11_opy_:
            self.logger.warning(bstack1l1_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠾ࠤဪ") + str(str(self.bstack1llll1l1l11_opy_)) + bstack1l1_opy_ (u"ࠤࠥါ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1l1_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧာ") + str(kwargs) + bstack1l1_opy_ (u"ࠦࠧိ"))
            return
        instance = self.__1llll1l11ll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1l1_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡧࡲࡨࡵࡀࠦီ") + str(args) + bstack1l1_opy_ (u"ࠨࠢု"))
            return
        try:
            if test_framework_state == bstack1111l11l1l_opy_.TEST:
                if not TestFramework.bstack111lll1l1l_opy_(instance, TestFramework.bstack1llll1ll11l_opy_) and test_hook_state == bstack1111l11l11_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1lll1ll11ll_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack1l1_opy_ (u"ࠢ࡭ࡱࡤࡨࡪࡪࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢူ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠣࠤေ"))
                if test_hook_state == bstack1111l11l11_opy_.PRE and not TestFramework.bstack111lll1l1l_opy_(instance, TestFramework.bstack1111111111_opy_):
                    TestFramework.bstack111l1ll11l_opy_(instance, TestFramework.bstack1111111111_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1llll11111l_opy_(instance, args)
                    self.logger.debug(bstack1l1_opy_ (u"ࠤࡶࡩࡹࠦࡴࡦࡵࡷ࠱ࡸࡺࡡࡳࡶࠣࡪࡴࡸࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢဲ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠥࠦဳ"))
                elif test_hook_state == bstack1111l11l11_opy_.POST and not TestFramework.bstack111lll1l1l_opy_(instance, TestFramework.bstack1llll1lll1l_opy_):
                    TestFramework.bstack111l1ll11l_opy_(instance, TestFramework.bstack1llll1lll1l_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1l1_opy_ (u"ࠦࡸ࡫ࡴࠡࡶࡨࡷࡹ࠳ࡥ࡯ࡦࠣࡪࡴࡸࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢဴ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠧࠨဵ"))
            elif test_framework_state == bstack1111l11l1l_opy_.STEP:
                if test_hook_state == bstack1111l11l11_opy_.PRE:
                    PytestBDDFramework.__1lllll11l11_opy_(instance, args)
                elif test_hook_state == bstack1111l11l11_opy_.POST:
                    PytestBDDFramework.__1llll1l11l1_opy_(instance, args)
            elif test_framework_state == bstack1111l11l1l_opy_.LOG and test_hook_state == bstack1111l11l11_opy_.POST:
                PytestBDDFramework.__1llll1l1l1l_opy_(instance, *args)
            elif test_framework_state == bstack1111l11l1l_opy_.LOG_REPORT and test_hook_state == bstack1111l11l11_opy_.POST:
                self.__1lllll1ll11_opy_(instance, *args)
            elif test_framework_state in PytestBDDFramework.bstack1lllll1l1l1_opy_:
                self.__1llllll11ll_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1l1_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢံ") + str(instance.ref()) + bstack1l1_opy_ (u"့ࠢࠣ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1llll1111ll_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
    def bstack1lllllllll1_opy_(self):
        return self.bstack1llll11ll11_opy_
    def __1llll1l111l_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1l1_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡴࡷ࡯ࡸࠧး"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1llll1lll11_opy_(rep, [bstack1l1_opy_ (u"ࠤࡺ࡬ࡪࡴ္ࠢ"), bstack1l1_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨ်ࠦ"), bstack1l1_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦျ"), bstack1l1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧြ"), bstack1l1_opy_ (u"ࠨࡳ࡬࡫ࡳࡴࡪࡪࠢွ"), bstack1l1_opy_ (u"ࠢ࡭ࡱࡱ࡫ࡷ࡫ࡰࡳࡶࡨࡼࡹࠨှ")])
        return None
    def __1lllll1ll11_opy_(self, instance: bstack1111ll1l11_opy_, *args):
        result = self.__1llll1l111l_opy_(*args)
        if not result:
            return
        failure = None
        bstack111llll11l_opy_ = None
        if result.get(bstack1l1_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤဿ"), None) == bstack1l1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ၀") and len(args) > 1 and getattr(args[1], bstack1l1_opy_ (u"ࠥࡩࡽࡩࡩ࡯ࡨࡲࠦ၁"), None) is not None:
            failure = [{bstack1l1_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧ၂"): [args[1].excinfo.exconly(), result.get(bstack1l1_opy_ (u"ࠧࡲ࡯࡯ࡩࡵࡩࡵࡸࡴࡦࡺࡷࠦ၃"), None)]}]
            bstack111llll11l_opy_ = bstack1l1_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢ၄") if bstack1l1_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥ၅") in getattr(args[1].excinfo, bstack1l1_opy_ (u"ࠣࡶࡼࡴࡪࡴࡡ࡮ࡧࠥ၆"), bstack1l1_opy_ (u"ࠤࠥ၇")) else bstack1l1_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦ၈")
        bstack1llll11lll1_opy_ = result.get(bstack1l1_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧ၉"), TestFramework.bstack1llll11l111_opy_)
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
            target = None # bstack1llll11l11l_opy_ bstack1llll1l1ll1_opy_ this to be bstack1l1_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧ၊")
            if test_framework_state == bstack1111l11l1l_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1lll1lll1l1_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1111l11l1l_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1l1_opy_ (u"ࠨ࡮ࡰࡦࡨࠦ။"), None), bstack1l1_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢ၌"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1l1_opy_ (u"ࠣࡰࡲࡨࡪࠨ၍"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack1l1_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤ၎"), None):
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
        bstack1lllll1lll1_opy_ = TestFramework.bstack111l11ll11_opy_(instance, PytestBDDFramework.bstack1lllllll1l1_opy_, {})
        if not key in bstack1lllll1lll1_opy_:
            bstack1lllll1lll1_opy_[key] = []
        bstack1lllll1llll_opy_ = TestFramework.bstack111l11ll11_opy_(instance, PytestBDDFramework.bstack1llll11llll_opy_, {})
        if not key in bstack1lllll1llll_opy_:
            bstack1lllll1llll_opy_[key] = []
        bstack1lll1llll1l_opy_ = {
            PytestBDDFramework.bstack1lllllll1l1_opy_: bstack1lllll1lll1_opy_,
            PytestBDDFramework.bstack1llll11llll_opy_: bstack1lllll1llll_opy_,
        }
        if test_hook_state == bstack1111l11l11_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack1l1_opy_ (u"ࠥ࡯ࡪࡿࠢ၏"): key,
                TestFramework.bstack1lllllll1ll_opy_: uuid4().__str__(),
                TestFramework.bstack1lll1llll11_opy_: TestFramework.bstack1llllll11l1_opy_,
                TestFramework.bstack11111111l1_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1llllll1ll1_opy_: [],
                TestFramework.bstack1lllll111l1_opy_: hook_name
            }
            bstack1lllll1lll1_opy_[key].append(hook)
            bstack1lll1llll1l_opy_[PytestBDDFramework.bstack1lllll11111_opy_] = key
        elif test_hook_state == bstack1111l11l11_opy_.POST:
            bstack1lll1lll111_opy_ = bstack1lllll1lll1_opy_.get(key, [])
            hook = bstack1lll1lll111_opy_.pop() if bstack1lll1lll111_opy_ else None
            if hook:
                result = self.__1llll1l111l_opy_(*args)
                if result:
                    bstack1lllll1l1ll_opy_ = result.get(bstack1l1_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧၐ"), TestFramework.bstack1llllll11l1_opy_)
                    if bstack1lllll1l1ll_opy_ != TestFramework.bstack1llllll11l1_opy_:
                        hook[TestFramework.bstack1lll1llll11_opy_] = bstack1lllll1l1ll_opy_
                hook[TestFramework.bstack1llll1llll1_opy_] = datetime.now(tz=timezone.utc)
                bstack1lllll1llll_opy_[key].append(hook)
                bstack1lll1llll1l_opy_[PytestBDDFramework.bstack1llllll1l1l_opy_] = key
        TestFramework.bstack1llll111l11_opy_(instance, bstack1lll1llll1l_opy_)
        self.logger.debug(bstack1l1_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡭ࡵ࡯࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࡱࡥࡺࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪ࠽ࡼࡪࡲࡳࡰࡹ࡟ࡴࡶࡤࡶࡹ࡫ࡤࡾࠢ࡫ࡳࡴࡱࡳࡠࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡀࠦၑ") + str(bstack1lllll1llll_opy_) + bstack1l1_opy_ (u"ࠨࠢၒ"))
    def __1llll11l1ll_opy_(
        self,
        context: bstack1lllll1ll1l_opy_,
        test_framework_state: bstack1111l11l1l_opy_,
        test_hook_state: bstack1111l11l11_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1llll1lll11_opy_(args[0], [bstack1l1_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨၓ"), bstack1l1_opy_ (u"ࠣࡣࡵ࡫ࡳࡧ࡭ࡦࠤၔ"), bstack1l1_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࡴࠤၕ"), bstack1l1_opy_ (u"ࠥ࡭ࡩࡹࠢၖ"), bstack1l1_opy_ (u"ࠦࡺࡴࡩࡵࡶࡨࡷࡹࠨၗ"), bstack1l1_opy_ (u"ࠧࡨࡡࡴࡧ࡬ࡨࠧၘ")]) if len(args) > 0 else {}
        request = args[0] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack1l1_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧၙ")) else fixturedef.get(bstack1l1_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨၚ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1l1_opy_ (u"ࠣࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࠨၛ")) else None
        node = request.node if hasattr(request, bstack1l1_opy_ (u"ࠤࡱࡳࡩ࡫ࠢၜ")) else None
        target = request.node.nodeid if hasattr(node, bstack1l1_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥၝ")) else None
        baseid = fixturedef.get(bstack1l1_opy_ (u"ࠦࡧࡧࡳࡦ࡫ࡧࠦၞ"), None) or bstack1l1_opy_ (u"ࠧࠨၟ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1l1_opy_ (u"ࠨ࡟ࡱࡻࡩࡹࡳࡩࡩࡵࡧࡰࠦၠ")):
            target = PytestBDDFramework.__1llll1l1111_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1l1_opy_ (u"ࠢ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠤၡ")) else None
            if target and not TestFramework.bstack1llllllll1l_opy_(target):
                self.__1lll1lll1l1_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1l1_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡧࡹࡩࡳࡺ࠺ࠡࡨࡤࡰࡱࡨࡡࡤ࡭ࠣࡸࡦࡸࡧࡦࡶࡀࡿࡹࡧࡲࡨࡧࡷࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡲࡴࡪࡥ࠾ࡽࡱࡳࡩ࡫ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥၢ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠤࠥၣ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1l1_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡩ࡫ࡦ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡧࡩ࡫ࢃࠠࡴࡥࡲࡴࡪࡃࡻࡴࡥࡲࡴࡪࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣၤ") + str(target) + bstack1l1_opy_ (u"ࠦࠧၥ"))
            return None
        instance = TestFramework.bstack1llllllll1l_opy_(target)
        if not instance:
            self.logger.warning(bstack1l1_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤࡧࡧࡳࡦ࡫ࡧࡁࢀࡨࡡࡴࡧ࡬ࡨࢂࠦࡴࡢࡴࡪࡩࡹࡃࠢၦ") + str(target) + bstack1l1_opy_ (u"ࠨࠢၧ"))
            return None
        bstack1llll111ll1_opy_ = TestFramework.bstack111l11ll11_opy_(instance, PytestBDDFramework.bstack1llll111lll_opy_, {})
        if os.getenv(bstack1l1_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡈࡏࡅࡌࡥࡆࡊ࡚ࡗ࡙ࡗࡋࡓࠣၨ"), bstack1l1_opy_ (u"ࠣ࠳ࠥၩ")) == bstack1l1_opy_ (u"ࠤ࠴ࠦၪ"):
            bstack1llllllllll_opy_ = bstack1l1_opy_ (u"ࠥ࠾ࠧၫ").join((scope, fixturename))
            bstack1llll1ll111_opy_ = datetime.now(tz=timezone.utc)
            bstack11111111ll_opy_ = {
                bstack1l1_opy_ (u"ࠦࡰ࡫ࡹࠣၬ"): bstack1llllllllll_opy_,
                bstack1l1_opy_ (u"ࠧࡺࡡࡨࡵࠥၭ"): PytestBDDFramework.__1lll1lllll1_opy_(request.node, scenario),
                bstack1l1_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫ࠢၮ"): fixturedef,
                bstack1l1_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨၯ"): scope,
                bstack1l1_opy_ (u"ࠣࡶࡼࡴࡪࠨၰ"): None,
            }
            try:
                if test_hook_state == bstack1111l11l11_opy_.POST and callable(getattr(args[-1], bstack1l1_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡵࡸࡰࡹࠨၱ"), None)):
                    bstack11111111ll_opy_[bstack1l1_opy_ (u"ࠥࡸࡾࡶࡥࠣၲ")] = TestFramework.bstack1lllllll111_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1111l11l11_opy_.PRE:
                bstack11111111ll_opy_[bstack1l1_opy_ (u"ࠦࡺࡻࡩࡥࠤၳ")] = uuid4().__str__()
                bstack11111111ll_opy_[PytestBDDFramework.bstack11111111l1_opy_] = bstack1llll1ll111_opy_
            elif test_hook_state == bstack1111l11l11_opy_.POST:
                bstack11111111ll_opy_[PytestBDDFramework.bstack1llll1llll1_opy_] = bstack1llll1ll111_opy_
            if bstack1llllllllll_opy_ in bstack1llll111ll1_opy_:
                bstack1llll111ll1_opy_[bstack1llllllllll_opy_].update(bstack11111111ll_opy_)
                self.logger.debug(bstack1l1_opy_ (u"ࠧࡻࡰࡥࡣࡷࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡂࠨၴ") + str(bstack1llll111ll1_opy_[bstack1llllllllll_opy_]) + bstack1l1_opy_ (u"ࠨࠢၵ"))
            else:
                bstack1llll111ll1_opy_[bstack1llllllllll_opy_] = bstack11111111ll_opy_
                self.logger.debug(bstack1l1_opy_ (u"ࠢࡴࡣࡹࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡂࢁࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࢂࠦࡴࡳࡣࡦ࡯ࡪࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴ࠿ࠥၶ") + str(len(bstack1llll111ll1_opy_)) + bstack1l1_opy_ (u"ࠣࠤၷ"))
        TestFramework.bstack111l1ll11l_opy_(instance, PytestBDDFramework.bstack1llll111lll_opy_, bstack1llll111ll1_opy_)
        self.logger.debug(bstack1l1_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡵࡀࡿࡱ࡫࡮ࠩࡶࡵࡥࡨࡱࡥࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࡶ࠭ࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤၸ") + str(instance.ref()) + bstack1l1_opy_ (u"ࠥࠦၹ"))
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
            PytestBDDFramework.bstack1llll111lll_opy_: {},
            PytestBDDFramework.bstack1llll11llll_opy_: {},
            PytestBDDFramework.bstack1lllllll1l1_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack111l1ll11l_opy_(ob, TestFramework.bstack1llllll1lll_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack111l1ll11l_opy_(ob, TestFramework.bstack111l111l11_opy_, context.platform_index)
        TestFramework.bstack1lllll11ll1_opy_[ctx.id] = ob
        self.logger.debug(bstack1l1_opy_ (u"ࠦࡸࡧࡶࡦࡦࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠥࡩࡴࡹ࠰࡬ࡨࡂࢁࡣࡵࡺ࠱࡭ࡩࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࡼࡶࡤࡶ࡬࡫ࡴࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦࡵࡀࠦၺ") + str(TestFramework.bstack1lllll11ll1_opy_.keys()) + bstack1l1_opy_ (u"ࠧࠨၻ"))
        return ob
    @staticmethod
    def __1llll11111l_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1l1_opy_ (u"࠭ࡩࡥࠩၼ"): id(step),
                bstack1l1_opy_ (u"ࠧࡵࡧࡻࡸࠬၽ"): step.name,
                bstack1l1_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩၾ"): step.keyword,
            })
        meta = {
            bstack1l1_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࠪၿ"): {
                bstack1l1_opy_ (u"ࠪࡲࡦࡳࡥࠨႀ"): feature.name,
                bstack1l1_opy_ (u"ࠫࡵࡧࡴࡩࠩႁ"): feature.filename,
                bstack1l1_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪႂ"): feature.description
            },
            bstack1l1_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨႃ"): {
                bstack1l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬႄ"): scenario.name
            },
            bstack1l1_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧႅ"): steps,
            bstack1l1_opy_ (u"ࠩࡨࡼࡦࡳࡰ࡭ࡧࡶࠫႆ"): PytestBDDFramework.__1llll11l1l1_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1lll1ll1lll_opy_: meta
            }
        )
    @staticmethod
    def __1lllll11l11_opy_(instance, args):
        request, bstack1lllll111ll_opy_ = args
        bstack1lll1lll1ll_opy_ = id(bstack1lllll111ll_opy_)
        bstack1llll111l1l_opy_ = instance.data[TestFramework.bstack1lll1ll1lll_opy_]
        step = next(filter(lambda st: st[bstack1l1_opy_ (u"ࠪ࡭ࡩ࠭ႇ")] == bstack1lll1lll1ll_opy_, bstack1llll111l1l_opy_[bstack1l1_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪႈ")]), None)
        step.update({
            bstack1l1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩႉ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1llll111l1l_opy_[bstack1l1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬႊ")]) if st[bstack1l1_opy_ (u"ࠧࡪࡦࠪႋ")] == step[bstack1l1_opy_ (u"ࠨ࡫ࡧࠫႌ")]), None)
        if index is not None:
            bstack1llll111l1l_opy_[bstack1l1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨႍ")][index] = step
        instance.data[TestFramework.bstack1lll1ll1lll_opy_] = bstack1llll111l1l_opy_
    @staticmethod
    def __1llll1l11l1_opy_(instance, args):
        bstack1l1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡸࡪࡨࡲࠥࡲࡥ࡯ࠢࡤࡶ࡬ࡹࠠࡪࡵࠣ࠶࠱ࠦࡩࡵࠢࡶ࡭࡬ࡴࡩࡧ࡫ࡨࡷࠥࡺࡨࡦࡴࡨࠤ࡮ࡹࠠ࡯ࡱࠣࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡦࡸࡧࡴࠢࡤࡶࡪࠦ࠭ࠡ࡝ࡵࡩࡶࡻࡥࡴࡶ࠯ࠤࡸࡺࡥࡱ࡟ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡮࡬ࠠࡢࡴࡪࡷࠥࡧࡲࡦࠢ࠶ࠤࡹ࡮ࡥ࡯ࠢࡷ࡬ࡪࠦ࡬ࡢࡵࡷࠤࡻࡧ࡬ࡶࡧࠣ࡭ࡸࠦࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨႎ")
        bstack1llllll1111_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1lllll111ll_opy_ = args[1]
        bstack1lll1lll1ll_opy_ = id(bstack1lllll111ll_opy_)
        bstack1llll111l1l_opy_ = instance.data[TestFramework.bstack1lll1ll1lll_opy_]
        step = None
        if bstack1lll1lll1ll_opy_ is not None and bstack1llll111l1l_opy_.get(bstack1l1_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪႏ")):
            step = next(filter(lambda st: st[bstack1l1_opy_ (u"ࠬ࡯ࡤࠨ႐")] == bstack1lll1lll1ll_opy_, bstack1llll111l1l_opy_[bstack1l1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬ႑")]), None)
            step.update({
                bstack1l1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ႒"): bstack1llllll1111_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack1l1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ႓"): bstack1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ႔"),
                bstack1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫ႕"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack1l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ႖"): bstack1l1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ႗"),
                })
        index = next((i for i, st in enumerate(bstack1llll111l1l_opy_[bstack1l1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬ႘")]) if st[bstack1l1_opy_ (u"ࠧࡪࡦࠪ႙")] == step[bstack1l1_opy_ (u"ࠨ࡫ࡧࠫႚ")]), None)
        if index is not None:
            bstack1llll111l1l_opy_[bstack1l1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨႛ")][index] = step
        instance.data[TestFramework.bstack1lll1ll1lll_opy_] = bstack1llll111l1l_opy_
    @staticmethod
    def __1llll11l1l1_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack1l1_opy_ (u"ࠪࡧࡦࡲ࡬ࡴࡲࡨࡧࠬႜ")):
                examples = list(node.callspec.params[bstack1l1_opy_ (u"ࠫࡤࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡨࡼࡦࡳࡰ࡭ࡧࠪႝ")].values())
            return examples
        except:
            return []
    def bstack1llll1lllll_opy_(self, instance: bstack1111ll1l11_opy_, bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_]):
        bstack1lllllll11l_opy_ = (
            PytestBDDFramework.bstack1lllll11111_opy_
            if bstack111ll111l1_opy_[1] == bstack1111l11l11_opy_.PRE
            else PytestBDDFramework.bstack1llllll1l1l_opy_
        )
        hook = PytestBDDFramework.bstack1llll1l1lll_opy_(instance, bstack1lllllll11l_opy_)
        entries = hook.get(TestFramework.bstack1llllll1ll1_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.bstack111l11ll11_opy_(instance, TestFramework.bstack1lllll11lll_opy_, []))
        return entries
    def bstack1llll11ll1l_opy_(self, instance: bstack1111ll1l11_opy_, bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_]):
        bstack1lllllll11l_opy_ = (
            PytestBDDFramework.bstack1lllll11111_opy_
            if bstack111ll111l1_opy_[1] == bstack1111l11l11_opy_.PRE
            else PytestBDDFramework.bstack1llllll1l1l_opy_
        )
        PytestBDDFramework.bstack1llll1ll1l1_opy_(instance, bstack1lllllll11l_opy_)
        TestFramework.bstack111l11ll11_opy_(instance, TestFramework.bstack1lllll11lll_opy_, []).clear()
    @staticmethod
    def bstack1llll1l1lll_opy_(instance: bstack1111ll1l11_opy_, bstack1lllllll11l_opy_: str):
        bstack1lllll11l1l_opy_ = (
            PytestBDDFramework.bstack1llll11llll_opy_
            if bstack1lllllll11l_opy_ == PytestBDDFramework.bstack1llllll1l1l_opy_
            else PytestBDDFramework.bstack1lllllll1l1_opy_
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
        hook = PytestBDDFramework.bstack1llll1l1lll_opy_(instance, bstack1lllllll11l_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1llllll1ll1_opy_, []).clear()
    @staticmethod
    def __1llll1l1l1l_opy_(instance: bstack1111ll1l11_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1l1_opy_ (u"ࠧ࡭ࡥࡵࡡࡵࡩࡨࡵࡲࡥࡵࠥ႞"), None)):
            return
        if os.getenv(bstack1l1_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡒࡏࡈࡕࠥ႟"), bstack1l1_opy_ (u"ࠢ࠲ࠤႠ")) != bstack1l1_opy_ (u"ࠣ࠳ࠥႡ"):
            PytestBDDFramework.logger.warning(bstack1l1_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡪࡰࡪࠤࡨࡧࡰ࡭ࡱࡪࠦႢ"))
            return
        bstack1llllllll11_opy_ = {
            bstack1l1_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤႣ"): (PytestBDDFramework.bstack1lllll11111_opy_, PytestBDDFramework.bstack1lllllll1l1_opy_),
            bstack1l1_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨႤ"): (PytestBDDFramework.bstack1llllll1l1l_opy_, PytestBDDFramework.bstack1llll11llll_opy_),
        }
        for when in (bstack1l1_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦႥ"), bstack1l1_opy_ (u"ࠨࡣࡢ࡮࡯ࠦႦ"), bstack1l1_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤႧ")):
            bstack1lll1ll1ll1_opy_ = args[1].get_records(when)
            if not bstack1lll1ll1ll1_opy_:
                continue
            records = [
                bstack1lll1ll111l_opy_(
                    kind=TestFramework.bstack1lllll1111l_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1l1_opy_ (u"ࠣ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨࠦႨ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1l1_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡦࠥႩ")) and r.created
                        else None
                    ),
                )
                for r in bstack1lll1ll1ll1_opy_
                if isinstance(getattr(r, bstack1l1_opy_ (u"ࠥࡱࡪࡹࡳࡢࡩࡨࠦႪ"), None), str) and r.message.strip()
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
    def __1lll1ll11ll_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1lll1l1ll1l_opy_(request.node, scenario)
        bstack1lll1ll1111_opy_ = feature.filename
        if not test_id or not test_name or not bstack1lll1ll1111_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1llll1ll1ll_opy_: uuid4().__str__(),
            TestFramework.bstack1llll1ll11l_opy_: test_id,
            TestFramework.bstack1lllll1l111_opy_: test_name,
            TestFramework.bstack1llllll1l11_opy_: test_id,
            TestFramework.bstack111111111l_opy_: bstack1lll1ll1111_opy_,
            TestFramework.bstack1lll1ll1l11_opy_: PytestBDDFramework.__1lll1lllll1_opy_(feature, scenario),
            TestFramework.bstack1lll1l1lll1_opy_: code,
            TestFramework.bstack1111l1l1ll_opy_: TestFramework.bstack1llll11l111_opy_,
            TestFramework.bstack1111l1l1l1_opy_: test_name
        }
    @staticmethod
    def __1lll1l1ll1l_opy_(node, scenario):
        if hasattr(node, bstack1l1_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭Ⴋ")):
            parts = node.nodeid.rsplit(bstack1l1_opy_ (u"ࠧࡡࠢႬ"))
            params = parts[-1]
            return bstack1l1_opy_ (u"ࠨࡻࡾࠢ࡞ࡿࢂࠨႭ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1lll1lllll1_opy_(feature, scenario) -> List[str]:
        return list(feature.tags) + list(scenario.tags)
    @staticmethod
    def __1llll1l1111_opy_(location):
        return bstack1l1_opy_ (u"ࠢ࠻࠼ࠥႮ").join(filter(lambda x: isinstance(x, str), location))