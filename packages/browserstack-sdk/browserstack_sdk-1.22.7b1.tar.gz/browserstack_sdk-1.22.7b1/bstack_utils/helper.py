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
import copy
import zipfile
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import (bstack1l1l1l1ll11_opy_, bstack111ll1ll1_opy_, bstack11l1111l1l_opy_, bstack11l11l1ll1_opy_,
                                    bstack1l1l1l1ll1l_opy_, bstack1l1l1l11l1l_opy_, bstack1l1l1ll1111_opy_, bstack1l1l1l1lll1_opy_)
from bstack_utils.messages import bstack1lll11l1ll_opy_, bstack11111lll1_opy_
from bstack_utils.proxy import bstack1lll1l1lll_opy_, bstack1l1ll11lll_opy_
from bstack_utils.constants import *
from bstack_utils import bstack11ll11llll_opy_
from browserstack_sdk._version import __version__
bstack111l11ll_opy_ = Config.bstack11l111ll_opy_()
logger = bstack11ll11llll_opy_.get_logger(__name__, bstack11ll11llll_opy_.bstack1lll111ll1l_opy_())
def bstack1l1111ll111_opy_(config):
    return config[bstack1l1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᝈ")]
def bstack1l111lll1l1_opy_(config):
    return config[bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᝉ")]
def bstack1ll11llll1_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack1l111ll1l1l_opy_(obj):
    values = []
    bstack1l111l1l11l_opy_ = re.compile(bstack1l1_opy_ (u"ࡷࠨ࡞ࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣࡡࡪࠫࠥࠤᝊ"), re.I)
    for key in obj.keys():
        if bstack1l111l1l11l_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1l11ll1l11l_opy_(config):
    tags = []
    tags.extend(bstack1l111ll1l1l_opy_(os.environ))
    tags.extend(bstack1l111ll1l1l_opy_(config))
    return tags
def bstack1l1111l1111_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack1l11l1lll1l_opy_(bstack1l11l1l11ll_opy_):
    if not bstack1l11l1l11ll_opy_:
        return bstack1l1_opy_ (u"࠭ࠧᝋ")
    return bstack1l1_opy_ (u"ࠢࡼࡿࠣࠬࢀࢃࠩࠣᝌ").format(bstack1l11l1l11ll_opy_.name, bstack1l11l1l11ll_opy_.email)
def bstack1l1111l1l11_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack1l11ll1l1l1_opy_ = repo.common_dir
        info = {
            bstack1l1_opy_ (u"ࠣࡵ࡫ࡥࠧᝍ"): repo.head.commit.hexsha,
            bstack1l1_opy_ (u"ࠤࡶ࡬ࡴࡸࡴࡠࡵ࡫ࡥࠧᝎ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack1l1_opy_ (u"ࠥࡦࡷࡧ࡮ࡤࡪࠥᝏ"): repo.active_branch.name,
            bstack1l1_opy_ (u"ࠦࡹࡧࡧࠣᝐ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack1l1_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡹ࡫ࡲࠣᝑ"): bstack1l11l1lll1l_opy_(repo.head.commit.committer),
            bstack1l1_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡺࡥࡳࡡࡧࡥࡹ࡫ࠢᝒ"): repo.head.commit.committed_datetime.isoformat(),
            bstack1l1_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࠢᝓ"): bstack1l11l1lll1l_opy_(repo.head.commit.author),
            bstack1l1_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࡠࡦࡤࡸࡪࠨ᝔"): repo.head.commit.authored_datetime.isoformat(),
            bstack1l1_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡡࡰࡩࡸࡹࡡࡨࡧࠥ᝕"): repo.head.commit.message,
            bstack1l1_opy_ (u"ࠥࡶࡴࡵࡴࠣ᝖"): repo.git.rev_parse(bstack1l1_opy_ (u"ࠦ࠲࠳ࡳࡩࡱࡺ࠱ࡹࡵࡰ࡭ࡧࡹࡩࡱࠨ᝗")),
            bstack1l1_opy_ (u"ࠧࡩ࡯࡮࡯ࡲࡲࡤ࡭ࡩࡵࡡࡧ࡭ࡷࠨ᝘"): bstack1l11ll1l1l1_opy_,
            bstack1l1_opy_ (u"ࠨࡷࡰࡴ࡮ࡸࡷ࡫ࡥࡠࡩ࡬ࡸࡤࡪࡩࡳࠤ᝙"): subprocess.check_output([bstack1l1_opy_ (u"ࠢࡨ࡫ࡷࠦ᝚"), bstack1l1_opy_ (u"ࠣࡴࡨࡺ࠲ࡶࡡࡳࡵࡨࠦ᝛"), bstack1l1_opy_ (u"ࠤ࠰࠱࡬࡯ࡴ࠮ࡥࡲࡱࡲࡵ࡮࠮ࡦ࡬ࡶࠧ᝜")]).strip().decode(
                bstack1l1_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩ᝝")),
            bstack1l1_opy_ (u"ࠦࡱࡧࡳࡵࡡࡷࡥ࡬ࠨ᝞"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack1l1_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡸࡥࡳࡪࡰࡦࡩࡤࡲࡡࡴࡶࡢࡸࡦ࡭ࠢ᝟"): repo.git.rev_list(
                bstack1l1_opy_ (u"ࠨࡻࡾ࠰࠱ࡿࢂࠨᝠ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1l11l1ll1ll_opy_ = []
        for remote in remotes:
            bstack1l11ll11111_opy_ = {
                bstack1l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᝡ"): remote.name,
                bstack1l1_opy_ (u"ࠣࡷࡵࡰࠧᝢ"): remote.url,
            }
            bstack1l11l1ll1ll_opy_.append(bstack1l11ll11111_opy_)
        bstack1l11l11l1ll_opy_ = {
            bstack1l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᝣ"): bstack1l1_opy_ (u"ࠥ࡫࡮ࡺࠢᝤ"),
            **info,
            bstack1l1_opy_ (u"ࠦࡷ࡫࡭ࡰࡶࡨࡷࠧᝥ"): bstack1l11l1ll1ll_opy_
        }
        bstack1l11l11l1ll_opy_ = bstack1l11l11ll1l_opy_(bstack1l11l11l1ll_opy_)
        return bstack1l11l11l1ll_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack1l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡵࡰࡶ࡮ࡤࡸ࡮ࡴࡧࠡࡉ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣᝦ").format(err))
        return {}
def bstack1l11l11ll1l_opy_(bstack1l11l11l1ll_opy_):
    bstack1l11l1lll11_opy_ = bstack1l111l11l1l_opy_(bstack1l11l11l1ll_opy_)
    if bstack1l11l1lll11_opy_ and bstack1l11l1lll11_opy_ > bstack1l1l1l1ll1l_opy_:
        bstack1l11l1ll1l1_opy_ = bstack1l11l1lll11_opy_ - bstack1l1l1l1ll1l_opy_
        bstack1l11l1l11l1_opy_ = bstack1l111l11l11_opy_(bstack1l11l11l1ll_opy_[bstack1l1_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠢᝧ")], bstack1l11l1ll1l1_opy_)
        bstack1l11l11l1ll_opy_[bstack1l1_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠣᝨ")] = bstack1l11l1l11l1_opy_
        logger.info(bstack1l1_opy_ (u"ࠣࡖ࡫ࡩࠥࡩ࡯࡮࡯࡬ࡸࠥ࡮ࡡࡴࠢࡥࡩࡪࡴࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦ࠱ࠤࡘ࡯ࡺࡦࠢࡲࡪࠥࡩ࡯࡮࡯࡬ࡸࠥࡧࡦࡵࡧࡵࠤࡹࡸࡵ࡯ࡥࡤࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤࢀࢃࠠࡌࡄࠥᝩ")
                    .format(bstack1l111l11l1l_opy_(bstack1l11l11l1ll_opy_) / 1024))
    return bstack1l11l11l1ll_opy_
def bstack1l111l11l1l_opy_(json_data):
    try:
        if json_data:
            bstack1l111ll1ll1_opy_ = json.dumps(json_data)
            bstack1l11l1lllll_opy_ = sys.getsizeof(bstack1l111ll1ll1_opy_)
            return bstack1l11l1lllll_opy_
    except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠤࡖࡳࡲ࡫ࡴࡩ࡫ࡱ࡫ࠥࡽࡥ࡯ࡶࠣࡻࡷࡵ࡮ࡨࠢࡺ࡬࡮ࡲࡥࠡࡥࡤࡰࡨࡻ࡬ࡢࡶ࡬ࡲ࡬ࠦࡳࡪࡼࡨࠤࡴ࡬ࠠࡋࡕࡒࡒࠥࡵࡢ࡫ࡧࡦࡸ࠿ࠦࡻࡾࠤᝪ").format(e))
    return -1
def bstack1l111l11l11_opy_(field, bstack1l111lll111_opy_):
    try:
        bstack1l11l111l11_opy_ = len(bytes(bstack1l1l1l11l1l_opy_, bstack1l1_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᝫ")))
        bstack1l111ll11l1_opy_ = bytes(field, bstack1l1_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᝬ"))
        bstack1l11l11lll1_opy_ = len(bstack1l111ll11l1_opy_)
        bstack1l11111l1l1_opy_ = ceil(bstack1l11l11lll1_opy_ - bstack1l111lll111_opy_ - bstack1l11l111l11_opy_)
        if bstack1l11111l1l1_opy_ > 0:
            bstack1l11111llll_opy_ = bstack1l111ll11l1_opy_[:bstack1l11111l1l1_opy_].decode(bstack1l1_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫ᝭"), errors=bstack1l1_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪ࠭ᝮ")) + bstack1l1l1l11l1l_opy_
            return bstack1l11111llll_opy_
    except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡺࡲࡶࡰࡦࡥࡹ࡯࡮ࡨࠢࡩ࡭ࡪࡲࡤ࠭ࠢࡱࡳࡹ࡮ࡩ࡯ࡩࠣࡻࡦࡹࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦࠣ࡬ࡪࡸࡥ࠻ࠢࡾࢁࠧᝯ").format(e))
    return field
def bstack111l1l1l1_opy_():
    env = os.environ
    if (bstack1l1_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡘࡖࡑࠨᝰ") in env and len(env[bstack1l1_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢ࡙ࡗࡒࠢ᝱")]) > 0) or (
            bstack1l1_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣࡍࡕࡍࡆࠤᝲ") in env and len(env[bstack1l1_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤࡎࡏࡎࡇࠥᝳ")]) > 0):
        return {
            bstack1l1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᝴"): bstack1l1_opy_ (u"ࠨࡊࡦࡰ࡮࡭ࡳࡹࠢ᝵"),
            bstack1l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᝶"): env.get(bstack1l1_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦ᝷")),
            bstack1l1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᝸"): env.get(bstack1l1_opy_ (u"ࠥࡎࡔࡈ࡟ࡏࡃࡐࡉࠧ᝹")),
            bstack1l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᝺"): env.get(bstack1l1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦ᝻"))
        }
    if env.get(bstack1l1_opy_ (u"ࠨࡃࡊࠤ᝼")) == bstack1l1_opy_ (u"ࠢࡵࡴࡸࡩࠧ᝽") and bstack1ll11l11l_opy_(env.get(bstack1l1_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡄࡋࠥ᝾"))):
        return {
            bstack1l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᝿"): bstack1l1_opy_ (u"ࠥࡇ࡮ࡸࡣ࡭ࡧࡆࡍࠧក"),
            bstack1l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢខ"): env.get(bstack1l1_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣគ")),
            bstack1l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣឃ"): env.get(bstack1l1_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡋࡑࡅࠦង")),
            bstack1l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢច"): env.get(bstack1l1_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࠧឆ"))
        }
    if env.get(bstack1l1_opy_ (u"ࠥࡇࡎࠨជ")) == bstack1l1_opy_ (u"ࠦࡹࡸࡵࡦࠤឈ") and bstack1ll11l11l_opy_(env.get(bstack1l1_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࠧញ"))):
        return {
            bstack1l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦដ"): bstack1l1_opy_ (u"ࠢࡕࡴࡤࡺ࡮ࡹࠠࡄࡋࠥឋ"),
            bstack1l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦឌ"): env.get(bstack1l1_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡅ࡙ࡎࡒࡄࡠ࡙ࡈࡆࡤ࡛ࡒࡍࠤឍ")),
            bstack1l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧណ"): env.get(bstack1l1_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨត")),
            bstack1l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦថ"): env.get(bstack1l1_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧទ"))
        }
    if env.get(bstack1l1_opy_ (u"ࠢࡄࡋࠥធ")) == bstack1l1_opy_ (u"ࠣࡶࡵࡹࡪࠨន") and env.get(bstack1l1_opy_ (u"ࠤࡆࡍࡤࡔࡁࡎࡇࠥប")) == bstack1l1_opy_ (u"ࠥࡧࡴࡪࡥࡴࡪ࡬ࡴࠧផ"):
        return {
            bstack1l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤព"): bstack1l1_opy_ (u"ࠧࡉ࡯ࡥࡧࡶ࡬࡮ࡶࠢភ"),
            bstack1l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤម"): None,
            bstack1l1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤយ"): None,
            bstack1l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢរ"): None
        }
    if env.get(bstack1l1_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡒࡂࡐࡆࡌࠧល")) and env.get(bstack1l1_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨវ")):
        return {
            bstack1l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤឝ"): bstack1l1_opy_ (u"ࠧࡈࡩࡵࡤࡸࡧࡰ࡫ࡴࠣឞ"),
            bstack1l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤស"): env.get(bstack1l1_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡋࡎ࡚࡟ࡉࡖࡗࡔࡤࡕࡒࡊࡉࡌࡒࠧហ")),
            bstack1l1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥឡ"): None,
            bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣអ"): env.get(bstack1l1_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧឣ"))
        }
    if env.get(bstack1l1_opy_ (u"ࠦࡈࡏࠢឤ")) == bstack1l1_opy_ (u"ࠧࡺࡲࡶࡧࠥឥ") and bstack1ll11l11l_opy_(env.get(bstack1l1_opy_ (u"ࠨࡄࡓࡑࡑࡉࠧឦ"))):
        return {
            bstack1l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧឧ"): bstack1l1_opy_ (u"ࠣࡆࡵࡳࡳ࡫ࠢឨ"),
            bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧឩ"): env.get(bstack1l1_opy_ (u"ࠥࡈࡗࡕࡎࡆࡡࡅ࡙ࡎࡒࡄࡠࡎࡌࡒࡐࠨឪ")),
            bstack1l1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨឫ"): None,
            bstack1l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦឬ"): env.get(bstack1l1_opy_ (u"ࠨࡄࡓࡑࡑࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦឭ"))
        }
    if env.get(bstack1l1_opy_ (u"ࠢࡄࡋࠥឮ")) == bstack1l1_opy_ (u"ࠣࡶࡵࡹࡪࠨឯ") and bstack1ll11l11l_opy_(env.get(bstack1l1_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࠧឰ"))):
        return {
            bstack1l1_opy_ (u"ࠥࡲࡦࡳࡥࠣឱ"): bstack1l1_opy_ (u"ࠦࡘ࡫࡭ࡢࡲ࡫ࡳࡷ࡫ࠢឲ"),
            bstack1l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣឳ"): env.get(bstack1l1_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡒࡖࡌࡇࡎࡊ࡜ࡄࡘࡎࡕࡎࡠࡗࡕࡐࠧ឴")),
            bstack1l1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ឵"): env.get(bstack1l1_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨា")),
            bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣិ"): env.get(bstack1l1_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡊࡐࡄࡢࡍࡉࠨី"))
        }
    if env.get(bstack1l1_opy_ (u"ࠦࡈࡏࠢឹ")) == bstack1l1_opy_ (u"ࠧࡺࡲࡶࡧࠥឺ") and bstack1ll11l11l_opy_(env.get(bstack1l1_opy_ (u"ࠨࡇࡊࡖࡏࡅࡇࡥࡃࡊࠤុ"))):
        return {
            bstack1l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧូ"): bstack1l1_opy_ (u"ࠣࡉ࡬ࡸࡑࡧࡢࠣួ"),
            bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧើ"): env.get(bstack1l1_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢ࡙ࡗࡒࠢឿ")),
            bstack1l1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨៀ"): env.get(bstack1l1_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥេ")),
            bstack1l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧែ"): env.get(bstack1l1_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡊࡆࠥៃ"))
        }
    if env.get(bstack1l1_opy_ (u"ࠣࡅࡌࠦោ")) == bstack1l1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢៅ") and bstack1ll11l11l_opy_(env.get(bstack1l1_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࠨំ"))):
        return {
            bstack1l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤះ"): bstack1l1_opy_ (u"ࠧࡈࡵࡪ࡮ࡧ࡯࡮ࡺࡥࠣៈ"),
            bstack1l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ៉"): env.get(bstack1l1_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨ៊")),
            bstack1l1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ់"): env.get(bstack1l1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡒࡁࡃࡇࡏࠦ៌")) or env.get(bstack1l1_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡐࡄࡑࡊࠨ៍")),
            bstack1l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ៎"): env.get(bstack1l1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢ៏"))
        }
    if bstack1ll11l11l_opy_(env.get(bstack1l1_opy_ (u"ࠨࡔࡇࡡࡅ࡙ࡎࡒࡄࠣ័"))):
        return {
            bstack1l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ៑"): bstack1l1_opy_ (u"ࠣࡘ࡬ࡷࡺࡧ࡬ࠡࡕࡷࡹࡩ࡯࡯ࠡࡖࡨࡥࡲࠦࡓࡦࡴࡹ࡭ࡨ࡫ࡳ្ࠣ"),
            bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ៓"): bstack1l1_opy_ (u"ࠥࡿࢂࢁࡽࠣ។").format(env.get(bstack1l1_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡈࡒ࡙ࡓࡊࡁࡕࡋࡒࡒࡘࡋࡒࡗࡇࡕ࡙ࡗࡏࠧ៕")), env.get(bstack1l1_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡓࡖࡔࡐࡅࡄࡖࡌࡈࠬ៖"))),
            bstack1l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣៗ"): env.get(bstack1l1_opy_ (u"ࠢࡔ࡛ࡖࡘࡊࡓ࡟ࡅࡇࡉࡍࡓࡏࡔࡊࡑࡑࡍࡉࠨ៘")),
            bstack1l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ៙"): env.get(bstack1l1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤ៚"))
        }
    if bstack1ll11l11l_opy_(env.get(bstack1l1_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࠧ៛"))):
        return {
            bstack1l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤៜ"): bstack1l1_opy_ (u"ࠧࡇࡰࡱࡸࡨࡽࡴࡸࠢ៝"),
            bstack1l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ៞"): bstack1l1_opy_ (u"ࠢࡼࡿ࠲ࡴࡷࡵࡪࡦࡥࡷ࠳ࢀࢃ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠨ៟").format(env.get(bstack1l1_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢ࡙ࡗࡒࠧ០")), env.get(bstack1l1_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡆࡉࡃࡐࡗࡑࡘࡤࡔࡁࡎࡇࠪ១")), env.get(bstack1l1_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡖࡒࡐࡌࡈࡇ࡙ࡥࡓࡍࡗࡊࠫ២")), env.get(bstack1l1_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨ៣"))),
            bstack1l1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ៤"): env.get(bstack1l1_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥ៥")),
            bstack1l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ៦"): env.get(bstack1l1_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤ៧"))
        }
    if env.get(bstack1l1_opy_ (u"ࠤࡄ࡞࡚ࡘࡅࡠࡊࡗࡘࡕࡥࡕࡔࡇࡕࡣࡆࡍࡅࡏࡖࠥ៨")) and env.get(bstack1l1_opy_ (u"ࠥࡘࡋࡥࡂࡖࡋࡏࡈࠧ៩")):
        return {
            bstack1l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ៪"): bstack1l1_opy_ (u"ࠧࡇࡺࡶࡴࡨࠤࡈࡏࠢ៫"),
            bstack1l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ៬"): bstack1l1_opy_ (u"ࠢࡼࡿࡾࢁ࠴ࡥࡢࡶ࡫࡯ࡨ࠴ࡸࡥࡴࡷ࡯ࡸࡸࡅࡢࡶ࡫࡯ࡨࡎࡪ࠽ࡼࡿࠥ៭").format(env.get(bstack1l1_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡌࡏࡖࡐࡇࡅ࡙ࡏࡏࡏࡕࡈࡖ࡛ࡋࡒࡖࡔࡌࠫ៮")), env.get(bstack1l1_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡐࡓࡑࡍࡉࡈ࡚ࠧ៯")), env.get(bstack1l1_opy_ (u"ࠪࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠪ៰"))),
            bstack1l1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ៱"): env.get(bstack1l1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧ៲")),
            bstack1l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ៳"): env.get(bstack1l1_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢ៴"))
        }
    if any([env.get(bstack1l1_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨ៵")), env.get(bstack1l1_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡘࡅࡔࡑࡏ࡚ࡊࡊ࡟ࡔࡑࡘࡖࡈࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࠣ៶")), env.get(bstack1l1_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡓࡐࡗࡕࡇࡊࡥࡖࡆࡔࡖࡍࡔࡔࠢ៷"))]):
        return {
            bstack1l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ៸"): bstack1l1_opy_ (u"ࠧࡇࡗࡔࠢࡆࡳࡩ࡫ࡂࡶ࡫࡯ࡨࠧ៹"),
            bstack1l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ៺"): env.get(bstack1l1_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡔ࡚ࡈࡌࡊࡅࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨ៻")),
            bstack1l1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ៼"): env.get(bstack1l1_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢ៽")),
            bstack1l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ៾"): env.get(bstack1l1_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤ៿"))
        }
    if env.get(bstack1l1_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡒࡺࡳࡢࡦࡴࠥ᠀")):
        return {
            bstack1l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᠁"): bstack1l1_opy_ (u"ࠢࡃࡣࡰࡦࡴࡵࠢ᠂"),
            bstack1l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᠃"): env.get(bstack1l1_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡓࡧࡶࡹࡱࡺࡳࡖࡴ࡯ࠦ᠄")),
            bstack1l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᠅"): env.get(bstack1l1_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡸ࡮࡯ࡳࡶࡍࡳࡧࡔࡡ࡮ࡧࠥ᠆")),
            bstack1l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᠇"): env.get(bstack1l1_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡓࡻ࡭ࡣࡧࡵࠦ᠈"))
        }
    if env.get(bstack1l1_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࠣ᠉")) or env.get(bstack1l1_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥ᠊")):
        return {
            bstack1l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᠋"): bstack1l1_opy_ (u"࡛ࠥࡪࡸࡣ࡬ࡧࡵࠦ᠌"),
            bstack1l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᠍"): env.get(bstack1l1_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤ᠎")),
            bstack1l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᠏"): bstack1l1_opy_ (u"ࠢࡎࡣ࡬ࡲࠥࡖࡩࡱࡧ࡯࡭ࡳ࡫ࠢ᠐") if env.get(bstack1l1_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥ᠑")) else None,
            bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᠒"): env.get(bstack1l1_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡌࡏࡔࡠࡅࡒࡑࡒࡏࡔࠣ᠓"))
        }
    if any([env.get(bstack1l1_opy_ (u"ࠦࡌࡉࡐࡠࡒࡕࡓࡏࡋࡃࡕࠤ᠔")), env.get(bstack1l1_opy_ (u"ࠧࡍࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨ᠕")), env.get(bstack1l1_opy_ (u"ࠨࡇࡐࡑࡊࡐࡊࡥࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨ᠖"))]):
        return {
            bstack1l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᠗"): bstack1l1_opy_ (u"ࠣࡉࡲࡳ࡬ࡲࡥࠡࡅ࡯ࡳࡺࡪࠢ᠘"),
            bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᠙"): None,
            bstack1l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᠚"): env.get(bstack1l1_opy_ (u"ࠦࡕࡘࡏࡋࡇࡆࡘࡤࡏࡄࠣ᠛")),
            bstack1l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᠜"): env.get(bstack1l1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣ᠝"))
        }
    if env.get(bstack1l1_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࠥ᠞")):
        return {
            bstack1l1_opy_ (u"ࠣࡰࡤࡱࡪࠨ᠟"): bstack1l1_opy_ (u"ࠤࡖ࡬࡮ࡶࡰࡢࡤ࡯ࡩࠧᠠ"),
            bstack1l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᠡ"): env.get(bstack1l1_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᠢ")),
            bstack1l1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᠣ"): bstack1l1_opy_ (u"ࠨࡊࡰࡤࠣࠧࢀࢃࠢᠤ").format(env.get(bstack1l1_opy_ (u"ࠧࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡎࡔࡈ࡟ࡊࡆࠪᠥ"))) if env.get(bstack1l1_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡏࡕࡂࡠࡋࡇࠦᠦ")) else None,
            bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᠧ"): env.get(bstack1l1_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᠨ"))
        }
    if bstack1ll11l11l_opy_(env.get(bstack1l1_opy_ (u"ࠦࡓࡋࡔࡍࡋࡉ࡝ࠧᠩ"))):
        return {
            bstack1l1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᠪ"): bstack1l1_opy_ (u"ࠨࡎࡦࡶ࡯࡭࡫ࡿࠢᠫ"),
            bstack1l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᠬ"): env.get(bstack1l1_opy_ (u"ࠣࡆࡈࡔࡑࡕ࡙ࡠࡗࡕࡐࠧᠭ")),
            bstack1l1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᠮ"): env.get(bstack1l1_opy_ (u"ࠥࡗࡎ࡚ࡅࡠࡐࡄࡑࡊࠨᠯ")),
            bstack1l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᠰ"): env.get(bstack1l1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢᠱ"))
        }
    if bstack1ll11l11l_opy_(env.get(bstack1l1_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡁࡄࡖࡌࡓࡓ࡙ࠢᠲ"))):
        return {
            bstack1l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᠳ"): bstack1l1_opy_ (u"ࠣࡉ࡬ࡸࡍࡻࡢࠡࡃࡦࡸ࡮ࡵ࡮ࡴࠤᠴ"),
            bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᠵ"): bstack1l1_opy_ (u"ࠥࡿࢂ࠵ࡻࡾ࠱ࡤࡧࡹ࡯࡯࡯ࡵ࠲ࡶࡺࡴࡳ࠰ࡽࢀࠦᠶ").format(env.get(bstack1l1_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡘࡋࡒࡗࡇࡕࡣ࡚ࡘࡌࠨᠷ")), env.get(bstack1l1_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤࡘࡅࡑࡑࡖࡍ࡙ࡕࡒ࡚ࠩᠸ")), env.get(bstack1l1_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡒࡖࡐࡢࡍࡉ࠭ᠹ"))),
            bstack1l1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᠺ"): env.get(bstack1l1_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠ࡙ࡒࡖࡐࡌࡌࡐ࡙ࠥᠻ")),
            bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᠼ"): env.get(bstack1l1_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢࡖ࡚ࡔ࡟ࡊࡆࠥᠽ"))
        }
    if env.get(bstack1l1_opy_ (u"ࠦࡈࡏࠢᠾ")) == bstack1l1_opy_ (u"ࠧࡺࡲࡶࡧࠥᠿ") and env.get(bstack1l1_opy_ (u"ࠨࡖࡆࡔࡆࡉࡑࠨᡀ")) == bstack1l1_opy_ (u"ࠢ࠲ࠤᡁ"):
        return {
            bstack1l1_opy_ (u"ࠣࡰࡤࡱࡪࠨᡂ"): bstack1l1_opy_ (u"ࠤ࡙ࡩࡷࡩࡥ࡭ࠤᡃ"),
            bstack1l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᡄ"): bstack1l1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࢀࢃࠢᡅ").format(env.get(bstack1l1_opy_ (u"ࠬ࡜ࡅࡓࡅࡈࡐࡤ࡛ࡒࡍࠩᡆ"))),
            bstack1l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᡇ"): None,
            bstack1l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᡈ"): None,
        }
    if env.get(bstack1l1_opy_ (u"ࠣࡖࡈࡅࡒࡉࡉࡕ࡛ࡢ࡚ࡊࡘࡓࡊࡑࡑࠦᡉ")):
        return {
            bstack1l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᡊ"): bstack1l1_opy_ (u"ࠥࡘࡪࡧ࡭ࡤ࡫ࡷࡽࠧᡋ"),
            bstack1l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᡌ"): None,
            bstack1l1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᡍ"): env.get(bstack1l1_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡒࡕࡓࡏࡋࡃࡕࡡࡑࡅࡒࡋࠢᡎ")),
            bstack1l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᡏ"): env.get(bstack1l1_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᡐ"))
        }
    if any([env.get(bstack1l1_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࠧᡑ")), env.get(bstack1l1_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡕࡓࡎࠥᡒ")), env.get(bstack1l1_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠤᡓ")), env.get(bstack1l1_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡖࡈࡅࡒࠨᡔ"))]):
        return {
            bstack1l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᡕ"): bstack1l1_opy_ (u"ࠢࡄࡱࡱࡧࡴࡻࡲࡴࡧࠥᡖ"),
            bstack1l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᡗ"): None,
            bstack1l1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᡘ"): env.get(bstack1l1_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᡙ")) or None,
            bstack1l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᡚ"): env.get(bstack1l1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢᡛ"), 0)
        }
    if env.get(bstack1l1_opy_ (u"ࠨࡇࡐࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᡜ")):
        return {
            bstack1l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᡝ"): bstack1l1_opy_ (u"ࠣࡉࡲࡇࡉࠨᡞ"),
            bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᡟ"): None,
            bstack1l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᡠ"): env.get(bstack1l1_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᡡ")),
            bstack1l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᡢ"): env.get(bstack1l1_opy_ (u"ࠨࡇࡐࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡈࡕࡕࡏࡖࡈࡖࠧᡣ"))
        }
    if env.get(bstack1l1_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᡤ")):
        return {
            bstack1l1_opy_ (u"ࠣࡰࡤࡱࡪࠨᡥ"): bstack1l1_opy_ (u"ࠤࡆࡳࡩ࡫ࡆࡳࡧࡶ࡬ࠧᡦ"),
            bstack1l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᡧ"): env.get(bstack1l1_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᡨ")),
            bstack1l1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᡩ"): env.get(bstack1l1_opy_ (u"ࠨࡃࡇࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡓࡇࡍࡆࠤᡪ")),
            bstack1l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᡫ"): env.get(bstack1l1_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᡬ"))
        }
    return {bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᡭ"): None}
def get_host_info():
    return {
        bstack1l1_opy_ (u"ࠥ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠧᡮ"): platform.node(),
        bstack1l1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨᡯ"): platform.system(),
        bstack1l1_opy_ (u"ࠧࡺࡹࡱࡧࠥᡰ"): platform.machine(),
        bstack1l1_opy_ (u"ࠨࡶࡦࡴࡶ࡭ࡴࡴࠢᡱ"): platform.version(),
        bstack1l1_opy_ (u"ࠢࡢࡴࡦ࡬ࠧᡲ"): platform.architecture()[0]
    }
def bstack111111ll1_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack1l1111l11l1_opy_():
    if bstack111l11ll_opy_.get_property(bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩᡳ")):
        return bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᡴ")
    return bstack1l1_opy_ (u"ࠪࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠩᡵ")
def bstack1l1111l11ll_opy_(driver):
    info = {
        bstack1l1_opy_ (u"ࠫࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪᡶ"): driver.capabilities,
        bstack1l1_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠩᡷ"): driver.session_id,
        bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧᡸ"): driver.capabilities.get(bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ᡹"), None),
        bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ᡺"): driver.capabilities.get(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ᡻"), None),
        bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࠬ᡼"): driver.capabilities.get(bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪ᡽"), None),
    }
    if bstack1l1111l11l1_opy_() == bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ᡾"):
        if bstack1l1111ll1_opy_():
            info[bstack1l1_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧ᡿")] = bstack1l1_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᢀ")
        elif driver.capabilities.get(bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᢁ"), {}).get(bstack1l1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ᢂ"), False):
            info[bstack1l1_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫᢃ")] = bstack1l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨᢄ")
        else:
            info[bstack1l1_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ᢅ")] = bstack1l1_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨᢆ")
    return info
