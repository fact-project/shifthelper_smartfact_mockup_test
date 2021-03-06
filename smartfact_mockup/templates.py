import string
import os.path
from datetime import datetime, timedelta

template_defaults = {
    'fact': {
        'timestamp_1': 0,
        'timestamp_2': 0,
        'system_status': 'Idle [single-pe]',
        'relative_camera_temperature': 12.7,
    },
    'status': {
        'timestamp': 0,
        'dim': 'V20r15',
        'dim_control': 'Running',
        'feedback': 'Connecting',
        'bias_control': 'Disconnected',
        'mcp': 'Idle',
        'drive_control': 'Locked',
    },
    'voltage': {
        'timestamp': 0,
        'median': 0.001
    },
    'temperature': {
        'timestamp': 0,
        'current': 19.4,
    },
    'current': {
        'timestamp': 0,
        'calibrated': 'yes',
        'max_per_sipm': 3.52,
        'median_per_sipm': -8.47,
    },
    'pointing': {
        'timestamp': 0,
        'zd': 101,
        'az': 0,
    },
    'weather': {
        'timestamp': 0,
        'wind_speed': 10.4,
        'wind_gusts': 11.6,
    },
    'trigger': {
        'timestamp': 0,
        'trigger_rate': 30.4,
    },
}


def get_template(name):
    CWD = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(CWD, 'templates', '{}.data'.format(name))
    return open(path, 'r').read()


def string_field_names(s):
    field_names = [v[1] for v in string.Formatter().parse(s)]
    field_names = set(field_names)
    if None in field_names:
        field_names.remove(None)
    return list(field_names)


def write_data_file(stuff):
    smartfact_data_path = '/home/factwww/smartfact/data'
    os.makedirs(smartfact_data_path, exist_ok=True)

    for name in template_defaults:
        kw = {
            key: transform(key, value)
            for key, value
            in {**template_defaults[name], **stuff.get(name, {})}.items()
        }
        tpl = get_template(name)
        sanity_check(name, kw, tpl)

        try:
            mockup_data = tpl.format(**kw)
        except KeyError:
            print('field_names in template:', string_field_names(tpl))
            print('kw:', kw)
            raise
        out_path = os.path.join(smartfact_data_path, name+'.data')
        with open(out_path, 'w') as out_file:
            out_file.write(mockup_data)


def transform(key, value):
    if 'timestamp' in key:
        time = datetime.utcnow() - timedelta(minutes=value)
        value = datetime_to_smartfact_ms_timestamp(time)
    return value


def datetime_to_smartfact_ms_timestamp(dt=datetime.utcnow()):
    return int(dt.timestamp() * 1e3)


def sanity_check(name, kwargs, tpl):
    incoming_keys = set(kwargs.keys())
    outgoing_keys = set(string_field_names(tpl))
    keys_needed_but_not_given = outgoing_keys.difference(incoming_keys)
    keys_given_but_not_needed = incoming_keys.difference(outgoing_keys)

    if keys_needed_but_not_given or keys_given_but_not_needed:
        print(30 * '-')
        print(name)
        print('incoming_keys', incoming_keys)
        print('outgoing_keys', outgoing_keys)
        print("keys needed but not given:", outgoing_keys.difference(incoming_keys))
        print("keys given but not needed:", incoming_keys.difference(outgoing_keys))
        print(30 * '-')
