var myArray = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];  
var dict = {};

async function longOperation(id, enableAwait) {
  const randomElement = myArray[Math.floor(Math.random() * myArray.length)];

  if (dict[randomElement] == null) {
    dict[randomElement] = 0;
  }
  if (enableAwait) {  
    dict[randomElement] = await dict[randomElement] + 1; 
  }
  else { 
    dict[randomElement] = dict[randomElement] + 1;
  }
  await new Promise(r => setTimeout(r, Math.random()));
  dict[randomElement] = dict[randomElement] - 1;
  console.log(id, dict);  
}

for (var i = 0; i < 10000; i ++) {
  longOperation(i, true);
}
console.log('done');

