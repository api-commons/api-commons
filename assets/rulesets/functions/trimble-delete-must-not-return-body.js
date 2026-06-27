export default (input) => {
  var delete_response = input["delete"];

  if (delete_response) {
    if (delete_response["responses"]) {
      var delete_response_204 = delete_response["responses"]["204"];

      if (delete_response_204) {
        var keys = Object.keys(delete_response_204);
        if (keys.some((item) => item.toLowerCase() === "content")) {
          return [
            {
              message: `Delete request must not have response body.`,
            },
          ];
        }
      }
    }
  }
};
