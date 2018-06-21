"""
Send file Google Cloud Storage
"""
from subprocess import call
import logging

logger = logging.getLogger(__name__)


class GCS(object):
    BUCKET = "gs://bnifsc_beta/csv/"

    @staticmethod
    def copy(csv_path):
        logger.info("csv path=" + csv_path)

        # call(["/Users/vinaymavi/google-cloud-sdk/bin/gsutil", "-m", "cp", "-r", csv_path, GCS.BUCKET])
