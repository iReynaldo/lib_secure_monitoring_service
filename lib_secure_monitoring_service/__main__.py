from lib_bgp_simulator import Simulator, BGPAS, Graph

from lib_rovpp import ROVPPV1SimpleAS

from lib_secure_monitoring_service.engine_inputs import V4SubprefixHijack
from lib_secure_monitoring_service.rov_sms import ROVSMS, ROVSMSK1, ROVSMSK2, ROVSMSK3
from lib_secure_monitoring_service.v4_graph import V4Graph


def main():
    Simulator().run(graphs=[V4Graph(percent_adoptions=[0,5,10,20,40,60,80,100],
                                    adopt_as_classes=[ROVPPV1SimpleAS, ROVSMS, ROVSMSK1, ROVSMSK2, ROVSMSK3],
                                    EngineInputCls=V4SubprefixHijack,
                                    num_trials=20,
                                    BaseASCls=BGPAS)]
                    )


if __name__ == "__main__":
    main()
