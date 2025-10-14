from abc import ABC, abstractmethod
from datetime import datetime, time


# ===== User 对象，包含信息 =====
class User:
    def __init__(self, is_new: bool, level: int, login_time: datetime):
        self.is_new = is_new
        self.level = level
        self.login_time = login_time


# ===== 抽象策略接口 =====
class RuleStrategy(ABC):
    @abstractmethod
    def is_valid(self, user: User) -> bool:
        pass


# ===== 具体策略 =====

class NewUserStrategy(RuleStrategy):
    def is_valid(self, user: User) -> bool:
        return user.is_new


class LevelStrategy(RuleStrategy):
    def __init__(self, min_level: int):
        self.min_level = min_level

    def is_valid(self, user: User) -> bool:
        return user.level >= self.min_level


class LoginTimeStrategy(RuleStrategy):
    def __init__(self, start: time, end: time):
        self.start = start
        self.end = end

    def is_valid(self, user: User) -> bool:
        login_time = user.login_time.time()
        return self.start <= login_time <= self.end


# ===== 支持多个策略组合（与操作） =====

class CompositeStrategy(RuleStrategy):
    def __init__(self, strategies: list[RuleStrategy]):
        self.strategies = strategies

    def is_valid(self, user: User) -> bool:
        return all(strategy.is_valid(user) for strategy in self.strategies)


# ===== 助力判断器 =====

class BoosterChecker:
    def __init__(self, strategy: RuleStrategy):
        self.strategy = strategy

    def check(self, user: User) -> bool:
        return self.strategy.is_valid(user)


# ===== 客户端代码示例 =====

if __name__ == "__main__":
    # 构造用户数据（老用户，等级5，晚上8点登录）
    user = User(is_new=False, level=5, login_time=datetime.strptime("2025-08-27 20:15:00", "%Y-%m-%d %H:%M:%S"))

    # 设定规则：等级≥5 且 登录时间在18:00~22:00
    rule1 = LevelStrategy(min_level=5)
    rule2 = LoginTimeStrategy(start=time(18, 0), end=time(22, 0))

    # 组合规则（可以添加更多策略）
    composite = CompositeStrategy([rule1, rule2])

    # 执行助力校验
    checker = BoosterChecker(composite)
    result = checker.check(user)

    print("助力是否生效:", result)
