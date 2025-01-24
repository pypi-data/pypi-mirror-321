from datetime import datetime
import logging
import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
import pytz
from opsgeniecli.opsgeniecli import alerts_list
from opsgenielib.opsgenielib import Opsgenie


@pytest.fixture
def cli_runner() -> CliRunner:
    return CliRunner()


@pytest.fixture
def mock_context():
    with patch.object(Opsgenie, "_authenticate", return_value=MagicMock()):
        opsgenie_instance = Opsgenie(api_key="dummy_api_key")
        context = MagicMock()
        context.opsgenie = opsgenie_instance
        yield context


def test_alerts_list_saas(
    cli_runner: CliRunner, mock_context: MagicMock
) -> None:
    # Mock the return value of the requests.Session.get call for the Opsgenie instance
    with patch.object(mock_context.opsgenie._session, "get") as mock_get:
        mock_get.return_value.json.return_value = {
            "data": [
                {
                    "id": "1",
                    "status": "active",
                    "description": "desc",
                    "time": {
                        "type": "type",
                        "startDate": "2023-01-01T00:00:00Z",
                        "endDate": "2023-01-02T00:00:00Z",
                    },
                }
            ]
        }
        mock_get.return_value.raise_for_status = MagicMock()

        # Use CliRunner to invoke the command
        result = cli_runner.invoke(
            cli=alerts_list, args=["--team-name", "saas", "--not-filtered", "--last", "7d"], obj=mock_context
        )

        # Check if the 'No maintenance policies found' message is in the output
        # assert "No maintenance policies found" in result.output

        # Check if the result is successful
        assert result.exit_code == 0, result.exc_info
