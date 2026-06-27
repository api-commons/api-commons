export default (input) => {
  var get_response = input["GET"] ? input["GET"] : input["get"];

  if (get_response) {
    var responses = get_response["responses"];
    if (responses) {
      var response_for_206 = responses["206"];

      if (response_for_206) {
        var headers = response_for_206["headers"];

        if (!headers) {
          return [
            {
              message:
                "Header block missing in the GET method 206 response code.",
            },
          ];
        }

        var keys = Object.keys(headers);

        if (
          !keys.some((item) => item.toLowerCase() === "content-type") ||
          !keys.some((item) => item.toLowerCase() === "content-range")
        ) {
          return [
            {
              message:
                "GET response code 206 should have Content-Type and Content-Range in the header.",
            },
          ];
        }
      }
    }
  }
};
