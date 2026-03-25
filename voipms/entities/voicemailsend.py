# coding=utf-8
"""
The Voicemail API endpoint send

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import validate_email, check_param


class VoicemailSend(BaseApi):
    """
    Send for the Voicemail endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(VoicemailSend, self).__init__(*args, **kwargs)
        self.endpoint = 'voicemail'

    def voicemail_email(self, mailbox, folder, message_num, email_address):
        """
        Move Voicemail Message to a Destination Folder

        :param mailbox: [Required] ID for a specific Mailbox (Example: 1001)
        :type mailbox: :py:class:`int`
        :param folder: [required] Name for specific Folder (Required if message id is passed, Example: 'INBOX', values from: voicemail.get_voicemail_folders)
        :type folder: :py:class:`str`
        :param message_num: [required] ID for specific Voicemail Message (Required if folder is passed, Example: 1)
        :type message_num: :py:class:`int`
        :param email_address: [required] Destination Email address (Example: john.doe@my-domain.com)
        :type email_address: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "sendVoicemailEmail"

        parameters = {
            "mailbox": check_param('mailbox', mailbox, int, '1001'),
            "folder": check_param('folder', folder, str, 'See voicemail.get_voicemail_folders'),
            "message_num": check_param('message_num', message_num, int, '1'),
            "email_address": check_param('email_address', email_address, str, '"john.doe@my-domain.com"', validator=validate_email),
        }

        return self._voipms_client._get(method, parameters)
