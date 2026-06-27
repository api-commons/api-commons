// Check operation summary and description to TDP conventions
// - Summary and description are required
// - Description is longer than summary
// -
export default (operation, _opts, paths) => {
  // We expect an operation object
  if (operation === null || typeof operation !== "object") {
    return [];
  }

  const path = paths.path || paths.target || [];

  // Declare errors return object
  const errors = [];

  const summary = operation.summary;
  const description = operation.description;

  if (summary && description) {
    // Summary and description should not be the same, case insensitive
    if (summary.toLowerCase() === description.toLowerCase()) {
      errors.push({
        message: "Summary and description should not match",
        path: [...path, "operation"],
      });
    } else if (summary.length >= description.length) {
      errors.push({
        message: "Description should be longer than summary",
        path: [...path, "operation"],
      });
    }
  }

  return errors;
};
