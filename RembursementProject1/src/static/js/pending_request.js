// The async keyword is added to a functions to tell them to return a promise rather than
// a value. The await keyword can only be used with an async function.

// async function get_characters(){
//   let xhr = new XMLHttpRequest() // ready state 0
//   let url = 'http://127.0.0.1:5000/Pending_Table'
  
//   xhr.onreadystatechange = async function(){
  
//       if(xhr.readyState === 4 && xhr.status === 200){
//           let characters = await JSON.parse(xhr.response)
      
//           let dropdown = document.getElementById('reimbursementTable')

//           console.log(characters) // not the characters you want

//           for(let character in characters){
//             console.log(character)
//             let table_row = document.createElement('tr')
//             for (let x in characters[character]){
//               let option = document.createElement('td')
//               option.innerText = characters[character][x]
//               table_row.append(option)
//               console.log(x)
//             }
//             dropdown.append(table_row)
//       }
//   }
//   }
//   xhr.open('GET', url)
//   xhr.send()
// }

let approved = document.getElementById('approved')
let denied = document.getElementById('denied')
let pending = document.getElementById('pending')
let all = document.getElementById('all')
let clearB = document.getElementById('clear')

async function approvalTable(){
    clearALL()
    let uri = 'http://127.0.0.1:5000/Approved_Table'
    let response = await fetch(uri)
    let characters = await response.json()
    let dropdown = document.getElementById('reimbursementTable')
        for(let character in characters){
            let table_row = document.createElement('tr')
            for (let x in characters[character]){
              if (x === "_economy"){
                console.log(characters[character][x])
                let option = document.createElement('td')
                option.innerText = characters[character][x]
                option.innerText = ("$" + option.innerText)
                // t = (new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(option.innerText))
                table_row.append(option)
                dropdown.append(table_row)
              }
              
              else{
                let option = document.createElement('td')
                option.innerText = characters[character][x]
                table_row.append(option)
                dropdown.append(table_row)
                }
              
            }
            dropdown.append(table_row)
          }
}


async function pendingTable(){
  clearALL()
  let uri = 'http://127.0.0.1:5000/Pending_Table'
  let response = await fetch(uri)
  let characters = await response.json()
  let dropdown = document.getElementById('reimbursementTable')
    console.log(characters) // not the characters you want
    for(let character in characters){
      let table_row = document.createElement('tr')
      for (let x in characters[character]){
        if (x === "_economy"){
          console.log(characters[character][x])
          let option = document.createElement('td')
          option.innerText = characters[character][x]
          option.innerText = ("$" + option.innerText)
          // t = (new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(option.innerText))
          table_row.append(option)
          dropdown.append(table_row)
        }
        
        else{
          let option = document.createElement('td')
          option.innerText = characters[character][x]
          table_row.append(option)
          dropdown.append(table_row)
          }
        
      }
      dropdown.append(table_row)
    }
}

async function deniedTable(){
  clearALL()
  let uri = 'http://127.0.0.1:5000/Denied_Table'
  let response = await fetch(uri)
  let characters = await response.json()
  let dropdown = document.getElementById('reimbursementTable')
  for(let character in characters){
    let table_row = document.createElement('tr')
    for (let x in characters[character]){
      if (x === "_economy"){
        console.log(characters[character][x])
        let option = document.createElement('td')
        option.innerText = characters[character][x]
        option.innerText = ("$" + option.innerText)
        // t = (new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(option.innerText))
        table_row.append(option)
        dropdown.append(table_row)
      }
      
      else{
        let option = document.createElement('td')
        option.innerText = characters[character][x]
        table_row.append(option)
        dropdown.append(table_row)
        }
      
    }
    dropdown.append(table_row)
  }
}

async function AllTable(){
  clearALL()
  let uri = 'http://127.0.0.1:5000/All_Reimbursements_Table'
  let response = await fetch(uri)
  let characters = await response.json()
  let dropdown = document.getElementById('reimbursementTable')
    for(let character in characters){
      let table_row = document.createElement('tr')
      for (let x in characters[character]){
        if (x === "_economy"){
          console.log(characters[character][x])
          let option = document.createElement('td')
          option.innerText = characters[character][x]
          option.innerText = ("$" + option.innerText)
          // t = (new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(option.innerText))
          table_row.append(option)
          dropdown.append(table_row)
        }
        
        else{
          let option = document.createElement('td')
          option.innerText = characters[character][x]
          table_row.append(option)
          dropdown.append(table_row)
          }
      }
    }
}

approved.addEventListener('click', approvalTable)
all.addEventListener('click', AllTable)
denied.addEventListener('click', deniedTable)
pending.addEventListener('click', pendingTable)

function clearALL(){
  let dropdown = document.getElementById('reimbursementTable')
  for(var i = dropdown.rows.length - 1; i > 0; i--)
  {
    dropdown.deleteRow(i);
  }
}

clearB.addEventListener('click', clearALL)

function disableappA(){
  approved.disabled = true;
  all.disabled = false;
  pending.disabled = false;
  denied.disabled = false;
}

function disableappALL(){
  approved.disabled = false;
  all.disabled = true;
  pending.disabled = false;
  denied.disabled = false;
}

function disableappP(){
  approved.disabled = false;
  all.disabled = false;
  pending.disabled= true;
  denied.disabled = false;
}

function disableappD(){
  approved.disabled = false;
  all.disabled = false;
  pending.disabled = false;
  denied.disabled = true;
}
// The window object has an onload property that we can use to 
// perform operations as soon as the window loads:

// Please note for immediately firing off functions, you can use
// IIFE (immediately Invoke function expression). They also help avoid
// cluttering the global namespace.


// async function approvallist(){
//   clearALL()
//   let uri = 'http://127.0.0.1:5000/Pending_Table'
//   let response = await fetch(uri)
//   let characters = await response.json()
//   let dropdown = document.getElementById('statusTable')
//     console.log(characters) // not the characters you want
//     for(let character in characters){
//       let table_row = document.createElement('tr')
//       for (let x in characters[character]){
//         if (x === "_economy"){
//           console.log(characters[character][x])
//           let option = document.createElement('td')
//           option.innerText = characters[character][x]
//           option.innerText = ("$" + option.innerText)
//           // t = (new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(option.innerText))
//           table_row.append(option)
//           dropdown.append(table_row)
//         }
        
//         else{
//           let option = document.createElement('td')
//           option.innerText = characters[character][x]
//           table_row.append(option)
//           dropdown.append(table_row)
//           }
        
//       }
//       dropdown.append(table_row)
//     }
// }

// window.onload = function(){
//   this.approvalTable()
// }