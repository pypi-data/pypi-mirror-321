from .cronconfig import CronConfig
from .utils import get_range_values, get_step_values


class CronField:
    def __init__(self, value_str, field_name):
        self.value_str = value_str
        self.field_name = field_name
        self.values = []
    def parse(self):
        if self.value_str == CronConfig.ANY_VALUE:
            # Any value case
            self.values = list(range(self.get_min(), self.get_max() + 1))
        elif CronConfig.VALUE_LIST_SEPARATOR in self.value_str:
            # List of values case
            values = []
            parts = self.value_str.split(",")
            for part in parts:
                if part == "*":
                    continue  # Skip the "*" character
                if "/" in part:
                    step_parts = part.split("/")
                    if len(step_parts) == 2:
                        if int(step_parts[1]) > self.get_max():
                            raise ValueError(f"Invalid cron field value for {self.field_name}: {self.value_str}")
                        range_values = get_step_values(step_parts[1], self.get_min(), self.get_max())
                        values.extend(range_values)
                    else:
                        raise ValueError(f"Invalid cron field value for {self.field_name}: {self.value_str}")
                elif "-" in part:
                    range_values = get_range_values(part)
                    values.extend(range_values)
                else:
                    values.append(int(part))
            self.values = values
        elif CronConfig.RANGE_OF_VALUES in self.value_str:
            # Range value case
            self.values = get_range_values(self.value_str)
        elif CronConfig.STEP_VALUES in self.value_str:
            # Step value case
            step_parts = self.value_str.split(CronConfig.STEP_VALUES)
            if len(step_parts) == 2:
                if int(step_parts[1]) > self.get_max():
                    raise ValueError(f"Invalid cron field value for {self.field_name}: {self.value_str}")
                self.values = get_step_values(step_parts[1], self.get_min(), self.get_max())
            else:
                raise ValueError(f"Invalid cron field value for {self.field_name}: {self.value_str}")
        else:
            # Single value case
            self.values = [int(self.value_str)]

    def get_min(self):
        _min = [0, 0, 1, 1, 0]
        return _min[CronConfig.FIELD_NAMES.index(self.field_name)]

    def get_max(self):
        maxes = [59, 23, 31, 12, 6]
        return maxes[CronConfig.FIELD_NAMES.index(self.field_name)]
