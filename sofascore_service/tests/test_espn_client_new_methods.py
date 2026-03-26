"""Tests for new ESPN client methods added during March 2026 audit."""

from pytest_httpx import HTTPXMock

from clients.espn_client import ESPNClient


class TestTeamSubResources:
    """Tests for team sub-resource endpoints (injuries, depth charts, transactions)."""

    def test_get_team_injuries(self, httpx_mock: HTTPXMock):
        """Test team injuries endpoint."""
        mock_response = {
            "team": {"id": "9", "abbreviation": "GSW"},
            "injuries": [
                {
                    "id": "1",
                    "athlete": {"id": "3136776", "displayName": "Stephen Curry"},
                    "status": "Doubtful",
                    "location": "left knee",
                }
            ],
        }
        httpx_mock.add_response(
            url="https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/9/injuries",
            json=mock_response,
        )

        with ESPNClient() as client:
            response = client.get_team_injuries("basketball", "nba", "9")

        assert response.is_success
        assert response.data["team"]["abbreviation"] == "GSW"
        assert len(response.data["injuries"]) == 1
        assert response.data["injuries"][0]["status"] == "Doubtful"

    def test_get_team_depth_chart(self, httpx_mock: HTTPXMock):
        """Test team depth chart endpoint."""
        mock_response = {
            "team": {"id": "6", "abbreviation": "DAL"},
            "positions": [
                {
                    "position": {"name": "Quarterback", "abbreviation": "QB"},
                    "athletes": [
                        {"rank": 1, "athlete": {"displayName": "Dak Prescott"}},
                        {"rank": 2, "athlete": {"displayName": "Cooper Rush"}},
                    ],
                }
            ],
        }
        httpx_mock.add_response(
            url="https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/6/depthcharts",
            json=mock_response,
        )

        with ESPNClient() as client:
            response = client.get_team_depth_chart("football", "nfl", "6")

        assert response.is_success
        assert response.data["team"]["abbreviation"] == "DAL"
        positions = response.data["positions"]
        assert positions[0]["position"]["abbreviation"] == "QB"
        assert len(positions[0]["athletes"]) == 2

    def test_get_team_transactions(self, httpx_mock: HTTPXMock):
        """Test team transactions endpoint."""
        mock_response = {
            "transactions": [
                {
                    "id": "1",
                    "type": {"text": "Signed"},
                    "athlete": {"displayName": "Test Player"},
                    "date": "2025-03-01",
                }
            ]
        }
        httpx_mock.add_response(
            url="https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/6/transactions",
            json=mock_response,
        )

        with ESPNClient() as client:
            response = client.get_team_transactions("football", "nfl", "6")

        assert response.is_success
        assert len(response.data["transactions"]) == 1
        assert response.data["transactions"][0]["type"]["text"] == "Signed"


class TestGameSituationEndpoints:
    """Tests for game situation sub-resource endpoints."""

    def test_get_game_situation(self, httpx_mock: HTTPXMock):
        """Test game situation endpoint (down, distance, possession)."""
        mock_response = {
            "down": 3,
            "distance": 7,
            "isRedZone": False,
            "possession": {"id": "12", "displayName": "Kansas City Chiefs"},
        }
        url = (
            "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl"
            "/events/401671823/competitions/401671823/situation"
        )
        httpx_mock.add_response(url=url, json=mock_response)

        with ESPNClient() as client:
            response = client.get_game_situation("football", "nfl", "401671823")

        assert response.is_success
        assert response.data["down"] == 3
        assert response.data["distance"] == 7

    def test_get_game_predictor(self, httpx_mock: HTTPXMock):
        """Test ESPN game predictor endpoint."""
        mock_response = {
            "header": "ESPN BPI Win Probability",
            "homeTeam": {"gameProjection": "63.4"},
            "awayTeam": {"gameProjection": "36.6"},
        }
        url = (
            "https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba"
            "/events/401765432/competitions/401765432/predictor"
        )
        httpx_mock.add_response(url=url, json=mock_response)

        with ESPNClient() as client:
            response = client.get_game_predictor("basketball", "nba", "401765432")

        assert response.is_success
        assert float(response.data["homeTeam"]["gameProjection"]) > 50

    def test_get_game_broadcasts(self, httpx_mock: HTTPXMock):
        """Test game broadcasts endpoint."""
        mock_response = {
            "count": 1,
            "items": [
                {
                    "media": {"shortName": "ESPN"},
                    "market": {"id": "1", "type": "National"},
                }
            ],
        }
        url = (
            "https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba"
            "/events/401765432/competitions/401765432/broadcasts"
        )
        httpx_mock.add_response(url=url, json=mock_response)

        with ESPNClient() as client:
            response = client.get_game_broadcasts("basketball", "nba", "401765432")

        assert response.is_success
        assert response.data["items"][0]["media"]["shortName"] == "ESPN"

    def test_game_endpoints_use_event_id_as_competition_id_default(
        self, httpx_mock: HTTPXMock
    ):
        """Test that competition_id defaults to event_id when not provided."""
        mock_response = {"count": 0, "items": []}
        url = (
            "https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba"
            "/events/99999/competitions/99999/broadcasts"
        )
        httpx_mock.add_response(url=url, json=mock_response)

        with ESPNClient() as client:
            response = client.get_game_broadcasts("basketball", "nba", "99999")

        assert response.is_success


