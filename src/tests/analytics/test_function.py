import csv
import os
import shutil

import pytest
from django.test import override_settings
from django.urls import reverse
from rest_framework import status

from tests.constants import ANALYTICS_DIR, MEDIA_DIR


class TestUploadFile:
    @pytest.fixture(autouse=True)
    @override_settings(MEDIA_ROOT=MEDIA_DIR)
    def setup_class(self, db):
        os.makedirs(f"{MEDIA_DIR}{ANALYTICS_DIR}")

        file_name = "test.csv"
        with open(file_name, "w") as file:
            writer = csv.writer(file)
            # Add some rows in csv file
            writer.writerow(["Key", "Value"])
            writer.writerow(
                ["test", "test"],
            )
        self.analytics_file = open(file_name, "rb")
        self.url_list = reverse('analytics-upload')

    def test_upload_csv_file(self, drf_client):
        response = drf_client.post(self.url_list,
                                   {'analytics_file': self.analytics_file},
                                   format="multipart")
        assert response.status_code == status.HTTP_302_FOUND

    def teardown_method(self):
        shutil.rmtree(MEDIA_DIR)
