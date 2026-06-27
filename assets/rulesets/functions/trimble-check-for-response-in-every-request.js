export default (input) => {
  let keys = Object.keys(input)
  let extraFields = ['parameters', 'servers', 'summary', 'description', '$ref']
  let httpVerbs = keys.filter((verb) => !(extraFields.includes(verb)));
  for(let index = 0; index < httpVerbs.length; index++)
  {
    if (!input[httpVerbs[index]]["responses"]) {
    return [
      {
        message: "Response body missing for the given request.",
      },
    ];
  }
  }
};
