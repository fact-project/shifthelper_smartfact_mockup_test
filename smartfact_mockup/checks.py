from datetime import datetime, timedelta
from .templates import write_data_file

utcnow = datetime.utcnow


def all_good():
    write_data_file('fact')
    write_data_file('status')
    write_data_file('weather')
    write_data_file('pointing')
    write_data_file('current')
    write_data_file('temperature')
    write_data_file('voltage')


def test_SmartFactUpToDate():
    all_good()
    write_data_file(
        'fact',
        timestamp_1=utcnow() - timedelta(minutes=11),
        timestamp_2=utcnow() - timedelta(minutes=11),
    )


def test_MAGICWeatherUpToDate():
    all_good()
    write_data_file(
        'weather',
        timestamp=utcnow() - timedelta(minutes=11),
    )


def test_MainJsStatusCheck():
    all_good()
    write_data_file('status', dim_control='Anything')


def test_WindSpeedCheck():
    all_good()
    write_data_file('weather', wind_speed=60)
    write_data_file('pointing', az=10, zd=45)  # not parked


def test_WindGustCheck():
    all_good()
    write_data_file('weather', wind_gusts=60)
    write_data_file('pointing', az=10, zd=45)  # not parked


def test_MedianCurrentCheck():
    all_good()
    write_data_file('current', calibrated='yes', median_per_sipm=116)


def test_MaximumCurrentCheck():
    all_good()
    write_data_file('current', calibrated='yes', max_per_sipm=170)


def test_RelativeCameraTemperatureCheck():
    all_good()
    write_data_file('fact', relative_camera_temperature=16.0)


def test_BiasNotOperatingDuringDataRun():
    all_good()
    # data run
    write_data_file('fact', system_status='Foo [data]')
    # Bias not operating
    write_data_file(
        'status',
        bias_control='Disconnected',  # Bias not operating
        mcp='TakingData',  # is taking data
    )


def test_BiasChannelsInOverCurrent():
    all_good()
    write_data_file('status', bias_control='OverCurrent')


def test_BiasVoltageNotAtReference():
    all_good()
    write_data_file('status', bias_control='NotReferenced')


def test_ContainerTooWarm():
    all_good()
    write_data_file('temperature', current=43)


def test_DriveInErrorDuringDataRun():
    all_good()
    # data run
    write_data_file('fact', system_status='Foo [data]')
    write_data_file(
        'status',
        drive_control='PositioningFailed',  # Drive in Error
        mcp='TakingData',  # data taking
    )


def test_BiasVoltageOnButNotCalibrated():
    all_good()
    # voltage on
    write_data_file('voltage', median=4)
    write_data_file(
        'status',
        bias_control='VoltageOn',
        feedback='Disconnected',     # feedback not calibrated
    )


def test_DIMNetworkNotAvailable():
    all_good()
    write_data_file('status', dim='Offline')


def test_NoDimCtrlServerAvailable():
    all_good()
    write_data_file('status', dim_control='Offline')


def test_TriggerRateLowForTenMinutes():
    all_good()
    write_data_file('trigger', trigger_rate=0)
