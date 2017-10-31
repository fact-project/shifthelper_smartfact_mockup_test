import time
import threading
from . import checks as checks_module
from . import templates


def doit(arg):
    t = threading.currentThread()
    print("working on %s" % arg.__name__)
    while getattr(t, "do_run", True):
        templates.write_data_file(arg())
        time.sleep(1)


def main():
    checks = [
        # checks_module.test_ShifterOnShift,
        checks_module.test_SmartFactUpToDate,
        checks_module.test_MAGICWeatherUpToDate,
        checks_module.test_MainJsStatusCheck,
        checks_module.test_WindSpeedCheck,
        checks_module.test_WindGustCheck,
        checks_module.test_MedianCurrentCheck,
        checks_module.test_MaximumCurrentCheck,
        checks_module.test_RelativeCameraTemperatureCheck,
        checks_module.test_BiasNotOperatingDuringDataRun,
        checks_module.test_BiasChannelsInOverCurrent,
        checks_module.test_BiasVoltageNotAtReference,
        checks_module.test_ContainerTooWarm,
        checks_module.test_DriveInErrorDuringDataRun,
        checks_module.test_BiasVoltageOnButNotCalibrated,
        checks_module.test_DIMNetworkNotAvailable,
        checks_module.test_NoDimCtrlServerAvailable,
        checks_module.test_TriggerRateLowForTenMinutes,
        # checks_module.test_IsUserAwakeBeforeShutdown,
        # checks_module.test_ParkingChecklistFilled,
    ]

    input('Make sure, you are shifter tonight.')

    for check in checks:
        t = threading.Thread(target=doit, args=(check,))
        t.start()
        input('wait for the call...')
        t.do_run = False
        t.join()

    input('Make sure, you reset the original shifter.')

if __name__ == '__main__':
    main()
