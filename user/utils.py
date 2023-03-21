from django.http import JsonResponse


def get_response(data=None, message="", status=200):
    if data is None:
        data = {}
    message_dict = {200: "Data Retrieved", 201: "Updated Successfully", 202: "Registered Successfully",
                    204: "Deleted Successfully", 405: "Method not allowed"}
    if message == "":
        message = message_dict.get(status)
    return JsonResponse({"data": data, "message": message, "status": status}, status=status)
