export default (input) => {
  var get_response = input["GET"] ? input["GET"] : input["get"];
  if (get_response) {
    var responses = get_response["responses"];
    if (!responses)
      return [
        {
          message: "Responses block missing in GET method.",
        },
      ];

    var response_for_200 = responses["200"];
    if (!response_for_200) {
      return [
        {
          message: "GET call must return a 200 response.",
        },
      ];
    }

    var content = response_for_200["content"];
    if (!content) {
      return [
        {
          message: "Content block missing in 200 response block of GET call.",
        },
      ];
    }

    if (!content["application/json"])
      return [
        {
          message:
            "All APIs that return structured data should be able to return that data formatted as JSON at a minimum and as the default.",
        },
      ];
  }
};
