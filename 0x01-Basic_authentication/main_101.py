#!/usr/bin/env python3
""" Main 101
created mine because why not?🥴
"""
from api.v1.auth.auth import Auth

a = Auth()

# Should return False
print(a.require_auth("/api/v1/status", ["/api/v1/stat*"]))
# Should return False
print(a.require_auth("/api/v1/stats", ["/api/v1/stat*"]))
# Should return True
print(a.require_auth("/api/v1/users", ["/api/v1/stat*"]))
# Should return False
print(a.require_auth("/api/v1/status", ["/api/v1/users", "/api/v1/stat*"]))
# Should return False
print(a.require_auth("/api/v1/users", ["/api/v1/users", "/api/v1/stat*"]))
# Should return True
print(a.require_auth("/api/v1/status", ["/api/v1/users"]))
