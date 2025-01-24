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
import atexit
import datetime
import inspect
import logging
import os
import signal
import threading
from uuid import uuid4
from bstack_utils.percy_sdk import PercySDK
import tempfile
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack11lll1ll1l_opy_, bstack1l1l1111l_opy_, update, bstack1ll1ll111_opy_,
                                       bstack11l11ll1ll_opy_, bstack111lll11l_opy_, bstack1lll1111l1_opy_, bstack1ll11l1l11_opy_,
                                       bstack1111llll1_opy_, bstack1l11lllll_opy_, bstack1l1l1lll1l_opy_, bstack1l1lllll1l_opy_,
                                       bstack1l11l11l1l_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack1ll1l11l1_opy_)
from browserstack_sdk.bstack1111llll_opy_ import bstack11l11111_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack11ll11llll_opy_
from bstack_utils.capture import bstack1l111l1l_opy_
from bstack_utils.config import Config
from bstack_utils.percy import *
from bstack_utils.constants import bstack11ll11ll11_opy_, bstack1ll11l111l_opy_, bstack1l1l11ll11_opy_, \
    bstack11ll1ll1l1_opy_
from bstack_utils.helper import bstack1l1111ll_opy_, bstack1l111lll11l_opy_, bstack1ll1l11l_opy_, bstack111111ll1_opy_, bstack1ll11l11111_opy_, bstack1l111ll1_opy_, \
    bstack1l11ll11l11_opy_, \
    bstack1l1111l1111_opy_, bstack1lll1lll11_opy_, bstack1ll1ll11l1_opy_, bstack1l11l1ll11l_opy_, bstack111lllll11_opy_, Notset, \
    bstack11llllll11_opy_, bstack1l111l1ll1l_opy_, bstack1l11l1l1ll1_opy_, Result, bstack1l1111lll11_opy_, bstack1l111llll11_opy_, bstack1lll111l_opy_, \
    bstack1l1l111111_opy_, bstack1l111l111_opy_, bstack1ll11l11l_opy_, bstack1l111l111l1_opy_
from bstack_utils.bstack1l1ll111l11_opy_ import bstack1l1l1llllll_opy_
from bstack_utils.messages import bstack1llll111l_opy_, bstack1ll1l1lll_opy_, bstack1ll11lll1_opy_, bstack1lll1ll1l_opy_, bstack111l1l1l_opy_, \
    bstack11111lll1_opy_, bstack1l1111l11_opy_, bstack11lll1ll11_opy_, bstack1l11ll1ll_opy_, bstack1l1llll111_opy_, \
    bstack1lll1111ll_opy_, bstack1l1l11l111_opy_
from bstack_utils.proxy import bstack1l1ll11lll_opy_, bstack1ll1111l1l_opy_
from bstack_utils.bstack1lll1l1ll_opy_ import bstack1l1l111ll1l_opy_, bstack1l1l111ll11_opy_, bstack1l1l11l11ll_opy_, bstack1l1l11l11l1_opy_, \
    bstack1l1l111llll_opy_, bstack1l1l111l1l1_opy_, bstack1l1l111l1ll_opy_, bstack111l11l1l_opy_, bstack1l1l11l1l1l_opy_
from bstack_utils.bstack1l111ll1l_opy_ import bstack11l111111l_opy_
from bstack_utils.bstack1llll11l11_opy_ import bstack1l1ll1ll11_opy_, bstack1l1l1l1l1l_opy_, bstack1l1l1l1lll_opy_, \
    bstack1l1lll1lll_opy_, bstack11ll1l11l_opy_
from bstack_utils.bstack1l1ll1ll_opy_ import bstack11llllll_opy_
from bstack_utils.bstack1lll1l1l_opy_ import bstack1llll1l1_opy_
import bstack_utils.accessibility as bstack111l1ll1_opy_
from bstack_utils.bstack1l11l1l1_opy_ import bstack1l1ll1l1_opy_
from bstack_utils.bstack11ll111lll_opy_ import bstack11ll111lll_opy_
from browserstack_sdk.__init__ import bstack11ll1ll1l_opy_
from browserstack_sdk.sdk_cli.bstack1ll1l1l1l11_opy_ import bstack1ll1l1l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l11l_opy_ import bstack1llll1l11l_opy_, Events, bstack11ll1111ll_opy_
from browserstack_sdk.sdk_cli.test_framework import bstack1lllll1ll1l_opy_, bstack1111l11l1l_opy_, bstack1111l11l11_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1llll1l11l_opy_ import bstack1llll1l11l_opy_, Events, bstack11ll1111ll_opy_
bstack1l111111ll_opy_ = None
bstack1lll1ll1ll_opy_ = None
bstack11lllllll1_opy_ = None
bstack1l1l11lll1_opy_ = None
bstack1l1l1l11ll_opy_ = None
bstack1ll1l11l11_opy_ = None
bstack11ll1l111_opy_ = None
bstack1l111111l_opy_ = None
bstack1ll111l11l_opy_ = None
bstack1111l11ll_opy_ = None
bstack1lll1ll111_opy_ = None
bstack11lll11l11_opy_ = None
bstack1ll1l1llll_opy_ = None
bstack11lll1l1ll_opy_ = bstack1l1_opy_ (u"ࠨࠩᱱ")
CONFIG = {}
bstack1ll1lll11_opy_ = False
bstack11ll1ll111_opy_ = bstack1l1_opy_ (u"ࠩࠪᱲ")
bstack1ll1ll11l_opy_ = bstack1l1_opy_ (u"ࠪࠫᱳ")
bstack1ll11llll_opy_ = False
bstack1l1ll1ll1l_opy_ = []
bstack1l1l11l1l1_opy_ = bstack11ll11ll11_opy_
bstack11l1ll1lll1_opy_ = bstack1l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᱴ")
bstack1ll111111_opy_ = {}
bstack1l1111lll_opy_ = False
logger = bstack11ll11llll_opy_.get_logger(__name__, bstack1l1l11l1l1_opy_)
store = {
    bstack1l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᱵ"): []
}
bstack11l1ll11111_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_1l1l11l1_opy_ = {}
current_test_uuid = None
cli_context = bstack1lllll1ll1l_opy_(
    test_framework_name=bstack1llll11l1l_opy_[bstack1l1_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙࠳ࡂࡅࡆࠪᱶ")] if bstack111lllll11_opy_() else bstack1llll11l1l_opy_[bstack1l1_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚ࠧᱷ")],
    test_framework_version=pytest.__version__,
    platform_index=-1,
)
def bstack11l1l1l111_opy_(page, bstack1llll1lll1_opy_):
    try:
        page.evaluate(bstack1l1_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤᱸ"),
                      bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿࠭ᱹ") + json.dumps(
                          bstack1llll1lll1_opy_) + bstack1l1_opy_ (u"ࠥࢁࢂࠨᱺ"))
    except Exception as e:
        print(bstack1l1_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡻࡾࠤᱻ"), e)
def bstack11l11l1l11_opy_(page, message, level):
    try:
        page.evaluate(bstack1l1_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᱼ"), bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫᱽ") + json.dumps(
            message) + bstack1l1_opy_ (u"ࠧ࠭ࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠪ᱾") + json.dumps(level) + bstack1l1_opy_ (u"ࠨࡿࢀࠫ᱿"))
    except Exception as e:
        print(bstack1l1_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡧ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠢࡾࢁࠧᲀ"), e)
def pytest_configure(config):
    global bstack11ll1ll111_opy_
    global CONFIG
    bstack111l11ll_opy_ = Config.bstack11l111ll_opy_()
    config.args = bstack1llll1l1_opy_.bstack1l1l11ll111_opy_(config.args)
    bstack111l11ll_opy_.bstack1l11ll1l11_opy_(bstack1ll11l11l_opy_(config.getoption(bstack1l1_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧᲁ"))))
    if cli.is_running():
        bstack1llll1l11l_opy_.invoke(Events.CONNECT, bstack11ll1111ll_opy_())
        cli_context.platform_index = int(os.environ.get(bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫᲂ"), bstack1l1_opy_ (u"ࠬ࠶ࠧᲃ")))
        config = json.loads(os.environ.get(bstack1l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࠧᲄ"), bstack1l1_opy_ (u"ࠢࡼࡿࠥᲅ")))
        cli.bstack1ll1llllll1_opy_(bstack1ll1ll11l1_opy_(bstack11ll1ll111_opy_, CONFIG), cli_context.platform_index, bstack1ll1ll111_opy_)
    if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
        cli.bstack1ll1ll111l1_opy_()
        logger.debug(bstack1l1_opy_ (u"ࠣࡅࡏࡍࠥ࡯ࡳࠡࡣࡦࡸ࡮ࡼࡥࠡࡨࡲࡶࠥࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࠢᲆ") + str(cli_context.platform_index) + bstack1l1_opy_ (u"ࠤࠥᲇ"))
        cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.BEFORE_ALL, bstack1111l11l11_opy_.PRE, config)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    when = getattr(call, bstack1l1_opy_ (u"ࠥࡻ࡭࡫࡮ࠣᲈ"), None)
    if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_) and when == bstack1l1_opy_ (u"ࠦࡨࡧ࡬࡭ࠤᲉ"):
        cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.LOG_REPORT, bstack1111l11l11_opy_.PRE, item, call)
    outcome = yield
    if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
        if when == bstack1l1_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦᲊ"):
            cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.BEFORE_EACH, bstack1111l11l11_opy_.POST, item, call, outcome)
        elif when == bstack1l1_opy_ (u"ࠨࡣࡢ࡮࡯ࠦ᲋"):
            cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.LOG_REPORT, bstack1111l11l11_opy_.POST, item, call, outcome)
        elif when == bstack1l1_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤ᲌"):
            cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.AFTER_EACH, bstack1111l11l11_opy_.POST, item, call, outcome)
        return # skip all existing bstack11l1l1ll111_opy_
    bstack11l1l1l1lll_opy_ = item.config.getoption(bstack1l1_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ᲍"))
    plugins = item.config.getoption(bstack1l1_opy_ (u"ࠤࡳࡰࡺ࡭ࡩ࡯ࡵࠥ᲎"))
    report = outcome.get_result()
    bstack11l1l1l11ll_opy_(item, call, report)
    if bstack1l1_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡲ࡯ࡹ࡬࡯࡮ࠣ᲏") not in plugins or bstack111lllll11_opy_():
        return
    summary = []
    driver = getattr(item, bstack1l1_opy_ (u"ࠦࡤࡪࡲࡪࡸࡨࡶࠧᲐ"), None)
    page = getattr(item, bstack1l1_opy_ (u"ࠧࡥࡰࡢࡩࡨࠦᲑ"), None)
    try:
        if (driver == None or driver.session_id == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None or cli.is_running()):
        bstack11l1ll1l111_opy_(item, report, summary, bstack11l1l1l1lll_opy_)
    if (page is not None):
        bstack11l1l1ll1l1_opy_(item, report, summary, bstack11l1l1l1lll_opy_)
def bstack11l1ll1l111_opy_(item, report, summary, bstack11l1l1l1lll_opy_):
    if report.when == bstack1l1_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬᲒ") and report.skipped:
        bstack1l1l11l1l1l_opy_(report)
    if report.when in [bstack1l1_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨᲓ"), bstack1l1_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥᲔ")]:
        return
    if not bstack1ll11l11111_opy_():
        return
    try:
        if (str(bstack11l1l1l1lll_opy_).lower() != bstack1l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᲕ") and not cli.is_running()):
            item._driver.execute_script(
                bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨᲖ") + json.dumps(
                    report.nodeid) + bstack1l1_opy_ (u"ࠫࢂࢃࠧᲗ"))
        os.environ[bstack1l1_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨᲘ")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack1l1_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥ࠻ࠢࡾ࠴ࢂࠨᲙ").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1l1_opy_ (u"ࠢࡸࡣࡶࡼ࡫ࡧࡩ࡭ࠤᲚ")))
    bstack11lll11lll_opy_ = bstack1l1_opy_ (u"ࠣࠤᲛ")
    bstack1l1l11l1l1l_opy_(report)
    if not passed:
        try:
            bstack11lll11lll_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack1l1_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡪࡦ࡯࡬ࡶࡴࡨࠤࡷ࡫ࡡࡴࡱࡱ࠾ࠥࢁ࠰ࡾࠤᲜ").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack11lll11lll_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack1l1_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧᲝ")))
        bstack11lll11lll_opy_ = bstack1l1_opy_ (u"ࠦࠧᲞ")
        if not passed:
            try:
                bstack11lll11lll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack1l1_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡨࡪࡺࡥࡳ࡯࡬ࡲࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡳࡧࡤࡷࡴࡴ࠺ࠡࡽ࠳ࢁࠧᲟ").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack11lll11lll_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤ࡬ࡲ࡫ࡵࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡧࡥࡹࡧࠢ࠻ࠢࠪᲠ")
                    + json.dumps(bstack1l1_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠡࠣᲡ"))
                    + bstack1l1_opy_ (u"ࠣ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࠦᲢ")
                )
            else:
                item._driver.execute_script(
                    bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡤࡢࡶࡤࠦ࠿ࠦࠧᲣ")
                    + json.dumps(str(bstack11lll11lll_opy_))
                    + bstack1l1_opy_ (u"ࠥࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࠨᲤ")
                )
        except Exception as e:
            summary.append(bstack1l1_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡤࡲࡳࡵࡴࡢࡶࡨ࠾ࠥࢁ࠰ࡾࠤᲥ").format(e))
def bstack11l1ll1111l_opy_(test_name, error_message):
    try:
        bstack11l1l1lll1l_opy_ = []
        bstack11l111l1ll_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬᲦ"), bstack1l1_opy_ (u"࠭࠰ࠨᲧ"))
        bstack11lllll1l1_opy_ = {bstack1l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᲨ"): test_name, bstack1l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᲩ"): error_message, bstack1l1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᲪ"): bstack11l111l1ll_opy_}
        bstack11l1ll1l1l1_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1_opy_ (u"ࠪࡴࡼࡥࡰࡺࡶࡨࡷࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨᲫ"))
        if os.path.exists(bstack11l1ll1l1l1_opy_):
            with open(bstack11l1ll1l1l1_opy_) as f:
                bstack11l1l1lll1l_opy_ = json.load(f)
        bstack11l1l1lll1l_opy_.append(bstack11lllll1l1_opy_)
        with open(bstack11l1ll1l1l1_opy_, bstack1l1_opy_ (u"ࠫࡼ࠭Წ")) as f:
            json.dump(bstack11l1l1lll1l_opy_, f)
    except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡧࡵࡷ࡮ࡹࡴࡪࡰࡪࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡲࡼࡸࡪࡹࡴࠡࡧࡵࡶࡴࡸࡳ࠻ࠢࠪᲭ") + str(e))
