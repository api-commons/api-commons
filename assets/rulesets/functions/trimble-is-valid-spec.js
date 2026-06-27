export default (input) => {
  if (JSON.stringify(input) === "{}") {
    return [
      {
        message: "The Open API Spec file must not be empty",
      },
    ];
  } else if (input==null) {
    return [
      {
        message: "The Open API Spec file must not be empty",
      },
    ];
  }
};