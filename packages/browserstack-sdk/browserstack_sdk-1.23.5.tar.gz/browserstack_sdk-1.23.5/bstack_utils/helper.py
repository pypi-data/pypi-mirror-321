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
import datetime
import json
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
import sys
import logging
from math import ceil
import urllib
from urllib.parse import urlparse
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import (bstack1llll1ll1ll_opy_, bstack11ll1l111_opy_, bstack1lll1lll1l_opy_, bstack11l1ll111_opy_,
                                    bstack1llll1ll1l1_opy_, bstack1lllll111ll_opy_, bstack1llll1lll11_opy_, bstack1llll1l1ll1_opy_)
from bstack_utils.messages import bstack1l11l1llll_opy_, bstack1l1111l1ll_opy_
from bstack_utils.proxy import bstack1llll1llll_opy_, bstack1llll111ll_opy_
bstack1llllll1l1_opy_ = Config.bstack11lll111l_opy_()
logger = logging.getLogger(__name__)
def bstack111111l11l_opy_(config):
    return config[bstack11111_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᑆ")]
def bstack111111lll1_opy_(config):
    return config[bstack11111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᑇ")]
def bstack1lll111ll1_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack1lll1111ll1_opy_(obj):
    values = []
    bstack1lll11lll11_opy_ = re.compile(bstack11111_opy_ (u"ࡷࠨ࡞ࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣࡡࡪࠫࠥࠤᑈ"), re.I)
    for key in obj.keys():
        if bstack1lll11lll11_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1lll1l11lll_opy_(config):
    tags = []
    tags.extend(bstack1lll1111ll1_opy_(os.environ))
    tags.extend(bstack1lll1111ll1_opy_(config))
    return tags
def bstack1llll1111ll_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack1lll11ll11l_opy_(bstack1lll111l111_opy_):
    if not bstack1lll111l111_opy_:
        return bstack11111_opy_ (u"࠭ࠧᑉ")
    return bstack11111_opy_ (u"ࠢࡼࡿࠣࠬࢀࢃࠩࠣᑊ").format(bstack1lll111l111_opy_.name, bstack1lll111l111_opy_.email)
def bstack11111111l1_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack1llll11111l_opy_ = repo.common_dir
        info = {
            bstack11111_opy_ (u"ࠣࡵ࡫ࡥࠧᑋ"): repo.head.commit.hexsha,
            bstack11111_opy_ (u"ࠤࡶ࡬ࡴࡸࡴࡠࡵ࡫ࡥࠧᑌ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11111_opy_ (u"ࠥࡦࡷࡧ࡮ࡤࡪࠥᑍ"): repo.active_branch.name,
            bstack11111_opy_ (u"ࠦࡹࡧࡧࠣᑎ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11111_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡹ࡫ࡲࠣᑏ"): bstack1lll11ll11l_opy_(repo.head.commit.committer),
            bstack11111_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡺࡥࡳࡡࡧࡥࡹ࡫ࠢᑐ"): repo.head.commit.committed_datetime.isoformat(),
            bstack11111_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࠢᑑ"): bstack1lll11ll11l_opy_(repo.head.commit.author),
            bstack11111_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࡠࡦࡤࡸࡪࠨᑒ"): repo.head.commit.authored_datetime.isoformat(),
            bstack11111_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡡࡰࡩࡸࡹࡡࡨࡧࠥᑓ"): repo.head.commit.message,
            bstack11111_opy_ (u"ࠥࡶࡴࡵࡴࠣᑔ"): repo.git.rev_parse(bstack11111_opy_ (u"ࠦ࠲࠳ࡳࡩࡱࡺ࠱ࡹࡵࡰ࡭ࡧࡹࡩࡱࠨᑕ")),
            bstack11111_opy_ (u"ࠧࡩ࡯࡮࡯ࡲࡲࡤ࡭ࡩࡵࡡࡧ࡭ࡷࠨᑖ"): bstack1llll11111l_opy_,
            bstack11111_opy_ (u"ࠨࡷࡰࡴ࡮ࡸࡷ࡫ࡥࡠࡩ࡬ࡸࡤࡪࡩࡳࠤᑗ"): subprocess.check_output([bstack11111_opy_ (u"ࠢࡨ࡫ࡷࠦᑘ"), bstack11111_opy_ (u"ࠣࡴࡨࡺ࠲ࡶࡡࡳࡵࡨࠦᑙ"), bstack11111_opy_ (u"ࠤ࠰࠱࡬࡯ࡴ࠮ࡥࡲࡱࡲࡵ࡮࠮ࡦ࡬ࡶࠧᑚ")]).strip().decode(
                bstack11111_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᑛ")),
            bstack11111_opy_ (u"ࠦࡱࡧࡳࡵࡡࡷࡥ࡬ࠨᑜ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11111_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡸࡥࡳࡪࡰࡦࡩࡤࡲࡡࡴࡶࡢࡸࡦ࡭ࠢᑝ"): repo.git.rev_list(
                bstack11111_opy_ (u"ࠨࡻࡾ࠰࠱ࡿࢂࠨᑞ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1lll111ll1l_opy_ = []
        for remote in remotes:
            bstack1lll11ll1ll_opy_ = {
                bstack11111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᑟ"): remote.name,
                bstack11111_opy_ (u"ࠣࡷࡵࡰࠧᑠ"): remote.url,
            }
            bstack1lll111ll1l_opy_.append(bstack1lll11ll1ll_opy_)
        bstack1lll1111111_opy_ = {
            bstack11111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᑡ"): bstack11111_opy_ (u"ࠥ࡫࡮ࡺࠢᑢ"),
            **info,
            bstack11111_opy_ (u"ࠦࡷ࡫࡭ࡰࡶࡨࡷࠧᑣ"): bstack1lll111ll1l_opy_
        }
        bstack1lll1111111_opy_ = bstack1lll1lll1ll_opy_(bstack1lll1111111_opy_)
        return bstack1lll1111111_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡵࡰࡶ࡮ࡤࡸ࡮ࡴࡧࠡࡉ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣᑤ").format(err))
        return {}
def bstack1lll1lll1ll_opy_(bstack1lll1111111_opy_):
    bstack1lll1l111ll_opy_ = bstack1lll1l1l1l1_opy_(bstack1lll1111111_opy_)
    if bstack1lll1l111ll_opy_ and bstack1lll1l111ll_opy_ > bstack1llll1ll1l1_opy_:
        bstack1lll1l1111l_opy_ = bstack1lll1l111ll_opy_ - bstack1llll1ll1l1_opy_
        bstack1ll1llllll1_opy_ = bstack1lll111111l_opy_(bstack1lll1111111_opy_[bstack11111_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠢᑥ")], bstack1lll1l1111l_opy_)
        bstack1lll1111111_opy_[bstack11111_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠣᑦ")] = bstack1ll1llllll1_opy_
        logger.info(bstack11111_opy_ (u"ࠣࡖ࡫ࡩࠥࡩ࡯࡮࡯࡬ࡸࠥ࡮ࡡࡴࠢࡥࡩࡪࡴࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦ࠱ࠤࡘ࡯ࡺࡦࠢࡲࡪࠥࡩ࡯࡮࡯࡬ࡸࠥࡧࡦࡵࡧࡵࠤࡹࡸࡵ࡯ࡥࡤࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤࢀࢃࠠࡌࡄࠥᑧ")
                    .format(bstack1lll1l1l1l1_opy_(bstack1lll1111111_opy_) / 1024))
    return bstack1lll1111111_opy_
def bstack1lll1l1l1l1_opy_(bstack1llllll1l_opy_):
    try:
        if bstack1llllll1l_opy_:
            bstack1lll11ll111_opy_ = json.dumps(bstack1llllll1l_opy_)
            bstack1lll11lll1l_opy_ = sys.getsizeof(bstack1lll11ll111_opy_)
            return bstack1lll11lll1l_opy_
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠤࡖࡳࡲ࡫ࡴࡩ࡫ࡱ࡫ࠥࡽࡥ࡯ࡶࠣࡻࡷࡵ࡮ࡨࠢࡺ࡬࡮ࡲࡥࠡࡥࡤࡰࡨࡻ࡬ࡢࡶ࡬ࡲ࡬ࠦࡳࡪࡼࡨࠤࡴ࡬ࠠࡋࡕࡒࡒࠥࡵࡢ࡫ࡧࡦࡸ࠿ࠦࡻࡾࠤᑨ").format(e))
    return -1
def bstack1lll111111l_opy_(field, bstack1llll11ll11_opy_):
    try:
        bstack1lll1ll111l_opy_ = len(bytes(bstack1lllll111ll_opy_, bstack11111_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᑩ")))
        bstack1lll1lllll1_opy_ = bytes(field, bstack11111_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᑪ"))
        bstack1lll1l11111_opy_ = len(bstack1lll1lllll1_opy_)
        bstack1lll1l1ll11_opy_ = ceil(bstack1lll1l11111_opy_ - bstack1llll11ll11_opy_ - bstack1lll1ll111l_opy_)
        if bstack1lll1l1ll11_opy_ > 0:
            bstack1lll11l1ll1_opy_ = bstack1lll1lllll1_opy_[:bstack1lll1l1ll11_opy_].decode(bstack11111_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᑫ"), errors=bstack11111_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪ࠭ᑬ")) + bstack1lllll111ll_opy_
            return bstack1lll11l1ll1_opy_
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡺࡲࡶࡰࡦࡥࡹ࡯࡮ࡨࠢࡩ࡭ࡪࡲࡤ࠭ࠢࡱࡳࡹ࡮ࡩ࡯ࡩࠣࡻࡦࡹࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦࠣ࡬ࡪࡸࡥ࠻ࠢࡾࢁࠧᑭ").format(e))
    return field
def bstack11l1llll_opy_():
    env = os.environ
    if (bstack11111_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡘࡖࡑࠨᑮ") in env and len(env[bstack11111_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢ࡙ࡗࡒࠢᑯ")]) > 0) or (
            bstack11111_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣࡍࡕࡍࡆࠤᑰ") in env and len(env[bstack11111_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤࡎࡏࡎࡇࠥᑱ")]) > 0):
        return {
            bstack11111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᑲ"): bstack11111_opy_ (u"ࠨࡊࡦࡰ࡮࡭ࡳࡹࠢᑳ"),
            bstack11111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᑴ"): env.get(bstack11111_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᑵ")),
            bstack11111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᑶ"): env.get(bstack11111_opy_ (u"ࠥࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᑷ")),
            bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᑸ"): env.get(bstack11111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᑹ"))
        }
    if env.get(bstack11111_opy_ (u"ࠨࡃࡊࠤᑺ")) == bstack11111_opy_ (u"ࠢࡵࡴࡸࡩࠧᑻ") and bstack1llll1lll1_opy_(env.get(bstack11111_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡄࡋࠥᑼ"))):
        return {
            bstack11111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᑽ"): bstack11111_opy_ (u"ࠥࡇ࡮ࡸࡣ࡭ࡧࡆࡍࠧᑾ"),
            bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᑿ"): env.get(bstack11111_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᒀ")),
            bstack11111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᒁ"): env.get(bstack11111_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡋࡑࡅࠦᒂ")),
            bstack11111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᒃ"): env.get(bstack11111_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࠧᒄ"))
        }
    if env.get(bstack11111_opy_ (u"ࠥࡇࡎࠨᒅ")) == bstack11111_opy_ (u"ࠦࡹࡸࡵࡦࠤᒆ") and bstack1llll1lll1_opy_(env.get(bstack11111_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࠧᒇ"))):
        return {
            bstack11111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᒈ"): bstack11111_opy_ (u"ࠢࡕࡴࡤࡺ࡮ࡹࠠࡄࡋࠥᒉ"),
            bstack11111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᒊ"): env.get(bstack11111_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡅ࡙ࡎࡒࡄࡠ࡙ࡈࡆࡤ࡛ࡒࡍࠤᒋ")),
            bstack11111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᒌ"): env.get(bstack11111_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᒍ")),
            bstack11111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᒎ"): env.get(bstack11111_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᒏ"))
        }
    if env.get(bstack11111_opy_ (u"ࠢࡄࡋࠥᒐ")) == bstack11111_opy_ (u"ࠣࡶࡵࡹࡪࠨᒑ") and env.get(bstack11111_opy_ (u"ࠤࡆࡍࡤࡔࡁࡎࡇࠥᒒ")) == bstack11111_opy_ (u"ࠥࡧࡴࡪࡥࡴࡪ࡬ࡴࠧᒓ"):
        return {
            bstack11111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᒔ"): bstack11111_opy_ (u"ࠧࡉ࡯ࡥࡧࡶ࡬࡮ࡶࠢᒕ"),
            bstack11111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᒖ"): None,
            bstack11111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᒗ"): None,
            bstack11111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᒘ"): None
        }
    if env.get(bstack11111_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡒࡂࡐࡆࡌࠧᒙ")) and env.get(bstack11111_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨᒚ")):
        return {
            bstack11111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᒛ"): bstack11111_opy_ (u"ࠧࡈࡩࡵࡤࡸࡧࡰ࡫ࡴࠣᒜ"),
            bstack11111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᒝ"): env.get(bstack11111_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡋࡎ࡚࡟ࡉࡖࡗࡔࡤࡕࡒࡊࡉࡌࡒࠧᒞ")),
            bstack11111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᒟ"): None,
            bstack11111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᒠ"): env.get(bstack11111_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᒡ"))
        }
    if env.get(bstack11111_opy_ (u"ࠦࡈࡏࠢᒢ")) == bstack11111_opy_ (u"ࠧࡺࡲࡶࡧࠥᒣ") and bstack1llll1lll1_opy_(env.get(bstack11111_opy_ (u"ࠨࡄࡓࡑࡑࡉࠧᒤ"))):
        return {
            bstack11111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᒥ"): bstack11111_opy_ (u"ࠣࡆࡵࡳࡳ࡫ࠢᒦ"),
            bstack11111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᒧ"): env.get(bstack11111_opy_ (u"ࠥࡈࡗࡕࡎࡆࡡࡅ࡙ࡎࡒࡄࡠࡎࡌࡒࡐࠨᒨ")),
            bstack11111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᒩ"): None,
            bstack11111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᒪ"): env.get(bstack11111_opy_ (u"ࠨࡄࡓࡑࡑࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᒫ"))
        }
    if env.get(bstack11111_opy_ (u"ࠢࡄࡋࠥᒬ")) == bstack11111_opy_ (u"ࠣࡶࡵࡹࡪࠨᒭ") and bstack1llll1lll1_opy_(env.get(bstack11111_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࠧᒮ"))):
        return {
            bstack11111_opy_ (u"ࠥࡲࡦࡳࡥࠣᒯ"): bstack11111_opy_ (u"ࠦࡘ࡫࡭ࡢࡲ࡫ࡳࡷ࡫ࠢᒰ"),
            bstack11111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᒱ"): env.get(bstack11111_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡒࡖࡌࡇࡎࡊ࡜ࡄࡘࡎࡕࡎࡠࡗࡕࡐࠧᒲ")),
            bstack11111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᒳ"): env.get(bstack11111_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᒴ")),
            bstack11111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᒵ"): env.get(bstack11111_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡊࡐࡄࡢࡍࡉࠨᒶ"))
        }
    if env.get(bstack11111_opy_ (u"ࠦࡈࡏࠢᒷ")) == bstack11111_opy_ (u"ࠧࡺࡲࡶࡧࠥᒸ") and bstack1llll1lll1_opy_(env.get(bstack11111_opy_ (u"ࠨࡇࡊࡖࡏࡅࡇࡥࡃࡊࠤᒹ"))):
        return {
            bstack11111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᒺ"): bstack11111_opy_ (u"ࠣࡉ࡬ࡸࡑࡧࡢࠣᒻ"),
            bstack11111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᒼ"): env.get(bstack11111_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢ࡙ࡗࡒࠢᒽ")),
            bstack11111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᒾ"): env.get(bstack11111_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᒿ")),
            bstack11111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᓀ"): env.get(bstack11111_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡊࡆࠥᓁ"))
        }
    if env.get(bstack11111_opy_ (u"ࠣࡅࡌࠦᓂ")) == bstack11111_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᓃ") and bstack1llll1lll1_opy_(env.get(bstack11111_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࠨᓄ"))):
        return {
            bstack11111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᓅ"): bstack11111_opy_ (u"ࠧࡈࡵࡪ࡮ࡧ࡯࡮ࡺࡥࠣᓆ"),
            bstack11111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᓇ"): env.get(bstack11111_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᓈ")),
            bstack11111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᓉ"): env.get(bstack11111_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡒࡁࡃࡇࡏࠦᓊ")) or env.get(bstack11111_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡐࡄࡑࡊࠨᓋ")),
            bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᓌ"): env.get(bstack11111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᓍ"))
        }
    if bstack1llll1lll1_opy_(env.get(bstack11111_opy_ (u"ࠨࡔࡇࡡࡅ࡙ࡎࡒࡄࠣᓎ"))):
        return {
            bstack11111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᓏ"): bstack11111_opy_ (u"ࠣࡘ࡬ࡷࡺࡧ࡬ࠡࡕࡷࡹࡩ࡯࡯ࠡࡖࡨࡥࡲࠦࡓࡦࡴࡹ࡭ࡨ࡫ࡳࠣᓐ"),
            bstack11111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᓑ"): bstack11111_opy_ (u"ࠥࡿࢂࢁࡽࠣᓒ").format(env.get(bstack11111_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡈࡒ࡙ࡓࡊࡁࡕࡋࡒࡒࡘࡋࡒࡗࡇࡕ࡙ࡗࡏࠧᓓ")), env.get(bstack11111_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡓࡖࡔࡐࡅࡄࡖࡌࡈࠬᓔ"))),
            bstack11111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᓕ"): env.get(bstack11111_opy_ (u"ࠢࡔ࡛ࡖࡘࡊࡓ࡟ࡅࡇࡉࡍࡓࡏࡔࡊࡑࡑࡍࡉࠨᓖ")),
            bstack11111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᓗ"): env.get(bstack11111_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤᓘ"))
        }
    if bstack1llll1lll1_opy_(env.get(bstack11111_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࠧᓙ"))):
        return {
            bstack11111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᓚ"): bstack11111_opy_ (u"ࠧࡇࡰࡱࡸࡨࡽࡴࡸࠢᓛ"),
            bstack11111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᓜ"): bstack11111_opy_ (u"ࠢࡼࡿ࠲ࡴࡷࡵࡪࡦࡥࡷ࠳ࢀࢃ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠨᓝ").format(env.get(bstack11111_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢ࡙ࡗࡒࠧᓞ")), env.get(bstack11111_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡆࡉࡃࡐࡗࡑࡘࡤࡔࡁࡎࡇࠪᓟ")), env.get(bstack11111_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡖࡒࡐࡌࡈࡇ࡙ࡥࡓࡍࡗࡊࠫᓠ")), env.get(bstack11111_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨᓡ"))),
            bstack11111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᓢ"): env.get(bstack11111_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᓣ")),
            bstack11111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᓤ"): env.get(bstack11111_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᓥ"))
        }
    if env.get(bstack11111_opy_ (u"ࠤࡄ࡞࡚ࡘࡅࡠࡊࡗࡘࡕࡥࡕࡔࡇࡕࡣࡆࡍࡅࡏࡖࠥᓦ")) and env.get(bstack11111_opy_ (u"ࠥࡘࡋࡥࡂࡖࡋࡏࡈࠧᓧ")):
        return {
            bstack11111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᓨ"): bstack11111_opy_ (u"ࠧࡇࡺࡶࡴࡨࠤࡈࡏࠢᓩ"),
            bstack11111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᓪ"): bstack11111_opy_ (u"ࠢࡼࡿࡾࢁ࠴ࡥࡢࡶ࡫࡯ࡨ࠴ࡸࡥࡴࡷ࡯ࡸࡸࡅࡢࡶ࡫࡯ࡨࡎࡪ࠽ࡼࡿࠥᓫ").format(env.get(bstack11111_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡌࡏࡖࡐࡇࡅ࡙ࡏࡏࡏࡕࡈࡖ࡛ࡋࡒࡖࡔࡌࠫᓬ")), env.get(bstack11111_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡐࡓࡑࡍࡉࡈ࡚ࠧᓭ")), env.get(bstack11111_opy_ (u"ࠪࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠪᓮ"))),
            bstack11111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᓯ"): env.get(bstack11111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧᓰ")),
            bstack11111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᓱ"): env.get(bstack11111_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢᓲ"))
        }
    if any([env.get(bstack11111_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᓳ")), env.get(bstack11111_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡘࡅࡔࡑࡏ࡚ࡊࡊ࡟ࡔࡑࡘࡖࡈࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࠣᓴ")), env.get(bstack11111_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡓࡐࡗࡕࡇࡊࡥࡖࡆࡔࡖࡍࡔࡔࠢᓵ"))]):
        return {
            bstack11111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᓶ"): bstack11111_opy_ (u"ࠧࡇࡗࡔࠢࡆࡳࡩ࡫ࡂࡶ࡫࡯ࡨࠧᓷ"),
            bstack11111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᓸ"): env.get(bstack11111_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡔ࡚ࡈࡌࡊࡅࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᓹ")),
            bstack11111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᓺ"): env.get(bstack11111_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢᓻ")),
            bstack11111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᓼ"): env.get(bstack11111_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤᓽ"))
        }
    if env.get(bstack11111_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡒࡺࡳࡢࡦࡴࠥᓾ")):
        return {
            bstack11111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᓿ"): bstack11111_opy_ (u"ࠢࡃࡣࡰࡦࡴࡵࠢᔀ"),
            bstack11111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᔁ"): env.get(bstack11111_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡓࡧࡶࡹࡱࡺࡳࡖࡴ࡯ࠦᔂ")),
            bstack11111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᔃ"): env.get(bstack11111_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡸ࡮࡯ࡳࡶࡍࡳࡧࡔࡡ࡮ࡧࠥᔄ")),
            bstack11111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᔅ"): env.get(bstack11111_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡓࡻ࡭ࡣࡧࡵࠦᔆ"))
        }
    if env.get(bstack11111_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࠣᔇ")) or env.get(bstack11111_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥᔈ")):
        return {
            bstack11111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᔉ"): bstack11111_opy_ (u"࡛ࠥࡪࡸࡣ࡬ࡧࡵࠦᔊ"),
            bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᔋ"): env.get(bstack11111_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᔌ")),
            bstack11111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᔍ"): bstack11111_opy_ (u"ࠢࡎࡣ࡬ࡲࠥࡖࡩࡱࡧ࡯࡭ࡳ࡫ࠢᔎ") if env.get(bstack11111_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥᔏ")) else None,
            bstack11111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᔐ"): env.get(bstack11111_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡌࡏࡔࡠࡅࡒࡑࡒࡏࡔࠣᔑ"))
        }
    if any([env.get(bstack11111_opy_ (u"ࠦࡌࡉࡐࡠࡒࡕࡓࡏࡋࡃࡕࠤᔒ")), env.get(bstack11111_opy_ (u"ࠧࡍࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨᔓ")), env.get(bstack11111_opy_ (u"ࠨࡇࡐࡑࡊࡐࡊࡥࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨᔔ"))]):
        return {
            bstack11111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᔕ"): bstack11111_opy_ (u"ࠣࡉࡲࡳ࡬ࡲࡥࠡࡅ࡯ࡳࡺࡪࠢᔖ"),
            bstack11111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᔗ"): None,
            bstack11111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᔘ"): env.get(bstack11111_opy_ (u"ࠦࡕࡘࡏࡋࡇࡆࡘࡤࡏࡄࠣᔙ")),
            bstack11111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᔚ"): env.get(bstack11111_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣᔛ"))
        }
    if env.get(bstack11111_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࠥᔜ")):
        return {
            bstack11111_opy_ (u"ࠣࡰࡤࡱࡪࠨᔝ"): bstack11111_opy_ (u"ࠤࡖ࡬࡮ࡶࡰࡢࡤ࡯ࡩࠧᔞ"),
            bstack11111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᔟ"): env.get(bstack11111_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᔠ")),
            bstack11111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᔡ"): bstack11111_opy_ (u"ࠨࡊࡰࡤࠣࠧࢀࢃࠢᔢ").format(env.get(bstack11111_opy_ (u"ࠧࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡎࡔࡈ࡟ࡊࡆࠪᔣ"))) if env.get(bstack11111_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡏࡕࡂࡠࡋࡇࠦᔤ")) else None,
            bstack11111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᔥ"): env.get(bstack11111_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᔦ"))
        }
    if bstack1llll1lll1_opy_(env.get(bstack11111_opy_ (u"ࠦࡓࡋࡔࡍࡋࡉ࡝ࠧᔧ"))):
        return {
            bstack11111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᔨ"): bstack11111_opy_ (u"ࠨࡎࡦࡶ࡯࡭࡫ࡿࠢᔩ"),
            bstack11111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᔪ"): env.get(bstack11111_opy_ (u"ࠣࡆࡈࡔࡑࡕ࡙ࡠࡗࡕࡐࠧᔫ")),
            bstack11111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᔬ"): env.get(bstack11111_opy_ (u"ࠥࡗࡎ࡚ࡅࡠࡐࡄࡑࡊࠨᔭ")),
            bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᔮ"): env.get(bstack11111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢᔯ"))
        }
    if bstack1llll1lll1_opy_(env.get(bstack11111_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡁࡄࡖࡌࡓࡓ࡙ࠢᔰ"))):
        return {
            bstack11111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᔱ"): bstack11111_opy_ (u"ࠣࡉ࡬ࡸࡍࡻࡢࠡࡃࡦࡸ࡮ࡵ࡮ࡴࠤᔲ"),
            bstack11111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᔳ"): bstack11111_opy_ (u"ࠥࡿࢂ࠵ࡻࡾ࠱ࡤࡧࡹ࡯࡯࡯ࡵ࠲ࡶࡺࡴࡳ࠰ࡽࢀࠦᔴ").format(env.get(bstack11111_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡘࡋࡒࡗࡇࡕࡣ࡚ࡘࡌࠨᔵ")), env.get(bstack11111_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤࡘࡅࡑࡑࡖࡍ࡙ࡕࡒ࡚ࠩᔶ")), env.get(bstack11111_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡒࡖࡐࡢࡍࡉ࠭ᔷ"))),
            bstack11111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᔸ"): env.get(bstack11111_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠ࡙ࡒࡖࡐࡌࡌࡐ࡙ࠥᔹ")),
            bstack11111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᔺ"): env.get(bstack11111_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢࡖ࡚ࡔ࡟ࡊࡆࠥᔻ"))
        }
    if env.get(bstack11111_opy_ (u"ࠦࡈࡏࠢᔼ")) == bstack11111_opy_ (u"ࠧࡺࡲࡶࡧࠥᔽ") and env.get(bstack11111_opy_ (u"ࠨࡖࡆࡔࡆࡉࡑࠨᔾ")) == bstack11111_opy_ (u"ࠢ࠲ࠤᔿ"):
        return {
            bstack11111_opy_ (u"ࠣࡰࡤࡱࡪࠨᕀ"): bstack11111_opy_ (u"ࠤ࡙ࡩࡷࡩࡥ࡭ࠤᕁ"),
            bstack11111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᕂ"): bstack11111_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࢀࢃࠢᕃ").format(env.get(bstack11111_opy_ (u"ࠬ࡜ࡅࡓࡅࡈࡐࡤ࡛ࡒࡍࠩᕄ"))),
            bstack11111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᕅ"): None,
            bstack11111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᕆ"): None,
        }
    if env.get(bstack11111_opy_ (u"ࠣࡖࡈࡅࡒࡉࡉࡕ࡛ࡢ࡚ࡊࡘࡓࡊࡑࡑࠦᕇ")):
        return {
            bstack11111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᕈ"): bstack11111_opy_ (u"ࠥࡘࡪࡧ࡭ࡤ࡫ࡷࡽࠧᕉ"),
            bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᕊ"): None,
            bstack11111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᕋ"): env.get(bstack11111_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡒࡕࡓࡏࡋࡃࡕࡡࡑࡅࡒࡋࠢᕌ")),
            bstack11111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᕍ"): env.get(bstack11111_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᕎ"))
        }
    if any([env.get(bstack11111_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࠧᕏ")), env.get(bstack11111_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡕࡓࡎࠥᕐ")), env.get(bstack11111_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠤᕑ")), env.get(bstack11111_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡖࡈࡅࡒࠨᕒ"))]):
        return {
            bstack11111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᕓ"): bstack11111_opy_ (u"ࠢࡄࡱࡱࡧࡴࡻࡲࡴࡧࠥᕔ"),
            bstack11111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᕕ"): None,
            bstack11111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᕖ"): env.get(bstack11111_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᕗ")) or None,
            bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᕘ"): env.get(bstack11111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢᕙ"), 0)
        }
    if env.get(bstack11111_opy_ (u"ࠨࡇࡐࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᕚ")):
        return {
            bstack11111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᕛ"): bstack11111_opy_ (u"ࠣࡉࡲࡇࡉࠨᕜ"),
            bstack11111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᕝ"): None,
            bstack11111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᕞ"): env.get(bstack11111_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᕟ")),
            bstack11111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᕠ"): env.get(bstack11111_opy_ (u"ࠨࡇࡐࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡈࡕࡕࡏࡖࡈࡖࠧᕡ"))
        }
    if env.get(bstack11111_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᕢ")):
        return {
            bstack11111_opy_ (u"ࠣࡰࡤࡱࡪࠨᕣ"): bstack11111_opy_ (u"ࠤࡆࡳࡩ࡫ࡆࡳࡧࡶ࡬ࠧᕤ"),
            bstack11111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᕥ"): env.get(bstack11111_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᕦ")),
            bstack11111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᕧ"): env.get(bstack11111_opy_ (u"ࠨࡃࡇࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡓࡇࡍࡆࠤᕨ")),
            bstack11111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᕩ"): env.get(bstack11111_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᕪ"))
        }
    return {bstack11111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᕫ"): None}
def get_host_info():
    return {
        bstack11111_opy_ (u"ࠥ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠧᕬ"): platform.node(),
        bstack11111_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨᕭ"): platform.system(),
        bstack11111_opy_ (u"ࠧࡺࡹࡱࡧࠥᕮ"): platform.machine(),
        bstack11111_opy_ (u"ࠨࡶࡦࡴࡶ࡭ࡴࡴࠢᕯ"): platform.version(),
        bstack11111_opy_ (u"ࠢࡢࡴࡦ࡬ࠧᕰ"): platform.architecture()[0]
    }
def bstack11l11l111_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack1llll11l1l1_opy_():
    if bstack1llllll1l1_opy_.get_property(bstack11111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩᕱ")):
        return bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᕲ")
    return bstack11111_opy_ (u"ࠪࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠩᕳ")
def bstack1lll11llll1_opy_(driver):
    info = {
        bstack11111_opy_ (u"ࠫࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪᕴ"): driver.capabilities,
        bstack11111_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠩᕵ"): driver.session_id,
        bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧᕶ"): driver.capabilities.get(bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᕷ"), None),
        bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪᕸ"): driver.capabilities.get(bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᕹ"), None),
        bstack11111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࠬᕺ"): driver.capabilities.get(bstack11111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪᕻ"), None),
    }
    if bstack1llll11l1l1_opy_() == bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᕼ"):
        if bstack11l1ll11l_opy_():
            info[bstack11111_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧᕽ")] = bstack11111_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᕾ")
        elif driver.capabilities.get(bstack11111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᕿ"), {}).get(bstack11111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ᖀ"), False):
            info[bstack11111_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫᖁ")] = bstack11111_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨᖂ")
        else:
            info[bstack11111_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ᖃ")] = bstack11111_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨᖄ")
    return info
