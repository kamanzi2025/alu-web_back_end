#!/usr/bin/env python3
"""Fixtures for the GithubOrgClient integration tests."""

TEST_PAYLOAD = [
  (
    {"repos_url": "https://api.github.com/orgs/google/repos"},
    [
      {
        "id": 7697149,
        "name": "episodes.dart",
        "full_name": "google/episodes.dart",
        "private": False,
        "license": None,
      },
      {
        "id": 7776515,
        "name": "cpp-netlib",
        "full_name": "google/cpp-netlib",
        "private": False,
        "license": {
          "key": "bsl-1.0",
          "name": "Boost Software License 1.0",
        },
      },
      {
        "id": 7968417,
        "name": "dagger",
        "full_name": "google/dagger",
        "private": False,
        "license": {
          "key": "apache-2.0",
          "name": "Apache License 2.0",
        },
      },
      {
        "id": 8165161,
        "name": "ios-webkit-debug-proxy",
        "full_name": "google/ios-webkit-debug-proxy",
        "private": False,
        "license": {
          "key": "other",
          "name": "Other",
        },
      },
      {
        "id": 8459994,
        "name": "google.github.io",
        "full_name": "google/google.github.io",
        "private": False,
        "license": None,
      },
      {
        "id": 8566972,
        "name": "kratu",
        "full_name": "google/kratu",
        "private": False,
        "license": {
          "key": "apache-2.0",
          "name": "Apache License 2.0",
        },
      },
      {
        "id": 8858648,
        "name": "build-debian-cloud",
        "full_name": "google/build-debian-cloud",
        "private": False,
        "license": {
          "key": "apache-2.0",
          "name": "Apache License 2.0",
        },
      },
      {
        "id": 9060347,
        "name": "traceur-compiler",
        "full_name": "google/traceur-compiler",
        "private": False,
        "license": {
          "key": "apache-2.0",
          "name": "Apache License 2.0",
        },
      },
      {
        "id": 9065917,
        "name": "firmata.py",
        "full_name": "google/firmata.py",
        "private": False,
        "license": {
          "key": "apache-2.0",
          "name": "Apache License 2.0",
        },
      },
    ],
    [
      'episodes.dart',
      'cpp-netlib',
      'dagger',
      'ios-webkit-debug-proxy',
      'google.github.io',
      'kratu',
      'build-debian-cloud',
      'traceur-compiler',
      'firmata.py',
    ],
    ['dagger', 'kratu', 'build-debian-cloud', 'traceur-compiler',
     'firmata.py'],
  )
]