def bstack11l1l1ll1l1_opy_(item, report, summary, bstack11l1l1l1lll_opy_):
    if report.when in [bstack1l1_opy_ (u"ࠨࡳࡦࡶࡸࡴࠧᲮ"), bstack1l1_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤᲯ")]:
        return
    if (str(bstack11l1l1l1lll_opy_).lower() != bstack1l1_opy_ (u"ࠨࡶࡵࡹࡪ࠭Ჰ")):
        bstack11l1l1l111_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1l1_opy_ (u"ࠤࡺࡥࡸࡾࡦࡢ࡫࡯ࠦᲱ")))
    bstack11lll11lll_opy_ = bstack1l1_opy_ (u"ࠥࠦᲲ")
    bstack1l1l11l1l1l_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack11lll11lll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack1l1_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥ࡬ࡡࡪ࡮ࡸࡶࡪࠦࡲࡦࡣࡶࡳࡳࡀࠠࡼ࠲ࢀࠦᲳ").format(e)
                )
        try:
            if passed:
                bstack11ll1l11l_opy_(getattr(item, bstack1l1_opy_ (u"ࠬࡥࡰࡢࡩࡨࠫᲴ"), None), bstack1l1_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨᲵ"))
            else:
                error_message = bstack1l1_opy_ (u"ࠧࠨᲶ")
                if bstack11lll11lll_opy_:
                    bstack11l11l1l11_opy_(item._page, str(bstack11lll11lll_opy_), bstack1l1_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢᲷ"))
                    bstack11ll1l11l_opy_(getattr(item, bstack1l1_opy_ (u"ࠩࡢࡴࡦ࡭ࡥࠨᲸ"), None), bstack1l1_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥᲹ"), str(bstack11lll11lll_opy_))
                    error_message = str(bstack11lll11lll_opy_)
                else:
                    bstack11ll1l11l_opy_(getattr(item, bstack1l1_opy_ (u"ࠫࡤࡶࡡࡨࡧࠪᲺ"), None), bstack1l1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ᲻"))
                bstack11l1ll1111l_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack1l1_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡺࡶࡤࡢࡶࡨࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࡻ࠱ࡿࠥ᲼").format(e))
try:
    from typing import Generator
    import pytest_playwright.pytest_playwright as p
    @pytest.fixture
    def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
        page = context.new_page()
        request.node._page = page
        yield page
except:
    pass
def pytest_addoption(parser):
    parser.addoption(bstack1l1_opy_ (u"ࠢ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦᲽ"), default=bstack1l1_opy_ (u"ࠣࡈࡤࡰࡸ࡫ࠢᲾ"), help=bstack1l1_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡧࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠣᲿ"))
    parser.addoption(bstack1l1_opy_ (u"ࠥ࠱࠲ࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤ᳀"), default=bstack1l1_opy_ (u"ࠦࡋࡧ࡬ࡴࡧࠥ᳁"), help=bstack1l1_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡯ࡣࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠦ᳂"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack1l1_opy_ (u"ࠨ࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠣ᳃"), action=bstack1l1_opy_ (u"ࠢࡴࡶࡲࡶࡪࠨ᳄"), default=bstack1l1_opy_ (u"ࠣࡥ࡫ࡶࡴࡳࡥࠣ᳅"),
                         help=bstack1l1_opy_ (u"ࠤࡇࡶ࡮ࡼࡥࡳࠢࡷࡳࠥࡸࡵ࡯ࠢࡷࡩࡸࡺࡳࠣ᳆"))
def bstack11ll1ll1_opy_(log):
    if not (log[bstack1l1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ᳇")] and log[bstack1l1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ᳈")].strip()):
        return
    active = bstack11llll1l_opy_()
    log = {
        bstack1l1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ᳉"): log[bstack1l1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ᳊")],
        bstack1l1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ᳋"): bstack1ll1l11l_opy_().isoformat() + bstack1l1_opy_ (u"ࠨ࡜ࠪ᳌"),
        bstack1l1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ᳍"): log[bstack1l1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ᳎")],
    }
    if active:
        if active[bstack1l1_opy_ (u"ࠫࡹࡿࡰࡦࠩ᳏")] == bstack1l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪ᳐"):
            log[bstack1l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭᳑")] = active[bstack1l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ᳒")]
        elif active[bstack1l1_opy_ (u"ࠨࡶࡼࡴࡪ࠭᳓")] == bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺ᳔ࠧ"):
            log[bstack1l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦ᳕ࠪ")] = active[bstack1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧ᳖ࠫ")]
    bstack1l1ll1l1_opy_.bstack1lll1111_opy_([log])
def bstack11llll1l_opy_():
    if len(store[bstack1l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥ᳗ࠩ")]) > 0 and store[bstack1l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦ᳘ࠪ")][-1]:
        return {
            bstack1l1_opy_ (u"ࠧࡵࡻࡳࡩ᳙ࠬ"): bstack1l1_opy_ (u"ࠨࡪࡲࡳࡰ࠭᳚"),
            bstack1l1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ᳛"): store[bstack1l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪ᳜ࠧ")][-1]
        }
    if store.get(bstack1l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨ᳝"), None):
        return {
            bstack1l1_opy_ (u"ࠬࡺࡹࡱࡧ᳞ࠪ"): bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷ᳟ࠫ"),
            bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ᳠"): store[bstack1l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ᳡")]
        }
    return None
def pytest_runtest_logstart(nodeid, location):
    if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
        cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.INIT_TEST, bstack1111l11l11_opy_.PRE, nodeid, location)
def pytest_runtest_logfinish(nodeid, location):
    if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
        cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.INIT_TEST, bstack1111l11l11_opy_.POST, nodeid, location)
