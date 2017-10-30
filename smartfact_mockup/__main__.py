from . import checks as checks_module
from . import templates


def main():
    checks = [
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
        # checks_module.test_ShifterOnShift,
        # checks_module.test_IsUserAwakeBeforeShutdown,
        # checks_module.test_ParkingChecklistFilled,
    ]

    templates.write_data_file('fact')
    templates.write_data_file('status')
    templates.write_data_file('weather')

    input('Make sure, you are shifter tonight.')

    for check in checks:
        print('executing:', check.__name__)
        check()
        input('wait for the call...')

    input('Make sure, you reset the original shifter.')

if __name__ == '__main__':
    main()
