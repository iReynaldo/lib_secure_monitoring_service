from pathlib import Path

import pytest

from lib_bgp_simulator import BaseGraphSystemTester
from lib_bgp_simulator import BGPSimpleAS
from lib_bgp_simulator import Graph043

from lib_rovpp import ROVPPV1SimpleAS

from lib_secure_monitoring_service.tests.system_tests.v4_base_graph_system_tester import V4BaseGraphSystemTester
from lib_secure_monitoring_service.tests.system_tests.unstable import Unstable
from lib_secure_monitoring_service.rov_sms import ROVSMS, ROVSMSK1
from lib_secure_monitoring_service.engine_inputs import V4SubprefixHijack


class BaseHiddenHijackTester(Unstable, V4BaseGraphSystemTester):
    GraphInfoCls = Graph043
    BaseASCls = BGPSimpleAS
    EngineInputCls = V4SubprefixHijack
    base_dir = Path(__file__).parent
    adopting_asns = (8, 4, 10, 3,)
    rov_adopting_asns = (7, )


class Test003HiddenHijackROVPPV1(BaseHiddenHijackTester):
    AdoptASCls = ROVPPV1SimpleAS


class Test004HiddenHijackROVSMS(BaseHiddenHijackTester):
    AdoptASCls = ROVSMS


class Test004HiddenHijackROVSMSK1(BaseHiddenHijackTester):
    AdoptASCls = ROVSMSK1

