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
from uuid import uuid4
from bstack_utils.helper import bstack1l111ll1_opy_, bstack1l111l1ll1l_opy_
from bstack_utils.bstack1lll1l1ll_opy_ import bstack1l1l111l11l_opy_
class bstack1llll111_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack11llll11l11_opy_=None, bstack11llll1lll1_opy_=True, bstack1llllll1111_opy_=None, bstack1l1l11lll_opy_=None, result=None, duration=None, bstack1l111lll_opy_=None, meta={}):
        self.bstack1l111lll_opy_ = bstack1l111lll_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack11llll1lll1_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack11llll11l11_opy_ = bstack11llll11l11_opy_
        self.bstack1llllll1111_opy_ = bstack1llllll1111_opy_
        self.bstack1l1l11lll_opy_ = bstack1l1l11lll_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1ll11ll1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11ll1l11_opy_(self, meta):
        self.meta = meta
    def bstack11ll1111_opy_(self, hooks):
        self.hooks = hooks
    def bstack11llll1l111_opy_(self):
        bstack11lllll11l1_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack1l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ᧍"): bstack11lllll11l1_opy_,
            bstack1l1_opy_ (u"ࠬࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠧ᧎"): bstack11lllll11l1_opy_,
            bstack1l1_opy_ (u"࠭ࡶࡤࡡࡩ࡭ࡱ࡫ࡰࡢࡶ࡫ࠫ᧏"): bstack11lllll11l1_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack1l1_opy_ (u"ࠢࡖࡰࡨࡼࡵ࡫ࡣࡵࡧࡧࠤࡦࡸࡧࡶ࡯ࡨࡲࡹࡀࠠࠣ᧐") + key)
            setattr(self, key, val)
    def bstack11llll1l11l_opy_(self):
        return {
            bstack1l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭᧑"): self.name,
            bstack1l1_opy_ (u"ࠩࡥࡳࡩࡿࠧ᧒"): {
                bstack1l1_opy_ (u"ࠪࡰࡦࡴࡧࠨ᧓"): bstack1l1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ᧔"),
                bstack1l1_opy_ (u"ࠬࡩ࡯ࡥࡧࠪ᧕"): self.code
            },
            bstack1l1_opy_ (u"࠭ࡳࡤࡱࡳࡩࡸ࠭᧖"): self.scope,
            bstack1l1_opy_ (u"ࠧࡵࡣࡪࡷࠬ᧗"): self.tags,
            bstack1l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ᧘"): self.framework,
            bstack1l1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭᧙"): self.started_at
        }
    def bstack11llll1llll_opy_(self):
        return {
         bstack1l1_opy_ (u"ࠪࡱࡪࡺࡡࠨ᧚"): self.meta
        }
    def bstack11lllll11ll_opy_(self):
        return {
            bstack1l1_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡖࡪࡸࡵ࡯ࡒࡤࡶࡦࡳࠧ᧛"): {
                bstack1l1_opy_ (u"ࠬࡸࡥࡳࡷࡱࡣࡳࡧ࡭ࡦࠩ᧜"): self.bstack11llll11l11_opy_
            }
        }
    def bstack11llll1ll11_opy_(self, bstack11llll111l1_opy_, details):
        step = next(filter(lambda st: st[bstack1l1_opy_ (u"࠭ࡩࡥࠩ᧝")] == bstack11llll111l1_opy_, self.meta[bstack1l1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭᧞")]), None)
        step.update(details)
    def bstack11ll11l1_opy_(self, bstack11llll111l1_opy_):
        step = next(filter(lambda st: st[bstack1l1_opy_ (u"ࠨ࡫ࡧࠫ᧟")] == bstack11llll111l1_opy_, self.meta[bstack1l1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨ᧠")]), None)
        step.update({
            bstack1l1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ᧡"): bstack1l111ll1_opy_()
        })
    def bstack1l111l11_opy_(self, bstack11llll111l1_opy_, result, duration=None):
        bstack1llllll1111_opy_ = bstack1l111ll1_opy_()
        if bstack11llll111l1_opy_ is not None and self.meta.get(bstack1l1_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪ᧢")):
            step = next(filter(lambda st: st[bstack1l1_opy_ (u"ࠬ࡯ࡤࠨ᧣")] == bstack11llll111l1_opy_, self.meta[bstack1l1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬ᧤")]), None)
            step.update({
                bstack1l1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ᧥"): bstack1llllll1111_opy_,
                bstack1l1_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪ᧦"): duration if duration else bstack1l111l1ll1l_opy_(step[bstack1l1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭᧧")], bstack1llllll1111_opy_),
                bstack1l1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ᧨"): result.result,
                bstack1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬ᧩"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack11llll11lll_opy_):
        if self.meta.get(bstack1l1_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫ᧪")):
            self.meta[bstack1l1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬ᧫")].append(bstack11llll11lll_opy_)
        else:
            self.meta[bstack1l1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭᧬")] = [ bstack11llll11lll_opy_ ]
    def bstack11llll111ll_opy_(self):
        return {
            bstack1l1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭᧭"): self.bstack1ll11ll1_opy_(),
            **self.bstack11llll1l11l_opy_(),
            **self.bstack11llll1l111_opy_(),
            **self.bstack11llll1llll_opy_()
        }
    def bstack11llll1ll1l_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack1l1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ᧮"): self.bstack1llllll1111_opy_,
            bstack1l1_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫ᧯"): self.duration,
            bstack1l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ᧰"): self.result.result
        }
        if data[bstack1l1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ᧱")] == bstack1l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭᧲"):
            data[bstack1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭᧳")] = self.result.bstack111llll11l_opy_()
            data[bstack1l1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩ᧴")] = [{bstack1l1_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬ᧵"): self.result.bstack1l1111lll1l_opy_()}]
        return data
    def bstack11llll1l1ll_opy_(self):
        return {
            bstack1l1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ᧶"): self.bstack1ll11ll1_opy_(),
            **self.bstack11llll1l11l_opy_(),
            **self.bstack11llll1l111_opy_(),
            **self.bstack11llll1ll1l_opy_(),
            **self.bstack11llll1llll_opy_()
        }
    def bstack1l11llll_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack1l1_opy_ (u"ࠫࡘࡺࡡࡳࡶࡨࡨࠬ᧷") in event:
            return self.bstack11llll111ll_opy_()
        elif bstack1l1_opy_ (u"ࠬࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ᧸") in event:
            return self.bstack11llll1l1ll_opy_()
    def bstack1lll1ll1_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1llllll1111_opy_ = time if time else bstack1l111ll1_opy_()
        self.duration = duration if duration else bstack1l111l1ll1l_opy_(self.started_at, self.bstack1llllll1111_opy_)
        if result:
            self.result = result
class bstack11llllll_opy_(bstack1llll111_opy_):
    def __init__(self, hooks=[], bstack1ll1llll_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1ll1llll_opy_ = bstack1ll1llll_opy_
        super().__init__(*args, **kwargs, bstack1l1l11lll_opy_=bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࠫ᧹"))
    @classmethod
    def bstack11llll11ll1_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1l1_opy_ (u"ࠧࡪࡦࠪ᧺"): id(step),
                bstack1l1_opy_ (u"ࠨࡶࡨࡼࡹ࠭᧻"): step.name,
                bstack1l1_opy_ (u"ࠩ࡮ࡩࡾࡽ࡯ࡳࡦࠪ᧼"): step.keyword,
            })
        return bstack11llllll_opy_(
            **kwargs,
            meta={
                bstack1l1_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࠫ᧽"): {
                    bstack1l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ᧾"): feature.name,
                    bstack1l1_opy_ (u"ࠬࡶࡡࡵࡪࠪ᧿"): feature.filename,
                    bstack1l1_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫᨀ"): feature.description
                },
                bstack1l1_opy_ (u"ࠧࡴࡥࡨࡲࡦࡸࡩࡰࠩᨁ"): {
                    bstack1l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᨂ"): scenario.name
                },
                bstack1l1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᨃ"): steps,
                bstack1l1_opy_ (u"ࠪࡩࡽࡧ࡭ࡱ࡮ࡨࡷࠬᨄ"): bstack1l1l111l11l_opy_(test)
            }
        )
    def bstack11llll1l1l1_opy_(self):
        return {
            bstack1l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪᨅ"): self.hooks
        }
    def bstack11lllll111l_opy_(self):
        if self.bstack1ll1llll_opy_:
            return {
                bstack1l1_opy_ (u"ࠬ࡯࡮ࡵࡧࡪࡶࡦࡺࡩࡰࡰࡶࠫᨆ"): self.bstack1ll1llll_opy_
            }
        return {}
    def bstack11llll1l1ll_opy_(self):
        return {
            **super().bstack11llll1l1ll_opy_(),
            **self.bstack11llll1l1l1_opy_()
        }
    def bstack11llll111ll_opy_(self):
        return {
            **super().bstack11llll111ll_opy_(),
            **self.bstack11lllll111l_opy_()
        }
    def bstack1lll1ll1_opy_(self):
        return bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨᨇ")
class bstack1l11l11l_opy_(bstack1llll111_opy_):
    def __init__(self, hook_type, *args,bstack1ll1llll_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack11llll11l1l_opy_ = None
        self.bstack1ll1llll_opy_ = bstack1ll1llll_opy_
        super().__init__(*args, **kwargs, bstack1l1l11lll_opy_=bstack1l1_opy_ (u"ࠧࡩࡱࡲ࡯ࠬᨈ"))
    def bstack11lll11l_opy_(self):
        return self.hook_type
    def bstack11lllll1111_opy_(self):
        return {
            bstack1l1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫᨉ"): self.hook_type
        }
    def bstack11llll1l1ll_opy_(self):
        return {
            **super().bstack11llll1l1ll_opy_(),
            **self.bstack11lllll1111_opy_()
        }
    def bstack11llll111ll_opy_(self):
        return {
            **super().bstack11llll111ll_opy_(),
            bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣ࡮ࡪࠧᨊ"): self.bstack11llll11l1l_opy_,
            **self.bstack11lllll1111_opy_()
        }
    def bstack1lll1ll1_opy_(self):
        return bstack1l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࠬᨋ")
    def bstack11ll111l_opy_(self, bstack11llll11l1l_opy_):
        self.bstack11llll11l1l_opy_ = bstack11llll11l1l_opy_