from .templates import write_data_file


def test_SmartFactUpToDate():
    return {'fact': {'timestamp_1': 11, 'timestamp_2': 11}}


def test_MAGICWeatherUpToDate():
    return{'weather': {'timestamp': 11}}


def test_MainJsStatusCheck():
    return{'status': {'dim_control': 'Anything'}}


def test_WindSpeedCheck():
    return {
        'weather': {'wind_speed': 60},
        'pointing': {'az': 10, 'zd': 45}  # not parked
    }


def test_WindGustCheck():
    return {
        'weather': {'wind_gusts': 60},
        'pointing': {'az': 10, 'zd': 45}  # not parked
    }


def test_MedianCurrentCheck():
    return {'current': {'calibrated': 'yes', 'median_per_sipm': 116}}


def test_MaximumCurrentCheck():
    return {'current': {'calibrated': 'yes', 'max_per_sipm': 170}}


def test_RelativeCameraTemperatureCheck():
    return {'fact': {'relative_camera_temperature': 16.0}}


def test_BiasNotOperatingDuringDataRun():
    return {
        'fact': {'system_status': 'Foo [data]'},
        'status': {'bias_control': 'Disconnected', 'mcp': 'TakingData'}
    }


def test_BiasChannelsInOverCurrent():
    return {'status': {'bias_control': 'OverCurrent'}}


def test_BiasVoltageNotAtReference():
    return {'status': {'bias_control': 'NotReferenced'}}


def test_ContainerTooWarm():
    return {'temperature': {'current': 43}}


def test_DriveInErrorDuringDataRun():
    return {
        'fact': {'system_status': 'Foo [data]'},
        'status': {'drive_control': 'PositioningFailed', 'mcp': 'TakingData'}
    }


def test_BiasVoltageOnButNotCalibrated():
    return {
        'voltage': {'median': 4},
        'status': {'bias_control': 'VoltageOn', 'feedback': 'Disconnected'},
    }


def test_DIMNetworkNotAvailable():
    return {'status': {'dim': 'Offline'}}


def test_NoDimCtrlServerAvailable():
    return {'status': {'dim_control': 'Offline'}}


def test_TriggerRateLowForTenMinutes():
    return {'status': {'mcp': 'TakingData'},
            'trigger': {'trigger_rate': 0}}
