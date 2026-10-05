"""Tests for ingest_stream argument routing to StreamIngestor."""

from unittest.mock import patch

import pytest

from reasongraph.ingest import stream_ingestor
from reasongraph.ingest.methods import ingest_stream


@pytest.mark.parametrize(
    "source, expected_url",
    [
        ({"queue": "q", "host": "mq.local", "port": 5673}, "amqp://mq.local:5673"),
        ({"queue": "q"}, "amqp://localhost:5672"),
        ({"queue": "q", "connection_url": "amqp://u:p@h:1/vh"}, "amqp://u:p@h:1/vh"),
    ],
)
def test_ingest_stream_rabbitmq_passes_connection_url(source, expected_url):
    with patch.object(
        stream_ingestor.StreamIngestor, "ingest_rabbitmq", autospec=True
    ) as ingest_rabbitmq:
        ingest_stream(source, method="rabbitmq")

    _, queue, connection_url = ingest_rabbitmq.call_args.args
    assert queue == "q"
    assert connection_url == expected_url
