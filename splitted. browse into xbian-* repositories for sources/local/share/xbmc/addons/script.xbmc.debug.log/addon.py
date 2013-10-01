import os
import re
import sys
import urllib
import urllib2
from xbmc import getCondVisibility as condtition, translatePath as translate
import xbmcaddon
import xbmcgui

addon = xbmcaddon.Addon(id='script.xbmc.debug.log')
ADDON_TITLE = addon.getAddonInfo('name')

DEBUG = False

STRINGS = {
    'do_upload': 30000,
    'upload_id': 30001,
    'upload_url': 30002,
    'no_email_set': 30003,
    'email_sent': 30004
}
UPLOAD_LINK = 'http://xbmclogs.com/show.php?id=%s'
UPLOAD_URL = 'http://xbmclogs.com/'


# Open Settings on first run
if not addon.getSetting('already_shown') == 'true':
    addon.openSettings()
    addon.setSetting('already_shown', 'true')


class LogUploader(object):

    def __init__(self):
        self.__log('started')
        self.get_settings()
        found_logs = self.__get_logs()
        uploaded_logs = []
        for logfile in found_logs:
            if self.ask_upload(logfile['title']):
                paste_id = self.upload_file(logfile['path'])
                if paste_id:
                    uploaded_logs.append({'paste_id': paste_id,
                                          'title': logfile['title']})
                    self.report_msg(paste_id)
        if uploaded_logs and self.email_address:
            self.report_mail(self.email_address, uploaded_logs)
            pass

    def get_settings(self):
        self.email_address = addon.getSetting('email')
        self.__log('settings: len(email)=%d' % len(self.email_address))
        self.skip_oldlog = addon.getSetting('skip_oldlog') == 'true'
        self.__log('settings: skip_oldlog=%s' % self.skip_oldlog)

    def upload_file(self, filepath):
        self.__log('reading log...')
        file_content = open(filepath, 'r').read()
        self.__log('starting upload "%s"...' % filepath)
        post_dict = {'paste_data': file_content,
                     'api_submit': True,
                     'mode': 'xml'}
        if filepath.endswith('.log'):
            post_dict['paste_lang'] = 'xbmc'
        elif filepath.endswith('.xml'):
            post_dict['paste_lang'] = 'advancedsettings'
        post_data = urllib.urlencode(post_dict)
        req = urllib2.Request(UPLOAD_URL, post_data)
        response = urllib2.urlopen(req).read()
        self.__log('upload done.')
        r_id = re.compile('<id>([0-9]+)</id>', re.DOTALL)
        m_id = re.search(r_id, response)
        if m_id:
            paste_id = m_id.group(1)
            self.__log('paste_id=%s' % paste_id)
            return paste_id
        else:
            self.__log('upload failed with response: %s' % repr(response))

    def ask_upload(self, logfile):
        Dialog = xbmcgui.Dialog()
        msg1 = _('do_upload') % logfile
        if self.email_address:
            msg2 = _('email_sent') % self.email_address
        else:
            msg2 = _('no_email_set')
        return Dialog.yesno(ADDON_TITLE, msg1, '', msg2)

    def report_msg(self, paste_id):
        url = UPLOAD_LINK % paste_id
        Dialog = xbmcgui.Dialog()
        msg1 = _('upload_id') % paste_id
        msg2 = _('upload_url') % url
        return Dialog.ok(ADDON_TITLE, msg1, '', msg2)

    def report_mail(self, mail_address, uploaded_logs):
        url = 'http://xbmclogs.com/xbmc-addon.php'
        if not mail_address:
            raise Exception('No Email set!')
        post_dict = {'email': mail_address}
        for logfile in uploaded_logs:
            if logfile['title'] == 'xbmc.log':
                post_dict['xbmclog_id'] = logfile['paste_id']
            elif logfile['title'] == 'xbmc.old.log':
                post_dict['oldlog_id'] = logfile['paste_id']
            elif logfile['title'] == 'crash.log':
                post_dict['crashlog_id'] = logfile['paste_id']
        post_data = urllib.urlencode(post_dict)
        if DEBUG:
            print post_data
        req = urllib2.Request(url, post_data)
        response = urllib2.urlopen(req).read()
        if DEBUG:
            print response

    def __get_logs(self):
        log_path = translate('special://logpath')
        crashlog_path = None
        crashfile_match = None
        if condtition('system.platform.osx') or condtition('system.platform.ios'):
            crashlog_path = os.path.join(
                os.path.expanduser('~'),
                'Library/Logs/CrashReporter'
            )
            crashfile_match = 'XBMC'
        elif condtition('system.platform.windows'):
            crashlog_path = log_path
            crashfile_match = '.dmp'
        elif condtition('system.platform.linux'):
            crashlog_path = os.path.expanduser('~')
            crashfile_match = 'xbmc_crashlog'
        # get fullpath for xbmc.log and xbmc.old.log
        log = os.path.join(log_path, 'xbmc.log')
        log_old = os.path.join(log_path, 'xbmc.old.log')
        # check for XBMC crashlogs
        log_crash = None
        if crashlog_path and crashfile_match:
            crashlog_files = [s for s in os.listdir(crashlog_path)
                              if os.path.isfile(os.path.join(crashlog_path, s))
                              and crashfile_match in s]
            if crashlog_files:
                # we have crashlogs, get fullpath from the last one by time
                crashlog_files = self.__sort_files_by_date(crashlog_path,
                                                           crashlog_files)
                log_crash = os.path.join(crashlog_path, crashlog_files[-1])
        found_logs = []
        if os.path.isfile(log):
            found_logs.append({
                'title': 'xbmc.log',
                'path': log
            })
        if not self.skip_oldlog and os.path.isfile(log_old):
            found_logs.append({
                'title': 'xbmc.old.log',
                'path': log_old
            })
        if log_crash and os.path.isfile(log_crash):
            found_logs.append({
                'title': 'crash.log',
                'path': log_crash
            })
        return found_logs

    def __sort_files_by_date(self, path, files):
        files.sort(key=lambda f: os.path.getmtime(os.path.join(path, f)))
        return files

    def __log(self, msg):
        xbmc.log(u'%s: %s' % (ADDON_TITLE, msg))


def _(string_id):
    if string_id in STRINGS:
        return addon.getLocalizedString(STRINGS[string_id])
    else:
        self.__log('String is missing: %s' % string_id)
        return string_id


if __name__ == '__main__':
    Uploader = LogUploader()
