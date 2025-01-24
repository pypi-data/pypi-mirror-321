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
import subprocess
import threading
import time
import sys
import grpc
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack111l11111l_opy_ import bstack111l1111l1_opy_
from browserstack_sdk.sdk_cli.bstack111l1ll1ll_opy_ import bstack111ll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l1l11_opy_ import bstack1ll1l1l111l_opy_
from browserstack_sdk.sdk_cli.bstack1lll11ll1ll_opy_ import bstack1lll1l111ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l1111_opy_ import bstack1lll111111l_opy_
from browserstack_sdk.sdk_cli.bstack111l1l1ll1_opy_ import bstack111l1l1111_opy_
from browserstack_sdk.sdk_cli.bstack1111l11lll_opy_ import bstack1111ll1111_opy_
from browserstack_sdk.sdk_cli.bstack1ll1l1l1l11_opy_ import bstack1ll1l1l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l11l_opy_ import bstack1llll1l11l_opy_, Events, bstack11ll1111ll_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1ll1l1lll11_opy_ import bstack1ll1lll11l1_opy_
from browserstack_sdk.sdk_cli.bstack111l111l1l_opy_ import bstack111l111ll1_opy_
from browserstack_sdk.sdk_cli.bstack111l11l1l1_opy_ import bstack11111ll111_opy_
from bstack_utils.helper import Notset, bstack1ll1lll1l11_opy_, get_cli_dir, bstack1ll1ll11111_opy_, bstack111lllll11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from bstack_utils.helper import bstack11l11lll1l_opy_, Notset, bstack1ll1lll1l11_opy_, get_cli_dir, bstack1ll1ll11111_opy_, bstack111lllll11_opy_, bstack11lll11l1l_opy_, bstack1ll1l1l11l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1111l11l1l_opy_, bstack1111ll1l11_opy_, bstack1111l11l11_opy_, bstack1lll1ll111l_opy_
from browserstack_sdk.sdk_cli.bstack111l11l1l1_opy_ import bstack111l1llll1_opy_, bstack111ll1ll11_opy_, bstack111ll11111_opy_
from bstack_utils.constants import *
from bstack_utils import bstack11ll11llll_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from bstack_utils.messages import bstack1lllll1l1l_opy_, bstack1l111l1l1_opy_
logger = bstack11ll11llll_opy_.get_logger(__name__, bstack11ll11llll_opy_.bstack1lll111ll1l_opy_())
def bstack1ll1l11ll1l_opy_(bs_config):
    bstack1ll1l1l1111_opy_ = None
    bstack1lll11l111l_opy_ = None
    try:
        bstack1lll11l111l_opy_ = get_cli_dir()
        bstack1ll1l1l1111_opy_ = bstack1ll1ll11111_opy_(bstack1lll11l111l_opy_)
        bstack1lll111l1ll_opy_ = bstack1ll1lll1l11_opy_(bstack1ll1l1l1111_opy_, bstack1lll11l111l_opy_, bs_config)
        bstack1ll1l1l1111_opy_ = bstack1lll111l1ll_opy_ if bstack1lll111l1ll_opy_ else bstack1ll1l1l1111_opy_
        if not bstack1ll1l1l1111_opy_:
            raise ValueError(bstack1l1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡖࡈࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡑࡃࡗࡌࠧგ"))
    except Exception as ex:
        logger.debug(bstack1l1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡥࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡺࡨࡦࠢ࡯ࡥࡹ࡫ࡳࡵࠢࡥ࡭ࡳࡧࡲࡺࠤდ"))
        bstack1ll1l1l1111_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡒࡄࡘࡍࠨე"))
        if bstack1ll1l1l1111_opy_:
            logger.debug(bstack1l1_opy_ (u"ࠦࡋࡧ࡬࡭࡫ࡱ࡫ࠥࡨࡡࡤ࡭ࠣࡸࡴࠦࡓࡅࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡕࡇࡔࡉࠢࡩࡶࡴࡳࠠࡦࡰࡹ࡭ࡷࡵ࡮࡮ࡧࡱࡸ࠿ࠦࠢვ") + str(bstack1ll1l1l1111_opy_) + bstack1l1_opy_ (u"ࠧࠨზ"))
        else:
            logger.debug(bstack1l1_opy_ (u"ࠨࡎࡰࠢࡹࡥࡱ࡯ࡤࠡࡕࡇࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡐࡂࡖࡋࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡥ࡯ࡸ࡬ࡶࡴࡴ࡭ࡦࡰࡷ࠿ࠥࡹࡥࡵࡷࡳࠤࡲࡧࡹࠡࡤࡨࠤ࡮ࡴࡣࡰ࡯ࡳࡰࡪࡺࡥ࠯ࠤთ"))
    return bstack1ll1l1l1111_opy_, bstack1lll11l111l_opy_
bstack1ll1l11lll1_opy_ = bstack1l1_opy_ (u"ࠢ࠺࠻࠼࠽ࠧი")
bstack1ll1ll1ll11_opy_ = bstack1l1_opy_ (u"ࠣࡴࡨࡥࡩࡿࠢკ")
bstack1ll1lll1lll_opy_ = bstack1l1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡖࡉࡘ࡙ࡉࡐࡐࡢࡍࡉࠨლ")
bstack1ll1l1ll111_opy_ = bstack1l1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡐࡎ࡙ࡔࡆࡐࡢࡅࡉࡊࡒࠣმ")
bstack1ll11ll1ll_opy_ = bstack1l1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠢნ")
bstack1lll1111l11_opy_ = re.compile(bstack1l1_opy_ (u"ࡷࠨࠨࡀ࡫ࠬ࠲࠯࠮ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࢁࡈࡓࠪ࠰࠭ࠦო"))
bstack1lll11l1ll1_opy_ = bstack1l1_opy_ (u"ࠨࡤࡦࡸࡨࡰࡴࡶ࡭ࡦࡰࡷࠦპ")
bstack1lll111llll_opy_ = [
    Events.bstack1ll1lll1l1_opy_,
    Events.CONNECT,
    Events.bstack1ll111l1l_opy_,
]
class SDKCLI:
    _1111111ll1_opy_ = None
    process: Union[None, Any]
    bstack1lll111ll11_opy_: bool
    bstack1ll1l1l11l1_opy_: bool
    bstack1ll1lll111l_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1ll1ll1l1l1_opy_: Union[None, grpc.Channel]
    bstack1ll1l1lllll_opy_: str
    test_framework: TestFramework
    bstack111l11l1l1_opy_: bstack11111ll111_opy_
    config: Union[None, Dict[str, Any]]
    web_driver: bstack111l1l1111_opy_
    bstack1lll11l1lll_opy_: bstack1111ll1111_opy_
    bstack1lll1111111_opy_: bstack1ll1l1l1ll1_opy_
    accessibility: bstack1ll1l1l111l_opy_
    ai: bstack1lll1l111ll_opy_
    bstack1lll1111ll1_opy_: bstack1lll111111l_opy_
    bstack1ll1ll1lll1_opy_: List[bstack111ll1l111_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1ll1lllll1l_opy_: Any
    bstack1ll1ll1l11l_opy_: Dict[str, timedelta]
    bstack1ll1lll11ll_opy_: str
    bstack111l11111l_opy_: bstack111l1111l1_opy_
    def __new__(cls):
        if not cls._1111111ll1_opy_:
            cls._1111111ll1_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1111111ll1_opy_
    def __init__(self):
        self.process = None
        self.bstack1lll111ll11_opy_ = False
        self.bstack1ll1ll1l1l1_opy_ = None
        self.bstack111ll1l11l_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1ll1l1ll111_opy_, None)
        self.bstack1ll1l1ll11l_opy_ = os.environ.get(bstack1ll1lll1lll_opy_, bstack1l1_opy_ (u"ࠢࠣჟ")) == bstack1l1_opy_ (u"ࠣࠤრ")
        self.bstack1ll1l1l11l1_opy_ = False
        self.bstack1ll1lll111l_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1ll1lllll1l_opy_ = None
        self.test_framework = None
        self.bstack111l11l1l1_opy_ = None
        self.bstack1ll1l1lllll_opy_=bstack1l1_opy_ (u"ࠤࠥს")
        self.logger = bstack11ll11llll_opy_.get_logger(self.__class__.__name__, bstack11ll11llll_opy_.bstack1lll111ll1l_opy_())
        self.bstack1ll1ll1l11l_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack111l11111l_opy_ = bstack111l1111l1_opy_()
        self.web_driver = bstack111l1l1111_opy_()
        self.bstack1lll11l1lll_opy_ = bstack1111ll1111_opy_()
        self.bstack1lll1111111_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1ll1ll1lll1_opy_ = [
            self.web_driver,
            self.bstack1lll11l1lll_opy_,
        ]
    def bstack11l11lll1l_opy_(self):
        return os.environ.get(bstack1ll11ll1ll_opy_).lower().__eq__(bstack1l1_opy_ (u"ࠥࡸࡷࡻࡥࠣტ"))
    def is_enabled(self, config):
        if bstack1l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨუ") in config and str(config[bstack1l1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩფ")]).lower() != bstack1l1_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬქ"):
            return False
        bstack1lll11l11l1_opy_ = [bstack1l1_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢღ"), bstack1l1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧყ")]
        return config.get(bstack1l1_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠧშ")) in bstack1lll11l11l1_opy_ or os.environ.get(bstack1l1_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫჩ")) in bstack1lll11l11l1_opy_
    def bstack1lll111lll_opy_(self):
        for event in bstack1lll111llll_opy_:
            bstack1llll1l11l_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack1llll1l11l_opy_.logger.debug(bstack1l1_opy_ (u"ࠦࢀ࡫ࡶࡦࡰࡷࡣࡳࡧ࡭ࡦࡿࠣࡁࡃࠦࡻࡢࡴࡪࡷࢂࠦࠢც") + str(kwargs) + bstack1l1_opy_ (u"ࠧࠨძ"))
            )
        bstack1llll1l11l_opy_.register(Events.bstack1ll1lll1l1_opy_, self.__1lll11l11ll_opy_)
        bstack1llll1l11l_opy_.register(Events.CONNECT, self.__1ll1l1llll1_opy_)
        bstack1llll1l11l_opy_.register(Events.bstack1ll111l1l_opy_, self.__1ll1l11ll11_opy_)
        bstack1llll1l11l_opy_.register(Events.bstack1l111llll_opy_, self.__1ll1lllllll_opy_)
    def bstack1ll1ll1l1l_opy_(self):
        return not self.bstack1ll1l1ll11l_opy_ and os.environ.get(bstack1ll1lll1lll_opy_, bstack1l1_opy_ (u"ࠨࠢწ")) != bstack1l1_opy_ (u"ࠢࠣჭ")
    def is_running(self):
        if self.bstack1ll1l1ll11l_opy_:
            return self.bstack1lll111ll11_opy_
        else:
            return bool(self.bstack1ll1ll1l1l1_opy_)
    def bstack1ll1l1l11ll_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1ll1ll1lll1_opy_) and cli.is_running()
    def __1ll1ll1llll_opy_(self, bstack1ll1lll1l1l_opy_=10):
        if self.bstack111ll1l11l_opy_:
            return
        bstack11l1l1ll11_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1ll1l1ll111_opy_, self.cli_listen_addr)
        self.logger.debug(bstack1l1_opy_ (u"ࠣ࡝ࠥხ") + str(id(self)) + bstack1l1_opy_ (u"ࠤࡠࠤࡨࡵ࡮࡯ࡧࡦࡸ࡮ࡴࡧࠣჯ"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack1l1_opy_ (u"ࠥ࡫ࡷࡶࡣ࠯ࡧࡱࡥࡧࡲࡥࡠࡪࡷࡸࡵࡥࡰࡳࡱࡻࡽࠧჰ"), 0), (bstack1l1_opy_ (u"ࠦ࡬ࡸࡰࡤ࠰ࡨࡲࡦࡨ࡬ࡦࡡ࡫ࡸࡹࡶࡳࡠࡲࡵࡳࡽࡿࠢჱ"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1ll1lll1l1l_opy_)
        self.bstack1ll1ll1l1l1_opy_ = channel
        self.bstack111ll1l11l_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1ll1ll1l1l1_opy_)
        self.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡧࡴࡴ࡮ࡦࡥࡷࠦჲ"), datetime.now() - bstack11l1l1ll11_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1ll1l1ll111_opy_] = self.cli_listen_addr
        self.logger.debug(bstack1l1_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡩ࡯࡯ࡰࡨࡧࡹ࡫ࡤ࠻ࠢ࡬ࡷࡤࡩࡨࡪ࡮ࡧࡣࡵࡸ࡯ࡤࡧࡶࡷࡂࠨჳ") + str(self.bstack1ll1ll1l1l_opy_()) + bstack1l1_opy_ (u"ࠢࠣჴ"))
    def __1ll1l11ll11_opy_(self, event_name):
        if self.bstack1ll1ll1l1l_opy_():
            self.logger.debug(bstack1l1_opy_ (u"ࠣࡥ࡫࡭ࡱࡪ࠭ࡱࡴࡲࡧࡪࡹࡳ࠻ࠢࡶࡸࡴࡶࡰࡪࡰࡪࠤࡈࡒࡉࠣჵ"))
        self.__1ll1ll11lll_opy_()
    def __1ll1lllllll_opy_(self, event_name, bstack1lll111l1l1_opy_ = None, bstack1l1ll111l_opy_=1):
        if bstack1l1ll111l_opy_ == 1:
            self.logger.error(bstack1l1_opy_ (u"ࠤࡖࡳࡲ࡫ࡴࡩ࡫ࡱ࡫ࠥࡽࡥ࡯ࡶࠣࡻࡷࡵ࡮ࡨࠤჶ"))
        bstack1ll1ll11ll1_opy_ = Path(bstack1lll1l111l1_opy_ (u"ࠥࡿࡸ࡫࡬ࡧ࠰ࡦࡰ࡮ࡥࡤࡪࡴࢀ࠳ࡺࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࡸ࠴ࡪࡴࡱࡱࠦჷ"))
        if self.bstack1lll11l111l_opy_ and bstack1ll1ll11ll1_opy_.exists():
            with open(bstack1ll1ll11ll1_opy_, bstack1l1_opy_ (u"ࠫࡷ࠭ჸ"), encoding=bstack1l1_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫჹ")) as fp:
                data = json.load(fp)
                try:
                    bstack11lll11l1l_opy_(bstack1l1_opy_ (u"࠭ࡐࡐࡕࡗࠫჺ"), bstack1ll1l1l11l_opy_(bstack1lll11ll1l_opy_), data, {
                        bstack1l1_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ჻"): (self.config[bstack1l1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪჼ")], self.config[bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬჽ")])
                    })
                except Exception as e:
                    logger.debug(bstack1l111l1l1_opy_.format(str(e)))
            bstack1ll1ll11ll1_opy_.unlink()
        sys.exit(bstack1l1ll111l_opy_)
    def __1lll11l11ll_opy_(self, event_name: str, data):
        self.bstack1ll1l1lllll_opy_, self.bstack1lll11l111l_opy_ = bstack1ll1l11ll1l_opy_(data.bs_config)
        os.environ[bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡ࡚ࡖࡎ࡚ࡁࡃࡎࡈࡣࡉࡏࡒࠨჾ")] = self.bstack1lll11l111l_opy_
        if not self.bstack1ll1l1lllll_opy_ or not self.bstack1lll11l111l_opy_:
            raise ValueError(bstack1l1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡺࡨࡦࠢࡖࡈࡐࠦࡃࡍࡋࠣࡦ࡮ࡴࡡࡳࡻࠥჿ"))
        if self.bstack1ll1ll1l1l_opy_():
            self.__1ll1l1llll1_opy_(event_name, bstack11ll1111ll_opy_())
            return
        start = datetime.now()
        is_started = self.__1ll1ll111ll_opy_()
        self.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠧࡹࡰࡢࡹࡱࡣࡹ࡯࡭ࡦࠤᄀ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1ll1ll1llll_opy_()
            self.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠨࡣࡰࡰࡱࡩࡨࡺ࡟ࡵ࡫ࡰࡩࠧᄁ"), datetime.now() - start)
            start = datetime.now()
            self.__1ll1llll1ll_opy_(data)
            self.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠢࡴࡶࡤࡶࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡵ࡫ࡰࡩࠧᄂ"), datetime.now() - start)
    def __1ll1l1llll1_opy_(self, event_name: str, data: bstack11ll1111ll_opy_):
        if not self.bstack1ll1ll1l1l_opy_():
            self.logger.debug(bstack1l1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡨࡵ࡮࡯ࡧࡦࡸ࠿ࠦ࡮ࡰࡶࠣࡥࠥࡩࡨࡪ࡮ࡧ࠱ࡵࡸ࡯ࡤࡧࡶࡷࠧᄃ"))
            return
        bin_session_id = os.environ.get(bstack1ll1lll1lll_opy_)
        start = datetime.now()
        self.__1ll1ll1llll_opy_()
        self.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠤࡦࡳࡳࡴࡥࡤࡶࡢࡸ࡮ࡳࡥࠣᄄ"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack1l1_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡦ࡬࡮ࡲࡤ࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠼ࠣࡧࡴࡴ࡮ࡦࡥࡷࡩࡩࠦࡴࡰࠢࡨࡼ࡮ࡹࡴࡪࡰࡪࠤࡈࡒࡉࠡࠤᄅ") + str(bin_session_id) + bstack1l1_opy_ (u"ࠦࠧᄆ"))
        start = datetime.now()
        self.__1lll111l111_opy_()
        self.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠧࡹࡴࡢࡴࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡺࡩ࡮ࡧࠥᄇ"), datetime.now() - start)
    def __1ll1llll1l1_opy_(self):
        if not self.bstack111ll1l11l_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack1l1_opy_ (u"ࠨࡣࡢࡰࡱࡳࡹࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡦࠢࡰࡳࡩࡻ࡬ࡦࡵࠥᄈ"))
            return
        if not self.bstack1lll1111111_opy_ and self.config_observability and self.config_observability.success: # bstack111lll111l_opy_
            self.bstack1lll1111111_opy_ = bstack1ll1l1l1ll1_opy_() # bstack1ll1lll1ll1_opy_
            self.bstack1ll1ll1lll1_opy_.append(self.bstack1lll1111111_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1ll1l1l111l_opy_()
            self.bstack1ll1ll1lll1_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack1l1_opy_ (u"ࠢࡴࡧ࡯ࡪࡍ࡫ࡡ࡭ࠤᄉ"), False) == True:
            self.ai = bstack1lll1l111ll_opy_()
            self.bstack1ll1ll1lll1_opy_.append(self.ai)
        if not self.percy and self.bstack1ll1lllll1l_opy_ and self.bstack1ll1lllll1l_opy_.success:
            self.percy = bstack1lll111111l_opy_(self.bstack1ll1lllll1l_opy_)
            self.bstack1ll1ll1lll1_opy_.append(self.percy)
        for mod in self.bstack1ll1ll1lll1_opy_:
            if not mod.bstack111l111111_opy_():
                mod.configure(self.bstack111ll1l11l_opy_, self.config, self.cli_bin_session_id, self.bstack111l11111l_opy_)
    def __1ll1l1l1l1l_opy_(self):
        for mod in self.bstack1ll1ll1lll1_opy_:
            if mod.bstack111l111111_opy_():
                mod.configure(self.bstack111ll1l11l_opy_, None, None, None)
    def __1ll1llll1ll_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack1ll1l1l11l1_opy_:
            return
        self.__1lll11l1l1l_opy_(data)
        bstack11l1l1ll11_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack1l1_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࠣᄊ")
        req.sdk_language = bstack1l1_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࠤᄋ")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1lll1111l11_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack1l1_opy_ (u"ࠥ࡟ࠧᄌ") + str(id(self)) + bstack1l1_opy_ (u"ࠦࡢࠦ࡭ࡢ࡫ࡱ࠱ࡵࡸ࡯ࡤࡧࡶࡷ࠿ࠦࡳࡵࡣࡵࡸࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠥᄍ"))
            r = self.bstack111ll1l11l_opy_.StartBinSession(req)
            self.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡹࡧࡲࡵࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢᄎ"), datetime.now() - bstack11l1l1ll11_opy_)
            os.environ[bstack1ll1lll1lll_opy_] = r.bin_session_id
            self.__1ll1l1l1lll_opy_(r)
            self.__1ll1llll1l1_opy_()
            self.bstack111l11111l_opy_.start()
            self.bstack1ll1l1l11l1_opy_ = True
            self.logger.debug(bstack1l1_opy_ (u"ࠨ࡛ࠣᄏ") + str(id(self)) + bstack1l1_opy_ (u"ࠢ࡞ࠢࡰࡥ࡮ࡴ࠭ࡱࡴࡲࡧࡪࡹࡳ࠻ࠢࡦࡳࡳࡴࡥࡤࡶࡨࡨࠧᄐ"))
        except grpc.bstack1lll111l11l_opy_ as bstack1lll11ll111_opy_:
            self.logger.error(bstack1l1_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡵ࡫ࡰࡩࡴ࡫ࡵࡵ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᄑ") + str(bstack1lll11ll111_opy_) + bstack1l1_opy_ (u"ࠤࠥᄒ"))
            traceback.print_exc()
            raise bstack1lll11ll111_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᄓ") + str(e) + bstack1l1_opy_ (u"ࠦࠧᄔ"))
            traceback.print_exc()
            raise e
    def __1lll111l111_opy_(self):
        if not self.bstack1ll1ll1l1l_opy_() or not self.cli_bin_session_id or self.bstack1ll1lll111l_opy_:
            return
        bstack11l1l1ll11_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬᄕ"), bstack1l1_opy_ (u"࠭࠰ࠨᄖ")))
        try:
            self.logger.debug(bstack1l1_opy_ (u"ࠢ࡜ࠤᄗ") + str(id(self)) + bstack1l1_opy_ (u"ࠣ࡟ࠣࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵ࠽ࠤࡨࡵ࡮࡯ࡧࡦࡸࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠥᄘ"))
            r = self.bstack111ll1l11l_opy_.ConnectBinSession(req)
            self.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡤࡱࡱࡲࡪࡩࡴࡠࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࠨᄙ"), datetime.now() - bstack11l1l1ll11_opy_)
            self.__1ll1l1l1lll_opy_(r)
            self.__1ll1llll1l1_opy_()
            self.bstack111l11111l_opy_.start()
            self.bstack1ll1lll111l_opy_ = True
            self.logger.debug(bstack1l1_opy_ (u"ࠥ࡟ࠧᄚ") + str(id(self)) + bstack1l1_opy_ (u"ࠦࡢࠦࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࡀࠠࡤࡱࡱࡲࡪࡩࡴࡦࡦࠥᄛ"))
        except grpc.bstack1lll111l11l_opy_ as bstack1lll11ll111_opy_:
            self.logger.error(bstack1l1_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡹ࡯࡭ࡦࡱࡨࡹࡹ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᄜ") + str(bstack1lll11ll111_opy_) + bstack1l1_opy_ (u"ࠨࠢᄝ"))
            traceback.print_exc()
            raise bstack1lll11ll111_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦᄞ") + str(e) + bstack1l1_opy_ (u"ࠣࠤᄟ"))
            traceback.print_exc()
            raise e
    def __1ll1l1l1lll_opy_(self, r):
        self.bstack1ll1l11l1ll_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack1l1_opy_ (u"ࠤࡸࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡳࡦࡴࡹࡩࡷࠦࡲࡦࡵࡳࡳࡳࡹࡥࠣᄠ") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack1l1_opy_ (u"ࠥࡩࡲࡶࡴࡺࠢࡦࡳࡳ࡬ࡩࡨࠢࡩࡳࡺࡴࡤࠣᄡ"))
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack1l1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡒࡨࡶࡨࡿࠠࡪࡵࠣࡷࡪࡴࡴࠡࡱࡱࡰࡾࠦࡡࡴࠢࡳࡥࡷࡺࠠࡰࡨࠣࡸ࡭࡫ࠠࠣࡅࡲࡲࡳ࡫ࡣࡵࡄ࡬ࡲࡘ࡫ࡳࡴ࡫ࡲࡲ࠱ࠨࠠࡢࡰࡧࠤࡹ࡮ࡩࡴࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤ࡮ࡹࠠࡢ࡮ࡶࡳࠥࡻࡳࡦࡦࠣࡦࡾࠦࡓࡵࡣࡵࡸࡇ࡯࡮ࡔࡧࡶࡷ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡘ࡭࡫ࡲࡦࡨࡲࡶࡪ࠲ࠠࡏࡱࡱࡩࠥ࡮ࡡ࡯ࡦ࡯࡭ࡳ࡭ࠠࡪࡵࠣ࡭ࡲࡶ࡬ࡦ࡯ࡨࡲࡹ࡫ࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᄢ")
        self.bstack1ll1lllll1l_opy_ = getattr(r, bstack1l1_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫᄣ"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᄤ")] = self.config_testhub.jwt
        os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᄥ")] = self.config_testhub.build_hashed_id
    def __1ll1ll111ll_opy_(self, bstack1ll1lll1l1l_opy_=10):
        if self.bstack1lll111ll11_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠣࡵࡷࡥࡷࡺ࠺ࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡵࡹࡳࡴࡩ࡯ࡩࠥᄦ"))
            return True
        self.logger.debug(bstack1l1_opy_ (u"ࠤࡶࡸࡦࡸࡴࠣᄧ"))
        if os.getenv(bstack1l1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡅࡏࡘࠥᄨ")) == bstack1lll11l1ll1_opy_:
            self.cli_bin_session_id = bstack1lll11l1ll1_opy_
            self.cli_listen_addr = bstack1l1_opy_ (u"ࠦࡺࡴࡩࡹ࠼࠲ࡸࡲࡶ࠯ࡴࡦ࡮࠱ࡵࡲࡡࡵࡨࡲࡶࡲ࠳ࠥࡴ࠰ࡶࡳࡨࡱࠢᄩ") % (self.cli_bin_session_id)
            self.bstack1lll111ll11_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1ll1l1lllll_opy_, bstack1l1_opy_ (u"ࠧࡹࡤ࡬ࠤᄪ")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1ll1ll1l1ll_opy_ compat for text=True in bstack1lll11ll1l1_opy_ python
            encoding=bstack1l1_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᄫ"),
            bufsize=1,
            close_fds=True,
        )
        bstack1ll1llll111_opy_ = threading.Thread(target=self.__1ll1lll1111_opy_, args=(bstack1ll1lll1l1l_opy_,))
        bstack1ll1llll111_opy_.start()
        bstack1ll1llll111_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack1l1_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡳࡱࡣࡺࡲ࠿ࠦࡲࡦࡶࡸࡶࡳࡩ࡯ࡥࡧࡀࡿࡸ࡫࡬ࡧ࠰ࡳࡶࡴࡩࡥࡴࡵ࠱ࡶࡪࡺࡵࡳࡰࡦࡳࡩ࡫ࡽࠡࡱࡸࡸࡂࢁࡳࡦ࡮ࡩ࠲ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡹࡴࡥࡱࡸࡸ࠳ࡸࡥࡢࡦࠫ࠭ࢂࠦࡥࡳࡴࡀࠦᄬ") + str(self.process.stderr.read()) + bstack1l1_opy_ (u"ࠣࠤᄭ"))
        if not self.bstack1lll111ll11_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠤ࡞ࠦᄮ") + str(id(self)) + bstack1l1_opy_ (u"ࠥࡡࠥࡩ࡬ࡦࡣࡱࡹࡵࠨᄯ"))
            self.__1ll1ll11lll_opy_()
        self.logger.debug(bstack1l1_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡴࡷࡵࡣࡦࡵࡶࡣࡷ࡫ࡡࡥࡻ࠽ࠤࠧᄰ") + str(self.bstack1lll111ll11_opy_) + bstack1l1_opy_ (u"ࠧࠨᄱ"))
        return self.bstack1lll111ll11_opy_
    def __1ll1lll1111_opy_(self, bstack1lll1111lll_opy_=10):
        bstack1ll1l1lll1l_opy_ = time.time()
        while self.process and time.time() - bstack1ll1l1lll1l_opy_ < bstack1lll1111lll_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack1l1_opy_ (u"ࠨࡩࡥ࠿ࠥᄲ") in line:
                    self.cli_bin_session_id = line.split(bstack1l1_opy_ (u"ࠢࡪࡦࡀࠦᄳ"))[-1:][0].strip()
                    self.logger.debug(bstack1l1_opy_ (u"ࠣࡥ࡯࡭ࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࡀࠢᄴ") + str(self.cli_bin_session_id) + bstack1l1_opy_ (u"ࠤࠥᄵ"))
                    continue
                if bstack1l1_opy_ (u"ࠥࡰ࡮ࡹࡴࡦࡰࡀࠦᄶ") in line:
                    self.cli_listen_addr = line.split(bstack1l1_opy_ (u"ࠦࡱ࡯ࡳࡵࡧࡱࡁࠧᄷ"))[-1:][0].strip()
                    self.logger.debug(bstack1l1_opy_ (u"ࠧࡩ࡬ࡪࡡ࡯࡭ࡸࡺࡥ࡯ࡡࡤࡨࡩࡸ࠺ࠣᄸ") + str(self.cli_listen_addr) + bstack1l1_opy_ (u"ࠨࠢᄹ"))
                    continue
                if bstack1l1_opy_ (u"ࠢࡱࡱࡵࡸࡂࠨᄺ") in line:
                    port = line.split(bstack1l1_opy_ (u"ࠣࡲࡲࡶࡹࡃࠢᄻ"))[-1:][0].strip()
                    self.logger.debug(bstack1l1_opy_ (u"ࠤࡳࡳࡷࡺ࠺ࠣᄼ") + str(port) + bstack1l1_opy_ (u"ࠥࠦᄽ"))
                    continue
                if line.strip() == bstack1ll1ll1ll11_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack1l1_opy_ (u"ࠦࡘࡊࡋࡠࡅࡏࡍࡤࡌࡌࡂࡉࡢࡍࡔࡥࡓࡕࡔࡈࡅࡒࠨᄾ"), bstack1l1_opy_ (u"ࠧ࠷ࠢᄿ")) == bstack1l1_opy_ (u"ࠨ࠱ࠣᅀ"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1lll111ll11_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack1l1_opy_ (u"ࠢࡦࡴࡵࡳࡷࡀࠠࠣᅁ") + str(e) + bstack1l1_opy_ (u"ࠣࠤᅂ"))
        return False
    def __1ll1ll11lll_opy_(self):
        if self.bstack1ll1ll1l1l1_opy_:
            self.bstack111l11111l_opy_.stop()
            start = datetime.now()
            if self.bstack1ll1ll11l1l_opy_():
                self.cli_bin_session_id = None
                if self.bstack1ll1lll111l_opy_:
                    self.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠤࡶࡸࡴࡶ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡶ࡬ࡱࡪࠨᅃ"), datetime.now() - start)
                else:
                    self.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠥࡷࡹࡵࡰࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡷ࡭ࡲ࡫ࠢᅄ"), datetime.now() - start)
            self.__1ll1l1l1l1l_opy_()
            start = datetime.now()
            self.bstack1ll1ll1l1l1_opy_.close()
            self.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠦࡩ࡯ࡳࡤࡱࡱࡲࡪࡩࡴࡠࡶ࡬ࡱࡪࠨᅅ"), datetime.now() - start)
            self.bstack1ll1ll1l1l1_opy_ = None
        if self.process:
            self.logger.debug(bstack1l1_opy_ (u"ࠧࡹࡴࡰࡲࠥᅆ"))
            start = datetime.now()
            self.process.terminate()
            self.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠨ࡫ࡪ࡮࡯ࡣࡹ࡯࡭ࡦࠤᅇ"), datetime.now() - start)
            self.process = None
            if self.bstack1ll1l1ll11l_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack11l111ll11_opy_()
                self.logger.info(
                    bstack1l1_opy_ (u"ࠢࡗ࡫ࡶ࡭ࡹࠦࡨࡵࡶࡳࡷ࠿࠵࠯ࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠦࡴࡰࠢࡹ࡭ࡪࡽࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡲࡲࡶࡹ࠲ࠠࡪࡰࡶ࡭࡬࡮ࡴࡴ࠮ࠣࡥࡳࡪࠠ࡮ࡣࡱࡽࠥࡳ࡯ࡳࡧࠣࡨࡪࡨࡵࡨࡩ࡬ࡲ࡬ࠦࡩ࡯ࡨࡲࡶࡲࡧࡴࡪࡱࡱࠤࡦࡲ࡬ࠡࡣࡷࠤࡴࡴࡥࠡࡲ࡯ࡥࡨ࡫ࠡ࡝ࡰࠥᅈ").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack1l1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧᅉ")] = self.config_testhub.build_hashed_id
        self.bstack1lll111ll11_opy_ = False
    def __1lll11l1l1l_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack1l1_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰࠦᅊ")] = selenium.__version__
            data.frameworks.append(bstack1l1_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧᅋ"))
        except:
            pass
    def bstack1ll1llllll1_opy_(self, hub_url: str, platform_index: int, bstack1ll1ll111_opy_: Any):
        if self.bstack111l11l1l1_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠦࡸࡱࡩࡱࡲࡨࡨࠥࡹࡥࡵࡷࡳࠤࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡀࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡵࡨࡸࠥࡻࡰࠣᅌ"))
            return
        try:
            bstack11l1l1ll11_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack1l1_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢᅍ")
            self.bstack111l11l1l1_opy_ = bstack111l111ll1_opy_(
                hub_url,
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack111l1l1lll_opy_={bstack1l1_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡥ࡯ࡱࡶ࡬ࡳࡳࡹ࡟ࡧࡴࡲࡱࡤࡩࡡࡱࡵࠥᅎ"): bstack1ll1ll111_opy_}
            )
            def bstack1lll11ll11l_opy_(self):
                return
            if self.config.get(bstack1l1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠤᅏ"), True):
                Service.start = bstack1lll11ll11l_opy_
                Service.stop = bstack1lll11ll11l_opy_
            def get_accessibility_results(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.get_accessibility_results(driver, framework_name=framework)
            def get_accessibility_results_summary(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.get_accessibility_results_summary(driver, framework_name=framework)
            def perform_scan(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.perform_scan(driver, method=None, framework_name=framework)
            WebDriver.getAccessibilityResults = get_accessibility_results
            WebDriver.get_accessibility_results = get_accessibility_results
            WebDriver.getAccessibilityResultsSummary = get_accessibility_results_summary
            WebDriver.get_accessibility_results_summary = get_accessibility_results_summary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤᅐ"), datetime.now() - bstack11l1l1ll11_opy_)
        except Exception as e:
            self.logger.error(bstack1l1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࡷࡳࠤࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡀࠠࠣᅑ") + str(e) + bstack1l1_opy_ (u"ࠥࠦᅒ"))
    def bstack1ll1ll111l1_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack1l1_opy_ (u"ࠦࡸࡱࡩࡱࡲࡨࡨࠥࡹࡥࡵࡷࡳࠤࡵࡿࡴࡦࡵࡷ࠾ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡳࡦࡶࠣࡹࡵࠨᅓ"))
            return
        if bstack111lllll11_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack1l1_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧᅔ"): pytest.__version__ }, [bstack1l1_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥᅕ")])
            return
        try:
            import pytest
            self.test_framework = bstack1ll1lll11l1_opy_({ bstack1l1_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢᅖ"): pytest.__version__ }, [bstack1l1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣᅗ")])
        except Exception as e:
            self.logger.error(bstack1l1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࡷࡳࠤࡵࡿࡴࡦࡵࡷ࠾ࠥࠨᅘ") + str(e) + bstack1l1_opy_ (u"ࠥࠦᅙ"))
        self.bstack1ll1l1ll1l1_opy_()
    def bstack1ll1l1ll1l1_opy_(self):
        if not self.bstack11l11lll1l_opy_():
            return
        bstack1lll1ll111_opy_ = None
        def bstack11l11ll1ll_opy_(config, startdir):
            return bstack1l1_opy_ (u"ࠦࡩࡸࡩࡷࡧࡵ࠾ࠥࢁ࠰ࡾࠤᅚ").format(bstack1l1_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠦᅛ"))
        def bstack111lll11l_opy_():
            return
        def bstack11l1llll11_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack1l1_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷ࠭ᅜ"):
                return bstack1l1_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨᅝ")
            else:
                return bstack1lll1ll111_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack1lll1ll111_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack11l11ll1ll_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack111lll11l_opy_
            Config.getoption = bstack11l1llll11_opy_
        except Exception as e:
            self.logger.error(bstack1l1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡴࡤࡪࠣࡴࡾࡺࡥࡴࡶࠣࡷࡪࡲࡥ࡯࡫ࡸࡱࠥ࡬࡯ࡳࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠻ࠢࠥᅞ") + str(e) + bstack1l1_opy_ (u"ࠤࠥᅟ"))
    def bstack1ll1l1ll1ll_opy_(self):
        bstack1ll1ll1111l_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack1ll1ll1111l_opy_, dict):
            if cli.config_observability:
                bstack1ll1ll1111l_opy_.update(
                    {bstack1l1_opy_ (u"ࠥࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠥᅠ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack1l1_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡸࡥࡴࡰࡡࡺࡶࡦࡶࠢᅡ") in accessibility.get(bstack1l1_opy_ (u"ࠧࡵࡰࡵ࡫ࡲࡲࡸࠨᅢ"), {}):
                    bstack1lll11111ll_opy_ = accessibility.get(bstack1l1_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡳࡳࡹࠢᅣ"))
                    bstack1lll11111ll_opy_.update({ bstack1l1_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࡖࡲ࡛ࡷࡧࡰࠣᅤ"): bstack1lll11111ll_opy_.pop(bstack1l1_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡵࡢࡸࡴࡥࡷࡳࡣࡳࠦᅥ")) })
                bstack1ll1ll1111l_opy_.update({bstack1l1_opy_ (u"ࠤࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠤᅦ"): accessibility })
        return bstack1ll1ll1111l_opy_
    def bstack1ll1ll11l1l_opy_(self, bstack1lll11111l1_opy_: str = None, bstack1lll111lll1_opy_: str = None, bstack1l1ll111l_opy_: int = None):
        if not self.cli_bin_session_id or not self.bstack111ll1l11l_opy_:
            return
        bstack11l1l1ll11_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if bstack1l1ll111l_opy_:
            req.bstack1l1ll111l_opy_ = bstack1l1ll111l_opy_
        if bstack1lll11111l1_opy_:
            req.bstack1lll11111l1_opy_ = bstack1lll11111l1_opy_
        if bstack1lll111lll1_opy_:
            req.bstack1lll111lll1_opy_ = bstack1lll111lll1_opy_
        try:
            r = self.bstack111ll1l11l_opy_.StopBinSession(req)
            self.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡷࡳࡵࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࠦᅧ"), datetime.now() - bstack11l1l1ll11_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack11l1ll11ll_opy_(self, key: str, value: timedelta):
        tag = bstack1l1_opy_ (u"ࠦࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶࠦᅨ") if self.bstack1ll1ll1l1l_opy_() else bstack1l1_opy_ (u"ࠧࡳࡡࡪࡰ࠰ࡴࡷࡵࡣࡦࡵࡶࠦᅩ")
        self.bstack1ll1ll1l11l_opy_[bstack1l1_opy_ (u"ࠨ࠺ࠣᅪ").join([tag + bstack1l1_opy_ (u"ࠢ࠮ࠤᅫ") + str(id(self)), key])] += value
    def bstack11l111ll11_opy_(self):
        if not os.getenv(bstack1l1_opy_ (u"ࠣࡆࡈࡆ࡚ࡍ࡟ࡑࡇࡕࡊࠧᅬ"), bstack1l1_opy_ (u"ࠤ࠳ࠦᅭ")) == bstack1l1_opy_ (u"ࠥ࠵ࠧᅮ"):
            return
        bstack1ll1lllll11_opy_ = dict()
        bstack1lllll11ll1_opy_ = []
        if self.test_framework:
            bstack1lllll11ll1_opy_.extend(list(self.test_framework.bstack1lllll11ll1_opy_.values()))
        if self.bstack111l11l1l1_opy_:
            bstack1lllll11ll1_opy_.extend(list(self.bstack111l11l1l1_opy_.bstack1lllll11ll1_opy_.values()))
        for instance in bstack1lllll11ll1_opy_:
            if not instance.platform_index in bstack1ll1lllll11_opy_:
                bstack1ll1lllll11_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1ll1lllll11_opy_[instance.platform_index]
            for k, v in instance.bstack11111l1111_opy_().items():
                report[k] += v
                report[k.split(bstack1l1_opy_ (u"ࠦ࠿ࠨᅯ"))[0]] += v
        bstack1ll1l11llll_opy_ = sorted([(k, v) for k, v in self.bstack1ll1ll1l11l_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1ll1ll1ll1l_opy_ = 0
        for r in bstack1ll1l11llll_opy_:
            bstack1ll1llll11l_opy_ = r[1].total_seconds()
            bstack1ll1ll1ll1l_opy_ += bstack1ll1llll11l_opy_
            self.logger.debug(bstack1l1_opy_ (u"ࠧࡡࡰࡦࡴࡩࡡࠥࡩ࡬ࡪ࠼ࡾࡶࡠ࠶࡝ࡾ࠿ࠥᅰ") + str(bstack1ll1llll11l_opy_) + bstack1l1_opy_ (u"ࠨࠢᅱ"))
        self.logger.debug(bstack1l1_opy_ (u"ࠢ࠮࠯ࠥᅲ"))
        bstack1lll1111l1l_opy_ = []
        for platform_index, report in bstack1ll1lllll11_opy_.items():
            bstack1lll1111l1l_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1lll1111l1l_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack11111111_opy_ = set()
        bstack1ll1ll11l11_opy_ = 0
        for r in bstack1lll1111l1l_opy_:
            bstack1ll1llll11l_opy_ = r[2].total_seconds()
            bstack1ll1ll11l11_opy_ += bstack1ll1llll11l_opy_
            bstack11111111_opy_.add(r[0])
            self.logger.debug(bstack1l1_opy_ (u"ࠣ࡝ࡳࡩࡷ࡬࡝ࠡࡶࡨࡷࡹࡀࡰ࡭ࡣࡷࡪࡴࡸ࡭࠮ࡽࡵ࡟࠵ࡣࡽ࠻ࡽࡵ࡟࠶ࡣࡽ࠾ࠤᅳ") + str(bstack1ll1llll11l_opy_) + bstack1l1_opy_ (u"ࠤࠥᅴ"))
        if self.bstack1ll1ll1l1l_opy_():
            self.logger.debug(bstack1l1_opy_ (u"ࠥ࠱࠲ࠨᅵ"))
            self.logger.debug(bstack1l1_opy_ (u"ࠦࡠࡶࡥࡳࡨࡠࠤࡨࡲࡩ࠻ࡥ࡫࡭ࡱࡪ࠭ࡱࡴࡲࡧࡪࡹࡳ࠾ࡽࡷࡳࡹࡧ࡬ࡠࡥ࡯࡭ࢂࠦࡴࡦࡵࡷ࠾ࡵࡲࡡࡵࡨࡲࡶࡲࡹ࠭ࡼࡵࡷࡶ࠭ࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠪࡿࡀࠦᅶ") + str(bstack1ll1ll11l11_opy_) + bstack1l1_opy_ (u"ࠧࠨᅷ"))
        else:
            self.logger.debug(bstack1l1_opy_ (u"ࠨ࡛ࡱࡧࡵࡪࡢࠦࡣ࡭࡫࠽ࡱࡦ࡯࡮࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠿ࠥᅸ") + str(bstack1ll1ll1ll1l_opy_) + bstack1l1_opy_ (u"ࠢࠣᅹ"))
        self.logger.debug(bstack1l1_opy_ (u"ࠣ࠯࠰ࠦᅺ"))
    def bstack1ll1l11l1ll_opy_(self, r):
        if r is not None and getattr(r, bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࠪᅻ"), None) and getattr(r.testhub, bstack1l1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡵࠪᅼ"), None):
            errors = json.loads(r.testhub.errors.decode(bstack1l1_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᅽ")))
            for bstack1ll1ll1l111_opy_, err in errors.items():
                if err[bstack1l1_opy_ (u"ࠬࡺࡹࡱࡧࠪᅾ")] == bstack1l1_opy_ (u"࠭ࡩ࡯ࡨࡲࠫᅿ"):
                    self.logger.info(err[bstack1l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᆀ")])
                else:
                    self.logger.error(err[bstack1l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᆁ")])
cli = SDKCLI()