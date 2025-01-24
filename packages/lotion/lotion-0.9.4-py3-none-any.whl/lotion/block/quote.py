from .block import Block
from .rich_text.rich_text import RichText


class Quote(Block):
    rich_text: RichText
    color: str

    def __init__(
        self,
        rich_text: RichText,
        color: str | None = None,
        id: str | None = None,
        archived: bool | None = None,
        created_time: str | None = None,
        last_edited_time: str | None = None,
        has_children: bool | None = None,
        parent: dict | None = None,
    ):
        super().__init__(
            id, archived, created_time, last_edited_time, has_children, parent
        )
        self.rich_text = rich_text
        self.color = color

    @staticmethod
    def of(block: dict) -> "Quote":
        quote = block["quote"]
        rich_text = RichText.from_entity(quote["rich_text"])
        return Quote(
            id=block["id"],
            archived=block["archived"],
            created_time=block["created_time"],
            last_edited_time=block["last_edited_time"],
            has_children=block["has_children"],
            parent=block["parent"],
            rich_text=rich_text,
            color=quote["color"],
        )

    @staticmethod
    def from_plain_text(text: str) -> "Quote":
        return Quote(rich_text=RichText.from_plain_text(text))

    @property
    def type(self) -> str:
        return "quote"

    def to_dict_sub(self) -> dict:
        result = {
            "rich_text": self.rich_text.to_dict(),
        }
        if self.color is not None:
            result["color"] = self.color
        return result

    def to_slack_text(self) -> str:
        return "> " + self.rich_text.to_slack_text()
