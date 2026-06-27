export default (input) => {
  var json = input;
  const pathsKeys = Object.keys(json);

  var pathParameters = pathsKeys.map((key) => {
    const matches = key.match(/\{(.*?)\}/g);
    if (matches) {
      return matches.map((match) => match.slice(1, -1));
    }
    return [];
  });

  pathParameters = pathParameters.map((list) =>
    list.map((item) => item.toLowerCase())
  );

  for (var [index, key] of pathsKeys.entries()) {
    const httpVerbs = Object.keys(json[key]);
    if (pathParameters[index].length !== 0) {
      for (const verb of httpVerbs) {
        // Get parameters from both path level and operation level
        const pathLevelParameters = json[key].parameters || [];
        const operationLevelParameters = json[key][verb].parameters || [];
        const allParameters = [...pathLevelParameters, ...operationLevelParameters];

        if (allParameters.length === 0) {
          return [
            {
              message:
                "The path does not contains parameters block for path parameters.",
            },
          ];
        } else {
          // Check for duplicate path parameters
          if (
            pathParameters[index].length !== new Set(pathParameters[index]).size
          ) {
            return [
              {
                message: "The path parameters has duplicate values.",
              },
            ];
          }

          // Check each path parameter
          for (var word in pathParameters[index]) {
            const pathParamName = pathParameters[index][word];
            
            // Check if the parameter with this name is actually a path parameter
            const hasPathParameter = allParameters.some((param) => {
              return (
                param.name.toLowerCase() === pathParamName &&
                param.in.toLowerCase() === "path"
              );
            });

            if (!hasPathParameter) {
              return [
                {
                  message:
                    `The path parameter '${pathParamName}' was not mentioned in the 'name' field of parameters block for '${verb}' request.`,

                },
              ];
            }
          }
        }
      }
    } else {
      for (const verb of httpVerbs) {
        // Get parameters from both path level and operation level
        const pathLevelParameters = json[key].parameters || [];
        const operationLevelParameters = json[key][verb].parameters || [];
        const allParameters = [...pathLevelParameters, ...operationLevelParameters];

        if (allParameters.length > 0) {
          const hasPathParameter = allParameters.some((param) => {
            return param.in === "path";
          });
          if (hasPathParameter) {
            return [
              {
                message: "No path parameters mentioned in the path.",
              },
            ];
          }
        }
      }
    }
  }
};
