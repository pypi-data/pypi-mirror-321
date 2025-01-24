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
import logging
from enum import Enum
import os
import threading
import traceback
from typing import Dict, List, Any, Callable, Tuple, Union
import abc
from datetime import datetime, timezone
from dataclasses import dataclass
from browserstack_sdk.sdk_cli.bstack11111l1l11_opy_ import bstack111111llll_opy_, bstack1111llll11_opy_
class bstack1111l11l11_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack1l1_opy_ (u"ࠣࡖࡨࡷࡹࡎ࡯ࡰ࡭ࡖࡸࡦࡺࡥ࠯ࡽࢀࠦቯ").format(self.name)
class bstack1111l11l1l_opy_(Enum):
    NONE = 0
    BEFORE_ALL = 1
    LOG = 2
    SETUP_FIXTURE = 3
    INIT_TEST = 4
    BEFORE_EACH = 5
    AFTER_EACH = 6
    TEST = 7
    STEP = 8
    LOG_REPORT = 9
    AFTER_ALL = 10
    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    def __repr__(self) -> str:
        return bstack1l1_opy_ (u"ࠤࡗࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡕࡷࡥࡹ࡫࠮ࡼࡿࠥተ").format(self.name)
class bstack1111ll1l11_opy_(bstack111111llll_opy_):
    bstack1llll1l1l11_opy_: List[str]
    bstack1lll1llllll_opy_: Dict[str, str]
    state: bstack1111l11l1l_opy_
    bstack11111l1lll_opy_: datetime
    bstack1l1lllllll1_opy_: datetime
    def __init__(
        self,
        context: bstack1111llll11_opy_,
        bstack1llll1l1l11_opy_: List[str],
        bstack1lll1llllll_opy_: Dict[str, str],
        state=bstack1111l11l1l_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1llll1l1l11_opy_ = bstack1llll1l1l11_opy_
        self.bstack1lll1llllll_opy_ = bstack1lll1llllll_opy_
        self.state = state
        self.bstack11111l1lll_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1lllllll1_opy_ = datetime.now(tz=timezone.utc)
    def bstack111l1ll11l_opy_(self, bstack1ll11111111_opy_: bstack1111l11l1l_opy_):
        bstack1l1llllll11_opy_ = bstack1111l11l1l_opy_(bstack1ll11111111_opy_).name
        if not bstack1l1llllll11_opy_:
            return False
        if bstack1ll11111111_opy_ == self.state:
            return False
        self.state = bstack1ll11111111_opy_
        self.bstack1l1lllllll1_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1lllll1ll1l_opy_:
    test_framework_name: str
    test_framework_version: str
    platform_index: int
@dataclass
class bstack1lll1ll111l_opy_:
    kind: str
    message: str
    level: Union[None, str] = None
    timestamp: Union[None, datetime] = datetime.now(tz=timezone.utc)
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1llll1ll1ll_opy_ = bstack1l1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡷࡸ࡭ࡩࠨቱ")
    bstack1llll1ll11l_opy_ = bstack1l1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡬ࡨࠧቲ")
    bstack1lllll1l111_opy_ = bstack1l1_opy_ (u"ࠧࡺࡥࡴࡶࡢࡲࡦࡳࡥࠣታ")
    bstack111111111l_opy_ = bstack1l1_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡡࡳࡥࡹ࡮ࠢቴ")
    bstack1lll1ll1l11_opy_ = bstack1l1_opy_ (u"ࠢࡵࡧࡶࡸࡤࡺࡡࡨࡵࠥት")
    bstack1111l1l1ll_opy_ = bstack1l1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡦࡵࡸࡰࡹࠨቶ")
    bstack1lll1ll1l1l_opy_ = bstack1l1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡧࡶࡹࡱࡺ࡟ࡢࡶࠥቷ")
    bstack1111111111_opy_ = bstack1l1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠧቸ")
    bstack1llll1lll1l_opy_ = bstack1l1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡨࡲࡩ࡫ࡤࡠࡣࡷࠦቹ")
    bstack1llllll1lll_opy_ = bstack1l1_opy_ (u"ࠧࡺࡥࡴࡶࡢࡰࡴࡩࡡࡵ࡫ࡲࡲࠧቺ")
    bstack1llllll111l_opy_ = bstack1l1_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࠧቻ")
    bstack1lll1l1llll_opy_ = bstack1l1_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠤቼ")
    bstack1lll1l1lll1_opy_ = bstack1l1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡣࡰࡦࡨࠦች")
    bstack1llllll1l11_opy_ = bstack1l1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡧࡵࡹࡳࡥ࡮ࡢ࡯ࡨࠦቾ")
    bstack111l111l11_opy_ = bstack1l1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࠦቿ")
    bstack1111lll11l_opy_ = bstack1l1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩࡥ࡮ࡲࡵࡳࡧࠥኀ")
    bstack1lll1ll11l1_opy_ = bstack1l1_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠤኁ")
    bstack1lllll11lll_opy_ = bstack1l1_opy_ (u"ࠨࡴࡦࡵࡷࡣࡱࡵࡧࡴࠤኂ")
    bstack1lll1ll1lll_opy_ = bstack1l1_opy_ (u"ࠢࡵࡧࡶࡸࡤࡳࡥࡵࡣࠥኃ")
    bstack1111l1l1l1_opy_ = bstack1l1_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵࡧࡢࡷࡪࡹࡳࡪࡱࡱࡣࡳࡧ࡭ࡦࠤኄ")
    bstack11111111l1_opy_ = bstack1l1_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠧኅ")
    bstack1llll1llll1_opy_ = bstack1l1_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡࡨࡲࡩ࡫ࡤࡠࡣࡷࠦኆ")
    bstack1lllllll1ll_opy_ = bstack1l1_opy_ (u"ࠦ࡭ࡵ࡯࡬ࡡ࡬ࡨࠧኇ")
    bstack1lll1llll11_opy_ = bstack1l1_opy_ (u"ࠧ࡮࡯ࡰ࡭ࡢࡶࡪࡹࡵ࡭ࡶࠥኈ")
    bstack1llllll1ll1_opy_ = bstack1l1_opy_ (u"ࠨࡨࡰࡱ࡮ࡣࡱࡵࡧࡴࠤ኉")
    bstack1lllll111l1_opy_ = bstack1l1_opy_ (u"ࠢࡩࡱࡲ࡯ࡤࡴࡡ࡮ࡧࠥኊ")
    bstack1llll11l111_opy_ = bstack1l1_opy_ (u"ࠣࡲࡨࡲࡩ࡯࡮ࡨࠤኋ")
    bstack1llllll11l1_opy_ = bstack1l1_opy_ (u"ࠤࡳࡩࡳࡪࡩ࡯ࡩࠥኌ")
    bstack1ll11ll1l1l_opy_ = bstack1l1_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࠧኍ")
    bstack1lllll1111l_opy_ = bstack1l1_opy_ (u"࡙ࠦࡋࡓࡕࡡࡏࡓࡌࠨ኎")
    bstack1lllll11ll1_opy_: Dict[str, bstack1111ll1l11_opy_] = dict()
    bstack1l1llllllll_opy_: Dict[str, List[Callable]] = dict()
    bstack1llll1l1l11_opy_: List[str]
    bstack1lll1llllll_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1llll1l1l11_opy_: List[str],
        bstack1lll1llllll_opy_: Dict[str, str],
    ):
        self.bstack1llll1l1l11_opy_ = bstack1llll1l1l11_opy_
        self.bstack1lll1llllll_opy_ = bstack1lll1llllll_opy_
    def track_event(
        self,
        context: bstack1lllll1ll1l_opy_,
        test_framework_state: bstack1111l11l1l_opy_,
        test_hook_state: bstack1111l11l11_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack1l1_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂࠦࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦ኏") + str(kwargs) + bstack1l1_opy_ (u"ࠨࠢነ"))
    def bstack1llll1111ll_opy_(
        self,
        instance: bstack1111ll1l11_opy_,
        bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_],
        *args,
        **kwargs,
    ):
        bstack1ll111111l1_opy_ = TestFramework.bstack1l1llllll1l_opy_(bstack111ll111l1_opy_)
        if not bstack1ll111111l1_opy_ in TestFramework.bstack1l1llllllll_opy_:
            return
        self.logger.debug(bstack1l1_opy_ (u"ࠢࡪࡰࡹࡳࡰ࡯࡮ࡨࠢࠥኑ") + str(len(TestFramework.bstack1l1llllllll_opy_[bstack1ll111111l1_opy_])) + bstack1l1_opy_ (u"ࠣࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࡷࠧኒ"))
        for callback in TestFramework.bstack1l1llllllll_opy_[bstack1ll111111l1_opy_]:
            try:
                callback(self, instance, bstack111ll111l1_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack1l1_opy_ (u"ࠤࡨࡶࡷࡵࡲࠡ࡫ࡱࡺࡴࡱࡩ࡯ࡩࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࠢና") + str(e) + bstack1l1_opy_ (u"ࠥࠦኔ"))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1lllllllll1_opy_(self):
        return
    @abc.abstractmethod
    def bstack1llll1lllll_opy_(self, instance, bstack111ll111l1_opy_):
        return
    @abc.abstractmethod
    def bstack1llll11ll1l_opy_(self, instance, bstack111ll111l1_opy_):
        return
    @staticmethod
    def bstack1llllllll1l_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack111111llll_opy_.create_context(target)
        instance = TestFramework.bstack1lllll11ll1_opy_.get(ctx.id, None)
        if instance and instance.bstack111111lll1_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1ll11ll1lll_opy_(reverse=True) -> List[bstack1111ll1l11_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1lllll11ll1_opy_.values(),
            ),
            key=lambda t: t.bstack11111l1lll_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1ll1l111l1l_opy_(ctx: bstack1111llll11_opy_, reverse=True) -> List[bstack1111ll1l11_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1lllll11ll1_opy_.values(),
            ),
            key=lambda t: t.bstack11111l1lll_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack111lll1l1l_opy_(instance: bstack1111ll1l11_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def bstack111l11ll11_opy_(instance: bstack1111ll1l11_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack111l1ll11l_opy_(instance: bstack1111ll1l11_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack1l1_opy_ (u"ࠦࡸ࡫ࡴࡠࡵࡷࡥࡹ࡫࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦ࡫ࡦࡻࡀࡿࡰ࡫ࡹࡾࠢࡹࡥࡱࡻࡥ࠾ࠤን") + str(value) + bstack1l1_opy_ (u"ࠧࠨኖ"))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1llll111l11_opy_(instance: bstack1111ll1l11_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack1l1_opy_ (u"ࠨࡳࡦࡶࡢࡷࡹࡧࡴࡦࡡࡨࡲࡹࡸࡩࡦࡵ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢࡨࡲࡹࡸࡩࡦࡵࡀࠦኗ") + str(entries) + bstack1l1_opy_ (u"ࠢࠣኘ"))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack1ll1111111l_opy_(instance: bstack1111l11l1l_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack1l1_opy_ (u"ࠣࡷࡳࡨࡦࡺࡥࡠࡵࡷࡥࡹ࡫࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦ࡫ࡦࡻࡀࡿࡰ࡫ࡹࡾࠢࡹࡥࡱࡻࡥ࠾ࠤኙ") + str(value) + bstack1l1_opy_ (u"ࠤࠥኚ"))
        instance.data.update(key, value)
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = TestFramework.bstack1llllllll1l_opy_(target, strict)
        return TestFramework.bstack111l11ll11_opy_(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = TestFramework.bstack1llllllll1l_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1l1llllll1l_opy_(bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_]):
        return bstack1l1_opy_ (u"ࠥ࠾ࠧኛ").join((bstack1111l11l1l_opy_(bstack111ll111l1_opy_[0]).name, bstack1111l11l11_opy_(bstack111ll111l1_opy_[1]).name))
    @staticmethod
    def bstack111l1ll111_opy_(bstack111ll111l1_opy_: Tuple[bstack1111l11l1l_opy_, bstack1111l11l11_opy_], callback: Callable):
        bstack1ll111111l1_opy_ = TestFramework.bstack1l1llllll1l_opy_(bstack111ll111l1_opy_)
        TestFramework.logger.debug(bstack1l1_opy_ (u"ࠦࡸ࡫ࡴࡠࡪࡲࡳࡰࡥࡣࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢ࡫ࡳࡴࡱ࡟ࡳࡧࡪ࡭ࡸࡺࡲࡺࡡ࡮ࡩࡾࡃࠢኜ") + str(bstack1ll111111l1_opy_) + bstack1l1_opy_ (u"ࠧࠨኝ"))
        if not bstack1ll111111l1_opy_ in TestFramework.bstack1l1llllllll_opy_:
            TestFramework.bstack1l1llllllll_opy_[bstack1ll111111l1_opy_] = []
        TestFramework.bstack1l1llllllll_opy_[bstack1ll111111l1_opy_].append(callback)
    @staticmethod
    def bstack1lllllll111_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack1l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡸ࡮ࡴࡳࠣኞ"):
            return klass.__qualname__
        return module + bstack1l1_opy_ (u"ࠢ࠯ࠤኟ") + klass.__qualname__
    @staticmethod
    def bstack1llll1lll11_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}