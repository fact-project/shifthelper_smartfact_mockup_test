import time
from datetime import timedelta
from . import fakes
from tqdm import tqdm


def test_SmartFactUpToDate():
    '''conditions:
        is_shift_at_the_moment,
        is_smartfact_outdatet,
        category=CATEGORY_SHIFTER
    '''
    fakes.fake_smartfact_outdated()
    print()
    print('test_SmartFactUpToDate')
    return input(
        'verify that SH is calling you, '
        'shows a WARNING message, '
        'and sends you a telegram message'
    )


def test_MAGICWeatherUpToDate():
    '''conditions:
        is_shift_at_the_moment
        is_magic_weather_outdatet
        category=CATEGORY_SHIFTER
    '''
    fakes.fake_magic_weather_outdated()
    print()
    print('test_MAGICWeatherUpToDate')
    return input(
        'verify that SH is calling you, '
        'shows a WARNING message, '
        'and sends you a telegram message'
    )


def test_ShifterOnShift():
    '''conditions:
        is_shift_at_the_moment
        is_nobody_on_shift:

        category=CATEGORY_DEVELOPER
    '''
    # The nobody on shift test, is not done using
    # the smartfact mockup, but using the shift scheduler.
    raise NotImplementedError('needs shift scheduler DB mockup.')
    print()
    print('test_ShifterOnShift')
    return input(
        'verify that SH is calling you, '
        'shows a WARNING message, '
        'and sends you a telegram message'
    )


def test_MainJsStatusCheck():
    '''conditions:
        is_shift_at_the_moment
        is_mainjs_not_running
        category=CATEGORY_SHIFTER
    '''
    fakes.fake_mainjs_not_running()
    print()
    print('test_MainJsStatusCheck')
    return input(
        'verify that SH is calling you, '
        'shows a WARNING message, '
        'and sends you a telegram message'
    )


def test_WindSpeedCheck():
    '''conditions:
        is_shift_at_the_moment
        is_high_windspeed
        is_not_parked
        category=CATEGORY_SHIFTER
    '''
    fakes.fake_high_windspeed()
    fakes.fake_not_parked()
    print()
    print('test_WindSpeedCheck')
    return input(
        'verify that SH is calling you, '
        'shows a WARNING message, '
        'and sends you a telegram message'
    )


def test_WindGustCheck():
    '''conditions:
        is_shift_at_the_moment
        is_high_windgusts
        is_not_parked:
        category=CATEGORY_SHIFTER
    '''
    fakes.fake_high_windgusts()
    fakes.fake_not_parked()
    print()
    print('test_WindGustCheck')
    return input(
        'verify that SH is calling you, '
        'shows a WARNING message, '
        'and sends you a telegram message'
    )


def test_MedianCurrentCheck():
    '''conditions:
        is_shift_at_the_moment
        is_median_current_high
        category=CATEGORY_SHIFTER
    '''
    fakes.fake_median_current_high()
    print()
    print('test_MedianCurrentCheck')
    return input(
        'verify that SH is calling you, '
        'shows a WARNING message, '
        'and sends you a telegram message'
    )


def test_MaximumCurrentCheck():
    '''conditions:
        is_shift_at_the_moment
        is_maximum_current_high
        category=CATEGORY_SHIFTER
    '''
    fakes.fake_maximum_current_high()
    print()
    print('test_MaximumCurrentCheck')
    return input(
        'verify that SH is calling you, '
        'shows a WARNING message, '
        'and sends you a telegram message'
    )


def test_RelativeCameraTemperatureCheck():
    '''conditions:
        is_shift_at_the_moment
        is_rel_camera_temperature_high
        category=CATEGORY_SHIFTER
    '''
    fakes.fake_rel_camera_temperature_high()
    print()
    print('test_RelativeCameraTemperatureCheck')
    return input(
        'verify that SH is calling you, '
        'shows a WARNING message, '
        'and sends you a telegram message'
    )


def test_BiasNotOperatingDuringDataRun():
    '''conditions:
        is_shift_at_the_moment
        is_data_taking
        is_data_run
        is_bias_not_operating
        category=CATEGORY_SHIFTER
    '''
    fakes.fake_data_run()
    fakes.fake_data_taking()
    fakes.fake_bias_not_operating()
    print()
    print('test_BiasNotOperatingDuringDataRun')
    return input(
        'verify that SH is calling you, '
        'shows a WARNING message, '
        'and sends you a telegram message'
    )


