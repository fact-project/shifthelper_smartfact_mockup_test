from datetime import timedelta
from . import fakes
from tqdm import tqdm


def test_SmartFactUpToDate():
    fakes.fake_smartfact_outdated()


def test_MAGICWeatherUpToDate():
    fakes.fake_magic_weather_outdated()


def test_MainJsStatusCheck():
    fakes.fake_mainjs_not_running()


def test_WindSpeedCheck():
    fakes.fake_high_windspeed()
    fakes.fake_not_parked()


def test_WindGustCheck():
    fakes.fake_high_windgusts()
    fakes.fake_not_parked()


def test_MedianCurrentCheck():
    fakes.fake_median_current_high()


def test_MaximumCurrentCheck():
    fakes.fake_maximum_current_high()


def test_RelativeCameraTemperatureCheck():
    fakes.fake_rel_camera_temperature_high()


def test_BiasNotOperatingDuringDataRun():
    fakes.fake_data_run()
    fakes.fake_data_taking()
    fakes.fake_bias_not_operating()


def test_BiasChannelsInOverCurrent():
    fakes.fake_overcurrent()


def test_BiasVoltageNotAtReference():
    fakes.fake_bias_voltage_not_at_reference()


def test_ContainerTooWarm():
    fakes.fake_container_too_warm()


def test_DriveInErrorDuringDataRun():
    fakes.fake_drive_in_error()
    fakes.fake_data_run()
    fakes.fake_data_taking()


def test_BiasVoltageOnButNotCalibrated():
    fakes.fake_voltage_on()
    fakes.fake_feedback_not_calibrated()


def test_DIMNetworkNotAvailable():
    fakes.fake_dim_network_down()


def test_NoDimCtrlServerAvailable():
    fakes.fake_no_dimctrl_server_available()


def test_TriggerRateLowForTenMinutes():
    fakes.fake_trigger_rate_low_for_ten_minutes()
