from warnings import deprecated
from .helpers import refuse_other_kwargs


class BaseApi(object):
    """
    Simple class to buid path for entities
    """
    def __init__(self, voipms_client):
        """
        Initialize the class with your voip_user and voip_api_password

        :param mc_client: The mailchimp client connection
        :type mc_client: :mod:`voipms.voipmsclient.VoipMsClient`
        """
        super(BaseApi, self).__init__()
        self._voipms_client = voipms_client

    @staticmethod
    def _refuse_other_kwargs(kwargs):
        """Convenience staticmethod to ensure kwargs is empty.

        If not empty, raise a VoipMSValidationError."""
        refuse_other_kwargs(kwargs)

    @property
    @deprecated('endoint renamed to endpoint')
    def endoint(self):
        return self.endpoint

    @endoint.setter
    @deprecated('endoint renamed to endpoint')
    def endoint(self, value):
        self.endpoint = value
