async function postFormDataAsJson({ url, formData }) {
	const plainFormData = Object.fromEntries(formData.entries());
	const formDataJsonString = JSON.stringify(plainFormData);

	const fetchOptions = {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			"Accept": "application/json"
		},
		/**
		 * The body of our POST request is the JSON string that
		 * we created above.
		 */
		body: formDataJsonString,
	};

	const response = await fetch(url, fetchOptions);

	if (!response.ok) {
		const errorMessage = await response.text();
		throw new Error(errorMessage);
	}

	return response.json();
}

function checkEmpty (jsonOb){
    return Object.keys(jsonOb).length===0
}

async function handleFormSubmit(event) {
	event.preventDefault();

	const form = event.currentTarget;
    const url = form.action;

    const formData = new FormData(form);
    const responseData = await postFormDataAsJson({ url, formData})
    console.log(responseData)
    console.log(checkEmpty(responseData))
    if (checkEmpty(responseData)){
        x = document.getElementById('issue')
        x.style.visibility = "visible";
    }
    else{
        window.location.href = ('http://127.0.0.1:5000/index')
    }
}
const loginForm = document.getElementById("loginForm");
loginForm.addEventListener("submit", handleFormSubmit)