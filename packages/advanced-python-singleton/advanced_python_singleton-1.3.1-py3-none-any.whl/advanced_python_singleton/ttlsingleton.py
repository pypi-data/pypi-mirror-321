from expiringdict import ExpiringDict

from advanced_python_singleton.singleton import Singleton


class TtlSingleton(Singleton):
    """
    TtlSingleton metaclass
    기능:
        Singleton과 동일하나, TTL(Time To Live)이 지원되는 Singleton
        TTL이 지나면 새로운 인스턴스 생성
    사용법:
        class SomeClass(metaclass=TtlSingleton, ttl=60):
    version: v1.3
    history:
        [v1.3][2025/01/15] ttl이 다른 클래스를 선언하면 마지막 클래스의 ttl값으로 초기화되는 문제 수정
        [v1.2][2025/01/13] 클래스 이름만으로도 동일한 인스턴스 여부를 파악하게 하는 옵션 추가(use_class_name_only)
        [v1.0][2024/07/04] 최초 작성
    """

    __DEFAULT_TTL = 60
    __MAX_BUFFER_SIZE = 1000

    __ttl_cache = {f'ttl_{__DEFAULT_TTL}': ExpiringDict(max_len=__MAX_BUFFER_SIZE, max_age_seconds=__DEFAULT_TTL)}

    def __new__(cls, name, bases, dct, **kwargs):
        ttl = kwargs.get('ttl', TtlSingleton.__DEFAULT_TTL)
        if TtlSingleton.__ttl_cache.get(f'ttl_{ttl}') is None:
            TtlSingleton.__ttl_cache[f'ttl_{ttl}'] = ExpiringDict(TtlSingleton.__MAX_BUFFER_SIZE, ttl)

        dct['_ttl'] = ttl
        return super().__new__(cls, name, bases, dct, **kwargs)

    def __call__(cls, *args, **kwargs):
        cache = TtlSingleton.__ttl_cache.get(f'ttl_{cls._ttl}')
        if cache is None:
            raise ValueError(f'TTL value is not assigned: {cls._ttl}')
        cls._cache = cache
        return super().__call__(*args, **kwargs)
