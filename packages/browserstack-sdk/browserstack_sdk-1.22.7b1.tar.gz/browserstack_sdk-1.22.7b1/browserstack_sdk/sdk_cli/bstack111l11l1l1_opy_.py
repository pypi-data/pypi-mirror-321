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
from typing import Dict, Tuple, Callable, Type, List, Any
import abc
from datetime import datetime, timezone, timedelta
from browserstack_sdk.sdk_cli.bstack11111l1l11_opy_ import bstack111111llll_opy_, bstack1111llll11_opy_
class bstack111ll11111_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack1l1_opy_ (u"ࠣࡊࡲࡳࡰ࡙ࡴࡢࡶࡨ࠲ࢀࢃࠢአ").format(self.name)
class bstack111ll1ll11_opy_(Enum):
    NONE = 0
    bstack111ll11l11_opy_ = 1
    bstack111ll1l1l1_opy_ = 2
    bstack1l1llll11l1_opy_ = 3
    QUIT = 4
    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    def __repr__(self) -> str:
        return bstack1l1_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡔࡶࡤࡸࡪ࠴ࡻࡾࠤኡ").format(self.name)
class bstack111l1llll1_opy_(bstack111111llll_opy_):
    framework_name: str
    framework_version: str
    state: bstack111ll1ll11_opy_
    previous_state: bstack111ll1ll11_opy_
    bstack11111l1lll_opy_: datetime
    bstack1l1lllllll1_opy_: datetime
    def __init__(
        self,
        context: bstack1111llll11_opy_,
        framework_name: str,
        framework_version: str,
        state=bstack111ll1ll11_opy_.NONE,
    ):
        super().__init__(context)
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.state = state
        self.previous_state = bstack111ll1ll11_opy_.NONE
        self.bstack11111l1lll_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1lllllll1_opy_ = datetime.now(tz=timezone.utc)
    def bstack111l1ll11l_opy_(self, bstack1ll11111111_opy_: bstack111ll1ll11_opy_):
        bstack1l1llllll11_opy_ = bstack111ll1ll11_opy_(bstack1ll11111111_opy_).name
        if not bstack1l1llllll11_opy_:
            return False
        if bstack1ll11111111_opy_ == self.state:
            return False
        if (
            bstack1ll11111111_opy_ == bstack111ll1ll11_opy_.NONE
            or (self.state != bstack111ll1ll11_opy_.NONE and bstack1ll11111111_opy_ == bstack111ll1ll11_opy_.bstack111ll11l11_opy_)
            or (self.state < bstack111ll1ll11_opy_.bstack111ll11l11_opy_ and bstack1ll11111111_opy_ == bstack111ll1ll11_opy_.bstack111ll1l1l1_opy_)
            or (self.state < bstack111ll1ll11_opy_.bstack111ll11l11_opy_ and bstack1ll11111111_opy_ == bstack111ll1ll11_opy_.QUIT)
        ):
            raise ValueError(bstack1l1_opy_ (u"ࠥ࡭ࡳࡼࡡ࡭࡫ࡧࠤࡸࡺࡡࡵࡧࠣࡸࡷࡧ࡮ࡴ࡫ࡷ࡭ࡴࡴ࠺ࠡࠤኢ") + str(self.state) + bstack1l1_opy_ (u"ࠦࠥࡃ࠾ࠡࠤኣ") + str(bstack1ll11111111_opy_))
        self.previous_state = self.state
        self.state = bstack1ll11111111_opy_
        self.bstack1l1lllllll1_opy_ = datetime.now(tz=timezone.utc)
        return True
