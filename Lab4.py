class SocialNetwork:
    """
    This is the base class for social networks.
    """

    def __init__(self, name: str, users: int):
        self.name = name
        self.users = users

    def __str__(self) -> str:
        return f"{self.name} - {self.users} users"

    def __repr__(self) -> str:
        return f"SocialNetwork({self.name}, {self.users})"


class Facebook(SocialNetwork):
    """
    This class represents the Facebook social network.
    """

    def __init__(self, name: str, users: int, active_users: int):
        super().__init__(name, users)
        self.active_users = active_users

    def __str__(self) -> str:
        return f"{self.name} - {self.users} total users, {self.active_users} active users"

    def __repr__(self) -> str:
        return f"Facebook({self.name}, {self.users}, {self.active_users})"

    @staticmethod
    def promote_post(post: str) -> str:
        """
        Promote a post on Facebook.
        """
        return f"The post '{post}' has been promoted on Facebook."


if __name__ == "__main__":
    facebook = Facebook("Facebook", 3000000, 1500000)
    print(facebook)