def bstack1l1111ll1_opy_():
    if bstack111l11ll_opy_.get_property(bstack1l1_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᢇ")):
        return True
    if bstack1ll11l11l_opy_(os.environ.get(bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩᢈ"), None)):
        return True
    return False
def bstack11lll11l1l_opy_(bstack1l11l111lll_opy_, url, data, config):
    headers = config.get(bstack1l1_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪᢉ"), None)
    proxies = bstack1lll1l1lll_opy_(config, url)
    auth = config.get(bstack1l1_opy_ (u"ࠪࡥࡺࡺࡨࠨᢊ"), None)
    response = requests.request(
            bstack1l11l111lll_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack11lll111l_opy_(bstack1llllll11_opy_, size):
    bstack11l1111lll_opy_ = []
    while len(bstack1llllll11_opy_) > size:
        bstack1l111l1111_opy_ = bstack1llllll11_opy_[:size]
        bstack11l1111lll_opy_.append(bstack1l111l1111_opy_)
        bstack1llllll11_opy_ = bstack1llllll11_opy_[size:]
    bstack11l1111lll_opy_.append(bstack1llllll11_opy_)
    return bstack11l1111lll_opy_
def bstack1l11l1l1111_opy_(message, bstack1l11l111l1l_opy_=False):
    os.write(1, bytes(message, bstack1l1_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᢋ")))
    os.write(1, bytes(bstack1l1_opy_ (u"ࠬࡢ࡮ࠨᢌ"), bstack1l1_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᢍ")))
    if bstack1l11l111l1l_opy_:
        with open(bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠭ࡰ࠳࠴ࡽ࠲࠭ᢎ") + os.environ[bstack1l1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧᢏ")] + bstack1l1_opy_ (u"ࠩ࠱ࡰࡴ࡭ࠧᢐ"), bstack1l1_opy_ (u"ࠪࡥࠬᢑ")) as f:
            f.write(message + bstack1l1_opy_ (u"ࠫࡡࡴࠧᢒ"))
def bstack1ll11l11111_opy_():
    return os.environ[bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨᢓ")].lower() == bstack1l1_opy_ (u"࠭ࡴࡳࡷࡨࠫᢔ")
def bstack1ll1l1l11l_opy_(bstack1l111lllll1_opy_):
    return bstack1l1_opy_ (u"ࠧࡼࡿ࠲ࡿࢂ࠭ᢕ").format(bstack1l1l1l1ll11_opy_, bstack1l111lllll1_opy_)
def bstack1l111ll1_opy_():
    return bstack1ll1l11l_opy_().replace(tzinfo=None).isoformat() + bstack1l1_opy_ (u"ࠨ࡜ࠪᢖ")
def bstack1l111l1ll1l_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack1l1_opy_ (u"ࠩ࡝ࠫᢗ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack1l1_opy_ (u"ࠪ࡞ࠬᢘ")))).total_seconds() * 1000
def bstack1l1111lll11_opy_(timestamp):
    return bstack1l111lll11l_opy_(timestamp).isoformat() + bstack1l1_opy_ (u"ࠫ࡟࠭ᢙ")
def bstack1l111l1111l_opy_(bstack1l1111l1lll_opy_):
    date_format = bstack1l1_opy_ (u"࡙ࠬࠫࠦ࡯ࠨࡨࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪ࠮ࠦࡨࠪᢚ")
    bstack1l11ll111l1_opy_ = datetime.datetime.strptime(bstack1l1111l1lll_opy_, date_format)
    return bstack1l11ll111l1_opy_.isoformat() + bstack1l1_opy_ (u"࡚࠭ࠨᢛ")
def bstack1l11ll11l11_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᢜ")
    else:
        return bstack1l1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᢝ")
def bstack1ll11l11l_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack1l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᢞ")
def bstack1l1111l1ll1_opy_(val):
    return val.__str__().lower() == bstack1l1_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩᢟ")
def bstack1lll111l_opy_(bstack1l11l11l1l1_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack1l11l11l1l1_opy_ as e:
                print(bstack1l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࢁࡽࠡ࠯ࡁࠤࢀࢃ࠺ࠡࡽࢀࠦᢠ").format(func.__name__, bstack1l11l11l1l1_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1l111l11111_opy_(bstack1l11l1l1l11_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack1l11l1l1l11_opy_(cls, *args, **kwargs)
            except bstack1l11l11l1l1_opy_ as e:
                print(bstack1l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡻࡾࠢ࠰ࡂࠥࢁࡽ࠻ࠢࡾࢁࠧᢡ").format(bstack1l11l1l1l11_opy_.__name__, bstack1l11l11l1l1_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1l111l11111_opy_
    else:
        return decorator
def bstack11l11lll1l_opy_(bstack11l11ll1_opy_):
    if os.getenv(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩᢢ")) is not None:
        return bstack1ll11l11l_opy_(os.getenv(bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪᢣ")))
    if bstack1l1_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᢤ") in bstack11l11ll1_opy_ and bstack1l1111l1ll1_opy_(bstack11l11ll1_opy_[bstack1l1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᢥ")]):
        return False
    if bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᢦ") in bstack11l11ll1_opy_ and bstack1l1111l1ll1_opy_(bstack11l11ll1_opy_[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᢧ")]):
        return False
    return True
def bstack111lllll11_opy_():
    try:
        from pytest_bdd import reporting
        bstack1l111ll1l11_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠧᢨ"), None)
        return bstack1l111ll1l11_opy_ is None or bstack1l111ll1l11_opy_ == bstack1l1_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦᢩࠥ")
    except Exception as e:
        return False
def bstack1ll1ll11l1_opy_(hub_url, CONFIG):
    if bstack1lll1lll11_opy_() <= version.parse(bstack1l1_opy_ (u"ࠧ࠴࠰࠴࠷࠳࠶ࠧᢪ")):
        if hub_url:
            return bstack1l1_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤ᢫") + hub_url + bstack1l1_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨ᢬")
        return bstack11l1111l1l_opy_
    if hub_url:
        return bstack1l1_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧ᢭") + hub_url + bstack1l1_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧ᢮")
    return bstack11l11l1ll1_opy_
def bstack1l11l1ll11l_opy_():
    return isinstance(os.getenv(bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡒࡕࡈࡋࡑࠫ᢯")), str)
def bstack11l1l11111_opy_(url):
    return urlparse(url).hostname
def bstack1ll1l1lll1_opy_(hostname):
    for bstack1l11111ll1_opy_ in bstack111ll1ll1_opy_:
        regex = re.compile(bstack1l11111ll1_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack1l1ll11llll_opy_(bstack1l111l11lll_opy_, file_name, logger):
    bstack1l1l111l11_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"࠭ࡾࠨᢰ")), bstack1l111l11lll_opy_)
    try:
        if not os.path.exists(bstack1l1l111l11_opy_):
            os.makedirs(bstack1l1l111l11_opy_)
        file_path = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠧࡿࠩᢱ")), bstack1l111l11lll_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack1l1_opy_ (u"ࠨࡹࠪᢲ")):
                pass
            with open(file_path, bstack1l1_opy_ (u"ࠤࡺ࠯ࠧᢳ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1lll11l1ll_opy_.format(str(e)))
def bstack1l1ll1l11l1_opy_(file_name, key, value, logger):
    file_path = bstack1l1ll11llll_opy_(bstack1l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᢴ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1ll11ll11l_opy_ = json.load(open(file_path, bstack1l1_opy_ (u"ࠫࡷࡨࠧᢵ")))
        else:
            bstack1ll11ll11l_opy_ = {}
        bstack1ll11ll11l_opy_[key] = value
        with open(file_path, bstack1l1_opy_ (u"ࠧࡽࠫࠣᢶ")) as outfile:
            json.dump(bstack1ll11ll11l_opy_, outfile)
def bstack1llllll11l_opy_(file_name, logger):
    file_path = bstack1l1ll11llll_opy_(bstack1l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᢷ"), file_name, logger)
    bstack1ll11ll11l_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack1l1_opy_ (u"ࠧࡳࠩᢸ")) as bstack11l111ll1l_opy_:
            bstack1ll11ll11l_opy_ = json.load(bstack11l111ll1l_opy_)
    return bstack1ll11ll11l_opy_
def bstack11llll111_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡨࡪࡲࡥࡵ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬᢹ") + file_path + bstack1l1_opy_ (u"ࠩࠣࠫᢺ") + str(e))
def bstack1lll1lll11_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack1l1_opy_ (u"ࠥࡀࡓࡕࡔࡔࡇࡗࡂࠧᢻ")
def bstack11llllll11_opy_(config):
    if bstack1l1_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᢼ") in config:
        del (config[bstack1l1_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᢽ")])
        return False
    if bstack1lll1lll11_opy_() < version.parse(bstack1l1_opy_ (u"࠭࠳࠯࠶࠱࠴ࠬᢾ")):
        return False
    if bstack1lll1lll11_opy_() >= version.parse(bstack1l1_opy_ (u"ࠧ࠵࠰࠴࠲࠺࠭ᢿ")):
        return True
    if bstack1l1_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨᣀ") in config and config[bstack1l1_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩᣁ")] is False:
        return False
    else:
        return True
def bstack11l1l11l11_opy_(args_list, bstack1l11l1111ll_opy_):
    index = -1
    for value in bstack1l11l1111ll_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack11lll111_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack11lll111_opy_ = bstack11lll111_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack1l1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᣂ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᣃ"), exception=exception)
    def bstack111llll11l_opy_(self):
        if self.result != bstack1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᣄ"):
            return None
        if isinstance(self.exception_type, str) and bstack1l1_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤᣅ") in self.exception_type:
            return bstack1l1_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣᣆ")
        return bstack1l1_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤᣇ")
    def bstack1l1111lll1l_opy_(self):
        if self.result != bstack1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᣈ"):
            return None
        if self.bstack11lll111_opy_:
            return self.bstack11lll111_opy_
        return bstack1l11l1l1ll1_opy_(self.exception)
def bstack1l11l1l1ll1_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack1l111llll11_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l1111ll_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack11111ll1l_opy_(config, logger):
    try:
        import playwright
        bstack1l1111lllll_opy_ = playwright.__file__
        bstack1l11l11l11l_opy_ = os.path.split(bstack1l1111lllll_opy_)
        bstack1l11111ll11_opy_ = bstack1l11l11l11l_opy_[0] + bstack1l1_opy_ (u"ࠪ࠳ࡩࡸࡩࡷࡧࡵ࠳ࡵࡧࡣ࡬ࡣࡪࡩ࠴ࡲࡩࡣ࠱ࡦࡰ࡮࠵ࡣ࡭࡫࠱࡮ࡸ࠭ᣉ")
        os.environ[bstack1l1_opy_ (u"ࠫࡌࡒࡏࡃࡃࡏࡣࡆࡍࡅࡏࡖࡢࡌ࡙࡚ࡐࡠࡒࡕࡓ࡝࡟ࠧᣊ")] = bstack1l1ll11lll_opy_(config)
        with open(bstack1l11111ll11_opy_, bstack1l1_opy_ (u"ࠬࡸࠧᣋ")) as f:
            file_content = f.read()
            bstack1l11l11ll11_opy_ = bstack1l1_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠬᣌ")
            bstack1l111l1l1l1_opy_ = file_content.find(bstack1l11l11ll11_opy_)
            if bstack1l111l1l1l1_opy_ == -1:
              process = subprocess.Popen(bstack1l1_opy_ (u"ࠢ࡯ࡲࡰࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠦᣍ"), shell=True, cwd=bstack1l11l11l11l_opy_[0])
              process.wait()
              bstack1l11l1l111l_opy_ = bstack1l1_opy_ (u"ࠨࠤࡸࡷࡪࠦࡳࡵࡴ࡬ࡧࡹࠨ࠻ࠨᣎ")
              bstack1l11l111ll1_opy_ = bstack1l1_opy_ (u"ࠤࠥࠦࠥࡢࠢࡶࡵࡨࠤࡸࡺࡲࡪࡥࡷࡠࠧࡁࠠࡤࡱࡱࡷࡹࠦࡻࠡࡤࡲࡳࡹࡹࡴࡳࡣࡳࠤࢂࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪࠪ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠩࠬ࠿ࠥ࡯ࡦࠡࠪࡳࡶࡴࡩࡥࡴࡵ࠱ࡩࡳࡼ࠮ࡈࡎࡒࡆࡆࡒ࡟ࡂࡉࡈࡒ࡙ࡥࡈࡕࡖࡓࡣࡕࡘࡏ࡙࡛ࠬࠤࡧࡵ࡯ࡵࡵࡷࡶࡦࡶࠨࠪ࠽ࠣࠦࠧࠨᣏ")
              bstack1l11l11111l_opy_ = file_content.replace(bstack1l11l1l111l_opy_, bstack1l11l111ll1_opy_)
              with open(bstack1l11111ll11_opy_, bstack1l1_opy_ (u"ࠪࡻࠬᣐ")) as f:
                f.write(bstack1l11l11111l_opy_)
    except Exception as e:
        logger.error(bstack11111lll1_opy_.format(str(e)))
def bstack1l1ll1111_opy_():
  try:
    bstack1l111llll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠴ࡪࡴࡱࡱࠫᣑ"))
    bstack1l11l11l111_opy_ = []
    if os.path.exists(bstack1l111llll1l_opy_):
      with open(bstack1l111llll1l_opy_) as f:
        bstack1l11l11l111_opy_ = json.load(f)
      os.remove(bstack1l111llll1l_opy_)
    return bstack1l11l11l111_opy_
  except:
    pass
  return []
def bstack1l1l111111_opy_(bstack1l11ll111_opy_):
  try:
    bstack1l11l11l111_opy_ = []
    bstack1l111llll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1_opy_ (u"ࠬࡵࡰࡵ࡫ࡰࡥࡱࡥࡨࡶࡤࡢࡹࡷࡲ࠮࡫ࡵࡲࡲࠬᣒ"))
    if os.path.exists(bstack1l111llll1l_opy_):
      with open(bstack1l111llll1l_opy_) as f:
        bstack1l11l11l111_opy_ = json.load(f)
    bstack1l11l11l111_opy_.append(bstack1l11ll111_opy_)
    with open(bstack1l111llll1l_opy_, bstack1l1_opy_ (u"࠭ࡷࠨᣓ")) as f:
        json.dump(bstack1l11l11l111_opy_, f)
  except:
    pass
def bstack1l111l111_opy_(logger, bstack1l11111lll1_opy_ = False):
  try:
    test_name = os.environ.get(bstack1l1_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪᣔ"), bstack1l1_opy_ (u"ࠨࠩᣕ"))
    if test_name == bstack1l1_opy_ (u"ࠩࠪᣖ"):
        test_name = threading.current_thread().__dict__.get(bstack1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡅࡨࡩࡥࡴࡦࡵࡷࡣࡳࡧ࡭ࡦࠩᣗ"), bstack1l1_opy_ (u"ࠫࠬᣘ"))
    bstack1l1111ll1l1_opy_ = bstack1l1_opy_ (u"ࠬ࠲ࠠࠨᣙ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack1l11111lll1_opy_:
        bstack11l111l1ll_opy_ = os.environ.get(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᣚ"), bstack1l1_opy_ (u"ࠧ࠱ࠩᣛ"))
        bstack11lllll1l1_opy_ = {bstack1l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᣜ"): test_name, bstack1l1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᣝ"): bstack1l1111ll1l1_opy_, bstack1l1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᣞ"): bstack11l111l1ll_opy_}
        bstack1l11l1l1lll_opy_ = []
        bstack1l111111lll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡵࡶࡰࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪᣟ"))
        if os.path.exists(bstack1l111111lll_opy_):
            with open(bstack1l111111lll_opy_) as f:
                bstack1l11l1l1lll_opy_ = json.load(f)
        bstack1l11l1l1lll_opy_.append(bstack11lllll1l1_opy_)
        with open(bstack1l111111lll_opy_, bstack1l1_opy_ (u"ࠬࡽࠧᣠ")) as f:
            json.dump(bstack1l11l1l1lll_opy_, f)
    else:
        bstack11lllll1l1_opy_ = {bstack1l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᣡ"): test_name, bstack1l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᣢ"): bstack1l1111ll1l1_opy_, bstack1l1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᣣ"): str(multiprocessing.current_process().name)}
        if bstack1l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭ᣤ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack11lllll1l1_opy_)
  except Exception as e:
      logger.warn(bstack1l1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡶࡹࡵࡧࡶࡸࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃࠢᣥ").format(e))
def bstack1ll1111111_opy_(error_message, test_name, index, logger):
  try:
    bstack1l11ll1111l_opy_ = []
    bstack11lllll1l1_opy_ = {bstack1l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᣦ"): test_name, bstack1l1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᣧ"): error_message, bstack1l1_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᣨ"): index}
    bstack1l111llllll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1_opy_ (u"ࠧࡳࡱࡥࡳࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨᣩ"))
    if os.path.exists(bstack1l111llllll_opy_):
        with open(bstack1l111llllll_opy_) as f:
            bstack1l11ll1111l_opy_ = json.load(f)
    bstack1l11ll1111l_opy_.append(bstack11lllll1l1_opy_)
    with open(bstack1l111llllll_opy_, bstack1l1_opy_ (u"ࠨࡹࠪᣪ")) as f:
        json.dump(bstack1l11ll1111l_opy_, f)
  except Exception as e:
    logger.warn(bstack1l1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡷࡵࡢࡰࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧᣫ").format(e))
def bstack11lll1l1l_opy_(bstack1l1l1l11l_opy_, name, logger):
  try:
    bstack11lllll1l1_opy_ = {bstack1l1_opy_ (u"ࠪࡲࡦࡳࡥࠨᣬ"): name, bstack1l1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᣭ"): bstack1l1l1l11l_opy_, bstack1l1_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᣮ"): str(threading.current_thread()._name)}
    return bstack11lllll1l1_opy_
  except Exception as e:
    logger.warn(bstack1l1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡤࡨ࡬ࡦࡼࡥࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥᣯ").format(e))
  return
def bstack1l111l111l1_opy_():
    return platform.system() == bstack1l1_opy_ (u"ࠧࡘ࡫ࡱࡨࡴࡽࡳࠨᣰ")
def bstack1l1lll1l11_opy_(bstack1l11111l11l_opy_, config, logger):
    bstack1l11l1llll1_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack1l11111l11l_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡬ࡵࡧࡵࠤࡨࡵ࡮ࡧ࡫ࡪࠤࡰ࡫ࡹࡴࠢࡥࡽࠥࡸࡥࡨࡧࡻࠤࡲࡧࡴࡤࡪ࠽ࠤࢀࢃࠢᣱ").format(e))
    return bstack1l11l1llll1_opy_
def bstack1l1ll1111l1_opy_(bstack1l1111ll1ll_opy_, bstack1l111lll1ll_opy_):
    bstack1l11l111111_opy_ = version.parse(bstack1l1111ll1ll_opy_)
    bstack1l111ll1111_opy_ = version.parse(bstack1l111lll1ll_opy_)
    if bstack1l11l111111_opy_ > bstack1l111ll1111_opy_:
        return 1
    elif bstack1l11l111111_opy_ < bstack1l111ll1111_opy_:
        return -1
    else:
        return 0
def bstack1ll1l11l_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack1l111lll11l_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack1l111ll11ll_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1l11llll1_opy_(options, framework, bstack1l11lll11_opy_={}):
    if options is None:
        return
    if getattr(options, bstack1l1_opy_ (u"ࠩࡪࡩࡹ࠭ᣲ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1l1111ll1l_opy_ = caps.get(bstack1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᣳ"))
    bstack1l111ll1lll_opy_ = True
    bstack1ll11lll11_opy_ = os.environ[bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᣴ")]
    if bstack1l1111l1ll1_opy_(caps.get(bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡘ࠵ࡆࠫᣵ"))) or bstack1l1111l1ll1_opy_(caps.get(bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦࡡࡺ࠷ࡨ࠭᣶"))):
        bstack1l111ll1lll_opy_ = False
    if bstack11llllll11_opy_({bstack1l1_opy_ (u"ࠢࡶࡵࡨ࡛࠸ࡉࠢ᣷"): bstack1l111ll1lll_opy_}):
        bstack1l1111ll1l_opy_ = bstack1l1111ll1l_opy_ or {}
        bstack1l1111ll1l_opy_[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪ᣸")] = bstack1l111ll11ll_opy_(framework)
        bstack1l1111ll1l_opy_[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ᣹")] = bstack1ll11l11111_opy_()
        bstack1l1111ll1l_opy_[bstack1l1_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭᣺")] = bstack1ll11lll11_opy_
        bstack1l1111ll1l_opy_[bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭᣻")] = bstack1l11lll11_opy_
        if getattr(options, bstack1l1_opy_ (u"ࠬࡹࡥࡵࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸࡾ࠭᣼"), None):
            options.set_capability(bstack1l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ᣽"), bstack1l1111ll1l_opy_)
        else:
            options[bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ᣾")] = bstack1l1111ll1l_opy_
    else:
        if getattr(options, bstack1l1_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩ᣿"), None):
            options.set_capability(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᤀ"), bstack1l111ll11ll_opy_(framework))
            options.set_capability(bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᤁ"), bstack1ll11l11111_opy_())
            options.set_capability(bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᤂ"), bstack1ll11lll11_opy_)
            options.set_capability(bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᤃ"), bstack1l11lll11_opy_)
        else:
            options[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧᤄ")] = bstack1l111ll11ll_opy_(framework)
            options[bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᤅ")] = bstack1ll11l11111_opy_()
            options[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪᤆ")] = bstack1ll11lll11_opy_
            options[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪᤇ")] = bstack1l11lll11_opy_
    return options
def bstack1l11l11llll_opy_(ws_endpoint, framework):
    bstack1l11lll11_opy_ = bstack111l11ll_opy_.get_property(bstack1l1_opy_ (u"ࠥࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡑࡔࡒࡈ࡚ࡉࡔࡠࡏࡄࡔࠧᤈ"))
    if ws_endpoint and len(ws_endpoint.split(bstack1l1_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪᤉ"))) > 1:
        ws_url = ws_endpoint.split(bstack1l1_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫᤊ"))[0]
        if bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩᤋ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack1l11ll1l111_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack1l1_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ᤌ"))[1]))
            bstack1l11ll1l111_opy_ = bstack1l11ll1l111_opy_ or {}
            bstack1ll11lll11_opy_ = os.environ[bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᤍ")]
            bstack1l11ll1l111_opy_[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᤎ")] = str(framework) + str(__version__)
            bstack1l11ll1l111_opy_[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᤏ")] = bstack1ll11l11111_opy_()
            bstack1l11ll1l111_opy_[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᤐ")] = bstack1ll11lll11_opy_
            bstack1l11ll1l111_opy_[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᤑ")] = bstack1l11lll11_opy_
            ws_endpoint = ws_endpoint.split(bstack1l1_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬᤒ"))[0] + bstack1l1_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ᤓ") + urllib.parse.quote(json.dumps(bstack1l11ll1l111_opy_))
    return ws_endpoint
def bstack1l1l111ll_opy_():
    global bstack1l1l1111ll_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1l1l1111ll_opy_ = BrowserType.connect
    return bstack1l1l1111ll_opy_
def bstack11l1111ll1_opy_(framework_name):
    global bstack11lll1l1ll_opy_
    bstack11lll1l1ll_opy_ = framework_name
    return framework_name
def bstack1l11llll11_opy_(self, *args, **kwargs):
    global bstack1l1l1111ll_opy_
    try:
        global bstack11lll1l1ll_opy_
        if bstack1l1_opy_ (u"ࠨࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸࠬᤔ") in kwargs:
            kwargs[bstack1l1_opy_ (u"ࠩࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹ࠭ᤕ")] = bstack1l11l11llll_opy_(
                kwargs.get(bstack1l1_opy_ (u"ࠪࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺࠧᤖ"), None),
                bstack11lll1l1ll_opy_
            )
    except Exception as e:
        logger.error(bstack1l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡦࡥࡵࡹ࠺ࠡࡽࢀࠦᤗ").format(str(e)))
    return bstack1l1l1111ll_opy_(self, *args, **kwargs)
def bstack1l11ll11l1l_opy_(bstack1l1111ll11l_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1lll1l1lll_opy_(bstack1l1111ll11l_opy_, bstack1l1_opy_ (u"ࠧࠨᤘ"))
        if proxies and proxies.get(bstack1l1_opy_ (u"ࠨࡨࡵࡶࡳࡷࠧᤙ")):
            parsed_url = urlparse(proxies.get(bstack1l1_opy_ (u"ࠢࡩࡶࡷࡴࡸࠨᤚ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack1l1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡈࡰࡵࡷࠫᤛ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack1l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡱࡵࡸࠬᤜ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack1l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭ᤝ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack1l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧᤞ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1lllll1l1_opy_(bstack1l1111ll11l_opy_):
    bstack1l111l1l1ll_opy_ = {
        bstack1l1l1l1lll1_opy_[bstack1l1111llll1_opy_]: bstack1l1111ll11l_opy_[bstack1l1111llll1_opy_]
        for bstack1l1111llll1_opy_ in bstack1l1111ll11l_opy_
        if bstack1l1111llll1_opy_ in bstack1l1l1l1lll1_opy_
    }
    bstack1l111l1l1ll_opy_[bstack1l1_opy_ (u"ࠧࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠧ᤟")] = bstack1l11ll11l1l_opy_(bstack1l1111ll11l_opy_, bstack111l11ll_opy_.get_property(bstack1l1_opy_ (u"ࠨࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸࠨᤠ")))
    bstack1l11111l1ll_opy_ = [element.lower() for element in bstack1l1l1ll1111_opy_]
    bstack1l11l1l1l1l_opy_(bstack1l111l1l1ll_opy_, bstack1l11111l1ll_opy_)
    return bstack1l111l1l1ll_opy_
def bstack1l11l1l1l1l_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack1l1_opy_ (u"ࠢࠫࠬ࠭࠮ࠧᤡ")
    for value in d.values():
        if isinstance(value, dict):
            bstack1l11l1l1l1l_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack1l11l1l1l1l_opy_(item, keys)
def bstack1l1111l111l_opy_():
    bstack1l111l1ll11_opy_ = [os.environ.get(bstack1l1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡋࡏࡉࡘࡥࡄࡊࡔࠥᤢ")), os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠤࢁࠦᤣ")), bstack1l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᤤ")), os.path.join(bstack1l1_opy_ (u"ࠫ࠴ࡺ࡭ࡱࠩᤥ"), bstack1l1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᤦ"))]
    for path in bstack1l111l1ll11_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack1l1_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࠬࠨᤧ") + str(path) + bstack1l1_opy_ (u"ࠢࠨࠢࡨࡼ࡮ࡹࡴࡴ࠰ࠥᤨ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack1l1_opy_ (u"ࠣࡉ࡬ࡺ࡮ࡴࡧࠡࡲࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲࡸࠦࡦࡰࡴࠣࠫࠧᤩ") + str(path) + bstack1l1_opy_ (u"ࠤࠪࠦᤪ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack1l1_opy_ (u"ࠥࡊ࡮ࡲࡥࠡࠩࠥᤫ") + str(path) + bstack1l1_opy_ (u"ࠦࠬࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡩࡣࡶࠤࡹ࡮ࡥࠡࡴࡨࡵࡺ࡯ࡲࡦࡦࠣࡴࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴࡳ࠯ࠤ᤬"))
            else:
                logger.debug(bstack1l1_opy_ (u"ࠧࡉࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥ࠭ࠢ᤭") + str(path) + bstack1l1_opy_ (u"ࠨࠧࠡࡹ࡬ࡸ࡭ࠦࡷࡳ࡫ࡷࡩࠥࡶࡥࡳ࡯࡬ࡷࡸ࡯࡯࡯࠰ࠥ᤮"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack1l1_opy_ (u"ࠢࡐࡲࡨࡶࡦࡺࡩࡰࡰࠣࡷࡺࡩࡣࡦࡧࡧࡩࡩࠦࡦࡰࡴࠣࠫࠧ᤯") + str(path) + bstack1l1_opy_ (u"ࠣࠩ࠱ࠦᤰ"))
            return path
        except Exception as e:
            logger.debug(bstack1l1_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡸࡴࠥ࡬ࡩ࡭ࡧࠣࠫࢀࡶࡡࡵࡪࢀࠫ࠿ࠦࠢᤱ") + str(e) + bstack1l1_opy_ (u"ࠥࠦᤲ"))
    logger.debug(bstack1l1_opy_ (u"ࠦࡆࡲ࡬ࠡࡲࡤࡸ࡭ࡹࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠣᤳ"))
    return None
def bstack1ll1lll1l11_opy_(binary_path, bstack1lll11l111l_opy_, bs_config):
    logger.debug(bstack1l1_opy_ (u"ࠧࡉࡵࡳࡴࡨࡲࡹࠦࡃࡍࡋࠣࡔࡦࡺࡨࠡࡨࡲࡹࡳࡪ࠺ࠡࡽࢀࠦᤴ").format(binary_path))
    bstack1l1111l1l1l_opy_ = bstack1l1_opy_ (u"࠭ࠧᤵ")
    bstack1l111l111ll_opy_ = {
        bstack1l1_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᤶ"): __version__,
        bstack1l1_opy_ (u"ࠣࡱࡶࠦᤷ"): platform.system(),
        bstack1l1_opy_ (u"ࠤࡲࡷࡤࡧࡲࡤࡪࠥᤸ"): platform.machine(),
        bstack1l1_opy_ (u"ࠥࡧࡱ࡯࡟ࡷࡧࡵࡷ࡮ࡵ࡮᤹ࠣ"): bstack1l1_opy_ (u"ࠫ࠵࠭᤺"),
        bstack1l1_opy_ (u"ࠧࡹࡤ࡬ࡡ࡯ࡥࡳ࡭ࡵࡢࡩࡨ᤻ࠦ"): bstack1l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭᤼")
    }
    try:
        if binary_path:
            bstack1l111l111ll_opy_[bstack1l1_opy_ (u"ࠧࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ᤽")] = subprocess.check_output([binary_path, bstack1l1_opy_ (u"ࠣࡸࡨࡶࡸ࡯࡯࡯ࠤ᤾")]).strip().decode(bstack1l1_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨ᤿"))
        response = requests.request(
            bstack1l1_opy_ (u"ࠪࡋࡊ࡚ࠧ᥀"),
            url=bstack1ll1l1l11l_opy_(bstack1l1l1ll1l11_opy_),
            headers=None,
            auth=(bs_config[bstack1l1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭᥁")], bs_config[bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ᥂")]),
            json=None,
            params=bstack1l111l111ll_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack1l1_opy_ (u"࠭ࡵࡳ࡮ࠪ᥃") in data.keys() and bstack1l1_opy_ (u"ࠧࡶࡲࡧࡥࡹ࡫ࡤࡠࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭᥄") in data.keys():
            logger.debug(bstack1l1_opy_ (u"ࠣࡐࡨࡩࡩࠦࡴࡰࠢࡸࡴࡩࡧࡴࡦࠢࡥ࡭ࡳࡧࡲࡺ࠮ࠣࡧࡺࡸࡲࡦࡰࡷࠤࡧ࡯࡮ࡢࡴࡼࠤࡻ࡫ࡲࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠤ᥅").format(bstack1l111l111ll_opy_[bstack1l1_opy_ (u"ࠩࡦࡰ࡮ࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ᥆")]))
            bstack1l11l1ll111_opy_ = bstack1l111l1lll1_opy_(data[bstack1l1_opy_ (u"ࠪࡹࡷࡲࠧ᥇")], bstack1lll11l111l_opy_)
            bstack1l1111l1l1l_opy_ = os.path.join(bstack1lll11l111l_opy_, bstack1l11l1ll111_opy_)
            os.chmod(bstack1l1111l1l1l_opy_, 0o777) # bstack1l111ll111l_opy_ permission
            return bstack1l1111l1l1l_opy_
    except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡧࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠ࡯ࡧࡺࠤࡘࡊࡋࠡࡽࢀࠦ᥈").format(e))
    return binary_path
def bstack1l111l1lll1_opy_(bstack1l11111ll1l_opy_, bstack1l11ll111ll_opy_):
    logger.debug(bstack1l1_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡗࡉࡑࠠࡣ࡫ࡱࡥࡷࡿࠠࡧࡴࡲࡱ࠿ࠦࠢ᥉") + str(bstack1l11111ll1l_opy_) + bstack1l1_opy_ (u"ࠨࠢ᥊"))
    zip_path = os.path.join(bstack1l11ll111ll_opy_, bstack1l1_opy_ (u"ࠢࡥࡱࡺࡲࡱࡵࡡࡥࡧࡧࡣ࡫࡯࡬ࡦ࠰ࡽ࡭ࡵࠨ᥋"))
    bstack1l11l1ll111_opy_ = bstack1l1_opy_ (u"ࠨࠩ᥌")
    with requests.get(bstack1l11111ll1l_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack1l1_opy_ (u"ࠤࡺࡦࠧ᥍")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack1l1_opy_ (u"ࠥࡊ࡮ࡲࡥࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࡨࡨࠥࡹࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭࡮ࡼ࠲ࠧ᥎"))
    with zipfile.ZipFile(zip_path, bstack1l1_opy_ (u"ࠫࡷ࠭᥏")) as zip_ref:
        bstack1l11111l111_opy_ = zip_ref.namelist()
        if len(bstack1l11111l111_opy_) > 0:
            bstack1l11l1ll111_opy_ = bstack1l11111l111_opy_[0] # bstack1l111l1l111_opy_ bstack1l11ll11lll_opy_ will be bstack1l111l1llll_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack1l11ll111ll_opy_)
        logger.debug(bstack1l1_opy_ (u"ࠧࡌࡩ࡭ࡧࡶࠤࡸࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬࡭ࡻࠣࡩࡽࡺࡲࡢࡥࡷࡩࡩࠦࡴࡰࠢࠪࠦᥐ") + str(bstack1l11ll111ll_opy_) + bstack1l1_opy_ (u"ࠨࠧࠣᥑ"))
    os.remove(zip_path)
    return bstack1l11l1ll111_opy_
def get_cli_dir():
    bstack1l111l11ll1_opy_ = bstack1l1111l111l_opy_()
    if bstack1l111l11ll1_opy_:
        bstack1lll11l111l_opy_ = os.path.join(bstack1l111l11ll1_opy_, bstack1l1_opy_ (u"ࠢࡤ࡮࡬ࠦᥒ"))
        if not os.path.exists(bstack1lll11l111l_opy_):
            os.makedirs(bstack1lll11l111l_opy_, mode=0o777, exist_ok=True)
        return bstack1lll11l111l_opy_
    else:
        raise FileNotFoundError(bstack1l1_opy_ (u"ࠣࡐࡲࠤࡼࡸࡩࡵࡣࡥࡰࡪࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡓࡅࡍࠣࡦ࡮ࡴࡡࡳࡻ࠱ࠦᥓ"))
def bstack1ll1ll11111_opy_(bstack1lll11l111l_opy_):
    bstack1l1_opy_ (u"ࠤࠥࠦࡌ࡫ࡴࠡࡶ࡫ࡩࠥࡶࡡࡵࡪࠣࡪࡴࡸࠠࡵࡪࡨࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡗࡉࡑࠠࡣ࡫ࡱࡥࡷࡿࠠࡪࡰࠣࡥࠥࡽࡲࡪࡶࡤࡦࡱ࡫ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻ࠱ࠦࠧࠨᥔ")
    bstack1l11l1111l1_opy_ = [
        os.path.join(bstack1lll11l111l_opy_, f)
        for f in os.listdir(bstack1lll11l111l_opy_)
        if os.path.isfile(os.path.join(bstack1lll11l111l_opy_, f)) and f.startswith(bstack1l1_opy_ (u"ࠥࡦ࡮ࡴࡡࡳࡻ࠰ࠦᥕ"))
    ]
    if len(bstack1l11l1111l1_opy_) > 0:
        return max(bstack1l11l1111l1_opy_, key=os.path.getmtime) # get bstack1l11ll11ll1_opy_ binary
    return bstack1l1_opy_ (u"ࠦࠧᥖ")