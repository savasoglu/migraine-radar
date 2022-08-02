import darksky

from constants import *

import schedule
import time

from messager import send_message

numbers = []


def is_headache_pressure(pressure: float) -> bool:
    return headache_pressure_range[0] <= pressure <= headache_pressure_range[1]


def run_pressure_check() -> None:
    print('[logger   ] running pressure check')

    current_pressure = darksky.get_current_pressure(new_canaan_coord)

    if not is_headache_pressure(current_pressure):
        for num in numbers:
            send_message(
                num,
                f'Current air pressure is {current_pressure} hPa in New Canaan, CT. '
                f'Air pressure in the range [{headache_pressure_range[0]} - {headache_pressure_range[1]}] hPa can '
                f'cause migraines. '
            )


schedule.every(60).seconds.do(run_pressure_check)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
