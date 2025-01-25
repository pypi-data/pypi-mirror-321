# seCronTab Expression Parser

This package is a simple cron expression parser that converts a cron expression into a human-readable format. 
It takes a standard cron string with five time fields (minute, hour, day of month, month, and day of week) and a command, 
and it formats the cron expression as properties to be passed to something like `apscheduler.triggers.cron`.

***

### Installation

To install `seCronTab`, use pip:

 ```bash
   pip install seCronTab
 ```

## Usage

### Example:
```python
import json
import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from seCronTab.crontab import CronTab


def runCRON():
    print(f'runCRON: {time.ctime()}, next: {CRON0_JOB.next_run_time}')

if __name__ == '__main__':
    # Parse the cron schedule
    oCron = CronTab("*/1 * * * * runCRON").parse()

    scheduler = BackgroundScheduler()

    print(f'\n{json.dumps(oCron.format_as_json(), indent=4)}')

    try:
        trigger = CronTrigger(minute=oCron.cron_minute, hour=oCron.cron_hour, day=oCron.cron_day_of_month, month=oCron.cron_month, day_of_week=oCron.cron_day_of_week)
        CRON0_JOB = scheduler.add_job(eval(oCron.cron_command), trigger)

        scheduler.start()

        print(f"Job added: {CRON0_JOB}")
    except Exception as e:
        print(f"Error: {e}")

    while True:
        try:
            # Simulate main work
            time.sleep(1)
        except KeyboardInterrupt:  # Handle keyboard interruption
            print("Program interrupted by user. Exiting gracefully...")
            break
        except Exception as e:
            print(f"Error: {e}")
```

Output:
```shell
{
    "expression": "*/1 * * * * runCRON",
    "minute": "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59",
    "hour": "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23",
    "day of month": "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31",
    "month": "1 2 3 4 5 6 7 8 9 10 11 12",
    "day of week": "0 1 2 3 4 5 6",
    "command": "runCRON"
}
Job added: runCRON (trigger: cron[month='*', day='*', day_of_week='*', hour='*', minute='*/1'], next run at: 2025-01-18 20:00:00 CST)
runCRON: Sat Jan 18 20:00:00 2025, next: 2025-01-18 20:01:00-06:00

```