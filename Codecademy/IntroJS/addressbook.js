var bob = {
    firstName: "Bob",
    lastName: "Jones",
    phoneNumber: "(650) 777-7777",
    email: "bob.jones@example.com"
};

var mary = {
    firstName: "Mary",
    lastName: "Johnson",
    phoneNumber: "(650) 888-8888",
    email: "mary.johnson@example.com"
};

var contacts = [bob, mary];

function printPerson(person) {
    console.log(person.firstName + " " + person.lastName);
}

function list() {
	var contactsLength = contacts.length;
	for (var i = 0; i < contactsLength; i++) {
		printPerson(contacts[i]);
	}
}

/*Create a search function
then call it passing "Jones"*/
function search(lastName) {
    var c = contacts.length
    for(var n = 0; n < c; n++) {
        if(contacts[n].lastName == lastName) {
            printPerson(contacts[n])
        }
    }
}
function add(firstName, lastName, email, phoneNumber) {
    var contact = {
        firstName: firstName,
        lastName: lastName,
        email: email,
        phoneNumber: phoneNumber
    }
    contacts[contacts.length] = contact
}

add("Josh", "Snider", "josh.snider@redacted.com", "(555)123-4567")
list()
