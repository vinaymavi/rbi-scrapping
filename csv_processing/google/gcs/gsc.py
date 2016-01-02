"""
Send file Google Cloud Storage
"""
from subprocess import call
import logging

logger = logging.getLogger(__name__)


class GCS(object):
    BUCKET = "gs://bnifsc-beta-01/csv"

    @staticmethod
    def copy(branch_path, bank_path):
        logger.info("branch=" + branch_path)
        logger.info("bank=" + bank_path)

        call(["/Users/vinaymavi/google-cloud-sdk/bin/gsutil", "cp", branch_path, GCS.BUCKET])
        call(["/Users/vinaymavi/google-cloud-sdk/bin/gsutil", "cp", bank_path, GCS.BUCKET])
