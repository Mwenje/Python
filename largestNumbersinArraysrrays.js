function largestOfFour(arr) {
  for (let i = 0; i < arr.length; i++) {
    const element = arr[i];
    console.log(element);

    let largest = 0;
    for (let j = 0; j < arr.length; j++) {
      const element = arr[i][j];
      console.log(element);

      if (element > largest) {
        largest = element;
      }

      console.log(`The largest is ${largest}`);
    }
  }

  return arr;
}

largestOfFour([
  [4, 5, 1, 3],
  [13, 27, 18, 26],
  [32, 35, 37, 39],
  [1000, 1001, 857, 1],
]);
