from pathlib import Path

import pytest

from lib_bgp_simulator import BGPSimpleAS
from lib_bgp_simulator import Graph020

from lib_rovpp import ROVPPV1SimpleAS

from lib_secure_monitoring_service.tests.system_tests.v4_base_graph_system_tester import V4BaseGraphSystemTester
from lib_secure_monitoring_service.tests.system_tests.unstable import Unstable
from lib_secure_monitoring_service.rov_sms import ROVSMS, ROVSMSK1, ROVSMSK2
from lib_secure_monitoring_service.engine_inputs import V4SubprefixHijack


class BaseHiddenHijackTester(Unstable, V4BaseGraphSystemTester):
    GraphInfoCls = Graph020
    BaseASCls = BGPSimpleAS
    EngineInputCls = V4SubprefixHijack
    base_dir = Path(__file__).parent
    adopting_asns = (32, 33, 89, )
    rov_adopting_asns = (77, )


class Test001HiddenHijackROVPPV1(BaseHiddenHijackTester):
    AdoptASCls = ROVPPV1SimpleAS


class Test002HiddenHijackROVSMS(BaseHiddenHijackTester):
    AdoptASCls = ROVSMS


class Test002HiddenHijackROVSMSK1(BaseHiddenHijackTester):
    AdoptASCls = ROVSMSK1


class Test002HiddenHijackROVSMSK2(BaseHiddenHijackTester):
    AdoptASCls = ROVSMSK2

