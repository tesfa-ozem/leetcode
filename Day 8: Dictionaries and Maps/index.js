const { readFileSync, promises: fsPromises } = require("fs");

async function processData() {
  //Enter your code here
  try {
    const input = await fsPromises.readFile("./data.txt", "utf-8");

    let a = input.split(/\r?\n/).map((i) => i.split(" "));
    let arrayCount = a.shift()
    arrayCount = parseInt(arrayCount[0])
    let phoneBook = a.slice(0, arrayCount);
    let searchNames = a.slice(arrayCount+1);
    
    var sortedPhoneBook = phoneBook.sort((a, b) => {
      if (a[0] < b[0]) {
        return -1;
      } else if (a[0] > b[0]) {
        return 1;
      }
    });
    console.log(a)
    // for (let index = 0; index < searchNames.length; index++) {
    //   let search = searchNames[index][0]
    //   let start = 0;
    //   let middle = 0;
    //   let phoneBookLen = arrayCount;
    //   while (start <= phoneBookLen) {
    //     middle = start+Math.floor((phoneBookLen - start) / 2);
        
    //     if (search == sortedPhoneBook[middle][0]) {
    //       console.log(`${sortedPhoneBook[middle][0]}=${sortedPhoneBook[middle][1]}`);
    //       break;
    //     } else if (search > sortedPhoneBook[middle][0]) {
    //       start = middle + 1;
    //     } else if (search < sortedPhoneBook[middle][0]) {
    //       phoneBookLen = middle - 1;
    //     }else{
    //       console.log("Not Found")
    //       break;
    //     }
    //   }
      
      
    // }
    
  } catch (error) {
    console.log(error);
  }
}

processData("mpsrcmrkon");
