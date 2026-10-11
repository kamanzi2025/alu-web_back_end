#!/usr/bin/env python3
"""Unit and integration tests for the client module."""
import unittest
from typing import Dict
from unittest.mock import Mock, PropertyMock, patch

from parameterized import parameterized, parameterized_class

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org: str, mock_get_json: Mock) -> None:
        """Test that org returns the get_json result for the right URL."""
        mock_get_json.return_value = {"login": org}
        client = GithubOrgClient(org)
        self.assertEqual(client.org, {"login": org})
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self) -> None:
        """Test that _public_repos_url comes from the org payload."""
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock,
                   return_value=payload):
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: Mock) -> None:
        """Test that public_repos lists the repo names from the payload."""
        mock_get_json.return_value = [
            {"name": "episodes.dart", "license": None},
            {"name": "dagger", "license": {"key": "apache-2.0"}},
            {"name": "kratu", "license": {"key": "apache-2.0"}},
        ]
        url = "https://api.github.com/orgs/google/repos"
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock,
                   return_value=url) as mock_url:
            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(),
                             ["episodes.dart", "dagger", "kratu"])
            mock_url.assert_called_once()
        mock_get_json.assert_called_once_with(url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict, license_key: str,
                         expected: bool) -> None:
        """Test that has_license matches the repo license key."""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient with only HTTP mocked."""

    @classmethod
    def setUpClass(cls) -> None:
        """Patch requests.get to return fixture payloads by URL."""
        route_payloads = {
            "https://api.github.com/orgs/google": cls.org_payload,
            cls.org_payload["repos_url"]: cls.repos_payload,
        }

        def get_payload(url):
            """Return a mock response whose json() gives the fixture."""
            if url in route_payloads:
                return Mock(**{"json.return_value": route_payloads[url]})
            raise ValueError("Unexpected URL: {}".format(url))

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """Stop the requests.get patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """Test public_repos against the fixture payloads."""
        self.assertEqual(GithubOrgClient("google").public_repos(),
                         self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """Test public_repos filtered by the apache-2.0 license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )
