export default (input) => {

    const httpVerbs = ['get', 'post', 'put', 'delete', 'patch', 'trace', 'options', 'head', 'connect', 'parameters'];

    if (!httpVerbs.includes(input.toLowerCase())) {
        return [{
            message : `${input} is not a valid HTTP verb.`
        }]
      } 
    
}
