from datetime import timedelta
from datetime.datetime import utcnow
from .templates import write_data_file


def test_SmartFactUpToDate():
    write_data_file(
        'fact',
        timestamp_1=utcnow() - timedelta(minutes=11),
        timestamp_2=utcnow() - timedelta(minutes=11),
    )


def test_MAGICWeatherUpToDate():
    write_data_file(
        'weather',
        timestamp=utcnow() - timedelta(minutes=11),
    )


def test_MainJsStatusCheck():
    write_data_file('status', dim_control='Anything')


def test_WindSpeedCheck():
    write_data_file('weather', wind_speed=60)
    write_data_file('pointing', az=10, zd=45)  # not parked


def test_WindGustCheck():
    write_data_file('weather', wind_gusts=60)
    write_data_file('pointing', az=10, zd=45)  # not parked


def test_MedianCurrentCheck():
    write_data_file('current', calibrated='yes', median_per_sipm=116)


def test_MaximumCurrentCheck():
    write_data_file('current', calibrated='yes', max_per_sipm=170)


def test_RelativeCameraTemperatureCheck():
    write_data_file('fact', relative_camera_temperature=16.0)


def test_BiasNotOperatingDuringDataRun():
    # data run
    write_data_file('fact', system_status='Foo [data]')
    # Bias not operating
    write_data_file(
        'status',
        bias_control='Disconnected',  # Bias not operating
        mcp='TakingData',  # is taking data
    )


def test_BiasChannelsInOverCurrent():
    write_data_file('status', bias_control='OverCurrent')


def test_BiasVoltageNotAtReference():
    write_data_file('status', bias_control='NotReferenced')


def test_ContainerTooWarm():
    write_data_file('temperature', current=43)


def test_DriveInErrorDuringDataRun():
    # data run
    write_data_file('fact', system_status='Foo [data]')
    write_data_file(
        'status',
        drive_control='PositioningFailed',  # Drive in Error
        mcp='TakingData',  # data taking
    )


def test_BiasVoltageOnButNotCalibrated():
    # voltage on
    write_data_file('voltage', median=4)
    write_data_file('status', bias_control='VoltageOn')

    # feedback not calibrated
    write_data_file('status', feedback='Disconnected')


def test_DIMNetworkNotAvailable():
    write_data_file('status', dim='Offline')


def test_NoDimCtrlServerAvailable():
    write_data_file('status', dim_control='Offline')


def test_TriggerRateLowForTenMinutes():
    write_data_file('trigger', trigger_rate=0)