def pytest_runtest_call(item):
    if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
        cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.TEST, bstack1111l11l11_opy_.PRE, item)
        return
    try:
        global CONFIG
        item._11l1l1llll1_opy_ = True
        bstack11l111llll_opy_ = bstack111l1ll1_opy_.bstack11l1lll1l_opy_(bstack1l1111l1111_opy_(item.own_markers))
        if not cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
            item._a11y_test_case = bstack11l111llll_opy_
            if bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ᳢"), None):
                driver = getattr(item, bstack1l1_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵ᳣ࠫ"), None)
                item._a11y_started = bstack111l1ll1_opy_.bstack111l1l111_opy_(driver, bstack11l111llll_opy_)
        if not bstack1l1ll1l1_opy_.on() or bstack11l1ll1lll1_opy_ != bstack1l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ᳤ࠫ"):
            return
        global current_test_uuid #, bstack1lll11ll_opy_
        bstack1l11l111_opy_ = {
            bstack1l1_opy_ (u"ࠬࡻࡵࡪࡦ᳥ࠪ"): uuid4().__str__(),
            bstack1l1_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶ᳦ࠪ"): bstack1ll1l11l_opy_().isoformat() + bstack1l1_opy_ (u"᳧࡛ࠧࠩ")
        }
        current_test_uuid = bstack1l11l111_opy_[bstack1l1_opy_ (u"ࠨࡷࡸ࡭ࡩ᳨࠭")]
        store[bstack1l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ᳩ")] = bstack1l11l111_opy_[bstack1l1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᳪ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _1l1l11l1_opy_[item.nodeid] = {**_1l1l11l1_opy_[item.nodeid], **bstack1l11l111_opy_}
        bstack11l1l1l11l1_opy_(item, _1l1l11l1_opy_[item.nodeid], bstack1l1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᳫ"))
    except Exception as err:
        print(bstack1l1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡷࡻ࡮ࡵࡧࡶࡸࡤࡩࡡ࡭࡮࠽ࠤࢀࢃࠧᳬ"), str(err))
def pytest_runtest_setup(item):
    store[bstack1l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯᳭ࠪ")] = item
    if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
        cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.BEFORE_EACH, bstack1111l11l11_opy_.PRE, item, bstack1l1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ᳮ"))
        return # skip all existing bstack11l1l1ll111_opy_
    global bstack11l1ll11111_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack1l11l1ll11l_opy_():
        atexit.register(bstack1l1ll1111l_opy_)
        if not bstack11l1ll11111_opy_:
            try:
                bstack11l1l1l1ll1_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack1l111l111l1_opy_():
                    bstack11l1l1l1ll1_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack11l1l1l1ll1_opy_:
                    signal.signal(s, bstack11l1ll111l1_opy_)
                bstack11l1ll11111_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack1l1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࠣࡶࡪ࡭ࡩࡴࡶࡨࡶࠥࡹࡩࡨࡰࡤࡰࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࡹ࠺ࠡࠤᳯ") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack1l1l111ll1l_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack1l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᳰ")
    try:
        if not bstack1l1ll1l1_opy_.on():
            return
        uuid = uuid4().__str__()
        bstack1l11l111_opy_ = {
            bstack1l1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᳱ"): uuid,
            bstack1l1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᳲ"): bstack1ll1l11l_opy_().isoformat() + bstack1l1_opy_ (u"ࠬࡠࠧᳳ"),
            bstack1l1_opy_ (u"࠭ࡴࡺࡲࡨࠫ᳴"): bstack1l1_opy_ (u"ࠧࡩࡱࡲ࡯ࠬᳵ"),
            bstack1l1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫᳶ"): bstack1l1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧ᳷"),
            bstack1l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪ࠭᳸"): bstack1l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ᳹")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack1l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩᳺ")] = item
        store[bstack1l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ᳻")] = [uuid]
        if not _1l1l11l1_opy_.get(item.nodeid, None):
            _1l1l11l1_opy_[item.nodeid] = {bstack1l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭᳼"): [], bstack1l1_opy_ (u"ࠨࡨ࡬ࡼࡹࡻࡲࡦࡵࠪ᳽"): []}
        _1l1l11l1_opy_[item.nodeid][bstack1l1_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ᳾")].append(bstack1l11l111_opy_[bstack1l1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ᳿")])
        _1l1l11l1_opy_[item.nodeid + bstack1l1_opy_ (u"ࠫ࠲ࡹࡥࡵࡷࡳࠫᴀ")] = bstack1l11l111_opy_
        bstack11l1l1l111l_opy_(item, bstack1l11l111_opy_, bstack1l1_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᴁ"))
    except Exception as err:
        print(bstack1l1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡸࡵ࡯ࡶࡨࡷࡹࡥࡳࡦࡶࡸࡴ࠿ࠦࡻࡾࠩᴂ"), str(err))
def pytest_runtest_teardown(item):
    if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
        cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.TEST, bstack1111l11l11_opy_.POST, item)
        cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.AFTER_EACH, bstack1111l11l11_opy_.PRE, item, bstack1l1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩᴃ"))
        return # skip all existing bstack11l1l1ll111_opy_
    try:
        global bstack1ll111111_opy_
        bstack11l111l1ll_opy_ = 0
        if bstack1ll11llll_opy_ is True:
            bstack11l111l1ll_opy_ = int(os.environ.get(bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᴄ")))
        if bstack11ll1lll11_opy_.bstack1l11lll111_opy_() == bstack1l1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᴅ"):
            if bstack11ll1lll11_opy_.bstack1lll11l11_opy_() == bstack1l1_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧᴆ"):
                bstack11l1l1l1111_opy_ = bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᴇ"), None)
                bstack111l111l1_opy_ = bstack11l1l1l1111_opy_ + bstack1l1_opy_ (u"ࠧ࠳ࡴࡦࡵࡷࡧࡦࡹࡥࠣᴈ")
                driver = getattr(item, bstack1l1_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧᴉ"), None)
                bstack1ll11ll1l1_opy_ = getattr(item, bstack1l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᴊ"), None)
                bstack1llll1111l_opy_ = getattr(item, bstack1l1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᴋ"), None)
                PercySDK.screenshot(driver, bstack111l111l1_opy_, bstack1ll11ll1l1_opy_=bstack1ll11ll1l1_opy_, bstack1llll1111l_opy_=bstack1llll1111l_opy_, bstack1l1l11l1l_opy_=bstack11l111l1ll_opy_)
        if not cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
            if getattr(item, bstack1l1_opy_ (u"ࠩࡢࡥ࠶࠷ࡹࡠࡵࡷࡥࡷࡺࡥࡥࠩᴌ"), False):
                bstack11l11111_opy_.bstack111l1111_opy_(getattr(item, bstack1l1_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫᴍ"), None), bstack1ll111111_opy_, logger, item)
        if not bstack1l1ll1l1_opy_.on():
            return
        bstack1l11l111_opy_ = {
            bstack1l1_opy_ (u"ࠫࡺࡻࡩࡥࠩᴎ"): uuid4().__str__(),
            bstack1l1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᴏ"): bstack1ll1l11l_opy_().isoformat() + bstack1l1_opy_ (u"࡚࠭ࠨᴐ"),
            bstack1l1_opy_ (u"ࠧࡵࡻࡳࡩࠬᴑ"): bstack1l1_opy_ (u"ࠨࡪࡲࡳࡰ࠭ᴒ"),
            bstack1l1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬᴓ"): bstack1l1_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡈࡅࡈࡎࠧᴔ"),
            bstack1l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡱࡥࡲ࡫ࠧᴕ"): bstack1l1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧᴖ")
        }
        _1l1l11l1_opy_[item.nodeid + bstack1l1_opy_ (u"࠭࠭ࡵࡧࡤࡶࡩࡵࡷ࡯ࠩᴗ")] = bstack1l11l111_opy_
        bstack11l1l1l111l_opy_(item, bstack1l11l111_opy_, bstack1l1_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨᴘ"))
    except Exception as err:
        print(bstack1l1_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡳࡷࡱࡸࡪࡹࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰ࠽ࠤࢀࢃࠧᴙ"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if bstack1l1l11l11l1_opy_(fixturedef.argname):
        store[bstack1l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡱࡴࡪࡵ࡭ࡧࡢ࡭ࡹ࡫࡭ࠨᴚ")] = request.node
    elif bstack1l1l111llll_opy_(fixturedef.argname):
        store[bstack1l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡨࡲࡡࡴࡵࡢ࡭ࡹ࡫࡭ࠨᴛ")] = request.node
    if not bstack1l1ll1l1_opy_.on():
        if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
            cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.SETUP_FIXTURE, bstack1111l11l11_opy_.PRE, fixturedef, request)
        outcome = yield
        if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
            cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.SETUP_FIXTURE, bstack1111l11l11_opy_.POST, fixturedef, request, outcome)
        return # skip all existing bstack11l1l1ll111_opy_
    start_time = datetime.datetime.now()
    if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
        cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.SETUP_FIXTURE, bstack1111l11l11_opy_.PRE, fixturedef, request)
    outcome = yield
    if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
        cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.SETUP_FIXTURE, bstack1111l11l11_opy_.POST, fixturedef, request, outcome)
        return # skip all existing bstack11l1l1ll111_opy_
    try:
        fixture = {
            bstack1l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᴜ"): fixturedef.argname,
            bstack1l1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᴝ"): bstack1l11ll11l11_opy_(outcome),
            bstack1l1_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨᴞ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack1l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫᴟ")]
        if not _1l1l11l1_opy_.get(current_test_item.nodeid, None):
            _1l1l11l1_opy_[current_test_item.nodeid] = {bstack1l1_opy_ (u"ࠨࡨ࡬ࡼࡹࡻࡲࡦࡵࠪᴠ"): []}
        _1l1l11l1_opy_[current_test_item.nodeid][bstack1l1_opy_ (u"ࠩࡩ࡭ࡽࡺࡵࡳࡧࡶࠫᴡ")].append(fixture)
    except Exception as err:
        logger.debug(bstack1l1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡷࡪࡺࡵࡱ࠼ࠣࡿࢂ࠭ᴢ"), str(err))
if bstack111lllll11_opy_() and bstack1l1ll1l1_opy_.on():
    def pytest_bdd_before_step(request, step):
        if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
            cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.STEP, bstack1111l11l11_opy_.PRE, request, step)
            return
        try:
            _1l1l11l1_opy_[request.node.nodeid][bstack1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᴣ")].bstack11ll11l1_opy_(id(step))
        except Exception as err:
            print(bstack1l1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࡀࠠࡼࡿࠪᴤ"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
            cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.STEP, bstack1111l11l11_opy_.POST, request, step, exception)
            return
        try:
            _1l1l11l1_opy_[request.node.nodeid][bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩᴥ")].bstack1l111l11_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack1l1_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡷࡹ࡫ࡰࡠࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠫᴦ"), str(err))
    def pytest_bdd_after_step(request, step):
        if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
            cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.STEP, bstack1111l11l11_opy_.POST, request, step)
            return
        try:
            bstack1l1ll1ll_opy_: bstack11llllll_opy_ = _1l1l11l1_opy_[request.node.nodeid][bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫᴧ")]
            bstack1l1ll1ll_opy_.bstack1l111l11_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack1l1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤࡹࡴࡦࡲࡢࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂ࠭ᴨ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack11l1ll1lll1_opy_
        try:
            if not bstack1l1ll1l1_opy_.on() or bstack11l1ll1lll1_opy_ != bstack1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠧᴩ"):
                return
            if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
                cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.TEST, bstack1111l11l11_opy_.PRE, request, feature, scenario)
                return
            driver = bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪᴪ"), None)
            if not _1l1l11l1_opy_.get(request.node.nodeid, None):
                _1l1l11l1_opy_[request.node.nodeid] = {}
            bstack1l1ll1ll_opy_ = bstack11llllll_opy_.bstack11llll11ll1_opy_(
                scenario, feature, request.node,
                name=bstack1l1l111l1l1_opy_(request.node, scenario),
                started_at=bstack1l111ll1_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack1l1_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸ࠲ࡩࡵࡤࡷࡰࡦࡪࡸࠧᴫ"),
                tags=bstack1l1l111l1ll_opy_(feature, scenario),
                bstack1ll1llll_opy_=bstack1l1ll1l1_opy_.bstack1llll11l_opy_(driver) if driver and driver.session_id else {}
            )
            _1l1l11l1_opy_[request.node.nodeid][bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩᴬ")] = bstack1l1ll1ll_opy_
            bstack11l1l1lll11_opy_(bstack1l1ll1ll_opy_.uuid)
            bstack1l1ll1l1_opy_.bstack1l11ll11_opy_(bstack1l1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨᴭ"), bstack1l1ll1ll_opy_)
        except Exception as err:
            print(bstack1l1_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࡀࠠࡼࡿࠪᴮ"), str(err))
def bstack11l1ll1l1ll_opy_(bstack11l1llll_opy_):
    if bstack11l1llll_opy_ in store[bstack1l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᴯ")]:
        store[bstack1l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᴰ")].remove(bstack11l1llll_opy_)
def bstack11l1l1lll11_opy_(test_uuid):
    store[bstack1l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᴱ")] = test_uuid
    threading.current_thread().current_test_uuid = test_uuid
@bstack1l1ll1l1_opy_.bstack11ll111l1ll_opy_
def bstack11l1l1l11ll_opy_(item, call, report):
    global bstack11l1ll1lll1_opy_
    bstack11l11l111l_opy_ = bstack1l111ll1_opy_()
    if hasattr(report, bstack1l1_opy_ (u"ࠬࡹࡴࡰࡲࠪᴲ")):
        bstack11l11l111l_opy_ = bstack1l1111lll11_opy_(report.stop)
    elif hasattr(report, bstack1l1_opy_ (u"࠭ࡳࡵࡣࡵࡸࠬᴳ")):
        bstack11l11l111l_opy_ = bstack1l1111lll11_opy_(report.start)
    try:
        if getattr(report, bstack1l1_opy_ (u"ࠧࡸࡪࡨࡲࠬᴴ"), bstack1l1_opy_ (u"ࠨࠩᴵ")) == bstack1l1_opy_ (u"ࠩࡦࡥࡱࡲࠧᴶ"):
            if bstack11l1ll1lll1_opy_ == bstack1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᴷ"):
                _1l1l11l1_opy_[item.nodeid][bstack1l1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᴸ")] = bstack11l11l111l_opy_
                bstack11l1l1l11l1_opy_(item, _1l1l11l1_opy_[item.nodeid], bstack1l1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᴹ"), report, call)
                store[bstack1l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪᴺ")] = None
            elif bstack11l1ll1lll1_opy_ == bstack1l1_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦᴻ"):
                bstack1l1ll1ll_opy_ = _1l1l11l1_opy_[item.nodeid][bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫᴼ")]
                bstack1l1ll1ll_opy_.set(hooks=_1l1l11l1_opy_[item.nodeid].get(bstack1l1_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᴽ"), []))
                exception, bstack11lll111_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack11lll111_opy_ = [call.excinfo.exconly(), getattr(report, bstack1l1_opy_ (u"ࠪࡰࡴࡴࡧࡳࡧࡳࡶࡹ࡫ࡸࡵࠩᴾ"), bstack1l1_opy_ (u"ࠫࠬᴿ"))]
                bstack1l1ll1ll_opy_.stop(time=bstack11l11l111l_opy_, result=Result(result=getattr(report, bstack1l1_opy_ (u"ࠬࡵࡵࡵࡥࡲࡱࡪ࠭ᵀ"), bstack1l1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᵁ")), exception=exception, bstack11lll111_opy_=bstack11lll111_opy_))
                bstack1l1ll1l1_opy_.bstack1l11ll11_opy_(bstack1l1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᵂ"), _1l1l11l1_opy_[item.nodeid][bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫᵃ")])
        elif getattr(report, bstack1l1_opy_ (u"ࠩࡺ࡬ࡪࡴࠧᵄ"), bstack1l1_opy_ (u"ࠪࠫᵅ")) in [bstack1l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪᵆ"), bstack1l1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧᵇ")]:
            bstack1l11l1ll_opy_ = item.nodeid + bstack1l1_opy_ (u"࠭࠭ࠨᵈ") + getattr(report, bstack1l1_opy_ (u"ࠧࡸࡪࡨࡲࠬᵉ"), bstack1l1_opy_ (u"ࠨࠩᵊ"))
            if getattr(report, bstack1l1_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪᵋ"), False):
                hook_type = bstack1l1_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨᵌ") if getattr(report, bstack1l1_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩᵍ"), bstack1l1_opy_ (u"ࠬ࠭ᵎ")) == bstack1l1_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬᵏ") else bstack1l1_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫᵐ")
                _1l1l11l1_opy_[bstack1l11l1ll_opy_] = {
                    bstack1l1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᵑ"): uuid4().__str__(),
                    bstack1l1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᵒ"): bstack11l11l111l_opy_,
                    bstack1l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ᵓ"): hook_type
                }
            _1l1l11l1_opy_[bstack1l11l1ll_opy_][bstack1l1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᵔ")] = bstack11l11l111l_opy_
            bstack11l1ll1l1ll_opy_(_1l1l11l1_opy_[bstack1l11l1ll_opy_][bstack1l1_opy_ (u"ࠬࡻࡵࡪࡦࠪᵕ")])
            bstack11l1l1l111l_opy_(item, _1l1l11l1_opy_[bstack1l11l1ll_opy_], bstack1l1_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨᵖ"), report, call)
            if getattr(report, bstack1l1_opy_ (u"ࠧࡸࡪࡨࡲࠬᵗ"), bstack1l1_opy_ (u"ࠨࠩᵘ")) == bstack1l1_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨᵙ"):
                if getattr(report, bstack1l1_opy_ (u"ࠪࡳࡺࡺࡣࡰ࡯ࡨࠫᵚ"), bstack1l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᵛ")) == bstack1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᵜ"):
                    bstack1l11l111_opy_ = {
                        bstack1l1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᵝ"): uuid4().__str__(),
                        bstack1l1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᵞ"): bstack1l111ll1_opy_(),
                        bstack1l1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᵟ"): bstack1l111ll1_opy_()
                    }
                    _1l1l11l1_opy_[item.nodeid] = {**_1l1l11l1_opy_[item.nodeid], **bstack1l11l111_opy_}
                    bstack11l1l1l11l1_opy_(item, _1l1l11l1_opy_[item.nodeid], bstack1l1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᵠ"))
                    bstack11l1l1l11l1_opy_(item, _1l1l11l1_opy_[item.nodeid], bstack1l1_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᵡ"), report, call)
    except Exception as err:
        print(bstack1l1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡦࡴࡤ࡭ࡧࡢࡳ࠶࠷ࡹࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸ࠿ࠦࡻࡾࠩᵢ"), str(err))
def bstack11l1ll11l11_opy_(test, bstack1l11l111_opy_, result=None, call=None, bstack1l1l11lll_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack1l1ll1ll_opy_ = {
        bstack1l1_opy_ (u"ࠬࡻࡵࡪࡦࠪᵣ"): bstack1l11l111_opy_[bstack1l1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᵤ")],
        bstack1l1_opy_ (u"ࠧࡵࡻࡳࡩࠬᵥ"): bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹ࠭ᵦ"),
        bstack1l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᵧ"): test.name,
        bstack1l1_opy_ (u"ࠪࡦࡴࡪࡹࠨᵨ"): {
            bstack1l1_opy_ (u"ࠫࡱࡧ࡮ࡨࠩᵩ"): bstack1l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬᵪ"),
            bstack1l1_opy_ (u"࠭ࡣࡰࡦࡨࠫᵫ"): inspect.getsource(test.obj)
        },
        bstack1l1_opy_ (u"ࠧࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᵬ"): test.name,
        bstack1l1_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࠧᵭ"): test.name,
        bstack1l1_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩᵮ"): bstack1llll1l1_opy_.bstack1l1llll1_opy_(test),
        bstack1l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ᵯ"): file_path,
        bstack1l1_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࠭ᵰ"): file_path,
        bstack1l1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᵱ"): bstack1l1_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧᵲ"),
        bstack1l1_opy_ (u"ࠧࡷࡥࡢࡪ࡮ࡲࡥࡱࡣࡷ࡬ࠬᵳ"): file_path,
        bstack1l1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᵴ"): bstack1l11l111_opy_[bstack1l1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᵵ")],
        bstack1l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ᵶ"): bstack1l1_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷࠫᵷ"),
        bstack1l1_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡗ࡫ࡲࡶࡰࡓࡥࡷࡧ࡭ࠨᵸ"): {
            bstack1l1_opy_ (u"࠭ࡲࡦࡴࡸࡲࡤࡴࡡ࡮ࡧࠪᵹ"): test.nodeid
        },
        bstack1l1_opy_ (u"ࠧࡵࡣࡪࡷࠬᵺ"): bstack1l1111l1111_opy_(test.own_markers)
    }
    if bstack1l1l11lll_opy_ in [bstack1l1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩᵻ"), bstack1l1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᵼ")]:
        bstack1l1ll1ll_opy_[bstack1l1_opy_ (u"ࠪࡱࡪࡺࡡࠨᵽ")] = {
            bstack1l1_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭ᵾ"): bstack1l11l111_opy_.get(bstack1l1_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧᵿ"), [])
        }
    if bstack1l1l11lll_opy_ == bstack1l1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧᶀ"):
        bstack1l1ll1ll_opy_[bstack1l1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᶁ")] = bstack1l1_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᶂ")
        bstack1l1ll1ll_opy_[bstack1l1_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᶃ")] = bstack1l11l111_opy_[bstack1l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᶄ")]
        bstack1l1ll1ll_opy_[bstack1l1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᶅ")] = bstack1l11l111_opy_[bstack1l1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᶆ")]
    if result:
        bstack1l1ll1ll_opy_[bstack1l1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᶇ")] = result.outcome
        bstack1l1ll1ll_opy_[bstack1l1_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨᶈ")] = result.duration * 1000
        bstack1l1ll1ll_opy_[bstack1l1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᶉ")] = bstack1l11l111_opy_[bstack1l1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᶊ")]
        if result.failed:
            bstack1l1ll1ll_opy_[bstack1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩᶋ")] = bstack1l1ll1l1_opy_.bstack111llll11l_opy_(call.excinfo.typename)
            bstack1l1ll1ll_opy_[bstack1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬᶌ")] = bstack1l1ll1l1_opy_.bstack11ll111l11l_opy_(call.excinfo, result)
        bstack1l1ll1ll_opy_[bstack1l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᶍ")] = bstack1l11l111_opy_[bstack1l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᶎ")]
    if outcome:
        bstack1l1ll1ll_opy_[bstack1l1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᶏ")] = bstack1l11ll11l11_opy_(outcome)
        bstack1l1ll1ll_opy_[bstack1l1_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩᶐ")] = 0
        bstack1l1ll1ll_opy_[bstack1l1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᶑ")] = bstack1l11l111_opy_[bstack1l1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᶒ")]
        if bstack1l1ll1ll_opy_[bstack1l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᶓ")] == bstack1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᶔ"):
            bstack1l1ll1ll_opy_[bstack1l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬᶕ")] = bstack1l1_opy_ (u"ࠧࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠨᶖ")  # bstack11l1ll1l11l_opy_
            bstack1l1ll1ll_opy_[bstack1l1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩᶗ")] = [{bstack1l1_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬᶘ"): [bstack1l1_opy_ (u"ࠪࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠧᶙ")]}]
        bstack1l1ll1ll_opy_[bstack1l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪᶚ")] = bstack1l11l111_opy_[bstack1l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᶛ")]
    return bstack1l1ll1ll_opy_
def bstack11l1ll1ll1l_opy_(test, bstack11lll1ll_opy_, bstack1l1l11lll_opy_, result, call, outcome, bstack11l1l1ll11l_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack11lll1ll_opy_[bstack1l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩᶜ")]
    hook_name = bstack11lll1ll_opy_[bstack1l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡴࡡ࡮ࡧࠪᶝ")]
    hook_data = {
        bstack1l1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᶞ"): bstack11lll1ll_opy_[bstack1l1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᶟ")],
        bstack1l1_opy_ (u"ࠪࡸࡾࡶࡥࠨᶠ"): bstack1l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩᶡ"),
        bstack1l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᶢ"): bstack1l1_opy_ (u"࠭ࡻࡾࠩᶣ").format(bstack1l1l111ll11_opy_(hook_name)),
        bstack1l1_opy_ (u"ࠧࡣࡱࡧࡽࠬᶤ"): {
            bstack1l1_opy_ (u"ࠨ࡮ࡤࡲ࡬࠭ᶥ"): bstack1l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩᶦ"),
            bstack1l1_opy_ (u"ࠪࡧࡴࡪࡥࠨᶧ"): None
        },
        bstack1l1_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࠪᶨ"): test.name,
        bstack1l1_opy_ (u"ࠬࡹࡣࡰࡲࡨࡷࠬᶩ"): bstack1llll1l1_opy_.bstack1l1llll1_opy_(test, hook_name),
        bstack1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩᶪ"): file_path,
        bstack1l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠩᶫ"): file_path,
        bstack1l1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᶬ"): bstack1l1_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪᶭ"),
        bstack1l1_opy_ (u"ࠪࡺࡨࡥࡦࡪ࡮ࡨࡴࡦࡺࡨࠨᶮ"): file_path,
        bstack1l1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᶯ"): bstack11lll1ll_opy_[bstack1l1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᶰ")],
        bstack1l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩᶱ"): bstack1l1_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺ࠭ࡤࡷࡦࡹࡲࡨࡥࡳࠩᶲ") if bstack11l1ll1lll1_opy_ == bstack1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬᶳ") else bstack1l1_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵࠩᶴ"),
        bstack1l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ᶵ"): hook_type
    }
    bstack11llll11l1l_opy_ = bstack11lllll1_opy_(_1l1l11l1_opy_.get(test.nodeid, None))
    if bstack11llll11l1l_opy_:
        hook_data[bstack1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡩࡥࠩᶶ")] = bstack11llll11l1l_opy_
    if result:
        hook_data[bstack1l1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᶷ")] = result.outcome
        hook_data[bstack1l1_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧᶸ")] = result.duration * 1000
        hook_data[bstack1l1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᶹ")] = bstack11lll1ll_opy_[bstack1l1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᶺ")]
        if result.failed:
            hook_data[bstack1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨᶻ")] = bstack1l1ll1l1_opy_.bstack111llll11l_opy_(call.excinfo.typename)
            hook_data[bstack1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫᶼ")] = bstack1l1ll1l1_opy_.bstack11ll111l11l_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack1l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᶽ")] = bstack1l11ll11l11_opy_(outcome)
        hook_data[bstack1l1_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭ᶾ")] = 100
        hook_data[bstack1l1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᶿ")] = bstack11lll1ll_opy_[bstack1l1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ᷀")]
        if hook_data[bstack1l1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ᷁")] == bstack1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥ᷂ࠩ"):
            hook_data[bstack1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩ᷃")] = bstack1l1_opy_ (u"࡚ࠫࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠬ᷄")  # bstack11l1ll1l11l_opy_
            hook_data[bstack1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭᷅")] = [{bstack1l1_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩ᷆"): [bstack1l1_opy_ (u"ࠧࡴࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠫ᷇")]}]
    if bstack11l1l1ll11l_opy_:
        hook_data[bstack1l1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ᷈")] = bstack11l1l1ll11l_opy_.result
        hook_data[bstack1l1_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪ᷉")] = bstack1l111l1ll1l_opy_(bstack11lll1ll_opy_[bstack1l1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺ᷊ࠧ")], bstack11lll1ll_opy_[bstack1l1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ᷋")])
        hook_data[bstack1l1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ᷌")] = bstack11lll1ll_opy_[bstack1l1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ᷍")]
        if hook_data[bstack1l1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺ᷎ࠧ")] == bstack1l1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ᷏"):
            hook_data[bstack1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨ᷐")] = bstack1l1ll1l1_opy_.bstack111llll11l_opy_(bstack11l1l1ll11l_opy_.exception_type)
            hook_data[bstack1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫ᷑")] = [{bstack1l1_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧ᷒"): bstack1l11l1l1ll1_opy_(bstack11l1l1ll11l_opy_.exception)}]
    return hook_data
def bstack11l1l1l11l1_opy_(test, bstack1l11l111_opy_, bstack1l1l11lll_opy_, result=None, call=None, outcome=None):
    bstack1l1ll1ll_opy_ = bstack11l1ll11l11_opy_(test, bstack1l11l111_opy_, result, call, bstack1l1l11lll_opy_, outcome)
    driver = getattr(test, bstack1l1_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭ᷓ"), None)
    if bstack1l1l11lll_opy_ == bstack1l1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᷔ") and driver:
        bstack1l1ll1ll_opy_[bstack1l1_opy_ (u"ࠧࡪࡰࡷࡩ࡬ࡸࡡࡵ࡫ࡲࡲࡸ࠭ᷕ")] = bstack1l1ll1l1_opy_.bstack1llll11l_opy_(driver)
    if bstack1l1l11lll_opy_ == bstack1l1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩᷖ"):
        bstack1l1l11lll_opy_ = bstack1l1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᷗ")
    bstack1l1111l1_opy_ = {
        bstack1l1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧᷘ"): bstack1l1l11lll_opy_,
        bstack1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭ᷙ"): bstack1l1ll1ll_opy_
    }
    bstack1l1ll1l1_opy_.bstack1ll1l111_opy_(bstack1l1111l1_opy_)
    if bstack1l1l11lll_opy_ == bstack1l1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᷚ"):
        threading.current_thread().bstackTestMeta = {bstack1l1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ᷛ"): bstack1l1_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨᷜ")}
    elif bstack1l1l11lll_opy_ == bstack1l1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᷝ"):
        threading.current_thread().bstackTestMeta = {bstack1l1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᷞ"): getattr(result, bstack1l1_opy_ (u"ࠪࡳࡺࡺࡣࡰ࡯ࡨࠫᷟ"), bstack1l1_opy_ (u"ࠫࠬᷠ"))}
def bstack11l1l1l111l_opy_(test, bstack1l11l111_opy_, bstack1l1l11lll_opy_, result=None, call=None, outcome=None, bstack11l1l1ll11l_opy_=None):
    hook_data = bstack11l1ll1ll1l_opy_(test, bstack1l11l111_opy_, bstack1l1l11lll_opy_, result, call, outcome, bstack11l1l1ll11l_opy_)
    bstack1l1111l1_opy_ = {
        bstack1l1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩᷡ"): bstack1l1l11lll_opy_,
        bstack1l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࠨᷢ"): hook_data
    }
    bstack1l1ll1l1_opy_.bstack1ll1l111_opy_(bstack1l1111l1_opy_)
def bstack11lllll1_opy_(bstack1l11l111_opy_):
    if not bstack1l11l111_opy_:
        return None
    if bstack1l11l111_opy_.get(bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᷣ"), None):
        return getattr(bstack1l11l111_opy_[bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫᷤ")], bstack1l1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᷥ"), None)
    return bstack1l11l111_opy_.get(bstack1l1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᷦ"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
        cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.LOG, bstack1111l11l11_opy_.PRE, request, caplog)
    yield
    if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
        cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_.LOG, bstack1111l11l11_opy_.POST, request, caplog)
        return # skip all existing bstack11l1l1ll111_opy_
    try:
        if not bstack1l1ll1l1_opy_.on():
            return
        places = [bstack1l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪᷧ"), bstack1l1_opy_ (u"ࠬࡩࡡ࡭࡮ࠪᷨ"), bstack1l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨᷩ")]
        logs = []
        for bstack11l1ll11lll_opy_ in places:
            records = caplog.get_records(bstack11l1ll11lll_opy_)
            bstack11l1ll111ll_opy_ = bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᷪ") if bstack11l1ll11lll_opy_ == bstack1l1_opy_ (u"ࠨࡥࡤࡰࡱ࠭ᷫ") else bstack1l1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᷬ")
            bstack11l1l1lllll_opy_ = request.node.nodeid + (bstack1l1_opy_ (u"ࠪࠫᷭ") if bstack11l1ll11lll_opy_ == bstack1l1_opy_ (u"ࠫࡨࡧ࡬࡭ࠩᷮ") else bstack1l1_opy_ (u"ࠬ࠳ࠧᷯ") + bstack11l1ll11lll_opy_)
            test_uuid = bstack11lllll1_opy_(_1l1l11l1_opy_.get(bstack11l1l1lllll_opy_, None))
            if not test_uuid:
                continue
            for record in records:
                if bstack1l111llll11_opy_(record.message):
                    continue
                logs.append({
                    bstack1l1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩᷰ"): bstack1l111lll11l_opy_(record.created).isoformat() + bstack1l1_opy_ (u"࡛ࠧࠩᷱ"),
                    bstack1l1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᷲ"): record.levelname,
                    bstack1l1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᷳ"): record.message,
                    bstack11l1ll111ll_opy_: test_uuid
                })
        if len(logs) > 0:
            bstack1l1ll1l1_opy_.bstack1lll1111_opy_(logs)
    except Exception as err:
        print(bstack1l1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡨࡵ࡮ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧ࠽ࠤࢀࢃࠧᷴ"), str(err))
def bstack1l1l11l11_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack1l1111lll_opy_
    bstack11l11ll111_opy_ = bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ᷵"), None) and bstack1l1111ll_opy_(
            threading.current_thread(), bstack1l1_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ᷶"), None)
    bstack1l111l111l_opy_ = getattr(driver, bstack1l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ᷷࠭"), None) != None and getattr(driver, bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴ᷸ࠧ"), None) == True
    if sequence == bstack1l1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨ᷹") and driver != None:
      if not bstack1l1111lll_opy_ and bstack1ll11l11111_opy_() and bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺ᷺ࠩ") in CONFIG and CONFIG[bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ᷻")] == True and bstack11ll111lll_opy_.bstack1lll11l1l1_opy_(driver_command) and (bstack1l111l111l_opy_ or bstack11l11ll111_opy_) and not bstack1ll1l11l1_opy_(args):
        try:
          bstack1l1111lll_opy_ = True
          logger.debug(bstack1l1_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡦࡰࡴࠣࡿࢂ࠭᷼").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack1l1_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡨࡶ࡫ࡵࡲ࡮ࠢࡶࡧࡦࡴࠠࡼࡿ᷽ࠪ").format(str(err)))
        bstack1l1111lll_opy_ = False
    if sequence == bstack1l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬ᷾"):
        if driver_command == bstack1l1_opy_ (u"ࠧࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷ᷿ࠫ"):
            bstack1l1ll1l1_opy_.bstack1l1ll1l11_opy_({
                bstack1l1_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ࠧḀ"): response[bstack1l1_opy_ (u"ࠩࡹࡥࡱࡻࡥࠨḁ")],
                bstack1l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪḂ"): store[bstack1l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨḃ")]
            })
def bstack1l1ll1111l_opy_():
    global bstack1l1ll1ll1l_opy_
    bstack11ll11llll_opy_.bstack1l111l1ll_opy_()
    logging.shutdown()
    bstack1l1ll1l1_opy_.bstack1l1l1ll1_opy_()
    for driver in bstack1l1ll1ll1l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack11l1ll111l1_opy_(*args):
    global bstack1l1ll1ll1l_opy_
    bstack1l1ll1l1_opy_.bstack1l1l1ll1_opy_()
    for driver in bstack1l1ll1ll1l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack11l1l1lll_opy_(self, *args, **kwargs):
    bstack111111111_opy_ = bstack1l111111ll_opy_(self, *args, **kwargs)
    bstack11lllll11_opy_ = getattr(threading.current_thread(), bstack1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࡙࡫ࡳࡵࡏࡨࡸࡦ࠭Ḅ"), None)
    if bstack11lllll11_opy_ and bstack11lllll11_opy_.get(bstack1l1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ḅ"), bstack1l1_opy_ (u"ࠧࠨḆ")) == bstack1l1_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩḇ"):
        bstack1l1ll1l1_opy_.bstack1ll1l111l_opy_(self)
    return bstack111111111_opy_
def bstack11ll1l1ll1_opy_(framework_name):
    from bstack_utils.config import Config
    bstack111l11ll_opy_ = Config.bstack11l111ll_opy_()
    if bstack111l11ll_opy_.get_property(bstack1l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡰࡳࡩࡥࡣࡢ࡮࡯ࡩࡩ࠭Ḉ")):
        return
    bstack111l11ll_opy_.set_property(bstack1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡱࡴࡪ࡟ࡤࡣ࡯ࡰࡪࡪࠧḉ"), True)
    global bstack11lll1l1ll_opy_
    global bstack1lll11111_opy_
    bstack11lll1l1ll_opy_ = framework_name
    logger.info(bstack1l1l11l111_opy_.format(bstack11lll1l1ll_opy_.split(bstack1l1_opy_ (u"ࠫ࠲࠭Ḋ"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1ll11l11111_opy_():
            Service.start = bstack1lll1111l1_opy_
            Service.stop = bstack1ll11l1l11_opy_
            webdriver.Remote.get = bstack1lll1lll1_opy_
            webdriver.Remote.__init__ = bstack1ll111ll11_opy_
            if not isinstance(os.getenv(bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡇࡒࡂࡎࡏࡉࡑ࠭ḋ")), str):
                return
            WebDriver.close = bstack1111llll1_opy_
            WebDriver.quit = bstack1l1l11ll1l_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        elif bstack1l1ll1l1_opy_.on():
            webdriver.Remote.__init__ = bstack11l1l1lll_opy_
        bstack1lll11111_opy_ = True
    except Exception as e:
        pass
    bstack11l1lll1l1_opy_()
    if os.environ.get(bstack1l1_opy_ (u"࠭ࡓࡆࡎࡈࡒࡎ࡛ࡍࡠࡑࡕࡣࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡋࡑࡗ࡙ࡇࡌࡍࡇࡇࠫḌ")):
        bstack1lll11111_opy_ = eval(os.environ.get(bstack1l1_opy_ (u"ࠧࡔࡇࡏࡉࡓࡏࡕࡎࡡࡒࡖࡤࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡌࡒࡘ࡚ࡁࡍࡎࡈࡈࠬḍ")))
    if not bstack1lll11111_opy_:
        bstack1l1l1lll1l_opy_(bstack1l1_opy_ (u"ࠣࡒࡤࡧࡰࡧࡧࡦࡵࠣࡲࡴࡺࠠࡪࡰࡶࡸࡦࡲ࡬ࡦࡦࠥḎ"), bstack1lll1111ll_opy_)
    if bstack1l1l11l11l_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._11l1l111ll_opy_ = bstack11l11llll1_opy_
        except Exception as e:
            logger.error(bstack11111lll1_opy_.format(str(e)))
    if bstack1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩḏ") in str(framework_name).lower():
        if not bstack1ll11l11111_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack11l11ll1ll_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack111lll11l_opy_
            Config.getoption = bstack11l1llll11_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack11l1l1lll1_opy_
        except Exception as e:
            pass
def bstack1l1l11ll1l_opy_(self):
    global bstack11lll1l1ll_opy_
    global bstack1ll1l1111_opy_
    global bstack1lll1ll1ll_opy_
    try:
        if bstack1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪḐ") in bstack11lll1l1ll_opy_ and self.session_id != None and bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡕࡷࡥࡹࡻࡳࠨḑ"), bstack1l1_opy_ (u"ࠬ࠭Ḓ")) != bstack1l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧḓ"):
            bstack1lll1l1l1l_opy_ = bstack1l1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧḔ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1l1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨḕ")
            bstack1l111l111_opy_(logger, True)
            if self != None:
                bstack1l1lll1lll_opy_(self, bstack1lll1l1l1l_opy_, bstack1l1_opy_ (u"ࠩ࠯ࠤࠬḖ").join(threading.current_thread().bstackTestErrorMessages))
        if not cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
            item = store.get(bstack1l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧḗ"), None)
            if item is not None and bstack1l1111ll_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪḘ"), None):
                bstack11l11111_opy_.bstack111l1111_opy_(self, bstack1ll111111_opy_, logger, item)
        threading.current_thread().testStatus = bstack1l1_opy_ (u"ࠬ࠭ḙ")
    except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࠢḚ") + str(e))
    bstack1lll1ll1ll_opy_(self)
    self.session_id = None
def bstack1ll111ll11_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1ll1l1111_opy_
    global bstack1l1lll111l_opy_
    global bstack1ll11llll_opy_
    global bstack11lll1l1ll_opy_
    global bstack1l111111ll_opy_
    global bstack1l1ll1ll1l_opy_
    global bstack11ll1ll111_opy_
    global bstack1ll1ll11l_opy_
    global bstack1ll111111_opy_
    CONFIG[bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩḛ")] = str(bstack11lll1l1ll_opy_) + str(__version__)
    command_executor = bstack1ll1ll11l1_opy_(bstack11ll1ll111_opy_, CONFIG)
    logger.debug(bstack1lll1ll1l_opy_.format(command_executor))
    proxy = bstack1l11l11l1l_opy_(CONFIG, proxy)
    bstack11l111l1ll_opy_ = 0
    try:
        if bstack1ll11llll_opy_ is True:
            bstack11l111l1ll_opy_ = int(os.environ.get(bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨḜ")))
    except:
        bstack11l111l1ll_opy_ = 0
    bstack1llll1l111_opy_ = bstack11lll1ll1l_opy_(CONFIG, bstack11l111l1ll_opy_)
    logger.debug(bstack11lll1ll11_opy_.format(str(bstack1llll1l111_opy_)))
    bstack1ll111111_opy_ = CONFIG.get(bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬḝ"))[bstack11l111l1ll_opy_]
    if bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧḞ") in CONFIG and CONFIG[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨḟ")]:
        bstack1l1l1l1lll_opy_(bstack1llll1l111_opy_, bstack1ll1ll11l_opy_)
    if bstack111l1ll1_opy_.bstack1llll1llll_opy_(CONFIG, bstack11l111l1ll_opy_) and bstack111l1ll1_opy_.bstack1ll1111ll_opy_(bstack1llll1l111_opy_, options, desired_capabilities):
        threading.current_thread().a11yPlatform = True
        if not cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
            bstack111l1ll1_opy_.set_capabilities(bstack1llll1l111_opy_, CONFIG)
    if desired_capabilities:
        bstack11l111l11_opy_ = bstack1l1l1111l_opy_(desired_capabilities)
        bstack11l111l11_opy_[bstack1l1_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬḠ")] = bstack11llllll11_opy_(CONFIG)
        bstack1ll11l11ll_opy_ = bstack11lll1ll1l_opy_(bstack11l111l11_opy_)
        if bstack1ll11l11ll_opy_:
            bstack1llll1l111_opy_ = update(bstack1ll11l11ll_opy_, bstack1llll1l111_opy_)
        desired_capabilities = None
    if options:
        bstack1l11lllll_opy_(options, bstack1llll1l111_opy_)
    if not options:
        options = bstack1ll1ll111_opy_(bstack1llll1l111_opy_)
    if proxy and bstack1lll1lll11_opy_() >= version.parse(bstack1l1_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭ḡ")):
        options.proxy(proxy)
    if options and bstack1lll1lll11_opy_() >= version.parse(bstack1l1_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭Ḣ")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1lll1lll11_opy_() < version.parse(bstack1l1_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧḣ")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack1llll1l111_opy_)
    logger.info(bstack1ll11lll1_opy_)
    if bstack1lll1lll11_opy_() >= version.parse(bstack1l1_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩḤ")):
        bstack1l111111ll_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1lll1lll11_opy_() >= version.parse(bstack1l1_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩḥ")):
        bstack1l111111ll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1lll1lll11_opy_() >= version.parse(bstack1l1_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫḦ")):
        bstack1l111111ll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    else:
        bstack1l111111ll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive)
    try:
        bstack1l11ll111_opy_ = bstack1l1_opy_ (u"ࠬ࠭ḧ")
        if bstack1lll1lll11_opy_() >= version.parse(bstack1l1_opy_ (u"࠭࠴࠯࠲࠱࠴ࡧ࠷ࠧḨ")):
            bstack1l11ll111_opy_ = self.caps.get(bstack1l1_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢḩ"))
        else:
            bstack1l11ll111_opy_ = self.capabilities.get(bstack1l1_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣḪ"))
        if bstack1l11ll111_opy_:
            bstack1l1l111111_opy_(bstack1l11ll111_opy_)
            if bstack1lll1lll11_opy_() <= version.parse(bstack1l1_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩḫ")):
                self.command_executor._url = bstack1l1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦḬ") + bstack11ll1ll111_opy_ + bstack1l1_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣḭ")
            else:
                self.command_executor._url = bstack1l1_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢḮ") + bstack1l11ll111_opy_ + bstack1l1_opy_ (u"ࠨ࠯ࡸࡦ࠲࡬ࡺࡨࠢḯ")
            logger.debug(bstack1ll1l1lll_opy_.format(bstack1l11ll111_opy_))
        else:
            logger.debug(bstack1llll111l_opy_.format(bstack1l1_opy_ (u"ࠢࡐࡲࡷ࡭ࡲࡧ࡬ࠡࡊࡸࡦࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤࠣḰ")))
    except Exception as e:
        logger.debug(bstack1llll111l_opy_.format(e))
    bstack1ll1l1111_opy_ = self.session_id
    if bstack1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨḱ") in bstack11lll1l1ll_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack1l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭Ḳ"), None)
        if item:
            bstack11l1ll11l1l_opy_ = getattr(item, bstack1l1_opy_ (u"ࠪࡣࡹ࡫ࡳࡵࡡࡦࡥࡸ࡫࡟ࡴࡶࡤࡶࡹ࡫ࡤࠨḳ"), False)
            if not getattr(item, bstack1l1_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬḴ"), None) and bstack11l1ll11l1l_opy_:
                setattr(store[bstack1l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩḵ")], bstack1l1_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧḶ"), self)
        bstack11lllll11_opy_ = getattr(threading.current_thread(), bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡔࡦࡵࡷࡑࡪࡺࡡࠨḷ"), None)
        if bstack11lllll11_opy_ and bstack11lllll11_opy_.get(bstack1l1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨḸ"), bstack1l1_opy_ (u"ࠩࠪḹ")) == bstack1l1_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫḺ"):
            bstack1l1ll1l1_opy_.bstack1ll1l111l_opy_(self)
    bstack1l1ll1ll1l_opy_.append(self)
    if bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧḻ") in CONFIG and bstack1l1_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪḼ") in CONFIG[bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩḽ")][bstack11l111l1ll_opy_]:
        bstack1l1lll111l_opy_ = CONFIG[bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪḾ")][bstack11l111l1ll_opy_][bstack1l1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ḿ")]
    logger.debug(bstack1l1llll111_opy_.format(bstack1ll1l1111_opy_))
def bstack1lll1lll1_opy_(self, url):
    global bstack1ll111l11l_opy_
    global CONFIG
    try:
        bstack1l1l1l1l1l_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1l11ll1ll_opy_.format(str(err)))
    try:
        bstack1ll111l11l_opy_(self, url)
    except Exception as e:
        try:
            parsed_error = str(e)
            if any(err_msg in parsed_error for err_msg in bstack1l1l11ll11_opy_):
                bstack1l1l1l1l1l_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1l11ll1ll_opy_.format(str(err)))
        raise e
def bstack1llll11lll_opy_(item, when):
    global bstack11lll11l11_opy_
    try:
        bstack11lll11l11_opy_(item, when)
    except Exception as e:
        pass
def bstack11l1l1lll1_opy_(item, call, rep):
    global bstack1ll1l1llll_opy_
    global bstack1l1ll1ll1l_opy_
    name = bstack1l1_opy_ (u"ࠩࠪṀ")
    try:
        if rep.when == bstack1l1_opy_ (u"ࠪࡧࡦࡲ࡬ࠨṁ"):
            bstack1ll1l1111_opy_ = threading.current_thread().bstackSessionId
            bstack11l1l1l1lll_opy_ = item.config.getoption(bstack1l1_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭Ṃ"))
            try:
                if (str(bstack11l1l1l1lll_opy_).lower() != bstack1l1_opy_ (u"ࠬࡺࡲࡶࡧࠪṃ")):
                    name = str(rep.nodeid)
                    bstack1l11ll11ll_opy_ = bstack1l1ll1ll11_opy_(bstack1l1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧṄ"), name, bstack1l1_opy_ (u"ࠧࠨṅ"), bstack1l1_opy_ (u"ࠨࠩṆ"), bstack1l1_opy_ (u"ࠩࠪṇ"), bstack1l1_opy_ (u"ࠪࠫṈ"))
                    os.environ[bstack1l1_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗࡣ࡙ࡋࡓࡕࡡࡑࡅࡒࡋࠧṉ")] = name
                    for driver in bstack1l1ll1ll1l_opy_:
                        if bstack1ll1l1111_opy_ == driver.session_id:
                            driver.execute_script(bstack1l11ll11ll_opy_)
            except Exception as e:
                logger.debug(bstack1l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬṊ").format(str(e)))
            try:
                bstack111l11l1l_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack1l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧṋ"):
                    status = bstack1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧṌ") if rep.outcome.lower() == bstack1l1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨṍ") else bstack1l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩṎ")
                    reason = bstack1l1_opy_ (u"ࠪࠫṏ")
                    if status == bstack1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫṐ"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack1l1_opy_ (u"ࠬ࡯࡮ࡧࡱࠪṑ") if status == bstack1l1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭Ṓ") else bstack1l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ṓ")
                    data = name + bstack1l1_opy_ (u"ࠨࠢࡳࡥࡸࡹࡥࡥࠣࠪṔ") if status == bstack1l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩṕ") else name + bstack1l1_opy_ (u"ࠪࠤ࡫ࡧࡩ࡭ࡧࡧࠥࠥ࠭Ṗ") + reason
                    bstack1l1lllll11_opy_ = bstack1l1ll1ll11_opy_(bstack1l1_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ṗ"), bstack1l1_opy_ (u"ࠬ࠭Ṙ"), bstack1l1_opy_ (u"࠭ࠧṙ"), bstack1l1_opy_ (u"ࠧࠨṚ"), level, data)
                    for driver in bstack1l1ll1ll1l_opy_:
                        if bstack1ll1l1111_opy_ == driver.session_id:
                            driver.execute_script(bstack1l1lllll11_opy_)
            except Exception as e:
                logger.debug(bstack1l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡩ࡯࡯ࡶࡨࡼࡹࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬṛ").format(str(e)))
    except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡴࡢࡶࡨࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿࢂ࠭Ṝ").format(str(e)))
    bstack1ll1l1llll_opy_(item, call, rep)
notset = Notset()
def bstack11l1llll11_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack1lll1ll111_opy_
    if str(name).lower() == bstack1l1_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࠪṝ"):
        return bstack1l1_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥṞ")
    else:
        return bstack1lll1ll111_opy_(self, name, default, skip)
def bstack11l11llll1_opy_(self):
    global CONFIG
    global bstack11ll1l111_opy_
    try:
        proxy = bstack1l1ll11lll_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack1l1_opy_ (u"ࠬ࠴ࡰࡢࡥࠪṟ")):
                proxies = bstack1ll1111l1l_opy_(proxy, bstack1ll1ll11l1_opy_())
                if len(proxies) > 0:
                    protocol, bstack1l1l111lll_opy_ = proxies.popitem()
                    if bstack1l1_opy_ (u"ࠨ࠺࠰࠱ࠥṠ") in bstack1l1l111lll_opy_:
                        return bstack1l1l111lll_opy_
                    else:
                        return bstack1l1_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣṡ") + bstack1l1l111lll_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack1l1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡵࡸ࡯ࡹࡻࠣࡹࡷࡲࠠ࠻ࠢࡾࢁࠧṢ").format(str(e)))
    return bstack11ll1l111_opy_(self)
def bstack1l1l11l11l_opy_():
    return (bstack1l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬṣ") in CONFIG or bstack1l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧṤ") in CONFIG) and bstack111111ll1_opy_() and bstack1lll1lll11_opy_() >= version.parse(
        bstack1ll11l111l_opy_)
def bstack1l1lll1ll_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack1l1lll111l_opy_
    global bstack1ll11llll_opy_
    global bstack11lll1l1ll_opy_
    CONFIG[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ṥ")] = str(bstack11lll1l1ll_opy_) + str(__version__)
    bstack11l111l1ll_opy_ = 0
    try:
        if bstack1ll11llll_opy_ is True:
            bstack11l111l1ll_opy_ = int(os.environ.get(bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬṦ")))
    except:
        bstack11l111l1ll_opy_ = 0
    CONFIG[bstack1l1_opy_ (u"ࠨࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧṧ")] = True
    bstack1llll1l111_opy_ = bstack11lll1ll1l_opy_(CONFIG, bstack11l111l1ll_opy_)
    logger.debug(bstack11lll1ll11_opy_.format(str(bstack1llll1l111_opy_)))
    if CONFIG.get(bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫṨ")):
        bstack1l1l1l1lll_opy_(bstack1llll1l111_opy_, bstack1ll1ll11l_opy_)
    if bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫṩ") in CONFIG and bstack1l1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧṪ") in CONFIG[bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ṫ")][bstack11l111l1ll_opy_]:
        bstack1l1lll111l_opy_ = CONFIG[bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧṬ")][bstack11l111l1ll_opy_][bstack1l1_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪṭ")]
    import urllib
    import json
    if bstack1l1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪṮ") in CONFIG and str(CONFIG[bstack1l1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫṯ")]).lower() != bstack1l1_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧṰ"):
        bstack1lll11lll1_opy_ = bstack11ll1ll1l_opy_()
        bstack1ll1ll1l1_opy_ = bstack1lll11lll1_opy_ + urllib.parse.quote(json.dumps(bstack1llll1l111_opy_))
    else:
        bstack1ll1ll1l1_opy_ = bstack1l1_opy_ (u"ࠩࡺࡷࡸࡀ࠯࠰ࡥࡧࡴ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࡄࡩࡡࡱࡵࡀࠫṱ") + urllib.parse.quote(json.dumps(bstack1llll1l111_opy_))
    browser = self.connect(bstack1ll1ll1l1_opy_)
    return browser
def bstack11l1lll1l1_opy_():
    global bstack1lll11111_opy_
    global bstack11lll1l1ll_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1l11llll11_opy_
        if not bstack1ll11l11111_opy_():
            global bstack1l1l1111ll_opy_
            if not bstack1l1l1111ll_opy_:
                from bstack_utils.helper import bstack1l1l111ll_opy_, bstack11l1111ll1_opy_
                bstack1l1l1111ll_opy_ = bstack1l1l111ll_opy_()
                bstack11l1111ll1_opy_(bstack11lll1l1ll_opy_)
            BrowserType.connect = bstack1l11llll11_opy_
            return
        BrowserType.launch = bstack1l1lll1ll_opy_
        bstack1lll11111_opy_ = True
    except Exception as e:
        pass
def bstack11l1l1l1l11_opy_():
    global CONFIG
    global bstack1ll1lll11_opy_
    global bstack11ll1ll111_opy_
    global bstack1ll1ll11l_opy_
    global bstack1ll11llll_opy_
    global bstack1l1l11l1l1_opy_
    CONFIG = json.loads(os.environ.get(bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࠩṲ")))
    bstack1ll1lll11_opy_ = eval(os.environ.get(bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬṳ")))
    bstack11ll1ll111_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡍ࡛ࡂࡠࡗࡕࡐࠬṴ"))
    bstack1l1lllll1l_opy_(CONFIG, bstack1ll1lll11_opy_)
    bstack1l1l11l1l1_opy_ = bstack11ll11llll_opy_.bstack1ll111l1l1_opy_(CONFIG, bstack1l1l11l1l1_opy_)
    if cli.bstack1ll1ll1l1l_opy_():
        bstack1llll1l11l_opy_.invoke(Events.CONNECT, bstack11ll1111ll_opy_())
        cli_context.platform_index = int(os.environ.get(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ṵ"), bstack1l1_opy_ (u"ࠧ࠱ࠩṶ")))
        cli.bstack1ll1llllll1_opy_(bstack1ll1ll11l1_opy_(bstack11ll1ll111_opy_, CONFIG), cli_context.platform_index, bstack1ll1ll111_opy_)
        cli.bstack1ll1ll111l1_opy_()
        logger.debug(bstack1l1_opy_ (u"ࠣࡅࡏࡍࠥ࡯ࡳࠡࡣࡦࡸ࡮ࡼࡥࠡࡨࡲࡶࠥࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࠢṷ") + str(cli_context.platform_index) + bstack1l1_opy_ (u"ࠤࠥṸ"))
        return # skip all existing bstack11l1l1ll111_opy_
    global bstack1l111111ll_opy_
    global bstack1lll1ll1ll_opy_
    global bstack11lllllll1_opy_
    global bstack1l1l11lll1_opy_
    global bstack1l1l1l11ll_opy_
    global bstack1ll1l11l11_opy_
    global bstack1l111111l_opy_
    global bstack1ll111l11l_opy_
    global bstack11ll1l111_opy_
    global bstack1lll1ll111_opy_
    global bstack11lll11l11_opy_
    global bstack1ll1l1llll_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack1l111111ll_opy_ = webdriver.Remote.__init__
        bstack1lll1ll1ll_opy_ = WebDriver.quit
        bstack1l111111l_opy_ = WebDriver.close
        bstack1ll111l11l_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack1l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ṹ") in CONFIG or bstack1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨṺ") in CONFIG) and bstack111111ll1_opy_():
        if bstack1lll1lll11_opy_() < version.parse(bstack1ll11l111l_opy_):
            logger.error(bstack1l1111l11_opy_.format(bstack1lll1lll11_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                bstack11ll1l111_opy_ = RemoteConnection._11l1l111ll_opy_
            except Exception as e:
                logger.error(bstack11111lll1_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack1lll1ll111_opy_ = Config.getoption
        from _pytest import runner
        bstack11lll11l11_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack111l1l1l_opy_)
    try:
        from pytest_bdd import reporting
        bstack1ll1l1llll_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡴࠦࡲࡶࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࡸ࠭ṻ"))
    bstack1ll1ll11l_opy_ = CONFIG.get(bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪṼ"), {}).get(bstack1l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩṽ"))
    bstack1ll11llll_opy_ = True
    bstack11ll1l1ll1_opy_(bstack11ll1ll1l1_opy_)
if (bstack1l11l1ll11l_opy_()):
    bstack11l1l1l1l11_opy_()
@bstack1lll111l_opy_(class_method=False)
def bstack11l1ll1ll11_opy_(hook_name, event, bstack1lllll1l1ll_opy_=None):
    if hook_name not in [bstack1l1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩṾ"), bstack1l1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ṿ"), bstack1l1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩẀ"), bstack1l1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪ࠭ẁ"), bstack1l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠪẂ"), bstack1l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠧẃ"), bstack1l1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭Ẅ"), bstack1l1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠪẅ")]:
        return
    node = store[bstack1l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭Ẇ")]
    if hook_name in [bstack1l1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩẇ"), bstack1l1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪ࠭Ẉ")]:
        node = store[bstack1l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥ࡭ࡰࡦࡸࡰࡪࡥࡩࡵࡧࡰࠫẉ")]
    elif hook_name in [bstack1l1_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡩ࡬ࡢࡵࡶࠫẊ"), bstack1l1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨẋ")]:
        node = store[bstack1l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡦࡰࡦࡹࡳࡠ࡫ࡷࡩࡲ࠭Ẍ")]
    hook_type = bstack1l1l11l11ll_opy_(hook_name)
    if event == bstack1l1_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩẍ"):
        if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
            cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_[hook_type], bstack1111l11l11_opy_.PRE, node, hook_name)
            return
        uuid = uuid4().__str__()
        bstack11lll1ll_opy_ = {
            bstack1l1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨẎ"): uuid,
            bstack1l1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨẏ"): bstack1l111ll1_opy_(),
            bstack1l1_opy_ (u"ࠬࡺࡹࡱࡧࠪẐ"): bstack1l1_opy_ (u"࠭ࡨࡰࡱ࡮ࠫẑ"),
            bstack1l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪẒ"): hook_type,
            bstack1l1_opy_ (u"ࠨࡪࡲࡳࡰࡥ࡮ࡢ࡯ࡨࠫẓ"): hook_name
        }
        store[bstack1l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭Ẕ")].append(uuid)
        bstack11l1l1l1l1l_opy_ = node.nodeid
        if hook_type == bstack1l1_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨẕ"):
            if not _1l1l11l1_opy_.get(bstack11l1l1l1l1l_opy_, None):
                _1l1l11l1_opy_[bstack11l1l1l1l1l_opy_] = {bstack1l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪẖ"): []}
            _1l1l11l1_opy_[bstack11l1l1l1l1l_opy_][bstack1l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫẗ")].append(bstack11lll1ll_opy_[bstack1l1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫẘ")])
        _1l1l11l1_opy_[bstack11l1l1l1l1l_opy_ + bstack1l1_opy_ (u"ࠧ࠮ࠩẙ") + hook_name] = bstack11lll1ll_opy_
        bstack11l1l1l111l_opy_(node, bstack11lll1ll_opy_, bstack1l1_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩẚ"))
    elif event == bstack1l1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨẛ"):
        if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
            cli.test_framework.track_event(cli_context, bstack1111l11l1l_opy_[hook_type], bstack1111l11l11_opy_.POST, node, None, bstack1lllll1l1ll_opy_)
            return
        bstack1l11l1ll_opy_ = node.nodeid + bstack1l1_opy_ (u"ࠪ࠱ࠬẜ") + hook_name
        _1l1l11l1_opy_[bstack1l11l1ll_opy_][bstack1l1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩẝ")] = bstack1l111ll1_opy_()
        bstack11l1ll1l1ll_opy_(_1l1l11l1_opy_[bstack1l11l1ll_opy_][bstack1l1_opy_ (u"ࠬࡻࡵࡪࡦࠪẞ")])
        bstack11l1l1l111l_opy_(node, _1l1l11l1_opy_[bstack1l11l1ll_opy_], bstack1l1_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨẟ"), bstack11l1l1ll11l_opy_=bstack1lllll1l1ll_opy_)
def bstack11l1ll11ll1_opy_():
    global bstack11l1ll1lll1_opy_
    if bstack111lllll11_opy_():
        bstack11l1ll1lll1_opy_ = bstack1l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫẠ")
    else:
        bstack11l1ll1lll1_opy_ = bstack1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨạ")
@bstack1l1ll1l1_opy_.bstack11ll111l1ll_opy_
def bstack11l1l1ll1ll_opy_():
    bstack11l1ll11ll1_opy_()
    if cli.bstack1ll1l1l11ll_opy_(bstack1ll1l1l1ll1_opy_):
        try:
            bstack1l1l1llllll_opy_(bstack11l1ll1ll11_opy_)
        except Exception as e:
            logger.debug(bstack1l1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡲࡳࡰࡹࠠࡱࡣࡷࡧ࡭ࡀࠠࡼࡿࠥẢ").format(e))
        return
    if bstack111111ll1_opy_():
        bstack11l111111l_opy_(bstack1l1l11l11_opy_)
    try:
        bstack1l1l1llllll_opy_(bstack11l1ll1ll11_opy_)
    except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡳࡴࡱࡳࠡࡲࡤࡸࡨ࡮࠺ࠡࡽࢀࠦả").format(e))
bstack11l1l1ll1ll_opy_()