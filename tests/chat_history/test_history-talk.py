import json

import pytest

from lib.history.base import ChatHistory
from lib.history.storage.memory import ChatHistoryMemoryStorage


@pytest.fixture
def history():
    with open("./tests/data/saru.json", "r") as f:
        data = json.load(f)

    memory_history = ChatHistoryMemoryStorage("123", "key")
    memory_history.restore(data)
    history = ChatHistory(memory_history)
    return history


def test_username(history):
    md = history.md({"user": "小学生", "assistant": "説明員", "system": "---"})
    res = "\n".join(
        [
            "",
            "## 小学生",
            "",
            "ニホンザルの生態を教えて",
            "",
            "## 説明員",
            "",
            "ニホンザルは、日本に生息する唯一の霊長類です。体長は約50～70cm、体重は約8～18kgで、オスの方がメスよりも大きくなります。毛色は黒褐色で、顔は赤い色をしています。ニホンザルは群れを成して生活し、群れの規模は数頭から数百頭にもなります。群れのリーダーはオスで、群れのメンバーを守り、争いを仲裁します。ニホンザルは雑食性で、果物、昆虫、木の芽、葉っぱ、魚、貝など、様々なものを食べます。ニホンザルは知能が高い動物で、道具を使うことも知られています。例えば、石を水で冷やして食べ物を食べたり、竹を割って穴を掘って水を飲んだりしています。ニホンザルはまた、鏡に映った自分自身を認識する能力も持っています。ニホンザルは、日本各地の山や森に生息しています。しかし、近年は生息地の減少や、開発による捕獲などにより、個体数は減少しています。ニホンザルは、日本の天然記念物に指定されており、国や地方自治体は、ニホンザルの生息地の保護や、ニホンザルに関する教育活動を行っています。ニホンザルは、私たちの祖先であるヒトに非常に近い動物です。ニホンザルの行動や生態を研究することで、ヒトの進化や脳の働きについて、多くのことを知ることができます。ニホンザルは、私たちにとって貴重な動物であり、その保護は重要です。",
            "",
        ]
    )

    assert md == res
