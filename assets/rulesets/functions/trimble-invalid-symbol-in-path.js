export default (input) => {
  if (input === "/") {
    return;
  }

  const segments = input.split(/(?=\/)/);

  for (const segment in segments) {
    if (segments[segment] === "/" && segments[segment - 1] === "/") {
      return [
        {
          message: "The given path contains invalid symbols in it.",
        },
      ];
    } else if (segments[segment] === "/") {
      continue;
    } else if (
      !(
        /^\/[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]$/.test(segments[segment]) ||
        /^\/\{[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z]\}$/.test(segments[segment])
      )
    ) {
      return [
        {
          message: "The given path contains invalid symbols in it.",
        },
      ];
    }
  }
};
