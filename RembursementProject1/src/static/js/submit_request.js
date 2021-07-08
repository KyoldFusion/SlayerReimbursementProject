
async function get_characters(){

    let url = 'http://127.0.0.1:5000/valid_managers'
    // let url = 'http://hp-api.herokuapp.com/api/characters'
    let response = await fetch(url)
    // Remember that fetch returns the response objectj, not the direct response body
    let characters = await response.json()
    // console.log(characters)
    let dropdown = document.getElementById('manager_id')
    // let option = document.createElement('option')

    for(let character of characters['employee_id']){
        let option = document.createElement('option')
        option.innerText = character
        dropdown.append(option)
    }

    // for (let x of characters['employee_id']){
    //     console.log(x)
    //     option.innerText = x
    //     console.log(option.innerText)
    //     dropdown.append(option)
    // }

}

window.onload = function(){
    this.get_characters()
}