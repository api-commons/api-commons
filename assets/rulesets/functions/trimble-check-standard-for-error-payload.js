export default (input) => {
  // Regex to match HTTP error status codes (4xx and 5xx)
  var errorStatusRegex = /^(4|5)\d{2}$/;
  
  // RFC3986 URI validation regex (more permissive than the previous one)
  const uriRegex = /^[a-zA-Z][a-zA-Z0-9+.-]*:.*$/;
  
  // Ensure input is an object and has properties
  if (!input || typeof input !== 'object') {
    return null;
  }
  
  for (let response in input) {
    var isErrorResponse = errorStatusRegex.test(response);
    
    if (isErrorResponse) {
      // Check if content block exists
      if (!input[response]["content"]) {
        return [
          {
            message: "Content block is missing in the error response body",
          },
        ];
      }
      
      // Check if application/json content type exists
      if (!input[response]["content"]["application/json"]) {
        return [
          {
            message: "All API error responses should return structured data in application/json format",
          },
        ];
      }
      
      // Check if schema exists
      if (!input[response]["content"]["application/json"]["schema"]) {
        return [
          {
            message: "Schema section is missing in the error response body",
          },
        ];
      }
      
      const schema = input[response]["content"]["application/json"]["schema"];
      
      // Check if schema is an object
      if (schema.type !== "object") {
        return [
          {
            message: "Error response schema must be of type 'object'",
          },
        ];
      }
      
      // Check if properties exist
      if (!schema.properties) {
        return [
          {
            message: "Properties section is missing in the error response schema",
          },
        ];
      }
      
      const properties = schema.properties;
      
      // Check required properties: type and title
      if (!properties.type) {
        return [
          {
            message: "The error payload must contain 'type' property",
          },
        ];
      }
      
      if (!properties.title) {
        return [
          {
            message: "The error payload must contain 'title' property",
          },
        ];
      }
      
      // Validate type property
      if (properties.type.type !== "string") {
        return [
          {
            message: "The 'type' property must be of type 'string'",
          },
        ];
      }
      
      if (properties.type.format && properties.type.format !== "uri") {
        return [
          {
            message: "The 'type' property format must be 'uri'",
          },
        ];
      }
      
      // Validate title property
      if (properties.title.type !== "string") {
        return [
          {
            message: "The 'title' property must be of type 'string'",
          },
        ];
      }
      
      // Validate optional properties if they exist
      if (properties.status) {
        if (properties.status.type !== "number") {
          return [
            {
              message: "The 'status' property must be of type 'number'",
            },
          ];
        }
      }
      
      if (properties.instance) {
        if (properties.instance.type !== "string") {
          return [
            {
              message: "The 'instance' property must be of type 'string'",
            },
          ];
        }
        if (properties.instance.format && properties.instance.format !== "uri") {
          return [
            {
              message: "The 'instance' property format must be 'uri'",
            },
          ];
        }
      }
      
      if (properties.detail) {
        if (properties.detail.type !== "string") {
          return [
            {
              message: "The 'detail' property must be of type 'string'",
            },
          ];
        }
      }
      
      if (properties.errors) {
        if (properties.errors.type !== "array") {
          return [
            {
              message: "The 'errors' property must be of type 'array'",
            },
          ];
        }
      }
    }
  }
  
  // Return undefined if all validations pass
  return undefined;
};
