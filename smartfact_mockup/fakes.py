from .templates import write_data_file
from .templates import datetime_to_smartfact_ms_timestamp
from datetime import datetime, timedelta


def fake_mainjs_not_running():
    write_data_file('status', dim_control='Anything')


def fake_lid_not_open():
    write_data_file('status', lid_control='Closed')


def fake_humidity_high():
    write_data_file('weather', humidity=99)


def fake_not_parked():
    write_data_file('pointing', az=10, zd=45)


def fake_drive_in_error():
    write_data_file('status', drive_control='PositioningFailed')


def fake_data_taking():
    write_data_file('status', mcp='TakingData')


def fake_data_run():
    write_data_file('fact', system_status='Foo [data]')


def fake_bias_not_operating():
    write_data_file('status', bias_control='Disconnected')


def fake_feedback_not_calibrated():
    write_data_file('status', feedback='Disconnected')


def fake_high_windspeed():
    write_data_file('weather', wind_speed=60)


def fake_high_windgusts():
    write_data_file('weather', wind_gusts=60)


def fake_magic_weather_outdated():
    write_data_file(
        'weather',
        timestamp=datetime_to_smartfact_ms_timestamp(
            datetime.utcnow() - timedelta(minutes=11)
            ),
    )


def fake_smartfact_outdated():
    write_data_file(
        'fact',
        timestamp_1=datetime_to_smartfact_ms_timestamp(
            datetime.utcnow() - timedelta(minutes=11)
            ),
        timestamp_2=datetime_to_smartfact_ms_timestamp(
            datetime.utcnow() - timedelta(minutes=11)
            ),
    )


def fake_median_current_high():
    write_data_file('current', calibrated='yes', median_per_sipm=116)


def fake_maximum_current_high():
    write_data_file('current', calibrated='yes', max_per_sipm=170)


def fake_rel_camera_temperature_high():
    write_data_file('fact', relative_camera_temperature=16.0)


def fake_overcurrent():
    write_data_file('status', bias_control='OverCurrent')


def fake_bias_voltage_not_at_reference():
    write_data_file('status', bias_control='NotReferenced')


def fake_container_too_warm():
    write_data_file('temperature', current=43)


def fake_voltage_on():
    write_data_file('voltage', median=4)
    write_data_file('status', bias_control='VoltageOn')


def fake_dim_network_down():
    write_data_file('status', dim='Offline')


def fake_no_dimctrl_server_available():
    write_data_file('status', dim_control='Offline')


def fake_trigger_rate_low_for_ten_minutes():
    write_data_file('trigger', trigger_rate=0)
