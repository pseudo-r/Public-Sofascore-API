"""Tests for the ingest_all_teams management command."""

from io import StringIO
from unittest.mock import MagicMock, patch

import pytest
from django.core.management import call_command
from django.core.management.base import CommandError

from apps.ingest.services import IngestionResult


@pytest.mark.django_db
class TestIngestAllTeamsCommand:
    """Tests for the ingest_all_teams management command."""

    def _make_result(self, created=1, updated=0, errors=0):
        """Helper to build a mock IngestionResult."""
        result = MagicMock(spec=IngestionResult)
        result.created = created
        result.updated = updated
        result.errors = errors
        return result

    def _call(self, *args, **kwargs):
        """Call the command and capture stdout."""
        out = StringIO()
        call_command("ingest_all_teams", *args, stdout=out, **kwargs)
        return out.getvalue()

    def test_dry_run_lists_leagues(self):
        """Dry run should list leagues without making any API calls."""
        with patch("apps.ingest.services.TeamIngestionService") as mock_svc:
            output = self._call("--dry-run")

        # No API calls
        mock_svc.return_value.ingest_teams.assert_not_called()
        assert "[DRY RUN]" in output
        # Spot-check a known league appears
        assert "basketball/nba" in output or "football/nfl" in output

    def test_dry_run_with_sport_filter(self):
        """Dry run with --sport should list only that sport's leagues."""
        with patch("apps.ingest.services.TeamIngestionService"):
            output = self._call("--dry-run", "--sport", "basketball")

        assert "basketball" in output
        assert "football" not in output

    def test_sport_filter_invalid_raises(self):
        """Unknown --sport should raise CommandError."""
        with pytest.raises(CommandError, match="No leagues configured"):
            self._call("--sport", "not-a-real-sport")

    def test_successful_ingestion(self):
        """Happy path: all leagues ingest successfully."""
        mock_result = self._make_result(created=30, updated=0, errors=0)

        with patch(
            "apps.ingest.management.commands.ingest_all_teams.TeamIngestionService"
        ) as mock_cls:
            mock_cls.return_value.ingest_teams.return_value = mock_result
            output = self._call("--sport", "basketball")

        assert "Done" in output
        # Should have ingested all basketball leagues
        service = mock_cls.return_value
        assert service.ingest_teams.call_count >= 1
        # All calls should be for basketball
        for call_args in service.ingest_teams.call_args_list:
            assert call_args[0][0] == "basketball"

    def test_continue_on_error_default(self):
        """Should continue processing remaining leagues on failure."""
        def side_effect(sport, league):
            if league == "nba":
                raise RuntimeError("API timeout")
            return self._make_result()

        with patch(
            "apps.ingest.management.commands.ingest_all_teams.TeamIngestionService"
        ) as mock_cls:
            mock_cls.return_value.ingest_teams.side_effect = side_effect
            # Should not raise — default is continue-on-error
            output = self._call("--sport", "basketball")

        assert "✗" in output  # error marker in output
        assert "Done" in output  # still completes

    def test_stop_on_error_when_flag_disabled(self):
        """With --continue-on-error=False, should stop at first failure."""
        with patch(
            "apps.ingest.management.commands.ingest_all_teams.TeamIngestionService"
        ) as mock_cls:
            mock_cls.return_value.ingest_teams.side_effect = RuntimeError("fail")

            with pytest.raises((CommandError, SystemExit, RuntimeError)):
                out = StringIO()
                call_command(
                    "ingest_all_teams",
                    "--sport", "basketball",
                    "--continue-on-error",
                    False,
                    stdout=out,
                )

    def test_summary_shows_totals(self):
        """Summary line should aggregate created/updated/error counts."""
        mock_result = self._make_result(created=15, updated=5, errors=0)

        with patch(
            "apps.ingest.management.commands.ingest_all_teams.TeamIngestionService"
        ) as mock_cls:
            mock_cls.return_value.ingest_teams.return_value = mock_result
            output = self._call("--sport", "football")

        # Summary should appear
        assert "Total" in output or "created=" in output
