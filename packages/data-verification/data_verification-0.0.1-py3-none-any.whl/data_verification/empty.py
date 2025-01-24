class Empty:
    @staticmethod
    def is_empty(value) -> bool:
        """
        检查给定值是否为空。
        :param value: 要检查的值。
        :return:
        """
        if bool(value):
            return False
        else:
            return True

    @staticmethod
    def is_not_empty(value) -> bool:
        """
        检查给定值是否非空。
        :param value: 要检查的值。
        :return:
        """
        return bool(value)


class EmptyAsync(Empty):
    @staticmethod
    async def is_empty(value):
        return Empty.is_empty(value)

    @staticmethod
    async def is_not_empty(value):
        return Empty.is_not_empty(value)
