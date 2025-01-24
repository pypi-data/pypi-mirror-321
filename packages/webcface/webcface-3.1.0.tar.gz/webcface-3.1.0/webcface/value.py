from typing import Optional, List, Callable, SupportsFloat, Union
import webcface.field
import webcface.member
import webcface.message
from webcface.typing import convertible_to_float


class Value:
    _base: "webcface.field.Field"

    def __init__(self, base: "webcface.field.Field", field: str = "") -> None:
        """Valueを指すクラス

        このコンストラクタを直接使わず、
        Member.value(), Member.values(), Member.onValueEntry などを使うこと

        詳細は `Valueのドキュメント <https://na-trium-144.github.io/webcface/md_10__value.html>`_ を参照
        """
        self._base = webcface.field.Field(
            base._data, base._member, field if field != "" else base._field
        )

    @property
    def member(self) -> "webcface.member.Member":
        """Memberを返す"""
        return webcface.member.Member(self._base)

    @property
    def name(self) -> str:
        """field名を返す"""
        return self._base._field

    def on_change(self, func: Callable) -> Callable:
        """値が変化したときのイベント
        (ver2.0〜)

        コールバックの引数にはValueオブジェクトが渡される。

        まだ値をリクエストされてなければ自動でリクエストされる
        """
        self.request()
        data = self._base._data_check()
        if self._base._member not in data.on_value_change:
            data.on_value_change[self._base._member] = {}
        data.on_value_change[self._base._member][self._base._field] = func
        return func

    def child(self, field: str) -> "Value":
        """「(thisの名前).(追加の名前)」を新しい名前とするValue"""
        return Value(self._base.child(field))

    def request(self) -> None:
        """値の受信をリクエストする"""
        req = self._base._data_check().value_store.add_req(
            self._base._member, self._base._field
        )
        if req > 0:
            self._base._data_check().queue_msg_req(
                [
                    webcface.message.ValueReq.new(
                        self._base._member, self._base._field, req
                    )
                ]
            )

    def try_get_vec(self) -> Optional[List[float]]:
        """値をlistまたはNoneで返す、まだリクエストされてなければ自動でリクエストされる"""
        self.request()
        return self._base._data_check().value_store.get_recv(
            self._base._member, self._base._field
        )

    def try_get(self) -> Optional[float]:
        """値をfloatまたはNoneで返す、まだリクエストされてなければ自動でリクエストされる"""
        v = self.try_get_vec()
        return v[0] if v is not None else None

    def get_vec(self) -> List[float]:
        """値をlistで返す、まだリクエストされてなければ自動でリクエストされる"""
        v = self.try_get_vec()
        return v if v is not None else []

    def get(self) -> float:
        """値をfloatで返す、まだリクエストされてなければ自動でリクエストされる"""
        v = self.try_get()
        return v if v is not None else 0

    def exists(self) -> bool:
        """このフィールドにデータが存在すればtrue
        (ver2.0〜)

        try_get() などとは違って、実際のデータを受信しない。
        リクエストもしない。
        """
        return self._base._field in self._base._data_check().value_store.get_entry(
            self._base._member
        )

    def __str__(self) -> str:
        """printしたときなど

        <member("...").value("...") = ...> のように表示する
        """
        return f'<member("{self.member.name}").value("{self.name}") = {self.try_get_vec()}>'

    def set(self, data: Union[List[SupportsFloat], SupportsFloat]) -> "Value":
        """値をセットする"""
        self._base._set_check()
        if convertible_to_float(data):
            self._base._set_check().value_store.set_send(
                self._base._field, [float(data)]
            )
        elif isinstance(data, list):
            self._base._set_check().value_store.set_send(
                self._base._field, [float(v) for v in data]
            )
        else:
            raise TypeError("unsupported data type for value.set(): " + str(data))
        on_change = (
            self._base._data_check()
            .on_value_change.get(self._base._member, {})
            .get(self._base._field)
        )
        if on_change is not None:
            on_change(self)
        return self
