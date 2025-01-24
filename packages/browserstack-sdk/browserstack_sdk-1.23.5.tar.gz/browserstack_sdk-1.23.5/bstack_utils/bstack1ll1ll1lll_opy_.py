# coding: UTF-8
import sys
bstack11lllll_opy_ = sys.version_info [0] == 2
bstack1l1l1_opy_ = 2048
bstack11ll11_opy_ = 7
def bstack11111_opy_ (bstack11l1lll_opy_):
    global bstack11l1l11_opy_
    bstack1ll1ll_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lllll1l_opy_ = bstack11l1lll_opy_ [:-1]
    bstack1l11_opy_ = bstack1ll1ll_opy_ % len (bstack1lllll1l_opy_)
    bstack1lllll1_opy_ = bstack1lllll1l_opy_ [:bstack1l11_opy_] + bstack1lllll1l_opy_ [bstack1l11_opy_:]
    if bstack11lllll_opy_:
        bstack11lll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1_opy_ - (bstack11111l_opy_ + bstack1ll1ll_opy_) % bstack11ll11_opy_) for bstack11111l_opy_, char in enumerate (bstack1lllll1_opy_)])
    else:
        bstack11lll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1_opy_ - (bstack11111l_opy_ + bstack1ll1ll_opy_) % bstack11ll11_opy_) for bstack11111l_opy_, char in enumerate (bstack1lllll1_opy_)])
    return eval (bstack11lll1l_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
from typing import Dict, List, Optional
from bstack_utils.constants import bstack111l111l1_opy_, EVENTS
from bstack_utils.helper import bstack11llll1l1l_opy_, get_host_info, bstack1llllll1l1_opy_
from datetime import datetime
from bstack_utils.bstack11l1l11ll_opy_ import get_logger
logger = get_logger(__name__)
bstack1ll1l11l1ll_opy_: Dict[str, float] = {}
bstack1ll1l11ll1l_opy_: List = []
bstack11l11ll1l_opy_ = os.path.join(os.getcwd(), bstack11111_opy_ (u"࠭࡬ࡰࡩࠪᙹ"), bstack11111_opy_ (u"ࠧ࡬ࡧࡼ࠱ࡲ࡫ࡴࡳ࡫ࡦࡷ࠳ࡰࡳࡰࡰࠪᙺ"))
lock = FileLock(bstack11l11ll1l_opy_+bstack11111_opy_ (u"ࠣ࠰࡯ࡳࡨࡱࠢᙻ"))
class bstack1ll1l11lll1_opy_:
    duration: float
    name: str
    startTime: float
    worker: int
    status: bool
    failure: str
    details: Optional[str]
    entryType: str
    platform: Optional[int]
    command: Optional[str]
    hookType: Optional[str]
    def __init__(self, duration: float, name: str, start_time: float, bstack1ll1l11ll11_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack1ll1l11ll11_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack11111_opy_ (u"ࠤࡰࡩࡦࡹࡵࡳࡧࠥᙼ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
class bstack1llllllllll_opy_:
    global bstack1ll1l11l1ll_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack1ll1l11l1ll_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨᙽ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1llllllllll_opy_.mark(end)
            bstack1llllllllll_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠦࡊࡸࡲࡰࡴ࠽ࠤࢀࢃࠢᙾ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack1ll1l11l1ll_opy_ or end not in bstack1ll1l11l1ll_opy_:
                logger.debug(bstack11111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡶࡤࡶࡹࠦ࡫ࡦࡻࠣࡻ࡮ࡺࡨࠡࡸࡤࡰࡺ࡫ࠠࡼࡿࠣࡳࡷࠦࡥ࡯ࡦࠣ࡯ࡪࡿࠠࡸ࡫ࡷ࡬ࠥࡼࡡ࡭ࡷࡨࠤࢀࢃࠢᙿ").format(start,end))
                return
            duration: float = bstack1ll1l11l1ll_opy_[end] - bstack1ll1l11l1ll_opy_[start]
            bstack1ll1l11l1l1_opy_: bstack1ll1l11lll1_opy_ = bstack1ll1l11lll1_opy_(duration, label, bstack1ll1l11l1ll_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack11111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝ࠨ "), 0), command, test_name, hook_type)
            del bstack1ll1l11l1ll_opy_[start]
            del bstack1ll1l11l1ll_opy_[end]
            bstack1llllllllll_opy_.bstack1ll1l11llll_opy_(bstack1ll1l11l1l1_opy_)
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠢࡆࡴࡵࡳࡷࡀࠠࡼࡿࠥᚁ").format(e))
    @staticmethod
    def bstack1ll1l11llll_opy_(bstack1ll1l11l1l1_opy_):
        os.makedirs(os.path.dirname(bstack11l11ll1l_opy_)) if not os.path.exists(os.path.dirname(bstack11l11ll1l_opy_)) else None
        try:
            with lock:
                with open(bstack11l11ll1l_opy_, bstack11111_opy_ (u"ࠣࡴ࠮ࠦᚂ"), encoding=bstack11111_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᚃ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack1ll1l11l1l1_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError:
            with lock:
                with open(bstack11l11ll1l_opy_, bstack11111_opy_ (u"ࠥࡻࠧᚄ"), encoding=bstack11111_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᚅ")) as file:
                    data = [bstack1ll1l11l1l1_opy_.__dict__]
                    json.dump(data, file, indent=4)
    @staticmethod
    def bstack11111l11ll_opy_(label: str) -> str:
        try:
            return bstack11111_opy_ (u"ࠧࢁࡽ࠻ࡽࢀࠦᚆ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠨࡅࡳࡴࡲࡶ࠿ࠦࡻࡾࠤᚇ").format(e))