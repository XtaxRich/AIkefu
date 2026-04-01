from __future__ import annotations

from dataclasses import dataclass, field

from .types import ExperienceRecord


@dataclass(slots=True)
class ExperienceStore:
    records: list[ExperienceRecord] = field(default_factory=list)

    def add(self, record: ExperienceRecord) -> None:
        self.records.append(record)

    def success_rate(self) -> float:
        if not self.records:
            return 0.0
        successes = sum(1 for record in self.records if record.success)
        return successes / len(self.records)
