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
import threading
import os
import logging
from uuid import uuid4
from bstack_utils.bstack1l1ll1ll_opy_ import bstack1l11l11l_opy_, bstack11llllll_opy_
from bstack_utils.bstack1lll1l1l_opy_ import bstack1llll1l1_opy_
from bstack_utils.helper import bstack1l1111ll_opy_, bstack1l111ll1_opy_, Result
from bstack_utils.bstack1l11l1l1_opy_ import bstack1l1ll1l1_opy_
from bstack_utils.capture import bstack1l111l1l_opy_
from bstack_utils.constants import *
logger = logging.getLogger(__name__)
class bstack11l1l11l_opy_:
    def __init__(self):
        self.bstack1lll11ll_opy_ = bstack1l111l1l_opy_(self.bstack11ll1ll1_opy_)
        self.tests = {}
    @staticmethod
    def bstack11ll1ll1_opy_(log):
        if not (log[bstack1l1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬू")] and log[bstack1l1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ृ")].strip()):
            return
        active = bstack1llll1l1_opy_.bstack11llll1l_opy_()
        log = {
            bstack1l1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬॄ"): log[bstack1l1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ॅ")],
            bstack1l1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫॆ"): bstack1l111ll1_opy_(),
            bstack1l1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪे"): log[bstack1l1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫै")],
        }
        if active:
            if active[bstack1l1_opy_ (u"ࠫࡹࡿࡰࡦࠩॉ")] == bstack1l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪॊ"):
                log[bstack1l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ो")] = active[bstack1l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧौ")]
            elif active[bstack1l1_opy_ (u"ࠨࡶࡼࡴࡪ्࠭")] == bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺࠧॎ"):
                log[bstack1l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪॏ")] = active[bstack1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫॐ")]
        bstack1l1ll1l1_opy_.bstack1lll1111_opy_([log])
    def start_test(self, attrs):
        test_uuid = uuid4().__str__()
        self.tests[test_uuid] = {}
        self.bstack1lll11ll_opy_.start()
        driver = bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫ॑"), None)
        bstack1l1ll1ll_opy_ = bstack11llllll_opy_(
            name=attrs.scenario.name,
            uuid=test_uuid,
            started_at=bstack1l111ll1_opy_(),
            file_path=attrs.feature.filename,
            result=bstack1l1_opy_ (u"ࠨࡰࡦࡰࡧ࡭ࡳ࡭॒ࠢ"),
            framework=bstack1l1_opy_ (u"ࠧࡃࡧ࡫ࡥࡻ࡫ࠧ॓"),
            scope=[attrs.feature.name],
            bstack1ll1llll_opy_=bstack1l1ll1l1_opy_.bstack1llll11l_opy_(driver) if driver and driver.session_id else {},
            meta={},
            tags=attrs.scenario.tags
        )
        self.tests[test_uuid][bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ॔")] = bstack1l1ll1ll_opy_
        threading.current_thread().current_test_uuid = test_uuid
        bstack1l1ll1l1_opy_.bstack1l11ll11_opy_(bstack1l1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪॕ"), bstack1l1ll1ll_opy_)
    def end_test(self, attrs):
        bstack11l1ll11_opy_ = {
            bstack1l1_opy_ (u"ࠥࡲࡦࡳࡥࠣॖ"): attrs.feature.name,
            bstack1l1_opy_ (u"ࠦࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠤॗ"): attrs.feature.description
        }
        current_test_uuid = threading.current_thread().current_test_uuid
        bstack1l1ll1ll_opy_ = self.tests[current_test_uuid][bstack1l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨक़")]
        meta = {
            bstack1l1_opy_ (u"ࠨࡦࡦࡣࡷࡹࡷ࡫ࠢख़"): bstack11l1ll11_opy_,
            bstack1l1_opy_ (u"ࠢࡴࡶࡨࡴࡸࠨग़"): bstack1l1ll1ll_opy_.meta.get(bstack1l1_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧज़"), []),
            bstack1l1_opy_ (u"ࠤࡶࡧࡪࡴࡡࡳ࡫ࡲࠦड़"): {
                bstack1l1_opy_ (u"ࠥࡲࡦࡳࡥࠣढ़"): attrs.feature.scenarios[0].name if len(attrs.feature.scenarios) else None
            }
        }
        bstack1l1ll1ll_opy_.bstack11ll1l11_opy_(meta)
        bstack1l1ll1ll_opy_.bstack11ll1111_opy_(bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠩफ़"), []))
        bstack11ll1l1l_opy_, exception = self._11l1lll1_opy_(attrs)
        bstack1ll111l1_opy_ = Result(result=attrs.status.name, exception=exception, bstack11lll111_opy_=[bstack11ll1l1l_opy_])
        self.tests[threading.current_thread().current_test_uuid][bstack1l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨय़")].stop(time=bstack1l111ll1_opy_(), duration=int(attrs.duration)*1000, result=bstack1ll111l1_opy_)
        bstack1l1ll1l1_opy_.bstack1l11ll11_opy_(bstack1l1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨॠ"), self.tests[threading.current_thread().current_test_uuid][bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪॡ")])
    def bstack11ll11l1_opy_(self, attrs):
        bstack1ll1111l_opy_ = {
            bstack1l1_opy_ (u"ࠨ࡫ࡧࠫॢ"): uuid4().__str__(),
            bstack1l1_opy_ (u"ࠩ࡮ࡩࡾࡽ࡯ࡳࡦࠪॣ"): attrs.keyword,
            bstack1l1_opy_ (u"ࠪࡷࡹ࡫ࡰࡠࡣࡵ࡫ࡺࡳࡥ࡯ࡶࠪ।"): [],
            bstack1l1_opy_ (u"ࠫࡹ࡫ࡸࡵࠩ॥"): attrs.name,
            bstack1l1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ०"): bstack1l111ll1_opy_(),
            bstack1l1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭१"): bstack1l1_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨ२"),
            bstack1l1_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭३"): bstack1l1_opy_ (u"ࠩࠪ४")
        }
        self.tests[threading.current_thread().current_test_uuid][bstack1l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭५")].add_step(bstack1ll1111l_opy_)
        threading.current_thread().current_step_uuid = bstack1ll1111l_opy_[bstack1l1_opy_ (u"ࠫ࡮ࡪࠧ६")]
    def bstack11l1l1l1_opy_(self, attrs):
        current_test_id = bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ७"), None)
        current_step_uuid = bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡴࡶࡨࡴࡤࡻࡵࡪࡦࠪ८"), None)
        bstack11ll1l1l_opy_, exception = self._11l1lll1_opy_(attrs)
        bstack1ll111l1_opy_ = Result(result=attrs.status.name, exception=exception, bstack11lll111_opy_=[bstack11ll1l1l_opy_])
        self.tests[current_test_id][bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ९")].bstack1l111l11_opy_(current_step_uuid, duration=int(attrs.duration)*1000, result=bstack1ll111l1_opy_)
        threading.current_thread().current_step_uuid = None
    def bstack11ll11ll_opy_(self, name, attrs):
        try:
            bstack11l1llll_opy_ = uuid4().__str__()
            self.tests[bstack11l1llll_opy_] = {}
            self.bstack1lll11ll_opy_.start()
            scopes = []
            driver = bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ॰"), None)
            current_thread = threading.current_thread()
            if not hasattr(current_thread, bstack1l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹࠧॱ")):
                current_thread.current_test_hooks = []
            current_thread.current_test_hooks.append(bstack11l1llll_opy_)
            if name in [bstack1l1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠢॲ"), bstack1l1_opy_ (u"ࠦࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠢॳ")]:
                file_path = os.path.join(attrs.config.base_dir, attrs.config.environment_file)
                scopes = [attrs.config.environment_file]
            elif name in [bstack1l1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤ࡬ࡥࡢࡶࡸࡶࡪࠨॴ"), bstack1l1_opy_ (u"ࠨࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪࠨॵ")]:
                file_path = attrs.filename
                scopes = [attrs.name]
            else:
                file_path = attrs.filename
                if hasattr(attrs, bstack1l1_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࠨॶ")):
                    scopes =  [attrs.feature.name]
            hook_data = bstack1l11l11l_opy_(
                name=name,
                uuid=bstack11l1llll_opy_,
                started_at=bstack1l111ll1_opy_(),
                file_path=file_path,
                framework=bstack1l1_opy_ (u"ࠣࡄࡨ࡬ࡦࡼࡥࠣॷ"),
                bstack1ll1llll_opy_=bstack1l1ll1l1_opy_.bstack1llll11l_opy_(driver) if driver and driver.session_id else {},
                scope=scopes,
                result=bstack1l1_opy_ (u"ࠤࡳࡩࡳࡪࡩ࡯ࡩࠥॸ"),
                hook_type=name
            )
            self.tests[bstack11l1llll_opy_][bstack1l1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡦࡤࡸࡦࠨॹ")] = hook_data
            current_test_id = bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠦࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠣॺ"), None)
            if current_test_id:
                hook_data.bstack11ll111l_opy_(current_test_id)
            if name == bstack1l1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤॻ"):
                threading.current_thread().before_all_hook_uuid = bstack11l1llll_opy_
            threading.current_thread().current_hook_uuid = bstack11l1llll_opy_
            bstack1l1ll1l1_opy_.bstack1l11ll11_opy_(bstack1l1_opy_ (u"ࠨࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠢॼ"), hook_data)
        except Exception as e:
            logger.debug(bstack1l1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦ࡯ࡤࡥࡸࡶࡷ࡫ࡤࠡ࡫ࡱࠤࡸࡺࡡࡳࡶࠣ࡬ࡴࡵ࡫ࠡࡧࡹࡩࡳࡺࡳ࠭ࠢ࡫ࡳࡴࡱࠠ࡯ࡣࡰࡩ࠿ࠦࠥࡴ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࠩࡸࠨॽ"), name, e)
    def bstack11l1ll1l_opy_(self, attrs):
        bstack1l11l1ll_opy_ = bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬॾ"), None)
        hook_data = self.tests[bstack1l11l1ll_opy_][bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬॿ")]
        status = bstack1l1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥঀ")
        exception = None
        bstack11ll1l1l_opy_ = None
        if hook_data.name == bstack1l1_opy_ (u"ࠦࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠢঁ"):
            self.bstack1lll11ll_opy_.reset()
            bstack11l1l111_opy_ = self.tests[bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬং"), None)][bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩঃ")].result.result
            if bstack11l1l111_opy_ == bstack1l1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ঄"):
                if attrs.hook_failures == 1:
                    status = bstack1l1_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣঅ")
                elif attrs.hook_failures == 2:
                    status = bstack1l1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤআ")
            elif attrs.bstack11l1l1ll_opy_:
                status = bstack1l1_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥই")
            threading.current_thread().before_all_hook_uuid = None
        else:
            if hook_data.name == bstack1l1_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠨঈ") and attrs.hook_failures == 1:
                status = bstack1l1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧউ")
            elif hasattr(attrs, bstack1l1_opy_ (u"࠭ࡥࡳࡴࡲࡶࡤࡳࡥࡴࡵࡤ࡫ࡪ࠭ঊ")) and attrs.error_message:
                status = bstack1l1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢঋ")
            bstack11ll1l1l_opy_, exception = self._11l1lll1_opy_(attrs)
        bstack1ll111l1_opy_ = Result(result=status, exception=exception, bstack11lll111_opy_=[bstack11ll1l1l_opy_])
        hook_data.stop(time=bstack1l111ll1_opy_(), duration=0, result=bstack1ll111l1_opy_)
        bstack1l1ll1l1_opy_.bstack1l11ll11_opy_(bstack1l1_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪঌ"), self.tests[bstack1l11l1ll_opy_][bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ঍")])
        threading.current_thread().current_hook_uuid = None
    def _11l1lll1_opy_(self, attrs):
        try:
            import traceback
            bstack11l11lll_opy_ = traceback.format_tb(attrs.exc_traceback)
            bstack11ll1l1l_opy_ = bstack11l11lll_opy_[-1] if bstack11l11lll_opy_ else None
            exception = attrs.exception
        except Exception:
            logger.debug(bstack1l1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡲࡧࡨࡻࡲࡳࡧࡧࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡨࡻࡳࡵࡱࡰࠤࡹࡸࡡࡤࡧࡥࡥࡨࡱࠢ঎"))
            bstack11ll1l1l_opy_ = None
            exception = None
        return bstack11ll1l1l_opy_, exception