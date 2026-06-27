// POST operation must have either a 201 or a 202 status code.
export default (operation, _opts, paths) => {
  // We expect an operation object
  if (operation === null || typeof operation !== "object") {
    return [];
  }

  const path = paths.path || paths.target || [];
  const statusCodes = Object.keys(operation);
  const errors = [];
  if (!statusCodes.includes("201") && !statusCodes.includes("202")) {
    errors.push({
      message: `A 201 or 202 status code should be returned by a POST operation`,
      path: [...path, "responses"],
    });
  }

  return errors;
};
