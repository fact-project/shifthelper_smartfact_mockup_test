from . import templates
from datetime import datetime, timedelta


def datetime_to_smartfact_ms_timestamp(dt=datetime.utcnow()):
    return int(dt.timestamp() * 1e3)


def fake_mainjs_not_running():
    templates.write_data_file(
        'status',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        dim_control='Anything'
    )


def fake_lid_not_open():
    templates.write_data_file(
        'status',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        lid_control='Closed'
    )


def fake_humidity_high():
    templates.write_data_file(
        'weather',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        humidity=99
    )


def fake_not_parked():
    templates.write_data_file(
        'pointing',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        az=10,
        zd=45,
    )


def fake_drive_in_error():
    templates.write_data_file(
        'status',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        drive_control='PositioningFailed',
    )


def fake_data_taking():
    templates.write_data_file(
        'status',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        mcp='TakingData',
    )


def fake_data_run():
    templates.write_data_file(
        'fact',
        timestamp_1=datetime_to_smartfact_ms_timestamp(),
        timestamp_2=datetime_to_smartfact_ms_timestamp(),
        system_status='Foo [data]',
    )


def fake_bias_not_operating():
    templates.write_data_file(
        'status',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        bias_control='Disconnected',
    )


def fake_feedback_not_calibrated():
    templates.write_data_file(
        'status',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        feedback='Disconnected',
    )


def fake_high_windspeed():
    templates.write_data_file(
        'weather',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        wind_speed=60,
    )


def fake_high_windgusts():
    templates.write_data_file(
        'weather',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        wind_gusts=60,
    )


def fake_magic_weather_outdated():
    templates.write_data_file(
        'weather',
        timestamp=datetime_to_smartfact_ms_timestamp(
            datetime.utcnow() - timedelta(minutes=11)
            ),
    )


def fake_smartfact_outdated():
    templates.write_data_file(
        'fact',
        timestamp_1=datetime_to_smartfact_ms_timestamp(
            datetime.utcnow() - timedelta(minutes=11)
            ),
        timestamp_2=datetime_to_smartfact_ms_timestamp(
            datetime.utcnow() - timedelta(minutes=11)
            ),
    )


def fake_median_current_high():
    templates.write_data_file(
        'current',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        calibrated='yes',
        median_per_sipm=116,
    )


def fake_maximum_current_high():
    templates.write_data_file(
        'current',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        calibrated='yes',
        max_per_sipm=170,
    )


def fake_rel_camera_temperature_high():
    templates.write_data_file(
        'fact',
        timestamp_1=datetime_to_smartfact_ms_timestamp(),
        timestamp_2=datetime_to_smartfact_ms_timestamp(),
        relative_camera_temperature=16.0,
    )


def fake_overcurrent():
    templates.write_data_file(
        'status',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        bias_control='OverCurrent',
    )


def fake_bias_voltage_not_at_reference():
    templates.write_data_file(
        'status',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        bias_control='NotReferenced',
    )


def fake_container_too_warm():
    templates.write_data_file(
        'temperature',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        current=43,
    )


def fake_voltage_on():
    templates.write_data_file(
        'voltage',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        median=4,
    )
    templates.write_data_file(
        'status',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        bias_control='VoltageOn',
    )


def fake_dim_network_down():
    templates.write_data_file(
        'status',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        dim='Offline',
    )


def fake_no_dimctrl_server_available():
    templates.write_data_file(
        'status',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        dim_control='Offline',
    )


def fake_trigger_rate_low_for_ten_minutes():
    templates.write_data_file(
        'trigger',
        timestamp=datetime_to_smartfact_ms_timestamp(),
        trigger_rate=0,
    )