def test_BiasChannelsInOverCurrent():
    '''conditions:
        is_shift_at_the_moment
        is_overcurrent
        category=CATEGORY_SHIFTER
    '''
    fakes.fake_overcurrent()
    print()
    print('test_BiasChannelsInOverCurrent')
    return input(
        'verify that SH is calling you, '
        'shows a WARNING message, '
        'and sends you a telegram message'
    )


def test_BiasVoltageNotAtReference():
    '''conditions:
        is_shift_at_the_moment
        is_bias_voltage_not_at_reference
        category=CATEGORY_SHIFTER
    '''
    fakes.fake_bias_voltage_not_at_reference()
    print()
    print('test_BiasVoltageNotAtReference')
    return input(
        'verify that SH is calling you, '
        'shows a WARNING message, '
        'and sends you a telegram message'
    )


def test_ContainerTooWarm():
    '''conditions:
        is_shift_at_the_moment
        is_container_too_warm
        category=CATEGORY_SHIFTER
    '''
    fakes.fake_container_too_warm()
    print()
    print('test_ContainerTooWarm')
    return input(
        'verify that SH is calling you, '
        'shows a WARNING message, '
        'and sends you a telegram message'
    )


def test_DriveInErrorDuringDataRun():
    '''conditions:
        is_shift_at_the_moment
        is_drive_error
        is_data_run
        is_data_taking
        category=CATEGORY_SHIFTER
    '''
    fakes.fake_drive_in_error()
    fakes.fake_data_run()
    fakes.fake_data_taking()
    print()
    print('test_DriveInErrorDuringDataRun')
    return input(
        'verify that SH is calling you, '
        'shows a WARNING message, '
        'and sends you a telegram message'
    )


def test_BiasVoltageOnButNotCalibrated():
    '''conditions:
        is_shift_at_the_moment
        is_voltage_on
        is_feedback_not_calibrated
        category=CATEGORY_SHIFTER
    '''
    fakes.fake_voltage_on()
    fakes.fake_feedback_not_calibrated()
    print()
    print('test_BiasVoltageOnButNotCalibrated')
    return input(
        'verify that SH is calling you, '
        'shows a WARNING message, '
        'and sends you a telegram message'
    )


def test_DIMNetworkNotAvailable():
    '''conditions:
        is_shift_at_the_moment
        is_dim_network_down
        category=CATEGORY_SHIFTER
    '''
    fakes.fake_dim_network_down()
    print()
    print('test_DIMNetworkNotAvailable')
    return input(
        'verify that SH is calling you, '
        'shows a WARNING message, '
        'and sends you a telegram message'
    )


def test_NoDimCtrlServerAvailable():
    '''conditions:
        is_shift_at_the_moment
        is_no_dimctrl_server_available
        category=CATEGORY_SHIFTER
    '''
    fakes.fake_no_dimctrl_server_available()
    print()
    print('test_NoDimCtrlServerAvailable')
    return input(
        'verify that SH is calling you, '
        'shows a WARNING message, '
        'and sends you a telegram message'
    )


def test_IsUserAwakeBeforeShutdown():
    '''conditions:
        is_shift_at_the_moment
        is_20minutes_or_less_before_shutdown
        is_nobody_awake
        category=CATEGORY_SHIFTER
    '''
    raise NotImplementedError(' needs to modify observation schedule.')


def test_ParkingChecklistFilled():
    '''conditions:
        is_shift_at_the_moment
        is_last_shutdown_already_10min_past
        is_checklist_not_filled

        category=CATEGORY_SHIFTER
    '''
    raise NotImplementedError(' needs to modify certain DBs.')


def test_TriggerRateLowForTenMinutes():
    '''conditions:
        is_shift_at_the_moment
        is_data_taking
        is_trigger_rate_low_for_ten_minutes
        category=CATEGORY_SHIFTER
    '''
    fakes.fake_trigger_rate_low_for_ten_minutes()
    for i in tqdm(range(int(timedelta(minutes=10).total_seconds()))):
        time.sleep(1)
    print()
    print('test_TriggerRateLowForTenMinutes')
    return input(
        'verify that SH is calling you, '
        'shows a WARNING message, '
        'and sends you a telegram message'
    )
