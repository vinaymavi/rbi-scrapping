"""
Send file Google Cloud Storage
"""
from subprocess import call


class GCS(object):
    BUCKET = "gs://bnifsc_beta/csv"

    @staticmethod
    def copy(file_path):
        call(["gsutil","cp", file_path, GCS.BUCKET])