class TestCoachesEndpoints:
    """Tests for coaches endpoints."""

    def test_get_coaches_current_season(self, httpx_mock: HTTPXMock):
        """Test coaches endpoint without season (current season)."""
        mock_response = {
            "count": 30,
            "items": [
                {
                    "id": "6010",
                    "firstName": "Steve",
                    "lastName": "Kerr",
                    "experience": 10,
                }
            ],
        }
        httpx_mock.add_response(
            url="https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/coaches?limit=100",
            json=mock_response,
        )

        with ESPNClient() as client:
            response = client.get_coaches("basketball", "nba")

        assert response.is_success
        assert response.data["count"] == 30
        assert response.data["items"][0]["lastName"] == "Kerr"

    def test_get_coaches_with_season(self, httpx_mock: HTTPXMock):
        """Test coaches endpoint with specific season."""
        mock_response = {"count": 32, "items": []}
        httpx_mock.add_response(
            url="https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/coaches?limit=100",
            json=mock_response,
        )

        with ESPNClient() as client:
            response = client.get_coaches("football", "nfl", season=2024)

        assert response.is_success

    def test_get_coach_by_id(self, httpx_mock: HTTPXMock):
        """Test single coach profile endpoint."""
        mock_response = {
            "id": "6010",
            "firstName": "Steve",
            "lastName": "Kerr",
            "experience": 10,
            "record": {"overall": {"wins": 548, "losses": 232}},
        }
        httpx_mock.add_response(
            url="https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/coaches/6010",
            json=mock_response,
        )

        with ESPNClient() as client:
            response = client.get_coach("basketball", "nba", "6010")

        assert response.is_success
        assert response.data["id"] == "6010"
        assert response.data["record"]["overall"]["wins"] == 548


class TestQBREndpoint:
    """Tests for QBR (Quarterback Rating) endpoint."""

    def test_get_qbr_season_totals(self, httpx_mock: HTTPXMock):
        """Test QBR season totals endpoint."""
        mock_response = {
            "leaders": [
                {"athlete": {"displayName": "Patrick Mahomes"}, "value": 82.4}
            ]
        }
        url = (
            "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl"
            "/seasons/2024/types/2/groups/1/qbr/0"
        )
        httpx_mock.add_response(url=url, json=mock_response)

        with ESPNClient() as client:
            response = client.get_qbr(league="nfl", season=2024)

        assert response.is_success
        assert response.data["leaders"][0]["value"] == 82.4

    def test_get_qbr_weekly(self, httpx_mock: HTTPXMock):
        """Test QBR weekly endpoint."""
        mock_response = {"leaders": []}
        url = (
            "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl"
            "/seasons/2024/types/2/weeks/1/qbr/0"
        )
        httpx_mock.add_response(url=url, json=mock_response)

        with ESPNClient() as client:
            response = client.get_qbr(league="nfl", season=2024, week=1)

        assert response.is_success

    def test_get_qbr_home_split(self, httpx_mock: HTTPXMock):
        """Test QBR with home split (split=1)."""
        mock_response = {"leaders": []}
        url = (
            "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl"
            "/seasons/2024/types/2/groups/1/qbr/1"
        )
        httpx_mock.add_response(url=url, json=mock_response)

        with ESPNClient() as client:
            response = client.get_qbr(league="nfl", season=2024, split=1)

        assert response.is_success

    def test_get_qbr_ncaaf(self, httpx_mock: HTTPXMock):
        """Test QBR for College Football (group=80)."""
        mock_response = {"leaders": []}
        url = (
            "https://sports.core.api.espn.com/v2/sports/football/leagues/college-football"
            "/seasons/2024/types/2/groups/80/qbr/0"
        )
        httpx_mock.add_response(url=url, json=mock_response)

        with ESPNClient() as client:
            response = client.get_qbr(
                league="college-football", season=2024, group=80
            )

        assert response.is_success


class TestPowerIndexEndpoint:
    """Tests for Power Index (BPI / SP+) endpoint."""

    def test_get_power_index_league_wide(self, httpx_mock: HTTPXMock):
        """Test power index for whole league."""
        mock_response = {
            "count": 351,
            "items": [{"team": {"id": "99"}, "value": 18.4}],
        }
        url = (
            "https://sports.core.api.espn.com/v2/sports/basketball/leagues"
            "/mens-college-basketball/seasons/2025/powerindex"
        )
        httpx_mock.add_response(url=url, json=mock_response)

        with ESPNClient() as client:
            response = client.get_power_index(
                "basketball", "mens-college-basketball", 2025
            )

        assert response.is_success
        assert response.data["count"] == 351

    def test_get_power_index_single_team(self, httpx_mock: HTTPXMock):
        """Test power index for a specific team."""
        mock_response = {
            "team": {"id": "150", "displayName": "Duke Blue Devils"},
            "value": 21.7,
        }
        url = (
            "https://sports.core.api.espn.com/v2/sports/basketball/leagues"
            "/mens-college-basketball/seasons/2025/powerindex/150"
        )
        httpx_mock.add_response(url=url, json=mock_response)

        with ESPNClient() as client:
            response = client.get_power_index(
                "basketball", "mens-college-basketball", 2025, team_id="150"
            )

        assert response.is_success
        assert response.data["value"] == 21.7
