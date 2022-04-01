# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import pytest
from rest_framework.test import APIClient


@pytest.fixture()
def drf_client():
    return APIClient()
