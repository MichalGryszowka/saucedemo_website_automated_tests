from dataclasses import dataclass


@dataclass
class UserName:
    user_1: str = "standard_user"
    user_2: str = "locked_out_user"
    user_3: str = "problem_user"
    user_4: str = "performance_glitch_user"


@dataclass
class Password:
    pwd: str = "secret_sauce"

