# Copyright 2020 Alvin Chen sonoma001@gmail.com
# SPDX-License-Identifier: GPL-2.0+


import json


class Error(Exception):
    """Base class for exceptions in this module."""

    pass


class AuthenticationError(Error):
    """Authentication error"""

    def __init__(self, url):
        self.url = url
        self.message = (
            f"An error occurred during authentication against {self.url}\n"
            f"Check your API Token and try again"
        )


class AuthorizationError(Error):
    """Authorization error"""

    def __init__(self, description, response):
        self.message = (
            f"{description}\n{json.loads(response.text)['message']} ({response.status_code})"
        )


class DependencyTrackApiError(Error):
    """Error during a DependencyTrack GET request"""

    def __init__(self, description, response):
        if response.status_code == 400:
            errors = json.loads(response.text)
            messages = ""
            for error in errors:
                messages += f"{error['message']}\n"

            self.message = (
                f"{description}: {messages} ({response.status_code})"
            )
        else:
            self.message = {
                f"{description}: {response.reason} ({response.status_code})"
            }
