# coding=utf-8
"""
The Voicemail API endpoint set

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import validate_email, convert_bool, check_param, validate_yesno, VoipMsValidationError


class VoicemailSet(BaseApi):
    """
    Set for the Voicemail endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(VoicemailSet, self).__init__(*args, **kwargs)
        self.endpoint = 'voicemail'

    def voicemail(self, mailbox, name, password, skip_password, attach_message, delete_message,
                  say_time, timezone, say_callerid, play_instructions, language, **kwargs):
        """
        Updates the information from a specific Voicemail

        :param mailbox: [Required] ID for a specific Mailbox (Example: 1001)
        :type mailbox: :py:class:`int`
        :param name: [Required] Name for the Mailbox
        :type name: :py:class:`str`
        :param password: [Required] Password for the Mailbox
        :type password: :py:class:`int`
        :param skip_password: [Required] True if Skipping Password (True/False)
        :type skip_password: :py:class:`bool`
        :param attach_message: [Required] Yes for Attaching WAV files to Message (Values: 'yes'/'no')
        :type attach_message: :py:class:`str`
        :param delete_message: [Required] Yes for Deleting Messages (Values: 'yes'/'no')
        :type delete_message: :py:class:`str`
        :param say_time: [Required] Yes for Saying Time Stamp (Values: 'yes'/'no')
        :type say_time: :py:class:`str`
        :param timezone: [Required] Time Zone for Mailbox (Values from voicemail.get_time_zones)
        :type timezone: :py:class:`str`
        :param say_callerid: [Required] Yes for Saying the Caller ID (Values: 'yes'/'no')
        :type say_callerid: :py:class:`str`
        :param play_instructions: [Required] Code for Play Instructions Setting (Values from voicemail.get_play_instructions)
        :type play_instructions: :py:class:`str`
        :param language: [Required] Code for Language (Values from general.get_languages)
        :type language: :py:class:`str`

        :param email: Client's e-mail address for receiving Messages
        :type email: :py:class:`str`
        :param email_attachment_format: Code for Email Attachment format (Values from voicemail.get_voicemail_attachment_formats)
        :type email_attachment_format: :py:class:`str`
        :param unavailable_message_recording: Recording for the Unavailable Message (values from dids.get_recordings)
        :type unavailable_message_recording: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "setVoicemail"

        parameters = {
            "mailbox": check_param('mailbox', mailbox, int, '1001'),
            "name": check_param('name', name, str),
            "password": check_param('password', password, int),
            "skip_password": check_param('skip_password', skip_password, bool, 'True/False', validator=convert_bool),
            "attach_message": check_param('attach_message', attach_message, str, '"yes"/"no"', validator=validate_yesno),
            "delete_message": check_param('delete_message', delete_message, str, '"yes"/"no"', validator=validate_yesno),
            "say_time": check_param('say_time', say_time, str, '"yes"/"no"', validator=validate_yesno),
            "timezone": check_param('timezone', timezone, str, 'See voicemail.get_time_zones'),
            "say_callerid": check_param('say_callerid', say_callerid, str, '"yes"/"no"', validator=validate_yesno),
            "play_instructions": check_param('play_instructions', play_instructions, str, 'See voicemail.get_play_instructions'),
            "language": check_param('language', language, str, 'See general.get_languages'),
        }

        if "email" in kwargs:
            parameters['email'] = check_param('email', str, kwargs.pop('email'), example='"foo@bar.com"', validator=validate_email)

        if "email_attachment_format" in kwargs:
            parameters['email_attachment_format'] = check_param('email_attachment_format', str, kwargs.pop('email_attachment_format'), example='See voicemail.get_voicemail_attachment_formats')

        if "unavailable_message_recording" in kwargs:
            parameters["unavailable_message_recording"] = check_param("unavailable_message_recording", int, kwargs.pop("unavailable_message_recording"), 'See dids.get_recordings')

        self._refuse_other_kwargs(kwargs)

        return self._voipms_client._get(method, parameters)
