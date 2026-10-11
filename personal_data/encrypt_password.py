#!/usr/bin/env python3
"""This module hashes and validates passwords with bcrypt."""
import bcrypt


def hash_password(password: str) -> bytes:
    """Return a salted bcrypt hash of the given password."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Return True if the password matches the given bcrypt hash."""
    return bcrypt.checkpw(password.encode(), hashed_password)
