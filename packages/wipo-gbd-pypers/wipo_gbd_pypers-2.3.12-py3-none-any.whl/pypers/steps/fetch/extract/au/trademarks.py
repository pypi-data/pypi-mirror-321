import json
import math
import requests
from pypers.steps.base.extract import ExtractBase


class Trademarks(ExtractBase):
    """
    Extract AUTM archive
    """
    spec = {
        "version": "2.0",
        "descr": [
            "Returns the directory with the extraction"
        ]
    }

    # we get the data_files from archive extract
    # need to collect img urls for download
    def process(self):

        # divide appnums into chunks of 100
        appnum_list_full = list(self.manifest['data_files'].keys())

        # only consider a slice based on the index present in the done file or 0 if not present
        # and the slize size given as parameter
        archive_name = self.manifest['archive_file']
        ind = archive_name.rfind("_")
        index = 0
        if ind != -1:
            index_str = archive_name[ind+1:].replace(".zip", "")
            try:
                index = int(index_str)
            except ValueError:
                self.logger.error("index parsing issue: %s: %s" % (index_str, e))

        slice_size = 50000
        max_bound = min((index+1)*slice_size, len(appnum_list_full))
        appnum_list = appnum_list_full[index*slice_size:max_bound]

        self.logger.info("processing %s records" % (str(len(appnum_list))))

        if len(appnum_list) < slice_size:
            # the last slice covers the end of the archive
            full_archive_file = self.manifest['archive_file']
            ind = full_archive_file.rfind("/")
            if ind == -1:
                self.logger.error("error recovering original archive name: %s" % (full_archive_file))
            else:
                full_archive_file = full_archive_file[ind+1:]
                ind = full_archive_file.rfind("_")
                if ind == -1:
                    self.logger.error("error recovering original archive name: %s" % (full_archive_file))
                else:
                    full_archive_file = full_archive_file[:ind]+".zip"
                    self.logger.info("last chunk for the archive file, added in manifest %s" % (full_archive_file))
                    self.manifest['archive_file'] = full_archive_file

        chunk_size = 100
        chunk_nb = int(math.ceil(float(len(appnum_list))/chunk_size))

        appnum_chunk_list = [
            appnum_list[i*chunk_size:i*chunk_size+chunk_size]
            for i in range(chunk_nb)]

        media_url = 'https://search.ipaustralia.gov.au/trademarks/external/' \
                    'api-v2/media?markId=%s'
        proxy_params, auth = self.get_connection_params('from_web')
        for appnum_chunk in appnum_chunk_list:
            with requests.session() as session:
                response = session.get(media_url % ','.join(appnum_chunk),
                                       proxies=proxy_params, auth=auth)
                medias = json.loads(response.content)

                for media in medias:
                    appnum = media['markId']
                    for idx, img in enumerate(media.get('images', [])):
                        self.add_img_url(appnum, img['location'])

