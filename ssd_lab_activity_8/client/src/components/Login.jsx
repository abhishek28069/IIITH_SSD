import React from "react";

export const Login = () => {
  const [rollNumber, setRollNumber] = React.useState();
  const [password, setPassword] = React.useState();
  const [role, setRole] = React.useState("ta");
  const signUp = async () => {
    var res = await fetch("http://localhost:5000/signup", {
      credentials: "include",
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ rollNumber: rollNumber, password: password, role: role }),
    });
    setRollNumber("");
    setPassword("");
    setRole("");
    if (res.status == 200) {
      sessionStorage.setItem("rollNumber", rollNumber);
    }
  };
  const login = async () => {
    var res = await fetch("http://localhost:5000/login", {
      credentials: "include",
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ rollNumber: rollNumber, password: password, role: role }),
    });
    setRollNumber("");
    setPassword("");
    setRole("");
    if (res.status == 200) {
      sessionStorage.setItem("rollNumber", rollNumber);
    }
  };
  return (
    <div className="center">
      <div className="login-container">
        <div>
          <label htmlFor="rollNumber">Roll Number</label>
          <input type="text" name="rollNumber" value={rollNumber} onChange={(e) => setRollNumber(e.target.value)} />
        </div>
        <div>
          <label htmlFor="password">Password</label>
          <input type="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </div>
        <div>
          <label htmlFor="role">Role</label>
          <select name="role" id="role" onChange={(e) => setRole(e.target.value)}>
            <option value="ta">TA</option>
            <option value="student">Student</option>
          </select>
        </div>
        <div>
          <button onClick={signUp}>Signup</button>
        </div>
        <div>
          <button onClick={login}>Login</button>
        </div>
      </div>
    </div>
  );
};
