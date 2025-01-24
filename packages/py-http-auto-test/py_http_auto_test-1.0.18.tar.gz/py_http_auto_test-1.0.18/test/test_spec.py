import pycurl

from http_test.spec import SpecTest, verify_response


def test_verify_response_multiple_headers():
    """
    Regression test.
    We can match requirements on response headers when there's multiple
    instances of the same HTTP header in the response.
    """
    response = {
        "status_code": 200,
        "response_headers": {
            "content-type": "application/json",
            "strict-transport-security": [
                "strict-transport-security: max-age=900",
                "strict-transport-security: max-age=86400",
            ],
        },
    }

    requirements = {
        "headers": [
            "strict-transport-security: max-age=86400",
        ]
    }

    assert verify_response(response, requirements)


def test_skipped():
    """
    Verify that return values for skipped tests run() method are correct.
    """
    test = SpecTest(name="test", spec={"skip": True, "config": {}})
    is_success, fail_reason = test.run()

    assert is_success is True
    assert fail_reason == "skipped"
