let mnameNode = document.getElementById("managerName");
let usernameNode = document.getElementById("username");
let emailNode = document.getElementById("email");
let teamleadNode = document.getElementById("teamlead");
let passwordNode = document.getElementById("password");
let password2Node = document.getElementById("password2");
let erroruserNode = document.getElementById("erroruser");
let errorpassNode = document.getElementById("errorpass");
let submitBtn = document.getElementById("submit");
let members = document.getElementById("members");
let mem = "";

usernameNode.addEventListener("input", (event) => {
  event.preventDefault();
  if (!event.target.checkValidity()) {
    console.log("Not valid - ", usernameNode.value);
    erroruserNode.innerHTML = "Error, atleast one number and one uppercase";
  } else {
    erroruserNode.innerHTML = "";
  }
});

password2Node.addEventListener("blur", (event) => {
  event.preventDefault();
  if (passwordNode.value !== password2Node.value) {
    console.log("not matching - ", passwordNode.value, " and ", password2Node.value);
    errorpassNode.innerHTML = "Error, not matching";
  } else {
    errorpassNode.innerHTML = "";
  }
});

const print = () => {
  let mname = mnameNode.value;
  let email = emailNode.value;
  let username = usernameNode.value;
  let lead = teamleadNode.value;
  alert("Name:  " + mname + "\nEmail:  " + email + "\nUsername:  " + username + "\nTeam Lead:  " + lead + "\nTeam Members:  " + mem);
};

// submitBtn.addEventListener("click", print);

const prevent = () => {
  getmembers();
  print();
};

function dragStart(event) {
  event.dataTransfer.setData("Text", event.target.id);
}
function allowDrop(event) {
  event.preventDefault();
}
function drop(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("Text");
  event.target.appendChild(document.getElementById(data));
  // document.getElementById("demo").innerHTML = "The p element was dropped";
}

function getmembers() {
  const list = members.childNodes;
  for (const iterator of list) {
    mem += iterator.innerText + ", ";
  }
  console.log(mem);
}
