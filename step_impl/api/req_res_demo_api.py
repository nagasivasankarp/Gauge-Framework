from getgauge.python import step
from utilities.base_api import API

api = API()


@step("Create a User")
def create_a_user():
    try:
        post_response = api.api_request(method='POST',
                                        endpoint='api/users',
                                        json_object={"name": "morpheus", "job": "leader"})
        assert post_response.status_code is 201
    except Exception as e:
        raise AssertionError("Exception is ", e)


@step("Get the User List")
def get_the_user_list():
    try:
        get_response = api.api_request(method='GET',
                                       endpoint='api/users?page=2',
                                       json_object=None)
        assert get_response.status_code is 200
    except Exception as e:
        raise AssertionError("Exception is ", e)


@step("Update the User")
def update_the_user():
    try:
        update_response = api.api_request(method='PUT',
                                          endpoint='api/users/2',
                                          json_object={"name": "morpheus", "job": "Team Member"})
        assert update_response.status_code is 200

    except Exception as e:
        raise AssertionError("Exception is ", e)


@step("Delete the User")
def delete_the_user():
    try:
        delete_response = api.api_request(method='DELETE',
                                          endpoint='api/users?page=2',
                                          json_object=None)
        assert delete_response.status_code is 204
    except Exception as e:
        raise AssertionError("Exception is ", e)
