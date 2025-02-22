from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from db.models.base_model import Base
import uuid
from typing import List
from db.models.relationship_model import (relationship_check_list_table,
                                          relationship_test_case_table,
                                          relationship_test_run)


class TestSuiteOrm(Base):
    __tablename__ = "test_suite"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"),
                                                 nullable=False,
                                                 index=True)
    author: Mapped['UserOrm'] = relationship()
    change_from: Mapped[uuid.UUID] = mapped_column(nullable=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"),
                                            nullable=False,
                                            index=True)
    project: Mapped['ProjectOrm'] = relationship(back_populates="test_suites")
    test_runs: Mapped[List['TestRunOrm'] | None] = relationship(back_populates="test_suite",
                                                                secondary=relationship_test_run)
    test_cases: Mapped[List['TestCaseOrm'] | None] = relationship(back_populates="test_suites",
                                                                  secondary=relationship_test_case_table)
    check_lists: Mapped[List['CheckListOrm'] | None] = relationship(back_populates="test_suites",
                                                                    secondary=relationship_check_list_table)
