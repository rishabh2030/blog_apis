from authentication.models import User 
from rest_framework import status

#-------------------------- STATUS CODE ---------------------------

status200 = status.HTTP_200_OK
status201 = status.HTTP_201_CREATED
status202 = status.HTTP_202_ACCEPTED
status204 = status.HTTP_204_NO_CONTENT
status400 = status.HTTP_400_BAD_REQUEST
status401 = status.HTTP_401_UNAUTHORIZED
status403 = status.HTTP_403_FORBIDDEN
status404 = status.HTTP_404_NOT_FOUND


#-------------------------------------- CLASS USER FUNCTIONS ------------------------------------

class UserFunctions:
    def get_user(mobile):
        """
        To get or create user object by mobile number
        params mobile: mobile of user
        result: object
        """
        user_obj = User.objects.get(mobile=mobile)
        return user_obj

#-------------------------------------- CLASS RESPONSE HANDLING ------------------------------------

class ResponseHandling:
    def failure_response_message(detail,result):
        """
        error message for failure
        :param detail: message to show in detail
        :param result : message or result to show
        :returns: dictionary
        """
        return {'detail' : detail, 'result' : result}

    def success_response_message(detail,result):
        """
        success message for Success
        :param detail: message to show in detail
        :param result : message or result to show
        :returns: dictionary
        """
        return {'detail' : detail, 'result' : result}

#-------------------------------------- ERROR GENERAL FUNCTIONS ------------------------------------

def error_message_function(errors):
    """
    return error message when serializer is not valid
    :param errors: error object
    :returns: string
    """
    for key, values in errors.items():
        error = [value[:] for value in values]
        err = ' '.join(map(str,error))
        return err