def bstack11l1ll11l_opy_():
    if bstack1llllll1l1_opy_.get_property(bstack11111_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᖅ")):
        return True
    if bstack1llll1lll1_opy_(os.environ.get(bstack11111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩᖆ"), None)):
        return True
    return False
def bstack11llll1l1l_opy_(bstack1lll1l11l1l_opy_, url, data, config):
    headers = config.get(bstack11111_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪᖇ"), None)
    proxies = bstack1llll1llll_opy_(config, url)
    auth = config.get(bstack11111_opy_ (u"ࠪࡥࡺࡺࡨࠨᖈ"), None)
    response = requests.request(
            bstack1lll1l11l1l_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack11l1l11l_opy_(bstack1ll1l1ll11_opy_, size):
    bstack11ll1ll1l1_opy_ = []
    while len(bstack1ll1l1ll11_opy_) > size:
        bstack111ll1ll1_opy_ = bstack1ll1l1ll11_opy_[:size]
        bstack11ll1ll1l1_opy_.append(bstack111ll1ll1_opy_)
        bstack1ll1l1ll11_opy_ = bstack1ll1l1ll11_opy_[size:]
    bstack11ll1ll1l1_opy_.append(bstack1ll1l1ll11_opy_)
    return bstack11ll1ll1l1_opy_
def bstack1llll11lll1_opy_(message, bstack1llll11l1ll_opy_=False):
    os.write(1, bytes(message, bstack11111_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᖉ")))
    os.write(1, bytes(bstack11111_opy_ (u"ࠬࡢ࡮ࠨᖊ"), bstack11111_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᖋ")))
    if bstack1llll11l1ll_opy_:
        with open(bstack11111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠭ࡰ࠳࠴ࡽ࠲࠭ᖌ") + os.environ[bstack11111_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧᖍ")] + bstack11111_opy_ (u"ࠩ࠱ࡰࡴ࡭ࠧᖎ"), bstack11111_opy_ (u"ࠪࡥࠬᖏ")) as f:
            f.write(message + bstack11111_opy_ (u"ࠫࡡࡴࠧᖐ"))
def bstack1llll1l1111_opy_():
    return os.environ[bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨᖑ")].lower() == bstack11111_opy_ (u"࠭ࡴࡳࡷࡨࠫᖒ")
def bstack1111l1lll_opy_(bstack111l111lll_opy_):
    return bstack11111_opy_ (u"ࠧࡼࡿ࠲ࡿࢂ࠭ᖓ").format(bstack1llll1ll1ll_opy_, bstack111l111lll_opy_)
def bstack1l1l11lll_opy_():
    return bstack11l11l1ll1_opy_().replace(tzinfo=None).isoformat() + bstack11111_opy_ (u"ࠨ࡜ࠪᖔ")
def bstack1lll1ll1lll_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11111_opy_ (u"ࠩ࡝ࠫᖕ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11111_opy_ (u"ࠪ࡞ࠬᖖ")))).total_seconds() * 1000
def bstack1lll1111lll_opy_(timestamp):
    return bstack1llll11llll_opy_(timestamp).isoformat() + bstack11111_opy_ (u"ࠫ࡟࠭ᖗ")
def bstack1lll1ll11ll_opy_(bstack1lll1111l11_opy_):
    date_format = bstack11111_opy_ (u"࡙ࠬࠫࠦ࡯ࠨࡨࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪ࠮ࠦࡨࠪᖘ")
    bstack1lll1llll11_opy_ = datetime.datetime.strptime(bstack1lll1111l11_opy_, date_format)
    return bstack1lll1llll11_opy_.isoformat() + bstack11111_opy_ (u"࡚࠭ࠨᖙ")
def bstack1lll11l11ll_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᖚ")
    else:
        return bstack11111_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᖛ")
def bstack1llll1lll1_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11111_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᖜ")
def bstack1lll1ll1l1l_opy_(val):
    return val.__str__().lower() == bstack11111_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩᖝ")
def bstack11l11ll11l_opy_(bstack1lll111llll_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack1lll111llll_opy_ as e:
                print(bstack11111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࢁࡽࠡ࠯ࡁࠤࢀࢃ࠺ࠡࡽࢀࠦᖞ").format(func.__name__, bstack1lll111llll_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1lll1llllll_opy_(bstack1lll1l11l11_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack1lll1l11l11_opy_(cls, *args, **kwargs)
            except bstack1lll111llll_opy_ as e:
                print(bstack11111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡻࡾࠢ࠰ࡂࠥࢁࡽ࠻ࠢࡾࢁࠧᖟ").format(bstack1lll1l11l11_opy_.__name__, bstack1lll111llll_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1lll1llllll_opy_
    else:
        return decorator
def bstack11l11l11l_opy_(bstack111ll1l111_opy_):
    if bstack11111_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᖠ") in bstack111ll1l111_opy_ and bstack1lll1ll1l1l_opy_(bstack111ll1l111_opy_[bstack11111_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᖡ")]):
        return False
    if bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᖢ") in bstack111ll1l111_opy_ and bstack1lll1ll1l1l_opy_(bstack111ll1l111_opy_[bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᖣ")]):
        return False
    return True
def bstack1ll1l1l1ll_opy_():
    try:
        from pytest_bdd import reporting
        bstack1lll1l1l1ll_opy_ = os.environ.get(bstack11111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡘࡗࡊࡘ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠥᖤ"), None)
        return bstack1lll1l1l1ll_opy_ is None or bstack1lll1l1l1ll_opy_ == bstack11111_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣᖥ")
    except Exception as e:
        return False
def bstack1llll1l11_opy_(hub_url, CONFIG):
    if bstack11ll1l1l1_opy_() <= version.parse(bstack11111_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬᖦ")):
        if hub_url != bstack11111_opy_ (u"࠭ࠧᖧ"):
            return bstack11111_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣᖨ") + hub_url + bstack11111_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧᖩ")
        return bstack1lll1lll1l_opy_
    if hub_url != bstack11111_opy_ (u"ࠩࠪᖪ"):
        return bstack11111_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧᖫ") + hub_url + bstack11111_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧᖬ")
    return bstack11l1ll111_opy_
def bstack1lll1l111l1_opy_():
    return isinstance(os.getenv(bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡒࡕࡈࡋࡑࠫᖭ")), str)
def bstack1ll1l1l1_opy_(url):
    return urlparse(url).hostname
def bstack1llll111_opy_(hostname):
    for bstack111ll1l1_opy_ in bstack11ll1l111_opy_:
        regex = re.compile(bstack111ll1l1_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack1lll1l11ll1_opy_(bstack1lll11lllll_opy_, file_name, logger):
    bstack11111l111_opy_ = os.path.join(os.path.expanduser(bstack11111_opy_ (u"࠭ࡾࠨᖮ")), bstack1lll11lllll_opy_)
    try:
        if not os.path.exists(bstack11111l111_opy_):
            os.makedirs(bstack11111l111_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11111_opy_ (u"ࠧࡿࠩᖯ")), bstack1lll11lllll_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11111_opy_ (u"ࠨࡹࠪᖰ")):
                pass
            with open(file_path, bstack11111_opy_ (u"ࠤࡺ࠯ࠧᖱ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1l11l1llll_opy_.format(str(e)))
def bstack1lll1l1llll_opy_(file_name, key, value, logger):
    file_path = bstack1lll1l11ll1_opy_(bstack11111_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᖲ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1l1lll111l_opy_ = json.load(open(file_path, bstack11111_opy_ (u"ࠫࡷࡨࠧᖳ")))
        else:
            bstack1l1lll111l_opy_ = {}
        bstack1l1lll111l_opy_[key] = value
        with open(file_path, bstack11111_opy_ (u"ࠧࡽࠫࠣᖴ")) as outfile:
            json.dump(bstack1l1lll111l_opy_, outfile)
def bstack1111111l_opy_(file_name, logger):
    file_path = bstack1lll1l11ll1_opy_(bstack11111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᖵ"), file_name, logger)
    bstack1l1lll111l_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11111_opy_ (u"ࠧࡳࠩᖶ")) as bstack1lllll1l1_opy_:
            bstack1l1lll111l_opy_ = json.load(bstack1lllll1l1_opy_)
    return bstack1l1lll111l_opy_
def bstack1l1l11lll1_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡨࡪࡲࡥࡵ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬᖷ") + file_path + bstack11111_opy_ (u"ࠩࠣࠫᖸ") + str(e))
def bstack11ll1l1l1_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11111_opy_ (u"ࠥࡀࡓࡕࡔࡔࡇࡗࡂࠧᖹ")
def bstack1lll11l1ll_opy_(config):
    if bstack11111_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᖺ") in config:
        del (config[bstack11111_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᖻ")])
        return False
    if bstack11ll1l1l1_opy_() < version.parse(bstack11111_opy_ (u"࠭࠳࠯࠶࠱࠴ࠬᖼ")):
        return False
    if bstack11ll1l1l1_opy_() >= version.parse(bstack11111_opy_ (u"ࠧ࠵࠰࠴࠲࠺࠭ᖽ")):
        return True
    if bstack11111_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨᖾ") in config and config[bstack11111_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩᖿ")] is False:
        return False
    else:
        return True
def bstack1l11ll1l_opy_(args_list, bstack1ll1lllll1l_opy_):
    index = -1
    for value in bstack1ll1lllll1l_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack11l1llll11_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack11l1llll11_opy_ = bstack11l1llll11_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack11111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᗀ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᗁ"), exception=exception)
    def bstack111l1ll1ll_opy_(self):
        if self.result != bstack11111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᗂ"):
            return None
        if isinstance(self.exception_type, str) and bstack11111_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤᗃ") in self.exception_type:
            return bstack11111_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣᗄ")
        return bstack11111_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤᗅ")
    def bstack1llll11ll1l_opy_(self):
        if self.result != bstack11111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᗆ"):
            return None
        if self.bstack11l1llll11_opy_:
            return self.bstack11l1llll11_opy_
        return bstack1llll111l1l_opy_(self.exception)
def bstack1llll111l1l_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack1llll111l11_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l11lll1ll_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1l111l1ll1_opy_(config, logger):
    try:
        import playwright
        bstack1lll11l1l1l_opy_ = playwright.__file__
        bstack1lll111l1l1_opy_ = os.path.split(bstack1lll11l1l1l_opy_)
        bstack1lll11111ll_opy_ = bstack1lll111l1l1_opy_[0] + bstack11111_opy_ (u"ࠪ࠳ࡩࡸࡩࡷࡧࡵ࠳ࡵࡧࡣ࡬ࡣࡪࡩ࠴ࡲࡩࡣ࠱ࡦࡰ࡮࠵ࡣ࡭࡫࠱࡮ࡸ࠭ᗇ")
        os.environ[bstack11111_opy_ (u"ࠫࡌࡒࡏࡃࡃࡏࡣࡆࡍࡅࡏࡖࡢࡌ࡙࡚ࡐࡠࡒࡕࡓ࡝࡟ࠧᗈ")] = bstack1llll111ll_opy_(config)
        with open(bstack1lll11111ll_opy_, bstack11111_opy_ (u"ࠬࡸࠧᗉ")) as f:
            bstack1ll1ll1l11_opy_ = f.read()
            bstack1lll11111l1_opy_ = bstack11111_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠬᗊ")
            bstack1lll11l111l_opy_ = bstack1ll1ll1l11_opy_.find(bstack1lll11111l1_opy_)
            if bstack1lll11l111l_opy_ == -1:
              process = subprocess.Popen(bstack11111_opy_ (u"ࠢ࡯ࡲࡰࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠦᗋ"), shell=True, cwd=bstack1lll111l1l1_opy_[0])
              process.wait()
              bstack1lll1ll1111_opy_ = bstack11111_opy_ (u"ࠨࠤࡸࡷࡪࠦࡳࡵࡴ࡬ࡧࡹࠨ࠻ࠨᗌ")
              bstack1lll1l1l111_opy_ = bstack11111_opy_ (u"ࠤࠥࠦࠥࡢࠢࡶࡵࡨࠤࡸࡺࡲࡪࡥࡷࡠࠧࡁࠠࡤࡱࡱࡷࡹࠦࡻࠡࡤࡲࡳࡹࡹࡴࡳࡣࡳࠤࢂࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪࠪ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠩࠬ࠿ࠥ࡯ࡦࠡࠪࡳࡶࡴࡩࡥࡴࡵ࠱ࡩࡳࡼ࠮ࡈࡎࡒࡆࡆࡒ࡟ࡂࡉࡈࡒ࡙ࡥࡈࡕࡖࡓࡣࡕࡘࡏ࡙࡛ࠬࠤࡧࡵ࡯ࡵࡵࡷࡶࡦࡶࠨࠪ࠽ࠣࠦࠧࠨᗍ")
              bstack1lll1l1ll1l_opy_ = bstack1ll1ll1l11_opy_.replace(bstack1lll1ll1111_opy_, bstack1lll1l1l111_opy_)
              with open(bstack1lll11111ll_opy_, bstack11111_opy_ (u"ࠪࡻࠬᗎ")) as f:
                f.write(bstack1lll1l1ll1l_opy_)
    except Exception as e:
        logger.error(bstack1l1111l1ll_opy_.format(str(e)))
def bstack1lll11lll1_opy_():
  try:
    bstack1llll1111l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠴ࡪࡴࡱࡱࠫᗏ"))
    bstack1llll11l11l_opy_ = []
    if os.path.exists(bstack1llll1111l1_opy_):
      with open(bstack1llll1111l1_opy_) as f:
        bstack1llll11l11l_opy_ = json.load(f)
      os.remove(bstack1llll1111l1_opy_)
    return bstack1llll11l11l_opy_
  except:
    pass
  return []
def bstack1ll11lll1l_opy_(bstack1l1l11ll1_opy_):
  try:
    bstack1llll11l11l_opy_ = []
    bstack1llll1111l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠬࡵࡰࡵ࡫ࡰࡥࡱࡥࡨࡶࡤࡢࡹࡷࡲ࠮࡫ࡵࡲࡲࠬᗐ"))
    if os.path.exists(bstack1llll1111l1_opy_):
      with open(bstack1llll1111l1_opy_) as f:
        bstack1llll11l11l_opy_ = json.load(f)
    bstack1llll11l11l_opy_.append(bstack1l1l11ll1_opy_)
    with open(bstack1llll1111l1_opy_, bstack11111_opy_ (u"࠭ࡷࠨᗑ")) as f:
        json.dump(bstack1llll11l11l_opy_, f)
  except:
    pass
def bstack1l1l1111l_opy_(logger, bstack1lll1l1lll1_opy_ = False):
  try:
    test_name = os.environ.get(bstack11111_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪᗒ"), bstack11111_opy_ (u"ࠨࠩᗓ"))
    if test_name == bstack11111_opy_ (u"ࠩࠪᗔ"):
        test_name = threading.current_thread().__dict__.get(bstack11111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡅࡨࡩࡥࡴࡦࡵࡷࡣࡳࡧ࡭ࡦࠩᗕ"), bstack11111_opy_ (u"ࠫࠬᗖ"))
    bstack1lll1lll111_opy_ = bstack11111_opy_ (u"ࠬ࠲ࠠࠨᗗ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack1lll1l1lll1_opy_:
        bstack111l11111_opy_ = os.environ.get(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᗘ"), bstack11111_opy_ (u"ࠧ࠱ࠩᗙ"))
        bstack11111l11_opy_ = {bstack11111_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᗚ"): test_name, bstack11111_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᗛ"): bstack1lll1lll111_opy_, bstack11111_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᗜ"): bstack111l11111_opy_}
        bstack1lll11ll1l1_opy_ = []
        bstack1lll1111l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡵࡶࡰࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪᗝ"))
        if os.path.exists(bstack1lll1111l1l_opy_):
            with open(bstack1lll1111l1l_opy_) as f:
                bstack1lll11ll1l1_opy_ = json.load(f)
        bstack1lll11ll1l1_opy_.append(bstack11111l11_opy_)
        with open(bstack1lll1111l1l_opy_, bstack11111_opy_ (u"ࠬࡽࠧᗞ")) as f:
            json.dump(bstack1lll11ll1l1_opy_, f)
    else:
        bstack11111l11_opy_ = {bstack11111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᗟ"): test_name, bstack11111_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᗠ"): bstack1lll1lll111_opy_, bstack11111_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᗡ"): str(multiprocessing.current_process().name)}
        if bstack11111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭ᗢ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack11111l11_opy_)
  except Exception as e:
      logger.warn(bstack11111_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡶࡹࡵࡧࡶࡸࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃࠢᗣ").format(e))
def bstack1111lll1_opy_(error_message, test_name, index, logger):
  try:
    bstack1lll1lll1l1_opy_ = []
    bstack11111l11_opy_ = {bstack11111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᗤ"): test_name, bstack11111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᗥ"): error_message, bstack11111_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᗦ"): index}
    bstack1lll11l11l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠧࡳࡱࡥࡳࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨᗧ"))
    if os.path.exists(bstack1lll11l11l1_opy_):
        with open(bstack1lll11l11l1_opy_) as f:
            bstack1lll1lll1l1_opy_ = json.load(f)
    bstack1lll1lll1l1_opy_.append(bstack11111l11_opy_)
    with open(bstack1lll11l11l1_opy_, bstack11111_opy_ (u"ࠨࡹࠪᗨ")) as f:
        json.dump(bstack1lll1lll1l1_opy_, f)
  except Exception as e:
    logger.warn(bstack11111_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡷࡵࡢࡰࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧᗩ").format(e))
def bstack11llll1l1_opy_(bstack1l1l1ll1_opy_, name, logger):
  try:
    bstack11111l11_opy_ = {bstack11111_opy_ (u"ࠪࡲࡦࡳࡥࠨᗪ"): name, bstack11111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᗫ"): bstack1l1l1ll1_opy_, bstack11111_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᗬ"): str(threading.current_thread()._name)}
    return bstack11111l11_opy_
  except Exception as e:
    logger.warn(bstack11111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡤࡨ࡬ࡦࡼࡥࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥᗭ").format(e))
  return
def bstack1lll111lll1_opy_():
    return platform.system() == bstack11111_opy_ (u"ࠧࡘ࡫ࡱࡨࡴࡽࡳࠨᗮ")
def bstack1lllll1111_opy_(bstack1lll1lll11l_opy_, config, logger):
    bstack1lll111ll11_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack1lll1lll11l_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡬ࡵࡧࡵࠤࡨࡵ࡮ࡧ࡫ࡪࠤࡰ࡫ࡹࡴࠢࡥࡽࠥࡸࡥࡨࡧࡻࠤࡲࡧࡴࡤࡪ࠽ࠤࢀࢃࠢᗯ").format(e))
    return bstack1lll111ll11_opy_
def bstack1llll111ll1_opy_(bstack1lll1ll1ll1_opy_, bstack1llll11l111_opy_):
    bstack1lll111l1ll_opy_ = version.parse(bstack1lll1ll1ll1_opy_)
    bstack1lll1ll11l1_opy_ = version.parse(bstack1llll11l111_opy_)
    if bstack1lll111l1ll_opy_ > bstack1lll1ll11l1_opy_:
        return 1
    elif bstack1lll111l1ll_opy_ < bstack1lll1ll11l1_opy_:
        return -1
    else:
        return 0
def bstack11l11l1ll1_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack1llll11llll_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack1llll111111_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack111ll11l_opy_(options, framework, bstack111l1ll1l_opy_={}):
    if options is None:
        return
    if getattr(options, bstack11111_opy_ (u"ࠩࡪࡩࡹ࠭ᗰ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1llll1111l_opy_ = caps.get(bstack11111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᗱ"))
    bstack1llll111lll_opy_ = True
    bstack11ll1111l1_opy_ = os.environ[bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᗲ")]
    if bstack1lll1ll1l1l_opy_(caps.get(bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡘ࠵ࡆࠫᗳ"))) or bstack1lll1ll1l1l_opy_(caps.get(bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦࡡࡺ࠷ࡨ࠭ᗴ"))):
        bstack1llll111lll_opy_ = False
    if bstack1lll11l1ll_opy_({bstack11111_opy_ (u"ࠢࡶࡵࡨ࡛࠸ࡉࠢᗵ"): bstack1llll111lll_opy_}):
        bstack1llll1111l_opy_ = bstack1llll1111l_opy_ or {}
        bstack1llll1111l_opy_[bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᗶ")] = bstack1llll111111_opy_(framework)
        bstack1llll1111l_opy_[bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᗷ")] = bstack1llll1l1111_opy_()
        bstack1llll1111l_opy_[bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᗸ")] = bstack11ll1111l1_opy_
        bstack1llll1111l_opy_[bstack11111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᗹ")] = bstack111l1ll1l_opy_
        if getattr(options, bstack11111_opy_ (u"ࠬࡹࡥࡵࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸࡾ࠭ᗺ"), None):
            options.set_capability(bstack11111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᗻ"), bstack1llll1111l_opy_)
        else:
            options[bstack11111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᗼ")] = bstack1llll1111l_opy_
    else:
        if getattr(options, bstack11111_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩᗽ"), None):
            options.set_capability(bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᗾ"), bstack1llll111111_opy_(framework))
            options.set_capability(bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᗿ"), bstack1llll1l1111_opy_())
            options.set_capability(bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᘀ"), bstack11ll1111l1_opy_)
            options.set_capability(bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᘁ"), bstack111l1ll1l_opy_)
        else:
            options[bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧᘂ")] = bstack1llll111111_opy_(framework)
            options[bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᘃ")] = bstack1llll1l1111_opy_()
            options[bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪᘄ")] = bstack11ll1111l1_opy_
            options[bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪᘅ")] = bstack111l1ll1l_opy_
    return options
def bstack1lll11l1lll_opy_(bstack1lll1l1l11l_opy_, framework):
    bstack111l1ll1l_opy_ = bstack1llllll1l1_opy_.get_property(bstack11111_opy_ (u"ࠥࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡑࡔࡒࡈ࡚ࡉࡔࡠࡏࡄࡔࠧᘆ"))
    if bstack1lll1l1l11l_opy_ and len(bstack1lll1l1l11l_opy_.split(bstack11111_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪᘇ"))) > 1:
        ws_url = bstack1lll1l1l11l_opy_.split(bstack11111_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫᘈ"))[0]
        if bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩᘉ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack1ll1lllllll_opy_ = json.loads(urllib.parse.unquote(bstack1lll1l1l11l_opy_.split(bstack11111_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ᘊ"))[1]))
            bstack1ll1lllllll_opy_ = bstack1ll1lllllll_opy_ or {}
            bstack11ll1111l1_opy_ = os.environ[bstack11111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᘋ")]
            bstack1ll1lllllll_opy_[bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᘌ")] = str(framework) + str(__version__)
            bstack1ll1lllllll_opy_[bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᘍ")] = bstack1llll1l1111_opy_()
            bstack1ll1lllllll_opy_[bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᘎ")] = bstack11ll1111l1_opy_
            bstack1ll1lllllll_opy_[bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᘏ")] = bstack111l1ll1l_opy_
            bstack1lll1l1l11l_opy_ = bstack1lll1l1l11l_opy_.split(bstack11111_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬᘐ"))[0] + bstack11111_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ᘑ") + urllib.parse.quote(json.dumps(bstack1ll1lllllll_opy_))
    return bstack1lll1l1l11l_opy_
def bstack11ll1lllll_opy_():
    global bstack11l111l1l_opy_
    from playwright._impl._browser_type import BrowserType
    bstack11l111l1l_opy_ = BrowserType.connect
    return bstack11l111l1l_opy_
def bstack11111ll1l_opy_(framework_name):
    global bstack1ll111l1l1_opy_
    bstack1ll111l1l1_opy_ = framework_name
    return framework_name
def bstack1l11lll111_opy_(self, *args, **kwargs):
    global bstack11l111l1l_opy_
    try:
        global bstack1ll111l1l1_opy_
        if bstack11111_opy_ (u"ࠨࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸࠬᘒ") in kwargs:
            kwargs[bstack11111_opy_ (u"ࠩࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹ࠭ᘓ")] = bstack1lll11l1lll_opy_(
                kwargs.get(bstack11111_opy_ (u"ࠪࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺࠧᘔ"), None),
                bstack1ll111l1l1_opy_
            )
    except Exception as e:
        logger.error(bstack11111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡦࡥࡵࡹ࠺ࠡࡽࢀࠦᘕ").format(str(e)))
    return bstack11l111l1l_opy_(self, *args, **kwargs)
def bstack1lll11l1l11_opy_(bstack1lll11l1111_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1llll1llll_opy_(bstack1lll11l1111_opy_, bstack11111_opy_ (u"ࠧࠨᘖ"))
        if proxies and proxies.get(bstack11111_opy_ (u"ࠨࡨࡵࡶࡳࡷࠧᘗ")):
            parsed_url = urlparse(proxies.get(bstack11111_opy_ (u"ࠢࡩࡶࡷࡴࡸࠨᘘ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack11111_opy_ (u"ࠨࡲࡵࡳࡽࡿࡈࡰࡵࡷࠫᘙ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack11111_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡱࡵࡸࠬᘚ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack11111_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭ᘛ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack11111_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧᘜ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1l1l1lll1_opy_(bstack1lll11l1111_opy_):
    bstack1lll1ll1l11_opy_ = {
        bstack1llll1l1ll1_opy_[bstack1lll1llll1l_opy_]: bstack1lll11l1111_opy_[bstack1lll1llll1l_opy_]
        for bstack1lll1llll1l_opy_ in bstack1lll11l1111_opy_
        if bstack1lll1llll1l_opy_ in bstack1llll1l1ll1_opy_
    }
    bstack1lll1ll1l11_opy_[bstack11111_opy_ (u"ࠧࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠧᘝ")] = bstack1lll11l1l11_opy_(bstack1lll11l1111_opy_, bstack1llllll1l1_opy_.get_property(bstack11111_opy_ (u"ࠨࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸࠨᘞ")))
    bstack1llll1l111l_opy_ = [element.lower() for element in bstack1llll1lll11_opy_]
    bstack1lll111l11l_opy_(bstack1lll1ll1l11_opy_, bstack1llll1l111l_opy_)
    return bstack1lll1ll1l11_opy_
def bstack1lll111l11l_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack11111_opy_ (u"ࠢࠫࠬ࠭࠮ࠧᘟ")
    for value in d.values():
        if isinstance(value, dict):
            bstack1lll111l11l_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack1lll111l11l_opy_(item, keys)