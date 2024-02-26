from typing import List

from fastapi import APIRouter, HTTPException, Depends

import services
from auth.database import async_session_maker, get_async_session
from entities.test_case_entities import TestCase, TestCaseRequest
from services import test_cases_service

test_cases_router = APIRouter(
    tags=["test-cases"],
    prefix="/test-cases"
)


@test_cases_router.get("/", response_model=List[TestCase])
def get_test_cases(skip: int = 0, limit: int = 50,
                   db: async_session_maker = Depends(get_async_session)):
    test_cases = services.test_cases_service.get_test_cases(skip=skip,
                                                            limit=limit,
                                                            db=db)
    return test_cases


@test_cases_router.get("/{id}", response_model=TestCase)
def get_one_test_case(id: int, db: async_session_maker = Depends(get_async_session)):
    one = services.test_cases_service.get_one_test_case(id=id, db=db)
    if not one:
        raise HTTPException(detail=f"test case with id {id} not found",
                            status_code=404)
    return one


@test_cases_router.post("/", response_model=TestCase)
def create_test_case(new_case: TestCaseRequest, db: async_session_maker = Depends(get_async_session)):
    new_one = services.test_cases_service.create_test_case(new_case=new_case,
                                                           db=db)
    return new_one


@test_cases_router.put("/{id}", response_model=TestCase)
def update_test_case(id: int, new_item: TestCaseRequest,
                     db: async_session_maker = Depends(get_async_session)):
    new_one = services.test_cases_service.update_test_case(id=id,
                                                           new_item=new_item,
                                                           db=db)
    if not new_one:
        raise HTTPException(detail=f"test case with id {id} not found",
                            status_code=404)
    return new_one


@test_cases_router.delete("/{id}")
def delete_test_case(id: int, db: async_session_maker = Depends(get_async_session)):
    services.test_cases_service.delete_test_case(id=id, db=db)
