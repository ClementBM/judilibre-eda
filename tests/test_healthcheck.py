from __future__ import print_function

import judilibre_client


def test_test():
    api_instance = judilibre_client.DefaultApi()
    is_ok = api_instance.healthcheck()
    assert is_ok
