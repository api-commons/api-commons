export default (input) => {
  var responses = input;

  if (responses) {
    if (responses["400"] && responses["400"]["description"] !== "Bad Request") {
      return [
        {
          message: "Description for 400 response must be 'Bad Request'.",
        },
      ];
    } else if (
      responses["401"] &&
      responses["401"]["description"] !== "Unauthorized"
    ) {
      return [
        {
          message: "Description for 401 response must be 'Unauthorized'.",
        },
      ];
    } else if (
      responses["403"] &&
      responses["403"]["description"] !== "Forbidden"
    ) {
      return [
        {
          message: "Description for 403 response must be 'Forbidden'.",
        },
      ];
    } else if (
      responses["404"] &&
      responses["404"]["description"] !== "Not Found"
    ) {
      return [
        {
          message: "Description for 404 response must be 'Not Found'.",
        },
      ];
    } else if (
      responses["405"] &&
      responses["405"]["description"] !== "Method Not Allowed"
    ) {
      return [
        {
          message: "Description for 405 response must be 'Method Not Allowed'.",
        },
      ];
    } else if (
      responses["406"] &&
      responses["406"]["description"] !== "Not Acceptable"
    ) {
      return [
        {
          message: "Description for 406 response must be 'Not Acceptable'.",
        },
      ];
    } else if (
      responses["409"] &&
      responses["409"]["description"] !== "Conflict"
    ) {
      return [
        {
          message: "Description for 409 response must be 'Conflict'.",
        },
      ];
    } else if (
      responses["500"] &&
      responses["500"]["description"] !== "Internal Server Error"
    ) {
      return [
        {
          message:
            "Description for 500 response must be 'Internal Server Error'.",
        },
      ];
    } else if (
      responses["504"] &&
      responses["504"]["description"] !== "Gateway Timeout"
    ) {
      return [
        {
          message: "Description for 504 response must be 'Gateway Timeout'.",
        },
      ];
    }
  }
};
