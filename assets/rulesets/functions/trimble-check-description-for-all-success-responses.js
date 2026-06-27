export default (input) => {
  for (var key in input) {
    if (key.toLowerCase() === "get") {
      var responses = input[key]["responses"];

      if (responses) {
        if (
          responses["206"] &&
          responses["206"]["description"] !== "Partial Content"
        ) {
          return [
            {
              message:
                "Description for 206 get response must be 'Partial Content'.",
            },
          ];
        }

        if (responses["200"] && responses["200"]["description"] !== "OK") {
          return [
            {
              message: "Description for 200 get response must be 'OK'.",
            },
          ];
        }
      }
    } else if (key.toLowerCase() === "post" || key.toLowerCase() === "put") {
      var responses = input[key]["responses"];
      if (responses) {
        if (responses["200"] && responses["200"]["description"] !== "OK") {
          return [
            {
              message: "Description for 200 " + key + " response must be 'OK'.",
            },
          ];
        }

        if (responses["201"] && responses["201"]["description"] !== "Created") {
          return [
            {
              message:
                "Description for 201 " + key + " response must be 'Created'.",
            },
          ];
        }

        if (
          responses["202"] &&
          responses["202"]["description"] !== "Accepted"
        ) {
          return [
            {
              message:
                "Description for 202 " + key + " response must be 'Accepted'.",
            },
          ];
        }
      }
    } else if (key.toLowerCase() === "delete") {
      var responses = input[key]["responses"];
      if (responses) {
        if (
          responses["204"] &&
          responses["204"]["description"] !== "No Content"
        ) {
          return [
            {
              message:
                "Description for 204 delete response must be 'No Content'.",
            },
          ];
        }
      }
    } else if (key.toLowerCase() === "patch") {
      var responses = input[key]["responses"];
      if (responses) {
        if (responses["200"] && responses["200"]["description"] !== "OK") {
          return [
            {
              message: "Description for 200 patch response must be 'OK'.",
            },
          ];
        }
      }
    }
  }
};
