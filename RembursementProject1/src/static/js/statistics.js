// The async keyword is added to a functions to tell them to return a promise rather than
// a value. The await keyword can only be used with an async function.

async function most_money_spent(){
    let xhr = new XMLHttpRequest() // ready state 0
    let url = 'http://127.0.0.1:5000/Most_Spent'
    
    xhr.onreadystatechange = async function(){
    
        if(xhr.readyState === 4 && xhr.status === 200){
            let characters = await JSON.parse(xhr.response)
            let dropdown = document.getElementById('economyTable')
  
  
            for(let character in characters){
              let table_row = document.createElement('tr')
              for (let x in characters[character]){
                if (x === "_economy"){
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
    }
    xhr.open('GET', url)
    xhr.send()
  }

  async function most_requested(){
    let xhr = new XMLHttpRequest() // ready state 0
    let url = 'http://127.0.0.1:5000/Most_Requested'
    
    xhr.onreadystatechange = async function(){
    
        if(xhr.readyState === 4 && xhr.status === 200){
            let characters = await JSON.parse(xhr.response)
        
            let dropdown = document.getElementById('requestTable')

            for(let character in characters){
              let table_row = document.createElement('tr')
              for (let x in characters[character]){
                let option = document.createElement('td')
                option.innerText = characters[character][x]
                table_row.append(option)
              }
              dropdown.append(table_row)
        }
    }
    }
    xhr.open('GET', url)
    xhr.send()
  }

  
  async function most_denied(){
    let xhr = new XMLHttpRequest() // ready state 0
    let url = 'http://127.0.0.1:5000/Most_Denied'
    
    xhr.onreadystatechange = async function(){
    
        if(xhr.readyState === 4 && xhr.status === 200){
            let characters = await JSON.parse(xhr.response)
        
            let dropdown = document.getElementById('deniedTable')
  
            for(let character in characters){
              let table_row = document.createElement('tr')
              for (let x in characters[character]){
                let option = document.createElement('td')
                option.innerText = characters[character][x]
                table_row.append(option)
              }
              dropdown.append(table_row)
        }
    }
    }
    xhr.open('GET', url)
    xhr.send()
  }

  async function gimmie_dat2 (){
    const response = await fetch('http://127.0.0.1:5000/Most_Denied')
    let characters = await response.json()
    
    function unpackArr (){
      names_full = []
    names_half = []
    names_comp = []
    last_name = []
    economyC = []
    
    
    for (const [key, value] of Object.entries(characters)) {
      names_full.push(value)
    }
    
    console.log(names_full)
    
    for (let i of names_full){
      names_comp.push(i['_reimbursements'])
      economyC.push(i['_first_name'])
      console.log(i['_reimbursements'])
    }
    }
    
    unpackArr();
    
    var ctx = document.getElementById('myChart2').getContext('2d');
    let  DATA_COUNT = [names_comp[0], names_comp[1], names_comp[2], names_comp[3]]
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: [economyC[0], economyC[1], economyC[2], economyC[3]],
            datasets: [{
                label: 'Requests Made',
                data: DATA_COUNT,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
                }]
        },
       
    });
    }


async function gimmie_dat1 (){
const response = await fetch('http://127.0.0.1:5000/Most_Requested')
let characters = await response.json()

function unpackArr (){
  names_full = []
names_half = []
names_comp = []
last_name = []
economyC = []


for (const [key, value] of Object.entries(characters)) {
  names_full.push(value)
}

console.log(names_full)

for (let i of names_full){
  names_comp.push(i['_reimbursements'])
  economyC.push(i['_first_name'])
  console.log(i['_reimbursements'])
}
}

unpackArr();

var ctx = document.getElementById('myChart1').getContext('2d');
let  DATA_COUNT = [names_comp[0], names_comp[1], names_comp[2], names_comp[3]]
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [economyC[0], economyC[1], economyC[2], economyC[3]],
        datasets: [{
            label: 'Requests Made',
            data: DATA_COUNT,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
            }]
    },
    options: {
      indexAxis: 'y',
      elements: {
        bar: {
          borderWidth: 2,
        }
      },
      scales: {
        x: {
          beginAtZero: true
        }
      }
    }
});
}

async function gimmie_dat (){
  const response = await fetch('http://127.0.0.1:5000/Most_Spent')
  let characters = await response.json()
  
  function unpackArr (){
    names_full = []
  names_half = []
  names_comp = []
  last_name = []
  economyC = []
  
  
  for (const [key, value] of Object.entries(characters)) {
    names_full.push(value)
  }
  
  console.log(names_full)
  
  for (let i of names_full){
    names_comp.push(i['_economy'])
    economyC.push(i['_first_name'])
  }
  }
  
  unpackArr();
  
  var ctx = document.getElementById('myChart').getContext('2d');
  var myChart = new Chart(ctx, {
      type: 'bar',
      data: {
          labels: [economyC[0], economyC[1], economyC[2], economyC[3]],
          datasets: [{
              label: 'Economy',
              data: [names_comp[0], names_comp[1], names_comp[2], names_comp[3]],
              backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 159, 64, 0.2)'
              ],
              borderColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(153, 102, 255, 1)',
                  'rgba(255, 159, 64, 1)'
              ],
              borderWidth: 1
          }]
      },
      options: {
          scales: {
              y: {
                  beginAtZero: false
              }
          }
      }
  });
  }

  // The window object has an onload property that we can use to 
  // perform operations as soon as the window loads:
  
  // Please note for immediately firing off functions, you can use
  // IIFE (immediately Invoke function expression). They also help avoid
  // cluttering the global namespace.
  window.onload = function(){
    this.most_money_spent()
    this.most_requested()
    this.most_denied()
    this.gimmie_dat()
    this.gimmie_dat1()
    this.gimmie_dat2()
  }