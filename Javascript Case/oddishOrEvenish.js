function oddishOrEvenish(number) {
    var number =  number.toString();
    var sum_of_digits = 0;

    for (let i = 0; i < number.length; i++) {

        sum_of_digits += (parseInt(number[i]))

    }
    if (sum_of_digits % 2 == 1) {
        console.log('Odd')
    }else {
        console.log('Even')
    }
}

oddishOrEvenish(4433)