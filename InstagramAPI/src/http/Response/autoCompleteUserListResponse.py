from InstagramAPI.src.http.Response.Objects.User import User
from InstagramAPI.src.http.Response.Response import Response


class autoCompleteUserListResponse(Response):
    def __init__(self):
        self._types = {}

        self.expires = None
        self._types["users"] = [User]
        self.users = None
