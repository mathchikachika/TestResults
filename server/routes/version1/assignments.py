import math

from fastapi import APIRouter, Depends, HTTPException, Request, status

from server.authentication.jwt_bearer import JWTBearer

router = APIRouter()


@router.post(
    "/create",
    dependencies=[Depends(JWTBearer(access_level="teacher"))],
    status_code=status.HTTP_200_OK,
)
async def create_new_assignment(new_assigment: None, request: Request):
    teacher_id = request.state.user_details["uuid"]
    created_assignment = None
    return {
        "detail": "Successfully Created Assignment",
        "created_assignment": created_assignment,
    }


@router.post(
    "/answer/{assignment_uuid}",
    dependencies=[Depends(JWTBearer(access_level="student"))],
    status_code=status.HTTP_200_OK,
)
async def answer_assignment(
    assignment_uuid: str, student_assignment_response: None, request: Request
):
    student_id = request.state.user_details["uuid"]
    assignment_response = None
    return {
        "detail": "Successfully Recorded Response",
        "assignment_response": assignment_response,
    }


@router.get(
    "/class/{class_uuid}/all_assignments",
    dependencies=[Depends(JWTBearer(access_level="teacher"))],
    status_code=status.HTTP_200_OK,
)
async def get_all_assignments_by_class(
    class_uuid: str, page_num: int = 1, page_size: int = 10
):
    assignments = None

    response = {
        "data": assignments[1],
        "count": len(assignments[1]),
        "total": assignments[0][0],
        "page": page_num,
        "no_of_pages": math.ceil(assignments[0][0] / page_size),
    }

    return response


@router.get(
    "/specific/{assignment_uuid}",
    dependencies=[Depends(JWTBearer(access_level="teacher"))],
    status_code=status.HTTP_200_OK,
)
async def get_specific_assignment_by_id(assignment_uuid: str):
    assignment = None
    return {"Assignment": assignment}


@router.put(
    "/update/{assignment_uuid}",
    dependencies=[Depends(JWTBearer(access_level="teacher"))],
    status_code=status.HTTP_200_OK,
)
async def update_assignment_details(assignment_uuid: str, new_assignment_data: None):
    # print(new_assignment_data)
    assignment = None
    return {"detail": "Successfully updated list", "updated_assignment": assignment}


@router.patch(
    "/open_assignment/{assignment_uuid}",
    dependencies=[Depends(JWTBearer(access_level="teacher"))],
    status_code=status.HTTP_200_OK,
)
async def open_assignment_to_students(assignment_uuid: str, list_of_students: None):
    assignment = None
    return {
        "detail": "Successfully updated list",
        "assignment_open_to_students": assignment,
    }


@router.delete(
    "/delete/{assignment_uuid}",
    dependencies=[Depends(JWTBearer(access_level="teacher"))],
    status_code=status.HTTP_200_OK,
)
async def delete_assignment_by_id(assignment_uuid: str):
    assignment = None
    return {"detail": "Successfully deleted assignment"}


# @router.get("/teacher/all_assignments", dependencies=[Depends(JWTBearer(access_level='teacher'))], status_code=status.HTTP_200_OK)
# async def create_new_class(request: Request):
#     teacher_id = request.state.user_details['uuid']
#     created_assignment = assignment_controller.create_new_assignment(
#         connection.engine, teacher_id, new_class)
#     return {"detail": "Successfully Created Assignment", "created_assignment": created_assignment}

# @router.get("/student/all_assignments", dependencies=[Depends(JWTBearer(access_level='student'))], status_code=status.HTTP_200_OK)
# async def create_new_class(request: Request):
#     student_id = request.state.user_details['uuid']
#     created_assignment = assignment_controller.create_new_assignment(
#         connection.engine, teacher_id, new_class)
#     return {"detail": "Successfully Created Assignment", "created_assignment": created_assignment}
