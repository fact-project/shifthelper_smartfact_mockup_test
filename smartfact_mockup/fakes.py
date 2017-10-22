from . import templates
from datetime import datetime, timedelta




def fake_mainjs_not_running():
    templates.write_data_file(
        'status',
        dim_control='Anything'
    )


def fake_lid_not_open():
    templates.write_data_file(
        'status',
        lid_control='Closed'
    )


def fake_humidity_high():
    templates.write_data_file(
        'weather',
        humidity=99
    )


def fake_not_parked():
    templates.write_data_file(
        'pointing',
        az=10,
        zd=45,
    )


def fake_drive_in_error():
    templates.write_data_file(
        'status',
        drive_control='PositioningFailed',
    )


def fake_data_taking():
    templates.write_data_file(
        'status',
        mcp='TakingData',
    )


def fake_data_run():
    templates.write_data_file(
        'fact',
        system_status='Foo [data]',
    )


def fake_bias_not_operating():
    templates.write_data_file(
        'status',
        bias_control='Disconnected',
    )


def fake_feedback_not_calibrated():
    templates.write_data_file(
        'status',
        feedback='Disconnected',
    )


def fake_high_windspeed():
    templates.write_data_file(
        'weather',
        wind_speed=60,
    )


def fake_high_windgusts():
    templates.write_data_file(
        'weather',
        wind_gusts=60,
    )


def fake_magic_weather_outdated():
    templates.write_data_file(
        'weather',
        timestamp=templates.datetime_to_smartfact_ms_timestamp(
            datetime.utcnow() - timedelta(minutes=11)
            ),
    )


def fake_smartfact_outdated():
    templates.write_data_file(
        'fact',
        timestamp_1=templates.datetime_to_smartfact_ms_timestamp(
            datetime.utcnow() - timedelta(minutes=11)
            ),
        timestamp_2=templates.datetime_to_smartfact_ms_timestamp(
            datetime.utcnow() - timedelta(minutes=11)
            ),
    )


def fake_median_current_high():
    templates.write_data_file(
        'current',
        calibrated='yes',
        median_per_sipm=116,
    )


def fake_maximum_current_high():
    templates.write_data_file(
        'current',
        calibrated='yes',
        max_per_sipm=170,
    )


def fake_rel_camera_temperature_high():
    templates.write_data_file(
        'fact',
        relative_camera_temperature=16.0,
    )


def fake_overcurrent():
    templates.write_data_file(
        'status',
        bias_control='OverCurrent',
    )


def fake_bias_voltage_not_at_reference():
    templates.write_data_file(
        'status',
        bias_control='NotReferenced',
    )


def fake_container_too_warm():
    templates.write_data_file(
        'temperature',
        current=43,
    )


def fake_voltage_on():
    templates.write_data_file(
        'voltage',
        median=4,
    )
    templates.write_data_file(
        'status',
        bias_control='VoltageOn',
    )


def fake_dim_network_down():
    templates.write_data_file(
        'status',
        dim='Offline',
    )


def fake_no_dimctrl_server_available():
    templates.write_data_file(
        'status',
        dim_control='Offline',
    )


def fake_trigger_rate_low_for_ten_minutes():
    templates.write_data_file(
        'trigger',
        trigger_rate=0,
    )
