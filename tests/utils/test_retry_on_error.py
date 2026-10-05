"""Tests for the retry_on_error decorator."""

import pytest

from reasongraph.utils.helpers import retry_on_error


def test_retries_then_succeeds():
    calls = []

    @retry_on_error(max_retries=2, delay=0)
    def flaky():
        calls.append(1)
        if len(calls) < 3:
            raise RuntimeError("boom")
        return "ok"

    assert flaky() == "ok"
    assert len(calls) == 3


def test_reraises_last_error_after_max_retries():
    calls = []

    @retry_on_error(max_retries=1, delay=0)
    def always_fails():
        calls.append(1)
        raise RuntimeError(f"attempt {len(calls)}")

    with pytest.raises(RuntimeError, match="attempt 2"):
        always_fails()
    assert len(calls) == 2


def test_zero_retries_calls_once():
    calls = []

    @retry_on_error(max_retries=0, delay=0)
    def fails():
        calls.append(1)
        raise RuntimeError("boom")

    with pytest.raises(RuntimeError):
        fails()
    assert len(calls) == 1


def test_negative_max_retries_rejected():
    with pytest.raises(ValueError):
        retry_on_error(max_retries=-1)
