from .cron_field import CronField
from .cronconfig import CronConfig

# https://github.com/aniljaiswal/cron-parser
class CronTab:
    def __init__(self, expression: str):
        self.expression = expression
        self.fields = []
        self.field_values = {}
        self.command = None

    def parse(self):
        # Split the cron expression and assign properties
        field_strings = self.expression.split(' ', 5)
        self.field_values = {
            CronConfig.FIELD_NAMES[i]: field_strings[i] for i in range(len(field_strings) - 1)
        }
        self.command = field_strings[-1]
        self._parse_fields()
        return self

    def _parse_fields(self):
        for field_name, field_value in self.field_values.items():
            cron_field = CronField(field_value, field_name)
            cron_field.parse()
            self.fields.append(cron_field)
        return self

    def format_as_json(self):
        formatted_json = {
            "expression": self.expression,
            **{field.field_name: ' '.join(map(str, field.values)) for field in self.fields},
            "command": self.command
        }
        return formatted_json

    @property
    def cron_minute(self):
        return str(self.field_values.get("minute"))

    @property
    def cron_hour(self):
        return self.field_values.get("hour")

    @property
    def cron_day_of_month(self):
        return self.field_values.get("day of month")

    @property
    def cron_month(self):
        return self.field_values.get("month")

    @property
    def cron_day_of_week(self):
        return self.field_values.get("day of week")

    @property
    def cron_command(self):
        return self.command
