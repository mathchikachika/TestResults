import math

from fastapi import APIRouter, Depends, HTTPException, Request, status

from server.authentication.jwt_bearer import JWTBearer

router = APIRouter()


@router.post(
    "/create",
    dependencies=[Depends(JWTBearer(access_level="teacher"))],
    status_code=status.HTTP_200_OK,
)
async def create_new_class(new_class: None, request: Request):
    teacher_id = request.state.user_details["uuid"]
    created_class = None
    return {"detail": "Successfully Created Class", "new_class": created_class}


@router.get(
    "/student/fetch/all",
    dependencies=[Depends(JWTBearer(access_level="student"))],
    status_code=status.HTTP_200_OK,
)
async def get_all_classes_by_student(request: Request):
    student_id = request.state.user_details["uuid"]
    classes = None
    return {"classes": classes}


@router.get(
    "/teacher/fetch/all",
    dependencies=[Depends(JWTBearer(access_level="teacher"))],
    status_code=status.HTTP_200_OK,
)
async def get_all_classes_by_teacher(
    request: Request, page_num: int = 1, page_size: int = 10
):
    teacher_id = request.state.user_details["uuid"]
    classes = None

    response = {
        "data": classes[1],
        "count": len(classes[1]),
        "total": classes[0][0],
        "page": page_num,
        "no_of_pages": math.ceil(classes[0][0] / page_size),
    }
    return response


@router.get(
    "/teacher/fetch/{class_uuid}",
    dependencies=[Depends(JWTBearer(access_level="teacher"))],
    status_code=status.HTTP_200_OK,
)
async def get_specific_class_teacher(request: Request, class_uuid: str):
    teacher_id = request.state.user_details["uuid"]
    fetched_class = None
    return {"Class": fetched_class}


@router.get(
    "/student/fetch/{class_uuid}",
    dependencies=[Depends(JWTBearer(access_level="student"))],
    status_code=status.HTTP_200_OK,
)
async def get_specific_class_student(request: Request, class_uuid: str):
    fetched_class = None
    return {"Class": fetched_class}


@router.get(
    "/student/search/{class_code}",
    dependencies=[Depends(JWTBearer(access_level="student"))],
    status_code=status.HTTP_200_OK,
)
async def get_class_by_code(request: Request, class_code: str):
    fetched_class = None
    return {"Class": fetched_class}


@router.put(
    "/update/{class_uuid}",
    dependencies=[Depends(JWTBearer(access_level="teacher"))],
    status_code=status.HTTP_200_OK,
)
async def update_class(updated_class: None, request: Request, class_uuid: str):
    teacher_id = request.state.user_details["uuid"]
    new_updated_class = None
    return {"Detail": "Updated Successfully", "Class": new_updated_class}


@router.delete(
    "/delete/{class_uuid}",
    dependencies=[Depends(JWTBearer(access_level="teacher"))],
    status_code=status.HTTP_200_OK,
)
async def delete_question(request: Request, class_uuid: str):
    teacher_id = request.state.user_details["uuid"]
    deleted_class = None
    return {"Detail": "Successfully deleted"}


@router.patch(
    "/join/{class_code}",
    dependencies=[Depends(JWTBearer(access_level="student"))],
    status_code=status.HTTP_200_OK,
)
async def join_class(class_code: str, request: Request):
    student_id = request.state.user_details["uuid"]
    join_class = None
    return {"detail": "Successfully Join the class"}


@router.patch(
    "/accept/student/{class_uuid}/{student_id}",
    dependencies=[Depends(JWTBearer(access_level="teacher"))],
    status_code=status.HTTP_200_OK,
)
async def accept_student(request: Request, class_uuid: str, student_id: str):
    teacher_id = request.state.user_details["uuid"]
    deleted_class = None
    return {"Detail": "Successfully accepted student to the class"}


@router.delete(
    "/remove/student/{class_uuid}/{student_id}",
    dependencies=[Depends(JWTBearer(access_level="teacher"))],
    status_code=status.HTTP_200_OK,
)
async def remove_student(request: Request, class_uuid: str, student_id: str):
    teacher_id = request.state.user_details["uuid"]
    deleted_class = None
    return {"Detail": "Successfully removed student from the class"}
