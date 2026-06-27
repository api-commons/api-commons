export default (input) =>{
	var post_request = input['post'] ? input['post']: input['POST']
	var put_request = input['PUT'] ? input['PUT'] : input['put']
	var responses=[]
	responses.push(post_request)
	responses.push(put_request)
	for(let index= 0; index<responses.length; index++)
	{
		if (responses[index] && responses[index]['requestBody']){

			var content = responses[index]['requestBody']['content']
			if(!content)
				return [{
				message : "Content block missing in request body of " + (index ==0 ? "POST" : "PUT") +" call."
			}]

			var applicationOrJsonContent = content['application/json']
			if(!applicationOrJsonContent)
				return [{
				message : "All APIs that accept a body MUST accept that body formatted as JSON. APIs MAY accept bodies in other formats."
			}]
	} 

	}
}
