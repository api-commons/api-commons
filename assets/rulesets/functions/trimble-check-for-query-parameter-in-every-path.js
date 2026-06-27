export default (input) => {
  const pattern = /\?([^=]+=[^&]+)(&[a-zA-Z0-9]{0,}=.*)?/g;
  const matches = input.match(pattern);

  if (matches) {
    return [
      {
        message:
          "Query parameters should not be used in the path. Provide the query params under the Parameters block as in : query.",
      },
    ];
  }
};