class bstack11111ll111_opy_(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lllll11ll1_opy_: Dict[str, bstack111l1llll1_opy_] = dict()
    framework_name: str
    framework_version: str
    classes: List[Type]
    def __init__(
        self,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
    ):
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.classes = classes
    @abc.abstractmethod
    def bstack1l1lllll11l_opy_(self, instance: bstack111l1llll1_opy_, method_name: str, bstack1l1llll1ll1_opy_: timedelta, *args, **kwargs):
        return
    @abc.abstractmethod
    def bstack1l1llll1l11_opy_(
        self, method_name, previous_state: bstack111ll1ll11_opy_, *args, **kwargs
    ) -> bstack111ll1ll11_opy_:
        return
    @abc.abstractmethod
    def bstack1l1llll1l1l_opy_(
        self,
        target: object,
        exec: Tuple[bstack111l1llll1_opy_, str],
        bstack111ll111l1_opy_: Tuple[bstack111ll1ll11_opy_, bstack111ll11111_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable:
        return
    def bstack1l1lllll1ll_opy_(self, bstack1l1llll111l_opy_: List[str]):
        for clazz in self.classes:
            for method_name in bstack1l1llll111l_opy_:
                bstack1l1llll1lll_opy_ = getattr(clazz, method_name, None)
                if not callable(bstack1l1llll1lll_opy_):
                    self.logger.warning(bstack1l1_opy_ (u"ࠧࡻ࡮ࡱࡣࡷࡧ࡭࡫ࡤࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠢࠥኤ") + str(method_name) + bstack1l1_opy_ (u"ࠨࠢእ"))
                    continue
                bstack1l1llll1111_opy_ = self.bstack1l1llll1l11_opy_(
                    method_name, previous_state=bstack111ll1ll11_opy_.NONE
                )
                bstack1l1llll11ll_opy_ = self.bstack1l1lllll111_opy_(
                    method_name,
                    (bstack1l1llll1111_opy_ if bstack1l1llll1111_opy_ else bstack111ll1ll11_opy_.NONE),
                    bstack1l1llll1lll_opy_,
                )
                if not callable(bstack1l1llll11ll_opy_):
                    self.logger.warning(bstack1l1_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪࠠ࡯ࡱࡷࠤࡵࡧࡴࡤࡪࡨࡨ࠿ࠦࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࠨࡼࡵࡨࡰ࡫࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽ࠻ࠢࠥኦ") + str(self.framework_version) + bstack1l1_opy_ (u"ࠣࠫࠥኧ"))
                    continue
                setattr(clazz, method_name, bstack1l1llll11ll_opy_)
    def bstack1l1lllll111_opy_(
        self,
        method_name: str,
        bstack1l1llll1111_opy_: bstack111ll1ll11_opy_,
        bstack1l1llll1lll_opy_: Callable,
    ):
        def wrapped(target, *args, **kwargs):
            bstack11l1l1ll11_opy_ = datetime.now()
            (bstack1l1llll1111_opy_,) = wrapped.__vars__
            bstack1l1llll1111_opy_ = (
                bstack1l1llll1111_opy_
                if bstack1l1llll1111_opy_ and bstack1l1llll1111_opy_ != bstack111ll1ll11_opy_.NONE
                else self.bstack1l1llll1l11_opy_(method_name, previous_state=bstack1l1llll1111_opy_, *args, **kwargs)
            )
            if bstack1l1llll1111_opy_ == bstack111ll1ll11_opy_.bstack111ll11l11_opy_:
                ctx = bstack111111llll_opy_.create_context(target)
                bstack11111ll111_opy_.bstack1lllll11ll1_opy_[ctx.id] = bstack111l1llll1_opy_(
                    ctx, self.framework_name, self.framework_version, bstack1l1llll1111_opy_
                )
                self.logger.debug(bstack1l1_opy_ (u"ࠤࡺࡶࡦࡶࡰࡦࡦࠣࡱࡪࡺࡨࡰࡦࠣࡧࡷ࡫ࡡࡵࡧࡧ࠾ࠥࢁࡴࡢࡴࡪࡩࡹ࠴࡟ࡠࡥ࡯ࡥࡸࡹ࡟ࡠࡿࠣࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥ࠾ࡽࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫ࡽࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡤࡶࡻࡁࢀࡩࡴࡹ࠰࡬ࡨࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࡴ࠿ࠥከ") + str(bstack11111ll111_opy_.bstack1lllll11ll1_opy_.keys()) + bstack1l1_opy_ (u"ࠥࠦኩ"))
            else:
                self.logger.debug(bstack1l1_opy_ (u"ࠦࡼࡸࡡࡱࡲࡨࡨࠥࡳࡥࡵࡪࡲࡨࠥ࡯࡮ࡷࡱ࡮ࡩࡩࡀࠠࡼࡶࡤࡶ࡬࡫ࡴ࠯ࡡࡢࡧࡱࡧࡳࡴࡡࡢࢁࠥࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࡀࡿࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦࡿࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࡂࢁࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷࡂࠨኪ") + str(bstack11111ll111_opy_.bstack1lllll11ll1_opy_.keys()) + bstack1l1_opy_ (u"ࠧࠨካ"))
            instance = bstack11111ll111_opy_.bstack1llllllll1l_opy_(target)
            if bstack1l1llll1111_opy_ == bstack111ll1ll11_opy_.NONE or not instance:
                ctx = bstack111111llll_opy_.create_context(target)
                self.logger.warning(bstack1l1_opy_ (u"ࠨࡷࡳࡣࡳࡴࡪࡪࠠ࡮ࡧࡷ࡬ࡴࡪࠠࡶࡰࡷࡶࡦࡩ࡫ࡦࡦ࠽ࠤࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡧࡹࡾ࠽ࡼࡥࡷࡼࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࡴ࠿ࠥኬ") + str(bstack11111ll111_opy_.bstack1lllll11ll1_opy_.keys()) + bstack1l1_opy_ (u"ࠢࠣክ"))
                return bstack1l1llll1lll_opy_(target, *args, **kwargs)
            bstack1lll1l11111_opy_ = self.bstack1l1llll1l1l_opy_(
                target,
                (instance, method_name),
                (bstack1l1llll1111_opy_, bstack111ll11111_opy_.PRE),
                None,
                *args,
                **kwargs,
            )
            if instance.bstack111l1ll11l_opy_(bstack1l1llll1111_opy_):
                self.logger.debug(bstack1l1_opy_ (u"ࠣࡣࡳࡴࡱ࡯ࡥࡥࠢࡶࡸࡦࡺࡥ࠮ࡶࡵࡥࡳࡹࡩࡵ࡫ࡲࡲ࠿ࠦࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡳࡶࡪࡼࡩࡰࡷࡶࡣࡸࡺࡡࡵࡧࢀࠤࡂࡄࠠࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡷࡹࡧࡴࡦࡿࠣࠬࢀࡺࡹࡱࡧࠫࡸࡦࡸࡧࡦࡶࠬࢁ࠳ࢁ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࢁࠥࢁࡡࡳࡩࡶࢁ࠮࡛ࠦࠣኮ") + str(instance.ref()) + bstack1l1_opy_ (u"ࠤࡠࠦኯ"))
            result = (
                bstack1lll1l11111_opy_(target, bstack1l1llll1lll_opy_, *args, **kwargs)
                if callable(bstack1lll1l11111_opy_)
                else bstack1l1llll1lll_opy_(target, *args, **kwargs)
            )
            bstack1l1lllll1l1_opy_ = self.bstack1l1llll1l1l_opy_(
                target,
                (instance, method_name),
                (bstack1l1llll1111_opy_, bstack111ll11111_opy_.POST),
                result,
                *args,
                **kwargs,
            )
            self.bstack1l1lllll11l_opy_(instance, method_name, datetime.now() - bstack11l1l1ll11_opy_, *args, **kwargs)
            return bstack1l1lllll1l1_opy_ if bstack1l1lllll1l1_opy_ else result
        wrapped.__name__ = method_name
        wrapped.__vars__ = (bstack1l1llll1111_opy_,)
        return wrapped
    @staticmethod
    def bstack1llllllll1l_opy_(target: object, strict=True):
        ctx = bstack111111llll_opy_.create_context(target)
        instance = bstack11111ll111_opy_.bstack1lllll11ll1_opy_.get(ctx.id, None)
        if instance and instance.bstack111111lll1_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1ll1l111l1l_opy_(
        ctx: bstack1111llll11_opy_, state: bstack111ll1ll11_opy_, reverse=True
    ) -> List[bstack111l1llll1_opy_]:
        return sorted(
            filter(
                lambda t: t.state == state
                and t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                bstack11111ll111_opy_.bstack1lllll11ll1_opy_.values(),
            ),
            key=lambda t: t.bstack11111l1lll_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack111lll1l1l_opy_(instance: bstack111l1llll1_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def bstack111l11ll11_opy_(instance: bstack111l1llll1_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack111l1ll11l_opy_(instance: bstack111l1llll1_opy_, key: str, value: Any) -> bool:
        instance.data[key] = value
        bstack11111ll111_opy_.logger.debug(bstack1l1_opy_ (u"ࠥࡷࡪࡺ࡟ࡴࡶࡤࡸࡪࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥࡱࡥࡺ࠿ࡾ࡯ࡪࡿࡽࠡࡸࡤࡰࡺ࡫࠽ࠣኰ") + str(value) + bstack1l1_opy_ (u"ࠦࠧ኱"))
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = bstack11111ll111_opy_.bstack1llllllll1l_opy_(target, strict)
        return bstack11111ll111_opy_.bstack111l11ll11_opy_(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = bstack11111ll111_opy_.bstack1llllllll1l_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True