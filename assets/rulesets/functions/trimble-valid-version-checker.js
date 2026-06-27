export default (input) => {
  for (let index in input) {
    let url = input[index]["url"];
    var re = /(.*)(\/v[1-9]{1}[0-9]{0,14}(-dev|-qa|-stage)?(\/)?)/;
    var validVersion = re.test(url);

    if (!validVersion)
      return [
        {
          message:
            "All API URLs MUST include the major version and MUST NOT include the minor version.",
        },
      ];
  }
};
