"""data247 - An API client for Data 24-7."""


from requests import get


## DATA POINTS
ADDRESS = 'A'
BALANCE = 'B'
CARRIER = 'C'
EMAIL = 'E'
IP = 'P'
SMS_ADDRESS = 'T'
SUBSCRIBER = 'I'
ZIP = 'Z'


class Data247(object):
    """A Data 24-7 API wrapper."""
    API_URI = 'https://api.data24-7.com/v/2.0?user=%s&pass=%s&api=%s&out=json&addfields=cost,billable%s&p1=%s'
    TIMEOUT = 3

    def __init__(self, username, password, data_point, extra_fields=None):
        """Create a new Data24-7 API client.

        :param str username: Your data24-7 username.
        :param str password: Your data24-7 password.
        :param str data_point: The desired response data.
        :param list extra_fields: Any extra data fields you'd like returned.
        """
        self.username = username
        self.password = password
        self.data_point = data_point
        self.extra_fields = extra_fields or []

    def get(self, search, timeout=TIMEOUT):
        """Fetch the desired desired data for the desired search term.

        :param str search: The search string.
        :param float timeout: (optional) The amount of seconds to wait for a
            response before returning.
        :rtype: dict
        :returns: The desired data as a JSON dict or {} if there were errors.
        """
        response = get(self.API_URI % (
            self.username,
            self.password,
            self.data_point,
            ',' + ','.join(self.extra_fields) if self.extra_fields else '',
            search,
        ), timeout=timeout)

        if response.status_code == 200:
            results = response.json()['response']['results'][0]
            if results['status'] == 'OK':
                del results['status']
                return results

        return {}
