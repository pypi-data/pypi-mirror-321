import os
import shutil
import datetime
import os
import io
import json
import time
import ntpath
from pathlib import Path
import yaml
import uuid
import datetime
import subprocess
from bs4 import BeautifulSoup
from pypers.steps.base.fetch_step_http import FetchStepHttpAuth 

class Trademarks(FetchStepHttpAuth):
    spec = {
        "version": "2.0",
        "descr": [
            "Fetch using HTTP with Basic Auth"
        ],
    }

    def parse_links(self, archive_name, count, cmd=None, archive_path=None,
                    callback=None, archive_url=None, index=0):
        if not archive_path:
            archive_path = archive_name
        if not archive_url:
            archive_url = os.path.join(self.page_url, archive_path)

        archive_name_with_index = archive_name.replace(".zip", "_" + str(index)+ ".zip")

        if archive_name in self.done_archives:
            return count, False
        if archive_name_with_index in self.done_archives:
            #return count, False
            if index>10:
                # this is a hard limit for the max number of slices for the same archive file
                return count, False
            return self.parse_links(archive_name, count, cmd=cmd, archive_path=archive_path,
                    callback=callback, archive_url=archive_url, index=index+1)
        if not self.rgx.match(archive_name):
            return count, False
        if self.limit and count == self.limit:
            return count, True
        archive_dest = os.path.join(self.output_dir, archive_name_with_index)

        self.logger.info('>> downloading: %s to %s' % (archive_url, archive_dest))

        if cmd:
            cmd = cmd % (archive_url, self.output_dir)
            retry = 0
            limit_retry = self.cmd_retry_limit
            while True:
                try:
                    subprocess.check_call(cmd.split(' '))
                    break
                except Exception as e:
                    self.logger.warning("Error in %s: %s" % (cmd, e))
                    retry += 1
                    self.logger.info("Retry %s: %s" % (retry, cmd))
                    if retry == limit_retry:
                        raise e
            os.rename(os.path.join(self.output_dir, archive_name), archive_dest)
        elif callback:
            callback(archive_dest, archive_url)
        count += 1
        self.output_files.append(archive_dest)
        if self.limit and count == self.limit:
            return count, True
        return count, False

    def specific_http_auth_process(self, session):

        count = 0
        marks_page = session.get(self.page_url, proxies=self.proxy_params,
                                 auth=self.auth)
        marks_dom = BeautifulSoup(marks_page.text, 'html.parser')
        # find marks links
        a_elts = marks_dom.findAll('a', href=self.rgx)
        a_links = [a.attrs['href'] for a in a_elts]
        a_links.reverse()
        print(a_links)

        cmd = 'wget -q --user=%s --password=%s'
        cmd += ' %s --directory-prefix=%s'
        cmd = cmd % (self.conn_params['credentials']['user'],
                     self.conn_params['credentials']['password'],
                     '%s', '%s')
        for archive_name in a_links:
            count, should_break = self.parse_links(archive_name, count, cmd=cmd)
            if should_break:
                break



