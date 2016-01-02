"""
Send file Google Cloud Storage
"""
from subprocess import call


class GCS(object):
    BUCKET = "gs://bnifsc-beta-01/csv"
    @staticmethod
    def copy(branch_path,bank_path):
        call(["gsutil","cp", branch_path, GCS.BUCKET])
        call(["gsutil","cp", bank_path, GCS.BUCKET])
