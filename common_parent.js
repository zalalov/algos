/*

    1
  2   3
 4 5   6
7

*/

var root = {
  value: 1,
  left: {
    value: 2,
    left: {
      value: 4,
      left: {
        value: 7
      }
    },
    right: {
      value: 5
    }
  },
  right: {
    value: 3,
    right: {
      value: 6
    }
  }
}

function findLCA(root, n1, n2) {
  let result = [false, false];
  
  if (root.value === n1) {
    result[0] = true;
  }else if (root.value === n2) {
    result[1] = true;
  }
  
  if (root.left) {
    left = findLCA(root.left, n1, n2);
    
    if (typeof(left) == 'number') {
      return left;
    } else {
      result = [result[0] || left[0], result[1] || left[1]];
    }
  }
  
  if (root.right) {
    right = findLCA(root.right, n1, n2);
    
    if (typeof(right) == 'number') {
      return right;
    } else {
      result = [result[0] || right[0], result[1] || right[1]];
    }
  }
  
  if (result[0] && result[1]) {
    return root.value;
  }
  
  return result;
}

findLCA(root, 1, 5);
