from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from db.models.base_model import Base
from uuid import UUID


class BugOrm(Base):
    __tablename__ = "bug"
    __allow_unmapped__ = True
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    importance: Mapped[str] = mapped_column(nullable=False)
    finder_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"),
                                            nullable=False,
                                            index=True)
    finder: Mapped['UserOrm'] = relationship()
    test_case_execution_id: Mapped[int] | None = mapped_column(ForeignKey("test_case_execution.id"),
                                                               index=True)
    test_case_execution: Mapped['TestExecutionOrm'] | None = relationship()
    check_list_execution_id: Mapped[int] | None = mapped_column(ForeignKey("check_list_execution.id"),
                                                                index=True)
    check_list: Mapped['ListExecutionOrm'] | None = relationship()
    test_run_id: Mapped[int] = mapped_column(ForeignKey("test_run.id"),
                                             nullable=False,
                                             index=True)
    test_run: Mapped['TestRunOrm'] = relationship(back_populates="bugs")
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"),
                                            nullable=False,
                                            index=True)
    project: Mapped['ProjectOrm'] = relationship(back_populates="bugs")
