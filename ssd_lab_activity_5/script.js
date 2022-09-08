document.getElementById("add").onclick = function () {
  document.getElementById("table").style.display = "block";
  var table = document.getElementById("table");
  var row = table.insertRow(-1);
  var rollcell = row.insertCell(0);
  var namecell = row.insertCell(1);
  rollcell.innerHTML = document.getElementById("rollno").value;
  namecell.innerHTML = document.getElementById("name").value;
  document.getElementById("rollno").value = "";
  document.getElementById("name").value = "";
  return;
};

document.getElementById("delete").onclick = function () {
  document.getElementById("table").style.display = "block";
  var table = document.getElementById("table");
  if (table.rows.length === 1) {
    return;
  }
  table.deleteRow(-1);

  return;
};
