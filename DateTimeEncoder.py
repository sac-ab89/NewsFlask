import json


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        """
        Encoder to encode a given datetime object to json
        :param obj: date time object
        :return: string representation of the date
        """
        try:
            return super(DatetimeEncoder, obj).default(obj)
        except TypeError:
            return str(obj)