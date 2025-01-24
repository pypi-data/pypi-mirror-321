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
from datetime import datetime, timezone
import os
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack111l11l1l1_opy_ import bstack111l1llll1_opy_, bstack111ll1ll11_opy_, bstack111ll11111_opy_
from browserstack_sdk.sdk_cli.bstack111l1ll1ll_opy_ import bstack111ll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1111l11lll_opy_ import bstack1111ll1111_opy_
from browserstack_sdk.sdk_cli.bstack111l111l1l_opy_ import bstack111l111ll1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1111l11l1l_opy_, bstack1111ll1l11_opy_, bstack1111l11l11_opy_, bstack1lll1ll111l_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1ll11l11111_opy_
bstack1ll11l1llll_opy_ = [bstack1l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᆂ"), bstack1l1_opy_ (u"ࠥࡴࡦࡸࡥ࡯ࡶࠥᆃ"), bstack1l1_opy_ (u"ࠦࡨࡵ࡮ࡧ࡫ࡪࠦᆄ"), bstack1l1_opy_ (u"ࠧࡹࡥࡴࡵ࡬ࡳࡳࠨᆅ"), bstack1l1_opy_ (u"ࠨࡰࡢࡶ࡫ࠦᆆ")]
bstack1ll11l1ll11_opy_ = {
    bstack1l1_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡱࡻࡷ࡬ࡴࡴ࠮ࡊࡶࡨࡱࠧᆇ"): bstack1ll11l1llll_opy_,
    bstack1l1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡲࡼࡸ࡭ࡵ࡮࠯ࡒࡤࡧࡰࡧࡧࡦࠤᆈ"): bstack1ll11l1llll_opy_,
    bstack1l1_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡳࡽࡹ࡮࡯࡯࠰ࡐࡳࡩࡻ࡬ࡦࠤᆉ"): bstack1ll11l1llll_opy_,
    bstack1l1_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡴࡾࡺࡨࡰࡰ࠱ࡇࡱࡧࡳࡴࠤᆊ"): bstack1ll11l1llll_opy_,
    bstack1l1_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡵࡿࡴࡩࡱࡱ࠲ࡋࡻ࡮ࡤࡶ࡬ࡳࡳࠨᆋ"): bstack1ll11l1llll_opy_
    + [
        bstack1l1_opy_ (u"ࠧࡵࡲࡪࡩ࡬ࡲࡦࡲ࡮ࡢ࡯ࡨࠦᆌ"),
        bstack1l1_opy_ (u"ࠨ࡫ࡦࡻࡺࡳࡷࡪࡳࠣᆍ"),
        bstack1l1_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥࡪࡰࡩࡳࠧᆎ"),
        bstack1l1_opy_ (u"ࠣ࡭ࡨࡽࡼࡵࡲࡥࡵࠥᆏ"),
        bstack1l1_opy_ (u"ࠤࡦࡥࡱࡲࡳࡱࡧࡦࠦᆐ"),
        bstack1l1_opy_ (u"ࠥࡧࡦࡲ࡬ࡰࡤ࡭ࠦᆑ"),
        bstack1l1_opy_ (u"ࠦࡸࡺࡡࡳࡶࠥᆒ"),
        bstack1l1_opy_ (u"ࠧࡹࡴࡰࡲࠥᆓ"),
        bstack1l1_opy_ (u"ࠨࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠣᆔ"),
        bstack1l1_opy_ (u"ࠢࡸࡪࡨࡲࠧᆕ"),
    ],
    bstack1l1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯࡯ࡤ࡭ࡳ࠴ࡓࡦࡵࡶ࡭ࡴࡴࠢᆖ"): [bstack1l1_opy_ (u"ࠤࡶࡸࡦࡸࡴࡱࡣࡷ࡬ࠧᆗ"), bstack1l1_opy_ (u"ࠥࡸࡪࡹࡴࡴࡨࡤ࡭ࡱ࡫ࡤࠣᆘ"), bstack1l1_opy_ (u"ࠦࡹ࡫ࡳࡵࡵࡦࡳࡱࡲࡥࡤࡶࡨࡨࠧᆙ"), bstack1l1_opy_ (u"ࠧ࡯ࡴࡦ࡯ࡶࠦᆚ")],
    bstack1l1_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡣࡰࡰࡩ࡭࡬࠴ࡃࡰࡰࡩ࡭࡬ࠨᆛ"): [bstack1l1_opy_ (u"ࠢࡪࡰࡹࡳࡨࡧࡴࡪࡱࡱࡣࡵࡧࡲࡢ࡯ࡶࠦᆜ"), bstack1l1_opy_ (u"ࠣࡣࡵ࡫ࡸࠨᆝ")],
    bstack1l1_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡩ࡭ࡽࡺࡵࡳࡧࡶ࠲ࡋ࡯ࡸࡵࡷࡵࡩࡉ࡫ࡦࠣᆞ"): [bstack1l1_opy_ (u"ࠥࡷࡨࡵࡰࡦࠤᆟ"), bstack1l1_opy_ (u"ࠦࡦࡸࡧ࡯ࡣࡰࡩࠧᆠ"), bstack1l1_opy_ (u"ࠧ࡬ࡵ࡯ࡥࠥᆡ"), bstack1l1_opy_ (u"ࠨࡰࡢࡴࡤࡱࡸࠨᆢ"), bstack1l1_opy_ (u"ࠢࡶࡰ࡬ࡸࡹ࡫ࡳࡵࠤᆣ"), bstack1l1_opy_ (u"ࠣ࡫ࡧࡷࠧᆤ")],
    bstack1l1_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡩ࡭ࡽࡺࡵࡳࡧࡶ࠲ࡘࡻࡢࡓࡧࡴࡹࡪࡹࡴࠣᆥ"): [bstack1l1_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࠣᆦ"), bstack1l1_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࠥᆧ"), bstack1l1_opy_ (u"ࠧࡶࡡࡳࡣࡰࡣ࡮ࡴࡤࡦࡺࠥᆨ")],
    bstack1l1_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡲࡶࡰࡱࡩࡷ࠴ࡃࡢ࡮࡯ࡍࡳ࡬࡯ࠣᆩ"): [bstack1l1_opy_ (u"ࠢࡸࡪࡨࡲࠧᆪ"), bstack1l1_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࠣᆫ")],
    bstack1l1_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡰࡥࡷࡱ࠮ࡴࡶࡵࡹࡨࡺࡵࡳࡧࡶ࠲ࡓࡵࡤࡦࡍࡨࡽࡼࡵࡲࡥࡵࠥᆬ"): [bstack1l1_opy_ (u"ࠥࡲࡴࡪࡥࠣᆭ"), bstack1l1_opy_ (u"ࠦࡵࡧࡲࡦࡰࡷࠦᆮ")],
    bstack1l1_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡳࡡࡳ࡭࠱ࡷࡹࡸࡵࡤࡶࡸࡶࡪࡹ࠮ࡎࡣࡵ࡯ࠧᆯ"): [bstack1l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᆰ"), bstack1l1_opy_ (u"ࠢࡢࡴࡪࡷࠧᆱ"), bstack1l1_opy_ (u"ࠣ࡭ࡺࡥࡷ࡭ࡳࠣᆲ")],
}
class bstack1ll1l1l1ll1_opy_(bstack111ll1l111_opy_):
    bstack1ll11l11lll_opy_ = bstack1l1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡥࡧࡩࡩࡷࡸࡥࡥࠤᆳ")
    bstack1ll11lll1l1_opy_ = bstack1l1_opy_ (u"ࠥࡍࡓࡌࡏࠣᆴ")
    bstack1ll11ll11l1_opy_ = bstack1l1_opy_ (u"ࠦࡊࡘࡒࡐࡔࠥᆵ")
    bstack1ll11ll1ll1_opy_: Callable
    bstack1ll1l111111_opy_: Callable
    def __init__(self):
        super().__init__()
        if os.getenv(bstack1l1_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡔ࠷࠱࡚ࠤᆶ"), bstack1l1_opy_ (u"ࠨ࠱ࠣᆷ")) != bstack1l1_opy_ (u"ࠢ࠲ࠤᆸ") or not self.is_enabled():
            self.logger.warning(bstack1l1_opy_ (u"ࠣࠤᆹ") + str(self.__class__.__name__) + bstack1l1_opy_ (u"ࠤࠣࡨ࡮ࡹࡡࡣ࡮ࡨࡨࠧᆺ"))
            return
        TestFramework.bstack111l1ll111_opy_((bstack1111l11l1l_opy_.TEST, bstack1111l11l11_opy_.PRE), self.bstack1111ll1l1l_opy_)
        TestFramework.bstack111l1ll111_opy_((bstack1111l11l1l_opy_.TEST, bstack1111l11l11_opy_.POST), self.bstack1111l111ll_opy_)
        for event in bstack1111l11l1l_opy_:
            for state in bstack1111l11l11_opy_:
                TestFramework.bstack111l1ll111_opy_((event, state), self.bstack1ll11l1ll1l_opy_)
        bstack111l111ll1_opy_.bstack111l1ll111_opy_((bstack111ll1ll11_opy_.bstack111ll1l1l1_opy_, bstack111ll11111_opy_.POST), self.bstack1ll11l1lll1_opy_)
        self.bstack1ll11ll1ll1_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1ll11l1111l_opy_(bstack1ll1l1l1ll1_opy_.bstack1ll11lll1l1_opy_, self.bstack1ll11ll1ll1_opy_)
        self.bstack1ll1l111111_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1ll11l1111l_opy_(bstack1ll1l1l1ll1_opy_.bstack1ll11ll11l1_opy_, self.bstack1ll1l111111_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1ll11l1ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1111ll1l11_opy_,
        bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1lllllllll1_opy_() and instance:
            bstack1ll1l11111l_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack111ll111l1_opy_
            if test_framework_state == bstack1111l11l1l_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1111l11l1l_opy_.LOG:
                bstack11l1l1ll11_opy_ = datetime.now()
                entries = f.bstack1llll1lllll_opy_(instance, bstack111ll111l1_opy_)
                if entries:
                    self.bstack1ll11llllll_opy_(instance, entries)
                    instance.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࠥᆻ"), datetime.now() - bstack11l1l1ll11_opy_)
                    f.bstack1llll11ll1l_opy_(instance, bstack111ll111l1_opy_)
                instance.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠦࡴ࠷࠱ࡺ࠼ࡲࡲࡤࡧ࡬࡭ࡡࡷࡩࡸࡺ࡟ࡦࡸࡨࡲࡹࡹࠢᆼ"), datetime.now() - bstack1ll1l11111l_opy_)
                return # do not send this event with the bstack1ll1l11l11l_opy_ bstack1ll1l11l1l1_opy_
            elif (
                test_framework_state == bstack1111l11l1l_opy_.TEST
                and test_hook_state == bstack1111l11l11_opy_.POST
                and not f.bstack111lll1l1l_opy_(instance, TestFramework.bstack1lll1ll1l1l_opy_)
            ):
                self.logger.warning(bstack1l1_opy_ (u"ࠧࡪࡲࡰࡲࡳ࡭ࡳ࡭ࠠࡥࡷࡨࠤࡹࡵࠠ࡭ࡣࡦ࡯ࠥࡵࡦࠡࡴࡨࡷࡺࡲࡴࡴࠢࠥᆽ") + str(TestFramework.bstack111lll1l1l_opy_(instance, TestFramework.bstack1lll1ll1l1l_opy_)) + bstack1l1_opy_ (u"ࠨࠢᆾ"))
                f.bstack111l1ll11l_opy_(instance, bstack1ll1l1l1ll1_opy_.bstack1ll11l11lll_opy_, True)
                return # do not send this event bstack1ll111lllll_opy_ bstack1ll11ll11ll_opy_
            elif (
                f.bstack111l11ll11_opy_(instance, bstack1ll1l1l1ll1_opy_.bstack1ll11l11lll_opy_, False)
                and test_framework_state == bstack1111l11l1l_opy_.LOG_REPORT
                and test_hook_state == bstack1111l11l11_opy_.POST
                and f.bstack111lll1l1l_opy_(instance, TestFramework.bstack1lll1ll1l1l_opy_)
            ):
                self.logger.warning(bstack1l1_opy_ (u"ࠢࡪࡰ࡭ࡩࡨࡺࡩ࡯ࡩࠣࡘࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡖࡸࡦࡺࡥ࠯ࡖࡈࡗ࡙࠲ࠠࡕࡧࡶࡸࡍࡵ࡯࡬ࡕࡷࡥࡹ࡫࠮ࡑࡑࡖࡘࠥࠨᆿ") + str(TestFramework.bstack111lll1l1l_opy_(instance, TestFramework.bstack1lll1ll1l1l_opy_)) + bstack1l1_opy_ (u"ࠣࠤᇀ"))
                self.bstack1ll11l1ll1l_opy_(f, instance, (bstack1111l11l1l_opy_.TEST, bstack1111l11l11_opy_.POST), *args, **kwargs)
            bstack11l1l1ll11_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1ll11lll111_opy_ = sorted(
                filter(lambda x: x.get(bstack1l1_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠧᇁ"), None), data.pop(bstack1l1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠥᇂ"), {}).values()),
                key=lambda x: x[bstack1l1_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠢᇃ")],
            )
            if bstack1111ll1111_opy_.bstack1111l1llll_opy_ in data:
                data.pop(bstack1111ll1111_opy_.bstack1111l1llll_opy_)
            data.update({bstack1l1_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࠧᇄ"): bstack1ll11lll111_opy_})
            instance.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠨࡪࡴࡱࡱ࠾ࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࠦᇅ"), datetime.now() - bstack11l1l1ll11_opy_)
            bstack11l1l1ll11_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1ll11l1l11l_opy_)
            instance.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠢ࡫ࡵࡲࡲ࠿ࡵ࡮ࡠࡣ࡯ࡰࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵࡵࠥᇆ"), datetime.now() - bstack11l1l1ll11_opy_)
            self.bstack1ll1l11l1l1_opy_(instance, bstack111ll111l1_opy_, event_json=event_json)
            instance.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠣࡱ࠴࠵ࡾࡀ࡯࡯ࡡࡤࡰࡱࡥࡴࡦࡵࡷࡣࡪࡼࡥ࡯ࡶࡶࠦᇇ"), datetime.now() - bstack1ll1l11111l_opy_)
    def bstack1111ll1l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1111ll1l11_opy_,
        bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_],
        *args,
        **kwargs,
    ):
        bstack1111l1111l_opy_ = [d for d, _ in f.bstack111l11ll11_opy_(instance, bstack1111ll1111_opy_.bstack1111l1llll_opy_, [])]
        if not bstack1111l1111l_opy_:
            return
        if not bstack1ll11l11111_opy_():
            return
        for bstack1ll11lll1ll_opy_ in bstack1111l1111l_opy_:
            driver = bstack1ll11lll1ll_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack1l1_opy_ (u"ࠤࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࡕࡼࡲࡨࡀࠢᇈ") + str(timestamp)
            driver.execute_script(
                bstack1l1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠣᇉ").format(
                    json.dumps(
                        {
                            bstack1l1_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦᇊ"): bstack1l1_opy_ (u"ࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢᇋ"),
                            bstack1l1_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤᇌ"): {
                                bstack1l1_opy_ (u"ࠢࡵࡻࡳࡩࠧᇍ"): bstack1l1_opy_ (u"ࠣࡃࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠧᇎ"),
                                bstack1l1_opy_ (u"ࠤࡧࡥࡹࡧࠢᇏ"): data,
                                bstack1l1_opy_ (u"ࠥࡰࡪࡼࡥ࡭ࠤᇐ"): bstack1l1_opy_ (u"ࠦࡩ࡫ࡢࡶࡩࠥᇑ")
                            }
                        }
                    )
                )
            )
    def bstack1111l111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1111ll1l11_opy_,
        bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_],
        *args,
        **kwargs,
    ):
        keys = [
            bstack1111ll1111_opy_.bstack1111l1llll_opy_,
            bstack1111ll1111_opy_.bstack1111llll1l_opy_,
        ]
        bstack1111l1111l_opy_ = [
            d for key in keys for _, d in f.bstack111l11ll11_opy_(instance, key, [])
        ]
        if not bstack1111l1111l_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦࡵ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡢࡰࡼࠤࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠦࡴࡰࠢ࡯࡭ࡳࡱࠢᇒ"))
            return
        self.bstack1ll1l1111ll_opy_(f, instance, bstack1111l1111l_opy_, bstack111ll111l1_opy_)
    def bstack1ll1l1111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1111ll1l11_opy_,
        bstack1111l1111l_opy_: List[bstack111l1llll1_opy_],
        bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_],
    ):
        if f.bstack111l11ll11_opy_(instance, bstack1111ll1111_opy_.bstack1111l11111_opy_, False):
            return
        self.bstack111l1lllll_opy_()
        bstack11l1l1ll11_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack111l11ll11_opy_(instance, TestFramework.bstack111l111l11_opy_)
        req.test_framework_name = TestFramework.bstack111l11ll11_opy_(instance, TestFramework.bstack1llllll111l_opy_)
        req.test_framework_version = TestFramework.bstack111l11ll11_opy_(instance, TestFramework.bstack1lll1l1llll_opy_)
        req.test_framework_state = bstack111ll111l1_opy_[0].name
        req.test_hook_state = bstack111ll111l1_opy_[1].name
        req.test_uuid = TestFramework.bstack111l11ll11_opy_(instance, TestFramework.bstack1llll1ll1ll_opy_)
        for driver in bstack1111l1111l_opy_:
            session = req.automation_sessions.add()
            session.provider = (
                bstack1l1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠧᇓ")
                if bstack111l111ll1_opy_.bstack111l11ll11_opy_(driver, bstack111l111ll1_opy_.bstack1ll11ll1l11_opy_, False)
                else bstack1l1_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࡠࡩࡵ࡭ࡩࠨᇔ")
            )
            session.ref = driver.ref()
            session.hub_url = bstack111l111ll1_opy_.bstack111l11ll11_opy_(driver, bstack111l111ll1_opy_.bstack1ll11l111ll_opy_, bstack1l1_opy_ (u"ࠣࠤᇕ"))
            session.framework_name = driver.framework_name
            session.framework_version = driver.framework_version
            session.framework_session_id = bstack111l111ll1_opy_.bstack111l11ll11_opy_(driver, bstack111l111ll1_opy_.bstack1ll1l111l11_opy_, bstack1l1_opy_ (u"ࠤࠥᇖ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        try:
            r = self.bstack111ll1l11l_opy_.TestSessionEvent(req)
            instance.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥࡴࡦࡵࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡫ࡶࡦࡰࡷࠦᇗ"), datetime.now() - bstack11l1l1ll11_opy_)
            f.bstack111l1ll11l_opy_(instance, bstack1111ll1111_opy_.bstack1111l11111_opy_, r.success)
            if not r.success:
                self.logger.info(bstack1l1_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨᇘ") + str(r) + bstack1l1_opy_ (u"ࠧࠨᇙ"))
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦᇚ") + str(e) + bstack1l1_opy_ (u"ࠢࠣᇛ"))
            traceback.print_exc()
            raise e
    def bstack1ll11l1lll1_opy_(
        self,
        f: bstack111l111ll1_opy_,
        _driver: object,
        exec: Tuple[bstack111l1llll1_opy_, str],
        _1ll11llll1l_opy_: Tuple[bstack111ll1ll11_opy_, bstack111ll11111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack111l111ll1_opy_.bstack1ll11l1l1l1_opy_(method_name):
            return
        if f.bstack1lll1l11l1l_opy_(*args) != bstack111l111ll1_opy_.bstack1ll11l11l1l_opy_:
            return
        bstack1ll1l11111l_opy_ = datetime.now()
        screenshot = result.get(bstack1l1_opy_ (u"ࠣࡸࡤࡰࡺ࡫ࠢᇜ"), None) if isinstance(result, dict) else None
        if not isinstance(screenshot, str) or len(screenshot) <= 0:
            self.logger.warning(bstack1l1_opy_ (u"ࠤ࡬ࡲࡻࡧ࡬ࡪࡦࠣࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠠࡪ࡯ࡤ࡫ࡪࠦࡢࡢࡵࡨ࠺࠹ࠦࡳࡵࡴࠥᇝ"))
            return
        bstack1ll11llll11_opy_ = self.bstack1ll11l11ll1_opy_(instance)
        if bstack1ll11llll11_opy_:
            entry = bstack1lll1ll111l_opy_(TestFramework.bstack1ll11ll1l1l_opy_, screenshot)
            self.bstack1ll11llllll_opy_(bstack1ll11llll11_opy_, [entry])
            instance.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠥࡳ࠶࠷ࡹ࠻ࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡩࡽ࡫ࡣࡶࡶࡨࠦᇞ"), datetime.now() - bstack1ll1l11111l_opy_)
        else:
            self.logger.warning(bstack1l1_opy_ (u"ࠦࡺࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡸࡪࡹࡴࠡࡨࡲࡶࠥࡽࡨࡪࡥ࡫ࠤࡹ࡮ࡩࡴࠢࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠦࡷࡢࡵࠣࡸࡦࡱࡥ࡯ࠢࡥࡽࠥࡪࡲࡪࡸࡨࡶࡂࠨᇟ") + str(instance.ref()) + bstack1l1_opy_ (u"ࠧࠨᇠ"))
    def bstack1ll11llllll_opy_(
        self,
        bstack1ll11llll11_opy_: bstack1111ll1l11_opy_,
        entries: List[bstack1lll1ll111l_opy_],
    ):
        self.bstack111l1lllll_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack111l11ll11_opy_(bstack1ll11llll11_opy_, TestFramework.bstack111l111l11_opy_)
        req.execution_context.hash = str(bstack1ll11llll11_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11llll11_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11llll11_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.bstack111l11ll11_opy_(bstack1ll11llll11_opy_, TestFramework.bstack1llllll111l_opy_)
            log_entry.test_framework_version = TestFramework.bstack111l11ll11_opy_(bstack1ll11llll11_opy_, TestFramework.bstack1lll1l1llll_opy_)
            log_entry.uuid = TestFramework.bstack111l11ll11_opy_(bstack1ll11llll11_opy_, TestFramework.bstack1llll1ll1ll_opy_)
            log_entry.test_framework_state = bstack1ll11llll11_opy_.state.name
            log_entry.message = entry.message.encode(bstack1l1_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᇡ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
        def bstack1ll11lllll1_opy_():
            bstack11l1l1ll11_opy_ = datetime.now()
            try:
                self.bstack111ll1l11l_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1ll11ll1l1l_opy_:
                    bstack1ll11llll11_opy_.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠦᇢ"), datetime.now() - bstack11l1l1ll11_opy_)
                else:
                    bstack1ll11llll11_opy_.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠ࡮ࡲ࡫ࠧᇣ"), datetime.now() - bstack11l1l1ll11_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l1_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᇤ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack111l11111l_opy_.enqueue(bstack1ll11lllll1_opy_)
    def bstack1ll1l11l1l1_opy_(
        self,
        instance: bstack1111ll1l11_opy_,
        bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_],
        event_json=None,
    ):
        self.bstack111l1lllll_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack111l11ll11_opy_(instance, TestFramework.bstack111l111l11_opy_)
        req.test_framework_name = TestFramework.bstack111l11ll11_opy_(instance, TestFramework.bstack1llllll111l_opy_)
        req.test_framework_version = TestFramework.bstack111l11ll11_opy_(instance, TestFramework.bstack1lll1l1llll_opy_)
        req.test_framework_state = bstack111ll111l1_opy_[0].name
        req.test_hook_state = bstack111ll111l1_opy_[1].name
        started_at = TestFramework.bstack111l11ll11_opy_(instance, TestFramework.bstack1111111111_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.bstack111l11ll11_opy_(instance, TestFramework.bstack1llll1lll1l_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1ll11l1l11l_opy_)).encode(bstack1l1_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᇥ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1ll11lllll1_opy_():
            bstack11l1l1ll11_opy_ = datetime.now()
            try:
                self.bstack111ll1l11l_opy_.TestFrameworkEvent(req)
                instance.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟ࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡧࡹࡩࡳࡺࠢᇦ"), datetime.now() - bstack11l1l1ll11_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l1_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᇧ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack111l11111l_opy_.enqueue(bstack1ll11lllll1_opy_)
    def bstack1ll11l11l11_opy_(self, event_url: str, bstack1l1l1l1l_opy_: dict) -> bool:
        return True # always return True so that old bstack1ll11l111l1_opy_ bstack1ll11ll111l_opy_'t bstack1ll1l111ll1_opy_
    def bstack1ll11l11ll1_opy_(self, instance: bstack111l1llll1_opy_):
        bstack1ll11ll1111_opy_ = TestFramework.bstack1ll1l111l1l_opy_(instance.context)
        for t in bstack1ll11ll1111_opy_:
            bstack1111l1111l_opy_ = TestFramework.bstack111l11ll11_opy_(t, bstack1111ll1111_opy_.bstack1111l1llll_opy_, [])
            if any(instance is d[1] for d in bstack1111l1111l_opy_):
                return t
    def bstack1ll11l1l1ll_opy_(self, message):
        self.bstack1ll11ll1ll1_opy_(message + bstack1l1_opy_ (u"ࠨ࡜࡯ࠤᇨ"))
    def log_error(self, message):
        self.bstack1ll1l111111_opy_(message + bstack1l1_opy_ (u"ࠢ࡝ࡰࠥᇩ"))
    def bstack1ll11l1111l_opy_(self, level, original_func):
        def bstack1ll11l1l111_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            bstack1ll11ll1111_opy_ = TestFramework.bstack1ll11ll1lll_opy_()
            if not bstack1ll11ll1111_opy_:
                return return_value
            bstack1ll11llll11_opy_ = next(
                (
                    instance
                    for instance in bstack1ll11ll1111_opy_
                    if TestFramework.bstack111lll1l1l_opy_(instance, TestFramework.bstack1llll1ll1ll_opy_)
                ),
                None,
            )
            if not bstack1ll11llll11_opy_:
                return
            entry = bstack1lll1ll111l_opy_(TestFramework.bstack1lllll1111l_opy_, message, level)
            self.bstack1ll11llllll_opy_(bstack1ll11llll11_opy_, [entry])
            return return_value
        return bstack1ll11l1l111_opy_
class bstack1ll11l1l11l_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1ll111llll1_opy_ = set()
        kwargs[bstack1l1_opy_ (u"ࠣࡵ࡮࡭ࡵࡱࡥࡺࡵࠥᇪ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1ll11lll11l_opy_(obj, self.bstack1ll111llll1_opy_)
def bstack1ll1l111lll_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1ll11lll11l_opy_(obj, bstack1ll111llll1_opy_=None, max_depth=3):
    if bstack1ll111llll1_opy_ is None:
        bstack1ll111llll1_opy_ = set()
    if id(obj) in bstack1ll111llll1_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1ll111llll1_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1ll1l1111l1_opy_ = TestFramework.bstack1lllllll111_opy_(obj)
    bstack1ll1l11l111_opy_ = next((k.lower() in bstack1ll1l1111l1_opy_.lower() for k in bstack1ll11l1ll11_opy_.keys()), None)
    if bstack1ll1l11l111_opy_:
        obj = TestFramework.bstack1llll1lll11_opy_(obj, bstack1ll11l1ll11_opy_[bstack1ll1l11l111_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack1l1_opy_ (u"ࠤࡢࡣࡸࡲ࡯ࡵࡵࡢࡣࠧᇫ")):
            keys = getattr(obj, bstack1l1_opy_ (u"ࠥࡣࡤࡹ࡬ࡰࡶࡶࡣࡤࠨᇬ"), [])
        elif hasattr(obj, bstack1l1_opy_ (u"ࠦࡤࡥࡤࡪࡥࡷࡣࡤࠨᇭ")):
            keys = getattr(obj, bstack1l1_opy_ (u"ࠧࡥ࡟ࡥ࡫ࡦࡸࡤࡥࠢᇮ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack1l1_opy_ (u"ࠨ࡟ࠣᇯ"))}
        if not obj and bstack1ll1l1111l1_opy_ == bstack1l1_opy_ (u"ࠢࡱࡣࡷ࡬ࡱ࡯ࡢ࠯ࡒࡲࡷ࡮ࡾࡐࡢࡶ࡫ࠦᇰ"):
            obj = {bstack1l1_opy_ (u"ࠣࡲࡤࡸ࡭ࠨᇱ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1ll1l111lll_opy_(key) or str(key).startswith(bstack1l1_opy_ (u"ࠤࡢࠦᇲ")):
            continue
        if value is not None and bstack1ll1l111lll_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1ll11lll11l_opy_(value, bstack1ll111llll1_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1ll11lll11l_opy_(o, bstack1ll111llll1_opy_, max_depth) for o in value]))
    return result or None