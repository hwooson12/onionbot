from slacker import Slacker

try:
    import config
    token = config.Token
except ImportError:
    token = None

if not token:
    class IonBase(object):
        def __init__(self, _token):
            self._token = _token
else:
    class IonBase(object):
        _token = token


class Ion(IonBase):
    def __init__(self, _token):
        IonBase.__init__(self, _token)

    def send_message(self, ch, msg):
        slack = Slacker(self._token)
        slack.chat.post_message(ch, msg)
