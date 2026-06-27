export default (input) => {
    var re =
      /^(100|101|102|103|200|201|202|203|204|205|206|207|208|226|300|301|302|303|304|305|307|308|400|401|402|403|404|405|406|407|408|409|410|411|412|413|414|415|416|417|418|421|422|423|424|425|426|428|429|431|451|500|501|502|503|504|505|506|507|508|510|511)$/;
    var valid = re.test(input);
  
    if (!valid) {
      return [
        {
          message: "All APIs should return a valid http response code." + input + " is not a valid HTTP response code",
        },
      ];
    }
  };

