from app import app
from chalice.test import Client
import pytest
import json
import logging


@pytest.mark.skip
def test_pass():
    assert 0 == 0


# @pytest.mark.skip
# def test_start_neptune():
#     logging.debug('Test start neptune')
#     with open('tests/start_neptune.json', ) as f:
#         data = json.load(f)
#     with Client(app, stage_name='prod') as client:
#         result = client.lambda_.invoke('handler', data)
#         logging.debug("result %s", result.payload)
#         assert result.payload is not None


# @pytest.mark.skip
# def test_start_ec2():
#     logging.debug('Test start Ec2')
#     with open('tests/start_neptune.json', ) as f:
#         data = json.load(f)
#     with Client(app, stage_name='prod') as client:
#         result = client.lambda_.invoke('start_ec2', data)
#         logging.debug("result %s", result.payload)
#         assert result.payload is not None


# @pytest.mark.skip
# def test_stop_neptune():
#     logging.debug('Test start neptune')
#     with open('tests/start_neptune.json', ) as f:
#         data = json.load(f)
#     with Client(app, stage_name='prod') as client:
#         result = client.lambda_.invoke('handler', data)
#         logging.debug("result %s", result.payload)
#         assert result.payload is not None
